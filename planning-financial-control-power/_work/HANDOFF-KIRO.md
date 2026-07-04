# Kiro Handoff — Finish PFC Power to MVP Live

Repo: `nhatnguyenquang1838-coder/myskills`

Target package: `planning-financial-control-power/`

## Mission

Finish the Planning & Financial Control Power to MVP-live validation status inside Kiro IDE.

MVP live means a user can bootstrap the Power into a workspace, validate graph/contracts, run baseline/report/change-control scenarios, and rely on Circuit Breaker + guardrails to block unsupported official claims.

## Boundary

PFC Power owns orchestration, graph, runtime, contracts, validation, guardrails, circuit breaker, checkpoint, and audit.

DL Skills are external black-box capabilities described by contracts only.

Do not modify or rebuild the DL Skill base. Do not copy DL Skill implementation into this Power. Do not treat samples as standards. Do not claim hooks are production-ready unless Kiro hook schema is verified.

## Read first

Read these files in order:

1. `README.md`
2. `_work/PLAN.md`
3. `_work/TASKS.md`
4. `_work/ROADMAP.md`
5. `_work/DECISIONS.md`
6. `_work/RISKS.md`
7. `_work/milestones/v0.2-contract-runtime-live.md`
8. `POWER.md`
9. `steering/13-use-case-standard-policy.md`
10. `steering/14-dl-skill-contract-policy.md`
11. `steering/15-runtime-execution-policy.md`
12. `steering/16-run-graph-policy.md`
13. `steering/17-complex-use-case-gate.md`
14. `knowledge/use-cases/use-case-standard-guideline.md`
15. `knowledge/use-cases/uc-00-create-controlled-baseline-standard.md`
16. `knowledge/runtime/pfc-runtime-execution-engine.md`
17. `knowledge/runtime/circuit-breaker-state-machine.md`
18. `contracts/dl-skill-contract-registry.md`
19. `contracts/dl-skills/`
20. `schemas/`
21. `tools/`
22. `scripts/`
23. `tests/use-cases/uc-test-suite-22.md`
24. `tests/use-cases/uc-test-matrix.md`
25. `tests/readiness-scorecard.md`

## Current status

Readiness score: `3.72 / 5`

Status: `MVP-live candidate`

Open blockers:

- `BLOCKER-06`: hooks not schema-verified
- `BLOCKER-07`: validators not yet run in a clean local checkout
- `BLOCKER-08`: bootstrap not yet tested in a real target workspace

Your job is to close or clearly document these blockers.

## Required architecture

Follow this pipeline strictly:

```txt
User request
-> Use Case Resolver
-> Readiness Mode Engine
-> Run Context Graph
-> DL Skill Contract Selector
-> Precondition Validation
-> DL Skill Execution as black box
-> Output Validation
-> Draft Graph Delta
-> Cascade / Context / Fact / Bias / Hallucination Checks
-> Circuit Breaker
-> Output / Write-back / Block
-> Checkpoint
```

Every meaningful output must include:

```txt
Mode:
Run type:
Use case:
Contracts used:
Skills called:
Graph nodes read:
Graph deltas proposed:
Circuit breaker state:
Allowed output:
Blocked claims:
Next action:
```

## Hard guardrails

```txt
No baseline -> no official RAG
No resource + rate + budget -> no budget status
No evidence -> no confirmed claim
No decision -> no approval claim
No contract -> no controlled skill call
History = benchmark only
DL Skills return draft deltas only
Only PFC writes approved deltas
```

## Branch rule

Create a separate branch or worktree, for example:

```txt
git checkout -b pfc-v0.2-live-validation
```

Do not work on an unrelated active branch.

## Required validation

From `planning-financial-control-power/`, install dependencies:

```txt
pip install pyyaml jsonschema
```

Run graph validation:

```txt
python tools/validate_project_control.py tests/fixtures/valid-project-control.yaml
python tools/validate_project_control.py tests/fixtures/invalid-project-control.yaml
```

Expected:

```txt
valid-project-control.yaml -> PASS
invalid-project-control.yaml -> FAIL
```

Run contract validation for all P0 contracts:

