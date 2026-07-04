# BCBS 239 — Governance and Infrastructure

Source: SRC-BCBS239-2013, Principles 1-2.

## Purpose for skills

Use this file when a skill designs or validates:

```txt
data governance
project control graph ownership
evidence ownership
risk/reporting framework
IT/data architecture assumptions
baseline approval
board/senior management reporting responsibilities
```

## Principle 1 — Governance

Core meaning:

```txt
Risk data aggregation and risk reporting must be governed like a critical risk-management capability.
Board and senior management must oversee ownership, resources, standards, validation, and limitations.
```

## Skill interpretation

A skill must not treat data/report output as an isolated artifact. It must ask:

```txt
Who owns this data?
Who owns this report?
What evidence supports it?
Who approved it?
What limitations exist?
What validation occurred?
```

## PFC implementation

| Governance expectation | PFC mechanism |
|---|---|
| board/senior management ownership | `decision_ids`, `owner`, `baseline_version` |
| documented framework | `project-control.yaml`, standards, contract registry |
| independent validation | `fact-check`, `context-audit`, `circuit-breaker` |
| limitations known | `missing_data`, `assumptions`, `blocked_claims` |
| data-quality risk management | evidence guardrail, source confidence, graph validation |
| new initiatives consider data/reporting impact | change-control use cases and cascade checks |

## Principle 2 — Data architecture and IT infrastructure

Core meaning:

```txt
Data architecture and IT infrastructure must support risk data aggregation and reporting in normal conditions and stress/crisis situations.
```

## Skill interpretation

A skill must check whether its output depends on:

```txt
manual workarounds
unclear source systems
fragmented data
missing lineage
missing taxonomy
stress/crisis reporting gaps
```

## PFC implementation

| Architecture expectation | PFC mechanism |
|---|---|
| consistent data taxonomy | graph node types: WP, MS, RA, RATE, COST, FCST, RISK, DEC, EVD, ASM |
| metadata and identifiers | every node has `id`, support IDs, confidence, baseline version |
| clear ownership | owner fields and decision/evidence links |
| controls across lifecycle | runtime execution record + checkpoint |
| business continuity / stress support | ad hoc/scenario run types and timeliness guardrails |

## Guardrails

```txt
No owner -> no controlled baseline claim
No evidence -> no confirmed data/report claim
No validation -> no official report
No baseline version -> no official RAG
Manual workaround -> label as limitation
```

## Circuit breakers

| Breaker | Opens when |
|---|---|
| Baseline breaker | baseline or official report requested without governance support |
| Evidence breaker | governance/ownership/approval claim lacks evidence |
| Context breaker | data source or report context is stale/unlinked |
| Contract breaker | DL Skill lacks contract for required governance outputs |

## Skill contract requirements

A DL Skill supporting governance or infrastructure must declare:

```txt
required inputs
source/evidence requirement
ownership fields
validation expectations
known limitations
whether it creates draft deltas or report-only output
```

## Output pattern

Every governance-sensitive output should include:

```txt
Governance status:
Owner:
Evidence used:
Decision / approval status:
Known limitations:
Validation performed:
Blocked claims:
```
