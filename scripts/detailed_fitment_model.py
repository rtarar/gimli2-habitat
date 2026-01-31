
import cadquery as cq

# --- Parameters ---
# Cabinet Space (Kitchen Base)
CABINET_DEPTH = 600.0   # mm
CABINET_HEIGHT_CLEAR = 860.0 # mm (Under counter 900 - top thickness)
# Kitchen starts at X_offset (behind bathroom). Length available?
# Bathroom (800) + Kitchen (2300)? Or Kitchen is the remaining space?
# Let's verify Kitchen Length available.
# We need to fit Battery Stack + Water Tank 1 side-by-side or fore-aft.

# Components
# Water Tank 1 (Standard Option B)
TANK1_L = 900.0
TANK1_W = 500.0
TANK1_H = 560.0
TANK1_CLEARANCE = 20.0

# Battery Stack (6 modules)
# 6x 540L x 250W x 220H
# Configuration: 3 High x 2 Deep? Or 3 Wide? 
# To optimize compactness in the cabinet.
# Let's try "Block" configuration.
BAT_MOD_L = 540.0
BAT_MOD_W = 250.0
BAT_MOD_H = 220.0
BAT_CLEARANCE = 25.0

# Driver Side Custom Tank
# Target Volume: 250 Liters
# Space: Under Dinette Bench (H_clear < 450mm).
# Dinette Bench Length: ~1200mm? (Side bench).
# Dinette Bench Width: 400mm? (Standard seat depth).
# If Seat Depth is 400mm, we can't fit a 500mm wide tank without widening the bench base.
# Decision: Widen bench base to 500mm? Or make tank longer/narrower?
# Let's test fit.

def model_kitchen_base(show_result=True):
    # --- 1. KITCHEN BASE LAYOUT (Passenger Side) ---
    # Constraint: Depth 600mm.
    
    # Battery Stack Layout
    # Option: 2 columns of 3 high.
    # W = 2 * (250 + 25) = 550mm. Fits in 600 Depth? Yes.
    # H = 3 * (220 + 25) = 735mm. Fits under 860 Height? Yes.
    # L = 540 + 25 = 565mm.
    # Footprint: 565mm (Longitudinal) x 550mm (Depth).
    
    # Water Tank 1 Layout
    # L = 900 + 40 = 940mm.
    # W = 500 + 40 = 540mm. Fits in 600 Depth? Yes.
    # H = 560 + 20 = 580mm. Fits under 860 Height? Yes.
    
    # Total Longitudinal Length Required:
    # 565 (Batts) + 940 (Tank) + 50 (Separation) = 1555mm.
    # Kitchen Zone Length is ~2300mm.
    # 1555mm < 2300mm. FITS EASILY!
    
    # Visualization
    batteries = cq.Workplane("XY").box(565, 550, 735).translate((565/2, 0, 735/2))
    tank1 = cq.Workplane("XY").box(940, 540, 580).translate((565 + 50 + 940/2, 0, 580/2))
    
    kitchen_assembly = cq.Assembly()
    kitchen_assembly.add(batteries, name="Battery_Bank", color=cq.Color("red"))
    kitchen_assembly.add(tank1, name="Water_Tank_1", color=cq.Color("blue"))
    
    # --- 2. DRIVER SIDE CUSTOM TANK ---
    # Constraint: Under Dinette Bench.
    # Bench Height = 450mm ( Seat Top). Internal Clear ~430mm?
    # Bench Depth = 400mm (Standard).
    # Need 250 Liters.
    
    # Attempt 1: Keep 400mm Depth (matches seat).
    # H = 400mm (max sensible).
    # Area Req = 250L / 4dm = 62.5 dm^2.
    # W = 4dm (400mm).
    # L = 62.5 / 4 = 15.625 dm = 1562.5 mm.
    # Does 1562mm fit?
    # Dinette Side Bench is usually ~1200mm long?
    # Check ZONE-005 file: "driver_side_bench: length: 1200".
    # 1562mm > 1200mm. FAILS LENGTH.
    
    # Attempt 2: Widen Bench Base (Intrudes into footwell).
    # Let's widen to 500mm or 600mm?
    # If W = 600mm (extends 200mm past seat? Or seat is 600 deep?)
    # Lounge seating is often 600 deep. Dining is 400-500.
    # Let's propose W = 550mm base.
    # L = 1200mm (max).
    # H = 400mm.
    # Vol = 12 * 5.5 * 4 = 264 Liters.
    # FITS!
    # Trade-off: Bench base is 550mm deep. Seat cushion can be 500mm.
    # Reduced footwell width by ~150mm.
    
    # Visualization
    tank2_custom = cq.Workplane("XY").box(1200, 550, 400).translate((0, -2000, 200)) # Offset for viz
    
    if show_result:
        print(f"KITCHEN BASE: Fits. Used 1555mm of ~2300mm.")
        print(f"DRIVER TANK: Custom 1200(L)x550(W)x400(H). Vol={1.2*0.55*0.4*1000}L.")
        print(f"  - Requires widening Dinette Bench base to 550mm.")
    
    return kitchen_assembly

if __name__ == "__main__":
    model_kitchen_base()
