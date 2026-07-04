# Use Case Control Catalog

Version: 0.2 draft
Scope: Planning & Financial Control Power

## Purpose

This catalog maps each use case to the execution mechanism:

```txt
User intent
-> PM Controller
-> Readiness mode
-> Run Context Graph
-> Agent / Skill combination
-> Hooks
-> Circuit Breaker
-> Guardrails
-> Bias / hallucination prevention
-> Output / write-back rule
```

## Global execution rule

```txt
Every use case must be graph-aware.
Only approved deltas write back to the persistent Project Control Graph.
```

## Global control components

| Component | Role |
|---|---|
| PM Controller agent | Orchestrates intent, graph loading, routing, checks, and output mode |
| Memory Context Controller skill | Loads linked memory/context and checks staleness/conflict |
| Context Audit skill | Validates loaded context is linked, current, and not biased |
| Fact Check skill | Validates all claims have evidence/assumption/decision/derived/baseline support |
| Circuit Breaker skill | Blocks or downgrades unsupported official claims |
| Cascade Impact Check skill | Ensures linked graph nodes are checked after any change |

---

# A. Foundational / Baseline Use Cases

## UC-00 — Create Full Controlled Baseline

| Field | Detail |
|---|---|
| Purpose | Convert full materials into M3 Controlled Baseline |
| Mode | Target M3; downgrade to M1/M2 if incomplete |
| Primary agent | `pm-controller` |
| Supporting agents | `timeline-planner`, `resource-planner`, `finance-analyst`, `pm-fact-checker`, `pm-context-auditor` |
| Skills | `intake-gate`, `timeline-planning`, `resource-planning-allocation`, `cost-calculator`, `cascade-impact-check`, `context-audit`, `fact-check`, `circuit-breaker` |
| Hooks | `intake-completeness-check`, `cascade-check`, `context-audit`, `report-fact-check`, `baseline-upgrade-check`, `circuit-breaker-check` |
| Graph reads | source docs/materials, existing graph if present |
| Graph writes | `project`, `work_packages`, `milestones`, `dependencies`, `resource_allocations`, `rate_cards`, `cost_lines`, `forecasts`, `evidence`, `risks`, `decisions`, `assumptions`, `baseline_version` |
| Circuit breaker | Baseline breaker, Finance breaker, Evidence breaker, Context breaker |
| Guardrails | No M3 if score < 16/18; no official RAG without approved baseline; no forecast without resource/rate/budget |
| Bias prevention | Do not let old project/history fill missing baseline fields; mark all inferred values as assumptions |
| Hallucination prevention | Every node must have `source_ids`, `assumption_ids`, `decision_ids`, or `derived_from` |
| Output | `project-control.yaml`, baseline checkpoint, readiness score, missing-data log |

## UC-00A — Import Materials to Graph

| Field | Detail |
|---|---|
| Purpose | Convert docs/sheets/Jira/export into candidate graph nodes |
| Mode | M0-M2, may support M3 after validation |
| Primary agent | `pm-controller` |
| Supporting agents | `pm-context-auditor`, `pm-fact-checker` |
| Skills | `intake-gate`, `memory-context-controller`, `context-audit`, `fact-check` |
| Hooks | `context-audit`, `circuit-breaker-check` |
| Graph reads | uploaded/linked material, existing graph |
| Graph writes | candidate evidence, assumptions, missing data, draft nodes |
| Circuit breaker | Context breaker, Evidence breaker |
| Guardrails | Imported material is not automatically approved baseline |
| Bias prevention | Latest file is not automatically correct; status must be checked |
| Hallucination prevention | Source extraction must create evidence IDs before claims are generated |
| Output | evidence ledger candidates, draft graph nodes, missing-data log |

## UC-00B — Validate Baseline Completeness

| Field | Detail |
|---|---|
| Purpose | Check if graph can support M3 complex use cases |
| Mode | All modes |
| Primary agent | `pm-controller` |
| Supporting agents | `pm-fact-checker`, `pm-context-auditor` |
| Skills | `intake-gate`, `fact-check`, `context-audit`, `circuit-breaker` |
| Hooks | `baseline-upgrade-check`, `circuit-breaker-check` |
| Graph reads | all baseline-required node groups |
| Graph writes | readiness score, missing-data log, blocked claims |
| Circuit breaker | Baseline breaker, Evidence breaker, Finance breaker |
| Guardrails | Score must be >= 16/18 for M3 |
| Bias prevention | Historical or draft data cannot count as approved evidence unless explicitly approved |
| Hallucination prevention | Missing field creates `MD-*`; never filled silently |
| Output | M0/M1/M2/M3 decision, blocked-output list |

