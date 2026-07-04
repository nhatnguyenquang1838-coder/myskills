# 09 — Template Policy

## Purpose

Standardize outputs so project plans, forecasts, and reports remain consistent and auditable.

## Universal output header

```md
## Output Control

Mode:
Confidence:
Allowed use:
Blocked claims:
Source graph nodes:
Evidence used:
Assumptions:
Missing data:
Decisions needed:
```

## Template requirements

Every template must include:

```txt
source graph nodes
confidence
evidence
assumptions
missing data
owner/action/decision where relevant
```

## Report template rule

Report Builder must not write free-form status before validating:

```txt
timeline_status
resource_status
budget_status
risk_status
overall_status
source_ids
```

## Change-impact template rule

Every change impact must show:

```txt
changed node
affected nodes
skill cascade
cost impact
resource impact
timeline impact
report impact
missing data
```
