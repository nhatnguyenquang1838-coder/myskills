# 18 — Workflow Enforcement Policy

## Purpose

Define mandatory enforcement gates for every Planning & Financial Control workflow.

This policy turns standards into runtime checks.

## Core rule

```txt
No workflow step is complete until its enforcement gate passes or downgrades/blocks the output.
```

## Enforcement gates

| Gate | Name | Runs when | Main breaker |
|---|---|---|---|
| E0 | Intent gate | every user request | Contract breaker if unsupported intent |
| E1 | Readiness gate | before output authority is selected | Baseline breaker |
| E2 | Graph gate | before loading context or skill execution | Context/Baseline breaker |
| E3 | Context and memory gate | before complex/report/history workflows | Context/History-bias breaker |
| E4 | Contract gate | before every DL Skill call | Contract breaker |
| E5 | Skill output gate | after every DL Skill output | Contract/Evidence breaker |
| E6 | Cascade gate | after any graph-linked change | Cascade breaker |
| E7 | Finance basis gate | before any cost/budget/forecast claim | Finance breaker |
| E8 | Report and claim gate | before report/output publish | Evidence/Baseline/Finance breaker |
| E9 | Write-back gate | before graph mutation | Baseline/Contract breaker |
| E10 | Checkpoint gate | after meaningful run | Evidence/Review guardrail |

## E0 — Intent gate

Required checks:

```txt
- request maps to known UC or unsupported intent
- request has target project or requires intake
- request output type is identified
```

Fail behavior:

```txt
unsupported intent -> ask critical clarification or return unsupported capability
```

## E1 — Readiness gate

Required checks:

```txt
- mode M0/M1/M2/M3 selected
- requested output authority is compatible with mode
- M3 is not assumed from user wording
```

Fail behavior:

```txt
block official output or downgrade to draft/scenario
```

## E2 — Graph gate

Required checks:

```txt
- Project Control Graph exists, or Intake Gate creates skeleton
- target graph IDs identified when needed
- required node chain exists for complex UC
- missing graph links become MD-* items
```

Fail behavior:

```txt
create missing-data item and open Baseline/Context/Cascade breaker as needed
```

## E3 — Context and memory gate

Required checks:

```txt
- load current graph first
- load memory only by linked graph IDs
- history labelled benchmark_only unless approved as evidence
- stale/conflicting memory blocked or downgraded
```

Fail behavior:

```txt
open Context or History-bias breaker
```

## E4 — Contract gate

Required checks:

```txt
- DL Skill contract exists
- contract supports current UC
- required inputs/preconditions exist
- contract maturity supports requested output authority
```

Fail behavior:

```txt
open Contract breaker; do not call skill for controlled workflow
```

## E5 — Skill output gate

Required checks:

```txt
- required outputs returned
- output format usable
- output stays within authority
- produced deltas target allowed graph nodes
- forbidden claims absent
```

Fail behavior:

```txt
reject output, downgrade, or request recovery
```

## E6 — Cascade gate

Required checks:

```txt
- changed WP checks MS/RA/COST/FCST/RPT
- changed MS checks RA/COST/FCST/RPT
- changed RA checks MS/COST/FCST/RPT
- changed RATE/COST checks FCST/RPT
- changed RISK/ASM/DEC checks all linked report claims
```

Fail behavior:

```txt
open Cascade breaker; block report publish
```

## E7 — Finance basis gate

Required checks:

```txt
- cost claim has RA + RATE/rate assumption + duration
- budget status has approved budget + forecast + threshold/rule
- every amount has derived_from or source_id
```

Fail behavior:

```txt
open Finance breaker; allow assumption/range only
```

## E8 — Report and claim gate

Required checks:

```txt
- report has source_ids
- RAG permitted only if mode and baseline allow
- budget/resource/timeline claims supported
- blocked claims visible
- counter-signals included for executive output
```

Fail behavior:

```txt
open Evidence/Baseline/Finance breaker; downgrade report
```

## E9 — Write-back gate

Required checks:

```txt
- run type allows write-back
- user approval exists
- graph schema validation passes or is scheduled
- breaker state CLOSED for official write-back
- previous baseline preserved if baseline changes
```

Fail behavior:

```txt
keep as draft delta; do not mutate Project Control Graph
```

## E10 — Checkpoint gate

Required checks:

```txt
- meaningful runs create run execution record
- baseline/report/change-control runs create checkpoint
- breaker OPEN/HALF_OPEN creates blocked claim record
```

Fail behavior:

```txt
output must state audit gap if checkpoint cannot be written
```

## Universal output enforcement header

Every meaningful output must include:

```txt
Mode:
Run type:
Use case:
Enforcement gates run:
Contracts used:
Skills called:
Graph nodes read:
Graph deltas proposed:
Circuit breaker state:
Guardrails applied:
Blocked claims:
Write-back decision:
Next action:
```

## Prohibited behavior

Agents must not:

```txt
skip contract validation
skip readiness mode
skip graph target selection
publish report after change without cascade check
state budget status without finance basis
state approval without decision_id
use history as current truth
write draft deltas as controlled graph truth
hide blocked claims
```
