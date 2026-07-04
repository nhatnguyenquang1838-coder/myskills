# UC Control Summary Reference

## Core rule

```txt
Every UC must be graph-aware.
Only approved deltas write back to the persistent Project Control Graph.
```

## Universal output block

Every UC output should include:

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

## Control concepts

| Concept | Meaning |
|---|---|
| Agent | Who performs or reviews the work |
| Skill | What capability is executed |
| Hook | When an automatic/manual control check is triggered |
| Circuit Breaker | Whether official output is allowed, downgraded, or blocked |
| Guardrail | Rule that must not be violated |
| Bias control | Prevents stale/history/selective context from distorting output |
| Hallucination control | Forces claims to be supported by graph/evidence/assumption/decision/derived calculation |

## UC family map

| UC family | Main agent | Main skills | Main hooks | Breakers |
|---|---|---|---|---|
| UC-00 Baseline creation | `pm-controller` | `intake-gate`, `timeline-planning`, `resource-planning-allocation`, `cost-calculator`, `fact-check`, `circuit-breaker` | `baseline-upgrade-check`, `cascade-check`, `circuit-breaker-check` | Baseline, Finance, Evidence, Context |
| UC-01/02 Intake and rough plan | `pm-controller` | `intake-gate`, `timeline-planning`, `resource-planning-allocation` | `intake-completeness-check` | Baseline, Finance |
| UC-05/08 Timeline planning | `timeline-planner` | `timeline-planning`, `fact-check` | `cascade-check`, `report-fact-check` | Evidence, Cascade |
| UC-09/12 Resource planning | `resource-planner` | `resource-planning-allocation`, `cascade-impact-check`, `cost-calculator` | `cascade-check` | Resource, Cascade, Finance |
| UC-13/17 Finance forecast | `finance-analyst` | `cost-calculator`, `fact-check`, `circuit-breaker` | `circuit-breaker-check`, `report-fact-check` | Finance, Evidence |
| UC-18/21 Reporting | `report-builder` | `report-builder`, `fact-check`, `circuit-breaker` | `report-fact-check`, `circuit-breaker-check` | Baseline, Evidence, Finance, Context |
| UC-22/25 Change control | `pm-controller` | `cascade-impact-check`, `timeline-planning`, `resource-planning-allocation`, `cost-calculator`, `report-builder`, `fact-check` | `cascade-check`, `baseline-upgrade-check` | Cascade, Baseline, Evidence |
| UC-26/29 Context and memory | `pm-context-auditor` | `memory-context-controller`, `context-audit`, `circuit-breaker` | `context-audit`, `circuit-breaker-check` | Context, History-bias |
| UC-30/34 Guardrails | `pm-fact-checker` | `fact-check`, `circuit-breaker` | `report-fact-check`, `circuit-breaker-check` | Evidence, Baseline, Finance, History-bias |

## Guardrail rules by UC family

| UC family | Guardrail |
|---|---|
| Baseline | No M3 if readiness score < 16/18 |
| Intake | Ask max 5 questions and accept unknown |
| Timeline | No unsupported date/dependency |
| Resource | No resource feasibility without allocation period and capacity basis |
| Finance | No reliable forecast without resource + rate + budget basis |
| Report | No official RAG without baseline and source-linked graph nodes |
| Change | No report update before cascade check |
| Context | Load by graph links, not broad folder scan |
| History | History is benchmark/risk signal only |
| Memory | Memory supports graph; memory does not replace graph |

## Bias and hallucination controls

| Risk | Prevention |
|---|---|
| Stale baseline | Current baseline version wins |
| Historical bias | History cannot replace current graph |
| Confirmation bias | Show risks/issues/missing data, not only positive evidence |
| Optimism bias | State assumptions and confidence explicitly |
| Recency bias | Latest file is not automatically approved truth |
| Hallucinated status | Every RAG/date/cost/resource claim needs graph support |
| Hallucinated cost | Every amount needs `derived_from` or source ID |
| Hallucinated decision | Every approval needs `decision_id` or missing-data item |

## Breaker state rule

| State | Meaning | Output authority |
|---|---|---|
| CLOSED | checks pass | official output allowed if mode permits |
| HALF_OPEN | some limitations | draft/scenario output only |
| OPEN | critical control failed | block official claims and show recovery path |
