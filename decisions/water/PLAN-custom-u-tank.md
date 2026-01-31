# Decision Log: Custom U-Shaped Water Tank Feasibility

## Context
The user requested an analysis of a custom U-shaped water tank integrated into the U-shaped rear seating/garage shell structure.
The goal is to maximize water capacity (target 500-600L), improve mass balance (centering weight), and utilize the "dead space" under the seating.

## Constraints & Assumptions
1.  **Geometry:**
    *   **Rear Section:** 2280mm (W) x 600mm (D) x 400mm (H)
    *   **Side Arms:** Two arms, extending forward from the rear section.
    *   **Arm Dimensions:** 600mm (W) x 800mm (L) x 400mm (H) (Length reduced to 800mm to fit Living Zone).
    *   **No Wheel Wells:** Confirmed by user. The floor is flat.

2.  **Mass Balance:**
    *   **Rear Axle Position:** ~2140mm from interior rear wall (from `habitat.yml` line 43 derived position, to be verified).
    *   **Diesel Tank:** Z = -500 (approx mid-rear).
    *   **Centroid Goal:** The tank's center of mass should be as close to the axle as possible.

3.  **Installation:**
    *   Must be installable through the rear hatches (600mm x 550mm) or entry door.
    *   A single rigid U-tank of this size is likely impossible to insert.
    *   **Solution:** Three separate rigid tanks (Rear + Left + Right) plumbed together with large diameter connections (e.g., 2-3" fernco or flange) to act as one volume, OR a custom rotomolded tank if it can be inserted before shell completion (unlikely for retrofit).
    *   **assumption:** We will model it as a verified volume, leaving the specific manufacturing (3-part vs 1-part) for detailed design.

## Finalized Design: "Clearance Adjusted" Extended U-Tank

### Geometry
1.  **Rear Connector (Manifold):**
    *   Dimensions: 2280mm (W) x 150mm (D) x 380mm (H)
    *   Purpose: Fluid balancing, minimal weight behind axle.
2.  **Living Zone Arms:**
    *   Dimensions: 350mm (W) x 800mm (L) x 380mm (H)
    *   Location: Inside dinette benches.
    *   Clearances: Left/Right gaps for 80/20 framing and PEX.
3.  **Forward Extensions (Toe-Kick):**
    *   Dimensions: 350mm (W) x 1500mm (L) x 180mm (H)
    *   Location: Under Kitchen and Cabinets (low profile).
    *   Purpose: Shifts mass forward of the axle.

### Volume Calculation (Net)
*   **Rear Connector:** ~130 Liters
*   **Living Arms:** ~212 Liters
*   **Forward Extensions:** ~190 Liters
*   **Total Volume:** **~532 Liters** (Meets 500-600L Goal)

### Mass Balance Analysis
*   **Axle Position (Z):** -250
*   **Tank Center (Estimated Z):** ~ -700
    *   Rear Connector is at Z ~ -1600.
    *   Forward Extensions reach to Z ~ +400.
    *   **Result:** Center of gravity is much closer to the axle (~450mm offset) compared to the original design (~1500mm offset).
    *   **Counter-Balance:** Batteries (300kg) at Z=+800 further neutralize this offset.
*   **Conclusion:** This design achieves high capacity with acceptable mass balance.

## Installation Strategy (3-Part)
*   The tank must likely be fabricated as 3 separate units (Left Side, Right Side, Rear Connector) and joined with large diameter flanges/hoses during assembly to allow installation into the shell.
*   **Clearances:** 100mm+ reserved width-wise in benches for systems routing avoids conflict with structural framing.
