# 14 — DL Skill Contract Policy

## Purpose

Define how the Planning & Financial Control Power interacts with external DL Skills.

## Core rule

```txt
DL Skills are black boxes with contracts.
The Power owns orchestration, graph, validation, guardrails, circuit breaker, and write-back.
```

## Boundary

```txt
PFC Power owns control.
DL Skills expose capability contracts.
PFC does not modify or depend on DL Skill implementation details.
```

## Authoritative contract files

```txt
contracts/dl-skill-contract-schema.yaml
contracts/dl-skill-contract-registry.md
contracts/dl-skill-contract-examples.md
schemas/dl-skill-contract.schema.json
```

Samples and historical behavior must not be treated as contracts.

## Dependency direction

```txt
Power -> DL Skill contracts
DL Skills must not depend on Power internals
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

## Required behavior before calling a DL Skill

```txt
1. Find the skill contract in the registry.
2. Check supported use cases.
3. Check required inputs.
4. Check accepted graph nodes.
5. Check preconditions.
6. Check readiness mode compatibility.
7. Prepare a Run Context Graph package.
8. Declare expected outputs.
```

## Required behavior after calling a DL Skill

```txt
1. Validate required outputs exist.
2. Validate output format.
3. Validate produced graph delta node types.
4. Validate no authority boundary was crossed.
5. Validate evidence/assumption/decision/derived support.
6. Run circuit breaker if validation fails.
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

## Write-back authority values

| Contract value | Meaning |
|---|---|
| none | skill only produces text/view, no graph delta |
| draft_delta | skill may propose graph delta |
| approved_delta_only | Power may write delta only after validation and approval |

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

## Contract breaker

Open Contract breaker when:

```txt
- contract missing
- preconditions fail
- required output missing
- unauthorized graph delta returned
- skill makes prohibited claim
- output cannot be validated
```

## Failure behavior

If the required DL contract is missing or incomplete:

```txt
1. Do not call the DL Skill for controlled workflow.
2. Downgrade to draft/scenario if safe.
3. Open Circuit Breaker HALF_OPEN or OPEN.
4. Create missing contract item.
5. Ask for contract completion only if critical.
```

If a contract fails after execution:

```txt
1. Do not use the output as fact.
2. Return contract failure reason.
3. Create missing-data or skill-gap item.
4. Downgrade use case if possible.
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
use history as current truth
accept output that exceeds contract constraints
```
