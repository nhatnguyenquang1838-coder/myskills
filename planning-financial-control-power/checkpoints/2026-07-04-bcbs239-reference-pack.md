# Checkpoint — BCBS239 Markdown Reference Pack

Date: 2026-07-04
Scope: Convert two Basel Committee PDFs into skill-ready Markdown references.

## Source PDFs

```txt
1. BCBS, Principles for effective risk data aggregation and risk reporting, January 2013.
2. BCBS, Progress in adopting the Principles for effective risk data aggregation and risk reporting, November 2023.
```

## Added files

```txt
knowledge/references/bcbs239/README.md
knowledge/references/bcbs239/source-index.md
knowledge/references/bcbs239/01-governance-and-infrastructure.md
knowledge/references/bcbs239/02-risk-data-aggregation.md
knowledge/references/bcbs239/03-risk-reporting-practices.md
knowledge/references/bcbs239/04-supervisory-review-remediation.md
knowledge/references/bcbs239/05-2023-progress-lessons.md
knowledge/references/bcbs239/06-pfc-skill-guardrail-map.md
knowledge/references/bcbs239/07-bcbs239-skill-contract-guidance.md
```

## Design decision

The PDFs were not copied verbatim.

They were broken into skill-friendly guidance modules:

```txt
governance and infrastructure
risk data aggregation
risk reporting practices
supervisory review and remediation
2023 progress lessons
PFC guardrail mapping
DL Skill contract guidance
```

## How the Power uses this pack

```txt
BCBS239 principles -> PFC guardrails
2023 progress lessons -> adoption risk patterns
case studies -> examples only, not universal standard
principles -> skill contract and report control requirements
```

## Key controls derived

```txt
No source -> no fact
No baseline -> no official RAG
No resource + rate + budget -> no budget status
No decision -> no approval claim
No lineage -> no aggregation claim
No as-of date -> no current status claim
History/case study -> benchmark or pattern only
```

## Next improvement

```txt
1. Add BCBS239 compliance checklist template.
2. Add report quality checklist template.
3. Add schema-based validation script for source-linked claims.
4. Add DL Skill contract score update based on BCBS239 guidance.
```
