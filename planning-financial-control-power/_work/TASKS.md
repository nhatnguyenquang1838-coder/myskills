# Planning & Financial Control Power — Go-Live Tasks

Status legend:

```txt
TODO
DOING
BLOCKED
DONE
```

Priority legend:

```txt
P0 = required for MVP live
P1 = required for team pilot
P2 = useful after live
```

## P0 — Required for MVP live

| ID | Task | Owner | Status | Output |
|---|---|---|---|---|
| P0-01 | Create `_work/` planning control files | PFC | DONE | PLAN/TASKS/ROADMAP/DECISIONS/RISKS |
| P0-02 | Add run graph policy | PFC | TODO | `steering/16-run-graph-policy.md` |
| P0-03 | Add complex use-case gate | PFC | TODO | `steering/17-complex-use-case-gate.md` |
| P0-04 | Add baseline creation standard | PFC | TODO | `knowledge/use-cases/uc-00-create-controlled-baseline-standard.md` |
| P0-05 | Add Project Control Graph validator script | PFC | TODO | `tools/validate_project_control.py` |
| P0-06 | Add DL Skill contract validator script | PFC | TODO | `tools/validate_dl_contract.py` |
| P0-07 | Add sample valid project-control graph | PFC | TODO | `tests/fixtures/valid-project-control.yaml` |
| P0-08 | Add sample invalid project-control graph | PFC | TODO | `tests/fixtures/invalid-project-control.yaml` |
| P0-09 | Define full contract for DL-00 intake | PFC | TODO | `contracts/dl-skills/DL-00-CORE-cognitive-intake-gate.yaml` |
| P0-10 | Define full contract for DL-11 milestone planner | PFC | TODO | `contracts/dl-skills/DL-11-PLAN-release-milestone-planner.yaml` |
| P0-11 | Define full contract for DL-12 resource allocator | PFC | TODO | `contracts/dl-skills/DL-12-PLAN-resource-allocator.yaml` |
| P0-12 | Define full contract for DL-27 project cost calculator | PFC | TODO | `contracts/dl-skills/DL-27-FIN-project-cost-calculator.yaml` |
| P0-13 | Define full contract for DL-26 report builder | PFC | TODO | `contracts/dl-skills/DL-26-RPT-report-builder.yaml` |
| P0-14 | Add workspace bootstrap script for Linux/macOS | PFC | TODO | `scripts/install-workspace.sh` |
| P0-15 | Add workspace bootstrap script for Windows | PFC | TODO | `scripts/install-workspace.ps1` |
| P0-16 | Add UC-00 baseline dry-run scenario | PFC | TODO | `tests/scenarios/uc-00-baseline-dry-run.md` |
| P0-17 | Add expected output for contract-driven execution | PFC | TODO | `tests/expected-outputs/contract-driven-execution.md` |
| P0-18 | Add expected output for executive report breaker | PFC | TODO | `tests/expected-outputs/executive-report-breaker.md` |
| P0-19 | Update readiness scorecard after P0 complete | PFC | TODO | `tests/readiness-scorecard.md` |
| P0-20 | Update README with live usage | PFC | TODO | `README.md` update |

## P1 — Required for team pilot

| ID | Task | Owner | Status | Output |
|---|---|---|---|---|
| P1-01 | Verify exact Kiro hook schema | PFC | TODO | corrected hook templates |
| P1-02 | Add memory-index schema validator | PFC | TODO | `schemas/memory-index.schema.json` + tool |
| P1-03 | Add history-index template and validator | PFC | TODO | `templates/history-index.yaml` + schema |
| P1-04 | Add baseline completeness checklist template | PFC | TODO | `templates/baseline-completeness-check.md` |
| P1-05 | Add BCBS239 report quality checklist | PFC | TODO | `templates/bcbs239-report-quality-checklist.md` |
| P1-06 | Add dry run for milestone delay cascade | PFC | TODO | scenario + expected output |
| P1-07 | Add dry run for budget cut impact | PFC | TODO | scenario + expected output |
| P1-08 | Add dry run for history-as-truth blocker | PFC | TODO | scenario + expected output |
| P1-09 | Add one real sample project walkthrough | PFC | TODO | `examples/sample-project-walkthrough/` |
| P1-10 | Create v0.3 team pilot checklist | PFC | TODO | `_work/milestones/v0.3-team-pilot.md` |

## P2 — After live

| ID | Task | Owner | Status | Output |
|---|---|---|---|---|
| P2-01 | Add Jira import mapper contract | PFC | TODO | contract + mapping standard |
| P2-02 | Add Confluence evidence ingestion contract | PFC | TODO | contract + evidence mapping |
| P2-03 | Add spreadsheet finance importer contract | PFC | TODO | contract + template |
| P2-04 | Add deck/report generation path | PFC | TODO | report/deck output pack |
| P2-05 | Add dashboard generation sample | PFC | TODO | sample dashboard/report view |

## Current critical path

```txt
P0-02 run graph policy
-> P0-03 complex use-case gate
-> P0-05/06 validators
-> P0-09..13 critical DL contracts
-> P0-14/15 install scripts
-> P0-16..18 dry run tests
-> P0-19 rescore
-> P0-20 live README
```

## MVP live blocker list

```txt
BLOCKER-01: run graph policy missing
BLOCKER-02: no executable validation script
BLOCKER-03: top DL Skill contracts are still registry-level only
BLOCKER-04: install/bootstrap not created
BLOCKER-05: expected outputs not created
BLOCKER-06: hooks not schema-verified
```
