#!/usr/bin/env python3
"""Validate Kiro v1 hook JSON files against the local PFC Kiro hook schema.

Usage:
  python tools/validate_kiro_hooks.py hooks/kiro-v1/pfc-workspace-hooks.json
  python tools/validate_kiro_hooks.py hooks/kiro-v1/*.json

The schema tracks the public Kiro v1 hook shape documented at:
  https://kiro.dev/docs/hooks/
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator  # type: ignore
except Exception as exc:  # pragma: no cover
    print("ERROR: jsonschema is required. Install with: pip install jsonschema", file=sys.stderr)
    raise SystemExit(2) from exc


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL: {path} is not valid JSON: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


def validate_file(path: Path, validator: Draft202012Validator) -> bool:
    data = load_json(path)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if errors:
        print(f"FAIL: {path} is invalid")
        for err in errors:
            loc = "/".join(str(p) for p in err.path) or "<root>"
            print(f"- {loc}: {err.message}")
        return False

    print(f"PASS: {path} is valid")
    return True


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_kiro_hooks.py <hook-file.json> [hook-file.json ...]", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    schema_path = root / "schemas" / "kiro-hook.schema.json"
    if not schema_path.exists():
        print(f"ERROR: schema not found: {schema_path}", file=sys.stderr)
        return 2

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    ok = True
    for arg in sys.argv[1:]:
        target = Path(arg)
        if not target.exists():
            print(f"ERROR: file not found: {target}", file=sys.stderr)
            ok = False
            continue
        ok = validate_file(target, validator) and ok

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
