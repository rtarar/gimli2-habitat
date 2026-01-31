#!/usr/bin/env python3
"""Visualize the habitat STEP file with openings highlighted.

Generates an HTML file with an interactive 3D viewer using three.js.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STEP = REPO_ROOT / "reference" / "Osterath_Habitat_1225 AF.step"
DEFAULT_OUTPUT = REPO_ROOT / "renders" / "habitat_viewer.html"


def create_box(width, depth, height, x, y, z):
    """Create a box at specific center coordinates."""
    import cadquery as cq
    # Habitat coords: X=Width, Y=Length (Forward), Z=Height
    # CadQuery standard: X, Y, Z. 
    # But in our viewer (three.js STL loader), the orientation depends on the export.
    # The STEP file dictates the shell orientation.
    # Our previous experiment showed we need to match that.
    # We will assume the coordinate system logic from generate_systems_cad.py is correct.
    box = cq.Workplane("XY").box(width, depth, height)
    return box.translate((x, y, z))

def generate_systems_geometry(step_path: Path) -> dict:
    """Generate STL data for all systems and zones."""
    import cadquery as cq
    from cadquery import importers
    import tempfile

    components = {}

    def export_stl(shape):
        with tempfile.NamedTemporaryFile(suffix=".stl", delete=False) as f:
            path = f.name
        cq.exporters.export(shape, path, exportType="STL")
        with open(path, "rb") as f:
            data = f.read()
        Path(path).unlink()
        return data

    # COLORS (Hex)
    COLOR_ALDE = 0xff4444      # Red
    COLOR_WATER = 0x4444ff     # Blue
    COLOR_BATTERY = 0xffaa00   # Orange/Yellow
    COLOR_ELEC = 0xaa44ff      # Purple
    COLOR_ZONE = 0x44aa44      # Green (Translucent)
    COLOR_DIESEL = 0x555555    # Grey

    # 1. ALDE HEATER (Driver Side Rear Garage Arm)
    alde = create_box(420, 500, 300, -840, -2090, 150)
    components['alde'] = {
        'data': export_stl(alde), 'color': COLOR_ALDE, 'name': 'Alde Heater', 'opacity': 1.0
    }

    # 2. ELECTRICAL CORE (Passenger Side Rear Garage Arm)
    elec = create_box(200, 400, 500, 840, -2090, 400)
    components['electrical'] = {
        'data': export_stl(elec), 'color': COLOR_ELEC, 'name': 'Electrical Core', 'opacity': 1.0
    }

    # 3. WATER TANK 1 (Passenger Kitchen Base)
    tank1 = create_box(500, 1000, 500, 840, -1000, 250)
    components['tank1'] = {
        'data': export_stl(tank1), 'color': COLOR_WATER, 'name': 'Water Tank 1 (Standard)', 'opacity': 1.0
    }

    # 4. WATER TANK 2 (Driver Dinette Base - Low Profile)
    tank2 = create_box(500, 1250, 400, -840, -1000, 200)
    components['tank2'] = {
        'data': export_stl(tank2), 'color': COLOR_WATER, 'name': 'Water Tank 2 (Low Profile)', 'opacity': 1.0
    }

    # 5. BATTERIES (Passenger Kitchen Base)
    batteries = create_box(400, 600, 400, 840, 0, 200)
    components['batteries'] = {
        'data': export_stl(batteries), 'color': COLOR_BATTERY, 'name': 'Battery Bank (300kg)', 'opacity': 1.0
    }

    # 6. DIESEL TANK (External Reference)
    diesel = create_box(500, 1500, 600, -1140, -500, -300)
    components['diesel'] = {
        'data': export_stl(diesel), 'color': COLOR_DIESEL, 'name': 'Diesel Tank (Ref)', 'opacity': 1.0
    }

    # 7. ZONES (Transparent)
    
    # Garage Zone
    garage_zone = create_box(2280, 600, 2160, 0, -2090, 1080)
    components['zone_garage'] = {
        'data': export_stl(garage_zone), 'color': COLOR_ZONE, 'name': 'Zone: Garage', 'opacity': 0.15
    }

    # Kitchen Zone
    kitchen_zone = create_box(600, 2300, 2160, 840, 40, 1080)
    components['zone_kitchen'] = {
        'data': export_stl(kitchen_zone), 'color': COLOR_ZONE, 'name': 'Zone: Kitchen', 'opacity': 0.15
    }

    # Bathroom Zone
    bathroom_zone = create_box(900, 1200, 2160, -690, 1790, 1080)
    components['zone_bathroom'] = {
        'data': export_stl(bathroom_zone), 'color': COLOR_ZONE, 'name': 'Zone: Bathroom', 'opacity': 0.15
    }

    # Dinette Zone
    dinette_zone = create_box(1000, 2300, 2160, -640, 40, 1080)
    components['zone_dinette'] = {
        'data': export_stl(dinette_zone), 'color': COLOR_ZONE, 'name': 'Zone: Dinette', 'opacity': 0.15
    }

    return components

def load_openings_from_yaml(yaml_path: Path) -> list:
    """Load openings from habitat.yml."""
    import yaml

    with yaml_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    openings = []
    features = data.get("features", {})

    for win in features.get("windows", []):
        openings.append({
            "id": win.get("id"),
            "model": win.get("model"),
            "kind": "window",
            "location": win.get("location"),
            "center_mm": win.get("center_mm"),
        })

    for door in features.get("doors", []):
        openings.append({
            "id": door.get("id"),
            "model": door.get("model"),
            "kind": "door",
            "location": door.get("location"),
            "center_mm": door.get("center_mm"),
        })

    for hatch in features.get("hatches", []):
        openings.append({
            "id": hatch.get("id"),
            "model": hatch.get("model"),
            "kind": "hatch",
            "location": hatch.get("location"),
            "center_mm": hatch.get("center_mm"),
        })

    return openings
    """Load openings from habitat.yml."""
    import yaml

    with yaml_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    openings = []
    features = data.get("features", {})

    for win in features.get("windows", []):
        openings.append({
            "id": win.get("id"),
            "model": win.get("model"),
            "kind": "window",
            "location": win.get("location"),
            "center_mm": win.get("center_mm"),
        })

    for door in features.get("doors", []):
        openings.append({
            "id": door.get("id"),
            "model": door.get("model"),
            "kind": "door",
            "location": door.get("location"),
            "center_mm": door.get("center_mm"),
        })

    for hatch in features.get("hatches", []):
        openings.append({
            "id": hatch.get("id"),
            "model": hatch.get("model"),
            "kind": "hatch",
            "location": hatch.get("location"),
            "center_mm": hatch.get("center_mm"),
        })

    return openings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate an interactive 3D viewer for the habitat.",
    )
    parser.add_argument(
        "--step",
        type=Path,
        default=DEFAULT_STEP,
        help="Path to the STEP file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Path to output HTML file.",
    )
    parser.add_argument(
        "--habitat",
        type=Path,
        default=REPO_ROOT / "habitat.yml",
        help="Path to habitat.yml.",
    )
    args = parser.parse_args()

    print(f"Loading STEP file: {args.step}")
    stl_data = load_step_to_stl(args.step)
    print(f"  Converted to STL: {len(stl_data)} bytes")

    print(f"Loading openings from: {args.habitat}")
    openings = load_openings_from_yaml(args.habitat)
    print(f"  Found {len(openings)} openings")

    print(f"Generating HTML viewer...")
    html = create_html_viewer(stl_data, openings)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"  Saved to: {args.output}")
    print()
    print(f"Open in browser: file://{args.output.resolve()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