## UC-00C — Upgrade Draft Graph to Baseline

| Field | Detail |
|---|---|
| Purpose | Promote draft M1/M2 graph to M3 baseline |
| Mode | M1/M2 -> M3 |
| Primary agent | `pm-controller` |
| Supporting agents | `pm-fact-checker`, `finance-analyst`, `timeline-planner`, `resource-planner` |
| Skills | `cascade-impact-check`, `fact-check`, `cost-calculator`, `circuit-breaker` |
| Hooks | `baseline-upgrade-check`, `cascade-check`, `report-fact-check` |
| Graph reads | draft graph, evidence, decisions, assumptions |
| Graph writes | `baseline_version`, controlled baseline status, checkpoint |
| Circuit breaker | Baseline breaker opens if approvals/evidence missing |
| Guardrails | No baseline upgrade without decision/evidence links |
| Bias prevention | Assumptions must remain assumptions unless approved |
| Hallucination prevention | Baseline status requires source-backed nodes |
| Output | `BL-001` checkpoint or blocked upgrade report |

## UC-00D — Freeze Baseline Version

| Field | Detail |
|---|---|
| Purpose | Create immutable baseline checkpoint |
| Mode | M3 |
| Primary agent | `pm-controller` |
| Supporting agents | `pm-fact-checker` |
| Skills | `fact-check`, `circuit-breaker` |
| Hooks | `baseline-upgrade-check`, `circuit-breaker-check` |
| Graph reads | approved graph nodes |
| Graph writes | baseline checkpoint, version metadata |
| Circuit breaker | Evidence breaker, Baseline breaker |
| Guardrails | Freeze only if all critical nodes are supported |
| Bias prevention | Do not include stale or historical nodes as current baseline |
| Hallucination prevention | Checkpoint must list evidence/decisions used |
| Output | `baseline_version: BL-xxx`, checkpoint |

---

# B. Onboarding / Intake Use Cases

## UC-01 — Start New Project With Idea Only

| Field | Detail |
|---|---|
| Mode | M0 |
| Primary agent | `pm-controller` |
| Skills | `intake-gate`, `memory-context-controller`, `circuit-breaker` |
| Hooks | `intake-completeness-check` |
| Graph writes | skeleton project, initial work package, assumptions, missing data |
| Circuit breaker | Baseline breaker keeps official outputs blocked |
| Guardrails | Ask max 5 questions; accept unknown |
| Bias prevention | Do not infer timeline/budget from old projects |
| Hallucination prevention | Mark unknown fields as `MD-*` or `ASM-*` |
| Output | project skeleton, M0 mode, missing-data log |

## UC-02 — Start Rough Project Plan

| Field | Detail |
|---|---|
| Mode | M1 |
| Primary agent | `pm-controller` |
| Supporting agents | `timeline-planner`, `resource-planner` |
| Skills | `intake-gate`, `timeline-planning`, `resource-planning-allocation`, `fact-check` |
| Hooks | `intake-completeness-check`, `cascade-check` |
| Graph writes | draft WP/MS/RA, assumptions, missing data |
| Circuit breaker | Finance breaker if cost forecast requested without rate/budget |
| Guardrails | Draft timeline only; no official baseline |
| Bias prevention | Do not anchor on historical schedule unless labeled benchmark |
| Hallucination prevention | All dates must be source-backed or assumption-backed |
| Output | draft milestone plan, rough resource demand |

## UC-03 — Import Project Materials

Same controls as UC-00A.

## UC-04 — Check Project Readiness

Same controls as UC-00B.

---

# C. Planning / Timeline Use Cases

## UC-05 — Build Milestone Plan

