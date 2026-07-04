# Circuit Breaker Support Document

## Purpose

Circuit Breaker protects the Planning & Financial Control Power from continuing when the current task would produce misleading, unsafe, or unsupported planning/finance output.

It is not a refusal mechanism. It is a control mechanism.

```txt
Detect unsafe state
-> stop or downgrade output
-> explain blocked claims
-> request only critical missing data
-> create recovery path
```

## Why this exists

Planning and finance outputs can create real project decisions. If the Power lacks source data, has conflicting context, or detects stale baseline usage, it must not continue as if everything is valid.

## Circuit Breaker states

| State | Meaning | Allowed action |
|---|---|---|
| CLOSED | Safe to continue | Run normal workflow |
| HALF_OPEN | Some data missing or confidence low | Continue with limited/draft output |
| OPEN | Critical condition broken | Stop official output and require recovery |

## Breaker triggers

### Evidence breaker

Open when:

```txt
report contains RAG/date/cost/resource claim with no evidence_id, assumption_id, decision_id, derived_from, or baseline_version
```

Action:

```txt
Block official report
Return unsupported claims
Ask for source or mark as assumption
```

### Baseline breaker

Open when:

```txt
output says approved/on track/budget sufficient but no approved baseline exists
```

Action:

```txt
Downgrade to draft mode
Set blocked claims: official RAG, controlled baseline, approved forecast
```

### Finance breaker

Open when:

```txt
cost forecast requested but resource allocation or rate card is missing
```

Action:

```txt
Return missing finance data checklist
Allow scenario range only if user accepts assumptions
```

### Context breaker

Open when:

```txt
loaded context is stale, unlinked to target graph node, or from historical archive used as current fact
```

Action:

```txt
Run context-audit
Reject stale/unlinked context
Reload by graph nodes
```

### Cascade breaker

Open when:

```txt
a graph node changed but linked nodes were not checked
```

Action:

```txt
Run cascade-impact-check
Block report refresh until affected nodes are reviewed
```

### History-bias breaker

Open when:

```txt
historical benchmark is used to declare current status
```

Action:

```txt
Rewrite as benchmark/risk signal
Do not modify baseline
```

## Breaker severity

| Severity | Meaning | Behavior |
|---|---|---|
| S0 | no issue | continue |
| S1 | minor missing info | continue with note |
| S2 | confidence limitation | continue as draft only |
| S3 | blocked official claim | block official output |
| S4 | unsafe contradiction | stop workflow and require resolution |

## Recovery pattern

When breaker opens, output must include:

```txt
Breaker:
Severity:
Reason:
Blocked claims:
Missing data:
Allowed fallback:
Recovery questions:
Next action:
```

## Example

User asks:

```txt
Generate executive report and say we are on budget.
```

But the graph has no rate card and no approved budget.

Output:

```txt
Breaker: Finance breaker
Severity: S3
Reason: Budget status requested but approved budget/rate/resource data is missing.
Blocked claims: budget is Green, on budget, approved forecast
Allowed fallback: draft finance section with missing data log
Recovery questions:
1. What is the approved budget or budget cap?
2. What rate card or monthly cost assumption should be used?
3. Which resource allocation should be costed?
```

## Relationship to readiness mode

| Mode | Breaker behavior |
|---|---|
| M0 | Most official outputs blocked; draft/skeleton allowed |
| M1 | Cost/RAG official claims blocked; draft planning allowed |
| M2 | Forecast allowed; approved baseline claims blocked |
| M3 | Official output allowed only if fact-check passes |

## Design rule

```txt
Circuit Breaker does not kill productivity.
It prevents fake confidence and routes the user to the safest next step.
```
