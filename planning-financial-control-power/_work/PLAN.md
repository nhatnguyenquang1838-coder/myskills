# Planning & Financial Control Power — Go-Live Plan

Version: v0.2 planning draft
Date: 2026-07-04

## Goal

Bring the Planning & Financial Control Power from design skeleton to live usable Power.

Live means:

```txt
A user can install the Power into a workspace, start a project, create a baseline, run contract-driven DL Skills, validate outputs, and produce controlled draft/official reports with traceable graph, evidence, and circuit-breaker behavior.
```

## Non-goals

```txt
Do not rebuild DL Skills inside this Power.
Do not make DL Skills depend on PFC internals.
Do not treat samples as standards.
Do not claim hook execution is production-ready until Kiro hook schema is verified.
```

## Operating boundary

```txt
PFC Power owns:
- orchestration
- Project Control Graph
- Run Context Graph
- readiness mode
- use-case standard
- DL Skill contract validation
- output validation
- guardrails
- circuit breaker
- checkpoint/audit

DL Skills provide:
- black-box capability contracts
- bounded transformations
- draft outputs or graph deltas
```

## Definition of live

The Power is considered live when all these are true:

```txt
1. Install path is documented and tested.
2. Workspace `.pm/` skeleton can be generated from templates.
3. Project Control Graph schema validates.
4. Minimum DL Skill contracts exist for baseline creation and reporting.
5. UC-00 Create Controlled Baseline can run in dry-run mode.
6. Contract-driven execution scenario passes.
7. Circuit Breaker blocks unsupported official RAG/budget/report claims.
8. Report output contains required control header.
9. Checkpoint/audit records are created for meaningful runs.
10. Readiness score reaches at least 3.7/5 for MVP live.
```

## Release stages

| Stage | Target | Description | Exit gate |
|---|---|---|---|
| G0 | Repo control | Create plan, tasks, risks, decisions | `_work/` exists |
| G1 | Standards locked | Use-case, runtime, contract, graph standards stable | Steering files reviewed |
| G2 | Contracts minimum | Critical DL Skill contracts defined | C3+ for P0 skills |
| G3 | Validation engine | Schema + basic validation scripts | sample graph and contracts validate |
| G4 | Workspace install | Install scripts/templates create `.pm/` | dry install works |
| G5 | Dry-run scenarios | UC-00, milestone delay, executive report dry-runs | expected outputs pass |
| G6 | Hook verification | Kiro hooks verified against official schema | hook templates corrected |
| G7 | MVP live | Usable in one real workspace | readiness >= 3.7 |
| G8 | Team pilot | Used by another project/person | readiness >= 4.0 |

## Priority workstreams

### WS1 — Power standards

```txt
Finalize standards:
- use-case standard
- runtime execution policy
- run graph policy
- complex use case gate
- output contract
- circuit breaker state machine
```

### WS2 — DL Skill contract layer

```txt
Define minimum contracts for critical external DL Skills:
- intake
- project setup
- document intake
- milestone planner
- dependency tracker
- resource allocator
- budget/cost tracker
- project cost calculator
- report builder
- readiness check
```

### WS3 — Graph and validation

```txt
Build:
- Project Control Graph schema
- memory index schema
- contract schema
- validation script
- sample valid graph
- sample invalid graph
```

### WS4 — Workspace bootstrap

```txt
Build install/bootstrap scripts:
- install-workspace.sh
- install-workspace.ps1
- create .pm structure
- copy templates
- initialize project-control.yaml
```

### WS5 — Runtime scenarios

```txt
Test:
- M0 empty start
- UC-00 full baseline creation
- contract-driven execution
- milestone delay cascade
- executive report with breaker
- history-as-truth blocker
```

### WS6 — Reporting and output authority

```txt
Finalize:
- report header
- blocked claims format
- run-execution-record
- checkpoint template
- executive report template
```

### WS7 — Hook readiness

```txt
Verify Kiro hook schema before treating hooks as executable.
Until verified, hooks remain prompt templates.
```

## MVP go-live scope

MVP live includes:

```txt
- installable Power package
- workspace .pm bootstrap
- use-case standard
- runtime execution contract
- Project Control Graph schema
- contract registry and top contracts
- circuit breaker state machine
- BCBS239 guardrail reference pack
- dry-run scenario tests
- readiness scorecard
```

MVP live excludes:

```txt
- real Jira/Confluence/Mail integrations
- fully automated hook execution
- all DL Skill contracts
- production multi-project usage
- UI/dashboard generation
```

## Go-live decision gate

Before declaring live:

```txt
[ ] Readiness >= 3.7
[ ] P0 tasks closed
[ ] No OPEN P0 risks
[ ] Contract-driven scenario passes
[ ] UC-00 baseline dry run passes
[ ] Report breaker test passes
[ ] Install/bootstrap tested in clean workspace
[ ] README has live usage instructions
```

## Live usage pattern

```txt
1. Install Power into workspace.
2. Run onboarding.
3. Create `.pm/control/project-control.yaml` skeleton.
4. Import or enter project materials.
5. Run readiness check.
6. Build baseline if material is sufficient.
7. Run planning/finance/reporting use cases.
8. Use circuit breaker to block unsupported claims.
9. Write approved deltas only.
10. Checkpoint meaningful runs.
```
