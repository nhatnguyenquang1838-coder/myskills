# Critical Flows With Controls

This reference shows the mechanisms of the Planning & Financial Control Power with explicit agents, skills, hooks, circuit breakers, guardrails, bias controls, and hallucination controls.

## Flow 1 — Simple: Start project with incomplete data

```mermaid
flowchart TD
    A["User request<br/>Plan MVP2, target end July, budget unknown"] --> B["Agent: pm-controller<br/>Intent: create_new_plan"]

    B --> C["Skill: intake-gate<br/>Hook: intake-completeness-check"]
    C --> D["Readiness scoring<br/>Scope, Timeline, Resource, Finance, Evidence, Decisions"]

    D --> E{"Enough data for M3?"}
    E -- "No" --> F["Mode: M0/M1<br/>Guardrail: no official RAG or forecast"]
    E -- "Yes" --> G["Mode: M3 candidate<br/>Run baseline checks"]

    F --> H["Write graph skeleton<br/>WP draft, ASM, MD"]
    H --> I["Circuit Breaker: Baseline/Finance HALF_OPEN<br/>Allowed: draft plan only"]

    I --> J["Hallucination prevention<br/>Unknowns become MD-*<br/>Assumptions become ASM-*"]
    J --> K["Output<br/>Draft plan + missing data + blocked claims"]
```

### Control block

| Control | Detail |
|---|---|
| Agent | `pm-controller` |
| Skill | `intake-gate`, optional `memory-context-controller` |
| Hook | `intake-completeness-check` |
| Breaker | Baseline breaker, Finance breaker |
| Guardrail | Ask max 5 questions; no official RAG/forecast |
| Bias control | Do not infer from past projects |
| Hallucination control | Unknown = `MD-*`; assumption = `ASM-*` |

---

## Flow 2 — Simple: Generate draft weekly report

```mermaid
flowchart TD
    A["User request<br/>Build weekly status"] --> B["Agent: pm-controller<br/>Intent: build_report"]

    B --> C["Build Run Context Graph<br/>Read linked MS, RA, FCST, RISK, ASM, EVD, DEC"]
    C --> D["Agent: report-builder<br/>Skill: report-builder"]
    D --> E["Draft weekly report"]

    E --> F["Hook: report-fact-check<br/>Skill: fact-check<br/>Agent: pm-fact-checker"]
    F --> G{"Unsupported RAG/date/cost/resource claims?"}

    G -- "Yes" --> H["Circuit Breaker: Evidence/Baseline/Finance OPEN or HALF_OPEN"]
    H --> I["Downgrade report<br/>Remove or label unsupported claims"]

    G -- "No" --> J["Circuit Breaker: CLOSED"]
    J --> K["Output controlled report"]
    I --> K
```

### Control block

| Control | Detail |
|---|---|
| Agent | `report-builder`, `pm-fact-checker` |
| Skill | `report-builder`, `fact-check`, `circuit-breaker` |
| Hook | `report-fact-check`, `circuit-breaker-check` |
| Breaker | Evidence, Baseline, Finance |
| Guardrail | Report status must be source-linked |
| Bias control | No greenwashing; include risks/missing data |
| Hallucination control | Every RAG claim requires graph/source support |

---

## Flow 3 — Complex: Create full controlled baseline

```mermaid
flowchart TD
    A["User request<br/>Create full baseline from materials"] --> B["Agent: pm-controller"]

    B --> C["Skill: intake-gate<br/>Classify scope/timeline/resource/finance/governance materials"]
    C --> D["Skill: memory-context-controller<br/>Load linked context, not broad archive"]
    D --> E["Skill: context-audit<br/>Check stale, conflict, history-as-truth"]

    E --> F{"Context valid?"}
    F -- "No" --> F1["Circuit Breaker: Context OPEN<br/>Block M3 baseline"]

    F -- "Yes" --> G["Agent: timeline-planner<br/>Skill: timeline-planning<br/>Write WP, MS, DEP"]
    G --> H["Agent: resource-planner<br/>Skill: resource-planning-allocation<br/>Write RA, capacity, conflicts"]
    H --> I["Agent: finance-analyst<br/>Skill: cost-calculator<br/>Write RATE, COST, FCST, variance"]

    I --> J["Skill: cascade-impact-check<br/>Check graph links WP->MS->RA->COST->FCST->RPT"]
    J --> K["Agent: pm-fact-checker<br/>Skill: fact-check"]

    K --> L{"All baseline claims supported?"}
    L -- "No" --> L1["Circuit Breaker: Evidence/Finance/Baseline OPEN<br/>Create missing-data log"]
    L -- "Yes" --> M["Hook: baseline-upgrade-check"]

    M --> N{"Readiness score >= 16/18?"}
    N -- "No" --> N1["Mode: M1/M2<br/>Draft baseline only"]
    N -- "Yes" --> O["Circuit Breaker: CLOSED"]

    O --> P["Write baseline_version BL-001<br/>Mode: M3 Controlled Baseline"]
    P --> Q["Create baseline checkpoint"]

    F1 --> R["Output blocked claims + recovery questions"]
    L1 --> R
    N1 --> R
```

### Control block

| Control | Detail |
|---|---|
| Agents | `pm-controller`, `timeline-planner`, `resource-planner`, `finance-analyst`, `pm-context-auditor`, `pm-fact-checker` |
| Skills | `intake-gate`, `memory-context-controller`, `context-audit`, `timeline-planning`, `resource-planning-allocation`, `cost-calculator`, `cascade-impact-check`, `fact-check`, `circuit-breaker` |
| Hooks | `intake-completeness-check`, `context-audit`, `cascade-check`, `baseline-upgrade-check`, `circuit-breaker-check` |
| Breakers | Baseline, Finance, Evidence, Context, History-bias |
| Guardrails | M3 requires score >= 16/18 and supported baseline nodes |
| Bias control | History cannot fill missing baseline fields |
| Hallucination control | Every baseline node must have source/assumption/decision/derived support |

