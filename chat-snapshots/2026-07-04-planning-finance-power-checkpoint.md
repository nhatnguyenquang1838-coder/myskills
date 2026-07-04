# Chat Snapshot — Planning & Financial Control Power

Date: 2026-07-04
Repo: `nhatnguyenquang1838-coder/myskills`
Purpose: checkpoint the design discussion for a Kiro Power that coordinates planning, resource allocation, cost calculation, reporting, context loading, onboarding, and anti-hallucination controls.

---

## 1. Problem statement

The user is building a reusable Kiro-based PM skill/power system. The focus of this checkpoint is the **Planning & Financial Control Power**.

Core issue identified during the conversation:

> Planning, resource allocation, finance, historical context, reports, steering, hooks, and onboarding were being designed as separate files/modules, but they were not strongly linked together.

The corrected direction is:

> Use one connected Project Control Graph as the source of truth. Skills do not own independent truth; they read/write linked graph nodes.

---

## 2. Final concept

The Planning & Financial Control Power coordinates four primary skills:

1. `timeline-planning`
2. `resource-planning-allocation`
3. `cost-calculator`
4. `report-builder`

These skills are coordinated by a controller and operate on one shared graph:

```txt
Scope / Work Package
  -> Timeline / Milestone
    -> Resource Allocation
      -> Cost Line
        -> Forecast
          -> Report
```

Every important node should link to:

```txt
Evidence
Assumption
Decision
Risk
Change Request
Baseline Version
```

Core rule:

```txt
No link -> no claim
No evidence -> mark as assumption
No baseline -> no official RAG
No rate/resource data -> no reliable cost forecast
```

---

## 3. Power architecture

```txt
Planning & Financial Control Power
│
├── Power Controller
│   ├── decides workflow
│   ├── routes to skills
│   ├── runs cascade check
│   └── blocks unsupported output
│
├── Four Skills
│   ├── timeline-planning
│   ├── resource-planning-allocation
│   ├── cost-calculator
│   └── report-builder
│
├── Project Control Graph
│   └── single source of truth
│
├── Intake Gate / Onboarding Wizard
│   ├── detects missing materials
│   ├── scores readiness
│   ├── selects mode
│   └── creates graph skeleton
│
├── Context Loader
│   └── loads only linked graph nodes needed for the task
│
├── Fact / Bias Control
│   ├── evidence check
│   ├── assumption check
│   ├── stale baseline check
│   └── historical bias check
│
└── Hooks
    ├── after timeline change
    ├── after resource change
    ├── after cost change
    └── before report publish
```

---

## 4. Project Control Graph

MVP starts with one file:

```txt
.pm/control/project-control.yaml
```

Do not begin with many disconnected files. Start with one linked control model and split later only if needed.

Example graph structure:

```yaml
project:
  id: PRJ-001
  name: Example Project
  baseline_version: BL-001
  readiness_mode: M1
  baseline_status: draft

work_packages:
  - id: WP-001
    name: Build Invoice UI
    scope_status: approved
    evidence_ids: [EVD-001]
    assumption_ids: []
    risk_ids: [RISK-001]

milestones:
  - id: MS-001
    name: Invoice UI Done
    work_package_ids: [WP-001]
    start_date: 2026-07-01
    end_date: 2026-07-15
    dependency_ids: [DEP-001]
    status: planned
    confidence: medium
    evidence_ids: [EVD-002]

resource_allocations:
  - id: RA-001
    work_package_id: WP-001
    milestone_id: MS-001
    role: Frontend Developer
    fte: 1.0
    start_date: 2026-07-01
    end_date: 2026-07-15
    rate_card_id: RATE-001
    evidence_ids: [EVD-003]

rate_cards:
  - id: RATE-001
    role: Frontend Developer
    monthly_rate: 5000
    currency: USD
    source: vendor contract
    evidence_ids: [EVD-004]

cost_lines:
  - id: COST-001
    resource_allocation_id: RA-001
    work_package_id: WP-001
    formula: fte * monthly_rate * duration_months
    amount: 2500
    currency: USD
    derived_from: [RA-001, RATE-001]

forecasts:
  - id: FCST-001
    baseline_budget: 10000
    forecast_amount: 2500
    variance: -7500
    status: green
    cost_line_ids: [COST-001]

reports:
  - id: RPT-001
    type: weekly
    timeline_status: amber
    resource_status: green
    budget_status: green
    overall_status: amber
    source_ids: [MS-001, RA-001, FCST-001, RISK-001]
```

---

## 5. Skill responsibilities

### 5.1 `timeline-planning`

Reads:

```txt
work_packages
dependencies
milestones
risks
decisions
assumptions
baseline_version
```

Writes:

