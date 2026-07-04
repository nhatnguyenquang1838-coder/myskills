# Kiro-Safe Logging Usage

Utility:

```txt
tools/kiro_safe_logging.py
```

## Purpose

Provide production-safe logging for Python Kiro Power tools.

## Rules

```txt
Do not write diagnostic text to stdout in MCP stdio tools.
Use stderr and local files.
Use .pm/audit/agent-action-log.ndjson for semantic PFC actions.
```

## Example

```python
from tools.kiro_safe_logging import setup_kiro_logger, append_agent_action_log

logger = setup_kiro_logger()

logger.info("Step: checking readiness")

append_agent_action_log({
    "run_id": "RUN-001",
    "action_id": "ACT-001",
    "agent": "pm-controller",
    "action_type": "READINESS_CHECKED",
    "status": "PASS",
    "mode": "M2",
    "summary": "Readiness mode selected."
})
```

## Live tail

```bash
tail -f .kiro/logs/power_steps.log
```

## Runtime log files

```txt
.kiro/logs/power_steps.log
.pm/audit/agent-action-log.ndjson
.pm/audit/ide-event-log.ndjson
.pm/audit/turn-analysis-log.md
```

## Git rule

Runtime logs must not be committed.

Commit templates, policies, and tools only.
