# Planning & Financial Control Power

Version: `0.1.0`
Status: first usable design skeleton

This Kiro Power coordinates planning, resource allocation, cost calculation, reporting, intake/onboarding, context loading, historical data usage, and anti-hallucination controls.

## Core model

The Power does not manage Planning and Finance as disconnected documents. It uses one linked **Project Control Graph**.

```txt
Work Package -> Milestone -> Resource Allocation -> Cost Line -> Forecast -> Report
       \             \              \                  \            \
      Evidence      Assumption      Decision           Risk        Change Request
```

## Main components

```txt
POWER.md
steering/      rules and interaction policy
skills/        task processors
agents/        role definitions
templates/     workspace starter files
hooks/         consistency checks
knowledge/     reusable PM methods and patterns
tests/         readiness and scenario tests
```

## Operating modes

| Mode | Meaning | Allowed output |
|---|---|---|
| M0 | Empty Start | Skeleton, intake questions, assumptions, missing-data log |
| M1 | Rough Planning | Draft timeline, rough resource demand, draft report |
| M2 | Forecast Ready | Cost forecast, variance, planning-finance impact |
| M3 | Controlled Baseline | RAG, executive report, baseline variance, change control |

## Non-negotiable rules

```txt
No baseline -> no official RAG
No rate/resource data -> no reliable cost forecast
No evidence -> mark as assumption
No link -> no claim
History can challenge the plan, not replace the baseline
```

## MVP install target

Copy these into a target workspace:

```txt
.kiro/steering/
.kiro/skills/
.kiro/agents/
.kiro/hooks/
.pm/control/project-control.yaml
.pm/intake/project-intake.yaml
.pm/audit/readiness-score.md
```

## First-version readiness target

This version targets **3.0–3.5 / 5** readiness: enough to start implementation and scenario testing, not yet distribution-ready.
