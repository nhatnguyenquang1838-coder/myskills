# Memory Context Controller Support Document

## Purpose

Memory Context Controller manages how the Power remembers, retrieves, validates, forgets, and isolates project context.

It prevents three failure modes:

```txt
1. The Power forgets important project decisions.
2. The Power overuses stale/historical context and creates biased output.
3. The Power exhausts the context window after a Circuit Breaker trip by replaying failed history.
```

## Core principle

```txt
Memory supports the graph.
Memory does not replace the graph.
```

The source of truth remains:

```txt
.pm/control/project-control.yaml
```

## Memory layers

| Layer | Meaning | Authority |
|---|---|---|
| L0 Interaction memory | Current chat/session details | low |
| L1 Working memory | Current task context and selected graph nodes | medium |
| L2 Project memory | Approved graph nodes, assumptions, decisions, evidence | high |
| L3 Historical memory | Similar old projects, lessons learned, benchmarks | benchmark only |
| L4 Raw archive | emails, transcripts, old docs, exports | low until indexed |
| L5 Failure recovery packet | isolated breaker recovery context | narrow and temporary |

## Memory types

| Type | Use | Example |
|---|---|---|
| Fact memory | approved/source-backed project truth | approved budget, milestone baseline |
| Decision memory | recorded decision and owner/date | scope approved by PM on date |
| Assumption memory | unverified but useful assumption | rate card estimated at X |
| Missing-data memory | known gap | QE capacity unknown |
| Pattern memory | reusable method/pattern | timeline delay cascade |
| Historical memory | benchmark/risk signal | similar project delayed due to vendor API |
| Failure recovery memory | breaker recovery packet | isolated context after Finance breaker |

## Memory write rules

Only write memory when it has:

```txt
id
type
source
created_date
confidence
linked_graph_ids
expiry_or_review_date
owner_optional
```

Do not write:

```txt
random chat observations
unsupported opinions
old project facts as current facts
private/sensitive details not needed for planning control
full failed conversation history after breaker trip
```

## Memory retrieval rules

Load memory by graph target, not by keyword alone.

```txt
User asks about WP-001
-> load WP-001
-> load linked MS/RA/COST/FCST/RISK
-> load memories linked to those IDs
-> load history only if benchmark/scenario is needed
```

## Memory confidence

| Confidence | Condition |
|---|---|
| High | approved baseline/evidence/decision with owner/date |
| Medium | documented but not approved |
| Low | assumption or verbal input |
| Blocked | critical source missing |

## Staleness policy

Memory becomes stale when:

```txt
baseline version changes
linked graph node changes
source date is older than allowed review window
contradicting evidence appears
owner marks it obsolete
```

Default review windows:

| Memory type | Review window |
|---|---|
| Fact memory | when baseline changes |
| Decision memory | when superseded by later decision |
| Assumption memory | every major output or 14 days |
| Missing-data memory | every intake/checkpoint |
| Historical memory | every use |
| Pattern memory | quarterly or after failure |
| Failure recovery memory | one recovery turn only |

## Conflict resolution

Authority order:

```txt
approved baseline
> latest approved decision
> current graph forecast
> documented evidence
> assumption
> historical benchmark
> raw archive
```

If memory conflicts with current graph:

```txt
1. Use current graph.
2. Flag conflict.
3. Create or update missing-data/decision-needed item.
4. Do not merge silently.
```

## Isolate-and-Condense function

Purpose:

```txt
Prevent context exhaustion and repeated hallucination after a Circuit Breaker trip.
```

Trigger:

```txt
Circuit Breaker state is HALF_OPEN or OPEN.
```

Hard rule:

```txt
When the circuit breaker trips, Kiro must intercept the prompt window, wipe the conversational memory buffer for the recovery turn, and inject only the failure recovery packet.
```

Function contract:

```txt
isolate_and_condense(breaker_event, breached_constraint, circuit_breaker_log) -> failure_recovery_packet
```

