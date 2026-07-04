#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-.}"
PM_DIR="$TARGET_DIR/.pm"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
POWER_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

mkdir -p \
  "$PM_DIR/control" \
  "$PM_DIR/intake" \
  "$PM_DIR/audit" \
  "$PM_DIR/reports" \
  "$PM_DIR/history" \
  "$PM_DIR/checkpoints" \
  "$PM_DIR/memory"

copy_if_missing() {
  local src="$1"
  local dst="$2"
  if [ ! -f "$dst" ]; then
    cp "$src" "$dst"
    echo "created $dst"
  else
    echo "kept existing $dst"
  fi
}

copy_if_missing "$POWER_DIR/templates/project-control.yaml" "$PM_DIR/control/project-control.yaml"
copy_if_missing "$POWER_DIR/templates/project-intake.yaml" "$PM_DIR/intake/project-intake.yaml"
copy_if_missing "$POWER_DIR/templates/readiness-score.md" "$PM_DIR/audit/readiness-score.md"
copy_if_missing "$POWER_DIR/templates/missing-data-log.md" "$PM_DIR/audit/missing-data-log.md"
copy_if_missing "$POWER_DIR/templates/circuit-breaker-log.md" "$PM_DIR/audit/circuit-breaker-log.md"
copy_if_missing "$POWER_DIR/templates/context-retrieval-log.md" "$PM_DIR/audit/context-retrieval-log.md"
copy_if_missing "$POWER_DIR/templates/run-execution-record.md" "$PM_DIR/audit/run-execution-record.md"
copy_if_missing "$POWER_DIR/templates/memory-index.yaml" "$PM_DIR/memory/memory-index.yaml"

echo "PFC workspace bootstrap complete: $PM_DIR"
