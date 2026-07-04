# 20 — Logging Depth Policy

## Purpose

Define how the Planning & Financial Control Power logs continuously without slowing the agent, corrupting MCP stdio, or mixing parallel runs.

## Decision

Use hybrid, parallel-safe logging:

```txt
1. Semantic PFC action log: always on, per run
2. Safe local debug log: always on for Python tools, per run
3. Turn analysis log: written only when requested or at explicit checkpoint, per run
4. Raw IDE event log: optional/debug/failure mode, per run
5. Hook execution logs: tiered into blocking and async
```

## Logging layers

| Layer | File | Purpose | Default |
|---|---|---|---|
| Safe tool debug | `.kiro/logs/runs/{run_id}.log` | tail one Kiro run without interleaving | ON |
| Semantic audit | `.pm/audit/runs/{run_id}.agent-action.ndjson` | deep analysis and improvement | ON |
| Turn analysis | `.pm/audit/runs/{run_id}.turn-analysis.md` | human-readable review | ON-DEMAND |
| Raw IDE events | `.pm/audit/runs/{run_id}.ide-event.ndjson` | debug/failure trace | OPTIONAL |
| Aggregate debug | `.kiro/logs/power_steps.log` | convenience only, not source of truth | OFF by default |

## Parallel execution rule

```txt
Every parallel run must write to its own files.
Every log line must include run_id and pid.
Per-run files are the source of truth.
Shared aggregate logs are optional and best-effort only.
```

## Hook execution tiers

Hooks must declare `execution_tier` in `schemas/kiro-hook.schema.json`.

| Tier | Value | Execution mode | Examples | Critical-path behavior |
|---|---|---|---|---|
| Tier 1 | `blocking` | synchronous | YAML/JSON schema validation, `baseline-upgrade-check.kiro.hook`, finance invariant checks | must finish before the next semantic turn or write-back |
| Tier 2 | `async` | background/parallel | `context-audit.kiro.hook`, `workflow-gap-review.md`, heavy qualitative BCBS239 review | must not block the agent's next semantic turn |

## Tier 1 — blocking hooks

Purpose:

```txt
Stop unsafe graph mutation, invalid schema, broken budget math, or baseline violations before they can be committed.
```

Allowed Tier 1 work:

```txt
YAML/JSON syntax checks
Project Control Graph schema validation
DL Skill contract schema validation
budget/cost sum invariant checks
baseline freeze structural checks
State Lock acquisition/release checks
```

Rules:

```txt
blocking hooks run synchronously
blocking hooks must be deterministic
blocking hooks must not call broad retrieval
blocking hooks must not request full conversation history
blocking hooks may block write-back
```

## Tier 2 — async hooks

Purpose:

```txt
Run heavy qualitative audits without increasing critical-path latency or exhausting context.
```

Allowed Tier 2 work:

```txt
context audit
workflow gap review
BCBS239 qualitative alignment review
history-bias analysis
long-form report quality review
multi-file improvement suggestions
```

Rules:

```txt
async hooks are scheduled in the background
async hooks write findings to per-run audit files
async hooks cannot directly mutate Project Control Graph
async findings become input to the next checkpoint or explicit review request
async hooks may open a follow-up issue/blocker but cannot retroactively rewrite an already committed graph state
```

## Tier interaction rule

```txt
Tier 1 protects correctness now.
Tier 2 improves quality later.
```

If Tier 2 finds a severe issue after the agent has moved on:

```txt
1. write finding to .pm/audit/runs/{run_id}.agent-action.ndjson
2. create or update missing-data/risk/blocker record
3. mark next related output as requiring review
4. do not silently mutate the graph
```

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

For hooks, also log:

```txt
HOOK_VALIDATED
HOOK_EXECUTION_STARTED
HOOK_EXECUTION_BACKGROUND_SCHEDULED
HOOK_EXECUTION_COMPLETED
HOOK_EXECUTION_FAILED
```

## What not to force into LLM context

Do not ask the LLM to summarize every log entry during execution.

```txt
Agent works.
Python logger records.
LLM analyzes only when explicitly asked.
```

## Runtime directory contract

Bootstrap creates:

```txt
.kiro/logs/runs/
.pm/audit/runs/
```

Runtime examples:

```txt
.kiro/logs/runs/RUN-20260704-120000-a1b2c3d4.log
.pm/audit/runs/RUN-20260704-120000-a1b2c3d4.agent-action.ndjson
.pm/audit/runs/RUN-20260704-120000-a1b2c3d4.ide-event.ndjson
.pm/audit/runs/RUN-20260704-120000-a1b2c3d4.turn-analysis.md
```

## Redundancy rule

Do not create root-level runtime logs as source of truth:

```txt
.pm/audit/agent-action-log.ndjson
.pm/audit/ide-event-log.ndjson
```

Those shared files are deprecated because they are unsafe/noisy under parallel execution.

## Retention rule

Runtime logs are local artifacts. Do not commit live logs.

Commit templates, policies, and tooling only.

## Failure rule

If logging fails, the agent must add this to the final output or checkpoint:

```txt
Audit gap: logging failed
Reason:
Recovery:
```