Allowed recovery packet contents:

```txt
1. A 2-sentence summary of the failure state.
2. The exact breached constraint from contracts/dl-skill-contract-schema.yaml or the relevant schema/policy that failed.
3. The structured error log from templates/circuit-breaker-log.md.
```

Forbidden recovery packet contents:

```txt
full trailing conversation
raw chain of thought
unbounded chat history
all project files
all historical examples
multiple old failed attempts
```

Recovery packet shape:

```yaml
failure_recovery_packet:
  breaker: Finance breaker
  severity: S3
  failure_summary:
    - "The requested budget status cannot be confirmed because cost line totals do not reconcile to the declared total budget."
    - "Official budget/RAG output is blocked until deterministic finance invariants pass."
  breached_constraint:
    source: contracts/dl-skill-contract-schema.yaml
    exact_text: "Skill outputs must satisfy declared output contract and may not create unsupported financial claims."
  circuit_breaker_log:
    breaker: Finance breaker
    blocked_claims:
      - "on budget"
    missing_data:
      - "reconciled cost line total"
    allowed_fallback: "draft scenario with failed reconciliation shown"
  next_allowed_actions:
    - "recalculate deterministic totals"
    - "ask for corrected cost payload"
    - "keep output as blocked/draft"
```

Context budget rule:

```txt
The failure recovery packet should be small enough to fit into a single recovery turn.
Target: <= 1,500 tokens.
```

Post-isolation behavior:

```txt
1. Do not resume from full conversation history.
2. Do not call broad retrieval.
3. Rebuild Run Context Graph from target IDs only if needed.
4. Use exact breached constraint and structured error log as recovery authority.
5. Allow only recovery, clarification, or downgraded output.
```

## Memory index format

Recommended file:

```txt
.pm/memory/memory-index.yaml
```

Example:

```yaml
memories:
  - id: MEM-001
    type: decision
    text: MVP2 keeps Telegram notification in scope.
    source: meeting note
    source_id: EVD-003
    linked_graph_ids: [WP-001]
    confidence: medium
    created_date: 2026-07-04
    review_date: 2026-07-18
    status: active

  - id: MEM-002
    type: historical_benchmark
    text: Similar vendor API dependency created 2-week delay in a past project.
    source: history-index
    linked_graph_ids: [DEP-001, RISK-001]
    confidence: low
    use_as: benchmark_only
    status: active
```

## Retrieval log

Every non-current memory retrieval must be logged:

```txt
.pm/audit/context-retrieval-log.md
```

Required fields:

```txt
date
request
target_graph_ids
memories_loaded
reason
used_as
bias_risk
output_claims_supported
```

## Memory Context Controller workflow

```txt
1. Identify user intent.
2. Identify target graph nodes.
3. Load current graph nodes.
4. Load linked active memories.
5. Check staleness and conflicts.
6. Load historical memories only if needed.
7. Run context audit.
8. Produce output with memory labels.
9. Log retrieval when memory influences output.
```

## Circuit breaker recovery workflow

```txt
1. Receive breaker_event.
2. Stop normal memory retrieval.
3. Run Isolate-and-Condense.
4. Wipe conversational memory buffer for recovery turn.
5. Inject only failure_recovery_packet.
6. Execute recovery action or ask critical clarification.
7. Discard failure recovery packet after one recovery turn unless explicitly checkpointed.
```

## Circuit breaker connection

Memory Context Controller must trigger Circuit Breaker when:

```txt
memory is stale but used as current fact
memory conflicts with approved baseline
historical memory is used as current truth
required linked graph node is missing
memory has no source or confidence
recovery attempts require full failed conversation replay
```

## Output labels

When memory is used, output must label it as:

```txt
Current fact
Decision memory
Assumption memory
Historical benchmark
Pattern memory
Failure recovery packet
Unknown / missing data
```

## Design rule

```txt
Remember enough to be useful.
Forget or downgrade enough to stay honest.
Recover with less context than the failed run.
```