```txt
milestones
dependencies
timeline impact
change_requests
```

Must not:

```txt
Do not create budget conclusion.
Do not say cost is fine.
Only create timeline impact signals.
```

---

### 5.2 `resource-planning-allocation`

Reads:

```txt
work_packages
milestones
dependencies
resource_allocations
capacity
risks
```

Writes:

```txt
resource_allocations
resource_conflicts
capacity risks
```

Must not:

```txt
Do not approve timeline.
Do not approve cost.
Only say whether allocation supports the timeline.
```

---

### 5.3 `cost-calculator`

Reads:

```txt
resource_allocations
rate_cards
cost_lines
forecast
budget
vendor contracts
assumptions
```

Writes:

```txt
cost_lines
forecast
budget variance
financial impact
```

Must not:

```txt
Do not set overall project status alone.
Do not override approved budget.
Only calculate financial impact.
```

---

### 5.4 `report-builder`

Reads:

```txt
milestones
resource_allocations
forecast
risks
decisions
assumptions
evidence
change_requests
```

Writes:

```txt
reports
executive summary
weekly status
decisions needed
```

Must not:

```txt
Do not invent status.
Do not use old history as current fact.
Do not make unsupported claims.
```

---

## 6. Cascade engine

Every change runs graph traversal.

```txt
Changed node -> find linked nodes -> run required skills -> update report
```

Example: milestone changed

```txt
MS-001 changed
  -> linked WP-001
  -> linked RA-001
  -> linked COST-001
  -> linked FCST-001
  -> linked RPT-001
```

Then controller runs:

```txt
timeline-planning
-> resource-planning-allocation
-> cost-calculator
-> report-builder
-> fact-checker
```

Cascade matrix:

| Changed item | Must check |
|---|---|
| Work package | Timeline, resource, cost, report |
| Milestone | Resource, cost, report |
| Dependency | Timeline, risk, report |
| Resource allocation | Timeline feasibility, cost, report |
| Rate card | Cost, forecast, report |
| Budget | Forecast, RAG, report |
| Risk | Timeline/resource/cost if linked, report |
| Decision | Any linked node |
| Assumption | Any dependent calculation/report |

---

## 7. Context loading

Bad model:

```txt
Load planning folder
Load finance folder
Load history folder
Load reports folder
```

Correct model:

```txt
User asks about WP-001
-> load WP-001
-> load linked MS
-> load linked RA
-> load linked COST
-> load linked FCST
-> load linked RISK
-> load linked EVD/ASM/DEC
```

Context loader algorithm:

```txt
1. Identify target object.
2. Load current baseline.
3. Load directly linked graph nodes.
4. Load second-level linked nodes only if needed.
5. Load historical data only as benchmark.
6. Reject stale/unlinked context.
7. Produce answer with source IDs.
```

---

## 8. Historical data and bias control

History is separate:

```txt
.pm/history/history-index.yaml
```

History can link to current graph only as:

```txt
benchmark
risk signal
lesson learned
scenario input
```

Never as current truth.

Rule:

```txt
History can challenge the plan.
History cannot replace the baseline.
```

Bias controls:

| Bias | Prevention |
|---|---|
| Anchoring on old plan | Current baseline version wins |
| Recency bias | Latest file is not automatically true |
| Historical bias | History only benchmark, not fact |
| Confirmation bias | Require counter-signal check |
| Overconfidence | Every claim has confidence |
| Stale data | Every node has baseline version/date |

---

## 9. Intake Gate and Onboarding

Most users will not have enough materials. The Power must support progressive onboarding.

Operating modes:

| Mode | When | Allowed output |
|---|---|---|
| M0 Empty Start | User has only idea/project name | Skeleton, questions, assumptions, missing-data log |
| M1 Rough Planning | Scope/timeline rough, finance incomplete | Draft timeline, rough resource demand, draft report |
| M2 Forecast Ready | Resource/rate/budget minimally available | Forecast, variance, planning-finance impact |
| M3 Controlled Baseline | Approved baseline/evidence/decision log exists | RAG, executive report, change control, variance |

Core gate rules:

```txt
No baseline -> no official RAG
No rate card -> no cost forecast, only cost assumption
No resource allocation -> no reliable budget
No evidence -> claim must be marked assumption
```

Readiness score dimensions:

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Scope | none | rough idea | work packages | approved scope |
| Timeline | none | target date | milestone plan | approved baseline |
| Resource | none | rough team | allocation plan | confirmed capacity |
| Finance | none | rough budget | rate + forecast | approved budget |
| Evidence | none | verbal/context | document source | approved evidence |
| Decisions | none | pending | recorded | approved |

Mode selection:

