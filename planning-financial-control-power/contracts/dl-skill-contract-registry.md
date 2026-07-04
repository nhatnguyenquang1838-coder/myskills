# DL Skill Contract Registry

Version: 0.1
Scope: Planning & Financial Control Power

## Purpose

This registry lists the external DL Skills that the Power may call as black-box capabilities.

The Power owns orchestration, graph, guardrails, circuit breaker, bias control, hallucination control, and write-back authority.

DL Skills only provide contracts for what they can do.

```txt
Power -> validates contract -> calls DL Skill -> validates result -> decides write-back/block/downgrade
```

## Registry rules

```txt
1. DL Skills do not own Project Control Graph.
2. DL Skills do not decide readiness mode.
3. DL Skills do not publish official output by themselves.
4. DL Skills return structured outputs or graph deltas.
5. PFC validates all outputs before use.
6. PFC writes approved deltas to graph only after controls pass.
```

## Contract index

| Skill ID | Contract Role | Category | Critical For | Expected Output | Write Authority | Required PFC Controls |
|---|---|---|---|---|---|---|
| DL-00-CORE-cognitive-intake-gate | classify request and missing data | CORE | Intake, baseline creation | intent, missing data, assumptions | none | readiness, hallucination check |
| DL-01-CORE-project-setup | create project skeleton | CORE | UC-00, UC-01 | draft project structure | draft_delta | graph validation |
| DL-04-CORE-document-intake | ingest source materials | CORE | UC-00A | evidence candidates, extracted facts | draft_delta | context audit, evidence breaker |
| DL-05-CORE-decision-action-risk-extractor | extract decisions/actions/risks | CORE | governance, report | DEC, action, RISK candidates | draft_delta | fact-check, evidence breaker |
| DL-10-PLAN-dependency-tracker | manage dependencies | PLAN | timeline/cascade | DEP nodes, dependency risks | draft_delta | cascade, context audit |
| DL-11-PLAN-release-milestone-planner | create/update milestones | PLAN | timeline baseline | MS nodes, milestone plan | draft_delta | evidence, cascade |
| DL-12-PLAN-resource-allocator | allocate resources | PLAN | baseline, resource planning | RA nodes, conflicts | draft_delta | resource guardrail, finance breaker |
| DL-14-FIN-budget-cost-tracking | track budget/cost | FIN | finance baseline | budget view, cost status input | draft_delta | finance breaker |
| DL-27-FIN-project-cost-calculator | calculate cost/forecast | FIN | forecast, variance | COST, FCST deltas | draft_delta | finance, evidence, derived_from check |
| DL-16-RISK-risk-register | maintain risks | RISK | reporting/change control | RISK nodes | draft_delta | evidence, bias check |
| DL-17-RISK-issue-blocker-tracker | track issues/blockers | RISK | report/cascade | issue/blocker nodes | draft_delta | context/evidence check |
| DL-18-PPL-stakeholder-map | map stakeholders | PPL | governance/report | stakeholder/owner context | draft_delta | evidence check |
| DL-19-PPL-onboarding-kt-coordinator | onboarding/KT plan | PPL | resource/governance | KT actions, owner gaps | draft_delta | decision/missing-data check |
| DL-21-RPT-executive-status-report | build executive report | RPT | executive report | report draft | none | report fact-check, circuit breaker |
| DL-22-RPT-okr-kpi-tracker | track OKR/KPI | RPT | management report | KPI status signals | draft_delta | evidence, baseline check |
| DL-26-RPT-report-builder | build final report artifact | RPT | weekly/executive report | formatted report | none | report fact-check, blocked claims check |
| DL-31-CORE-red-team-devils-advocate | challenge output | CORE | bias/quality | counter-signals, weaknesses | none | bias guardrail |
| DL-34-CORE-standalone-readiness-check | readiness scoring | CORE | mode gate | readiness score, gaps | none | baseline breaker |

## Missing contracts to define later

```txt
DL skill contracts must be promoted from registry row to full YAML contract before they are used for M3 official workflows.
```

## Minimum contract completeness for use

| Use level | Required contract completeness |
|---|---|
| Draft use | purpose + input/output + constraints |
| Scenario use | draft use + failure modes + graph nodes |
| M2 forecast use | scenario use + evidence rule + result validation |
| M3 official use | full contract + pass tests + guardrails + breakers |
