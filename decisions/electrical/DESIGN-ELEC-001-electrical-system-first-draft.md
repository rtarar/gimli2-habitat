# Electrical System Design — First Draft

**ID:** DESIGN-ELEC-001
**Version:** 0.3 (Updated with alternator, heater, CPAP, Starlink decisions)
**Date:** 2026-02-28
**Status:** DRAFT — Pending Owner Review
**Resolves:** DECISIONS-ELEC-001 (Sections A–F) + REVIEW-ELEC-001 (Findings #1–#10)

---

## 0. Design Basis & Assumptions

**Design locale:** Southeast USA (primary); worldwide expedition (secondary).
**Autonomy target:** 10 days without shore power or engine charging.
**Cooking strategy:** Indoor electric when weather is poor; outdoor propane kitchen when weather permits. Load scenarios modelled as "Heavy" (all-electric cooking) and "Conservation" (propane cooking, minimal AC loads).
**Bus voltage:** 24 V DC (DECIDED 2026-02-28).
**Battery chemistry:** LiFePO4 (Victron NG series).
**Ecosystem:** Victron throughout for integration, international parts availability, and Cerbo GX monitoring.
**Generator backup:** Diesel generator in rear storage box, driver side (DECIDED 2026-02-28).
**Wiring standard:** ABYC E-11 marine-grade throughout (DECIDED 2026-02-28).
**Charge sources (4):** Solar array, alternator DC-DC, shore power, diesel generator.

---

## 1. Battery Bank (B3, B9 — DECIDED)

**Selection:** 4 × Victron Lithium NG 25.6V / 300Ah, connected in parallel.

| Parameter | Value |
|---|---|
| Nominal voltage | 25.6 V |
| Total capacity | 1,200 Ah |
| Total energy | 30.7 kWh |
| Usable energy (95% DoD) | 29.2 kWh |
| Max continuous discharge | 1,200 A (4 × 300A) |
| Dimensions per unit | 841 × 206 × 205 mm (L × H × D) |
| Weight per unit | 52 kg |
| Total battery weight | 208 kg |
| BMS required | Lynx Smart BMS NG 1000A |

### 1.1 Fitment Verification (Updated)

The original CONFLICT-001 resolution assumed 6 modules at 540 × 250 × 220 mm, totalling 300 kg. The new selection is 4 × NG 25.6V/300Ah — significantly different geometry but **92 kg lighter**.

**Proposed arrangement:** 2 × 2 stack (2 across depth, 2 high) in the Passenger-Side Kitchen Base, above the water tank toe-kick extension.

| Dimension | Required (with 25mm clearance) | Available | Status |
|---|---|---|---|
| Depth | 485 mm (2 × 205 + 3 × 25) | 600 mm | FITS |
| Height | 487 mm (2 × 206 + 3 × 25) | ~600 mm (above 200mm tank) | FITS |
| Length | 891 mm (841 + 2 × 25) | Along habitat axis | FITS |

**Mass balance impact:** 208 kg at Z ≈ +800 (forward of axle) continues to serve as counterweight to the rear water/structure mass. The 92 kg weight reduction vs. original assumption improves the overall mass budget.

**Action required:** Confirm the 891mm length along the habitat axis does not conflict with adjacent cabinetry or the water tank extension footprint.

---

## 2. Appliance Selections (Section A)

### A1 — Induction Cooktop (2-Burner)

**Recommended:** Camplux RIH602BF or equivalent 2-burner, 120V / 1800W shared power.

| Parameter | Value |
|---|---|
| Rated power | 1800 W (shared between burners) |
| Surge | ~2200 W (momentary at startup) |
| Voltage | 120 V AC / 15A circuit |
| Mounting | Built-in or countertop |

**Notes:** 1800W shared means both burners cannot run at full power simultaneously — one operates at reduced output. This is standard for RV 15A circuits. For heavy Indian cooking with two pots, expect to stagger burners or use mid-power settings. The outdoor propane kitchen handles overflow.

### A2 — Convection Microwave / Oven / Air Fryer Combo

**Status: OPEN — Research required.**

No final decision has been recorded on this appliance. Options to evaluate:

1. **Convection microwave only** (e.g., Sharp R1874T, ~1500W input) — proven RV choice, compact.
2. **Microwave + air fryer combo** (e.g., Toshiba ML2-EC10SA, Galanz GSWWA16BKSA10) — adds air-frying without a separate appliance.
3. **Dedicated air fryer + separate microwave** — better at each task but takes two slots/circuits.

**Placeholder for load table:** Using 1,500W input / 1,800W surge until model is selected.

| Parameter | Value (placeholder) |
|---|---|
| Input power | ~1,500 W |
| Surge | ~1,800 W |
| Voltage | 120 V AC / dedicated 15A circuit |

**Action required:** Owner to research combo units and decide. Key criteria: 120V operation, ≤1500W input, fits RV cutout dimensions, available internationally (or easy to replace).

### A3 — Roof Fans (× 2)

**Recommended:** MaxxFan Deluxe 7000K (with remote control + thermostat).

| Parameter | Value |
|---|---|
| Voltage | 12 V DC (requires 24V→12V converter) |
| Current draw | 0.2 A (low) to 2.66 A (max) per unit |
| Average draw (mid speed) | ~1.3 A per unit at 12V ≈ 16W each |
| Total for 2 units | ~32 W average |

### A4 — Washer

**Recommended:** Compact portable washer, shore-power only.

| Parameter | Value |
|---|---|
| NA market | 120V unit (Comfee or equivalent, ~300W) |
| International | 230V unit for European/Indian shore power |
| Operation | Shore-only (per REQ-ELEC-001 §7.2) |

**Strategy:** Carry one 120V unit for NA, or source a universal-voltage compact washer. The 230V outlet (Section F) on shore power handles international camping. This appliance is excluded from the battery load table.

### A5 — Fridge / Freezer (DECIDED)

**Selected:** Vitrifrigo SLIM250 CHR HP, Black.

| Parameter | Value |
|---|---|
| Total capacity | 250 L (two compartments: upper front-opening + lower drawer) |
| Voltage | 12/24 V DC and 115/230 V AC |
| Rated power | 75 W |
| Compressor | NextGen R600a (high performance, 3 kg lighter than standard) |
| Dimensions | 595 mm (W) × 651 mm (D) × 1,550 mm (H) |
| Weight | ~59 kg |
| Daily consumption (est.) | ~900–1,200 Wh/day (75W × 50–65% duty cycle) |

**Notes:** The SLIM250 is a significantly larger unit than the C115i originally considered. The 75W rated power with duty cycling in hot SE USA conditions could push daily consumption to ~1,200 Wh/day. This is a meaningful increase in the load table. The unit should run on 24V DC directly to avoid inverter losses. Confirm 24V DC operation from the SLIM250 specs.

### A6 — Separate Freezer

**Not required.** The SLIM250 has a dedicated lower freezer drawer compartment, providing ample frozen storage for expedition provisioning.

### A7 — Starlink (DECIDED)

**Selected:** Starlink Standard (flat dish, Gen 3).

| Parameter | Value |
|---|---|
| Active power | 50–75 W |
| Idle/standby | ~20 W |
| Daily consumption (16h active / 8h idle) | ~960–1,360 Wh |
| Voltage | Proprietary PoE, 48V from router brick |

**Notes:** Starlink is the single largest continuous DC load. Schedule Starlink sleep mode overnight to save ~160 Wh/night. The load table uses 960 Wh/day (16h active at 60W average).

### A8 — Router

**Recommended:** Pepwave MAX BR1 Pro 5G.

| Parameter | Value |
|---|---|
| Nominal power | 8 W |
| Max power | 19 W |
| Average | 12 W |
| Input | 12 V DC |
| Daily consumption | ~288 Wh |

### A9 — CPAP (DECIDED)

**Selected:** ResMed AirSense 10 (primary, with humidifier) + ResMed AirMini (travel/backup).

#### AirSense 10 (Primary — with Humidifier)

| Parameter | Value |
|---|---|
| Power supply | 24V DC / 90W rated |
| Typical power (with humidifier, no heated tube) | ~30–53 W |
| Peak power (with heated tube + humidifier) | ~70–104 W |
| Nightly consumption (8 hrs, humidifier on) | ~240–420 Wh |
| Input | 24V DC (native — matches bus voltage directly) |

#### AirMini (Travel / Backup)

| Parameter | Value |
|---|---|
| Typical power | ~6.3 W |
| Peak power | 27 W |
| Nightly consumption (8 hrs) | ~50–70 Wh |
| Input | 24V DC (native) |

**Notes:** Both units run natively on 24V DC, matching the bus voltage — no inverter needed. The AirSense 10 with humidifier is the heavier load (~240–420 Wh/night depending on heated tube setting). Use a direct 24V DC cable adapter for both. The AirMini uses waterless humidification (HumidX cartridge) and draws significantly less power, making it ideal for deep off-grid nights when power is scarce or as backup if the AirSense 10 develops issues.

**Load table impact:** Using AirSense 10 with humidifier at mid-range (~330 Wh/night) as the baseline. This is a meaningful increase from the original 72 Wh estimate (AirSense 11 without humidifier).

### A10 — UV Water Filter

**Recommended:** Viqua S2Q-P/12VDC.

| Parameter | Value |
|---|---|
| Power | 17 W |
| Flow rate | 3 GPM |
| Voltage | 12 V DC |
| Daily consumption | ~4 Wh (on-demand only) |

---

## 2B. Additional Systems (Electrical Load Inputs)

### Diesel Heater — Webasto ThermaPro 90 (DECIDED)

The habitat will use a Webasto ThermaPro 90 external diesel heater with heat exchanger, tapping into the engine coolant circuit. A future hydronic heating solution for the habitat interior will be integrated later.

| Parameter | Value |
|---|---|
| Heat output | Up to 9.1 kW |
| Fuel | Diesel (0.2–0.9 L/hr) |
| Electrical consumption | 37–83 W (operating range), 110 W max |
| Voltage | 24V DC (CONFIRMED) |
| Operating temp range | −40 to +80°C |

**Electrical impact:** When running, the ThermaPro 90 draws 37–83W from the DC bus. In cold-weather camping (heater running 12+ hrs/day), this adds 450–1,000 Wh/day to the load table. Added as a winter-use line item.

### Water Cabinet — Integrated Pump + Accumulator (DECIDED)

The water system will use a MotorCraft (or equivalent) integrated water cabinet solution combining the pump, accumulator, and associated plumbing components in a single pre-assembled unit.

**Electrical impact:** The integrated pump unit replaces the separate pump line items in the load table. Typical draw: 60W when running, intermittent duty cycle (~30 min/day total). ~30 Wh/day.

**Action required:** Confirm exact brand/model and power specifications for the water cabinet. The "MotorCraft" name did not return results — may be a different brand (Whale, Truma, Fiamma?). Please confirm.

---

## 3. Load Table (B1)

### 3.1 AC Loads (Through Inverter)

| Load | W (cont) | W (surge) | Heavy Wh/day | Conservation Wh/day |
|---|---|---|---|---|
| Induction cooktop | 1,800 | 2,200 | 2,935 | 0 |
| Convection microwave | 1,500 | 1,800 | 815 | 0 |
| Instapot | 1,000 | 1,200 | 815 | 0 |
| Blender/grinder | 500 | 1,200 | 54 | 0 |
| TV/monitor | 60 | 80 | 196 | 130 |
| Laptop charging ×2 | 130 | 130 | 565 | 424 |
| Phone/tablet charging | 30 | 30 | 98 | 65 |
| Heat pad | 60 | 60 | 130 | 65 |
| Vacuum | 400 | 600 | 65 | 43 |
| **AC subtotal (at battery, 92% inv eff)** | | | **5,674** | **728** |

### 3.2 DC Loads (Direct from Bus)

| Load | W (cont) | W (surge) | Heavy Wh/day | Conservation Wh/day |
|---|---|---|---|---|
| Fridge/freezer (SLIM250) | 45 | 75 | 1,080 | 1,080 |
| Starlink Standard | 60 | 100 | 960 | 480 |
| Pepwave BR1 Pro 5G | 12 | 19 | 288 | 288 |
| MaxxFan ×2 | 32 | 64 | 384 | 256 |
| Interior lighting (all) | 50 | 100 | 300 | 200 |
| Cabinet/drawer lights | 5 | 15 | 5 | 2 |
| Water pump (internal) | 60 | 120 | 30 | 18 |
| Water pump (stream intake) | 80 | 150 | 20 | 0 |
| UV water filter | 17 | 17 | 4 | 3 |
| Cameras ×4 | 12 | 16 | 288 | 288 |
| NVR | 10 | 15 | 240 | 240 |
| IR emitters ×6 | 12 | 18 | 120 | 120 |
| CPAP (AirSense 10 + humidifier) | 40 | 104 | 330 | 330 |
| Camera/drone/GoPro charging | 50 | 50 | 100 | 25 |
| Toothbrush/shaver charging | 10 | 10 | 20 | 10 |
| Lynx BMS + Cerbo GX | 15 | 20 | 360 | 360 |
| ThermaPro 90 diesel heater (24V) | 60 | 110 | 0 | 0 |
| *(ThermaPro winter use: add 720 Wh/day when heating 12 hrs)* | | | | |
| **DC subtotal** | | | **4,529** | **3,700** |

### 3.3 Daily Totals

| Scenario | AC (Wh) | DC (Wh) | Losses (Wh) | Total (Wh) | Total (kWh) |
|---|---|---|---|---|---|
| **Heavy cooking day** | 5,674 | 4,529 | 200 | **10,403** | **10.4** |
| **Conservation mode** | 728 | 3,700 | 200 | **4,628** | **4.6** |
| **Conservation + winter heating** | 728 | 4,420 | 200 | **5,348** | **5.3** |

**Note on v0.3 changes:** AirSense 10 with humidifier adds ~258 Wh/day vs original no-humidifier estimate (72 → 330 Wh/night). Starlink Standard retained. The SLIM250 fridge (1,080 Wh/day) remains the dominant baseline load at ~23% of conservation demand.

---

## 4. Daily Demand & Autonomy Analysis (B2)

### 4.1 Autonomy Without Solar

| Scenario | Daily demand | Battery autonomy (29.2 kWh usable) |
|---|---|---|
| Heavy cooking | 10.4 kWh | 2.8 days |
| Conservation (propane) | 4.6 kWh | 6.3 days |
| Conservation + winter heating | 5.3 kWh | 5.5 days |

### 4.2 Key Finding — 10-Day Target

With the SLIM250 fridge, Starlink Standard, and AirSense 10 with humidifier, the 10-day no-solar target requires active energy management. At 4.6 kWh/day conservation mode, pure battery provides 6.3 days.

**Realistic scenario analysis:**

1. **Even overcast days produce solar:** At just 1 peak sun hour (heavy cloud), the 2050W array produces ~1.7 kWh/day, reducing the net drain to ~2.9 kWh/day → **10.0 days autonomy**.
2. **Starlink scheduling:** Reducing Starlink to 8 hours/day saves ~480 Wh/day → brings conservation demand to ~4.1 kWh/day → **7.1 days** pure battery, **12+ days** with minimal solar.
3. **CPAP fallback:** Switching from AirSense 10 (330 Wh/night) to AirMini (60 Wh/night) saves ~270 Wh/night — significant savings for deep off-grid stretches.
4. **Driving days:** 4 hours of engine charging adds 3.2 kWh via DC-DC chargers, nearly offsetting a full conservation day.
5. **Fridge eco-mode:** If the SLIM250 duty cycle can be reduced (cooler ambient, less door opening), consumption could drop to ~800 Wh/day, saving ~280 Wh/day.

**Realistic assessment:** The system achieves 10+ days off-grid in scenarios with minimal solar (even heavy overcast). In true zero-input scenarios (dense forest canopy, no driving), expect 6–7 days. The AirMini provides a meaningful power-saving fallback for extended off-grid. A 5th battery (+7.7 kWh, +52 kg) would push pure-battery conservation to ~8.0 days. The 10-day absolute-zero-input target may warrant the 5th battery — owner decision.

**With generator (DECIDED):** The Fischer Panda 4000s Neo eliminates the autonomy concern entirely. A 4-hour generator run charges ~10 kWh, covering 2+ days of conservation-mode demand. With the 500L diesel tank, the generator provides 500+ hours of runtime — effectively unlimited electrical autonomy regardless of solar conditions. The 10-day target is comfortably met even in zero-solar scenarios.

**Recommendation:** Start with 4 batteries. The generator provides the safety net. A 5th battery is no longer needed for autonomy — only consider it if real-world data shows you want to reduce generator run frequency.

---

## 5. Inverter / Charger (B4, B5, F1)

**Recommended:** Victron MultiPlus-II 24/5000/120-95.

| Parameter | Value |
|---|---|
| Continuous output | 4,000 W |
| Surge output (5 sec) | 9,000 W |
| AC output | 120 V / 60 Hz |
| Built-in charger | 120 A @ 24V = 2,880 W from shore |
| AC input range | 90–140 V (handles weak shore power) |
| Dimensions | 627 × 350 × 150 mm |
| Weight | 29 kg |

### 5.1 Peak Load Headroom

| Scenario | Load (W) | Inverter capacity | Headroom |
|---|---|---|---|
| Realistic peak (cooking + TV + laptop) | 1,990 | 4,000 W | 2,010 W |
| Worst case (induction + microwave) | 3,300 | 4,000 W | 700 W |
| Absolute max (cooking + Instapot) | 3,500 | 4,000 W | 500 W |

### 5.2 Dual-Voltage / International Strategy (F1)

**Decision: Single inverter/charger, field-switchable.**

The MultiPlus-II can be reconfigured between 120V/60Hz and 230V/50Hz output via software (VictronConnect). For world travel:

1. **NA mode:** 120V/60Hz output, 120V shore input — standard configuration.
2. **International mode:** Reflash to 230V/50Hz output, 230V shore input.
3. **Shore inlet:** Install a dual-standard inlet with adaptor kit (NEMA 14-50 for NA, CEE17 blue 32A for international). The MultiPlus-II's wide input range handles both.

This avoids carrying two inverters and saves ~29 kg + significant cabinet space. The trade-off is that 120V NA appliances need a step-down transformer when running in 230V mode overseas, but this only matters for the cooktop and microwave (all other loads run on DC).

**Alternative (if dual simultaneous output needed):** Add a Victron Autotransformer for split-phase or step-down functionality.

### 5.3 Washer Circuit (F2)

The washer runs shore-only. Provide a dedicated 230V/16A outlet wired directly from the shore input bus, bypassing the inverter. An interlock relay ensures this outlet is only live when shore power is connected. For NA, use the MultiPlus's AC-2 output (unswitched pass-through).

### 5.4 Additional 230V Outlet (F3)

One additional 230V general outlet in the utility zone, also on the shore-only bus. Useful for hair dryers, power tools, or other occasional high-draw appliances at campsites.

---

## 6. Solar Array (B6)

### 6.1 Panel Selection

**Recommended:** 5 × 410W monocrystalline panels (generic high-quality, e.g., Trina, JA Solar, or similar).

| Parameter | Value |
|---|---|
| Panel dimensions | 1,722 × 1,134 × 30 mm |
| Weight per panel | 21.5 kg |
| Total array | 2,050 W |
| Total weight | 107.5 kg |

### 6.2 Roof Layout

Roof area: 4,750 × 2,280 mm (10.8 m²).

**Layout:** 4 panels in 2×2 portrait grid (occupying 3,444 × 2,268 mm at the forward section), plus 1 panel in landscape orientation (1,134 × 1,722 mm) offset. Remaining roof area (~1,300 × 2,280 mm at the rear) accommodates 2× MaxxFan roof vents, Starlink dish mount, and the consolidated cable penetration.

### 6.3 Solar Production by Location

| Location | Peak Sun Hours | Net Production (kWh/day) |
|---|---|---|
| SE USA (summer) | 5.5 | 9.2 |
| SE USA (winter) | 3.5 | 5.9 |
| SE USA (annual avg) | 4.5 | 7.6 |
| Northern Europe (summer) | 4.0 | 6.7 |
| Northern Europe (winter) | 1.5 | 2.5 |
| India (annual avg) | 5.0 | 8.4 |
| Overcast / cloudy | 1.0 | 1.7 |

(Net = gross × 0.82 system efficiency factor for MPPT efficiency, cable losses, temperature derating, and dust/soiling.)

### 6.4 Net Energy Balance (Updated for SLIM250 Fridge)

| Scenario | Demand | Solar | Net drain | Battery days |
|---|---|---|---|---|
| Heavy cooking, SE USA avg | 10.4 kWh | 7.6 kWh | +2.8 kWh | 10.4 days |
| Heavy cooking, no sun | 10.4 kWh | 0 | +10.4 kWh | 2.8 days |
| Conservation, SE USA avg | 4.6 kWh | 7.6 kWh | −3.0 kWh | ∞ (net charge) |
| Conservation, no sun | 4.6 kWh | 0 | +4.6 kWh | 6.3 days |
| Conservation, cloudy (1 PSH) | 4.6 kWh | 1.7 kWh | +2.9 kWh | 10.0 days |
| Conservation + winter heat, SE USA | 5.3 kWh | 7.6 kWh | −2.3 kWh | ∞ (net charge) |

**Conclusion:** In SE USA with average sun, the solar array fully covers all scenarios including winter heating. The system is solar-positive for conservation and near break-even for heavy cooking. The CPAP with humidifier adds ~258 Wh/night vs the original estimate; the AirMini backup provides a meaningful off-grid power-saving fallback. The SLIM250 fridge remains the dominant baseline load.

### 6.5 MPPT Controller

**Recommended:** Victron SmartSolar MPPT 250/100 VE.Can.

| Parameter | Value |
|---|---|
| Max PV power (at 24V) | 2,900 W (headroom for 2,050W array) |
| Max charge current | 100 A |
| Max PV Voc | 250 V |
| String config | 5S1P (cold Voc ~209V, within limit) or 2S2P + 1 |

**Preferred string configuration:** 5 panels in series (5S1P). This keeps the array current low (~13A) reducing cable losses, and the cold-weather Voc (~209V at −10°C) stays safely within the 250V controller limit. Higher voltage also improves MPPT efficiency at low light levels.

---

## 7. Alternator Charging (B10) — DECIDED

**Selected:** 2 × Victron Orion-Tr Smart 24/24-17A (isolated), wired in parallel.

| Parameter | Value |
|---|---|
| Truck alternator | 24V / 110A (CONFIRMED) |
| Per unit | 17A continuous / 400W |
| Combined output | 34A / 800W |
| Daily charge (4 hrs driving) | 3.2 kWh |

**Notes:** The truck alternator is confirmed as 24V / 110A. The 34A combined draw from the two Orion-Tr units represents ~31% of the alternator's rated capacity — well within safe continuous loading (typically 70–80% of rated output). The Orion-Tr Smart has engine-detection logic, adaptive 3-stage charging, and Bluetooth monitoring. Two units in parallel provide redundancy — if one fails, the other continues charging at 400W.

For trucks with smart alternators or Euro 6 emissions alternators, the Orion-Tr's current-limiting protects the alternator.

---

## 7B. Diesel Generator — DECIDED

**Selected:** Fischer Panda 4000s Neo PMS (AC output version).

| Parameter | Value |
|---|---|
| Continuous output | 3.0 kW (3.6 kVA) |
| Max output | 3.4 kW (4.0 kVA) |
| Voltage | 230V / 50Hz (also configurable for 120V / 60Hz) |
| Engine | Fischer Panda single-cylinder diesel, water-cooled |
| Cooling | Double-circuit freshwater heat exchanger + air-cooled radiator |
| Noise | 54 dB(A) at 7m (whisper-quiet, conversational volume) |
| Dimensions | 558 × 460 × 518 mm (L × W × H) |
| Weight (dry) | 92 kg |
| Fuel consumption | 0.6–1.2 L/hr |
| Fuel source | Tapped from main truck diesel tank |

**Location:** Rear storage box, driver side, behind rear storage. Compartment minimum: 733 × 635 × 568 mm (including service clearances and vibration mount gaps).

**Integration:** Generator AC output connects to the shore power input bus via a changeover relay. The MultiPlus-II auto-detects AC input and begins charging at up to 2,880W (120A @ 24V). Auto-start via Cerbo GX relay: triggers at 25% SOC, stops at 85% SOC.

**Installation details:** Vibration-isolated mounts (Fischer Panda OEM kit), 3mm steel reinforcement plate on box floor, marine-grade wet exhaust routed to rear/underside, fuel tap with anti-siphon valve and dedicated filter, air-cooled radiator with 12V fan for heat rejection. Compartment lined with 25mm closed-cell acoustic foam (mass-loaded vinyl backed). CO detector mandatory inside habitat.

**Charge time from generator:**

| Battery state | Time to 90% SOC |
|---|---|
| From 20% (emergency) | ~8.5 hours |
| From 50% (typical top-up) | ~4.7 hours |
| From 70% (light top-up) | ~2.4 hours |

**Why Fischer Panda:** OEM supplier for Unicat, Action Mobil, and military expedition platforms. International marine dealer network covers most port cities worldwide. Water-cooled design allows sealed compartment (no air vents for engine cooling). 54 dB at 7m is roughly 4× quieter perceived than the Onan QD 3200 alternative (72 dB at 3m).

See [DESIGN-ELEC-002-generator-selection.md](DESIGN-ELEC-002-generator-selection.md) for full comparison of evaluated models and detailed installation specifications.

---

## 8. DC Distribution (B8)

### 8.1 Bus Architecture

```
[Battery Bank 24V] → [Lynx Smart BMS NG 1000A] → [Lynx Distributor]
                                                         │
                    ┌────────────────────────────────────┤
                    │            │            │           │
              [MultiPlus-II] [MPPT 250/100] [DC-DC ×2] [DC Bus]
              (Inverter/Chgr) (Solar)       (Alternator)   │
                    │                                      │
    ┌───────────────┤                            ┌────────┤────────┐
    │               │                            │        │        │
[AC Input Bus] [AC Panel]                  [24V Loads] [24→12V ×2] [24→48V]
    │     │                                            Converters  (Starlink)
    │     │                                               │
[Shore] [Fischer Panda]                              [12V Loads]
 Power   Generator                            (Split: critical / non-critical)
         (Auto-start via Cerbo)
```

### 8.2 24V Direct Loads

Loads that can run directly on the 24V bus (or have 24V versions available): CPAP (AirSense 10 + AirMini, both native 24V), Cerbo GX, Lynx BMS, ThermaPro 90 heater (24V confirmed), some LED drivers.

### 8.3 12V Loads (via 24V→12V DC-DC Converter)

Most RV appliances run on 12V: fridge, fans, water pump, cameras, NVR, lighting, UV filter, router. Dual Victron Orion 24/12-25 (300W each) non-isolated converters provide the 12V rail with redundancy (see §13.5 and Finding #7).

| 12V Load | Draw (A at 12V) |
|---|---|
| Fridge (SLIM250) | 3.75 avg, 6.25 surge |
| MaxxFan ×2 | 2.6 avg, 5.3 max |
| Water pump | 5 avg, 10 surge |
| Lighting | 4.2 avg |
| Cameras + NVR | 1.8 |
| IR emitters | 1.0 |
| UV filter | 1.4 (intermittent) |
| Router | 1.0 |
| Misc charging | 3.0 |
| ThermaPro 90 heater | 2.5 avg, 4.6 max |
| **Total 12V** | **~24 A avg, ~38 A peak** |

**Dual converter configuration (redundancy — per REVIEW-ELEC-001 Finding #7):**

| Converter | Loads | Rating |
|---|---|---|
| **Converter A (Critical)** — Orion 24/12-25 | Fridge, water pump, interior lighting, BMS/Cerbo | 25A / 300W |
| **Converter B (Non-critical)** — Orion 24/12-25 | Fans, cameras, NVR, IR emitters, charging, heater | 25A / 300W |

If one converter fails, critical loads (fridge, pump, lights) continue on the surviving unit. Non-critical loads can be manually reconnected via a crossover switch.

### 8.4 Starlink Power (DECIDED)

Starlink Standard uses a proprietary 48V PoE feed from its router/power brick. The power brick runs on 100–240V AC. Feed from the MultiPlus-II AC output (simplest approach). A 24V→48V PoE injector could improve efficiency by avoiding inverter losses — consider as a future optimisation if Starlink power draw becomes a concern.

### 8.5 DC Fuse / Breaker Sizing

All DC circuits protected via Mega fuses (high current) or standard blade fuses (branch circuits), housed in a Lynx Distributor or Victron fuse block.

| Circuit | Fuse (A) | Wire gauge |
|---|---|---|
| Battery → BMS | 300A class-T | 4/0 AWG (short run) |
| BMS → Lynx Distributor | 300A MEGA | 4/0 AWG |
| Distributor → MultiPlus-II | 250A MEGA | 2/0 AWG |
| Distributor → MPPT | 100A MEGA | 4 AWG |
| Distributor → DC-DC (alt) | 40A | 8 AWG |
| Distributor → 12V converter | 30A | 10 AWG |
| 12V branch circuits | 5–15A blade fuses | 14–10 AWG |

---

## 9. AC Distribution (B7)

### 9.1 Branch Circuit Plan

| Circuit # | Load | Breaker | Wire | Notes |
|---|---|---|---|---|
| AC-1 | Induction cooktop | 20A / 120V | 12 AWG | Dedicated |
| AC-2 | Convection microwave | 15A / 120V | 14 AWG | Dedicated |
| AC-3 | Kitchen duplex (Instapot, blender) | 15A / 120V | 14 AWG | GFCI protected |
| AC-4 | Sitting area outlets (L + R) | 15A / 120V | 14 AWG | GFCI protected |
| AC-5 | Electronics charging drawer | 15A / 120V | 14 AWG | |
| AC-6 | Medicine cabinet + vacuum + misc | 15A / 120V | 14 AWG | |
| AC-7 | Exterior outlets (3 locations) | 20A / 120V | 12 AWG | GFCI + weatherproof |
| AC-8 | Starlink power brick | 15A / 120V | 14 AWG | Always-on (inverter output) |
| SHORE-1 | Washer (230V) | 16A / 230V | 2.5mm² | Shore-only, interlocked |
| SHORE-2 | General 230V outlet | 16A / 230V | 2.5mm² | Shore-only |

### 9.2 GFCI / AFCI Zones

All circuits serving countertop outlets, bathroom, and exterior locations are GFCI protected (per NEC for NA; equivalent RCD for international). AFCI on bedroom/sleeping area circuits if required by local code.

### 9.3 AC Panel Location

Compact RV breaker panel located adjacent to the MultiPlus-II in the Passenger Kitchen Base electrical compartment. Accessible for maintenance but not visible in the living space.

---

## 10. Switching & Control Architecture (Section C)

### C1 — Ambient Lighting Controller

**Recommended:** Victron Cerbo GX + Bluetooth LED controllers (e.g., Shelly RGBW2 or equivalent 12V RGBW LED dimmer).

The Cerbo GX provides the central hub. Individual zone LED controllers communicate via Bluetooth or Modbus for integration. Each zone has its own RGBW controller for independent dimming and colour selection (warm white / red / blue stealth modes).

**Zones:**
1. Entry + Bathroom — 1× controller
2. Kitchen + Hall — 1× controller
3. Sleeping + Sitting — 1× controller (or split into 2 for bed/sitting independence)

### C2 — Cabinet / Drawer Lighting

**Method:** Magnetic reed switches (door-triggered). Simple, reliable, no digital controller needed. Each cabinet/drawer has a surface-mount reed switch wired to a local LED strip. Power from the 12V rail via the nearest lighting zone.

### C3 — Master Ambient Switch Wiring

**Method:** Smart switch bus via Shelly or equivalent WiFi/Bluetooth relay modules at each of the 3 master switch locations (cab pass-through, main entry, bed area). Each switch sends a "scene" command to all zone controllers simultaneously.

Physical fallback: A latching relay in each zone allows the master switch to work even if the smart bus is down. Belt-and-suspenders reliability for an expedition rig.

### C4 — Bluetooth / App Control

**Platform:** VictronConnect + Cerbo GX with VRM portal. The Cerbo GX already provides app-based monitoring of all Victron equipment (battery, inverter, solar, charger). Lighting control via the smart switch modules can be accessed through a dedicated lighting app (e.g., Shelly app) or integrated via Node-RED on the Cerbo.

No KNX or complex home automation. Keep it simple and debuggable on the road.

### C5 — Bed Day/Night Mode

**Method:** Manual rocker switch at the bed position. Toggles between day-mode (under-bed ambient for sitting area) and night-mode (ceiling low-level ambient + bed reading lights active). A bed-position sensor is a nice-to-have but adds complexity and a failure point. Manual switch is more reliable for expedition use.

---

## 11. Placement & Layout (Section D)

### D1 — Kitchen Duplex Outlet

Position on the backsplash wall between the cooktop and sink, centred at countertop height (~1050mm from floor). Accessible for Instapot and blender use without cord draping over the cooktop.

### D2 — Sitting Area Outlets

One duplex each side, positioned at armrest height (~600mm from floor) on the side walls. Primary charge stations for laptops, phones, and tablets.

### D3 — Medicine Cabinet Charging

4 × USB-C outlets (PD capable) inside the medicine cabinet. USB-C handles toothbrushes, shavers, and modern chargers. No USB-A needed — all modern devices are USB-C or have USB-C cables.

### D4 — Vacuum Charging Outlet

Standard 120V outlet inside the pantry or tall storage cabinet near the entry. The vacuum lives in this cabinet, always docked and charging.

### D5 — Electronics Charging Drawer

Dedicated drawer in the cabinetry adjacent to the sitting area, fitted with a 4-outlet power strip inside. Passive ventilation via slots in the drawer rear panel (warm air rises out). Houses camera chargers, drone batteries, GoPros.

### D6 — Exterior Outlets (3 locations)

| Position | Type | Notes |
|---|---|---|
| Outdoor kitchen box (passenger) | 120V / 20A GFCI, weatherproof | Feeds outdoor blender, induction |
| Passenger rear | 120V / 20A GFCI, weatherproof | Near rear storage |
| Driver rear | 120V / 20A GFCI, weatherproof | Near tool/grill access |

All exterior outlets on a dedicated circuit (AC-7) with in-use weatherproof covers (bubble type).

### D7 — Shore Power Inlet

**Side:** Passenger side (same side as electrical compartment — shortest cable run to MultiPlus-II).
**Connector:** Combination inlet box with NEMA 14-50 (NA, 50A) and CEE17 blue (international, 32A). Adaptor cables for smaller connections (30A TT-30, standard 15A).

### D8 — Roof Penetration & Conduit

Single consolidated roof penetration near the rear of the solar array zone. Uses a marine-grade deck gland or Renogy entry plate for multiple cable pass-throughs (solar, Starlink). Conduit routes internally along the ceiling channel to the battery/electrical zone in the kitchen base.

---

## 12. Exterior Lighting (Section E)

### E1/E2 — Rock Lights

**Recommended:** 6 × RGBW LED rock lights (e.g., Sunpie or Xprite RGBW).

| Position | Count |
|---|---|
| Front (L + R) | 2 |
| Mid (L + R) | 2 |
| Rear (L + R) | 2 |

Built-in blue mode via RGBW controller. Single Bluetooth RGBW controller for all 6 lights, mounted in the DC distribution area. Manual on/off via a dedicated rocker switch + app control for colour selection.

### E3 — Front Security Floods

**Recommended:** 4 × round LED flood lamps (retro-style, per REQ-ELEC-001). Each 20–30W, warm white. Mounted on the front face of the habitat shell, 2 per side of centre.

### E4 — Side Floods

2 × high-mount LED floods (1 per side), mounted on the upper habitat GRP wall using non-penetrating adhesive mounts or bracket-to-extrusion clamps. Each 30–50W.

### E5 — Rear Flood

1 × LED flood bar mounted on the rear wall or box lid hinge support. 40–60W, covers rear perimeter.

### E6 — IR Emitters

6 × 850nm IR LED emitters positioned to cover the camera FOVs at each perimeter position. Each ~2W. Wired into the security circuit (always powered when security mode is active).

### E7 — Awning Light

Hardwired 12V connection point at the awning mounting rail. A waterproof 2-pin plug allows the awning light (user's choice of LED strip or fixture) to connect without permanent installation.

### Exterior Lighting Control

All exterior lights controlled via a dedicated rocker switch panel near the main entry door:

| Switch | Lights |
|---|---|
| Rock lights | All 6 (RGBW controller) |
| Security floods | All front, side, rear floods |
| IR night vision | All IR emitters |
| Awning | Awning light |

A "full perimeter" master button activates floods + IR simultaneously.

---

## 13. Expedition Hardening (per REVIEW-ELEC-001)

The following measures are adopted from the expedition manufacturer review to bring this design to production-grade standards.

### 13.1 Wiring Construction Standard — ABYC E-11 Marine Grade (Finding #3)

All electrical wiring in the habitat adopts the ABYC E-11 marine electrical standard:

| Requirement | Specification |
|---|---|
| Wire type | Tinned copper, marine-grade stranded, XLPE or TXL insulation rated 105°C minimum |
| Terminations | Adhesive-lined heat-shrink crimp terminals only. No bare crimps, no twist-and-tape. |
| Connectors | Deutsch DT/DTP series (IP67, vibration-rated) for all multi-pin connections. No Molex or spade terminals in vibration-exposed locations. |
| Loom construction | Adel clamps (cushioned P-clips) at max 300mm intervals. No cable ties as primary restraint. Split corrugated conduit or woven loom tape for protection. |
| Labelling | Every wire labelled at both ends with permanent heat-shrink labels (Brady or equivalent). |

### 13.2 Galvanic Isolator (Finding #4)

**Added:** Victron VDI-32 Galvanic Isolator installed in series with the shore power ground conductor at the inlet. Blocks low-voltage DC galvanic currents between chassis and international shore power grounds while passing AC fault currents for safety. Weight: 0.5 kg, cost: ~$100.

### 13.3 Battery Thermal Management (Finding #5)

The Victron NG LFP batteries cannot charge below 5°C (BMS lockout). The following measures ensure cold-climate operation:

| Measure | Detail |
|---|---|
| Insulated compartment | 25mm closed-cell foam on all six sides of the battery bay |
| Heating pads | 4× self-regulating 24V heating pads (one per battery), ~20W each = 80W total when active |
| BMS integration | Lynx Smart BMS NG has a dedicated heating relay output — pads activate automatically based on battery temperature sensor |
| Passive warming | Diesel heater coolant loop routed near (not through) battery compartment for ambient warming |

### 13.4 Surge Protection (Finding #6)

| Location | Device | Purpose |
|---|---|---|
| Solar input (before MPPT) | Type 2 SPD (e.g., Victron SPD Kit) | Lightning-induced surges from rooftop array |
| Shore power input | Type 2 SPD on AC input | Voltage spikes from international shore power |
| DC bus (after distributor) | DC SPD | Transient protection for sensitive electronics |

Total cost: ~$200–400. Weight: negligible (~1 kg total).

### 13.5 Inverter Redundancy (Finding #2)

**Decision:** Carry a pre-wired spare MultiPlus-II 24/5000 in storage. The spare has a pre-made cable harness (battery leads, AC output leads) with labelled connectors for rapid field swap. Estimated swap time: 30–45 minutes with basic tools. Weight: 29 kg (stored). Cost: ~$2,500.

### 13.6 Solar Panel Mounting (Finding #8)

| Requirement | Specification |
|---|---|
| Mount type | Z-bracket or L-bracket with rubber isolation pads (vibration dampening) |
| Attachment | Through-bolted to roof rails or structural aluminium extrusion. No adhesive-only mounting. |
| Air gap | 25–50mm between panel and roof for cooling (panel efficiency drops ~0.4%/°C above 25°C) |
| Edge protection | Sacrificial aluminium angle around panel perimeter to absorb branch impacts |
| Rating | Must survive continuous corrugated road vibration and 130+ km/h wind loads |

### 13.7 Load Shedding / Critical Load Priority (Finding #9)

The Cerbo GX controls programmable relay outputs to disconnect load groups based on battery SOC:

| SOC Threshold | Action |
|---|---|
| < 40% | **Warning** — Cerbo GX alert to VRM app + audible buzzer |
| < 30% | **Shed Tier 1** — Disconnect non-essential AC loads (TV, charging drawer, vacuum) via relay |
| < 20% | **Shed Tier 2** — Disconnect Starlink, exterior lighting, non-critical 12V converter |
| < 15% | **Shed Tier 3** — Only critical loads remain: fridge, water pump, interior emergency lighting, cameras, BMS |
| < 10% | **Generator auto-start** (if enabled) — Fischer Panda starts automatically |
| < 5% | **BMS disconnect** — Lynx Smart BMS disconnects all loads to protect batteries |

**Emergency lighting:** A dedicated 12V LED strip in the entry and bathroom wired on the last-disconnect circuit. Always on until the BMS physically opens the contactor.

### 13.8 Shore Power Cable Storage (Finding #10)

Dedicated exterior storage compartment (or section of the rear garage bay) for shore power cables and adaptors. Cable inventory for world travel:

| Cable / Adaptor | Region |
|---|---|
| NEMA 14-50 (50A) shore cord | North America |
| NEMA TT-30 (30A) adaptor | NA campgrounds |
| CEE17 blue 32A cord | Europe |
| CEE17 blue 16A adaptor | EU campgrounds |
| Indian 3-pin adaptor | India / South Asia |
| AU/NZ adaptor | Australia / New Zealand |
| South African 3-pin adaptor | Southern Africa |
| 25m extension cord | Universal |

All cables labelled with country/standard. Hook-and-coil storage to prevent tangles.

---

## 14. System Weight Budget

| Component | Weight (kg) | Location |
|---|---|---|
| **Core Electrical** | | |
| Batteries (4× NG 25.6V/300Ah) | 208.0 | Passenger kitchen base |
| Lynx Smart BMS NG 1000A | 5.0 | Adjacent to batteries |
| MultiPlus-II 24/5000 (active) | 29.0 | Passenger kitchen base |
| MultiPlus-II 24/5000 (spare) | 29.0 | Stored (garage/under bench) |
| SmartSolar MPPT 250/100 | 4.5 | Passenger kitchen base |
| Orion-Tr Smart DC-DC ×2 (alternator) | 3.4 | Passenger kitchen base |
| Orion 24/12-25 ×2 (12V converters) | 2.0 | DC distribution area |
| Cerbo GX + GX Touch 50 | 1.5 | Accessible panel |
| **Solar** | | |
| Solar panels (5× 410W) | 107.5 | Roof |
| Solar mounting (Z-brackets, edge guards) | 5.0 | Roof |
| **Generator** | | |
| Fischer Panda 4000s Neo PMS | 92.0 | Rear storage box, driver side |
| Generator mounting (plate, isolators) | 8.0 | Rear storage box |
| Generator cooling (radiator, hoses, fluid) | 5.0 | Rear storage box |
| Generator exhaust system | 3.0 | Rear underside |
| Generator fuel lines + filter | 2.0 | Rear to main tank |
| Generator wiring + changeover relay | 2.0 | Rear to passenger side |
| Generator compartment acoustic treatment | 3.0 | Rear storage box |
| **Expedition Hardening** | | |
| Galvanic isolator (VDI-32) | 0.5 | Shore inlet |
| Battery heating pads (×4) + insulation | 2.0 | Battery compartment |
| Surge protection (SPDs ×3) | 1.0 | Solar/shore/DC bus |
| **Distribution & Wiring** | | |
| Cabling (marine-grade tinned copper) | 28.0 | Throughout |
| DC distribution (Lynx Distributor, busbars, fuses) | 8.0 | Passenger kitchen base |
| AC distribution (breakers, panel) | 5.0 | Passenger kitchen base |
| Misc (Deutsch connectors, Adel clamps, conduit) | 12.0 | Throughout |
| **TOTAL** | **~566** | |

**Weight breakdown by zone:**

| Zone | Weight (kg) |
|---|---|
| Passenger kitchen base (batteries + electronics) | ~293 |
| Roof (solar) | ~113 |
| Rear driver side (generator) | ~115 |
| Distributed (cabling, distribution) | ~45 |

---

## 15. Full Bill of Materials

### Victron Components

| Item | Model | Qty | Role |
|---|---|---|---|
| Battery | Victron Lithium NG 25.6V/300Ah | 4 | Energy storage |
| BMS | Lynx Smart BMS NG 1000A | 1 | Battery management |
| Inverter/Charger (active) | MultiPlus-II 24/5000/120-95 | 1 | AC power + shore charging |
| Inverter/Charger (spare) | MultiPlus-II 24/5000/120-95 | 1 | Pre-wired field-swap spare |
| Solar MPPT | SmartSolar MPPT 250/100 VE.Can | 1 | Solar charge control |
| DC-DC Charger (alternator) | Orion-Tr Smart 24/24-17A (isolated) | 2 | Alternator charging |
| 24→12V Converter (critical loads) | Orion 24/12-25 (non-isolated) | 1 | Fridge, pump, lights |
| 24→12V Converter (non-critical loads) | Orion 24/12-25 (non-isolated) | 1 | Fans, cameras, charging |
| DC Distribution | Lynx Distributor | 1 | Main DC bus |
| System Monitor | Cerbo GX + GX Touch 50 | 1 | Central monitoring + app + auto-start |
| Galvanic Isolator | VDI-32 | 1 | Shore power ground protection |
| Solar Panel | 410W Monocrystalline (Trina/JA Solar) | 5 | Solar generation |

### Non-Victron Components

| Item | Model | Qty | Role |
|---|---|---|---|
| Generator | Fischer Panda 4000s Neo PMS | 1 | Backup charging (3.0–3.4 kW diesel) |
| Surge protector (solar) | Type 2 SPD (Phoenix Contact or equiv.) | 1 | Lightning/surge on PV input |
| Surge protector (shore) | Type 2 SPD | 1 | Shore power transient protection |
| Surge protector (DC bus) | DC SPD | 1 | Battery bus transient protection |
| Battery heating pads | 24V self-regulating, 20W each | 4 | Cold-climate charge enable |
| CO detector | Marine-rated CO alarm | 1 | Generator compartment safety |

---

## 16. Decisions Made This Session (2026-02-28)

| # | Decision | Resolution |
|---|---|---|
| B3 | Battery bank size | 4 × Victron NG 25.6V/300Ah = 1,200 Ah / 30.7 kWh |
| B9 | Bus voltage | 24 V DC |
| B10 | Truck alternator | 24V / 110A confirmed — Orion-Tr Smart 24/24-17A ×2 validated |
| — | Generator | Fischer Panda 4000s Neo PMS, rear storage box driver side |
| — | Wiring standard | ABYC E-11 marine-grade throughout |
| — | Galvanic isolator | Victron VDI-32 on shore power ground |
| — | Battery thermal | Heating pads + insulated compartment |
| — | Surge protection | SPDs on solar, shore, DC bus |
| — | Inverter redundancy | Carry pre-wired spare MultiPlus-II |
| — | 12V converter redundancy | Dual Orion 24/12-25 (critical/non-critical split) |
| — | Load shedding | Cerbo GX relay groups with SOC thresholds |
| — | Solar mounting | Vibration-rated Z-bracket with edge guards |
| — | ThermaPro 90 voltage | 24V version confirmed |
| A7 | Starlink | Starlink Standard (flat dish Gen 3, 50–75W, 48V PoE) |
| A9 | CPAP | AirSense 10 with humidifier (primary) + AirMini (travel/backup) |

## 17. Remaining Open Items

*Items resolved in v0.3: ~~#2 Alternator voltage~~ (24V/110A confirmed), ~~#5 ThermaPro 90 voltage~~ (24V confirmed), ~~#7 CPAP~~ (AirSense 10 + humidifier + AirMini), ~~#9 Starlink model~~ (Standard selected).*

| # | Item | Impact | Urgency |
|---|---|---|---|
| 1 | Confirm 891mm battery length fits kitchen base layout along habitat axis | Fitment | HIGH |
| 2 | **Research convection microwave / air fryer combo** — no decision recorded yet | Appliance selection (A2) | HIGH |
| 3 | **Confirm water cabinet brand/model** — "MotorCraft" not found; clarify exact product | Plumbing/electrical interface | MEDIUM |
| 4 | Verify SLIM250 actual daily consumption (75W rated; duty cycle TBD) | Load table accuracy | MEDIUM |
| 5 | Select specific exterior light fixtures | Mounting details | LOW |
| 6 | Confirm washer voltage strategy (single 120V unit or dual) | Shore circuit | LOW |
| 7 | Review smart switch platform preference (Shelly, ESP32, other) | Controls | MEDIUM |
| 8 | Define hydronic heating distribution plan for habitat interior (future, ties to ThermoPro 90) | HVAC design | LOW (future phase) |
| 9 | Confirm Fischer Panda cooling method: standalone radiator vs auxiliary truck cooling | Generator install | MEDIUM |
| 10 | Decide generator auto-start via Cerbo (yes/no) | Convenience vs complexity | LOW |

---

## 18. Related Files

- [REQ-ELEC-001-electrical-requirements.md](REQ-ELEC-001-electrical-requirements.md) — Full requirements
- [DECISIONS-ELEC-001-open-decisions.md](DECISIONS-ELEC-001-open-decisions.md) — Decision tracker
- [DESIGN-ELEC-002-generator-selection.md](DESIGN-ELEC-002-generator-selection.md) — Generator selection + installation details
- [REVIEW-ELEC-001-expedition-manufacturer-perspective.md](REVIEW-ELEC-001-expedition-manufacturer-perspective.md) — Expedition review (Unicat/Bliss Mobil/EarthRoamer perspective)
- [PLAN-electrical-layout.md](PLAN-electrical-layout.md) — Battery + inverter placement
- [CONFLICT-001-battery-fitment.md](../conflicts/CONFLICT-001-battery-fitment.md) — Battery fitment resolution
- [CONFLICT-002-water-tank-fitment.md](../conflicts/CONFLICT-002-water-tank-fitment.md) — Water tank resolution

---

*v0.1 generated 2026-02-28. v0.2 updated same day with generator decision (Fischer Panda 4000s Neo), expedition hardening measures (ABYC E-11 wiring, galvanic isolation, battery thermal, surge protection, inverter/converter redundancy, load shedding, solar mounting). v0.3 updated same day with: truck alternator confirmed 24V/110A, ThermoPro 90 confirmed 24V, CPAP decided (AirSense 10 + humidifier primary + AirMini travel/backup), Starlink Standard selected. Load table and autonomy recalculated (CPAP humidifier adds ~258 Wh/night). Open items reduced from 14 to 10. All calculations verified programmatically. Wiring gauges and fuse sizes are preliminary — final validation required during detailed electrical engineering.*
