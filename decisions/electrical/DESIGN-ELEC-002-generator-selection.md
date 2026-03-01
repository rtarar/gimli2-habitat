# Generator Selection & Installation — Gimli2 Habitat

**ID:** DESIGN-ELEC-002
**Date:** 2026-02-28
**Status:** DRAFT — Pending Owner Review
**Resolves:** REVIEW-ELEC-001 Finding #1 (No backup charge source)
**Location:** Rear storage box area, driver side, behind rear storage

---

## 1. Sizing — How Big Does It Need to Be?

### 1.1 What the Generator Must Cover

The generator serves two roles — they have very different power requirements:

**Role A — Battery bank charging (primary use, 90% of runtime):**
The generator feeds the MultiPlus-II's built-in charger, which draws up to 2,880W from shore/generator AC input (120A × 24V). This is the main use case: park in jungle, run the generator for 3–4 hours, top up the batteries, shut down.

**Role B — Simultaneous charging + light AC loads:**
While charging batteries, you might also want to run the fridge on AC, charge laptops, and run lighting. This adds ~500W on top of the charger load.

| Use Case | Power Required |
|---|---|
| Battery charging only (MultiPlus charger) | 2,880 W |
| Charging + light AC loads | ~3,400 W |
| Charging + cooking (induction) | ~4,700 W (unlikely use case) |

### 1.2 Recommended Generator Size

**Minimum: 3.0 kW continuous.**
**Sweet spot: 3.5–4.0 kW continuous.**

At 3.5 kW, the generator comfortably runs the MultiPlus charger at full rate while handling background AC loads. You'd never need to cook on the generator (that's what the propane outdoor kitchen is for), so the 4.7 kW cooking scenario is irrelevant.

A 3.5 kW generator charging the 30.7 kWh battery bank at ~2.5 kW net (accounting for charger efficiency):

| Battery State | Charge Time to 90% |
|---|---|
| From 20% (emergency) | ~8.5 hours |
| From 50% (typical top-up) | ~4.7 hours |
| From 70% (light top-up) | ~2.4 hours |

---

## 2. Generator Comparison

### 2.1 The Contenders

I've evaluated five generators across two categories: purpose-built vehicle/marine units (premium, whisper-quiet) and conventional RV generators (proven, more affordable).

---

#### TIER 1 — Premium Whisper-Quiet (Expedition Grade)

**A. Fischer Panda Panda 4000s Neo PMS**

| Parameter | Value |
|---|---|
| Continuous output | 3.0 kW (3.6 kVA) |
| Max output | 3.4 kW (4.0 kVA) |
| Voltage | 230V / 50Hz (also available 120V / 60Hz) |
| Engine | Fischer Panda single-cylinder diesel, water-cooled |
| Cooling | Double-circuit freshwater heat exchanger |
| Noise | **54 dB(A) at 7m** |
| Dimensions | 558 × 460 × 518 mm (L × W × H) |
| Weight (dry) | **92 kg** |
| Fuel consumption | 0.6–1.2 L/hr |
| Key feature | "Supersilenced" — fully encapsulated, vibration-isolated |

**Verdict:** The gold standard for expedition vehicles. This is what Unicat specs. Water-cooled means no air vents needed in the compartment. 54 dB at 7m is conversational volume — you can run it at a campsite without annoying neighbours. The 230V output works directly with the MultiPlus-II in international mode; for NA, the MultiPlus accepts 120V or 230V input.

---

**B. Fischer Panda AGT-DC 4000 24V**

| Parameter | Value |
|---|---|
| Continuous output | 3.2 kW DC |
| Max output | 4.0 kW DC |
| Output | **24V DC direct** (no inverter/charger needed!) |
| Engine | Kubota diesel, water-cooled, variable speed |
| Noise | **54 dB(A) at 7m** |
| Dimensions | ~550 × 450 × 520 mm (estimated) |
| Weight (dry) | **90–142 kg** (depends on configuration) |
| Fuel consumption | 0.5–1.0 L/hr |
| Key feature | DC output charges batteries directly, bypassing the inverter/charger entirely |

**Verdict:** The most elegant solution for a 24V battery bank. The AGT-DC outputs 24V DC directly to the battery bus, eliminating the AC→charger conversion step. Higher efficiency, simpler integration, and the generator's variable-speed controller manages the charge profile. However, it's more expensive and niche — harder to find parts internationally. The Victron Lynx BMS would need to coordinate with the AGT's charge controller.

