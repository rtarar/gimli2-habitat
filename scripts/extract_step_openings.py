#!/usr/bin/env python3
"""Extract window and door opening positions from the habitat STEP file.

This script uses cadquery to load the STEP file, scans planar faces for
rectangular openings that match expected cutout sizes from habitat.yml,
then reports center coordinates and sill/threshold heights in model units.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STEP = REPO_ROOT / "reference" / "Osterath_Habitat_1225 AF.step"
DEFAULT_HABITAT = REPO_ROOT / "habitat.yml"


@dataclass(frozen=True)
class OpeningSpec:
    feature_id: str
    kind: str
    width: float
    height: float
    location: Optional[str]


@dataclass(frozen=True)
class FaceMatch:
    feature_id: str
    kind: str
    location: Optional[str]
    normal: Tuple[float, float, float]
    center: Tuple[float, float, float]
    bbox_min: Tuple[float, float, float]
    bbox_max: Tuple[float, float, float]
    size_2d: Tuple[float, float]
    size_error: float


def ensure_dependency(module_name: str, package_hint: str) -> None:
    if importlib.util.find_spec(module_name) is None:
        message = (
            f"Missing dependency: {module_name}. Install with: {package_hint}"
        )
        raise SystemExit(message)


def load_yaml(path: Path) -> dict:
    ensure_dependency("yaml", "pip install pyyaml")
    import yaml  # noqa: PLC0415 (import after check)

    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def normalize(vector: Iterable[float]) -> Tuple[float, float, float]:
    x, y, z = vector
    length = math.sqrt(x * x + y * y + z * z)
    if length == 0:
        return 0.0, 0.0, 0.0
    return x / length, y / length, z / length


def dot(a: Tuple[float, float, float], b: Tuple[float, float, float]) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def face_normal(face) -> Tuple[float, float, float]:
    normal = face.normalAt()
    return normalize((normal.x, normal.y, normal.z))


def face_bbox(face) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    bbox = face.BoundingBox()
    return (bbox.xmin, bbox.ymin, bbox.zmin), (bbox.xmax, bbox.ymax, bbox.zmax)


def face_center(face) -> Tuple[float, float, float]:
    center = face.Center()
    return (center.x, center.y, center.z)


def face_size_2d(face, normal: Tuple[float, float, float]) -> Tuple[float, float]:
    (xmin, ymin, zmin), (xmax, ymax, zmax) = face_bbox(face)
    xlen = xmax - xmin
    ylen = ymax - ymin
    zlen = zmax - zmin
    axis = max(range(3), key=lambda idx: abs(normal[idx]))
    if axis == 0:
        return ylen, zlen
    if axis == 1:
        return xlen, zlen
    return xlen, ylen


def size_error(candidate: Tuple[float, float], target: Tuple[float, float]) -> float:
    return abs(candidate[0] - target[0]) + abs(candidate[1] - target[1])


def match_face(
    faces: Iterable,
    opening: OpeningSpec,
    tolerance: float,
) -> Optional[FaceMatch]:
    target = (opening.width, opening.height)
    best: Optional[FaceMatch] = None
    for face in faces:
        if face.geomType() != "PLANE":
            continue
        normal = face_normal(face)
        size = face_size_2d(face, normal)
        candidates = [size, (size[1], size[0])]
        error = min(size_error(c, target) for c in candidates)
        if error > tolerance:
            continue
        if best is None or error < best.size_error:
            center = face_center(face)
            bbox_min, bbox_max = face_bbox(face)
            best = FaceMatch(
                feature_id=opening.feature_id,
                kind=opening.kind,
                location=opening.location,
                normal=normal,
                center=center,
                bbox_min=bbox_min,
                bbox_max=bbox_max,
                size_2d=size,
                size_error=error,
            )
    return best


def load_openings(habitat: dict) -> List[OpeningSpec]:
    openings: List[OpeningSpec] = []
    for window in habitat.get("features", {}).get("windows", []):
        if not window.get("cutout_width") or not window.get("cutout_height"):
            continue
        openings.append(
            OpeningSpec(
                feature_id=window["id"],
                kind="window",
                width=float(window["cutout_width"]),
                height=float(window["cutout_height"]),
                location=window.get("location"),
            )
        )
    for door in habitat.get("features", {}).get("doors", []):
        if not door.get("opening_width") or not door.get("opening_height"):
            continue
        openings.append(
            OpeningSpec(
                feature_id=door["id"],
                kind="door",
                width=float(door["opening_width"]),
                height=float(door["opening_height"]),
                location=door.get("location"),
            )
        )
    return openings


def load_faces(step_path: Path):
    ensure_dependency("cadquery", "pip install cadquery")
    import cadquery as cq  # noqa: PLC0415 (import after check)
    from cadquery import importers  # noqa: PLC0415

    shape = importers.importStep(str(step_path))
    if isinstance(shape, cq.Workplane):
        shape = shape.val()
    return shape.Faces()


def format_match(match: FaceMatch) -> str:
    cx, cy, cz = match.center
    min_x, min_y, min_z = match.bbox_min
    max_x, max_y, max_z = match.bbox_max
    nx, ny, nz = match.normal
    return (
        f"- id: {match.feature_id}\n"
        f"  kind: {match.kind}\n"
        f"  location: {match.location}\n"
        f"  normal: [{nx:.4f}, {ny:.4f}, {nz:.4f}]\n"
        f"  center_mm: [{cx:.2f}, {cy:.2f}, {cz:.2f}]\n"
        f"  bbox_min_mm: [{min_x:.2f}, {min_y:.2f}, {min_z:.2f}]\n"
        f"  bbox_max_mm: [{max_x:.2f}, {max_y:.2f}, {max_z:.2f}]\n"
        f"  size_2d_mm: [{match.size_2d[0]:.2f}, {match.size_2d[1]:.2f}]\n"
        f"  size_error_mm: {match.size_error:.2f}\n"
        f"  sill_or_threshold_height_mm: {min_z:.2f}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract window/door opening positions from a STEP file.",
    )
    parser.add_argument(
        "--step",
        type=Path,
        default=DEFAULT_STEP,
        help="Path to the STEP file.",
    )
    parser.add_argument(
        "--habitat",
        type=Path,
        default=DEFAULT_HABITAT,
        help="Path to habitat.yml.",
    )
    parser.add_argument(
        "--tolerance",
        type=float,
        default=3.0,
        help="Tolerance in mm for size matching.",
    )
    args = parser.parse_args()

    habitat = load_yaml(args.habitat)
    openings = load_openings(habitat)
    if not openings:
        print("No openings found in habitat.yml.")
        return 1

    faces = load_faces(args.step)
    matches: List[FaceMatch] = []
    for opening in openings:
        match = match_face(faces, opening, args.tolerance)
        if match is None:
            print(
                f"No match found for {opening.feature_id} ({opening.kind}) "
                f"size {opening.width}x{opening.height} mm",
            )
            continue
        matches.append(match)

    if not matches:
        print("No opening matches found.")
        return 1

    print("matches:")
    for match in matches:
        print(format_match(match), end="")

    return 0


if __name__ == "__main__":
    sys.exit(main())
