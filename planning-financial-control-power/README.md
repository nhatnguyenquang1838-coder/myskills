# Planning & Financial Control Power

Version: `0.2.0-draft`
Status: MVP-live candidate

This Kiro Power coordinates planning, resource allocation, cost calculation, reporting, intake/onboarding, context loading, historical data usage, DL Skill contract routing, workflow enforcement, native Kiro hooks, bounded multi-agent convergence, parallel-safe agent action logging, deterministic finance checks, and anti-hallucination controls.

## Core model

The Power does not manage Planning and Finance as disconnected documents. It uses one linked **Project Control Graph**.

```txt
Work Package -> Milestone -> Resource Allocation -> Cost Line -> Forecast -> Report
       \             \              \                  \            \
      Evidence      Assumption      Decision           Risk        Change Request
```

## Boundary

```txt
PFC Power owns:
- orchestration
- Project Control Graph
- Run Context Graph
- readiness mode
- use-case standard
- bounded convergence loops
- State Lock for controlled graph writes
- DL Skill contract validation
- output validation
- deterministic finance invariants
- BCBS239 action lineage tags
- guardrails
- circuit breaker
- enforcement gates
- native Kiro hook bundle
- parallel-safe agent action logging
- checkpoint/audit

DL Skills provide:
- black-box capability contracts
- bounded transformations
- draft outputs or graph deltas
```

## Main components

```txt
POWER.md
steering/      operating policies and control rules
contracts/     external DL Skill contracts
schemas/       Project Control Graph, contract, audit, and hook schemas
tools/         validators, output checkers, logging utilities
scripts/       workspace bootstrap scripts
skills/        Power-owned support skills
agents/        role definitions
templates/     reusable workspace starter files
hooks/         native Kiro v1 hook bundle and legacy hook templates
knowledge/     reusable PM methods, BCBS239 references, standards, patterns
tests/         scenarios, fixtures, expected outputs, enforcement matrix
_work/         plan/tasks/risks/decisions to bring Power live
```

## Operating modes

| Mode | Meaning | Allowed output |
|---|---|---|
| M0 | Empty Start | Skeleton, intake questions, assumptions, missing-data log |
| M1 | Rough Planning | Draft timeline, rough resource demand, draft report |
| M2 | Forecast Ready | Cost forecast, variance, planning-finance impact |
| M3 | Controlled Baseline | RAG, executive report, baseline variance, change control |

## Execution patterns

| Pattern | Use when | Control rule |
|---|---|---|
| Linear cascade | one agent output feeds the next without conflict | validate each output then continue |
| Bounded-Convergence-Loop | agents return conflicting but negotiable deltas | negotiate up to `MAX_ITERATIONS = 3`, then converge/downgrade/block |

Bounded convergence is used for conflicts such as:

```txt
budget cut -> resource conflict -> timeline delay -> forecast recalculation
```

Hard rules:

```txt
MAX_ITERATIONS = 3
No unbounded agent debate
No full conversation replay into each iteration
No graph write during negotiation
No invented compromise after iteration 3
```

## State Lock

Controlled graph writes must use a State Lock.

```txt
.pm/control/.project-control.lock
```

State Lock protects:

```txt
.pm/control/project-control.yaml
templates/project-control.yaml when used as a controlled baseline source
baseline_freeze
controlled_update
bounded_convergence
forecast/cost recalculation write-back
```

Write-back requires:

```txt
State Lock acquired
state_hash_before still matches
breaker CLOSED
schema validation passed
programmatic invariants passed
BCBS239 lineage tags present
user approval if persistent graph mutation is requested
```

## Non-negotiable rules

