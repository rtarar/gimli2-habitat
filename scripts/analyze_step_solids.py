#!/usr/bin/env python3
"""Analyze all solids in the STEP file to identify components (like wheels)."""

from __future__ import annotations
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STEP = REPO_ROOT / "reference" / "Osterath_Habitat_1225 AF.step"

def analyze_solids(step_path: Path):
    try:
        import cadquery as cq
        from cadquery import importers
    except ImportError:
        print("Error: cadquery not found. Run this inside the docker container.")
        sys.exit(1)

    print(f"Loading STEP file: {step_path}")
    model = importers.importStep(str(step_path))
    
    # Depending on structure, it might be a Compound, or list of solids.
    # If it's a Workplane, val() gets the underlying object.
    if isinstance(model, cq.Workplane):
        obj = model.val()
    else:
        obj = model

    # Extract all solids
    # In CadQuery/OCCT, we can traverse looking for Solids.
    # If it's a Compound, we can get solids if exposed, or verify shape type.
    
    solids = []
    if hasattr(obj, "Solids"):
        solids = obj.Solids()
    else:
        # If it is a single solid
        if obj.ShapeType() == "Solid":
            solids = [obj]
        else:
            print(f"Top level object is type: {obj.ShapeType()}")
            # Try exploring
            from OCP.TopExp import TopExp_Explorer
            from OCP.TopAbs import TopAbs_SOLID
            from cadquery import Shape

            exp = TopExp_Explorer(obj.wrapped, TopAbs_SOLID)
            while exp.More():
                solids.append(Shape(exp.Current()))
                exp.Next()
    
    print(f"Found {len(solids)} solids.")
    
    print(f"{'ID':<4} | {'Volume (mm3)':<15} | {'Center (X, Y, Z)':<30} | {'BBox Min':<30} | {'BBox Max':<30}")
    print("-" * 120)

    for i, solid in enumerate(solids):
        bbox = solid.BoundingBox()
        center = solid.Center()
        volume = solid.Volume()
        
        c_str = f"({center.x:.2f}, {center.y:.2f}, {center.z:.2f})"
        min_str = f"({bbox.xmin:.2f}, {bbox.ymin:.2f}, {bbox.zmin:.2f})"
        max_str = f"({bbox.xmax:.2f}, {bbox.ymax:.2f}, {bbox.zmax:.2f})"
        
        print(f"{i:<4} | {volume:<15.2f} | {c_str:<30} | {min_str:<30} | {max_str:<30}")

if __name__ == "__main__":
    analyze_solids(DEFAULT_STEP)
