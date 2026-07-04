# Planning & Financial Control Power — Decisions

## DEC-001 — Power owns orchestration and control

Decision:

```txt
PFC Power owns orchestration, graph, readiness mode, validation, guardrails, circuit breaker, and write-back.
```

Rationale:

```txt
DL Skills are external black-box capabilities. They should not own PFC state or baseline authority.
```

Impact:

```txt
All DL Skill usage must go through contract validation and output validation.
```

## DEC-002 — DL Skills are contracts only

Decision:

```txt
DL Skills expose what they can do through contracts.
PFC does not copy DL Skill implementation.
```

Impact:

```txt
Create and maintain `contracts/` and `schemas/dl-skill-contract.schema.json`.
```

## DEC-003 — Use cases are standards, samples are examples

Decision:

```txt
Use-case standard guideline is authoritative.
Use-case samples illustrate behavior but do not define the standard.
```

Impact:

```txt
Agents must load `knowledge/use-cases/use-case-standard-guideline.md` as authority.
```

## DEC-004 — One persistent graph, one run graph per run

Decision:

```txt
A workspace has one persistent Project Control Graph.
Every meaningful run builds a temporary Run Context Graph.
```

Impact:

```txt
Avoid uncontrolled graph drift.
Only approved deltas write back.
```

## DEC-005 — Complex use cases require baseline gate

Decision:

```txt
Complex UCs must check baseline completeness before official output.
```

Impact:

```txt
If M3 baseline is absent, complex UC downgrades to draft/scenario or blocks official claims.
```

## DEC-006 — Circuit Breaker blocks fake confidence

Decision:

```txt
Circuit Breaker should block unsupported official claims, not block all useful draft work.
```

Impact:

```txt
HALF_OPEN state allows draft/scenario output with limitations.
OPEN state blocks official claims.
```

## DEC-007 — BCBS239 is used as control reference, not raw legal compliance engine

Decision:

```txt
BCBS239 principles and progress lessons are converted into PFC guardrails, report quality rules, and contract guidance.
```

Impact:

```txt
The Power uses BCBS239 for governance/reporting/data-quality discipline but does not claim regulatory compliance by default.
```

## DEC-008 — Hooks are templates until schema verified

Decision:

```txt
Kiro hook files remain templates until exact hook schema is verified.
```

Impact:

```txt
Do not mark hook execution production-ready in v0.2 unless verified.
```
