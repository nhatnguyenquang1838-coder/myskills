# UC-00 — Create Full Controlled Baseline Standard

## Purpose

Create a complete controlled baseline from project materials and validated DL Skill outputs.

This use case is foundational. Complex use cases depend on it.

## Required readiness result

Target:

```txt
M3 Controlled Baseline
```

If the input material is incomplete, downgrade to:

```txt
M1 rough planning
M2 forecast-ready
```

## Required materials

| Area | Required materials |
|---|---|
| Scope | objective, in-scope, out-of-scope, work packages, acceptance criteria |
| Timeline | milestones, target dates, dependencies, constraints |
| Resource | roles, FTE, capacity, allocation period, vendor/internal split |
| Finance | approved budget, rate card, duration, vendor/internal cost, contingency |
| Governance | evidence, assumptions, decisions, risk log, issue log, owner/approver |

## Required graph nodes

```txt
project
work_packages
milestones
dependencies
resource_allocations
rate_cards
cost_lines
forecasts
risks
assumptions
evidence
decisions
missing_data
baseline_version
```

## Agent and skill contract chain

| Step | Agent | DL Skill contract | Purpose |
|---:|---|---|---|
| 1 | pm-controller | DL-00-CORE-cognitive-intake-gate | classify request and gaps |
| 2 | pm-controller | DL-01-CORE-project-setup | create draft project structure if needed |
| 3 | pm-controller / pm-context-auditor | DL-04-CORE-document-intake | create evidence candidates from materials |
| 4 | timeline-planner | DL-11-PLAN-release-milestone-planner | create milestone baseline candidates |
| 5 | resource-planner | DL-12-PLAN-resource-allocator | create resource allocation candidates |
| 6 | finance-analyst | DL-27-FIN-project-cost-calculator | create cost lines and forecast |
| 7 | report-builder | DL-26-RPT-report-builder | create baseline report view |
| 8 | pm-controller | DL-34-CORE-standalone-readiness-check | score readiness and gate M3 |

## PFC-owned checks

```txt
Run Context Graph
Contract validation
Output validation
Graph schema validation
Cascade check
Context audit
Fact check
Bias / hallucination check
Circuit Breaker
Checkpoint
```

## Circuit breakers

| Breaker | Opens when |
|---|---|
| Contract breaker | required DL Skill contract missing or output invalid |
| Baseline breaker | M3 requested but readiness < 16/18 or required nodes missing |
| Finance breaker | cost forecast/budget status lacks RA/RATE/BUDGET basis |
| Evidence breaker | baseline claims lack source/assumption/decision/derived support |
| Context breaker | stale/unlinked context affects baseline |
| Cascade breaker | graph chain WP->MS->RA->COST->FCST is incomplete |

## Guardrails

```txt
No full node chain -> no controlled baseline
No evidence -> no confirmed baseline claim
No approved budget -> no budget baseline
No rate/resource/duration -> no reliable forecast
No decision -> no approved baseline
No validation -> no M3
```

## Output contract

UC-00 output must include:

```txt
Mode:
Run type:
Use case: UC-00 Create Full Controlled Baseline
Contracts used:
Skills called:
Graph nodes read:
Graph deltas proposed:
Graph nodes written:
Readiness score:
Circuit breaker state:
Allowed output:
Blocked claims:
Missing data:
Next action:
```

## Write-back rule

```txt
All DL Skill outputs are draft deltas.
Only PFC Controller writes approved deltas to Project Control Graph.
Baseline version is written only when gate passes and user approves.
```

## Pass criteria

```txt
[ ] required materials mapped or missing data logged
[ ] required graph nodes created or missing data logged
[ ] P0 DL Skill contracts pass validation
[ ] graph schema validation passes
[ ] readiness score >= 16/18 for M3
[ ] fact-check passes
[ ] circuit breaker CLOSED
[ ] baseline checkpoint created
```

## Failure behavior

If UC-00 cannot create controlled baseline:

```txt
1. Open relevant breaker.
2. Downgrade to M1/M2 if safe.
3. Create missing-data log.
4. Block official baseline/RAG/budget claims.
5. Return recovery questions.
```