---

**C. WhisperPower Piccolo 4**

| Parameter | Value |
|---|---|
| Continuous output | 3.5 kW |
| Voltage | 120V or 230V options |
| Noise | **< 55 dB(A)** |
| Weight | **68 kg (150 lbs)** |
| Key feature | Lightest in class, compact diesel |

**Verdict:** Excellent weight-to-power ratio. 68 kg is significantly lighter than the Fischer Panda (92 kg). Similar noise levels. Good choice if weight is the primary concern. WhisperPower has a solid marine dealer network but less expedition-vehicle presence than Fischer Panda.

---

#### TIER 2 — Proven RV Generators (Value)

**D. Cummins Onan QD 3200**

| Parameter | Value |
|---|---|
| Continuous output | 3.2 kW |
| Voltage | 120V / 60Hz |
| Engine | 347cc single-cylinder diesel, air-cooled |
| Noise | **72 dB(A) at 3m** (~60 dB(A) at 50ft — meets National Park requirements) |
| Dimensions | 767 × 440 × 457 mm (L × W × H) |
| Weight | **93 kg (205 lbs)** |
| Fuel consumption | 0.3–0.7 L/hr |
| Key feature | Industry standard RV generator, massive dealer/parts network, runs from vehicle fuel tank |

**Verdict:** The workhorse choice. Every RV dealer in North America stocks Onan parts. Air-cooled means simpler installation (no coolant plumbing) but louder than water-cooled units. At 72 dB at 3m it's noticeably louder than the Fischer Panda (54 dB at 7m — that's roughly 4× louder perceived). 120V only — needs the MultiPlus to be in NA mode, or a step-up transformer internationally.

---

**E. Dometic TEC 29** (Petrol — included for reference)

| Parameter | Value |
|---|---|
| Continuous output | 2.6 kW |
| Voltage | 230V / 50Hz |
| Engine | Honda GX160 **petrol** (not diesel) |
| Noise | **54 dB(A) at 7m** |
| Dimensions | 480 × 385 × 290 mm |
| Weight | **44 kg** |
| Key feature | Extremely compact, under-floor mounting, lightest option |

**Verdict:** The lightest and most compact option by far at only 44 kg. However, it runs on **petrol, not diesel** — meaning you'd need to carry a separate fuel supply. For an expedition truck running diesel everywhere, this is a significant logistics downside. The 2.6 kW output is also marginal for the MultiPlus charger at full rate. Included for completeness but not recommended for a diesel expedition rig.

---

### 2.2 Comparison Matrix

| Feature | Fischer Panda 4000s Neo | Fischer Panda AGT-DC 4000 | WhisperPower Piccolo 4 | Onan QD 3200 | Dometic TEC 29 |
|---|---|---|---|---|---|
| **Output** | 3.0–3.4 kW AC | 3.2–4.0 kW DC | 3.5 kW AC | 3.2 kW AC | 2.6 kW AC |
| **Fuel** | Diesel | Diesel | Diesel | Diesel | **Petrol** |
| **Cooling** | Water | Water | Water | **Air** | Air |
| **Noise (7m)** | 54 dB(A) | 54 dB(A) | <55 dB(A) | ~62 dB(A)* | 54 dB(A) |
| **Weight** | 92 kg | 90–142 kg | **68 kg** | 93 kg | **44 kg** |
| **Dimensions (LWH mm)** | 558×460×518 | ~550×450×520 | ~500×400×480 | 767×440×457 | 480×385×290 |
| **Fuel from main tank** | Yes | Yes | Yes | Yes | **No (petrol)** |
| **International parts** | Good (marine network) | Niche | Good (marine) | **Excellent (NA)** | Good (EU) |
| **Integration with 24V bus** | Via MultiPlus charger | **Direct DC — best** | Via MultiPlus charger | Via MultiPlus charger | Via MultiPlus charger |
| **Vibration isolation** | Excellent | Excellent | Good | Good | Good |
| **Est. price** | $8,000–12,000 | $10,000–15,000 | $6,000–9,000 | **$4,000–5,000** | $3,000–4,000 |

*Onan noise estimated at 7m from the 3m spec using inverse-square law.

---

## 3. Recommendation

### Primary Recommendation: Fischer Panda 4000s Neo PMS

**Why:**

1. **Whisper-quiet at 54 dB.** You can run this at a campsite, in a national park, or at 2am in a parking lot without drawing attention. The Onan at 72 dB is roughly 4× louder to the human ear.

