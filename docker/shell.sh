#!/usr/bin/env bash
# Start an interactive shell in the CadQuery container

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

IMAGE_NAME="${IMAGE_NAME:-gimli2-habitat-cadquery}"
IMAGE_TAG="${IMAGE_TAG:-latest}"

if ! docker image inspect "${IMAGE_NAME}:${IMAGE_TAG}" &>/dev/null; then
    echo "Image ${IMAGE_NAME}:${IMAGE_TAG} not found."
    echo "Run: ./docker/build.sh"
    exit 1
fi

echo "Starting interactive shell..."
echo "Project mounted at /workspace (read-write)"
echo ""

docker run --rm -it \
    --volume "${PROJECT_ROOT}:/workspace:rw" \
    --workdir /workspace \
    "${IMAGE_NAME}:${IMAGE_TAG}" \
    /bin/bash
