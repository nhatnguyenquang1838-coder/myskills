# 13 — Use Case Standard Policy

## Purpose

Define how agents must treat use cases inside the Planning & Financial Control Power.

## Core rule

```txt
Use-case standard guideline is authoritative.
Sample use cases are examples only.
```

## Authoritative source

```txt
knowledge/use-cases/use-case-standard-guideline.md
```

## Sample source

```txt
references/use-cases/
knowledge/use-cases/use-case-control-catalog.md
```

Samples can illustrate behavior, but they must not override the standard.

## Required behavior

Before executing or designing any use case, agents must check:

```txt
1. What is the use-case category?
2. What readiness mode is required?
3. What graph nodes must be read/written?
4. Which agent is primary?
5. Which skills are required?
6. Which hooks must run?
7. Which circuit breakers can open?
8. Which guardrails apply?
9. Which bias risks apply?
10. Which hallucination controls apply?
11. What outputs are allowed or blocked?
12. Is checkpoint/audit required?
```

## Standard output header

Every use-case output must include:

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

## Prohibited behavior

Agents must not:

```txt
use sample UCs as fixed truth
skip graph contract
skip breaker/guardrail declaration
claim official output without readiness check
write to Project Control Graph without approved write-back rule
use historical examples as current project truth
hide missing data
```

## Downgrade rule

If a use case cannot satisfy the standard:

```txt
1. Open relevant Circuit Breaker.
2. Downgrade to draft/scenario if safe.
3. Block official claims.
4. Create missing-data/recovery path.
```