---

## Flow 4 — Complex: Milestone delay full cascade

```mermaid
flowchart TD
    A["User request<br/>MS-001 delayed by 2 weeks"] --> B["Agent: pm-controller<br/>Intent: assess_change_impact"]

    B --> C["Build Run Context Graph<br/>Load MS-001 + linked WP, RA, COST, FCST, RPT, RISK, ASM, EVD, DEC"]
    C --> D["Agent: timeline-planner<br/>Skill: timeline-planning<br/>Propose milestone delta"]

    D --> E["Hook: cascade-check<br/>Skill: cascade-impact-check"]
    E --> F{"All affected nodes checked?"}

    F -- "No" --> F1["Circuit Breaker: Cascade OPEN<br/>Block report update"]

    F -- "Yes" --> G["Agent: resource-planner<br/>Skill: resource-planning-allocation<br/>Check extension/conflict"]
    G --> H["Agent: finance-analyst<br/>Skill: cost-calculator<br/>Recalculate COST/FCST delta"]
    H --> I["Agent: report-builder<br/>Skill: report-builder<br/>Draft change-impact report"]

    I --> J["Hook: report-fact-check<br/>Agent: pm-fact-checker<br/>Skill: fact-check"]
    J --> K{"Claims supported?"}

    K -- "No" --> K1["Circuit Breaker: Evidence OPEN<br/>Downgrade unsupported claims"]
    K -- "Yes" --> L["Circuit Breaker: CLOSED or HALF_OPEN"]

    L --> M{"User approves write-back?"}
    M -- "No" --> N["Keep as draft delta"]
    M -- "Yes" --> O["Write approved delta to Project Control Graph"]

    F1 --> P["Create change checkpoint"]
    K1 --> P
    N --> P
    O --> P
```

### Control block

| Control | Detail |
|---|---|
| Agents | `pm-controller`, `timeline-planner`, `resource-planner`, `finance-analyst`, `report-builder`, `pm-fact-checker` |
| Skills | `timeline-planning`, `cascade-impact-check`, `resource-planning-allocation`, `cost-calculator`, `report-builder`, `fact-check`, `circuit-breaker` |
| Hooks | `cascade-check`, `report-fact-check`, `circuit-breaker-check` |
| Breakers | Cascade, Evidence, Finance, Baseline |
| Guardrails | No direct report update after milestone change |
| Bias control | Do not assume cost impact zero or recovery easy |
| Hallucination control | Impact must derive from linked RA/COST/FCST/RPT nodes |

---

## Flow 5 — Complex: Executive report with memory/history controls

```mermaid
flowchart TD
    A["User request<br/>Generate executive report"] --> B["Agent: pm-controller<br/>Intent: executive_report"]

    B --> C["Check readiness mode"]
    C --> D{"Mode = M3?"}

    D -- "No" --> D1["Circuit Breaker: Baseline HALF_OPEN/OPEN<br/>Allowed: draft only"]

    D -- "Yes" --> E["Skill: memory-context-controller<br/>Load current graph first"]
    E --> F["Load linked memory"]
    F --> G["Load history only if benchmark needed"]

    G --> H["Agent: pm-context-auditor<br/>Skill: context-audit"]
    H --> I{"Context valid and not biased?"}

    I -- "No" --> I1["Circuit Breaker: Context/History-bias OPEN"]
    I -- "Yes" --> J["Agent: report-builder<br/>Skill: report-builder<br/>Draft executive report"]

    J --> K["Agent: pm-fact-checker<br/>Skill: fact-check"]
    K --> L{"Every executive claim supported?"}

    L -- "No" --> L1["Circuit Breaker: Evidence OPEN<br/>Remove/downgrade claims"]
    L -- "Yes" --> M["Skill: circuit-breaker<br/>Final breaker evaluation"]

    M --> N{"Breaker state"}
    N -- "CLOSED" --> O["Publish official executive report"]
    N -- "HALF_OPEN" --> P["Downgrade to draft report"]
    N -- "OPEN" --> Q["Block official report"]

    D1 --> R["Create report checkpoint"]
    I1 --> R
    L1 --> R
    O --> R
    P --> R
    Q --> R
```

### Control block

| Control | Detail |
|---|---|
| Agents | `pm-controller`, `report-builder`, `pm-context-auditor`, `pm-fact-checker` |
| Skills | `memory-context-controller`, `context-audit`, `report-builder`, `fact-check`, `circuit-breaker` |
| Hooks | `context-audit`, `report-fact-check`, `circuit-breaker-check` |
| Breakers | Baseline, Evidence, Finance, Context, History-bias |
| Guardrails | Official executive report requires M3 and fact-check pass |
| Bias control | Include counter-signals: risks, issues, missing data, unfavorable variance |
| Hallucination control | Every executive claim links to graph node/source |

---

## Final mechanism summary

```mermaid
flowchart LR
    A["User intent"] --> B["PM Controller"]
    B --> C["Readiness mode"]
    C --> D["Run Context Graph"]
    D --> E["Memory Context Controller"]
    E --> F["Agent + Skill Execution"]
    F --> G["Hooks"]
    G --> H["Cascade Check"]
    H --> I["Context Audit"]
    I --> J["Fact Check"]
    J --> K["Circuit Breaker"]

    K --> L{"Safe?"}
    L -- "Yes" --> M["Output / approved write-back"]
    L -- "Partial" --> N["Draft / scenario output"]
    L -- "No" --> O["Block official claims"]

    M --> P["Checkpoint"]
    N --> P
    O --> P
```
