# Checkpoint — Parallel-Safe Logging Cleanup

Date: 2026-07-04
Scope: Upgrade PFC Power logging for parallel Kiro runs and clean redundant shared logging artifacts.

## Changed

```txt
tools/kiro_safe_logging.py
schemas/agent-action-log.schema.json
steering/20-logging-depth-policy.md
tools/logging-usage.md
scripts/install-workspace.sh
scripts/install-workspace.ps1
README.md
.gitignore
_work/TASKS.md
```

## Removed

```txt
templates/agent-action-log.yaml
templates/agent-action-log.ndjson
```

## Retained

```txt
templates/ide-event-log.ndjson
```

Reason: connector blocked deletion once. It is no longer copied by bootstrap and no longer part of the runtime source-of-truth model.

## New source-of-truth runtime model

```txt
.kiro/logs/runs/{run_id}.log
.pm/audit/runs/{run_id}.agent-action.ndjson
.pm/audit/runs/{run_id}.ide-event.ndjson
.pm/audit/runs/{run_id}.turn-analysis.md
```

## Key rules

```txt
Every parallel run writes to its own files.
Every log line includes run_id and pid.
Per-run files are source of truth.
Shared aggregate logs are optional only.
stdout remains forbidden for MCP diagnostic logging.
```

## Remaining blockers

```txt
hooks not schema-verified
validators not run in clean local checkout
bootstrap not tested in real target workspace
logging smoke test not yet run in clean workspace
```
