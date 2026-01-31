## Conflict Detected: Battery Modules vs Garage Shell Depth

**Type:** Constraint Conflict (Physical Fitment)

**Artifact A:** `habitat.yml` (Battery Specs from User Prompt)
- Module Dimensions: 540 mm (L) x 250 mm (W) x 220 mm (H)
- Required Clearance: 25 mm all sides
- Minimum bounding box per module: **590 mm x 300 mm**

**Artifact B:** `zones/functional/ZONE-003-garage-shell.yml`
- Current Shell Depth: **509 mm**
- Internal Arm Width: 473 mm

**Nature of Conflict:**
The battery modules (540mm long) physically cannot fit inside the Garage Shell arms (509mm deep), regardless of orientation. They protrude by at least 31mm before adding clearance or wall thickness.

**Detected During:** `scripts/battery_layout_solver.py` execution.

**Suggested Resolution Options:**
1.  **Increase Garage Shell Depth**: Extend `shell_depth` from 509mm to **600mm**.
    *   *Pros*: comfortably fits batteries (590mm required with clearance).
    *   *Cons*: Reduces Living/Dinette floor space by ~9cm; slightly encroaches on Kitchen aisle.
    *   *Status*: **RECOMMENDED**

2.  **Relocate Batteries**: Move batteries to a different zone (e.g., under false floor or in a new cabinet).
    *   *Pros*: Preserves garage shell geometry.
    *   *Cons*: Raises center of mass (bad for vehicle dynamics); consumes prime living storage.

3.  **Change Battery Spec**: Switch to smaller/denser modules.
    *   *Pros*: Fits current geometry.
    *   *Cons*: User specified "6 identical modules" as a hard constraint.

**Agent Recommendation:**
Option 1. Increasing the shell depth to 600mm aligns with standard countertop/cabinet depths (often 600mm) and provides necessary volume for both batteries and larger water tanks.

**Status:** RESOLVED
**Resolution:** Adopted Scenario E (Mass Balance).
- **Placement:** Batteries moved to **Passenger-Side Kitchen Base**.
- **Rationale:** Necessary to counter-balance the 500L (450kg) Driver-side diesel tank.
- **Fit:** Fits in 600mm deep cabinetry alongside Water Tank 1.
