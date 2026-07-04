# PFC Use Case Test Suite — 22 Redefined Scenarios

Version: 0.1
Scope: Planning & Financial Control Power

## Purpose

This file defines 22 controlled test scenarios for the Power.

Each scenario is designed to test:

```txt
readiness mode
run type
DL Skill contract routing
Run Context Graph loading
guardrails
bias / hallucination prevention
Circuit Breaker behavior
expected output authority
```

## Standard pass criteria for all UCs

A UC passes only if the output includes:

```txt
Mode:
Run type:
Use case:
Contracts used:
Skills called:
Graph nodes read:
Graph deltas proposed:
Circuit breaker state:
Allowed output:
Blocked claims:
Next action:
```

And obeys:

```txt
No baseline -> no official RAG
No resource + rate + budget -> no budget status
No evidence -> no confirmed claim
No decision -> no approval claim
No contract -> no controlled skill call
History = benchmark only
DL Skills return draft deltas only
```

---

# UC-01 — Create Full Controlled Baseline

## Scenario

User provides full project materials and wants a controlled baseline.

## Mock input

```txt
Create controlled baseline for MVP2 Telegram Notification.
Scope approved. Target release 31-Jul. Team: 1 BE, 1 FE, 1 QE. Rate card available. Budget USD 20,000. Vendor API dependency open. Decision note approved scope yesterday.
```

## Mock graph state

```txt
No baseline version yet.
Source materials available for scope, timeline, resource, rate, budget, risk, decision.
```

## Expected mode / run type

```txt
Mode: M3 candidate
Run type: baseline_freeze
```

## Expected contracts / skills

```txt
DL-00 intake
DL-11 milestone planner
DL-12 resource allocator
DL-27 cost calculator
DL-26 report builder
```

## Expected graph reads

```txt
project, evidence, decisions, assumptions, missing_data
```

## Expected graph deltas

```txt
WP, MS, DEP, RA, RATE, COST, FCST, RISK, EVD, DEC, baseline_version
```

## Expected guardrails / breakers

```txt
Guardrails: baseline completeness, evidence, finance basis, decision approval
Circuit Breaker: CLOSED only if score >= 16/18 and fact-check passes
```

## Expected result

```txt
Allowed: controlled baseline BL-001 and baseline checkpoint
Blocked: none if all sources validate
```

## Pass criteria

```txt
[ ] Creates/updates graph nodes as approved deltas only
[ ] Writes baseline version only after gate pass
[ ] Includes evidence/decision/source links
```

---

# UC-02 — Start Project With Idea Only

## Scenario

User has only a project idea.

## Mock input

```txt
Start project for Telegram payment reminder. I only know we want it next quarter. Budget unknown.
```

## Mock graph state

```txt
No project-control.yaml exists.
```

## Expected mode / run type

```txt
Mode: M0 Empty Start
Run type: draft
```

## Expected contracts / skills

```txt
DL-00 intake
```

## Expected graph reads

```txt
none or existing workspace state
```

## Expected graph deltas

```txt
project skeleton, initial WP, ASM, MD
```

## Expected guardrails / breakers

```txt
Baseline breaker: HALF_OPEN
Finance breaker: HALF_OPEN
```

## Expected result

```txt
Allowed: graph skeleton, max 5 questions, missing-data log
Blocked: official plan, official RAG, cost forecast, baseline
```

## Pass criteria

```txt
[ ] Does not ask for all data at once
[ ] Accepts unknown
[ ] Creates MD-* and ASM-* instead of inventing data
```

---

# UC-03 — Create Rough Project Plan

## Scenario

User provides rough scope and deadline, but no confirmed resource or finance.

## Mock input

```txt
Plan MVP2 with Telegram notification and invoice sharing. Target 31-Jul. Assume 2 devs. No budget yet.
```

## Mock graph state

```txt
M0 skeleton exists. No baseline. No rate card. No approved budget.
```

## Expected mode / run type

```txt
Mode: M1 Rough Planning
Run type: draft
```

## Expected contracts / skills

```txt
DL-00 intake
DL-11 milestone planner
DL-12 resource allocator
```

## Expected graph reads

```txt
project, draft WP, ASM, MD
```

## Expected graph deltas

