#!/usr/bin/env bash
# Build the CadQuery Docker image for STEP file processing

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

IMAGE_NAME="${IMAGE_NAME:-gimli2-habitat-cadquery}"
IMAGE_TAG="${IMAGE_TAG:-latest}"

echo "Building Docker image: ${IMAGE_NAME}:${IMAGE_TAG}"

docker build \
    --tag "${IMAGE_NAME}:${IMAGE_TAG}" \
    --file "${SCRIPT_DIR}/Dockerfile" \
    "${SCRIPT_DIR}"

echo ""
echo "Build complete: ${IMAGE_NAME}:${IMAGE_TAG}"
echo ""
echo "Usage:"
echo "  ./docker/run.sh"
echo "  ./docker/shell.sh"
