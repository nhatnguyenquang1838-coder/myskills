# BCBS 239 — 2023 Progress Lessons

Source: SRC-BCBS239-2023.

## Purpose for skills

Use this file to update skills and Power controls with practical lessons from post-implementation progress observations.

The 2023 progress report is not a new principle set. It explains adoption gaps, recurring challenges, supervisory recommendations, and case-study patterns.

## Key observations

### 1. Full adoption remains difficult

The progress report highlights that banks remain at different adoption stages and that additional work is required at all banks to attain or sustain full compliance.

Power implication:

```txt
Do not assume mature data/reporting capability.
Always run readiness and contract checks before official output.
```

### 2. Governance and board ownership remain critical

The report stresses board and senior management responsibility for data governance, robust frameworks, ownership, and accountability.

Power implication:

```txt
Official baseline/report claims require owner, evidence, decision, and review trail.
```

### 3. Persistent challenges include fragmented IT, legacy systems, and manual processes

These issues slow adoption and weaken data aggregation/reporting reliability.

Power implication:

```txt
Manual workaround or fragmented source = limitation label + lower confidence.
```

### 4. Common taxonomy and lineage remain major gaps

Lack of taxonomy and complete data lineage complicates harmonisation, defect detection, and reliable reporting.

Power implication:

```txt
Use Project Control Graph IDs, source_ids, derived_from, and baseline_version as lightweight taxonomy/lineage controls.
```

### 5. Stress events expose weaknesses

Pandemic and recent stress events showed that ad hoc, higher-frequency, granular reporting strains fragmented systems and manual reporting processes.

Power implication:

```txt
Stress/ad hoc reporting use cases must apply timeliness, completeness, and approximation guardrails.
```

### 6. Data quality is prerequisite for digitalisation

New technology may help automate documentation, lineage, and data flow visualisation, but poor source data undermines downstream output.

Power implication:

```txt
No AI-generated report should bypass source-quality checks.
```

## Recommendations to banks — skill interpretation

| Recommendation theme | Skill/Power requirement |
|---|---|
| continue long-term BCBS239 roadmap | maintain improvement backlog and readiness rescoring |
| board oversight of data governance | require owner/decision/evidence for controlled outputs |
| ownership and accountability for data quality | include data owner / control owner fields |
| broader application beyond risk reports | apply principles to delivery/finance/risk/reporting data |
| data quality before digitalisation | do not use automation to mask poor source quality |

## Supervisory approach lessons

The report describes supervisory activities such as:

```txt
onsite inspections
deep dive reviews
risk-specific reviews
fire drills
self-assessments
continuous supervision
offsite reviews
independent reviews
```

Power interpretation:

| Supervisory tool | PFC equivalent |
|---|---|
| self-assessment | readiness scorecard |
| deep dive | focused graph/context audit |
| fire drill | stress/ad hoc scenario run |
| independent review | fact-checker/context-auditor |
| follow-up letter | blocked claims + remediation action |
| forceful measure | Circuit Breaker OPEN and escalation |

## Case-study patterns useful for skills

### Governance arrangements

Patterns:

```txt
group-wide data governance framework
clear roles and responsibilities
data owners and business data officers
board/senior management reporting
independent validation by second line
```

Skill use:

```txt
governance-sensitive output must show owner, source, validation, limitation, and escalation.
```

### IT infrastructure and data architecture

Patterns:

```txt
data lake rationalisation
central repositories
data dictionaries
data taxonomies
lineage and metadata
standardised data formats
data hubs
```

Skill use:

```txt
PFC graph should serve as a lightweight taxonomy and lineage layer for project planning/finance control.
```

### Risk data aggregation

Patterns:

```txt
preventive and detective controls
data reconciliation
variance analysis
SLA monitoring
formal adjustment process
KPI/KRI scorecards
issue logs
manual intervention tracking
```

Skill use:

```txt
Forecast/cost/report skills must expose derived_from, reconciliation status, manual adjustments, and data quality notes.
```

### Risk reporting

Patterns:

```txt
ad hoc data request governance
granular data availability
automated distribution
full audit trail
balance between granularity and usefulness
```

Skill use:

```txt
Report builder must provide concise output while preserving traceability and blocked claims.
```

## Guardrails from 2023 report

```txt
Do not overtrust bank/project self-assessment.
Do not assume board attention exists.
Do not assume implementation roadmap is funded or realistic.
Do not treat AI/digitalisation as solution without source data quality.
Do not ignore stress/ad hoc reporting capability.
Do not hide manual processes.
```

## Circuit breaker triggers inspired by 2023 findings

| Trigger | Breaker |
|---|---|
| self-assessed compliance but missing evidence | Evidence breaker |
| fragmented sources and no lineage | Context breaker |
| manual stress reporting without limitation label | Timeliness/Context breaker |
| official report from low-quality source data | Evidence breaker |
| digital output without data quality validation | Contract/Evidence breaker |
| unresolved long-standing data gap | Baseline breaker or escalation |
