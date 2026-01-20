#!/usr/bin/env bash
# Run the STEP opening extraction script in Docker

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

IMAGE_NAME="${IMAGE_NAME:-gimli2-habitat-cadquery}"
IMAGE_TAG="${IMAGE_TAG:-latest}"

STEP_FILE="${STEP_FILE:-/workspace/reference/Osterath_Habitat_1225 AF.step}"
HABITAT_FILE="${HABITAT_FILE:-/workspace/habitat.yml}"
TOLERANCE="${TOLERANCE:-3.0}"

if ! docker image inspect "${IMAGE_NAME}:${IMAGE_TAG}" &>/dev/null; then
    echo "Image ${IMAGE_NAME}:${IMAGE_TAG} not found."
    echo "Run: ./docker/build.sh"
    exit 1
fi

echo "Running STEP extraction..."
echo "  Tolerance: ${TOLERANCE} mm"
echo ""

docker run --rm \
    --volume "${PROJECT_ROOT}:/workspace:ro" \
    --workdir /workspace \
    "${IMAGE_NAME}:${IMAGE_TAG}" \
    python scripts/extract_step_openings.py \
        --step "${STEP_FILE}" \
        --habitat "${HABITAT_FILE}" \
        --tolerance "${TOLERANCE}"
