# 11 — Circuit Breaker Policy

## Purpose

Stop or downgrade Planning & Financial Control outputs when critical safety, evidence, context, cascade, or finance conditions fail.

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

Open when forecast or budget status is requested but resource allocation, rate card, or approved budget is missing.

### Context breaker

Open when stale, unlinked, or historical context is being used as current project fact.

### Cascade breaker

Open when a changed graph node has not propagated to linked nodes.

### History-bias breaker

Open when historical benchmark is used to declare current project status.

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
