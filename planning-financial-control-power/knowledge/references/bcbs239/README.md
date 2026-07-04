# BCBS 239 Skill Reference Pack

Scope: Planning & Financial Control Power
Sources:

1. Basel Committee on Banking Supervision, *Principles for effective risk data aggregation and risk reporting*, January 2013.
2. Basel Committee on Banking Supervision, *Progress in adopting the Principles for effective risk data aggregation and risk reporting*, November 2023.

## Purpose

This folder converts the two BCBS 239 source PDFs into skill-usable Markdown guidance.

It is not a raw copy of the PDFs. It is a structured interpretation for Power, agent, skill contract, guardrail, reporting, and governance design.

## Files

| File | Purpose |
|---|---|
| `source-index.md` | Source inventory, trust level, and usage rule |
| `01-governance-and-infrastructure.md` | BCBS 239 Principles 1-2 translated into Power/skill guidance |
| `02-risk-data-aggregation.md` | Principles 3-6 translated into graph/data aggregation controls |
| `03-risk-reporting-practices.md` | Principles 7-11 translated into report-builder controls |
| `04-supervisory-review-remediation.md` | Principles 12-14 translated into audit/remediation controls |
| `05-2023-progress-lessons.md` | 2023 progress report lessons, gaps, and modern stress-event implications |
| `06-pfc-skill-guardrail-map.md` | Maps BCBS 239 principles to PFC guardrails, circuit breakers, and DL Skill contracts |
| `07-bcbs239-skill-contract-guidance.md` | Contract requirements that DL Skills should expose to support BCBS-style controls |

## How to use in skills

Use these references when a skill or Power flow deals with:

```txt
risk data quality
risk reporting
executive reporting
board/senior management reporting
data governance
manual workaround controls
lineage / taxonomy / evidence
stress/ad hoc reporting
forecast and risk data aggregation
control validation
remediation tracking
```

## Authority rule

```txt
BCBS 239 source PDFs = authoritative regulatory reference.
This folder = skill-friendly interpretation.
PFC Power standards = execution rules for this repository.
```

## Skill loading rule

Skills should load only the relevant chunk:

| Task | Load |
|---|---|
| Baseline governance / ownership | `01-governance-and-infrastructure.md` |
| Data aggregation / graph validity | `02-risk-data-aggregation.md` |
| Report quality / RAG output | `03-risk-reporting-practices.md` |
| Audit / remediation / supervisory response | `04-supervisory-review-remediation.md` |
| Modern gaps / stress events / adoption problems | `05-2023-progress-lessons.md` |
| Guardrail design | `06-pfc-skill-guardrail-map.md` |
| DL Skill contract design | `07-bcbs239-skill-contract-guidance.md` |
