# 19 — Agent Action Logging Policy

## Purpose

Ensure every meaningful agent action in the Planning & Financial Control Power is traceable.

This policy creates an audit trail for:

```txt
who did what
when it happened
why it happened
what input was used
what output was produced
what graph nodes were read/written
what guardrails/breakers were applied
what was blocked or downgraded
```

## Core rule

```txt
No meaningful agent action should be invisible.
Every workflow step must produce or append an Agent Action Log entry.
```

## Runtime log location

In a target workspace, write runtime logs to:

```txt
.pm/audit/agent-action-log.yaml
```

For one-off reports or debugging, also attach log summaries to:

```txt
.pm/audit/run-execution-record.md
```

## Logging granularity

Log one entry per meaningful action, not one entry per token.

Meaningful actions include:

```txt
user request received
use case resolved
readiness mode selected
Project Control Graph loaded
Run Context Graph built
memory/context loaded
DL Skill contract checked
DL Skill called
DL Skill output validated
graph delta proposed
cascade check run
finance basis check run
report/claim check run
circuit breaker evaluated
write-back requested
write-back approved/blocked
checkpoint written
error/recovery triggered
```

## Required log fields

Every action log entry must include:

```txt
action_id
run_id
timestamp
agent
agent_role
action_type
use_case
mode
run_type
status
input_refs
output_refs
graph_nodes_read
graph_deltas_proposed
graph_nodes_written
enforcement_gates
guardrails_applied
breaker_state
blocked_claims
writeback_decision
summary
```

## Optional log fields

```txt
duration_ms
skill_id
contract_id
source_ids
memory_ids
history_ids
file_paths_touched
commands_run
errors
recovery_action
review_required
redaction_note
```

## Action status values

```txt
STARTED
PASS
DOWNGRADED
BLOCKED
FAILED
SKIPPED
```

## Action types

```txt
USER_REQUEST_RECEIVED
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
WRITEBACK_DONE
WRITEBACK_BLOCKED
CHECKPOINT_WRITTEN
ERROR_HANDLED
```

## Sensitive data rule

Do not log raw secrets, passwords, tokens, customer PII, or full private documents.

Instead log:

```txt
source reference
file path
summary
redacted value
hash/reference ID
```

## Failure rule

If the agent cannot write the log, the final output must state:

```txt
Audit gap: agent action log was not written.
Reason:
Recovery:
```

## Enforcement mapping

| Workflow gate | Required log action |
|---|---|
| E0 Intent gate | USE_CASE_RESOLVED |
| E1 Readiness gate | READINESS_CHECKED |
| E2 Graph gate | GRAPH_LOADED, RUN_CONTEXT_BUILT |
| E3 Context/memory gate | MEMORY_CONTEXT_LOADED |
| E4 Contract gate | CONTRACT_CHECKED |
| E5 Skill output gate | SKILL_OUTPUT_VALIDATED |
| E6 Cascade gate | CASCADE_CHECKED |
| E7 Finance gate | FINANCE_BASIS_CHECKED |
| E8 Report/claim gate | REPORT_CLAIM_CHECKED |
| E9 Write-back gate | WRITEBACK_REQUESTED, WRITEBACK_DONE or WRITEBACK_BLOCKED |
| E10 Checkpoint gate | CHECKPOINT_WRITTEN |

## Minimum pass rule

```txt
A workflow is not fully auditable unless every mandatory enforcement gate has at least one corresponding log entry.
```