| Field | Detail |
|---|---|
| Mode | M1+ |
| Primary agent | `timeline-planner` |
| Skills | `timeline-planning`, `fact-check`, `circuit-breaker` |
| Hooks | `cascade-check` |
| Graph reads | WP, DEP, ASM, EVD, DEC |
| Graph writes | MS, DEP, missing data |
| Circuit breaker | Evidence breaker for unsupported dates |
| Guardrails | Dates require evidence/assumption/decision |
| Bias prevention | Avoid copying old milestone durations without similarity label |
| Hallucination prevention | No invented dependencies |
| Output | milestone nodes, dependency nodes |

## UC-06 — Update Milestone Date

| Field | Detail |
|---|---|
| Mode | M1+ |
| Primary agent | `timeline-planner` |
| Supporting agents | `resource-planner`, `finance-analyst`, `report-builder`, `pm-fact-checker` |
| Skills | `timeline-planning`, `cascade-impact-check`, `resource-planning-allocation`, `cost-calculator`, `report-builder`, `fact-check`, `circuit-breaker` |
| Hooks | `cascade-check`, `report-fact-check`, `circuit-breaker-check` |
| Graph writes | milestone delta, CR, affected RA/COST/FCST/RPT signals |
| Circuit breaker | Cascade breaker if linked nodes not checked |
| Guardrails | Report cannot update directly after date change |
| Bias prevention | Do not assume cost impact zero |
| Hallucination prevention | Cost/report impact must be derived from linked RA/COST/FCST |
| Output | change-impact assessment |

## UC-07 — Check Critical Path / Dependency Risk

| Field | Detail |
|---|---|
| Mode | M1+ |
| Primary agent | `timeline-planner` |
| Skills | `timeline-planning`, `cascade-impact-check`, `context-audit` |
| Hooks | `cascade-check`, `context-audit` |
| Graph reads | DEP, MS, WP, RISK, ASM |
| Graph writes | risk signal, dependency impact |
| Circuit breaker | Context breaker if dependency status source is stale |
| Guardrails | Dependency risk requires source or assumption |
| Bias prevention | Do not overstate vendor risk from history alone |
| Hallucination prevention | Unknown dependency status remains unknown |
| Output | critical-path/dependency-risk view |

## UC-08 — Build Release Roadmap

| Field | Detail |
|---|---|
| Mode | M1+ |
| Primary agent | `timeline-planner` |
| Supporting agents | `report-builder` |
| Skills | `timeline-planning`, `report-builder`, `fact-check` |
| Hooks | `report-fact-check` |
| Graph reads | WP, MS, DEP, RISK |
| Graph writes | roadmap report/view |
| Circuit breaker | Evidence breaker for unsupported dates/status |
| Guardrails | Roadmap is draft unless M3 baseline exists |
| Bias prevention | Historical roadmap patterns cannot replace current graph |
| Hallucination prevention | Every roadmap item links to WP/MS |
| Output | roadmap view |

---

# D. Resource / Allocation Use Cases

## UC-09 — Build Rough Resource Demand

| Field | Detail |
|---|---|
| Mode | M1+ |
| Primary agent | `resource-planner` |
| Skills | `resource-planning-allocation`, `fact-check` |
| Hooks | `cascade-check` |
| Graph reads | WP, MS, assumptions |
| Graph writes | draft RA, role demand, missing capacity data |
| Circuit breaker | Resource feasibility blocked if capacity missing |
| Guardrails | Demand estimate is not confirmed allocation |
| Bias prevention | Do not infer capacity from past team unless benchmark-labeled |
| Hallucination prevention | Named people/teams require source |
| Output | role/FTE demand model |

## UC-10 — Allocate Named Resources / Teams

| Field | Detail |
|---|---|
| Mode | M2+ |
| Primary agent | `resource-planner` |
| Skills | `resource-planning-allocation`, `cascade-impact-check`, `cost-calculator` |
| Hooks | `cascade-check` |
| Graph reads | WP, MS, capacity, team/resource source |
| Graph writes | RA, capacity conflicts, cost recalculation signal |
| Circuit breaker | Resource breaker if capacity/source missing |
| Guardrails | Allocation must link to period and milestone |
| Bias prevention | Do not assume 100% availability |
| Hallucination prevention | Allocation requires evidence/assumption |
| Output | resource allocation nodes |

## UC-11 — Detect Capacity Conflict

