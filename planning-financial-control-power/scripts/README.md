# PFC Workspace Bootstrap Scripts

## Purpose

Create the runtime `.pm/` structure inside a target project workspace.

## Linux/macOS

From `planning-financial-control-power/`:

```bash
bash scripts/install-workspace.sh /path/to/target-project
```

## Windows PowerShell

From `planning-financial-control-power/`:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install-workspace.ps1 -TargetDir C:\path\to\target-project
```

## Created structure

```txt
.pm/
├── control/project-control.yaml
├── intake/project-intake.yaml
├── audit/readiness-score.md
├── audit/missing-data-log.md
├── audit/circuit-breaker-log.md
├── audit/context-retrieval-log.md
├── audit/run-execution-record.md
├── reports/
├── history/
├── checkpoints/
└── memory/memory-index.yaml
```

## Rule

The script copies templates only when target files are missing. Existing runtime data is preserved.