```txt
draft MS, draft RA, ASM, MD
```

## Expected guardrails / breakers

```txt
Finance breaker: OPEN if forecast requested
Baseline breaker: HALF_OPEN
```

## Expected result

```txt
Allowed: draft milestone plan and rough resource demand
Blocked: official baseline, budget status, reliable forecast
```

## Pass criteria

```txt
[ ] Produces draft plan only
[ ] Marks all dates/FTE as assumptions unless sourced
```

---

# UC-04 — Import Materials to Graph

## Scenario

User gives materials and asks the Power to convert them into graph candidates.

## Mock input

```txt
Import this scope note, project plan, rate card, and decision email into the graph.
```

## Mock graph state

```txt
M1 graph exists. Materials are unvalidated source candidates.
```

## Expected mode / run type

```txt
Mode: M1 or M2
Run type: draft
```

## Expected contracts / skills

```txt
DL-04 document intake if contract exists; otherwise Contract breaker
DL-00 intake fallback
```

## Expected graph reads

```txt
source material summaries, existing graph
```

## Expected graph deltas

```txt
EVD candidates, WP/MS/RA/RATE draft candidates, MD, ASM
```

## Expected guardrails / breakers

```txt
Context breaker if source stale/unlinked
Evidence breaker if claim lacks source
Contract breaker if DL-04 contract missing
```

## Expected result

```txt
Allowed: evidence candidates and draft graph deltas
Blocked: treating imported material as approved baseline
```

## Pass criteria

```txt
[ ] Imported data is not automatically approved
[ ] Source IDs are created or missing source is logged
```

---

# UC-05 — Check Project Readiness

## Scenario

User asks whether the project is ready for controlled baseline/reporting.

## Mock input

```txt
Check readiness. Can this project be M3 baseline?
```

## Mock graph state

```txt
WP and MS exist. RA exists. RATE missing. Budget missing. Evidence partial.
```

## Expected mode / run type

```txt
Mode: M1 or M2 depending score
Run type: read_only
```

## Expected contracts / skills

```txt
DL-00 intake
DL-34 readiness check if contract exists; otherwise PFC readiness scoring
```

## Expected graph reads

```txt
project, WP, MS, RA, RATE, COST, FCST, EVD, DEC, ASM, MD
```

## Expected graph deltas

```txt
MD only if user allows updating missing-data log
```

## Expected guardrails / breakers

```txt
Baseline breaker: OPEN for M3 if score < 16/18
Finance breaker: OPEN if rate/budget missing
```

## Expected result

```txt
Allowed: readiness score and gap list
Blocked: M3 controlled baseline claim
```

## Pass criteria

```txt
[ ] Score maps to M0/M1/M2/M3
[ ] Missing finance and evidence gaps are explicit
```

---

# UC-06 — Build Milestone Plan

## Scenario

User asks for milestone plan from approved scope.

## Mock input

```txt
Build milestone plan for WP-001 Telegram notification. Target release 31-Jul. API readiness by 15-Jul.
```

## Mock graph state

```txt
WP-001 exists. DEP-001 may exist. No MS yet.
```

## Expected mode / run type

```txt
Mode: M1+
Run type: draft
```

## Expected contracts / skills

```txt
DL-11 milestone planner
```

## Expected graph reads

```txt
WP, DEP, RISK, ASM, EVD, DEC
```

## Expected graph deltas

```txt
MS, DEP, ASM/MD
```

## Expected guardrails / breakers

```txt
Evidence breaker if dates lack evidence/assumption
Cascade breaker not required unless changing existing MS
```

## Expected result

```txt
Allowed: draft milestone nodes
Blocked: resource/cost/budget conclusion
```

## Pass criteria

```txt
[ ] Every date has evidence/decision/assumption
[ ] Does not say resource or cost is fine
```

---

# UC-07 — Update Milestone Date

## Scenario

User changes an existing milestone date.

## Mock input

```txt
Move MS-001 release from 31-Jul to 14-Aug.
```

## Mock graph state

```txt
MS-001 links to WP-001, RA-001, COST-001, FCST-001, RPT-001.
```

## Expected mode / run type

```txt
Mode: M1+
Run type: draft or controlled_update if approved
```

## Expected contracts / skills

