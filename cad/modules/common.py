"""Common constants and utilities for habitat modules.

All dimensions in millimeters unless otherwise noted.
Coordinate system:
  X: Width (driver side negative, passenger side positive)
  Y: Height (floor to ceiling)
  Z: Length (front/cab to rear)
"""

from dataclasses import dataclass
from typing import Tuple
import cadquery as cq


# =============================================================================
# HABITAT SHELL DIMENSIONS (from STEP file analysis)
# =============================================================================

@dataclass(frozen=True)
class HabitatDimensions:
    """Habitat shell dimensions."""

    # Exterior bounding box
    ext_x_min: float = -1202
    ext_x_max: float = 1202
    ext_y_min: float = -570  # Below main floor (storage)
    ext_y_max: float = 2588  # Roof exterior
    ext_z_min: float = 755   # Front wall exterior
    ext_z_max: float = 5802  # Rear wall exterior

    # Interior dimensions (approximate)
    int_x_min: float = -1140  # Driver wall interior
    int_x_max: float = 1140   # Passenger wall interior
    int_y_floor: float = 288  # Floor surface
    int_y_ceiling: float = 2448  # Ceiling surface
    int_z_front: float = 900  # Front wall interior
    int_z_rear: float = 5680  # Rear wall interior

    # Computed properties
    @property
    def interior_width(self) -> float:
        return self.int_x_max - self.int_x_min  # ~2280mm

    @property
    def interior_height(self) -> float:
        return self.int_y_ceiling - self.int_y_floor  # ~2160mm

    @property
    def interior_length(self) -> float:
        return self.int_z_rear - self.int_z_front  # ~4780mm

    @property
    def floor_center_y(self) -> float:
        return self.int_y_floor

    @property
    def ceiling_center_y(self) -> float:
        return self.int_y_ceiling


HABITAT = HabitatDimensions()


# =============================================================================
# ZONE DEFINITIONS (Z-axis ranges)
# =============================================================================

@dataclass(frozen=True)
class Zone:
    """A zone along the Z-axis."""
    name: str
    z_start: float
    z_end: float
    description: str = ""

    @property
    def z_center(self) -> float:
        return (self.z_start + self.z_end) / 2

    @property
    def depth(self) -> float:
        return self.z_end - self.z_start


# Zone definitions (front to rear)
ZONE_BATHROOM = Zone("bathroom", 900, 1700, "Wet entry, shower, toilet")
ZONE_KITCHEN = Zone("kitchen", 1700, 3200, "Kitchen galley and storage")
ZONE_LIVING = Zone("living", 3200, 4500, "Seating and bed system")
ZONE_GARAGE = Zone("garage", 4500, 5500, "Rear garage/storage")

ZONES = {
    "bathroom": ZONE_BATHROOM,
    "kitchen": ZONE_KITCHEN,
    "living": ZONE_LIVING,
    "garage": ZONE_GARAGE,
}


# =============================================================================
# MATERIAL THICKNESSES
# =============================================================================

@dataclass(frozen=True)
class Materials:
    """Standard material thicknesses."""
    plywood_thin: float = 9      # 9mm plywood
    plywood_standard: float = 12  # 12mm plywood
    plywood_thick: float = 18    # 18mm plywood
    aluminum_sheet: float = 2    # 2mm aluminum
    aluminum_angle: float = 3    # 3mm aluminum angle
    insulation: float = 25       # 25mm insulation
    wall_panel: float = 4        # 4mm wall panel


MATERIALS = Materials()


# =============================================================================
# OPENING POSITIONS (from habitat.yml / STEP analysis)
# =============================================================================

@dataclass(frozen=True)
class Opening:
    """An opening (window, door, hatch) in the shell."""
    id: str
    center: Tuple[float, float, float]  # (x, y, z)
    width: float
    height: float
    normal: Tuple[float, float, float]  # Face normal direction


# Windows
WIN_01 = Opening("WIN-01", (-1158, 723, 5109), 670, 1063, (-1, 0, 0))  # Rear driver
WIN_02 = Opening("WIN-02", (1158, 723, 5109), 670, 1063, (1, 0, 0))   # Rear passenger
WIN_03 = Opening("WIN-03", (0, 2478, 3615), 554, 698, (0, 1, 0))      # Roof skylight
WIN_04 = Opening("WIN-04", (-1158, 1942, 1359), 570, 673, (-1, 0, 0)) # Bathroom driver
WIN_05 = Opening("WIN-05", (1158, 1641, 2710), 670, 1063, (1, 0, 0))  # Kitchen passenger

# Door
DOOR_01 = Opening("DOOR-01", (1158, 1251, 1406), 1766, 693, (1, 0, 0))  # Entry door

