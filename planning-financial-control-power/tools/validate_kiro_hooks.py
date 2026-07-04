#!/usr/bin/env python3
"""Validate and optionally schedule Kiro v1 hook JSON files.

Usage:
  python tools/validate_kiro_hooks.py hooks/kiro-v1/pfc-workspace-hooks.json
  python tools/validate_kiro_hooks.py --run-hooks hooks/kiro-v1/*.json

Tier behavior:
- execution_tier=blocking: command hooks run synchronously when --run-hooks is used.
- execution_tier=async: command hooks are scheduled in a background thread that starts a detached subprocess; the validator does not wait for completion.

The schema tracks the public Kiro v1 hook shape plus PFC's required execution_tier.
"""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator  # type: ignore
except Exception as exc:  # pragma: no cover
    print("ERROR: jsonschema is required. Install with: pip install jsonschema", file=sys.stderr)
    raise SystemExit(2) from exc


ASYNC_EXECUTOR = ThreadPoolExecutor(max_workers=8, thread_name_prefix="pfc-hook-async")


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL: {path} is not valid JSON: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


def validate_file(path: Path, validator: Draft202012Validator) -> tuple[bool, dict[str, Any] | None]:
    data = load_json(path)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if errors:
        print(f"FAIL: {path} is invalid")
        for err in errors:
            loc = "/".join(str(p) for p in err.path) or "<root>"
            print(f"- {loc}: {err.message}")
        return False, data

    hooks = data.get("hooks", [])
    blocking = sum(1 for hook in hooks if hook.get("execution_tier") == "blocking")
    async_count = sum(1 for hook in hooks if hook.get("execution_tier") == "async")
    print(f"PASS: {path} is valid ({blocking} blocking hooks, {async_count} async hooks)")
    return True, data


def schedule_async_command(command: str, hook_name: str) -> None:
    """Start a detached command from a short-lived background thread.

    The thread only starts the process. It does not wait for the command to finish, so
    Tier 2 hooks do not block the caller's next semantic turn.
    """
    def _start() -> None:
        try:
            subprocess.Popen(  # noqa: S603 - hook command is user-authored workspace config
                shlex.split(command),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
            print(f"ASYNC_STARTED: {hook_name}: {command}")
        except Exception as exc:  # pragma: no cover
            print(f"ASYNC_FAILED_TO_START: {hook_name}: {exc}", file=sys.stderr)

    ASYNC_EXECUTOR.submit(_start)


def run_blocking_command(command: str, hook_name: str, timeout: int | None) -> bool:
    try:
        completed = subprocess.run(  # noqa: S603 - hook command is user-authored workspace config
            shlex.split(command),
            check=False,
            timeout=timeout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except subprocess.TimeoutExpired:
        print(f"BLOCKING_TIMEOUT: {hook_name}: timeout={timeout}", file=sys.stderr)
        return False

    if completed.stdout:
        print(completed.stdout, end="")
    if completed.stderr:
        print(completed.stderr, end="", file=sys.stderr)

    if completed.returncode != 0:
        print(f"BLOCKING_FAIL: {hook_name}: exit={completed.returncode}", file=sys.stderr)
        return False

    print(f"BLOCKING_PASS: {hook_name}")
    return True


def execute_hooks(data: dict[str, Any]) -> bool:
    """Execute command hooks according to execution_tier.

    Agent-prompt hooks are not executed by this utility; they are reported only because
    Kiro owns agent prompt execution.
    """
    ok = True
    for hook in data.get("hooks", []):
        if hook.get("enabled") is False:
            print(f"SKIP_DISABLED: {hook.get('name')}")
            continue

        name = hook.get("name", "<unnamed>")
        tier = hook.get("execution_tier")
        action = hook.get("action", {})
        action_type = action.get("type")

        if action_type == "agent":
            print(f"SKIP_AGENT_ACTION: {name}: Kiro must execute agent prompt hooks")
            continue

        if action_type != "command":
            print(f"SKIP_UNKNOWN_ACTION: {name}: {action_type}")
            continue

        command = action.get("command")
        timeout = hook.get("timeout")

        if tier == "blocking":
            ok = run_blocking_command(command, name, timeout) and ok
        elif tier == "async":
            schedule_async_command(command, name)
        else:
            print(f"ERROR: unknown execution_tier for {name}: {tier}", file=sys.stderr)
            ok = False

    return ok


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("hook_files", nargs="+", help="Kiro hook JSON files to validate")
    parser.add_argument(
        "--run-hooks",
        action="store_true",
        help="After validation, execute command hooks according to execution_tier. Agent hooks are reported only.",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    schema_path = root / "schemas" / "kiro-hook.schema.json"
    if not schema_path.exists():
        print(f"ERROR: schema not found: {schema_path}", file=sys.stderr)
        return 2

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    ok = True
    validated_data: list[dict[str, Any]] = []
    for arg in args.hook_files:
        target = Path(arg)
        if not target.exists():
            print(f"ERROR: file not found: {target}", file=sys.stderr)
            ok = False
            continue
        valid, data = validate_file(target, validator)
        ok = valid and ok
        if valid and data is not None:
            validated_data.append(data)

    if args.run_hooks and ok:
        for data in validated_data:
            ok = execute_hooks(data) and ok

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