```txt
No baseline -> no official RAG
No rate/resource/budget data -> no reliable budget status
No deterministic reconciliation -> no cost/budget write-back
No BCBS239 principle tag -> no semantic action log validity
No evidence -> mark as assumption
No link -> no claim
No DL Skill contract -> no controlled skill call
History can challenge the plan, not replace the baseline
DL Skills return draft deltas only; PFC controls write-back
MCP stdio tools must not write diagnostics to stdout
Parallel runs must write to per-run log files
Never pass full trailing conversation history after a Circuit Breaker trip
```

## Live definition

The Power is considered MVP live when a user can:

```txt
1. Install/bootstrap `.pm/` into a target workspace.
2. Create or load a Project Control Graph.
3. Validate graph and DL Skill contracts.
4. Run UC-00 controlled-baseline dry run.
5. Run contract-driven planning/finance/reporting flows.
6. Block unsupported official claims via Circuit Breaker.
7. Produce run execution records and checkpoints.
8. Capture per-run semantic action logs for later analysis.
9. Install native Kiro v1 hooks into `.kiro/hooks/`.
10. Run deterministic finance invariants before budget/cost write-back.
```

## Bootstrap target workspace

Linux/macOS:

```bash
bash scripts/install-workspace.sh /path/to/target-project
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install-workspace.ps1 -TargetDir C:\path\to\target-project
```

Created runtime structure:

```txt
.pm/
├── control/project-control.yaml
├── intake/project-intake.yaml
├── audit/readiness-score.md
├── audit/missing-data-log.md
├── audit/circuit-breaker-log.md
├── audit/context-retrieval-log.md
├── audit/run-execution-record.md
├── audit/runs/
├── reports/
├── history/
├── checkpoints/
└── memory/memory-index.yaml

.kiro/
├── hooks/pfc-workspace-hooks.json
└── logs/runs/
```

## Native Kiro hooks

Source hook bundle:

```txt
hooks/kiro-v1/pfc-workspace-hooks.json
```

Validate hook schema:

```bash
python tools/validate_kiro_hooks.py hooks/kiro-v1/pfc-workspace-hooks.json
```

Installed target after bootstrap:

```txt
.kiro/hooks/pfc-workspace-hooks.json
```

Hooks must declare:

```txt
execution_tier: blocking | async
```

Tier behavior:

| Tier | Behavior | Examples |
|---|---|---|
| blocking | synchronous, protects critical path | schema checks, baseline checks, deterministic finance invariant checks |
| async | background, non-blocking quality review | context audit, workflow gap review, BCBS239 qualitative review |

Enabled by default:

```txt
pfc-cascade-check        # async
pfc-report-fact-check    # async
```

Disabled by default until narrowed in Kiro IDE pilot:

```txt
pfc-enforcement-preflight       # blocking
pfc-enforcement-contract-gate   # blocking
pfc-enforcement-output-gate     # blocking
pfc-enforcement-writeback-gate  # blocking
```

## Production logging model

Use hybrid, parallel-safe logging:

```txt
Kiro agent keeps working.
Python tools log safely to stderr and per-run local files.
LLM analyzes logs only when explicitly requested.
```

| Layer | File | Purpose | Default |
|---|---|---|---|
| Safe tool debug | `.kiro/logs/runs/{run_id}.log` | tail one Kiro run without interleaving | ON |
| Semantic audit | `.pm/audit/runs/{run_id}.agent-action.ndjson` | deep analysis and continuous improvement | ON |
| Turn analysis | `.pm/audit/runs/{run_id}.turn-analysis.md` | human-readable review | ON-DEMAND |
| Raw IDE events | `.pm/audit/runs/{run_id}.ide-event.ndjson` | debug/failure trace | OPTIONAL |
| Aggregate debug | `.kiro/logs/power_steps.log` | convenience only, not source of truth | OFF by default |

Semantic action logs require BCBS239 tags from:

```txt
knowledge/references/bcbs239/
```

Allowed tags:

```txt
01-governance-and-infrastructure
02-risk-data-aggregation
03-risk-reporting-practices
04-supervisory-review-remediation
05-2023-progress-lessons
06-pfc-skill-guardrail-map
07-bcbs239-skill-contract-guidance
```

