#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STEP_PATH="${STEP_PATH:-$ROOT_DIR/reference/Osterath_Habitat_1225 AF.step}"
HABITAT_PATH="${HABITAT_PATH:-$ROOT_DIR/habitat.yml}"
OUTPUT_PATH="${OUTPUT_PATH:-$ROOT_DIR/tmp/step_openings.yaml}"
TOLERANCE_MM="${TOLERANCE_MM:-3.0}"

mkdir -p "$(dirname "$OUTPUT_PATH")"

python "$ROOT_DIR/scripts/extract_step_openings.py" \
  --step "$STEP_PATH" \
  --habitat "$HABITAT_PATH" \
  --tolerance "$TOLERANCE_MM" \
  > "$OUTPUT_PATH"

echo "Wrote output to $OUTPUT_PATH"
