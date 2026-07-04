# 11 — Circuit Breaker Policy

## Purpose

Stop or downgrade Planning & Financial Control outputs when critical safety, evidence, context, cascade, finance, or BCBS239 conditions fail.

## Breaker states

| State | Meaning | Behavior |
|---|---|---|
| CLOSED | safe | continue normal workflow |
| HALF_OPEN | limited confidence | draft/scenario output only |
| OPEN | unsafe or unsupported | block official output and recover |

## Breaker triggers

### Evidence breaker

Open when official report or RAG claim lacks support from:

```txt
evidence_id
assumption_id
decision_id
derived_from
baseline_version
```

### Baseline breaker

Open when output claims approved/on-track/controlled baseline without approved baseline nodes.

### Finance breaker

Open when forecast or budget status is requested but resource allocation, rate card, approved budget, or deterministic sum reconciliation is missing or invalid.

### Context breaker

Open when stale, unlinked, or historical context is being used as current project fact.

### Cascade breaker

Open when a changed graph node has not propagated to linked nodes.

### History-bias breaker

Open when historical benchmark is used to declare current project status.

### Contract breaker

Open when a DL Skill is called without a valid contract, required preconditions are absent, or the output breaches `contracts/dl-skill-contract-schema.yaml`.

### BCBS239 breaker

Open when an agent action, output, or graph delta lacks required BCBS239 principle tags, source lineage, reconciliation evidence, or deterministic validation for finance/reporting claims.

## Required breaker output

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

## Context isolation after breaker trip

Strict directive:

```txt
Never pass the full trailing conversational history to an agent after a circuit breaker trip.
```

Reason:

```txt
Full trailing history after a failure can reintroduce stale assumptions, hallucinated claims, repeated failed reasoning, and token-window exhaustion.
```

Required behavior after `HALF_OPEN` or `OPEN`:

```txt
1. Stop normal context loading.
2. Run Memory Context Controller Isolate-and-Condense.
3. Wipe the active conversational memory buffer for the recovery turn.
4. Inject only the approved failure recovery packet.
5. Ask only critical recovery questions or return allowed fallback.
```

Approved failure recovery packet:

```txt
1. 2-sentence failure-state summary.
2. Exact breached constraint from contracts/dl-skill-contract-schema.yaml or relevant policy/schema.
3. Structured error log from templates/circuit-breaker-log.md.
```

Forbidden after breaker trip:

```txt
full conversation replay
broad file search without target graph IDs
history benchmark loading unless explicitly requested as benchmark_only
multi-agent convergence without a new scoped Run Context Graph
write-back attempt without a fresh State Lock
```

## Severity

| Severity | Meaning | Behavior |
|---|---|---|
| S0 | no issue | continue |
| S1 | minor issue | continue with note |
| S2 | confidence limitation | draft only |
| S3 | official claim blocked | block official output |
| S4 | contradiction/unsafe | stop and require resolution |

## Rule

Circuit Breaker should not block useful work. It should block fake confidence.

## Recovery rule

```txt
Recovery must be smaller than the failed context.
If recovery requires more context than the original failed run, the recovery design is wrong.
```
