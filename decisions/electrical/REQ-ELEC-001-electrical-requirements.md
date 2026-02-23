# Electrical Requirements — Gimli2 Habitat + Truck

**ID:** REQ-ELEC-001
**Version:** 0.1
**Date:** 2026-02-23
**Status:** ACTIVE — pending load calculations and open decisions (see DECISIONS-ELEC-001)

---

## 0. Guiding Principles (Locked)

- **Off-grid first:** All core systems operate on battery + inverter without shore power. Exception: washer is shore-only.
- **Simplicity bias:** Avoid unnecessary wiring complexity. Battery-operated lights acceptable in cab and selectively elsewhere.
- **Lighting taxonomy:** Two categories only — **ambient** (spatial guidance + mood) and **task** (focused work/reading).
- **Master controls:** Act on ambient only. Never activate task lights.
- **Dimming:** All ambient is dimmable. Task lights generally dimmable. Bathroom dimming NOT required.
- **Stealth / wildlife mode:** Red or blue ambient options to minimise exterior light spill. Task lights remain conventional white.

---

## 1. Interior Lighting

### 1.1 Zones

| Zone | Area | Ambient | Task | Dimming |
|---|---|---|---|---|
| Zone 1 | Entry + Bathroom | Yes | No special requirement | Ambient yes; bathroom not required |
| Zone 2 | Kitchen + Hall | Yes (hidden/indirect preferred) | Galley: sink + cooktop (separate switches) | Yes |
| Zone 3 | Sleeping + Sitting | Yes (ceiling + indirect) | Reading lights | Yes |
| Master | All zones | Ambient on across all zones | NOT activated | — |

### 1.2 Ambient Lighting Behaviours

- Hidden/indirect preferred (warm, non-glare).
- Provides spatial guidance for walking at night.
- **Every cabinet and drawer interior** lit when opened (door-triggered switch, controller, or sensor — method TBD).
- Under-bed and under-structure ambient hidden lighting around bed and sitting area.
- Under-cabinet / toe-kick indirect lighting in kitchen and walking areas.
- Optional decorative hook lights (Nixie-tube style) — nice-to-have; provide hardwired or USB power point rather than batteries.

### 1.3 Task Lighting

| Location | Requirement | Switch |
|---|---|---|
| Kitchen sink | Dedicated task light | Independent switch |
| Kitchen cooktop | Dedicated task light | Independent switch (NOT shared with sink) |
| Sitting area | Reading lights at seating corners (approx 4) | Independent from ambient master |
| Bed (night mode) | 2 reading lights at head/upper corners | Independent from ambient master |
| Bathroom | Adequate light only | No special task requirement |

### 1.4 Day / Night Mode Lighting Behaviour

| Mode | Bed position | Ambient source | Task available |
|---|---|---|---|
| Day | Raised | Under-bed ambient lights sitting area | Reading lights available |
| Night | Lowered | Ceiling ambient low-level | 2 bed reading lights |

### 1.5 Colour / Stealth / Wildlife Mode

- Ambient supports **white + red/blue** modes.
- Red/blue for wildlife/low-impact use (turtle beaches etc.), not security.
- Task lights remain white only.

---

## 2. Interior Switches & Controls

### 2.1 Master Ambient Switch Locations (3 required)

| Location | Notes |
|---|---|
| Cab pass-through entry | Adjacent to pass-through; exact side TBD |
| Main entry door (inside) | Accessible on entry |
| Bed area | Night accessibility |

**Behaviour:** Turns on ambient across all zones. Does NOT activate task lighting.

### 2.2 Local Controls

- Sink task light — independent switch
- Cooktop task light — independent switch
- Reading lights — independent
- Each fan — independent switch
- Centralized control capability acceptable (Bluetooth/app) but must not add complexity

---

## 3. Interior AC Outlets & Charging

### 3.1 General Rules

- All outlets **flush wall-mounted** (no pop-up countertop outlets)
- Standard: **120V / 15A**; kitchen circuit possibly **20A**
- One **220V** outlet for washer or specialty appliance (shore-only; decision pending)

### 3.2 Kitchen Outlets

| Circuit | Load |
|---|---|
| Duplex outlet (2 receptacles) | Instapot, blender/grinder |
| Dedicated circuit | Induction cooktop (2-burner) |
| Dedicated circuit | Convection microwave/oven |

### 3.3 Sitting Area Outlets

- One duplex outlet each side (left + right)
- Primary charge station: laptops, phones, tablets, TV/monitor accessories

### 3.4 Bathroom / Medicine Cabinet

- Medicine cabinet: 3–4 charging points
- Supports: toothbrushes × 2, shaver, misc
- Items kept continuously charged

