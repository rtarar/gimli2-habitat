
import cadquery as cq

# --- Parameters ---
TOTAL_VOLUME_L = 500.0
# Constraints
REAR_AXLE_X_FROM_REAR = 2380.0
Z_MAX_FROM_FLOOR = 800.0
X_TOLERANCE_CENTER = 300.0
CLEARANCE = 20.0

# Tank Specs
# Option A
OPT_A_L = 1200.0
OPT_A_W = 600.0
OPT_A_H = 700.0
OPT_A_MASS = 500.0
# Option B (Split)
OPT_B_L = 900.0
OPT_B_W = 500.0
OPT_B_H = 560.0 # Each
OPT_B_MASS = 250.0 # Each

# Habitat Geometry for Placement Logic
# Garage Shell Arm (ZONE-003)
# Assuming 600mm depth (recommended change) or 509mm (current)?
# Let's assume 600mm to even see if it fits, otherwise revert to 509mm logic
SHELL_DEPTH = 600.0 
SHELL_WALL = 18.0
INNER_WIDTH_ARM = SHELL_DEPTH - 2 * SHELL_WALL 
# If shell_depth=600, inner=564mm. If shell_depth=509, inner=473mm.

REAR_WALL_THICKNESS = 60.0 # usually external minus internal
# Coordinates: Rear Wall Interior Face is Y=0? 
# Usually in 3D: Z is front-to-rear length? 
# Let's align with habitat.yml: X=Left/Right, Y=Up, Z=Front/Rear
# Wait, analyze_step_solids output implied Y=Up, Z=Longitudinal?
# "X=driver-to-passenger" (Width 2280)
# "Y=floor-to-ceiling" (Height 2160)
# "Z=rear-to-front" (Length 4780)
# Origin: Rear Axle is Z = 2380 from Rear Wall (Z=0)
# Actually, let's just stick to the prompt's frame: "Rear axle located at x = 2380 mm from rear wall"
# So prompt uses X = Longitudinal?
# Let's assume Prompt X = Longitudinal Distance from Rear Wall.

def analyze_tank_fit():
    results = []

    # OPTION A: Single Tank
    # Dim: 1200(L) x 600(W) x 700(H)
    # Fit in Garage Arm?
    # Arm Depth (Prompt-Frame Y width?) = 600mm? No, arm extends forward.
    # Garage Arm is a long box along the side wall.
    # Interior Width available inside arm = SHELL_DEPTH - 2*Walls.
    
    # If Shell Depth = 509 mm -> Inner = 473mm.
    # Tank W = 600mm.
    # FAIL. Option A cannot fit inside a 509mm deep arm. 
    # Even with 600mm depth -> Inner = 564mm. 600mm tank > 564mm. FAIL.
    
    # Option A must go SOMEWHERE ELSE if it doesn't fit in arms?
    # Center of U-Bench?
    # Center Width = 2280 - 2*Arms.
    # If 509mm arms => 1262mm width. Tank L=1200mm fits!
    # If 600mm arms => 1080mm width. Tank L=1200mm FAIL.
    
    results.append("OPTION A (Single 1200x600x700):")
    results.append(" - In 509mm Arms: FAIL (Width 600 > 473)")
    results.append(" - In 600mm Arms: FAIL (Width 600 > 564)")
    results.append(" - In Center (509mm arms): FITS (Width 1262 > 1200).")
    results.append("   - Centroid X = tank L/2 = 600mm from rear wall?")
    results.append("   - Target X = 2380 +/- 300 (2080-2680).")
    results.append("   - 600mm is WAY too far rear. Bad weight distribution.")

    # OPTION B: Split Tanks (2x)
    # Dim: 900(L) x 500(W) x 560(H)
    # Fit in Arms?
    # W=500mm.
    # In 509mm Arms (Inner 473mm): FAIL (500 > 473).
    # In 600mm Arms (Inner 564mm): FITS (500 < 564).
    
    results.append("\nOPTION B (Split 900x500x560):")
    results.append(" - In 509mm Arms: FAIL (Width 500 > 473)")
    results.append(" - In 600mm Arms: FITS (Width 500 < 564)")
    
    # Check placement for Option B in 600mm Arms
    # Place one in Driver Arm, one in Passenger Arm.
    # Longitudinal Position (Prompt X):
    # Length = 900mm.
    # We want centroid at X=2380.
    # So Tank Extent = [2380 - 450, 2380 + 450] = [1930, 2830]
    # Check bounds: rear wall is X=0.
    # Is Garage Shell long enough?
    # Shell extends forward?
    # Current Shell definition doesn't specify length forward clearly, just "U shape".
    # Usually Garage is at REAR.
    # If we place tanks at X=2380 (near axle), that is likely OUTSIDE the traditional "Garage" zone (usually X=0 to X=1200 or so).
    # X=2380 is mid-ship (Dinette/Kitchen area).
    
    # This implies tanks are NOT in the rear garage bench, but under the Dinette/Kitchen benches forward of the garage?
    
    return "\n".join(results)

print(analyze_tank_fit())