Safe Python utility:

```txt
tools/kiro_safe_logging.py
```

Usage:

```python
from tools.kiro_safe_logging import setup_kiro_logger, append_agent_action_log

run_id = "RUN-001"
logger = setup_kiro_logger(run_id=run_id)
logger.info("Step: checking readiness")

append_agent_action_log({
    "run_id": run_id,
    "action_id": "ACT-001",
    "agent": "pm-controller",
    "action_type": "READINESS_CHECKED",
    "status": "PASS",
    "bcbs239_principle_tag": ["01-governance-and-infrastructure"],
    "summary": "Readiness mode selected."
})
```

Live tail for one run:

```bash
tail -f .kiro/logs/runs/RUN-001.log
```

Smoke-test safe logging:

```bash
python tools/kiro_safe_logging.py
```

Expected smoke files:

```txt
.kiro/logs/runs/RUN-SMOKE.log
.pm/audit/runs/RUN-SMOKE.agent-action.ndjson
.pm/audit/runs/RUN-SMOKE.ide-event.ndjson
.pm/audit/runs/RUN-SMOKE.turn-analysis.md
```

MCP stdio safety rule:

```txt
stdout = protocol channel
stderr/local file = logging channel
```

Do not use Python `print()` or Node `console.log()` for diagnostics inside stdio MCP tools. Use `logging`, `print(..., file=sys.stderr)`, `console.error()`, or append-only local log files.

## Circuit Breaker context isolation

After any `HALF_OPEN` or `OPEN` breaker state:

```txt
Do not pass full trailing conversation history.
Run Isolate-and-Condense.
Inject only the failure recovery packet.
```

Allowed recovery packet:

```txt
1. 2-sentence failure summary
2. exact breached constraint from contract/schema/policy
3. structured error log from templates/circuit-breaker-log.md
```

## Validate assets

Install dependencies:

```bash
pip install pyyaml jsonschema
```

Validate graph:

```bash
python tools/validate_project_control.py tests/fixtures/valid-project-control.yaml
python tools/validate_project_control.py tests/fixtures/invalid-project-control.yaml
```

Validate P0 DL Skill contracts:

```bash
python tools/validate_dl_contract.py contracts/dl-skills/DL-00-CORE-cognitive-intake-gate.yaml
python tools/validate_dl_contract.py contracts/dl-skills/DL-11-PLAN-release-milestone-planner.yaml
python tools/validate_dl_contract.py contracts/dl-skills/DL-12-PLAN-resource-allocator.yaml
python tools/validate_dl_contract.py contracts/dl-skills/DL-27-FIN-project-cost-calculator.yaml
python tools/validate_dl_contract.py contracts/dl-skills/DL-26-RPT-report-builder.yaml
```

Validate Kiro hooks:

```bash
python tools/validate_kiro_hooks.py hooks/kiro-v1/pfc-workspace-hooks.json
```

Run output enforcement / deterministic finance checks:

```bash
python tools/check_pfc_output_enforcement.py path/to/output.md
```

If a DL-27 finance total fails, the checker prints:

```txt
TRIP: enforcement-output-gate.kiro.hook
```

## Current MVP gate

Target readiness:

```txt
>= 3.7 / 5
```

Current candidate score:

```txt
3.99 / 5
```

Known limitations:

```txt
Full graph/contract validators still need to be run in a true clean local checkout.
Kiro IDE runtime behavior for enabled hooks still needs pilot observation.
Memory-index and history-index schema validators are still missing.
Tiered hook execution and deterministic finance invariants need clean-checkout smoke tests.
```

## Work control

Go-live plan and tasks live here:

```txt
_work/PLAN.md
_work/TASKS.md
_work/ROADMAP.md
_work/DECISIONS.md
_work/RISKS.md
_work/milestones/v0.2-contract-runtime-live.md
```
