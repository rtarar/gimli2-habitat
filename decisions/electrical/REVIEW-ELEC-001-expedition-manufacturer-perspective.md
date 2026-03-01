# Expedition Manufacturer Review — Electrical System Design

**ID:** REVIEW-ELEC-001
**Date:** 2026-02-28
**Reviewing:** DESIGN-ELEC-001 v0.1
**Perspective:** As if reviewed by engineering teams at Unicat, Bliss Mobil, or EarthRoamer
**Status:** REVIEW — For owner consideration

---

## Executive Summary

The Gimli2 electrical design is a solid first draft with well-reasoned component selection and honest load analysis. The Victron ecosystem choice, 24V bus, and 2050W solar array are consistent with current expedition vehicle best practices. However, the design has gaps that a production expedition builder would address before signing off — primarily around **redundancy, wiring standards, thermal management, and generator backup**. None are dealbreakers; all are solvable.

**Overall rating: 7/10 for a first draft** — with the items below addressed, this moves to production-ready.

---

## 1. How Gimli2 Compares to Industry Benchmarks

| Parameter | Gimli2 | Unicat MD56c | Bliss Mobil 15ft | EarthRoamer LTx | Assessment |
|---|---|---|---|---|---|
| Battery capacity | 30.7 kWh | 24.6 kWh | 10–20 kWh | 18 kWh | **ABOVE AVERAGE** — generous bank |
| Solar array | 2,050 W | 1,850 W | 860–1,000 W | 1,480 W | **ABOVE AVERAGE** — excellent for the roof size |
| Inverter | 4,000 W cont. | Dual inverters | Victron | 9,000 W (LTx) | **ADEQUATE** — see note on redundancy |
| Bus voltage | 24 V | 24 V | 24 V | 24 V | **MATCHES INDUSTRY STANDARD** |
| Autonomy (no solar) | 6.6 days (conservation) | ~14 days (claimed) | ~7 days | ~5–7 days | **COMPETITIVE** — but see note |
| Generator | None | Yes (diesel) | Optional | Auto-start engine | **GAP — see Finding #1** |
| Total electrical weight | 407 kg | N/A | N/A | N/A | Reasonable for the capacity |

---

## 2. Critical Findings

### FINDING #1 — No Generator or Engine Auto-Start (CRITICAL GAP)

**The issue:** Every major expedition builder includes either a dedicated diesel generator (Unicat, Bliss Mobil) or an auto-start engine charging system (EarthRoamer). The Gimli2 design relies entirely on solar + alternator DC-DC + shore power. In a 10-day zero-solar scenario (jungle canopy, sustained overcast, mechanical breakdown preventing driving), the system runs dry at ~6.6 days.

**Why this matters for world travel:** In equatorial rainforest, dense jungle, or northern European winter, you may face extended periods with near-zero solar and no access to shore power. The alternator charges at 800W — but only when driving. If the truck is parked for repairs, you have no backup charge source.

**Mitigations (choose one or combine):**

| Option | Weight | Cost | Complexity | Recommendation |
|---|---|---|---|---|
| **A. Portable diesel generator** (e.g., Honda EU2200i or Dometic T4500) | 21–45 kg | $1,000–4,000 | Low — external, fuel from main tank | RECOMMENDED for world travel |
| **B. Engine auto-start system** (EarthRoamer approach) | ~5 kg (relay + controller) | $500 | Medium — auto-starts truck engine when SOC drops below threshold, charges via DC-DC | Elegant but adds engine hours |
| **C. 5th battery** (+7.7 kWh, extends to ~8.4 days) | 52 kg | ~$3,500 | None | Buys time but doesn't solve the root problem |
| **D. Accept the limitation** | 0 | $0 | None | Viable if travel plans avoid extended zero-solar scenarios |

**Production builders' choice:** Unicat and Bliss Mobil spec a dedicated generator. EarthRoamer uses auto-start. For a world-travel rig, Option A (portable generator, fuel from main diesel tank) is the most pragmatic.

---

### FINDING #2 — Single Inverter, Single Point of Failure (HIGH)

**The issue:** The design uses a single MultiPlus-II 24/5000. If it fails in a remote location, you lose all AC power — no cooking (induction), no microwave, no charging from shore power. Unicat specs dual inverters; Bliss Mobil uses redundant Victron units.