| Field | Detail |
|---|---|
| Mode | M2+ |
| Primary agent | `resource-planner` |
| Skills | `resource-planning-allocation`, `cascade-impact-check`, `circuit-breaker` |
| Hooks | `cascade-check`, `circuit-breaker-check` |
| Graph reads | RA, capacity, MS |
| Graph writes | resource conflict, risk, decision needed |
| Circuit breaker | Cascade breaker if timeline/cost not checked |
| Guardrails | Conflict must propagate to timeline and cost impact |
| Bias prevention | Do not blame team/vendor without evidence |
| Hallucination prevention | Conflict formula/source must be shown |
| Output | conflict log and impact signals |

## UC-12 — Replan After Resource Change

| Field | Detail |
|---|---|
| Mode | M2+ |
| Primary agent | `pm-controller` |
| Supporting agents | `resource-planner`, `timeline-planner`, `finance-analyst`, `report-builder` |
| Skills | `resource-planning-allocation`, `timeline-planning`, `cost-calculator`, `report-builder`, `cascade-impact-check`, `fact-check` |
| Hooks | `cascade-check`, `report-fact-check` |
| Graph writes | RA delta, timeline feasibility, cost delta, report impact |
| Circuit breaker | Cascade breaker and Finance breaker |
| Guardrails | No report update until resource/timeline/cost are checked |
| Bias prevention | Do not assume adding resources improves timeline linearly |
| Hallucination prevention | Impact must be derived from RA/MS/COST |
| Output | replan impact assessment |

---

# E. Finance / Cost / Forecast Use Cases

## UC-13 — Build Cost Assumption

| Field | Detail |
|---|---|
| Mode | M1 |
| Primary agent | `finance-analyst` |
| Skills | `cost-calculator`, `fact-check`, `circuit-breaker` |
| Hooks | `circuit-breaker-check` |
| Graph reads | WP, MS, draft RA |
| Graph writes | cost assumptions, missing rate/budget data |
| Circuit breaker | Finance breaker keeps official forecast blocked |
| Guardrails | Scenario/assumption only |
| Bias prevention | Historical costs benchmark only |
| Hallucination prevention | No single-point estimate without assumptions |
| Output | cost assumption/range, missing finance data |

## UC-14 — Calculate Cost Forecast

| Field | Detail |
|---|---|
| Mode | M2+ |
| Primary agent | `finance-analyst` |
| Skills | `cost-calculator`, `fact-check`, `circuit-breaker` |
| Hooks | `report-fact-check`, `circuit-breaker-check` |
| Graph reads | RA, RATE, COST, budget, assumptions |
| Graph writes | COST, FCST, variance |
| Circuit breaker | Finance breaker if RA/RATE/BUDGET missing |
| Guardrails | Forecast confidence must be labeled |
| Bias prevention | Do not hide contingency or assumptions |
| Hallucination prevention | Every amount derived_from RA/RATE/budget evidence |
| Output | cost lines, forecast, variance |

## UC-15 — Budget Cut Impact

| Field | Detail |
|---|---|
| Mode | M2+ |
| Primary agent | `pm-controller` |
| Supporting agents | `finance-analyst`, `resource-planner`, `timeline-planner`, `report-builder` |
| Skills | `cost-calculator`, `resource-planning-allocation`, `timeline-planning`, `report-builder`, `cascade-impact-check`, `fact-check`, `circuit-breaker` |
| Hooks | `cascade-check`, `report-fact-check`, `circuit-breaker-check` |
| Graph reads | budget, FCST, COST, RA, MS, RISK |
| Graph writes | new variance, options, decision needed, risk |
| Circuit breaker | Cascade breaker if resource/timeline not checked |
| Guardrails | Do not cut resources without timeline feasibility check |
| Bias prevention | Avoid optimism bias on recovery options |
| Hallucination prevention | Every option must state assumption and impact |
| Output | budget-cut impact assessment |

## UC-16 — Rate Card Change Impact

| Field | Detail |
|---|---|
| Mode | M2+ |
| Primary agent | `finance-analyst` |
| Skills | `cost-calculator`, `cascade-impact-check`, `report-builder`, `fact-check` |
| Hooks | `cascade-check`, `report-fact-check` |
| Graph reads | RATE, RA, COST, FCST, RPT |
| Graph writes | updated cost lines, forecast delta, report impact |
| Circuit breaker | Finance breaker if rate source not approved/clear |
| Guardrails | Rate change requires source and effective date |
| Bias prevention | Do not selectively update only favorable cost lines |
| Hallucination prevention | Recalculate all linked RA/COST nodes |
| Output | rate-card change impact |

