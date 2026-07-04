# DL Skill Contract Standard

Version: 0.2 draft
Scope: Planning & Financial Control Power

## Purpose

This standard defines how Planning & Financial Control Power may use DL Skills.

DL Skills are external capabilities. The Power does not own or modify DL Skill implementation.

```txt
PFC Power owns orchestration, graph, readiness, guardrails, and output authority.
DL Skills expose capability contracts only.
```

## Boundary

| Area | Owner |
|---|---|
| Use-case standard | PFC Power |
| Project Control Graph | PFC Power |
| Readiness mode | PFC Power |
| Circuit Breaker | PFC Power |
| Guardrails / fact-check | PFC Power |
| Skill capability description | DL Skill contract |
| Skill implementation prompt/files | DL Skill base |
| Skill output content | DL Skill execution, validated by PFC |

## Contract principle

```txt
A DL Skill tells PFC what it can do.
PFC decides when it is allowed to run, what context it receives, and whether its output can be trusted or written back.
```

## Required contract schema

Each DL Skill contract must define:

```md
# DL Skill Contract — <DL-ID> <Skill Name>

## Identity

- DL skill ID:
- Name:
- Category:
- Contract version:
- Skill maturity:

## Capability

What this skill can do.

## Does not do

What this skill must not be used for.

## Inputs required

Minimum input fields required to run safely.

## Optional inputs

Inputs that improve quality but are not mandatory.

## Outputs produced

Allowed output types.

## Graph interface

### Reads

Project Control Graph node types the skill may read.

### Produces draft

Node types the skill may propose.

### Never writes directly

Node types the skill must not write without PFC approval.

## PFC use cases supported

List of PFC UC IDs this contract can support.

## Required controls

### Required hooks

### Required circuit breakers

### Required guardrails

### Bias risks

### Hallucination risks

## Output quality contract

What a valid output must contain.

## Failure behavior

What to return when required inputs are missing.
```

## Graph interface rule

DL Skills do not directly own the Project Control Graph.

```txt
DL Skill output = proposal / draft / calculation / report fragment
PFC Controller = validates and decides write-back
```

## Output authority rule

A DL Skill must not claim:

```txt
approved baseline
official RAG
budget is sufficient
timeline is confirmed
resource capacity is confirmed
stakeholders agreed
```

Unless PFC provides the relevant baseline/evidence/decision context and allows that output mode.

## Required control declaration

Every DL Skill contract must declare:

```txt
required_hooks
required_breakers
required_guardrails
bias_risks
hallucination_risks
```

If a contract lacks these fields, PFC may use the skill only in draft mode.

## Contract maturity

| Contract maturity | Meaning | PFC usage allowed |
|---|---|---|
| C0 | no contract | not allowed |
| C1 | identity + capability only | draft exploratory only |
| C2 | inputs/outputs defined | draft use case support |
| C3 | graph interface + controls defined | controlled workflow support |
| C4 | tested with sample outputs | M2/M3 support with checks |
| C5 | validated in real project | production/team usage |

## Contract validation rule

PFC must validate a contract before routing to a DL Skill.

```txt
No contract -> do not call skill
Incomplete contract -> draft mode only
Graph contract missing -> no graph write-back
Controls missing -> Circuit Breaker HALF_OPEN
```
