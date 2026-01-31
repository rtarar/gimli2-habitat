## Conflict Detected: Water Tank Fitment vs Axle Loading

**Type:** Constraint Conflict (Physical Fitment & Weight Distribution)

**Artifact A:** `habitat.yml` (Water Tank Specs from User Prompt)
- Option A: Single 1200x600x700mm (500kg).
- Option B: Split 2x 900x500x560mm (250kg each).
- **CRITICAL CONSTRAINT:** Centroid must be near Rear Axle (X=2380mm).

**Artifact B:** `zones/functional/ZONE-003-garage-shell.yml`
- Current Shell Depth: 509mm.
- Location: "Rear section" (X=0 to X=~1000mm).

**Nature of Conflict:**
1.  **Option A (Single Tank)**: Physically fits in the center channel width-wise, but forces the mass to the extreme rear (Centroid X ~600mm). This violates the axle loading constraint (Target X=2380mm) by nearly 1.8 meters, creating a dangerous "pendulum effect."
2.  **Option B (Split Tanks)**: Provides excellent weight distribution potential (can be placed mid-ship). However, the individual tanks (500mm wide) **do not fit** inside the current 509mm deep side shells (473mm internal width).

**Detected During:** `scripts/water_tank_solver.py` execution.

**Suggested Resolution Options:**
1.  **Adopt Option B + Increase Shell Depth to 600mm**:
    *   Enable Split Tanks (Option B).
    *   Increase `shell_depth` to **600mm** (matches CONFLICT-001 recommendation).
    *   Place tanks longitudinally starting from the garage shell and extending forward into the dinette/kitchen base units to hit X=2380 centroid.
    *   *Status*: **STRONGLY RECOMMENDED**

2.  **Custom Tank Shapes**:
    *   Commission custom L-shaped or narrower tanks to fit current geometry.
    *   *Cons*: High cost, long lead time.

**Agent Recommendation:**
This conflict double-confirms the need to standardize on a **600mm shell depth**. It solves both the battery fitment (CONFLICT-001) and enables the only viable water tank option (Option B) that respects vehicle dynamics.

**Status:** RESOLVED
**Resolution:** Adopted Scenario E (Mass Balance).
- **Water Tank 1 (Passenger):** Standard 560mm High tank in Kitchen Base (alongside Batteries).
- **Water Tank 2 (Driver):** **Custom Low-Profile Tank** (H=400mm) under Dinette Bench.
- **Rationale:** Splits water mass 250kg/250kg. The Passenger tank helps counter the Diesel mass.
