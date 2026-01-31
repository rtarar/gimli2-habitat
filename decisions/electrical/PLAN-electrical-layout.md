# Decision Log: Battery & Electrical Component Placement

## Core Question
Now that the Water Tank is defined (Low Profile U-Shape), where should the **Battery Bank (300kg)** and **Electrical Core (Inverter/Fuses)** be placed?
Also, how should we utilize the newly available space in the Rear Bench (above the low-profile tank connector)?

## Analysis: Component Proximity

### 1. Battery <-> Inverter
**Rule:** These should be as close as physically possible.
*   **Reason:** High current (up to 250A-300A for a 3kW inverter).
*   **Impact:** Long cables require massive gauge (4/0 AWG), are heavy, expensive, and suffer voltage drop.
*   **Target:** < 1 meter cable run.

### 2. Battery <-> Center of Gravity (Axle)
**Rule:** Heavy items (300kg) must balance the vehicle.
*   **Current State:**
    *   Water Tank (500kg) is rear-biased (Centroid Z ~ -700).
    *   Axle is at Z = -250.
    *   Rear Garage structure is heavy and far back.
*   **Impact:** Placing batteries in the rear (Z ~ -1700) would make the vehicle dangerously tail-heavy.
*   **Recommendation:** Batteries **MUST BE FORWARD** of the axle to counterbalance the rear water/structure.

## Evaluation of Locations

### Option A: Rear Bench (Inside U-Shell)
*   **Mass Balance:** **POOR CRITICAL**. Adds 300kg to the rear lever arm.
*   **Electrical Efficiency:** Good if inverter is also there.
*   **Conclusion:** Rejected due to weight distribution risks.

### Option B: Forward Kitchen Base (Passenger Side)
*   **Mass Balance:** **EXCELLENT**. Placing 300kg at Z ~ +800 acts as a counterweight to the rear loads.
*   **Electrical Efficiency:** Good location for centralized distribution.
*   **Space:** The "Toe-Kick" water tank extension is only 200mm high. The kitchen base is ~860mm high.
    *   Tank: 0-200mm.
    *   **Available for Voltage:** 200mm - 800mm.
    *   Plenty of space above the water tank extension.

## Proposed Layout

### 1. Electrical & Battery Zone (Passenger Kitchen/Dinette Base)
*   **Location:** Passenger side, forward of the U-Shell arms.
*   **Stack:**
    *   **Level 0 (Floor):** Water Tank Extension (Height 200mm).
    *   **Level 1 (Shelf above Tank):** **Battery Bank** (300kg). Securely mounted to chassis/floor through the shelf.
        *   Proximity to Axle: Forward (~1m in front of axle).
    *   **Level 2 (Vertical Compartment):** **Inverter/Charger + Fuses + Busbars**.
        *   Mounted directly above or adjacent to batteries.
        *   Cable run: Extremely short (~30-50cm).

### 2. Rear Bench Space (Utility Zone)
*   **Space Available:** Above the slim 150mm deep water manifold.
*   **Usage:**
    *   **Plumbing Core:** Water Pump, Accumulator, Water Filter, Valves.
        *   *Reason:* Close to the main tank connector. Leaks are contained in the "wet" rear zone.
    *   **Storage:** Light items only (Bedding, Clothes).

## Decision Recommendation
1.  **Keep Batteries Forward:** Essential for safe vehicle handling.
2.  **Keep Inverter with Batteries:** Essential for electrical performance.
3.  **Use Rear Bench for PLUMBING:** Keep the water pump and complex manifold logic back there, close to the tank source.

**Status:** Proposed for User Approval.
