"""Gimli2 Habitat Module System.

Parametric CadQuery modules for the habitat interior and exterior.
"""

from pathlib import Path

MODULE_DIR = Path(__file__).parent

# Module registry - maps module names to their classes
MODULES = {
    # Interior modules
    "bathroom_shower": "bathroom_shower.BathroomShower",
    "bathroom_toilet": "bathroom_toilet.BathroomToilet",
    "kitchen": "kitchen.Kitchen",
    "storage_cabinets": "storage_cabinets.StorageCabinets",
    "seating": "seating.Seating",
    "bed_system": "bed_system.BedSystem",
    "garage": "garage.Garage",
    # Infrastructure modules
    "electrical": "electrical.Electrical",
    "plumbing": "plumbing.Plumbing",
    "heating": "heating.Heating",
    "security": "security.Security",
    # Exterior modules
    "rear_left_box": "rear_left_box.RearLeftBox",
    "rear_right_box": "rear_right_box.RearRightBox",
    "solar_roof": "solar_roof.SolarRoof",
    "starlink": "starlink.Starlink",
}


def get_module(name: str):
    """Get a module class by name."""
    if name not in MODULES:
        raise ValueError(f"Unknown module: {name}")

    module_path, class_name = MODULES[name].rsplit(".", 1)
    import importlib

    mod = importlib.import_module(f".{module_path}", package="cad.modules")
    return getattr(mod, class_name)


def list_modules() -> list:
    """List all available module names."""
    return list(MODULES.keys())
