# 20 — Logging Depth Policy

## Purpose

Define how the Planning & Financial Control Power logs continuously without slowing the agent or consuming LLM context.

## Decision

Use hybrid logging:

```txt
1. Semantic PFC action log: always on
2. Safe local debug log: always on for Python tools
3. Turn analysis log: written only when requested or at explicit checkpoint
4. Raw IDE event log: optional/debug/failure mode
```

## Logging layers

| Layer | File | Purpose | Default |
|---|---|---|---|
| Safe tool debug | `.kiro/logs/power_steps.log` | tail live while Kiro works | ON |
| Semantic audit | `.pm/audit/agent-action-log.ndjson` | deep analysis and improvement | ON |
| Turn analysis | `.pm/audit/turn-analysis-log.md` | human-readable review | ON-DEMAND |
| Raw IDE events | `.pm/audit/ide-event-log.ndjson` | debug/failure trace | OPTIONAL |

## stdout rule for MCP stdio tools

```txt
stdout is reserved for MCP / JSON-RPC protocol messages.
Do not write diagnostic text to stdout.
```

Forbidden in Python MCP stdio tools:

```txt
print("debug")
```

Allowed:

```txt
logger.info(...)
print(..., file=sys.stderr)
append local file logs
```

Forbidden in Node MCP stdio tools:

```txt
console.log("debug")
```

Allowed:

```txt
console.error(...)
append local file logs
```

## What to log every time

Log every semantic PFC step:

```txt
USE_CASE_RESOLVED
READINESS_CHECKED
GRAPH_LOADED
RUN_CONTEXT_BUILT
MEMORY_CONTEXT_LOADED
CONTRACT_CHECKED
SKILL_CALLED
SKILL_OUTPUT_VALIDATED
GRAPH_DELTA_PROPOSED
CASCADE_CHECKED
FINANCE_BASIS_CHECKED
REPORT_CLAIM_CHECKED
CIRCUIT_BREAKER_EVALUATED
OUTPUT_GENERATED
WRITEBACK_REQUESTED
WRITEBACK_DONE / WRITEBACK_BLOCKED
CHECKPOINT_WRITTEN
ERROR_HANDLED
```

## What not to force into LLM context

Do not ask the LLM to summarize every log entry during execution.

```txt
Agent works.
Python logger records.
LLM analyzes only when explicitly asked.
```

## Retention rule

Runtime logs are local artifacts. Do not commit live logs.

Commit templates and tooling only.

## Failure rule

If logging fails, the agent must add this to the final output or checkpoint:

```txt
Audit gap: logging failed
Reason:
Recovery:
```
