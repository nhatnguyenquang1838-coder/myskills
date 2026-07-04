# Checkpoint — Kiro Hook Schema, Bootstrap, and Logging Smoke

Date: 2026-07-04
Package: `planning-financial-control-power/`

## Scope

Close the remaining live-readiness blockers where possible:

```txt
BLOCKER-06: hooks not schema-verified
BLOCKER-08: bootstrap not tested in a target workspace
BLOCKER-10: logging smoke test not yet run in clean workspace
```

`BLOCKER-07` remains open because a true GitHub clean checkout could not be cloned from this execution container.

## Kiro hook schema verification

Verified against public Kiro hook v1 documentation:

```txt
Root: { version: "v1", hooks: [...] }
Hook fields: name, description, trigger, matcher, action, timeout, enabled
Action types: command, agent
Workspace location: .kiro/hooks/
```

## Files added

```txt
schemas/kiro-hook.schema.json
hooks/kiro-v1/pfc-workspace-hooks.json
tools/validate_kiro_hooks.py
```

## Files updated

```txt
scripts/install-workspace.sh
scripts/install-workspace.ps1
```

## Native hook package

Source:

```txt
hooks/kiro-v1/pfc-workspace-hooks.json
```

Bootstrap target:

```txt
.kiro/hooks/pfc-workspace-hooks.json
```

Enabled hooks:

```txt
pfc-cascade-check
pfc-report-fact-check
```

Disabled-by-default optional hooks:

```txt
pfc-enforcement-preflight
pfc-enforcement-contract-gate
pfc-enforcement-output-gate
pfc-enforcement-writeback-gate
```

Reason: broad Kiro triggers such as user prompt or task execution should not be enabled until narrowed in IDE usage.

## Local evidence

Hook validation:

```txt
PASS: hooks/kiro-v1/pfc-workspace-hooks.json is valid
```

Bootstrap smoke target:

```txt
/mnt/data/pfc-real-workspace-smoke
```

Bootstrap created:

```txt
.pm/control/project-control.yaml
.pm/intake/project-intake.yaml
.pm/audit/readiness-score.md
.pm/audit/missing-data-log.md
.pm/audit/circuit-breaker-log.md
.pm/audit/context-retrieval-log.md
.pm/audit/run-execution-record.md
.pm/memory/memory-index.yaml
.kiro/hooks/pfc-workspace-hooks.json
.kiro/logs/runs/
.pm/audit/runs/
```

Logging smoke result:

```txt
stdout: empty
stderr: logger initialized and log paths printed
PASS: .kiro/logs/runs/RUN-SMOKE.log
PASS: .pm/audit/runs/RUN-SMOKE.agent-action.ndjson
PASS: .pm/audit/runs/RUN-SMOKE.ide-event.ndjson
PASS: .pm/audit/runs/RUN-SMOKE.turn-analysis.md
```

Clean checkout limitation:

```txt
Container clone attempt failed because github.com DNS resolution was unavailable.
```

## Blocker status after this checkpoint

```txt
RESOLVED: BLOCKER-06 hooks not schema-verified
OPEN:     BLOCKER-07 validators not yet run in a clean local checkout
RESOLVED: BLOCKER-08 bootstrap not yet tested in a target workspace
RESOLVED: BLOCKER-10 logging smoke test not yet run in clean workspace
```

## Updated readiness signal

```txt
Previous readiness: 3.91 / 5
Updated readiness:  3.99 / 5
Status: MVP-live candidate; one clean-checkout validation blocker remains before team pilot.
```