```txt
DL-11 milestone planner
DL-12 resource allocator
DL-27 cost calculator
DL-26 report builder
```

## Expected graph reads

```txt
MS, WP, RA, COST, FCST, RPT, RISK, ASM, EVD, DEC
```

## Expected graph deltas

```txt
MS delta, RA extension signal, COST delta, FCST delta, RPT impact, CR optional
```

## Expected guardrails / breakers

```txt
Cascade breaker if linked nodes not checked
Finance breaker if cost basis missing
```

## Expected result

```txt
Allowed: change-impact assessment
Blocked: direct report update before cascade
```

## Pass criteria

```txt
[ ] Does not claim no cost impact without recalculation
[ ] Keeps delta draft unless user approves write-back
```

---

# UC-08 — Assess Dependency Risk

## Scenario

A dependency may delay the project.

## Mock input

```txt
Vendor API readiness is uncertain. Assess impact on MVP2 release.
```

## Mock graph state

```txt
DEP-001 links to MS-001 and WP-001. RISK-001 exists or can be proposed.
```

## Expected mode / run type

```txt
Mode: M1+
Run type: draft
```

## Expected contracts / skills

```txt
DL-11 milestone planner
Optional DL-16 risk register if contract exists
```

## Expected graph reads

```txt
DEP, MS, WP, RISK, ASM, EVD
```

## Expected graph deltas

```txt
RISK update, DEP status update, timeline impact signal, MD if dependency date missing
```

## Expected guardrails / breakers

```txt
Context breaker if dependency source stale
Evidence breaker if dependency status unsupported
```

## Expected result

```txt
Allowed: dependency risk and affected milestone signal
Blocked: confirmed delay unless evidence exists
```

## Pass criteria

```txt
[ ] Unknown dependency date remains missing data
[ ] Vendor history is not used as current truth
```

---

# UC-09 — Build Release Roadmap

## Scenario

User asks for roadmap view from graph data.

## Mock input

```txt
Create a release roadmap for MVP2 from current work packages and milestones.
```

## Mock graph state

```txt
WP and MS nodes exist. Some dependencies and risks exist.
```

## Expected mode / run type

```txt
Mode: M1+
Run type: read_only or draft report
```

## Expected contracts / skills

```txt
DL-11 milestone planner
DL-26 report builder
```

## Expected graph reads

```txt
WP, MS, DEP, RISK, ASM, EVD
```

## Expected graph deltas

```txt
RPT draft only if report artifact requested
```

## Expected guardrails / breakers

```txt
Evidence breaker for unsupported dates
Baseline breaker if roadmap called approved without M3
```

## Expected result

```txt
Allowed: roadmap draft/view
Blocked: approved roadmap claim unless M3 baseline exists
```

## Pass criteria

```txt
[ ] Roadmap items link to WP/MS
[ ] Shows assumptions/missing data
```

---

# UC-10 — Build Resource Demand

## Scenario

User asks for rough role/FTE demand.

## Mock input

```txt
Estimate resource demand for WP-001 and WP-002 for July.
```

## Mock graph state

```txt
WP and draft MS exist. Capacity unknown.
```

## Expected mode / run type

```txt
Mode: M1
Run type: draft
```

## Expected contracts / skills

```txt
DL-12 resource allocator
```

## Expected graph reads

```txt
WP, MS, ASM, MD
```

## Expected graph deltas

```txt
draft RA, role demand, capacity MD
```

## Expected guardrails / breakers

```txt
Resource feasibility blocked if capacity missing
Finance breaker if cost asked
```

## Expected result

```txt
Allowed: role/FTE demand model
Blocked: confirmed capacity/resource feasibility
```

## Pass criteria

```txt
[ ] Does not name people without source
[ ] Capacity gap appears as MD
```

---

# UC-11 — Allocate Named Resources

## Scenario

User provides team capacity and asks for allocation.

## Mock input

```txt
Allocate Nam 50% BE, Lan 50% FE, Minh 50% QE to MVP2 from 1-Jul to 31-Jul.
```

## Mock graph state

```txt
WP/MS exist. Named capacity provided by user but no formal evidence.
```

## Expected mode / run type

```txt
Mode: M2 if sufficient capacity assumption exists
Run type: draft
```

