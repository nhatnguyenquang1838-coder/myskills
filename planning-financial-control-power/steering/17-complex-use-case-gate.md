# 17 — Complex Use Case Gate

## Purpose

Prevent complex Planning & Financial Control use cases from producing official outputs without sufficient baseline, graph, evidence, and contract support.

## Core rule

```txt
Complex use cases require baseline readiness check first.
```

## Complex use cases

A use case is complex if it involves at least one of:

```txt
baseline creation or upgrade
official report / executive report
RAG status
budget status / forecast vs budget
scope change
milestone delay
resource replan
rate card change
budget cut
history/memory used in decision output
persistent graph write-back
```

## Required gate checks

Before running a complex UC, PM Controller must check:

```txt
1. Project Control Graph exists.
2. Baseline version exists if official output is requested.
3. Readiness mode supports requested output.
4. Required graph node chain exists.
5. DL Skill contracts exist for selected skills.
6. Required evidence/assumption/decision support exists.
7. Circuit Breaker can evaluate the output.
```

## Required node chains

### Official report

```txt
MS + RA + FCST + RISK + EVD + DEC + baseline_version
```

### Budget status

```txt
RA + RATE + COST + FCST + approved_budget + derived_from
```

### Milestone delay impact

```txt
MS -> WP -> RA -> COST -> FCST -> RPT
plus RISK/ASM/EVD/DEC
```

### Scope change impact

```txt
new/changed WP -> MS -> RA -> COST -> FCST -> RPT
plus RISK/ASM/EVD/DEC/CR
```

### Baseline creation

```txt
WP + MS + DEP + RA + RATE + COST + FCST + RISK + EVD + DEC + ASM
```

## Gate outcomes

| Outcome | Meaning | Behavior |
|---|---|---|
| PASS | required data and contracts exist | run controlled workflow |
| PARTIAL | enough for draft/scenario only | downgrade to M1/M2 output |
| FAIL | critical data/contract missing | open Circuit Breaker and block official claims |

## Downgrade rules

```txt
No baseline -> no official RAG/report
No resource + rate + budget -> no budget status
No evidence -> no confirmed claim
No decision -> no approved claim
No cascade -> no report update
No contract -> no controlled skill call
```

## Circuit breakers

| Missing/failed gate | Breaker |
|---|---|
| baseline missing | Baseline breaker |
| cost basis missing | Finance breaker |
| evidence missing | Evidence breaker |
| graph links missing | Cascade breaker |
| stale context | Context breaker |
| contract missing/incomplete | Contract breaker |
| history used as current truth | History-bias breaker |

## Required output on gate failure

```txt
Complex UC gate: FAIL or PARTIAL
Missing data:
Missing contracts:
Blocked claims:
Allowed fallback:
Recovery questions:
Next action:
```

## Rule for official output

```txt
Official output requires:
- M3 mode
- required node chain exists
- required DL Skill contracts valid
- fact-check pass
- circuit breaker CLOSED
```
