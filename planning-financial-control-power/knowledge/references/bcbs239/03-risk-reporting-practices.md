# BCBS 239 — Risk Reporting Practices

Source: SRC-BCBS239-2013, Principles 7-11.

## Purpose for skills

Use this file when a skill generates or validates:

```txt
weekly status report
executive status report
SteerCo update
risk report
forecast report
RAG report
decision-needed report
ad hoc risk/impact report
```

## Principle 7 — Report Accuracy

Core meaning:

```txt
Risk reports must accurately and precisely convey aggregated data and should be reconciled and validated.
```

## PFC implementation

| Requirement | PFC mechanism |
|---|---|
| report reconciled to data | report `source_ids` link to graph nodes |
| validation rules | report fact-check and output contract |
| error/weakness identification | blocked claims and missing-data log |
| approximation reliability | assumptions, confidence, scenario label |

## Principle 8 — Comprehensiveness

Core meaning:

```txt
Risk reports must cover all material risk areas relevant to the organisation and recipient.
```

## PFC interpretation

For PFC, a comprehensive project/control report should cover:

```txt
timeline
resource
cost / forecast / budget
risks
issues / blockers
dependencies
decisions needed
assumptions and missing data
```

## Principle 9 — Clarity and Usefulness

Core meaning:

```txt
Reports must be clear, concise, understandable, decision-useful, and tailored to the recipient.
```

## PFC controls

| Requirement | PFC mechanism |
|---|---|
| tailored to recipient | report audience metadata |
| balance data and interpretation | output sections: facts, analysis, decisions |
| meaningful recommendations | decision-needed list with impact |
| avoid ambiguity | blocked claims and confidence labels |

## Principle 10 — Frequency

Core meaning:

```txt
Report frequency should reflect recipient needs, risk type, speed of change, and stress/crisis conditions.
```

## PFC controls

| Requirement | PFC mechanism |
|---|---|
| normal reporting cadence | weekly/monthly report metadata |
| stress/crisis cadence | ad hoc/stress report run type |
| ability to produce in timeframe | timeliness guardrail |
| periodic review | checkpoint and report feedback loop |

## Principle 11 — Distribution

Core meaning:

```txt
Reports must be distributed to relevant parties while maintaining confidentiality.
```

## PFC controls

| Requirement | PFC mechanism |
|---|---|
| relevant recipients | stakeholder/audience field |
| confidentiality | output classification and distribution note |
| timely dissemination | report frequency + timestamp |

## Guardrails

```txt
No report source_ids -> no official report
No baseline -> no official RAG
No finance basis -> no budget status
No audience -> report must be generic draft
No decision impact -> do not fabricate recommendations
No confidentiality context -> avoid sensitive distribution claim
```

## Circuit breakers

| Breaker | Opens when |
|---|---|
| Evidence breaker | report claim lacks graph/source support |
| Baseline breaker | official RAG/report requested without M3 baseline |
| Finance breaker | budget/forecast claim lacks RA/RATE/budget basis |
| Context breaker | report uses stale/unlinked context |
| History-bias breaker | historical benchmark used as current status |

## Skill contract requirements

Report-building DL Skills must declare:

```txt
required input graph nodes
required source IDs
allowed report types
allowed output authority
forbidden claims
required fact-checks
recipient/audience requirements
blocked-output behavior
```

## Required report output header

```txt
Mode:
Run type:
Report type:
Audience:
Reporting period:
Graph nodes read:
Source IDs used:
Circuit breaker state:
Allowed output:
Blocked claims:
Confidence:
```

## Report quality checklist

```txt
[ ] accurate: claims link to graph/source
[ ] comprehensive: covers material status dimensions
[ ] clear: executive summary is understandable
[ ] useful: decision-needed items are explicit
[ ] timely: as-of date and reporting period shown
[ ] distributed safely: audience/confidentiality noted
```
