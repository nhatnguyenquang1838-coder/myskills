#!/usr/bin/env python3
"""Kiro-safe logging helpers for PFC Power tools.

Rules:
- Do not write diagnostic text to stdout in MCP stdio tools.
- Use stderr and local files for debug logs.
- Use .pm/audit/agent-action-log.ndjson for semantic PFC audit events.
"""

from __future__ import annotations

import json
import logging
import sys
from datetime import datetime, timezone
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def setup_kiro_logger(name: str = "kiro_power_agent", root: str | Path = ".") -> logging.Logger:
    """Return a logger that writes to stderr and .kiro/logs/power_steps.log.

    Safe for MCP stdio tools because it does not write diagnostics to stdout.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(formatter)
    logger.addHandler(stderr_handler)

    root_path = Path(root).resolve()
    log_dir = root_path / ".kiro" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    file_handler = RotatingFileHandler(
        log_dir / "power_steps.log",
        maxBytes=5_000_000,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def append_ndjson(path: Path, event: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    event.setdefault("ts", utc_now())
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")


def append_agent_action_log(event: dict[str, Any], root: str | Path = ".") -> None:
    """Append a semantic PFC action event.

    Intended file:
      .pm/audit/agent-action-log.ndjson
    """
    root_path = Path(root).resolve()
    event.setdefault("log_level", "semantic_action")
    append_ndjson(root_path / ".pm" / "audit" / "agent-action-log.ndjson", event)


def append_ide_event_log(event: dict[str, Any], root: str | Path = ".") -> None:
    """Append optional raw IDE/tool event.

    Intended file:
      .pm/audit/ide-event-log.ndjson
    """
    root_path = Path(root).resolve()
    event.setdefault("log_level", "raw_event")
    append_ndjson(root_path / ".pm" / "audit" / "ide-event-log.ndjson", event)


def append_turn_analysis(text: str, root: str | Path = ".") -> None:
    """Append human-readable turn analysis on demand.

    Intended file:
      .pm/audit/turn-analysis-log.md
    """
    root_path = Path(root).resolve()
    path = root_path / ".pm" / "audit" / "turn-analysis-log.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(f"\n---\n\n## Turn Analysis — {utc_now()}\n\n{text.strip()}\n")


if __name__ == "__main__":
    logger = setup_kiro_logger()
    logger.info("Kiro-safe logger initialized")
    append_agent_action_log({
        "run_id": "RUN-SMOKE",
        "action_id": "ACT-SMOKE",
        "agent": "kiro_power_agent",
        "action_type": "OUTPUT_GENERATED",
        "status": "PASS",
        "summary": "Smoke event written by kiro_safe_logging.py",
    })
