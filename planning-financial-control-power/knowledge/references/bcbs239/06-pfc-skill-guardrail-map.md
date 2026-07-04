# BCBS 239 to PFC Skill Guardrail Map

## Purpose

Map BCBS 239 principles and 2023 progress lessons into Planning & Financial Control Power controls.

This file is used by:

```txt
pm-controller
pm-fact-checker
pm-context-auditor
report-builder
finance-analyst
DL Skill contract validation
```

## Principle-to-control map

| BCBS area | Principle | PFC guardrail | Circuit breaker |
|---|---|---|---|
| Governance | P1 Governance | no controlled claim without owner/evidence/decision | Baseline / Evidence |
| Infrastructure | P2 Data architecture / IT | graph IDs, source IDs, lineage, metadata required | Context / Contract |
| Aggregation | P3 Accuracy and integrity | every calculation must have source or derived_from | Evidence |
| Aggregation | P4 Completeness | material missing data must be logged | Baseline / Evidence |
| Aggregation | P5 Timeliness | stale context cannot support current claim | Context |
| Aggregation | P6 Adaptability | ad hoc/scenario output must be scoped and labelled | Context / Baseline |
| Reporting | P7 Report accuracy | report claims must reconcile to graph source_ids | Evidence |
| Reporting | P8 Comprehensiveness | reports cover material dimensions or state omissions | Baseline / Evidence |
| Reporting | P9 Clarity/usefulness | output must be decision-useful and audience-specific | Evidence |
| Reporting | P10 Frequency | report as-of date and cadence must be clear | Context |
| Reporting | P11 Distribution | audience/confidentiality must be noted when relevant | Evidence |
| Supervision | P12 Review | readiness/checkpoint/audit must be possible | Contract / Evidence |
| Supervision | P13 Remediation | gaps become actions with owner/due date | Baseline |
| Supervision | P14 Cooperation | shared source of truth avoids conflicting views | Context |

## PFC guardrail library

### G-01 — Evidence-backed claims

```txt
Every date, cost, RAG, resource, risk, dependency, or approval claim must link to evidence_id, assumption_id, decision_id, derived_from, baseline_version, or missing_data_id.
```

### G-02 — Graph lineage

```txt
Every output must identify graph nodes read and graph deltas proposed.
```

### G-03 — Completeness limitation

```txt
If material data is missing, output must state missing data and block completeness/baseline claims.
```

### G-04 — Timeliness limitation

```txt
If source data is stale or as-of date is unclear, output cannot claim current status.
```

### G-05 — Manual workaround label

```txt
If output uses manual adjustment, expert judgment, or approximation, it must be labelled and confidence reduced.
```

### G-06 — Report recipient clarity

```txt
Reports must state audience, reporting period, allowed use, and blocked claims.
```

### G-07 — Stress/ad hoc mode

```txt
Stress or ad hoc requests must be scoped as scenario unless controlled baseline and timely data exist.
```

### G-08 — Remediation path

```txt
Material gaps must produce missing-data or remediation items with owner/due date if possible.
```

## Bias controls

| Bias risk | Control |
|---|---|
| Self-assessment optimism | require independent/fact-check result |
| Stale baseline | current baseline version wins |
| Recency bias | latest source is not automatically approved truth |
| Historical bias | history is benchmark/risk signal only |
| Confirmation bias | output must include counter-signals and missing data |
| Automation bias | AI/report automation cannot bypass source quality checks |

## Hallucination controls

```txt
No source -> no fact
No baseline -> no official RAG
No rate/resource/budget -> no budget status
No decision -> no approval claim
No owner -> no governance claim
No lineage -> no aggregation claim
No as-of date -> no current status claim
```

## Skill contract controls

Each DL Skill contract must declare:

```txt
accepted graph nodes
required evidence
output authority
produced graph deltas
forbidden claims
required guardrails
required circuit breakers
failure mode for missing data
```

## Report-builder controls

Before a report can be official:

```txt
1. Mode must be M3.
2. Controlled baseline must exist.
3. Report source_ids must exist.
4. Budget claim must have finance basis.
5. Risk claim must have risk source or assumption.
6. Missing data must be shown.
7. Circuit Breaker must be CLOSED.
```

## Cost/forecast controls

Before a cost forecast can be treated as reliable:

```txt
1. Resource allocation exists.
2. Rate card or explicit rate assumption exists.
3. Duration exists.
4. Formula/derived_from exists.
5. Budget exists if budget variance/RAG is requested.
6. Assumptions are labelled.
```

## Context controls

Before memory/history/context can support output:

```txt
1. Context is linked to graph node.
2. Source date is known.
3. Baseline version conflict is checked.
4. History is labelled benchmark_only unless approved as evidence.
5. Retrieval is logged if it influences output.
```
