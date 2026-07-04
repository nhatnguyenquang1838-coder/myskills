# Kiro-Safe Logging Usage

Utility:

```txt
tools/kiro_safe_logging.py
```

## Purpose

Provide production-safe and parallel-safe logging for Python Kiro Power tools.

## Rules

```txt
Do not write diagnostic text to stdout in MCP stdio tools.
Use stderr and per-run local files.
Use .pm/audit/runs/{run_id}.agent-action.ndjson for semantic PFC actions.
Per-run files are the source of truth.
```

## Example

```python
from tools.kiro_safe_logging import setup_kiro_logger, append_agent_action_log

run_id = "RUN-001"
logger = setup_kiro_logger(run_id=run_id)

logger.info("Step: checking readiness")

append_agent_action_log({
    "run_id": run_id,
    "action_id": "ACT-001",
    "agent": "pm-controller",
    "action_type": "READINESS_CHECKED",
    "status": "PASS",
    "mode": "M2",
    "summary": "Readiness mode selected."
})
```

## Live tail for one run

```bash
tail -f .kiro/logs/runs/RUN-001.log
```

## Runtime log files

```txt
.kiro/logs/runs/{run_id}.log
.pm/audit/runs/{run_id}.agent-action.ndjson
.pm/audit/runs/{run_id}.ide-event.ndjson
.pm/audit/runs/{run_id}.turn-analysis.md
```

## Smoke test

```bash
python tools/kiro_safe_logging.py
```

Expected new files:

```txt
.kiro/logs/runs/RUN-SMOKE.log
.pm/audit/runs/RUN-SMOKE.agent-action.ndjson
.pm/audit/runs/RUN-SMOKE.ide-event.ndjson
.pm/audit/runs/RUN-SMOKE.turn-analysis.md
```

## Aggregate logs

`.kiro/logs/power_steps.log` is optional only.

Use `aggregate_log=True` if needed, but do not treat the aggregate log as the source of truth during parallel execution.

## Git rule

Runtime logs must not be committed.

Commit templates, policies, and tools only.