2. **Water-cooled = sealed compartment.** No air vents needed in the storage box — the heat exchanger rejects heat through coolant. This keeps dust, rain, and insects out of the generator compartment.

3. **Diesel from the main tank.** One fuel system for the truck, heater, and generator. No carrying petrol.

4. **Right-sized at 3.0–3.4 kW.** Covers the MultiPlus charger at full rate with a little headroom.

5. **Expedition pedigree.** Fischer Panda is the OEM generator supplier for Unicat, Action Mobil, and numerous military expedition platforms. International marine dealer network means you can get service in most port cities worldwide.

**Trade-offs:** It's the second-heaviest option at 92 kg (vs 68 kg for the WhisperPower Piccolo 4), and the most expensive at $8,000–12,000. The water-cooling system adds plumbing complexity (coolant loop, raw-water intake or air-cooled radiator for vehicle installation).

### Alternative: WhisperPower Piccolo 4

If weight is critical (24 kg lighter) and budget matters, the Piccolo 4 delivers similar performance and noise levels at lower cost. It's a legitimate choice — just less proven in the expedition vehicle world than Fischer Panda.

### Budget Alternative: Cummins Onan QD 3200

If you're starting in North America and the noise difference is acceptable, the Onan is half the price with the best parts network on the continent. Consider this if the rig will spend most of its life in NA campgrounds where generator hours are common.

---

## 4. Installation — Rear Storage Box, Driver Side

### 4.1 Space Requirements

The Fischer Panda 4000s Neo needs 558 × 460 × 518 mm plus service clearances:

| Requirement | Dimension |
|---|---|
| Generator footprint | 558 × 460 mm |
| Service clearance (one side) | +150 mm |
| Exhaust routing | +100 mm rear |
| Vibration mount clearance | +25 mm all sides |
| **Total compartment minimum** | **733 × 635 × 568 mm** |

### 4.2 Mounting

1. **Vibration isolation mounts.** Fischer Panda supplies their own isolation mount kit. The generator bolts to 4× rubber-isolated mounting studs secured to a steel plate welded or bolted to the storage box floor. This is critical — diesel generator vibration will destroy the GRP shell and cabinetry if hard-mounted.

2. **Weight reinforcement.** 92 kg concentrated in the rear storage box needs structural reinforcement of the box floor. A 3mm steel plate spanning the full compartment width distributes the load to the chassis rails.

3. **Levelling.** The generator must remain within 15° of level for oil lubrication. For an expedition vehicle traversing side slopes, this is usually fine — but confirm the storage box mounting doesn't compound the angle.

### 4.3 Exhaust

1. **Route to rear/underside.** Exhaust pipe exits through the floor or rear of the storage box, pointing down and away from the cabin air intakes.

2. **Marine-grade wet exhaust** (if water-cooled exhaust option selected) — mixes cooling water with exhaust for further noise reduction.

3. **Spark arrestor / rain cap** at the exit point.

4. **High-temperature insulation** on all exhaust routing inside the compartment (fibreglass wrap or ceramic sleeve).

### 4.4 Fuel Supply

1. **Tap from main diesel tank.** A T-fitting on the truck's fuel supply line feeds the generator through its own fuel filter and shutoff valve.

2. **Return line** back to the main tank (diesel generators return unused fuel).

3. **Anti-siphon valve** to prevent fuel draining if the generator is below the tank level.

4. **Fuel filter** — separate from the truck's filters, easily accessible for service.

### 4.5 Cooling (Water-Cooled Generator)

Two options for heat rejection:

**Option A — Keel cooler / air-cooled radiator (RECOMMENDED):**
A compact air-cooled radiator (similar to an intercooler core) mounted behind the storage box with a 12V electric fan. The generator's coolant loop circulates through this radiator. No raw water intake needed — fully self-contained.

**Option B — Raw water cooling (marine style):**
Only relevant if the rig will be parked near water. Not practical for a land vehicle. Reject this option.

### 4.6 Electrical Integration

```
[Generator AC Output] → [Shore Power Inlet Bus] → [MultiPlus-II AC Input]
                              ↑
                        [Shore Power Cord]
                        (when on shore power)
```

The generator connects to the same AC input bus as shore power, through a changeover relay or the MultiPlus-II's built-in transfer switch. The MultiPlus automatically detects AC input and begins charging.