### 3.5 Electronics Charging Zone

- Dedicated drawer(s) with outlets for:
  - Camera battery chargers
  - Drone batteries
  - GoPros
  - Misc rechargeable gear
- Location: near sitting/work zone (cabinetry placement TBD)

### 3.6 Vacuum Charging

- Dedicated outlet for vacuum (location TBD)

---

## 4. Exterior AC Outlets

| Location | Requirement |
|---|---|
| Outdoor kitchen box (passenger side) | Power inside box for appliance use (blender, induction outdoors) |
| Passenger side rear | Near rear storage hatch |
| Driver side rear | Near rear storage hatch / tool / grill proximity |

Minimum 3 exterior AC points. Exact count and placement TBD in layout.

---

## 5. Exterior Lighting

### 5.1 Storage / Garage Lighting

- All exterior storage boxes: light on when opened
- Garage: light on when garage door opened
- Utility ambient type

### 5.2 Awning Lighting

- Hardwired power provision (no battery management)
- Exact fixture TBD

### 5.3 Rock Lights (Undercarriage)

- **6 rock lights** total — front / mid / rear
- Manual control (no motion trigger)
- Blue colour mode nice-to-have for dark step-out situations

### 5.4 Security Flood Lighting

| Position | Requirement |
|---|---|
| Front | 4 × round lamps preferred (retro style) over single bar |
| Driver side mid | High-mount flood on habitat wall |
| Passenger side mid | High-mount flood on habitat wall |
| Rear | Flood covering rear perimeter |

Goal: single-shot full perimeter illumination on demand.

### 5.5 Infrared (IR) for Cameras

- IR illumination around full camper perimeter
- Separate from visible security floods
- Must be powered and wired to camera positions

---

## 6. Cab Electrical

- **One standard dome/task light** only
- No ambient lighting system in cab
- Flashlight/torch for map-reading tasks
- Rationale: reduce complexity; cab not used for night-driving operations

---

## 7. Appliance & Load Inventory

### 7.1 Off-Grid Loads (battery + inverter capable)

| Category | Item | Notes |
|---|---|---|
| Climate | Roof fan × 2 | Model TBD |
| Lighting | All interior ambient zones | Zoned + dimmable |
| Lighting | All interior task lights | Galley + reading |
| Lighting | Cabinet/drawer lights | Door-triggered |
| Refrigeration | Fridge + freezer | Model + draw TBD |
| Cooking | Induction cooktop 2-burner | Model TBD |
| Cooking | Convection microwave/oven | Model TBD |
| Cooking | Instapot | |
| Cooking | Blender / grinder | |
| Connectivity | Starlink | Roof-mounted; internal power + router |
| Connectivity | Router / Wi-Fi (Pepwave or similar) | |
| Entertainment | Smart TV / monitor | |
| Security | Cameras (perimeter) | |
| Security | NVR / recorder | Lightweight |
| Water | Internal pump | |
| Water | External stream intake pump | |
| Water | UV filtration system | Power draw TBD |
| Charging | Laptops, phones, tablets | |
| Charging | Camera / drone / GoPro batteries | |
| Charging | Toothbrushes × 2, shaver | |
| Charging | Heat pad | |
| Charging | Vacuum | |
| Medical | CPAP | If used |

### 7.2 Shore-Only Loads

| Item | Notes |
|---|---|
| Washer | Shore-only; reduces inverter/battery demand |

---

## 8. Shore Power & Global Compatibility

- Must accept **120V / 60Hz** (North America)
- Must accept **230V / 50Hz** (EU / India / international)
- Dual-input capability required
- Shore inlet location: either side acceptable (TBD)
- Integrates with inverter/charger architecture (TBD)

---

## 9. Roof Penetrations / Cable Routing

- Consolidated roof conduit/penetration for:
  - Solar cabling
  - Starlink cabling
- Route toward battery/electrical zone
- Minimise number of roof holes (prefer single consolidated entry point)

---

## 10. Constraints (DO NOT violate)

- No pop-up countertop outlets
- No cab ambient lighting system
- Sink and cooktop task lights MUST be on separate switches
- Task lights MUST NOT activate via master ambient switches
- Avoid switch-gating appliances — use proper fusing/breakers

---

## Related Files

- [PLAN-electrical-layout.md](PLAN-electrical-layout.md) — battery + inverter placement decisions
- [DECISIONS-ELEC-001-open-decisions.md](DECISIONS-ELEC-001-open-decisions.md) — open decisions and todos
- [DEC-004-electrical-placement.md](../DEC-004-electrical-placement.md) — component placement decision
