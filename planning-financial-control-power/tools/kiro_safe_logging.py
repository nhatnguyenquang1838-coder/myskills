#!/usr/bin/env python3
"""Parallel-safe Kiro logging helpers for PFC Power tools.

Rules:
- Do not write diagnostic text to stdout in MCP stdio tools.
- Use stderr and per-run local files for debug logs.
- Use .pm/audit/runs/{run_id}.agent-action.ndjson for semantic PFC audit events.
- Shared aggregate logs are optional convenience only; per-run files are source of truth.
- Semantic action logs must include BCBS239 principle tags.
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

RUN_ID_PATTERN = re.compile(r"[^A-Za-z0-9_.-]+")
DEFAULT_BCBS239_TAGS = ["06-pfc-skill-guardrail-map"]
VALID_BCBS239_TAGS = {
    "01-governance-and-infrastructure",
    "02-risk-data-aggregation",
    "03-risk-reporting-practices",
    "04-supervisory-review-remediation",
    "05-2023-progress-lessons",
    "06-pfc-skill-guardrail-map",
    "07-bcbs239-skill-contract-guidance",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_run_id(prefix: str = "RUN") -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    return f"{prefix}-{stamp}-{uuid.uuid4().hex[:8]}"


def sanitize_run_id(run_id: str) -> str:
    cleaned = RUN_ID_PATTERN.sub("-", run_id.strip())
    cleaned = cleaned.strip(".-_")
    return cleaned or new_run_id()


def get_run_id(explicit_run_id: str | None = None) -> str:
    """Resolve run_id from argument, environment, or generated ID."""
    candidate = explicit_run_id or os.getenv("PFC_RUN_ID") or os.getenv("KIRO_RUN_ID")
    return sanitize_run_id(candidate) if candidate else new_run_id()


def short_run_id(run_id: str) -> str:
    return sanitize_run_id(run_id)[-8:]


def normalize_bcbs239_tags(tags: Any) -> list[str]:
    """Return valid BCBS239 tags, defaulting to the PFC guardrail map.

    Runtime logging must not fail silently just because a caller omitted the tag.
    The default tag keeps the event schema-compliant while signaling that the event
    is governed by PFC guardrails. Callers should pass more specific tags when known.
    """
    if tags is None:
        return DEFAULT_BCBS239_TAGS.copy()
    if isinstance(tags, str):
        candidate = [tags]
    elif isinstance(tags, list):
        candidate = [str(item) for item in tags]
    else:
        candidate = DEFAULT_BCBS239_TAGS.copy()

    valid = [tag for tag in candidate if tag in VALID_BCBS239_TAGS]
    return valid or DEFAULT_BCBS239_TAGS.copy()


def run_debug_log_path(run_id: str, root: str | Path = ".") -> Path:
    root_path = Path(root).resolve()
    return root_path / ".kiro" / "logs" / "runs" / f"{sanitize_run_id(run_id)}.log"


def agent_action_log_path(run_id: str, root: str | Path = ".") -> Path:
    root_path = Path(root).resolve()
    return root_path / ".pm" / "audit" / "runs" / f"{sanitize_run_id(run_id)}.agent-action.ndjson"


def ide_event_log_path(run_id: str, root: str | Path = ".") -> Path:
    root_path = Path(root).resolve()
    return root_path / ".pm" / "audit" / "runs" / f"{sanitize_run_id(run_id)}.ide-event.ndjson"


def turn_analysis_path(run_id: str, root: str | Path = ".") -> Path:
    root_path = Path(root).resolve()
    return root_path / ".pm" / "audit" / "runs" / f"{sanitize_run_id(run_id)}.turn-analysis.md"


def setup_kiro_logger(
    name: str = "kiro_power_agent",
    root: str | Path = ".",
    run_id: str | None = None,
    aggregate_log: bool = False,
) -> logging.Logger:
    """Return a parallel-safe logger.

    The logger writes to:
    - stderr, with run_id and pid markers
    - .kiro/logs/runs/{run_id}.log

    aggregate_log=True also writes to .kiro/logs/power_steps.log, but that file is
    not the source of truth during parallel execution.
    """
    resolved_run_id = get_run_id(run_id)
    safe_run_id = sanitize_run_id(resolved_run_id)
    logger_name = f"{name}.{safe_run_id}"

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    setattr(logger, "pfc_run_id", safe_run_id)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt=f"%(asctime)s [%(levelname)s] [run={short_run_id(safe_run_id)}] [pid={os.getpid()}] %(message)s",
        datefmt="%H:%M:%S",
    )

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(formatter)
    logger.addHandler(stderr_handler)

    per_run_path = run_debug_log_path(safe_run_id, root)
    per_run_path.parent.mkdir(parents=True, exist_ok=True)

    file_handler = RotatingFileHandler(
        per_run_path,
        maxBytes=5_000_000,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if aggregate_log:
        root_path = Path(root).resolve()
        aggregate_path = root_path / ".kiro" / "logs" / "power_steps.log"
        aggregate_path.parent.mkdir(parents=True, exist_ok=True)
        aggregate_handler = RotatingFileHandler(
            aggregate_path,
            maxBytes=10_000_000,
            backupCount=3,
            encoding="utf-8",
        )
        aggregate_handler.setFormatter(formatter)
        logger.addHandler(aggregate_handler)

    return logger


def append_ndjson(path: Path, event: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    event.setdefault("ts", utc_now())
    event.setdefault("pid", os.getpid())
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")


def append_agent_action_log(event: dict[str, Any], root: str | Path = ".", run_id: str | None = None) -> str:
    """Append a semantic PFC action event to a per-run NDJSON file.

    Returns the resolved run_id.
    """
    resolved_run_id = get_run_id(run_id or event.get("run_id"))
    event.setdefault("run_id", resolved_run_id)
    event.setdefault("log_level", "semantic_action")
    event["bcbs239_principle_tag"] = normalize_bcbs239_tags(event.get("bcbs239_principle_tag"))
    append_ndjson(agent_action_log_path(resolved_run_id, root), event)
    return resolved_run_id


def append_ide_event_log(event: dict[str, Any], root: str | Path = ".", run_id: str | None = None) -> str:
    """Append optional raw IDE/tool event to a per-run NDJSON file.

    Returns the resolved run_id.
    """
    resolved_run_id = get_run_id(run_id or event.get("run_id") or event.get("session_id"))
    event.setdefault("run_id", resolved_run_id)
    event.setdefault("log_level", "raw_event")
    append_ndjson(ide_event_log_path(resolved_run_id, root), event)
    return resolved_run_id


def append_turn_analysis(text: str, root: str | Path = ".", run_id: str | None = None) -> str:
    """Append human-readable turn analysis to a per-run Markdown file.

    Returns the resolved run_id.
    """
    resolved_run_id = get_run_id(run_id)
    path = turn_analysis_path(resolved_run_id, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(f"\n---\n\n## Turn Analysis — {utc_now()}\n\nRun ID: `{resolved_run_id}`\n\n{text.strip()}\n")
    return resolved_run_id


def log_paths_summary(run_id: str, root: str | Path = ".") -> dict[str, str]:
    """Return the expected per-run log paths for display or debugging."""
    safe = sanitize_run_id(run_id)
    return {
        "run_id": safe,
        "debug_log": str(run_debug_log_path(safe, root)),
        "agent_action_log": str(agent_action_log_path(safe, root)),
        "ide_event_log": str(ide_event_log_path(safe, root)),
        "turn_analysis": str(turn_analysis_path(safe, root)),
    }


if __name__ == "__main__":
    smoke_run_id = get_run_id("RUN-SMOKE")
    logger = setup_kiro_logger(run_id=smoke_run_id)
    logger.info("Kiro parallel-safe logger initialized")
    append_agent_action_log({
        "run_id": smoke_run_id,
        "action_id": "ACT-SMOKE",
        "agent": "kiro_power_agent",
        "action_type": "OUTPUT_GENERATED",
        "status": "PASS",
        "bcbs239_principle_tag": ["06-pfc-skill-guardrail-map"],
        "summary": "Smoke event written by kiro_safe_logging.py",
    })
    append_ide_event_log({
        "run_id": smoke_run_id,
        "event": "logger_smoke_test",
        "status": "PASS",
        "summary": "Smoke IDE/debug event written.",
    })
    append_turn_analysis("Smoke test completed for parallel-safe logging.", run_id=smoke_run_id)
    logger.info("Log paths: %s", json.dumps(log_paths_summary(smoke_run_id), sort_keys=True))
