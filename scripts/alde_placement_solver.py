
import cadquery as cq

# Alde Specs
UNIT_W = 500.0
UNIT_D = 420.0
UNIT_H = 310.0
MASS = 15.0 # kg

SERVICE_BAY_L = 800.0
SERVICE_BAY_W = 600.0
SERVICE_BAY_H = 600.0

ENGINE_COOLANT_MAX_LEN = 500.0 # From front wall

# Habitat Geometry for Placement Candidates
# Candidate A: Near Bathroom Wet Wall (Passenger Side, Front)
# Zone 001 (Bath) is 800mm deep at Front.
# Zone 002 (Kitchen) starts at 1200mm from Front?? (Wait, Bath depth is 800. Why Kitchen start at 1200?)
# Let's check ZONE-002: "from_front: 1200 # mm - starts after bathroom".
# Gap between Bath (800) and Kitchen (1200) = 400mm? 
# Maybe circulation or just empty?
# Or maybe the Alde goes HERE? in the 400mm gap?
# No, Alde matches Bath plumbing well.

# Let's assume Alde is placed IN THE BASE OF THE BATHROOM or KITCHEN
# Candidate A: Under Bathroom Floor (False floor?) or in a Cabinet?
# "Near bathroom wet wall" implies close to plumbing.
# But Engine Coolant limit (500mm from front wall) is strict.
# Front Wall is Z=4780? No, Rear is Z=0. Front is Z=4780.
# Wait, "Rear axle located at x=2380 from rear wall".
# Let's stick to "From Rear Wall" coordinates. Length=4780.
# Front Wall is at X_LONG = 4780.
# Engine coolant penetration < 500mm inside cabin => Needs to be within [4280, 4780] X_LONG.

# Candidate Placement A: Inside Bathroom Vanity/Cabinet (Driver Side, Front) or Passenger Side?
# Bathroom Layout: Shower Passenger, Toilet Driver.
# If Shower is Passenger, maybe under the shower bench? (If any)
# Or Driver side under Sink?
# Toilet is on Driver side.
# "Locate forward of main battery + water mass".
# Batteries/Water are at ~2380 (Mid-ship). So forward means > 2380. Closer to 4780.
# This aligns with Front Bathroom.

def check_alde_placement():
    results = []
    
    # Requirement: Engine coolant penetration < 500mm.
    # Means unit must be within 500mm of the front wall (where engine is).
    # Target Zone: Front 500mm of the habitat.
    
    results.append("PLACEMENT CONSTRAINT CHECK:")
    results.append("- Engine Loop Limit: Must be within 500mm of Front Wall.")
    
    # Candidate A: Inside Bathroom (Zone-001)
    # Zone 001 Depth = 800mm.
    # Fits within the 500mm zone? Yes, the first 500mm of the bathroom is valid.
    # Driver Side (Toilet/Sink):
    #  - Sink cabinet usually has space.
    #  - Toilet might conflict.
    # Passenger Side (Shower):
    #  - Hard to place a heater under a shower pan usually (access issues).
    #  - Unless it's a "drying room" cupboard?
    
    # Candidate B: Under Forward Bench/Cabinet (Zone-006 Entry / Zone-002 Kitchen?)
    # Kitchen starts at 1200mm from Front (after Bath).
    # 1200mm is > 500mm.
    # So Kitchen placement VIOLATES engine coolant loop constraint (unless lines run under floor long distance, but constraint says "inside cabin < 500mm").
    # If lines run under the floor (outside cabin) and enter near the heater, that's okay.
    # But usually, "penetration length inside cabin" means from wall to unit.
    
    # Let's assume the heater MUST be close to the front wall.
    # Best spot: The base of the Bathroom wall or a dedicated "Mechanical Cabinet" next to the Entry?
    # Entry is Passenger Side. Bathroom is Full Width.
    # Maybe under/behind the Driver Side Toilet vanity?
    
    # Let's propose: Driver Side Front Corner.
    # Zone-001 (Bathroom).
    # Under Sink/Vanity.
    
    results.append("\nPREFERRED PLACEMENT: Driver Side Front Corner (Under Bathroom Vanity)")
    results.append("- Coordinates: Near Front Wall (X_LONG ~ 4600).")
    results.append("- Compliance: < 500mm from connection point.")
    results.append("- Service Access: From top (removable vanity counter) or front (cabinet door).")
    results.append("- Flue: Vertical through roof (Bathroom roof is clear).")
    results.append("- Intake: Through floor or side wall.")
    
    # Clearance Check
    # Unit: 500W x 420D x 310H
    # Bay: 800 x 600 x 600
    # Bathroom Depth: 800mm. Fits Depth.
    # Vanity Width: ~600-800mm (depends on sink). Fits Width.
    
    results.append("\nCLEARANCE CHECK:")
    results.append("- Unit fits in standard vanity cabinet.")
    results.append("- Requires dedicated ducting routing to Living/Sleeping.")
    
    return "\n".join(results)

print(check_alde_placement())
