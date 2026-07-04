# PFC Required DL Skill Contracts

Version: 0.2 draft
Scope: Planning & Financial Control Power

## Purpose

This document lists the DL Skill contracts required by the Planning & Financial Control Power.

The Power does not copy or own these skills. It only requires contracts that describe what each DL Skill can safely do.

## Contract dependency model

```txt
PFC Use Case
-> required capability
-> required DL Skill contract
-> PFC controller routes execution
-> PFC validates output before write-back
```

## Critical contracts for PFC baseline creation

| Required contract | Capability needed by PFC | PFC use cases | Minimum contract maturity |
|---|---|---|---|
| `DL-00-CORE-cognitive-intake-gate` | classify request, detect missing data, select initial mode | UC-00, UC-01, UC-02, UC-04 | C3 |
| `DL-01-CORE-project-setup` | create project skeleton and initial structure | UC-00, UC-01, UC-02 | C3 |
| `DL-04-CORE-document-intake` | extract structured facts from materials | UC-00, UC-00A, UC-03 | C3 |
| `DL-10-PLAN-dependency-tracker` | create/check dependency nodes and dependency risks | UC-00, UC-05, UC-07, UC-24 | C3 |
| `DL-11-PLAN-release-milestone-planner` | build milestone/release plan | UC-00, UC-05, UC-06, UC-08, UC-22 | C3 |
| `DL-12-PLAN-resource-allocator` | create resource demand/allocation and capacity signal | UC-00, UC-09, UC-10, UC-11, UC-12 | C3 |
| `DL-14-FIN-budget-cost-tracking` | track budget, forecast, variance | UC-00, UC-14, UC-15, UC-17 | C3 |
| `DL-27-FIN-project-cost-calculator` | calculate cost lines and forecast from resource/rate/duration | UC-00, UC-13, UC-14, UC-15, UC-16, UC-17 | C3 |
| `DL-16-RISK-risk-register` | create risk nodes and risk status | UC-00, UC-07, UC-21, UC-22, UC-23, UC-24 | C3 |
| `DL-17-RISK-issue-blocker-tracker` | create blocker/issue nodes and escalation signals | UC-21, UC-22, UC-24, UC-33 | C3 |
| `DL-21-RPT-executive-status-report` | produce executive report structure | UC-19, UC-20 | C3 |
| `DL-26-RPT-report-builder` | assemble report from graph-backed sections | UC-18, UC-19, UC-20, UC-21, UC-22, UC-23 | C3 |
| `DL-31-CORE-red-team-devils-advocate` | counter-signal and bias review | UC-19, UC-28, UC-30, UC-32, UC-34 | C2 |
| `DL-34-CORE-standalone-readiness-check` | readiness scoring and baseline gate support | UC-00, UC-00B, UC-00C, UC-04, UC-19 | C3 |

## Optional but useful contracts

| Optional contract | Capability | PFC use cases |
|---|---|---|
| `DL-18-PPL-stakeholder-map` | stakeholder/owner map | UC-20, UC-21, UC-25 |
| `DL-19-PPL-onboarding-kt-coordinator` | onboarding/KT dependency context | UC-00, UC-12, UC-21 |
| `DL-22-RPT-okr-kpi-tracker` | KPI/OKR status | UC-19, UC-20 |
| `DL-23-RPT-retrospective-facilitator` | lessons learned and retrospective notes | UC-28, UC-29 |
| `DL-33-TOOL-confluence-publisher` | publish approved output to Confluence | UC-18, UC-19, UC-20 |
| `DL-08-CORE-token-saving-rules` | token/context discipline | all large-context use cases |

## Minimum contract fields required by PFC

Every required contract must include:

```txt
identity
capability
does_not_do
inputs_required
outputs_produced
graph_reads
graph_produces_draft
graph_never_writes_directly
pfc_use_cases_supported
required_hooks
required_breakers
required_guardrails
bias_risks
hallucination_risks
failure_behavior
```

## Contract enforcement

PFC Controller must enforce:

```txt
No DL contract -> do not route to DL Skill
C1-C2 contract -> draft/scenario only
C3+ contract -> controlled workflow support with checks
No graph interface -> no graph write-back
No guardrail declaration -> Circuit Breaker HALF_OPEN
```

## Important boundary

```txt
This document does not define DL Skill implementation.
It defines what PFC requires from DL Skill contracts.
```