## UC-17 — Compare Forecast vs Budget

| Field | Detail |
|---|---|
| Mode | M2+ |
| Primary agent | `finance-analyst` |
| Skills | `cost-calculator`, `fact-check`, `circuit-breaker` |
| Hooks | `report-fact-check`, `circuit-breaker-check` |
| Graph reads | FCST, approved budget, COST |
| Graph writes | variance status signal |
| Circuit breaker | Finance breaker if budget/forecast missing |
| Guardrails | Budget RAG only if threshold/rule exists |
| Bias prevention | Do not normalize overspend without decision log |
| Hallucination prevention | Variance formula and source IDs required |
| Output | budget variance and status signal |

---

# F. Reporting / Governance Use Cases

## UC-18 — Generate Draft Weekly Report

| Field | Detail |
|---|---|
| Mode | M1+ |
| Primary agent | `report-builder` |
| Skills | `report-builder`, `fact-check`, `circuit-breaker` |
| Hooks | `report-fact-check`, `circuit-breaker-check` |
| Graph reads | MS, RA, FCST, RISK, ASM, EVD, DEC |
| Graph writes | weekly report view, blocked claims |
| Circuit breaker | Evidence, Finance, Baseline breakers as needed |
| Guardrails | Report status must be source-linked |
| Bias prevention | No history-as-current-status |
| Hallucination prevention | Unsupported RAG is downgraded or blocked |
| Output | draft weekly report |

## UC-19 — Generate Executive Report

| Field | Detail |
|---|---|
| Mode | M3 preferred |
| Primary agent | `report-builder` |
| Supporting agents | `pm-controller`, `pm-fact-checker`, `pm-context-auditor` |
| Skills | `memory-context-controller`, `context-audit`, `report-builder`, `fact-check`, `circuit-breaker` |
| Hooks | `context-audit`, `report-fact-check`, `circuit-breaker-check` |
| Graph reads | controlled baseline, MS, RA, FCST, RISK, DEC, EVD |
| Graph writes | executive report, checkpoint |
| Circuit breaker | Baseline, Evidence, Finance, Context, History-bias breakers |
| Guardrails | Executive report is official only in M3 with fact-check pass |
| Bias prevention | Counter-signal check: show risks/issues, not only positive story |
| Hallucination prevention | Every executive claim must link to graph node/source |
| Output | executive report or downgraded draft |

## UC-20 — Generate SteerCo Update

| Field | Detail |
|---|---|
| Mode | M3 preferred |
| Primary agent | `report-builder` |
| Skills | `report-builder`, `fact-check`, `circuit-breaker` |
| Hooks | `report-fact-check`, `circuit-breaker-check` |
| Graph reads | RPT, MS, FCST, RISK, DEC |
| Graph writes | SteerCo summary, decision asks |
| Circuit breaker | Evidence/Baseline breakers |
| Guardrails | Decision asks must map to risks/issues/changes |
| Bias prevention | Do not hide blocked claims or missing data |
| Hallucination prevention | No unsupported management narrative |
| Output | SteerCo report outline/summary |

## UC-21 — Build Decision-Needed List

| Field | Detail |
|---|---|
| Mode | M1+ |
| Primary agent | `pm-controller` |
| Skills | `cascade-impact-check`, `report-builder`, `fact-check` |
| Hooks | `cascade-check` |
| Graph reads | RISK, CR, MD, ASM, FCST variance, resource conflicts |
| Graph writes | decision-needed list |
| Circuit breaker | Evidence breaker for false approvals |
| Guardrails | Decision item requires reason and impact |
| Bias prevention | Do not convert assumptions into decisions |
| Hallucination prevention | Decision owner/date required or marked missing |
| Output | decision-needed list |

---

# G. Change Control / Cascade Use Cases

## UC-22 — Assess Milestone Delay

Same control combination as UC-06, with explicit delay impact output.

## UC-23 — Assess Scope Increase