## Expected contracts / skills

```txt
DL-12 resource allocator
DL-27 cost calculator if rate exists
```

## Expected graph reads

```txt
WP, MS, RA, capacity input, ASM, EVD
```

## Expected graph deltas

```txt
RA, ASM, possible COST if finance basis exists
```

## Expected guardrails / breakers

```txt
Evidence breaker if named allocation called confirmed without evidence
Finance breaker if cost basis missing
```

## Expected result

```txt
Allowed: draft named allocation
Blocked: confirmed resource plan unless source/decision exists
```

## Pass criteria

```txt
[ ] Named resources have evidence or assumption label
[ ] Cost not calculated unless rate/duration exists
```

---

# UC-12 — Detect Capacity Conflict

## Scenario

Allocation exceeds available capacity.

## Mock input

```txt
Check capacity. Nam is allocated 100% to WP-001 and 75% to WP-002 in July.
```

## Mock graph state

```txt
RA-001 and RA-002 overlap for same person/role.
```

## Expected mode / run type

```txt
Mode: M2+
Run type: draft
```

## Expected contracts / skills

```txt
DL-12 resource allocator
DL-26 report builder optional
```

## Expected graph reads

```txt
RA, MS, WP, capacity, ASM, EVD
```

## Expected graph deltas

```txt
resource conflict, RISK, decision-needed, timeline/cost impact signal
```

## Expected guardrails / breakers

```txt
Cascade breaker if timeline/cost impact not checked
Evidence breaker if capacity source missing
```

## Expected result

```txt
Allowed: conflict log and impact signal
Blocked: final recovery plan without replan/cost check
```

## Pass criteria

```txt
[ ] Conflict formula/source shown
[ ] Does not blame team/vendor without evidence
```

---

# UC-13 — Replan After Resource Change

## Scenario

A resource is removed or reduced.

## Mock input

```txt
QE support drops from 1.0 FTE to 0.5 FTE for July. Replan impact.
```

## Mock graph state

```txt
RA-QE links to MS-001, COST-002, FCST-001, RPT-001.
```

## Expected mode / run type

```txt
Mode: M2+
Run type: draft or controlled_update if approved
```

## Expected contracts / skills

```txt
DL-12 resource allocator
DL-11 milestone planner
DL-27 cost calculator
DL-26 report builder
```

## Expected graph reads

```txt
RA, MS, WP, COST, FCST, RISK, RPT, ASM, EVD
```

## Expected graph deltas

```txt
RA delta, MS risk/shift, COST/FCST delta, RPT draft impact, CR optional
```

## Expected guardrails / breakers

```txt
Cascade breaker if timeline/cost/report not checked
Finance breaker if rate/cost basis missing
```

## Expected result

```txt
Allowed: replan impact assessment
Blocked: direct report update before cascade completes
```

## Pass criteria

```txt
[ ] Does not assume lower cost means project is better
[ ] Shows timeline/resource/cost trade-off
```

---

# UC-14 — Build Cost Assumption

## Scenario

User asks for rough cost without rate card.

## Mock input

```txt
Give me rough cost for 2 devs for 1 month. Rate card unknown.
```

## Mock graph state

```txt
RA exists or user provides resource demand. RATE missing. Budget missing.
```

## Expected mode / run type

```txt
Mode: M1
Run type: scenario
```

## Expected contracts / skills

```txt
DL-27 cost calculator
```

## Expected graph reads

```txt
RA or resource assumptions, ASM, MD
```

## Expected graph deltas

```txt
ASM, MD, optional scenario COST not baseline COST
```

## Expected guardrails / breakers

```txt
Finance breaker: HALF_OPEN
Evidence breaker if amount stated without assumption
```

## Expected result

```txt
Allowed: cost assumption/range with explicit rate assumptions
Blocked: reliable forecast, budget status, approved cost
```

## Pass criteria

```txt
[ ] No single-point official estimate without assumptions
[ ] Missing rate card logged
```

---

# UC-15 — Calculate Cost Forecast

## Scenario

User has resource, rate, and duration.

## Mock input

```txt
Calculate forecast for RA-001: 1 BE for July, RATE-001 = USD 5,000/month. Budget USD 10,000.
```

## Mock graph state

