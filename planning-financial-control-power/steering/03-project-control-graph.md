# 03 — Project Control Graph

## Purpose

The Project Control Graph is the single source of truth for planning and financial control.

## Required chain

```txt
WP -> MS -> RA -> COST -> FCST -> RPT
```

| Code | Node |
|---|---|
| WP | Work Package |
| MS | Milestone |
| RA | Resource Allocation |
| COST | Cost Line |
| FCST | Forecast |
| RPT | Report |

## Linked control nodes

Every major node should link to relevant control nodes:

```txt
EVD = Evidence
ASM = Assumption
DEC = Decision
RISK = Risk
CR = Change Request
MD = Missing Data
HIST = History Reference
```

## Required node fields

```yaml
id:
type:
name:
status:
baseline_version:
confidence:
source_ids:
assumption_ids:
decision_ids:
risk_ids:
last_updated:
```

## Claim rule

Any date, cost, resource, RAG, delay, or delivery-status claim must trace back to one of:

```txt
evidence_id
assumption_id
decision_id
derived_from
baseline_version
```

## Bad pattern

```txt
Timeline looks delayed.
```

## Good pattern

```txt
Timeline is Amber because MS-003 moved from 2026-07-15 to 2026-07-22 and is linked to RISK-002 and CR-001.
```
