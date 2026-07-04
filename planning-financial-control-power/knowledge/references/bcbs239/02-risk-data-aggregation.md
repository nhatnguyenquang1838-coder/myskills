# BCBS 239 — Risk Data Aggregation Capabilities

Source: SRC-BCBS239-2013, Principles 3-6.

## Purpose for skills

Use this file when a skill aggregates, validates, reconciles, or transforms planning/finance/risk/reporting data.

Relevant PFC areas:

```txt
Project Control Graph
Run Context Graph
forecast calculation
resource allocation aggregation
risk aggregation
missing data handling
manual workaround control
scenario/ad hoc reporting
```

## Principle 3 — Accuracy and Integrity

Core meaning:

```txt
Risk data must be accurate, reliable, controlled, reconciled, and protected from unauthorised or inconsistent manipulation.
```

## Skill interpretation

A skill must not aggregate or calculate from unclear inputs.

It must check:

```txt
Are source nodes known?
Are calculations reproducible?
Is the data reconciled or at least source-linked?
Are manual adjustments documented?
Is derived output traceable?
```

## PFC controls

| Requirement | PFC mechanism |
|---|---|
| accurate and reliable data | evidence IDs, derived_from, fact-check |
| reconciliation | graph link validation and calculation trace |
| single authoritative source | Project Control Graph as source of truth |
| manual workaround control | assumption/manual limitation label |
| validation | fact-check, schema validation, circuit breaker |

## Principle 4 — Completeness

Core meaning:

```txt
All material data needed for risk decision-making must be captured and aggregated across relevant dimensions.
```

## Skill interpretation

A skill must not claim completeness unless the graph covers the material scope.

Check material coverage across:

```txt
work packages
milestones
dependencies
resource allocations
rate cards
cost lines
forecasts
risks
issues
decisions
evidence
```

## PFC controls

| Requirement | PFC mechanism |
|---|---|
| all material risk data included | baseline completeness check |
| exceptions identified | missing-data log |
| material omissions explained | blocked claims + limitations |
| aggregation dimensions clear | graph node categories and IDs |

## Principle 5 — Timeliness

Core meaning:

```txt
Aggregated data must be available in time to support decision-making, including under stress/crisis conditions.
```

## Skill interpretation

A skill must label whether output is timely enough for the requested decision.

Check:

```txt
as-of date
last_updated
reporting period
normal vs stress/crisis need
frequency requirement
stale data risk
```

## PFC controls

| Requirement | PFC mechanism |
|---|---|
| data currentness | `last_updated`, context audit |
| stress/ad hoc timeliness | scenario run and time-critical output mode |
| stale data handling | Context breaker |
| frequency | report metadata and recurring report policy |

## Principle 6 — Adaptability

Core meaning:

```txt
Risk data aggregation must support ad hoc, on-demand, scenario, stress, and supervisory-style requests.
```

## Skill interpretation

A skill should be able to answer bounded ad hoc questions by loading a Run Context Graph instead of scanning everything.

Examples:

```txt
impact if milestone slips
cost if rate card changes
risk view by dependency
resource view by milestone
forecast under budget cut
```

## PFC controls

| Requirement | PFC mechanism |
|---|---|
| flexible aggregation | Run Context Graph |
| scenario/ad hoc output | scenario run type |
| drill-down | graph-linked node traversal |
| new request adaptation | use-case resolver + skill contract selector |

## Guardrails

```txt
No source/derived_from -> no calculated claim
Incomplete material scope -> no completeness claim
Stale as-of date -> no current status claim
Manual adjustment -> label limitation
Scenario output -> no baseline write-back
```

## Circuit breakers

| Breaker | Opens when |
|---|---|
| Evidence breaker | aggregation/calculation lacks source or derived_from |
| Context breaker | data is stale or unlinked |
| Finance breaker | cost/forecast lacks RA/RATE/budget basis |
| Baseline breaker | completeness/baseline claim lacks required nodes |
| Contract breaker | DL Skill cannot guarantee required aggregation output |

## Skill contract requirements

Any DL Skill that aggregates data must declare:

```txt
accepted graph nodes
required input dimensions
aggregation logic or output format
produced graph deltas
confidence requirements
manual assumptions allowed
failure behavior for incomplete data
```

## Output pattern

```txt
Aggregation scope:
Data sources:
As-of date:
Completeness status:
Manual assumptions:
Derived calculations:
Missing data:
Confidence:
```