| Field | Detail |
|---|---|
| Mode | M1+ |
| Primary agent | `pm-controller` |
| Supporting agents | `timeline-planner`, `resource-planner`, `finance-analyst`, `report-builder` |
| Skills | `timeline-planning`, `resource-planning-allocation`, `cost-calculator`, `cascade-impact-check`, `report-builder`, `fact-check`, `circuit-breaker` |
| Hooks | `cascade-check`, `report-fact-check`, `circuit-breaker-check` |
| Graph writes | new WP/CR, MS impact, RA demand, COST delta, RISK, DEC needed |
| Circuit breaker | Cascade breaker if not all impacts checked |
| Guardrails | Scope increase cannot be called free/no-impact without checks |
| Bias prevention | Avoid optimism bias and sunk-cost framing |
| Hallucination prevention | Every impact must map to graph nodes or missing data |
| Output | scope-change impact assessment |

## UC-24 — Assess Dependency Delay

| Field | Detail |
|---|---|
| Mode | M1+ |
| Primary agent | `timeline-planner` |
| Supporting agents | `pm-context-auditor`, `report-builder` |
| Skills | `timeline-planning`, `cascade-impact-check`, `context-audit`, `report-builder`, `fact-check` |
| Hooks | `cascade-check`, `context-audit`, `report-fact-check` |
| Graph reads | DEP, MS, WP, RISK, EVD |
| Graph writes | dependency risk, affected milestones, report signal |
| Circuit breaker | Context breaker if dependency source is stale |
| Guardrails | Dependency delay needs source or assumption |
| Bias prevention | Vendor-history is only benchmark |
| Hallucination prevention | Unknown dependency date remains missing data |
| Output | dependency-delay impact |

## UC-25 — Approve Baseline Change

| Field | Detail |
|---|---|
| Mode | M3 |
| Primary agent | `pm-controller` |
| Skills | `cascade-impact-check`, `fact-check`, `circuit-breaker` |
| Hooks | `baseline-upgrade-check`, `cascade-check`, `circuit-breaker-check` |
| Graph reads | CR, affected nodes, DEC, EVD |
| Graph writes | new baseline version, checkpoint |
| Circuit breaker | Baseline breaker if decision/evidence missing |
| Guardrails | Approved change must have decision ID and affected nodes |
| Bias prevention | Do not silently rewrite history; preserve previous baseline |
| Hallucination prevention | No approval without decision evidence |
| Output | new baseline checkpoint |

---

# H. Context / Memory / History Use Cases

## UC-26 — Load Run Context Graph

| Field | Detail |
|---|---|
| Mode | All |
| Primary agent | `pm-controller` |
| Skills | `memory-context-controller`, `context-audit` |
| Hooks | `context-audit` |
| Graph reads | target node and linked subgraph |
| Graph writes | none by default; retrieval log if memory/history used |
| Circuit breaker | Context breaker if graph target missing or stale |
| Guardrails | Load by graph IDs, not broad folder scan |
| Bias prevention | Do not over-load old archive |
| Hallucination prevention | No claim from unlinked context |
| Output | selected run context bundle |

## UC-27 — Retrieve Project Memory

| Field | Detail |
|---|---|
| Mode | All |
| Primary agent | `pm-context-auditor` |
| Skills | `memory-context-controller`, `context-audit` |
| Hooks | `context-audit` |
| Graph reads | memory-index, target graph nodes |
| Graph writes | retrieval log, stale/conflict flags |
| Circuit breaker | Context breaker if memory conflicts with baseline |
| Guardrails | Memory must have source/confidence/review date |
| Bias prevention | Authority order: baseline > decision > forecast > evidence > assumption > history |
| Hallucination prevention | Memory without source cannot support official claim |
| Output | labeled memory bundle |

## UC-28 — Use Historical Benchmark

| Field | Detail |
|---|---|
| Mode | M1+ |
| Primary agent | `pm-context-auditor` |
| Skills | `memory-context-controller`, `context-audit`, `circuit-breaker` |
| Hooks | `context-audit`, `circuit-breaker-check` |
| Graph reads | history-index, linked current nodes |
| Graph writes | retrieval log; optional risk signal |
| Circuit breaker | History-bias breaker if used as current fact |
| Guardrails | History can challenge plan, not replace baseline |
| Bias prevention | Similarity and bias risk must be labeled |
| Hallucination prevention | Historical benchmark cannot produce current RAG alone |
| Output | benchmark/risk note |

