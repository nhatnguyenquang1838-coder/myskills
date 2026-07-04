# Planning & Financial Control Power

Version: `0.2.0-draft`
Status: stronger MVP-live candidate

This Kiro Power coordinates planning, resource allocation, cost calculation, reporting, intake/onboarding, context loading, historical data usage, DL Skill contract routing, workflow enforcement, parallel-safe agent action logging, and anti-hallucination controls.

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
- DL Skill contract validation
- output validation
- guardrails
- circuit breaker
- enforcement gates
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
schemas/       Project Control Graph, contract, and audit schemas
tools/         validators, output checkers, logging utilities
scripts/       workspace bootstrap scripts
skills/        Power-owned support skills
agents/        role definitions
templates/     reusable workspace starter files
hooks/         hook templates until schema is verified
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

## Non-negotiable rules

```txt
No baseline -> no official RAG
No rate/resource/budget data -> no reliable budget status
No evidence -> mark as assumption
No link -> no claim
No DL Skill contract -> no controlled skill call
History can challenge the plan, not replace the baseline
DL Skills return draft deltas only; PFC controls write-back
MCP stdio tools must not write diagnostics to stdout
Parallel runs must write to per-run log files
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
└── logs/runs/
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

## Current MVP gate

Target readiness:

```txt
>= 3.7 / 5
```

Current candidate score:

```txt
3.91 / 5
```

Known limitations:

```txt
Hook files are still templates until exact Kiro hook schema is verified.
Validators still need to be run in a clean local checkout.
Bootstrap still needs real target workspace evidence.
Logging smoke test still needs to be run in a clean workspace.
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
