#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-.}"
PM_DIR="$TARGET_DIR/.pm"
KIRO_DIR="$TARGET_DIR/.kiro"
KIRO_LOG_DIR="$KIRO_DIR/logs"
KIRO_HOOK_DIR="$KIRO_DIR/hooks"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
POWER_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

mkdir -p \
  "$PM_DIR/control" \
  "$PM_DIR/intake" \
  "$PM_DIR/audit/runs" \
  "$PM_DIR/reports" \
  "$PM_DIR/history" \
  "$PM_DIR/checkpoints" \
  "$PM_DIR/memory" \
  "$KIRO_LOG_DIR/runs" \
  "$KIRO_HOOK_DIR"

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

if [ -d "$POWER_DIR/hooks/kiro-v1" ]; then
  for hook_file in "$POWER_DIR"/hooks/kiro-v1/*.json; do
    [ -e "$hook_file" ] || continue
    copy_if_missing "$hook_file" "$KIRO_HOOK_DIR/$(basename "$hook_file")"
  done
fi

echo "PFC workspace bootstrap complete: $PM_DIR"
echo "Parallel-safe PFC audit run directory ready: $PM_DIR/audit/runs"
echo "Parallel-safe Kiro debug run directory ready: $KIRO_LOG_DIR/runs"
echo "Kiro hook directory ready: $KIRO_HOOK_DIR"
