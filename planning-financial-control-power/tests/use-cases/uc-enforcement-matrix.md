# 22 UC Enforcement Matrix

Version: 0.1
Scope: Planning & Financial Control Power

## Enforcement gate legend

```txt
E0 Intent gate
E1 Readiness gate
E2 Graph gate
E3 Context/memory gate
E4 Contract gate
E5 Skill output gate
E6 Cascade gate
E7 Finance basis gate
E8 Report/claim gate
E9 Write-back gate
E10 Checkpoint gate
```

## Matrix

| UC | Workflow | Mandatory gates | Key guardrails | Breakers that may open | Required hooks/templates |
|---|---|---|---|---|---|
| UC-01 | Create Full Controlled Baseline | E0,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10 | no M3 below 16/18; no baseline without evidence/decision; all DL outputs draft until approved | Contract, Baseline, Finance, Evidence, Context, Cascade | enforcement-preflight, contract-gate, output-gate, writeback-gate, run-execution-record, checkpoint |
| UC-02 | Start Project With Idea Only | E0,E1,E2,E4,E5,E8,E10 | ask max 5 questions; unknown becomes MD; no official RAG/forecast | Baseline, Finance, Evidence | enforcement-preflight, contract-gate, output-gate, run-execution-record |
| UC-03 | Create Rough Project Plan | E0,E1,E2,E4,E5,E6,E8,E10 | draft only; no budget status; dates/FTE are assumptions unless sourced | Baseline, Finance, Evidence, Cascade | enforcement-preflight, contract-gate, cascade-check, output-gate |
| UC-04 | Import Materials to Graph | E0,E1,E2,E3,E4,E5,E8,E10 | imported data is candidate evidence, not approved baseline | Contract, Context, Evidence | enforcement-preflight, context-audit, contract-gate, output-gate |
| UC-05 | Check Project Readiness | E0,E1,E2,E3,E8,E10 | readiness score decides output authority; missing data is explicit | Baseline, Finance, Evidence, Context | enforcement-preflight, context-audit, output-gate |
| UC-06 | Build Milestone Plan | E0,E1,E2,E4,E5,E8,E10 | every date has evidence/decision/assumption; no resource/cost conclusion | Evidence, Contract | enforcement-preflight, contract-gate, output-gate |
| UC-07 | Update Milestone Date | E0,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10 | no direct report update; no zero-cost claim without recalculation | Cascade, Finance, Evidence, Baseline | enforcement-preflight, contract-gate, cascade-check, finance-basis, output-gate, writeback-gate |
| UC-08 | Assess Dependency Risk | E0,E1,E2,E3,E4,E5,E6,E8,E10 | unknown dependency remains MD; vendor history is benchmark only | Context, Evidence, Cascade, History-bias | enforcement-preflight, context-audit, contract-gate, cascade-check, output-gate |
| UC-09 | Build Release Roadmap | E0,E1,E2,E4,E5,E8,E10 | roadmap links to WP/MS; approved roadmap requires M3 | Evidence, Baseline | enforcement-preflight, contract-gate, output-gate |
| UC-10 | Build Resource Demand | E0,E1,E2,E4,E5,E6,E8,E10 | demand is not confirmed allocation; no feasibility without capacity | Evidence, Cascade, Finance | enforcement-preflight, contract-gate, cascade-check, output-gate |
| UC-11 | Allocate Named Resources | E0,E1,E2,E4,E5,E6,E7,E8,E10 | named people require source/assumption; cost only with rate/duration | Evidence, Finance, Cascade | enforcement-preflight, contract-gate, finance-basis, cascade-check, output-gate |
| UC-12 | Detect Capacity Conflict | E0,E1,E2,E4,E5,E6,E8,E10 | conflict formula/source shown; timeline/cost impact signal required | Cascade, Evidence | enforcement-preflight, contract-gate, cascade-check, output-gate |
| UC-13 | Replan After Resource Change | E0,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10 | resource change must cascade to timeline/cost/report; no direct report update | Cascade, Finance, Evidence, Baseline | enforcement-preflight, context-audit, contract-gate, cascade-check, finance-basis, output-gate, writeback-gate |
| UC-14 | Build Cost Assumption | E0,E1,E2,E4,E5,E7,E8,E10 | scenario only; no reliable forecast without rate basis | Finance, Evidence | enforcement-preflight, contract-gate, finance-basis, output-gate |
| UC-15 | Calculate Cost Forecast | E0,E1,E2,E4,E5,E7,E8,E9,E10 | every amount has derived_from; budget RAG only if rule exists | Finance, Evidence, Baseline | enforcement-preflight, contract-gate, finance-basis, output-gate, writeback-gate |
| UC-16 | Budget Cut Impact | E0,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10 | no no-impact claim without timeline/resource/cost checks; options state assumptions | Cascade, Finance, Evidence, Baseline | enforcement-preflight, context-audit, contract-gate, cascade-check, finance-basis, output-gate, writeback-gate |
| UC-17 | Rate Card Change Impact | E0,E1,E2,E4,E5,E6,E7,E8,E9,E10 | rate source/effective date required; recalc all linked cost lines | Finance, Evidence, Cascade | enforcement-preflight, contract-gate, finance-basis, cascade-check, output-gate, writeback-gate |
| UC-18 | Compare Forecast vs Budget | E0,E1,E2,E4,E5,E7,E8,E10 | variance allowed; Green/Red only with threshold and mode authority | Finance, Evidence, Baseline | enforcement-preflight, contract-gate, finance-basis, output-gate |
| UC-19 | Generate Draft Weekly Report | E0,E1,E2,E3,E4,E5,E8,E10 | draft unless M3; blocked claims visible; source IDs listed | Baseline, Finance, Evidence, Context | enforcement-preflight, context-audit, contract-gate, output-gate |
| UC-20 | Generate Executive Report | E0,E1,E2,E3,E4,E5,E6,E7,E8,E10 | official only if M3 and breaker CLOSED; include counter-signals | Baseline, Finance, Evidence, Context, History-bias, Cascade | enforcement-preflight, context-audit, contract-gate, cascade-check, finance-basis, output-gate |
| UC-21 | History-As-Truth Blocker | E0,E1,E2,E3,E5,E8,E10 | history benchmark only; cannot produce current status alone | History-bias, Context, Finance, Evidence | enforcement-preflight, context-audit, output-gate |
| UC-22 | Unsupported RAG / Budget Claim Breaker | E0,E1,E2,E4,E5,E7,E8,E10 | fake Green/on-budget must be blocked; draft fallback only | Baseline, Finance, Evidence | enforcement-preflight, contract-gate, finance-basis, output-gate |

## Minimum pass rule

```txt
A UC test cannot pass unless every mandatory gate is either PASS, DOWNGRADED, or explicitly BLOCKED with breaker reason.
```

## Unsafe fail conditions

```txt
- official RAG appears without M3 baseline
- on-budget claim appears without finance basis
- report publishes after graph change without cascade check
- DL Skill result is written directly to graph
- history becomes current truth
- missing data is hidden
```
