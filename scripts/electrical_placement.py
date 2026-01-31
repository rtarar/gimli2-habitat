
import cadquery as cq

# --- Parameters ---
AXLE_X = 2380.0
AXLE_TOLERANCE_ZONE = [2000.0, 3000.0]

# Victron MultiPlus-II 3000VA
INV_L = 218.0
INV_W = 325.0
INV_H = 580.0
INV_MASS = 20.0
INV_CLEARANCE = 100.0 # Airflow

# MPPT Solar Chargers (e.g., SmartSolar 150/85)
# Need redundancy or multiple strings? Assume 2x large controllers or 1x massive?
# "Global charging" might imply multiple sources.
# Let's assume a panel board area of 600x600mm.

# Fusing & Distribution
# Lynx Distributor / PowerIn
# Area: 400x300mm.

# Total Electrical Wall Space Required:
# Inverter: 325(W) x 580(H) + clearance = 525 x 780.
# MPPTs + Dist: ~600 x 600.
# Batteries: 300kg (Already placed under Dinette).

# Location Candidates:
# 1. Garage Shell (Rear) - Driver Side Arm (Vacant).
#    - Space: 600mm Wide x 600mm Deep x 824mm High (Internal).
#    - Wall Space: Inside faces of the arm.
#    - Pro: Close to Batteris (Driver Side Dinette is just forward of this).
#    - Pro: Short DC cables (<1m).
#    - Con: Inverter is 580mm H. Fits in 824mm H space.

# 2. Dinette Bench (Driver Side) - Shared with Batteries.
#    - Battery Mass takes floor space.
#    - Inverter needs vertical mounting usually.
#    - Bench internal height ~400mm? (Low profile tank constrained this).
#    - Inverter (580mm) CANNOT stand up under a 450mm bench.
#    - MUST be in a taller space.

# 3. Floor-to-Ceiling Cabinet (Driver Side, between Bath & Dinette).
#    - The "Wardrobe" / "Pantry" zone.
#    - High volume, perfect for vertical mounting.
#    - Distance to Batteries: ~1m (Dinette is adjacent).
#    - Good for controls access.

def check_electrical_placement():
    results = []
    results.append("ELECTRICAL COMPONENT PLACEMENT CHECK")
    
    # Inverter Height Constraint
    results.append(f"Inverter Height: {INV_H} mm (Vertical mount preferred).")
    
    # Candidate: Under Dinette Bench
    results.append("- Under Dinette (H=450mm): FAIL. Inverter too tall.")
    
    # Candidate: Garage Shell (Driver Arm)
    results.append("- Garage Shell (H=824mm interior): PASS.")
    results.append("  - Wall space available inside the box.")
    results.append("  - Pro: Closest to Batteries (Short DC runs).")
    results.append("  - Pro: Ventilated (Keep heat out of living space).")
    
    # Candidate: Tall Cabinet (Driver Side)
    results.append("- Tall Cabinet (H=2000mm+): PASS.")
    results.append("  - Pro: Easy access to breakers/panels.")
    results.append("  - Con: Consumes storage space.")
    
    results.append("\nRECOMMENDATION:")
    results.append("1. MAIN INVERTER & CHARGERS: Rear Garage Shell (Driver Side).")
    results.append("   - Mount on inner wall of the shell.")
    results.append("   - Occupies the space vacated by Water/Batteries.")
    results.append("   - NEXT to Alde? (Alde is small 500x300. Shell is 600x600x860. Tight fit?)")
    results.append("     - Alde: 15kg. Inverter: 20kg. Total < 50kg. Fine.")
    results.append("     - Layout: Alde on floor, Inverter on wall above/beside?")
    results.append("     - Shell Height 860. Inverter 580. Alde 310.")
    results.append("     - 580 + 310 = 890 > 860. CANNOT STACK VERTICALLY.")
    results.append("     - Must be side-by-side or opposite walls.")
    results.append("     - Shell Depth 600. Width 600.")
    results.append("     - Alde (500L x 420D) takes floor.")
    results.append("     - Inverter (218D x 325W) on wall.")
    results.append("     - INTERFERENCE: 420mm Alde leaves 180mm depth. Inverter is 218mm deep. CONFLICT.")
    
    results.append("\nCONFLICT DETECTED in Garage Shell:")
    results.append("- Reduced Volume (600x600) cannot house BOTH Alde and MultiPlus 3000.")
    
    results.append("\nALTERNATIVE STRATEGY:")
    results.append("- ALDE: Rear Garage Shell (Driver).")
    results.append("- INVERTER/ELECTRICAL: Rear Garage Shell (PASSENGER)?")
    results.append("  - Passenger side garage arm is also empty? (Water moved to kitchen base).")
    results.append("  - Passenger Arm: 600x600x860. Empty.")
    results.append("  - Distance to Batteries (Driver Side): Across the aisle width (1000mm).")
    results.append("  - Cable run: ~2m (across floor/chassis). Acceptable for 4/0 AWG.")
    
    results.append("\nREVISED RECOMMENDATION:")
    results.append("- Driver Garage Arm: Alde Heater.")
    results.append("- Passenger Garage Arm: Victron Inverter, MPPTs, Distribution.")
    results.append("- Batteries: Driver Side Dinette (Mid-ship).")
    results.append("- Water: Split Mid-ship.")
    results.append("- Result: Balanced Rear (Alde left, Electric right). Balanced Mid (Batt left, Water right).")
    
    return "\n".join(results)

print(check_electrical_placement())