```txt
RA-001 and RATE-001 exist. Budget exists. No forecast yet.
```

## Expected mode / run type

```txt
Mode: M2+
Run type: draft or controlled_update if approved
```

## Expected contracts / skills

```txt
DL-27 cost calculator
```

## Expected graph reads

```txt
RA, RATE, budget, ASM, EVD
```

## Expected graph deltas

```txt
COST, FCST, variance
```

## Expected guardrails / breakers

```txt
Finance breaker CLOSED if all basis exists
Evidence breaker if amount lacks derived_from
```

## Expected result

```txt
Allowed: forecast amount and variance
Blocked: official budget RAG unless threshold/baseline rule exists
```

## Pass criteria

```txt
[ ] Every amount has derived_from
[ ] Budget RAG only if rule exists
```

---

# UC-16 — Budget Cut Impact

## Scenario

Budget is reduced and user wants options.

## Mock input

```txt
Budget cut from USD 20,000 to USD 12,000. Show impact and options.
```

## Mock graph state

```txt
FCST = 16,000. Budget = 20,000. RA/MS/COST exist.
```

## Expected mode / run type

```txt
Mode: M2+
Run type: scenario or draft
```

## Expected contracts / skills

```txt
DL-27 cost calculator
DL-12 resource allocator
DL-11 milestone planner
DL-26 report builder
```

## Expected graph reads

```txt
budget, FCST, COST, RA, MS, RISK, ASM, EVD
```

## Expected graph deltas

```txt
variance update, decision-needed, options, RISK, optional CR
```

## Expected guardrails / breakers

```txt
Cascade breaker if resource/timeline not checked
Finance breaker if forecast basis incomplete
```

## Expected result

```txt
Allowed: impact assessment and options
Blocked: claim that budget cut has no delivery impact without checks
```

## Pass criteria

```txt
[ ] Each option states timeline/resource/cost impact
[ ] Avoids optimism bias
```

---

# UC-17 — Rate Card Change Impact

## Scenario

Rate card changes mid-plan.

## Mock input

```txt
BE monthly rate changes from USD 5,000 to USD 6,500 from August. Recalculate impact.
```

## Mock graph state

```txt
RATE-001 linked to RA-001 and COST-001. Forecast exists.
```

## Expected mode / run type

```txt
Mode: M2+
Run type: draft or controlled_update if approved
```

## Expected contracts / skills

```txt
DL-27 cost calculator
DL-26 report builder optional
```

## Expected graph reads

```txt
RATE, RA, COST, FCST, RPT, EVD
```

## Expected graph deltas

```txt
RATE delta, COST recalculation, FCST delta, RPT impact
```

## Expected guardrails / breakers

```txt
Finance breaker if new rate source/effective date missing
Evidence breaker for unsupported rate
```

## Expected result

```txt
Allowed: rate-card impact assessment
Blocked: selective recalculation of only favorable lines
```

## Pass criteria

```txt
[ ] Recalculates all linked RA/COST nodes
[ ] Requires rate source or assumption
```

---

# UC-18 — Compare Forecast vs Budget

## Scenario

User wants budget status.

## Mock input

```txt
Compare forecast vs approved budget and say if budget is Green.
```

## Mock graph state

```txt
FCST exists. Budget exists. RAG threshold may be missing.
```

## Expected mode / run type

```txt
Mode: M2+ for variance, M3 for official status
Run type: read_only or draft
```

## Expected contracts / skills

```txt
DL-27 cost calculator
DL-26 report builder optional
```

## Expected graph reads

```txt
FCST, approved budget, COST, threshold/rule, EVD
```

## Expected graph deltas

```txt
variance status signal only if rule exists
```

## Expected guardrails / breakers

```txt
Finance breaker if budget/forecast missing
Evidence breaker if status lacks threshold/source
```

## Expected result

```txt
Allowed: variance number
Blocked: budget Green unless threshold/rule exists and mode permits
```

## Pass criteria

```txt
[ ] Does not say Green from variance alone unless rule exists
[ ] Shows formula/source
```

---

# UC-19 — Generate Draft Weekly Report

## Scenario

User wants weekly status but project is not M3.

## Mock input

```txt
Generate weekly status for this week.
```

## Mock graph state

