
import cadquery as cq

# --- Parameters ---
AXLE_X = 2380.0
AXLE_TOLERANCE = 300.0  # Range: 2080 - 2680

# Systems
# Water Option B (Split)
TANK_L = 900.0
TANK_W = 500.0
TANK_H = 560.0
TANK_MASS = 250.0 # Each

# Batteries (6x modules)
BAT_L = 540.0
BAT_W = 250.0
BAT_H = 220.0
BAT_MASS = 50.0
TOTAL_BAT_MASS = 300.0

# Furniture / Zones geometry (Approximate X ranges from Rear Wall = 0)
# Length = 4780
# Rear Wall = 0
# Front Wall = 4780

# ZONE-003 Garage Shell (High Bench, H=860)
# Location: Rear. Depth 600mm.
GARAGE_X_START = 0
GARAGE_X_END = 600
GARAGE_H = 860
# Valid for tanks/batteries height-wise (H > 560).
# Invalid for location (600 < 2080).

# ZONE-005 Living/Dinette (Driver Side)
# Location: Forward of Garage. X = 600 to ??
# Seats: H = 450 mm.
# Tank H (560) > Seat H (450).
# BAT H (220) < Seat H (450). -> BATTERIES FIT UNDER SEATS!

# ZONE-002 Kitchen (Passenger Side)
# Location: Forward of Garage? Or does it start later?
# "Behind bathroom". Bath is at Front (4780, depth 800) -> Ends at 3980.
# Kitchen starts at 3980? Runs rearward?
# Zone-002 file: "from_front: 1200". Front=4780. So starts at 3580?
# Depth 2300. 3580 - 2300 = 1280.
# So Kitchen spans X = 1280 to 3580.
# Overlaps Axle (2380)? YES.
# Height: 900 (Countertop).
# Tank H (560) < Counter H (900). -> TANKS FIT IN KITCHEN!
# Batteries H (220) < Counter H (900). -> BATTERIES FIT IN KITCHEN!

def check_placement():
    results = []
    results.append(f"TARGET AXLE ZONE: X = {AXLE_X} +/- {AXLE_TOLERANCE} ({AXLE_X - AXLE_TOLERANCE} to {AXLE_X + AXLE_TOLERANCE})")

    # 1. WATER TANKS (2x)
    # Tank 1: Passenger Side (Kitchen)
    # Kitchen spans 1280 - 3580.
    # Axle is 2380.
    # PERFECT FIT.
    results.append("WATER TANK 1 (Passenger): Fits in Kitchen Base Cabinet.")
    results.append(" - Location: Centered at X=2380.")
    results.append(" - Height Clearance: 560mm < 900mm.")
    
    # Tank 2: Driver Side (Dinette)
    # Dinette Bench spans X = 600 to 2600 (length 2000).
    # Axle (2380) is under the Dinette Bench.
    # Height Constraint: Seat Height = 450mm.
    # Tank Height = 560mm.
    # CONFLICT: Tank is taller than the seat.
    results.append("WATER TANK 2 (Driver): CONFLICT.")
    results.append(" - Location: Fits longitudinally (X=2380 is under bench).")
    results.append(" - Height Conflict: Tank (560mm) > Seat (450mm).")
    results.append(" - Solution A: Raise bench to 600mm? (Uncomfortable).")
    results.append(" - Solution B: Custom Tank (Lower/Wider)?")
    results.append("   - If H=400, Vol=250L -> Area = 0.25 / 0.4 = 0.625 m2.")
    results.append("   - If W=500mm, Length = 1250mm. (Fits length-wise).")
    results.append(" - Solution C: Place both tanks on Passenger Side? (Heavy imbalance).")
    results.append(" - Solution D: Tank in Garage Shell (Rear)? (Violates Axle pref).")

    # 2. BATTERIES (6x)
    # Total Mass 300kg.
    # Option: Driver Side (balance Kitchen).
    # Fits under Dinette Seat (H=450)?
    # Battery H = 220 + Clearance = 270mm.
    # 270 < 450. FITS!
    results.append("\nBATTERIES (Driver Side): Fits under Dinette Bench.")
    results.append(" - Height: 270mm < 450mm.")
    results.append(" - Mass: 300kg helps balance Kitchen side.")
    results.append(" - Location: Can center near Axle (2380).")
    
    # 3. SUMMARY
    # Passenger Side: 1x Water Tank (250kg) + Kitchen Mass.
    # Driver Side: Batteries (300kg) + 1x Water Tank (250kg)?
    #   - If we solve the Tank Height issue.
    #   - If we use a custom "Low Profile" tank for Driver side: 1250L x 500W x 400H.
    #     - Fits under 450mm seat!
    
    results.append("\nRECOMMENDATION:")
    results.append("- Passenger Side: Standard shape tank (Option B) in Kitchen.")
    results.append("- Driver Side: Custom LOW PROFILE tank + Batteries under Dinette Bench.")
    
    return "\n".join(results)

print(check_placement())
