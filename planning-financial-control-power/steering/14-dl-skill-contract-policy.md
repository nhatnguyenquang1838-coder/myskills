# 14 — DL Skill Contract Policy

## Purpose

Define how Planning & Financial Control Power routes work to DL Skills.

## Boundary

```txt
PFC Power owns control.
DL Skills expose capability contracts.
PFC does not modify or depend on DL Skill implementation details.
```

## Authoritative contract files

```txt
knowledge/contracts/dl-skill-contract-standard.md
knowledge/contracts/pfc-required-dl-skill-contracts.md
templates/dl-skill-contract.md
```

## Routing rule

Before routing to a DL Skill, PM Controller must check:

```txt
1. Does a DL Skill contract exist?
2. Does the contract support the current PFC use case?
3. Does the contract define required inputs?
4. Does the contract define graph reads/proposed writes?
5. Does the contract declare required hooks?
6. Does the contract declare required circuit breakers?
7. Does the contract declare guardrails, bias risks, and hallucination risks?
8. Is the contract maturity sufficient for the requested output authority?
```

## Contract maturity usage

| Contract maturity | PFC usage |
|---|---|
| C0 | do not call |
| C1 | exploratory only |
| C2 | draft/scenario only |
| C3 | controlled workflow with checks |
| C4 | M2/M3 support with checks |
| C5 | production/team use |

## Write-back rule

DL Skills must not directly write approved graph state.

```txt
DL Skill output -> PFC validation -> approved/draft/scenario write decision
```

Only PM Controller may write approved deltas to:

```txt
.pm/control/project-control.yaml
```

## Output authority rule

DL Skill output is not automatically trusted.

PFC must run:

```txt
context-audit
cascade-impact-check if graph-linked change exists
fact-check
circuit-breaker
```

before official output or graph write-back.

## Failure behavior

If the required DL contract is missing or incomplete:

```txt
1. Do not call the DL Skill for controlled workflow.
2. Downgrade to draft/scenario if safe.
3. Open Circuit Breaker HALF_OPEN or OPEN.
4. Create missing contract item.
5. Ask for contract completion only if critical.
```

## Prohibited behavior

PFC agents must not:

```txt
copy DL Skill implementation into PFC
assume a DL Skill can do something not in its contract
let a DL Skill declare official RAG/status by itself
let a DL Skill write baseline directly
use sample output as contract
use historical DL behavior as current contract
```