# Hatches
HATCH_01 = Opening("HATCH-01", (890, -295, 898), 600, 550, (0, 0, -1))   # Lower floor
HATCH_02 = Opening("HATCH-02", (890, -295, 2298), 600, 550, (0, 0, 1))   # Upper floor

OPENINGS = {
    "WIN-01": WIN_01,
    "WIN-02": WIN_02,
    "WIN-03": WIN_03,
    "WIN-04": WIN_04,
    "WIN-05": WIN_05,
    "DOOR-01": DOOR_01,
    "HATCH-01": HATCH_01,
    "HATCH-02": HATCH_02,
}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def make_box(
    x_size: float,
    y_size: float,
    z_size: float,
    center: Tuple[float, float, float] = (0, 0, 0),
    shell_thickness: float = 0,
) -> cq.Workplane:
    """Create a box, optionally shelled.

    Args:
        x_size: Width (X dimension)
        y_size: Height (Y dimension)
        z_size: Depth (Z dimension)
        center: Center point of the box
        shell_thickness: If > 0, hollow the box with this wall thickness
    """
    wp = (
        cq.Workplane("XY")
        .box(x_size, y_size, z_size)
        .translate(center)
    )

    if shell_thickness > 0:
        wp = wp.faces("+Y").shell(-shell_thickness)

    return wp


def make_cabinet(
    width: float,
    height: float,
    depth: float,
    position: Tuple[float, float, float],
    wall_thickness: float = 18,
    open_face: str = "+Z",
) -> cq.Workplane:
    """Create a cabinet shell.

    Args:
        width: X dimension
        height: Y dimension
        depth: Z dimension
        position: (x, y, z) of the cabinet's bottom-front-left corner
        wall_thickness: Thickness of cabinet walls
        open_face: Which face is open ("+X", "-X", "+Y", "-Y", "+Z", "-Z")
    """
    # Create solid box
    wp = cq.Workplane("XY").box(width, height, depth)

    # Shell it (remove the open face)
    wp = wp.faces(open_face).shell(-wall_thickness)

    # Position it
    # Move so that position is at bottom-front-left
    offset = (
        position[0] + width / 2,
        position[1] + height / 2,
        position[2] + depth / 2,
    )
    wp = wp.translate(offset)

    return wp


def add_mounting_holes(
    workplane: cq.Workplane,
    hole_positions: list,
    hole_diameter: float = 8,
    hole_depth: float = 20,
) -> cq.Workplane:
    """Add mounting holes to a workplane.

    Args:
        workplane: The workplane to add holes to
        hole_positions: List of (x, y, z) positions for holes
        hole_diameter: Diameter of the holes
        hole_depth: Depth of the holes
    """
    for pos in hole_positions:
        workplane = (
            workplane
            .pushPoints([pos[:2]])  # x, y only for 2D positioning
            .hole(hole_diameter, hole_depth)
        )
    return workplane


def export_step(workplane: cq.Workplane, filepath: str) -> None:
    """Export a workplane to STEP format."""
    cq.exporters.export(workplane, filepath, exportType="STEP")


def export_stl(workplane: cq.Workplane, filepath: str) -> None:
    """Export a workplane to STL format."""
    cq.exporters.export(workplane, filepath, exportType="STL")


# =============================================================================
# BASE MODULE CLASS
# =============================================================================

class HabitatModule:
    """Base class for all habitat modules."""

    # Module metadata (override in subclasses)
    MODULE_ID: str = "base"
    MODULE_NAME: str = "Base Module"
    ZONE: Zone = None

    def __init__(self, params: dict = None):
        """Initialize the module with optional parameters."""
        self.params = params or {}
        self._geometry = None

    def generate(self) -> cq.Workplane:
        """Generate the module geometry. Override in subclasses."""
        raise NotImplementedError("Subclasses must implement generate()")

    @property
    def geometry(self) -> cq.Workplane:
        """Get the module geometry, generating if needed."""
        if self._geometry is None:
            self._geometry = self.generate()
        return self._geometry

    def export_step(self, filepath: str) -> None:
        """Export the module to STEP format."""
        export_step(self.geometry, filepath)

    def export_stl(self, filepath: str) -> None:
        """Export the module to STL format."""
        export_stl(self.geometry, filepath)

    def get_bounding_box(self) -> dict:
        """Get the bounding box of the module."""
        bb = self.geometry.val().BoundingBox()
        return {
            "x_min": bb.xmin,
            "x_max": bb.xmax,
            "y_min": bb.ymin,
            "y_max": bb.ymax,
            "z_min": bb.zmin,
            "z_max": bb.zmax,
        }
