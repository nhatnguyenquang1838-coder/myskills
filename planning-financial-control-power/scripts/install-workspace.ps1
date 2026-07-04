param(
  [string]$TargetDir = "."
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PowerDir = Split-Path -Parent $ScriptDir
$PmDir = Join-Path $TargetDir ".pm"
$KiroLogDir = Join-Path $TargetDir ".kiro\logs"

$Dirs = @(
  "control",
  "intake",
  "audit",
  "reports",
  "history",
  "checkpoints",
  "memory"
)

foreach ($d in $Dirs) {
  New-Item -ItemType Directory -Force -Path (Join-Path $PmDir $d) | Out-Null
}

New-Item -ItemType Directory -Force -Path $KiroLogDir | Out-Null

function Copy-IfMissing($src, $dst) {
  if (-not (Test-Path $dst)) {
    Copy-Item $src $dst
    Write-Host "created $dst"
  } else {
    Write-Host "kept existing $dst"
  }
}

Copy-IfMissing (Join-Path $PowerDir "templates/project-control.yaml") (Join-Path $PmDir "control/project-control.yaml")
Copy-IfMissing (Join-Path $PowerDir "templates/project-intake.yaml") (Join-Path $PmDir "intake/project-intake.yaml")
Copy-IfMissing (Join-Path $PowerDir "templates/readiness-score.md") (Join-Path $PmDir "audit/readiness-score.md")
Copy-IfMissing (Join-Path $PowerDir "templates/missing-data-log.md") (Join-Path $PmDir "audit/missing-data-log.md")
Copy-IfMissing (Join-Path $PowerDir "templates/circuit-breaker-log.md") (Join-Path $PmDir "audit/circuit-breaker-log.md")
Copy-IfMissing (Join-Path $PowerDir "templates/context-retrieval-log.md") (Join-Path $PmDir "audit/context-retrieval-log.md")
Copy-IfMissing (Join-Path $PowerDir "templates/run-execution-record.md") (Join-Path $PmDir "audit/run-execution-record.md")
Copy-IfMissing (Join-Path $PowerDir "templates/agent-action-log.ndjson") (Join-Path $PmDir "audit/agent-action-log.ndjson")
Copy-IfMissing (Join-Path $PowerDir "templates/ide-event-log.ndjson") (Join-Path $PmDir "audit/ide-event-log.ndjson")
Copy-IfMissing (Join-Path $PowerDir "templates/turn-analysis-log.md") (Join-Path $PmDir "audit/turn-analysis-log.md")
Copy-IfMissing (Join-Path $PowerDir "templates/memory-index.yaml") (Join-Path $PmDir "memory/memory-index.yaml")

Write-Host "PFC workspace bootstrap complete: $PmDir"
Write-Host "Kiro debug log directory ready: $KiroLogDir"