```txt
contracts/dl-skills/DL-00-CORE-cognitive-intake-gate.yaml
contracts/dl-skills/DL-11-PLAN-release-milestone-planner.yaml
contracts/dl-skills/DL-12-PLAN-resource-allocator.yaml
contracts/dl-skills/DL-27-FIN-project-cost-calculator.yaml
contracts/dl-skills/DL-26-RPT-report-builder.yaml
```

Expected: all 5 pass with `tools/validate_dl_contract.py`.

If anything fails, fix the schema, fixture, or contract. Do not bypass validation.

## Add E2E validation runner

Create:

```txt
tools/run_pfc_validation.py
```

It should run:

1. valid Project Control Graph fixture
2. invalid Project Control Graph fixture, expected fail
3. all 5 P0 DL Skill contracts

Expected summary:

```txt
PFC Validation Summary
- Project graph valid fixture: PASS
- Project graph invalid fixture: EXPECTED FAIL
- DL-00 contract: PASS
- DL-11 contract: PASS
- DL-12 contract: PASS
- DL-27 contract: PASS
- DL-26 contract: PASS
Overall: PASS
```

Also add:

```txt
tools/validation-report-template.md
```

## Test workspace bootstrap

Run the shell bootstrap against a temporary target workspace and verify `.pm/` is created with:

```txt
control/project-control.yaml
intake/project-intake.yaml
audit/readiness-score.md
audit/missing-data-log.md
audit/circuit-breaker-log.md
audit/context-retrieval-log.md
audit/run-execution-record.md
reports/
history/
checkpoints/
memory/memory-index.yaml
```

If bootstrap `project-control.yaml` is an M0 draft template and not schema-valid, document that clearly.

## Run 6 critical UC tests

Use `tests/use-cases/uc-test-suite-22.md`.

Run these first:

- UC-02 Start Project With Idea Only
- UC-01 Create Full Controlled Baseline
- UC-07 Update Milestone Date
- UC-15 Calculate Cost Forecast
- UC-20 Generate Executive Report
- UC-22 Unsupported RAG / Budget Claim Breaker

Create:

```txt
tests/use-cases/uc-test-results.md
```

Minimum rule:

```txt
If UC-22 fails, the Power is unsafe.
If UC-01 fails, complex UCs cannot run officially.
If UC-07 fails, cascade control is broken.
If UC-15 fails, finance forecast is unreliable.
```

## Hook schema verification

Current hook files are templates.

Verify actual Kiro hook schema in Kiro IDE or official docs.

If verified, update `hooks/`.

If not verified, keep status:

```txt
Hook templates only. Not production executable.
```

Update `_work/RISKS.md`, `_work/TASKS.md`, and `tests/readiness-scorecard.md` accordingly.

## Required files to update after work

Update:

```txt
_work/TASKS.md
_work/RISKS.md
tests/readiness-scorecard.md
README.md
```

Add checkpoint:

```txt
checkpoints/YYYY-MM-DD-kiro-live-validation.md
```

Checkpoint must include:

```txt
what was tested
commands run
pass/fail result
files changed
remaining blockers
new readiness score
```

## Acceptance criteria

MVP-live validation passes if:

```txt
[ ] graph validator passes valid fixture
[ ] graph validator fails invalid fixture as expected
[ ] all 5 P0 DL contracts pass schema validation
[ ] bootstrap script creates .pm runtime structure
[ ] 6 critical UCs have test results
[ ] UC-22 blocks fake Green/on-budget claim
[ ] UC-01 does not create M3 baseline without full support
[ ] UC-07 enforces cascade
[ ] UC-15 requires derived_from for cost
[ ] UC-20 blocks official executive report unless M3 + breaker CLOSED
[ ] checkpoint created
[ ] readiness score updated
```

Do not mark as team-ready unless all 22 UCs are tested, hook schema is verified, and a real workspace walkthrough exists.

## Final response expected from Kiro

Return:

```md
# Kiro Handoff Result — PFC Power

## Summary
## Commands Run
## Validation Results
## UC Test Results
## Files Changed
## Remaining Blockers
## Readiness Score Before / After
## Recommendation

PASS / PARTIAL / FAIL
```

## Short instruction

```txt
Finish v0.2 live validation, not new feature expansion.
Validate graph/contracts, test bootstrap, run 6 critical UCs, update scorecard/tasks/risks, checkpoint everything.
```