## UC-29 — Detect Stale Memory

| Field | Detail |
|---|---|
| Mode | All |
| Primary agent | `pm-context-auditor` |
| Skills | `memory-context-controller`, `context-audit`, `circuit-breaker` |
| Hooks | `context-audit`, `circuit-breaker-check` |
| Graph reads | memory-index, baseline version, current graph |
| Graph writes | stale-memory flags, conflict log |
| Circuit breaker | Context breaker if stale memory influences output |
| Guardrails | Stale memory downgraded or blocked |
| Bias prevention | Recency is checked; latest is not automatically true |
| Hallucination prevention | Conflicting memory cannot support claims |
| Output | context audit result |

---

# I. Guardrails / Circuit Breaker Use Cases

## UC-30 — Block Unsupported RAG

| Field | Detail |
|---|---|
| Mode | M0-M2 most common |
| Primary agent | `pm-fact-checker` |
| Skills | `fact-check`, `circuit-breaker` |
| Hooks | `report-fact-check`, `circuit-breaker-check` |
| Graph reads | report draft, baseline, evidence |
| Graph writes | blocked claims, breaker log |
| Circuit breaker | Evidence/Baseline breaker |
| Guardrails | RAG requires baseline/rules/source nodes |
| Bias prevention | Avoid greenwashing status |
| Hallucination prevention | Unsupported RAG is removed or downgraded |
| Output | blocked claim list and recovery path |

## UC-31 — Block Unsupported Budget Claim

| Field | Detail |
|---|---|
| Mode | M0-M1 common |
| Primary agent | `finance-analyst` |
| Supporting agents | `pm-fact-checker` |
| Skills | `cost-calculator`, `fact-check`, `circuit-breaker` |
| Hooks | `circuit-breaker-check`, `report-fact-check` |
| Graph reads | budget, RA, RATE, COST, FCST |
| Graph writes | breaker log, missing finance data |
| Circuit breaker | Finance breaker |
| Guardrails | No budget status without budget + forecast basis |
| Bias prevention | Historical cost does not equal current budget truth |
| Hallucination prevention | Amounts require derived_from/source IDs |
| Output | finance breaker result |

## UC-32 — Block History-As-Truth

| Field | Detail |
|---|---|
| Mode | All |
| Primary agent | `pm-context-auditor` |
| Skills | `memory-context-controller`, `context-audit`, `circuit-breaker` |
| Hooks | `context-audit`, `circuit-breaker-check` |
| Graph reads | history-index, current graph |
| Graph writes | retrieval log, breaker log |
| Circuit breaker | History-bias breaker |
| Guardrails | History is benchmark/risk signal only |
| Bias prevention | Similarity and bias-risk label required |
| Hallucination prevention | History cannot generate current status alone |
| Output | downgraded historical statement |

## UC-33 — Block Report Before Cascade

| Field | Detail |
|---|---|
| Mode | M1+ |
| Primary agent | `pm-controller` |
| Skills | `cascade-impact-check`, `report-builder`, `circuit-breaker` |
| Hooks | `cascade-check`, `report-fact-check`, `circuit-breaker-check` |
| Graph reads | changed nodes, affected links, report draft |
| Graph writes | cascade log, blocked report claim |
| Circuit breaker | Cascade breaker |
| Guardrails | No report publish until affected nodes checked |
| Bias prevention | Avoid premature good/bad status |
| Hallucination prevention | Report status must come after cascade output |
| Output | blocked report or completed cascade report |

## UC-34 — Downgrade Output to Draft

| Field | Detail |
|---|---|
| Mode | All |
| Primary agent | `pm-controller` |
| Skills | `circuit-breaker`, `fact-check` |
| Hooks | `circuit-breaker-check` |
| Graph reads | current mode, output draft, missing data |
| Graph writes | blocked claims, output mode |
| Circuit breaker | Any breaker in HALF_OPEN state |
| Guardrails | Keep useful content but label limitations |
| Bias prevention | Show uncertainty and assumptions |
| Hallucination prevention | Remove unsupported certainty words |
| Output | draft/scenario output with blocked claims |

---

# Required output block for every UC

Every UC output must include:

```txt
Mode:
Run type:
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
