# UC-XX — Use Case Name

## Purpose

Define what job this use case performs for the Power.

## User intent examples

```txt
Example user request 1
Example user request 2
```

## Trigger conditions

```txt
When should this UC run?
```

## Required readiness mode

| Output type | Minimum mode |
|---|---|
| Skeleton / questions | M0 |
| Draft plan / rough report | M1 |
| Forecast / variance | M2 |
| Official baseline / executive report / RAG | M3 |

## Minimum required data

| Data item | Required for | Blocking level |
|---|---|---|
|  |  | Blocker / Limitation / Enhancement |

## Graph contract

### Graph nodes read

```txt
List graph node types this UC must read.
```

### Graph nodes written

```txt
List graph node types this UC may write.
```

### Draft-only nodes

```txt
List nodes that must remain draft unless approved.
```

### Approved write-back rules

```txt
State what approval/evidence is needed before persistent graph update.
```

## Execution contract

### Primary agent

```txt
agent-name
```

### Supporting agents

```txt
agent-name
```

### Required skills

```txt
skill-name
```

### Required hooks

```txt
hook-name
```

## Control contract

### Circuit breakers

| Breaker | When it opens |
|---|---|
| Baseline breaker |  |
| Finance breaker |  |
| Evidence breaker |  |
| Context breaker |  |
| Cascade breaker |  |
| History-bias breaker |  |

### Guardrails

```txt
Non-negotiable rules for this UC.
```

### Bias prevention

```txt
Bias checks required for this UC.
```

### Hallucination prevention

```txt
Required source/evidence/assumption/decision/derived links.
```

## Output contract

### Required output header

```txt
Mode:
Run type:
Use case:
Agents used:
Skills used:
Hooks triggered:
Graph nodes read:
Graph nodes written:
Circuit breaker state:
Guardrails applied:
Bias checks:
Hallucination checks:
Allowed output:
Blocked claims:
Next action:
```

### Allowed outputs

```txt
What this UC is allowed to produce.
```

### Blocked outputs

```txt
What this UC must not produce.
```

## Checkpoint / audit requirements

```txt
State whether this UC must create logs/checkpoints.
```

## Pass criteria

```txt
Conditions that prove this UC ran correctly.
```

## Failure / downgrade behavior

```txt
What happens if required data or controls fail.
```
