
import cadquery as cq

# --- External Masses (Fixed) ---
# Driver Side (-X)
DIESEL_MASS = 500.0 * 0.85 # approx 0.85 kg/L + tank weight -> ~450kg? Or user said "500L diesel tank"... assume 450-500kg. Let's use 450kg.
DIESEL_X = -1000.0 # Arbitrary negative X for Driver Side

# Passenger Side (+X)
GREY_MASS_EMPTY = 30.0 # Tank weight
GREY_MASS_FULL = 330.0 # 300L
# Design condition: User said "mostly empty". Use Empty or Partial?
# Let's design for "Travel Condition" -> Diesel Full, Grey Empty.
GREY_TRAVEL_MASS = 30.0 
GREY_X = 1000.0 # Arbitrary positive X for Passenger Side

# Imbalance to correct:
# Driver: 450kg
# Passenger: 30kg
# Delta: -420kg (Left heavy).
# WE NEED +420kg on Passenger Side to level the truck.

# --- Internal Systems (Moveable) ---
# Batteries: 300kg.
# Water: 500kg (500L).
# Inverter/Alde: ~50kg total (Negligible compared to tank deltas, but useful for fine tuning).

def calculate_balance():
    results = []
    results.append(f"EXTERNAL IMBALANCE (Travel Mode): {DIESEL_MASS}kg (Driver) vs {GREY_TRAVEL_MASS}kg (Pass). Delta = {GREY_TRAVEL_MASS - DIESEL_MASS} kg.")
    results.append("TARGET: Shift ~400kg of internal mass to Passenger Side.")
    
    # Scenario A: Previous "Axle Center" (Split Water, Split Batts/Elec)
    # Batts (300) Driver. Water (250) Driver. Water (250) Pass.
    # Driver Internal: 300 + 250 = 550.
    # Passenger Internal: 250.
    # Total Imbalance: (450+550) vs (30 + 250) = 1000 vs 280.
    # DISASTER. 720kg list to Driver side.
    results.append("\nSCENARIO A (Previous Plan): FAIL. 720kg Driver-Heavy list.")
    
    # Scenario B: Move Batteries to Passenger Side
    # Batts (300) Pass.
    # Water: Split 250/250.
    # Driver Internal: 250 (Water).
    # Pass Internal: 300 (Batts) + 250 (Water) = 550.
    # Totals:
    # Driver: 450 (Diesel) + 250 (Water) = 700.
    # Pass: 30 (Grey) + 550 (Int) = 580.
    # Delta: 120kg Driver-Heavy.
    # MUCH BETTER. Acceptable? Maybe.
    results.append("\nSCENARIO B (Batts on Passegner): BETTER. 120kg Driver-Heavy.")
    
    # Scenario C: Move Batteries AND Bias Water to Passenger
    # Batts (300) Pass.
    # Water Option A (Single 500L)? No, fits poorly.
    # Water Option B (Split): Both on Passenger?
    # can we fit 2x900mm tanks in Passenger Kitchen?
    # Kitchen Length ~2300mm.
    # 2x 900 = 1800mm.
    # Batts (Stack of 6?): 540mm long?
    # 1800 + 540 = 2340mm.
    # TIGHT fit in 2300mm kitchen.
    # Maybe place Batts in Rear Garage Passenger Arm?
    
    # Let's try:
    # Driver Internal: Empty / Light (Alde + Inverter = 40kg).
    # Pass Internal: Batts (300) + Water (500).
    # Totals:
    # Driver: 450 + 40 = 490.
    # Pass: 30 + 800 = 830.
    # Delta: 340kg PASSENGER-Heavy.
    # Over-corrected.
    
    # Scenario D: Perfect Balance?
    # We need Pass Internal = Driver Internal + 420.
    # Total Internal Mass = 800kg (Water+Batts).
    # P = D + 420.
    # P + D = 800.
    # (D+420) + D = 800 => 2D = 380 => D = 190kg.
    # P = 610kg.
    # So we need ~610kg on Passenger, ~190kg on Driver.
    
    # Combination D:
    # Passenger: Water (500kg) + Inverter (20kg)? = 520kg.
    # Driver: Batteries (300kg) + Alde (15kg) = 315kg.
    # Imbalance Check:
    # Driver Total: 450 (Diesel) + 315 = 765.
    # Pass Total: 30 (Grey) + 520 = 550.
    # Still Driver Heavy (215kg).
    
    # Combination E (Batts on Pass):
    # Passenger: Batteries (300kg) + Water 1 (250kg) = 550kg.
    # Driver: Water 2 (250kg).
    # Check:
    # Driver Total: 450 (Diesel) + 250 = 700.
    # Pass Total: 30 (Grey) + 550 = 580.
    # Delta: 120kg Driver Heavy.
    # This is likely the sweet spot. 120kg is < 2 adults (maybe).
    # Also Diesel burns off. At 50% fuel (225kg):
    # Driver: 225 + 250 = 475.
    # Pass: 30 + 550 = 580.
    # Delta: 105kg Passenger Heavy.
    # This swings from +120 Left to +100 Right depending on fuel.
    # THIS IS BALANCED.
    
    results.append("\nSCENARIO E (OPTIMAL):")
    results.append("- Passenger Side: Batteries (300kg) + Water Tank 1 (250kg).")
    results.append("- Driver Side: Water Tank 2 (250kg).")
    results.append("  - Plus Diesel (450kg).")
    results.append("- Dynamic Balance: swings +/- 100kg depending on fuel state.")
    
    # GEOMETRY CHECK FOR SCENARIO E
    # Passenger Side (Kitchen Base):
    # Needs to fit Batts + Tank 1.
    # Tank 1: 900mm L.
    # Batts (6x): Stacked 2x3?
    #   - 3x 250mm wide = 750mm? No, 6 mods.
    #   - 3 long, 2 high? 3*540 = 1620mm. Too long.
    #   - 3 wide? 3*250 = 750mm. Depth 600. Fits.
    #   - Length = 540mm.
    #   - So 2x3 Stack is approx 540mm Long x 750mm Wide.
    #   - Wait, Kitchen Depth is 600mm. 750mm W won't fit.
    #   - Orientation: Long axis parallel to wall?
    #   - Batts are 540L x 250W.
    #   - 2 Deep (500mm) fits in 600mm cabinet.
    #   - 3 High? 3*220 = 660mm. Fits under 900 counter.
    #   - Length: 540mm.
    #   - So stack is 540mm L x 500mm D x 660mm H.
    #   - Fits nicely in Kitchen Base.
    #   - Remaining Kitchen Length: 2300 - 540 (Batts) - 900 (Tank) = 860mm.
    #   - PLENTY of space.
    
    results.append("\nPLACEMENT E:")
    results.append("- Passenger Mid-Ship (Kitchen):")
    results.append("  - Battery Stack (300kg).")
    results.append("  - Water Tank 1 (250kg).")
    results.append("- Driver Mid-Ship (Dinette):")
    results.append("  - Water Tank 2 (250kg) - Custom Low Profile.")
    results.append("- Rear Garage (Driver): Alde.")
    results.append("- Rear Garage (Passenger): Electrical.")
    
    return "\n".join(results)

print(calculate_balance())