**Why this matters:** Inverters are the highest-stress component in the system (thermal cycling, surge loads, vibration). They fail. In a Namibian desert or Mongolian steppe, replacement lead time could be weeks.

**Mitigations:**

| Option | Weight | Cost | Notes |
|---|---|---|---|
| **A. Carry a spare MultiPlus-II** | 29 kg | ~$2,500 | Simplest. Pre-wired connector for fast swap. Victron units are field-replaceable. |
| **B. Dual MultiPlus-II in parallel** | +29 kg | +$2,500 | Active redundancy — both share load. If one fails, the other covers ~2,000W. Victron supports parallel operation natively. |
| **C. Add a small backup inverter** (e.g., Phoenix 24/1200) | 5 kg | ~$500 | Covers essential loads only (laptop, phone charging, lighting). Doesn't handle cooking. |
| **D. Accept and carry a spare** | 29 kg stored | $2,500 | Most weight-efficient — spare doesn't add parasitic losses. |

**Recommendation:** Option A (carry a pre-wired spare) for weight efficiency, or Option B (dual parallel) if the weight budget allows. A production Unicat would do Option B without question.

---

### FINDING #3 — No Wiring Standards Specification (MEDIUM-HIGH)

**The issue:** The design specifies wire gauges and fuse sizes but does not specify wiring construction standards. Production expedition vehicles use marine-grade practices because the environment (vibration, moisture, temperature cycling) is identical to offshore marine.

**What's missing:**

1. **Wire type specification** — All wiring should be tinned copper, marine-grade stranded (not solid), with cross-linked polyethylene (XLPE) or TXL insulation rated to 105°C minimum. Standard automotive PVC wire degrades in 3–5 years of expedition vibration.

2. **Termination standard** — All ring terminals should be adhesive-lined heat-shrink crimp terminals (not bare crimps). No twist-and-tape connections anywhere. Butt splices only with adhesive heat-shrink. This is non-negotiable for a rig expected to survive African corrugated roads.

3. **Connector standard** — All multi-pin connectors should be Deutsch DT/DTP series (IP67, vibration-rated) or equivalent. No Molex, no spade terminals in any location subject to vibration.

4. **Loom construction** — All wiring looms secured with Adel clamps (cushioned P-clips) at maximum 300mm intervals. No cable ties as primary restraint (they fatigue and snap). Looms protected with split corrugated conduit or woven loom tape.

5. **Labelling** — Every wire labelled at both ends with permanent heat-shrink labels. Brady or equivalent. Critical for field troubleshooting in a remote workshop.

**Mitigation:** Add a "Wiring Construction Standards" section to the design document specifying ABYC E-11 (marine electrical) as the baseline standard, adapted for vehicular use. This is what Bliss Mobil and Unicat follow.

---

### FINDING #4 — Galvanic Isolation Not Addressed (MEDIUM)

**The issue:** When connected to shore power in different countries, the ground reference can vary. Without galvanic isolation, stray currents can flow between the chassis, the habitat ground, and the shore ground — causing corrosion of the aluminum/steel chassis, tripping GFCIs, or in worst cases, electric shock hazard.

**What production builders do:** Victron makes a Galvanic Isolator (VDI-16, VDI-32, VDI-64) specifically for this. It's a small device (~$100, ~0.5 kg) installed in series with the shore power ground conductor. It blocks low-voltage DC galvanic currents while passing AC fault currents for safety.

**Mitigation:** Add a Victron VDI-32 Galvanic Isolator to the shore power inlet circuit. Trivial cost and weight. Should be mandatory for any rig connecting to international shore power.

---

### FINDING #5 — Battery Thermal Management Not Addressed (MEDIUM)

**The issue:** The Victron NG LFP batteries have a charge temperature range of 5°C to 50°C. Below 5°C, the BMS will block charging. The design doesn't address how the batteries will be kept warm in cold climates (Northern Europe winter, high-altitude camping, Canadian Rockies).

**Why this matters:** If you arrive at camp after a cold drive with depleted batteries and the ambient temperature is below 5°C, the solar and shore charger will be locked out until the batteries warm up. You're stuck with whatever charge you have.

**What production builders do:**