```txt
0–5    -> M0 Empty Start
6–10   -> M1 Rough Planning
11–15  -> M2 Forecast Ready
16–18  -> M3 Controlled Baseline
```

---

## 10. Interaction steering

A dedicated steering layer is required to control how the Power talks to users when material is incomplete.

Recommended files:

```txt
planning-financial-control-power/steering/
├── interaction-policy.md
├── intake-gate-policy.md
├── question-policy.md
├── output-mode-policy.md
├── missing-data-policy.md
└── confidence-language-policy.md
```

### Interaction policy

```txt
1. Do not ask for all material at once.
2. Ask only missing critical information required for the current intent.
3. Accept unknown as a valid answer.
4. If data is missing, continue in assumption mode.
5. Always label output mode: M0/M1/M2/M3.
6. Never present draft/assumption output as official baseline.
7. Always separate confirmed facts, assumptions, missing data, and decisions needed.
8. Do not block useful progress unless missing data makes the requested output unsafe or misleading.
```

### Question policy

```txt
Maximum questions per turn: 5.

Ask questions only when:
1. The answer changes the workflow path.
2. The missing data blocks the requested output.
3. The missing data affects timeline, resource, cost, or report confidence.
```

Priority questions:

```txt
1. Project name / objective
2. Target date or time constraint
3. Work packages / scope
4. Resource availability
5. Budget / rate / cost assumption
```

---

## 11. Minimum file structure

Workspace MVP:

```txt
.pm/
├── control/
│   └── project-control.yaml
│
├── reports/
│   └── weekly-status.md
│
├── history/
│   └── history-index.yaml
│
└── audit/
    ├── context-retrieval-log.md
    ├── cascade-check-log.md
    ├── fact-check-log.md
    ├── missing-data-log.md
    └── readiness-score.md
```

Power package:

```txt
planning-financial-control-power/
├── POWER.md
├── steering/
│   ├── project-control-graph.md
│   ├── cascade-rules.md
│   ├── context-loading-policy.md
│   ├── evidence-policy.md
│   ├── bias-control.md
│   ├── interaction-policy.md
│   ├── intake-gate-policy.md
│   ├── question-policy.md
│   ├── output-mode-policy.md
│   ├── missing-data-policy.md
│   └── confidence-language-policy.md
│
├── skills/
│   ├── timeline-planning/SKILL.md
│   ├── resource-planning-allocation/SKILL.md
│   ├── cost-calculator/SKILL.md
│   └── report-builder/SKILL.md
│
├── agents/
│   ├── pm-controller.md
│   ├── timeline-planner.md
│   ├── resource-planner.md
│   ├── finance-analyst.md
│   ├── report-builder.md
│   ├── pm-fact-checker.md
│   └── pm-context-auditor.md
│
└── hooks/
    ├── cascade-check.json
    ├── context-audit.json
    ├── report-fact-check.json
    ├── intake-completeness-check.json
    └── baseline-upgrade-check.json
```

---

## 12. Final operating flow

### New plan

```txt
User: create plan for MVP2

pm-controller
-> intake gate
-> readiness score
-> create graph skeleton
-> timeline-planning creates milestones
-> resource-planning maps allocation
-> cost-calculator creates forecast only if data allows
-> report-builder creates summary
-> fact-checker validates links
-> save project-control.yaml
```

### Timeline change

```txt
User: MVP2 delayed by 2 weeks

pm-controller
-> update MS node
-> traverse linked RA/COST/FCST/RPT
-> resource-planning checks extension
-> cost-calculator recalculates cost
-> report-builder updates RAG if allowed by mode
-> fact-checker validates
```

### Budget change

```txt
User: budget cut by 20%

pm-controller
-> update budget node
-> cost-calculator recalculates variance
-> resource-planning checks feasible reduction
-> timeline-planning checks scope/date impact
-> report-builder creates decision options
```

### Weekly report

```txt
User: build weekly report

pm-controller
-> load current graph
-> reject stale historical data
-> report-builder drafts
-> fact-checker verifies every claim
-> output weekly-status.md
```

---

## 13. Key final decisions

1. Use **one combined Planning & Financial Control Power**, not separate planning and finance powers.
2. Use **Project Control Graph** as the single source of truth.
3. Start with **one YAML graph file** to avoid drift.
4. Keep historical data outside the main graph; use it only as benchmark/risk signal.
5. Add **Intake Gate + Onboarding** because users may lack materials.
6. Add **Interaction Steering** so the Power asks minimally, proceeds honestly, and labels confidence.
7. Every report/date/number/RAG/status must link to evidence, assumption, decision, derived calculation, or baseline.
8. The Power should help users start with incomplete data, but must not pretend incomplete data is complete.

Final principle:

```txt
Start useful, stay honest, upgrade confidence only when evidence improves.
```
