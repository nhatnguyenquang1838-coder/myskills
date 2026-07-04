# Use Case Standard Guideline

Version: 0.2 draft
Scope: Planning & Financial Control Power

## Purpose

This document defines the standard guideline for use cases in this Power.

Use cases are not historical examples. They are reusable operating contracts that tell the Power:

```txt
what job is being performed
what input is required
which graph nodes are involved
which agents/skills/hooks execute the job
which outputs are allowed
which claims must be blocked
how to prevent bias and hallucination
```

## Relationship to readiness modes

Readiness modes and use cases are separate dimensions.

| Concept | Answers |
|---|---|
| Readiness mode | How much confidence/output authority is allowed? |
| Use case | What job is the Power performing? |

A use case can run in multiple modes, but the output authority changes by mode.

Example:

```txt
UC: Generate report
M1 -> draft report only
M2 -> forecast-based report, pending approval
M3 -> official executive report if fact-check passes
```

## Standard use-case schema

Every use case must follow this structure.

```md
# UC-XX — Use Case Name

## Purpose

## User intent examples

## Trigger conditions

## Required readiness mode

## Minimum required data

## Graph contract

### Graph nodes read

### Graph nodes written

### Draft-only nodes

### Approved write-back rules

## Execution contract

### Primary agent

### Supporting agents

### Required skills

### Required hooks

## Control contract

### Circuit breakers

### Guardrails

### Bias prevention

### Hallucination prevention

## Output contract

### Allowed outputs

### Blocked outputs

### Required output header

## Checkpoint / audit requirements

## Pass criteria

## Failure / downgrade behavior
```

## Required output header

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

## Use-case categories

All use cases must belong to one category.

| Category | Purpose |
|---|---|
| Baseline | Create, validate, upgrade, or freeze controlled baseline |
| Intake | Start from incomplete material and create graph skeleton |
| Planning | Create or change timeline, milestone, dependency, release roadmap |
| Resource | Create resource demand, allocation, capacity/conflict check |
| Finance | Create cost assumptions, forecast, variance, budget comparison |
| Reporting | Generate weekly, executive, SteerCo, decision-needed reports |
| Change Control | Assess scope/timeline/resource/cost/report impact |
| Context / Memory | Load run context, project memory, benchmark/history |
| Guardrail | Block unsupported claims, stale context, fake RAG, fake budget |

## Baseline dependency rule

Complex use cases require baseline check first.

```txt
Before running a complex UC, the Power must:
1. Check Project Control Graph exists
2. Check baseline version exists
3. Check readiness score
4. Check required node chain exists
5. Run Circuit Breaker if required data is missing
6. Downgrade to draft/scenario mode if not M3
```

## Graph-aware rule

Every UC must be graph-aware.

```txt
No graph target -> run Intake Gate or ask for target
No linked nodes -> create missing-data item
No evidence/source -> mark as assumption
No approved decision -> do not claim approval
```

## Write-back rule

Use cases may read many nodes and propose many deltas, but only approved deltas write back to the persistent Project Control Graph.

| Run type | Write behavior |
|---|---|
| Read-only | no write |
| Draft | draft delta only |
| Scenario | scenario output, no baseline write |
| Controlled update | approved graph write-back |
| Baseline freeze | checkpoint + baseline version write |

## Agent/skill/hook rule

Each UC must explicitly declare:

```txt
Primary agent
Supporting agents
Required skills
Required hooks
Manual hooks if needed
Automatic hooks if supported
```

No UC should rely on an implicit agent/skill/hook chain.

## Circuit breaker rule

Every UC must define which breaker can open.

| Breaker | Opens when |
|---|---|
| Baseline breaker | official baseline/RAG requested without controlled baseline |
| Finance breaker | budget/forecast claim requested without resource/rate/budget basis |
| Evidence breaker | date/cost/status/resource claim lacks source or assumption |
| Context breaker | stale/unlinked memory/context is used |
| Cascade breaker | changed node does not propagate to linked nodes |
| History-bias breaker | historical benchmark is used as current truth |

## Guardrail rule

Guardrails are non-negotiable constraints.

```txt
No baseline -> no official RAG
No resource + rate + budget -> no reliable forecast
No cascade check -> no report update after change
No evidence -> no confirmed claim
No decision log -> no approved commitment
History can challenge plan, not replace baseline
Memory supports graph, memory does not replace graph
```

## Bias prevention rule

Each UC must check for at least these bias risks when relevant:

| Bias | Prevention |
|---|---|
| Historical bias | label history as benchmark only |
| Stale baseline bias | current baseline version wins |
| Confirmation bias | include risks, missing data, negative evidence |
| Optimism bias | state recovery assumptions explicitly |
| Recency bias | latest file is not automatically approved truth |
| Anchoring bias | old plan does not override new baseline |

## Hallucination prevention rule

Every important claim must link to one of:

```txt
evidence_id
assumption_id
decision_id
derived_from
baseline_version
missing_data_id
```

If no link exists:

```txt
Do not state the claim as fact.
Downgrade it to assumption or missing data.
```

## Use-case readiness rule

Each UC must specify minimum mode.

| Output type | Minimum mode |
|---|---|
| skeleton / questions | M0 |
| draft plan / rough report | M1 |
| forecast / variance | M2 |
| official baseline / executive report / RAG | M3 |

## Standard pass criteria

A UC passes only if:

```txt
1. Correct mode selected
2. Correct graph nodes loaded
3. Correct agents/skills/hooks used
4. Unsupported claims blocked or downgraded
5. Bias controls applied
6. Hallucination controls applied
7. Output header is present
8. Write-back follows approval rule
9. Checkpoint/audit created when needed
```

## Standard failure behavior

If a UC cannot safely complete:

```txt
1. Open the relevant Circuit Breaker
2. State blocked claims
3. State missing data
4. Provide allowed fallback
5. Ask only critical recovery questions
6. Do not silently invent data
```

## Guideline status

This guideline is the standard. Sample files only illustrate how the standard can be applied.