1. **Insulated battery compartment** — The passenger kitchen base should be insulated (25mm closed-cell foam on all sides) to retain heat.
2. **Battery heating pads** — Self-regulating 24V heating pads mounted under each battery, controlled by the BMS temperature sensor. The Victron NG BMS has temperature-based heating output control. ~20W per battery = 80W total when active.
3. **Waste heat recovery** — Route the diesel heater coolant loop near (not through) the battery compartment to provide passive warming.

**Mitigation:** Add battery heating pads (trivial cost, ~$200 total) and insulate the battery compartment. The NG BMS has a dedicated heating relay output for exactly this purpose.

---

### FINDING #6 — No Surge Protection / Lightning Strategy (MEDIUM)

**The issue:** 2050W of rooftop solar panels on a tall expedition vehicle create a significant lightning and surge risk. The design includes no surge protection devices (SPDs) on the solar input, shore input, or DC bus.

**What production builders do:**

1. **Solar SPD** — Type 2 surge arrester on the solar input side of the MPPT (e.g., Victron SPD Kit or Phoenix Contact VAL-SEC-T2). Protects against induced surges from nearby strikes.
2. **Shore power SPD** — Type 2 arrester on the AC input. International shore power quality varies wildly — voltage spikes, transients, and poor grounding are common.
3. **DC bus SPD** — Protects the battery bus from transients.

**Mitigation:** Add SPDs on solar input, shore input, and DC bus. Total cost ~$200–400, weight negligible. Standard practice on marine and expedition electrical systems.

---

### FINDING #7 — 24V→12V Converter is a Single Point of Failure (MEDIUM)

**The issue:** A single Orion 24/12-40 feeds all 12V loads: fridge, fans, water pump, cameras, lighting, heater. If this converter fails, you lose essentially every DC load in the habitat.

**Mitigations:**

| Option | Notes |
|---|---|
| **A. Dual converters** — 2× Orion 24/12-25, one for critical loads (fridge, pump, lighting), one for non-critical (cameras, fans, charging) | True redundancy. If one fails, manually reconnect critical loads to the surviving unit. |
| **B. Carry a spare** | Same approach as the inverter spare. The Orion converters are small and light (~1 kg). |
| **C. Emergency bypass** — Pre-wire a manual switch to connect critical 12V loads directly to a single battery (12.8V tap from one NG battery in the parallel bank, if possible) | Emergency-only. The NG batteries are 25.6V units so this is NOT possible without a separate 12V source. |

**Recommendation:** Option A (dual converters with split loads). Adds ~1 kg and ~$300. A production builder would always do this.

---

### FINDING #8 — Solar Panel Mounting Not Specified (MEDIUM)

**The issue:** The design specifies panel count and layout but not the mounting system. For an expedition vehicle, this is a critical detail. Panels must survive:

- Corrugated road vibration (continuous for hours)
- Tree branch impacts (African bush driving)
- High-speed driving wind loads (130+ km/h)
- Thermal expansion/contraction cycles

**What production builders do:**

1. **Z-bracket or L-bracket mounts** with rubber isolation pads between panel and bracket (vibration dampening).
2. **Through-bolted to roof rails** or structural extrusion — not adhesive-only (VHB tape fails in extreme heat/cold cycling).
3. **Air gap** of 25–50mm between panel and roof for cooling (panel efficiency drops ~0.4%/°C above 25°C).
4. **Sacrificial edge guards** — Aluminum angle around panel perimeter to take branch impacts instead of the glass.

**Mitigation:** Specify the mounting system in the design. Reference the Victron or Renogy expedition mounting kits as a baseline.

---

### FINDING #9 — No Emergency Lighting / Critical Load Priority (LOW-MEDIUM)

**The issue:** The design doesn't define what happens when the battery SOC reaches critical levels (5–10%). In a well-designed expedition system, there's a load-shedding sequence:

1. **First shed:** Non-essential AC loads (TV, charging drawer, vacuum)
2. **Then shed:** Starlink, exterior lighting
3. **Preserve:** Fridge, water pump, interior lighting, cameras, BMS/Cerbo
4. **Last resort:** Emergency LED strip on a separate circuit with its own small fuse — always powered until the BMS disconnects

**What production builders do:**

The Cerbo GX supports programmable relay outputs that can disconnect load groups based on SOC thresholds. Wire the DC distribution so non-critical loads pass through a relay that the Cerbo can open.

Additionally, install a small emergency LED light (battery-backed or on the very last BMS disconnect threshold) in the entry and bathroom areas.