**Auto-start option:** Wire the generator's start/stop to a Cerbo GX relay output. The Cerbo can trigger generator start when battery SOC drops below a threshold (e.g., 25%) and stop when it reaches a target (e.g., 85%). This is a standard Victron feature — no custom logic needed.

### 4.7 Ventilation

Even though the generator is water-cooled (no large air intake needed for engine cooling), the compartment still needs:

1. **Combustion air intake** — small louvred vent (100 × 200 mm) in the compartment wall or floor.
2. **Heat soak ventilation** — passive vents at top and bottom of compartment to prevent heat buildup when the generator is off in hot climates.
3. **CO detection** — mandatory carbon monoxide detector inside the habitat, near the generator compartment wall.

### 4.8 Soundproofing (Belt and Suspenders)

The Fischer Panda is already supersilenced at 54 dB. For additional stealth:

1. **Line the compartment** with 25mm closed-cell acoustic foam (mass-loaded vinyl backed) on all interior surfaces.
2. **Seal all gaps** — sound leaks through the smallest opening. Weather-strip the access door.
3. **Duct the air intake** through a baffled path to attenuate intake noise.

Target: **< 50 dB(A) at 7m** with compartment treatment. This is quieter than a typical conversation.

---

## 5. Mass Balance Impact

| Item | Weight (kg) | Position |
|---|---|---|
| Generator (Fischer Panda 4000s Neo) | 92 | Rear driver side |
| Mounting plate + isolators | 8 | Rear driver side |
| Coolant system (radiator, hoses, fluid) | 5 | Rear driver side |
| Fuel lines + filter | 2 | Rear |
| Exhaust system | 3 | Rear |
| Wiring + changeover relay | 2 | Rear to passenger side |
| Acoustic treatment | 3 | Rear driver side |
| **TOTAL** | **115 kg** | **Rear driver side** |

**Mass balance concern:** 115 kg added to the rear driver side compounds the existing rear-heavy tendency (water tank, diesel tank). However, the batteries (208 kg) are forward of the axle on the passenger side, providing significant counterbalance. The generator weight is comparable to a passenger — manageable but worth validating in the overall mass balance model.

---

## 6. Operational Scenarios

### Scenario A — Jungle / Zero Solar (Primary Use Case)

Battery at 40% after 4 days in dense canopy. Run generator for 4 hours in the morning → charges ~10 kWh → battery back to ~75%. Repeat every 3–4 days. Fuel cost: ~4L diesel = negligible.

### Scenario B — Emergency / Breakdown

Truck broken down, can't drive, no sun. Generator provides indefinite autonomy at ~1L/hr. With a 500L diesel tank, that's 500+ hours of generator runtime — months of power.

### Scenario C — Winter Heating + Charging

Run generator 2–3 hours/day to supplement solar shortfall in Northern European winter. The ThermaPro 90 heater runs on diesel anyway, so the generator just adds electrical charging capacity.

### Scenario D — Shore Power Substitute

At a campsite with no power hookups (common in Africa, South America, remote Asia). Run generator for 3–4 hours to do laundry (washer), charge batteries, and run any shore-only loads.

---

## 7. Owner Decisions Required

| # | Decision | Options | Impact |
|---|---|---|---|
| 1 | **Generator brand/model** | Fischer Panda 4000s Neo (recommended) / WhisperPower Piccolo 4 / Onan QD 3200 | Cost, weight, noise |
| 2 | **AC vs DC generator** | AC via MultiPlus (simpler) / DC direct to bus (Fischer Panda AGT-DC, more efficient) | Integration complexity |
| 3 | **Auto-start via Cerbo GX?** | Yes (hands-off) / No (manual start only) | Convenience vs. complexity |
| 4 | **Cooling method** | Air-cooled radiator (self-contained, recommended) / Auxiliary from truck cooling | Plumbing complexity |
| 5 | **Acoustic treatment level** | Standard (Fischer Panda enclosure only, 54 dB) / Enhanced (compartment treatment, <50 dB) | Cost, weight |

---

## 8. Related Files

- [DESIGN-ELEC-001-electrical-system-first-draft.md](DESIGN-ELEC-001-electrical-system-first-draft.md) — Main electrical design
- [REVIEW-ELEC-001-expedition-manufacturer-perspective.md](REVIEW-ELEC-001-expedition-manufacturer-perspective.md) — Expedition review (Finding #1)

---

*Generator sizing based on Gimli2 load table (DESIGN-ELEC-001 §3). Specifications sourced from manufacturer published data. Prices are approximate market estimates and vary by region and dealer.*
