## Decision: Electrical System Placement

**ID:** DEC-004
**Date:** 2026-01-31
**Status:** PROPOSED

## Decision Maker
- **Human:** User
- **AI Assistant:** Antigravity

## Context
The electrical system is substantial:
- **Inverter:** Victron MultiPlus-II 3000VA (Large vertical footprint, high heat).
- **Solar:** Global offshore capabilities (MPPTs).
- **Distribution:** Fuses, Busbars (Lynx system).
- **Batteries:** Located mid-ship driver side (resolved in CONFLICT-001).

Space Constraints:
- Inverter (580mm H) does not fit under Dinette Benches (450mm H).
- Driver Rear Garage Arm is occupied by Alde Heater (DEC-003).

## Options Considered

### Option 1: Passenger Rear Garage Arm (RECOMMENDED)
**Description:** Dedicate the Passenger Side Rear U-shell arm to electrical components.
**Pros:**
- **Volume:** 600x600x860mm space is sufficient for vertical mounting of Inverter + Solar Controllers.
- **Separation:** Keeps high-voltage/high-heat electronics away from water/plumbing (Kitchen/Bath).
- **Ventilation:** Can be vented to rear/side easily.
- **Balance:** Balances the Alde heater mass on the Driver side.
**Cons:**
- **Cable Run:** Requires crossing the aisle (~2m) to reach batteries. Acceptable.

### Option 2: Tall Cabinet (Driver Side)
**Description:** Upper section of a floor-to-ceiling cabinet.
**Pros:**
- **Access:** Eye-level controls.
**Cons:**
- **Center of Gravity:** High mass (20kg+) mounted high up is bad for vehicle dynamics.
- **Storage:** Consumes prime clothing/pantry space.

## Decision
**Select Option 1:** Place the Electrical Core (Inverter, MPPT, Dist) in the **Passenger Rear Garage Arm**.

## Rationale
This creates a symmetrical "Mechanical Rear":
1.  **Driver Rear:** Heating (Alde).
2.  **Passenger Rear:** Electrical (Victron).
3.  **Mid-Ship Passenger:** Batteries are just forward in the Kitchen Base. Cable run is short (~1.5m) and stays on the same side of the vehicle!

## Status
APPROVED - Confirmed by Mass Balance analysis.
