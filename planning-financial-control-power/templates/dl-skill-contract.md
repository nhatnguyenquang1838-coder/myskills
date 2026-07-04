# DL Skill Contract — <DL-ID> <Skill Name>

## Identity

| Field | Value |
|---|---|
| DL skill ID |  |
| Name |  |
| Category | CORE / PLAN / FIN / RISK / PPL / RPT / TOOL |
| Contract version | 0.1 |
| Skill maturity | Detailed / Functional / Scaffold / Missing |
| Contract maturity | C0 / C1 / C2 / C3 / C4 / C5 |

## Capability

This skill can:

```txt
- 
```

## Does not do

This skill must not be used to:

```txt
- approve baseline
- set official RAG by itself
- write directly to Project Control Graph
- claim stakeholder approval without decision evidence
```

## Inputs required

| Input | Required? | Description | Missing behavior |
|---|---:|---|---|
|  | Yes |  | Create missing-data item |

## Optional inputs

| Input | Description | Benefit |
|---|---|---|
|  |  |  |

## Outputs produced

| Output | Type | Can support official output? | Notes |
|---|---|---:|---|
|  | draft/proposal/calculation/report_fragment | No | PFC validates before official use |

## Graph interface

### Reads

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
issues
assumptions
evidence
decisions
reports
```

### Produces draft

```txt
<node types this skill can propose>
```

### Never writes directly

```txt
baseline_version
approved_status
official_RAG
controlled_forecast
```

## PFC use cases supported

| UC ID | Role in UC | Minimum readiness mode |
|---|---|---|
|  |  |  |

## Required controls

### Required hooks

```txt
intake-completeness-check
context-audit
cascade-check
report-fact-check
baseline-upgrade-check
circuit-breaker-check
```

### Required circuit breakers

```txt
Baseline breaker
Finance breaker
Evidence breaker
Context breaker
Cascade breaker
History-bias breaker
```

### Required guardrails

```txt
- 
```

### Bias risks

```txt
- historical bias
- stale baseline bias
- confirmation bias
- optimism bias
- recency bias
- anchoring bias
```

### Hallucination risks

```txt
- unsupported date claim
- unsupported budget claim
- unsupported RAG claim
- unsupported resource capacity claim
- unsupported approval claim
```

## Output quality contract

A valid output must include:

```txt
Inputs used:
Graph nodes read:
Draft nodes proposed:
Evidence used:
Assumptions used:
Missing data:
Confidence:
Limitations:
```

## Failure behavior

If required input is missing:

```txt
1. Do not invent it.
2. Return missing-data item.
3. State what output is blocked.
4. Provide draft fallback if safe.
```