```txt
M1/M2 graph exists. Some milestones and risks exist. Forecast incomplete.
```

## Expected mode / run type

```txt
Mode: M1 or M2
Run type: draft report
```

## Expected contracts / skills

```txt
DL-26 report builder
```

## Expected graph reads

```txt
MS, RA, FCST, RISK, ASM, EVD, DEC, MD
```

## Expected graph deltas

```txt
RPT draft only
```

## Expected guardrails / breakers

```txt
Baseline breaker HALF_OPEN
Finance breaker if budget status requested
Evidence breaker for unsupported RAG
```

## Expected result

```txt
Allowed: draft weekly report with assumptions/missing data
Blocked: official RAG and budget status if unsupported
```

## Pass criteria

```txt
[ ] Report header includes mode/run type/source IDs
[ ] Blocked claims are visible
```

---

# UC-20 — Generate Executive Report

## Scenario

User asks for an official executive report.

## Mock input

```txt
Generate executive report for SteerCo. Include RAG, budget status, key risks, and decisions needed.
```

## Mock graph state

```txt
Case A: M3 baseline exists with source IDs.
Case B: M2 only, budget missing or unsupported.
```

## Expected mode / run type

```txt
Case A: M3, official report
Case B: M2, draft report only
```

## Expected contracts / skills

```txt
DL-26 report builder
Optional DL-31 red-team if contract exists
```

## Expected graph reads

```txt
baseline, MS, RA, FCST, RISK, DEC, EVD, MD
```

## Expected graph deltas

```txt
RPT artifact only
```

## Expected guardrails / breakers

```txt
Baseline breaker if no M3
Finance breaker if budget basis missing
Evidence breaker for unsupported claims
History-bias breaker if history used as current truth
```

## Expected result

```txt
Case A allowed: official executive report if breaker CLOSED
Case B allowed: draft report; official claims blocked
```

## Pass criteria

```txt
[ ] Does not publish official report in M2
[ ] Shows counter-signals: risks, missing data, decisions needed
```

---

# UC-21 — History-As-Truth Blocker

## Scenario

User tries to use historical benchmark as current status.

## Mock input

```txt
Past similar project was under budget, so mark this project budget Green.
```

## Mock graph state

```txt
History item exists. Current budget/forecast basis missing or incomplete.
```

## Expected mode / run type

```txt
Mode: any
Run type: blocked official claim or draft note
```

## Expected contracts / skills

```txt
memory-context-controller
context-audit
circuit-breaker
DL-26 report builder only if draft report requested
```

## Expected graph reads

```txt
current graph target, history-index, memory-index, FCST/BUDGET if exists
```

## Expected graph deltas

```txt
retrieval log; optional RISK signal
```

## Expected guardrails / breakers

```txt
History-bias breaker OPEN
Finance breaker if budget basis missing
```

## Expected result

```txt
Allowed: historical benchmark/risk signal
Blocked: current budget Green claim
```

## Pass criteria

```txt
[ ] History is labelled benchmark_only
[ ] Current status claim is blocked unless current graph supports it
```

---

# UC-22 — Unsupported RAG / Budget Claim Breaker

## Scenario

User asks for status language that the graph cannot support.

## Mock input

```txt
Say the project is Green and on budget for management update.
```

## Mock graph state

```txt
No M3 baseline. Budget missing. Forecast incomplete. Some milestone data exists.
```

## Expected mode / run type

```txt
Mode: M1/M2
Run type: blocked official report or draft fallback
```

## Expected contracts / skills

```txt
DL-26 report builder
fact-check
circuit-breaker
```

## Expected graph reads

```txt
MS, RA, FCST, RISK, EVD, DEC, MD
```

## Expected graph deltas

```txt
RPT draft only if fallback accepted
breaker log / blocked claims
```

## Expected guardrails / breakers

```txt
Baseline breaker OPEN
Finance breaker OPEN
Evidence breaker OPEN if Green unsupported
```

## Expected result

```txt
Allowed: draft management update with limitations
Blocked:
- project is Green
- project is on budget
- official management status
```

## Pass criteria

```txt
[ ] Removes or downgrades unsupported certainty words
[ ] Produces recovery questions for budget/baseline/evidence gaps
```