**Mitigation:** Define a load-shedding table and wire the DC distribution with relay-switched groups. The Cerbo GX + Lynx Distributor can implement this in software.

---

### FINDING #10 — Shore Power Cable Storage & Management (LOW)

**The issue:** World travel means carrying multiple shore power cables and adaptors: NEMA 14-50 (NA), NEMA TT-30 (NA campgrounds), CEE17 blue 32A (Europe), CEE17 blue 16A (Europe campgrounds), Indian/Australian/South African adaptors, and extension cables. This is a significant storage requirement that isn't addressed.

**Mitigation:** Designate a specific exterior storage compartment or garage bay for shore power cables and adaptors. Include a cable management system (hook-and-reel or coiled storage) to prevent tangles. Label all cables with their country/standard.

---

## 3. Positive Observations — What's Done Right

These aspects of the design align with or exceed expedition manufacturer standards:

1. **Victron ecosystem throughout.** This is exactly what Unicat and Bliss Mobil use. Global dealer network, consistent software, and proven reliability. Smart choice for international travel.

2. **24V bus voltage.** Industry standard for expedition vehicles in this weight class. Good balance between cable gauge and component availability.

3. **Battery-forward mass balance.** Placing 208 kg of batteries forward of the axle as counterweight is a detail that many DIY builders miss. This shows proper engineering thinking.

4. **Honest autonomy analysis.** The design doesn't fudge the 10-day target — it clearly shows where it falls short and provides realistic scenarios. A production builder would respect this transparency.

5. **Solar array sizing.** 2050W on a habitat this size is excellent — above Unicat and EarthRoamer. Combined with the MPPT 250/100, this is a strong solar system.

6. **Dual DC-DC chargers.** Built-in redundancy for alternator charging. Good practice.

7. **CPAP on native 24V DC.** Small detail but shows attention — avoiding inverter losses on a nightly medical device.

8. **Shore power dual-standard strategy.** The field-switchable MultiPlus-II approach is clever and weight-efficient. Most builders would carry two separate units.

---

## 4. Summary — Priority Action Items

| Priority | Finding | Action | Est. Cost | Est. Weight |
|---|---|---|---|---|
| **CRITICAL** | #1 Generator backup | Add portable diesel generator or engine auto-start | $1,000–4,000 | 21–45 kg |
| **HIGH** | #2 Inverter redundancy | Carry a pre-wired spare MultiPlus-II | $2,500 | 29 kg (stored) |
| **HIGH** | #3 Wiring standards | Adopt ABYC E-11 marine wiring standard throughout | $500–1,000 (premium materials) | ~0 |
| **MEDIUM** | #4 Galvanic isolator | Add Victron VDI-32 | $100 | 0.5 kg |
| **MEDIUM** | #5 Battery thermal | Add heating pads + insulate compartment | $200 | 2 kg |
| **MEDIUM** | #6 Surge protection | Add SPDs on solar, shore, DC bus | $200–400 | ~1 kg |
| **MEDIUM** | #7 12V converter redundancy | Split to 2× Orion converters | $300 | 1 kg |
| **MEDIUM** | #8 Solar mounting | Specify vibration-rated expedition mounting | $500–800 | 5 kg |
| **LOW-MED** | #9 Load shedding | Define SOC thresholds + relay groups | $100 | ~0 |
| **LOW** | #10 Cable storage | Designate shore cable compartment | $0 | 0 |
| | | **TOTAL ADDITIONS** | **$5,400–9,600** | **~59–84 kg** |

---

## 5. Final Assessment

The Gimli2 electrical design is **above average for a DIY expedition build** and competitive with production vehicles on battery capacity and solar. The primary gaps are in **redundancy, construction standards, and backup power** — areas where production builders invest heavily because their warranty and reputation depend on it.

Addressing Findings #1–#5 would bring this design to a level that a Unicat or Bliss Mobil engineer would nod approvingly at. Findings #6–#10 are polish items that separate a good system from a great one.

The Victron ecosystem choice is the single best decision in this design. It means every component talks to every other component, the Cerbo GX provides a unified monitoring and control platform, and Victron dealers exist in nearly every country the rig will visit. This is exactly how the professionals do it.

---

*Review generated 2026-02-28 from expedition vehicle industry benchmarks and publicly available specifications from Unicat, Bliss Mobil, and EarthRoamer.*
