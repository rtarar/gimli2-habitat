# Electrical Open Decisions & Todos

**ID:** DECISIONS-ELEC-001
**Version:** 0.1
**Date:** 2026-02-23
**Status:** ACTIVE

These todos must be resolved before load calculations and system sizing can be finalised.
Work through Section A (appliance selection) first — those answers feed directly into Section B (engineering).

---

## A — Appliance / Model Selection (resolve first)

These drive the load table and therefore all sizing calculations.

- [ ] **A1** Select induction cooktop model (2-burner) — need rated wattage + surge
- [ ] **A2** Select convection microwave/oven model — need rated wattage + surge
- [ ] **A3** Confirm roof fan model (MaxxFan or alternative) — need current draw × 2
- [ ] **A4** Select washer model — confirm 120V or 230V; shore-only; drum size
- [ ] **A5** Confirm fridge model — need continuous watt-hours/day
- [ ] **A6** Confirm freezer model (separate unit or combined?) — need continuous watt-hours/day
- [ ] **A7** Confirm Starlink dish model (Standard / HP / Mini) — need idle + active draw
- [ ] **A8** Confirm router/Pepwave model — need idle draw
- [ ] **A9** Confirm CPAP model if used — need wattage + nightly hours
- [ ] **A10** Confirm UV filter system model — need wattage + duty cycle

---

## B — Electrical Engineering & Sizing (requires A complete)

- [ ] **B1** Build full load table (continuous + peak/surge) for all items in REQ-ELEC-001 §7
- [ ] **B2** Calculate daily amp-hour demand (watt-hours/day → Ah at 12V or 48V bus)
- [ ] **B3** Size battery bank — capacity (Ah) for target autonomy (how many days off-grid without solar/charge?)
- [ ] **B4** Size inverter — must cover simultaneous peak loads (induction + microwave + other)
- [ ] **B5** Size shore power charger — for both 120V/60Hz and 230V/50Hz input
- [ ] **B6** Size solar array — panels + MPPT controller for daily recharge target
- [ ] **B7** Define AC distribution: branch circuits, breaker sizing, GFCI/AFCI zones
- [ ] **B8** Define DC distribution: lighting zones, fans, pumps, security, networking
- [ ] **B9** Define battery bus voltage — 12V vs 24V vs 48V (affects cable sizing throughout)
- [ ] **B10** Determine alternator charging strategy — truck alternator → DC-DC charger sizing

---

## C — Switching & Control Architecture

- [ ] **C1** Select ambient lighting controller — must support: zoning, dimming, white + red/blue colour, 3× master switch locations
- [ ] **C2** Define cabinet/drawer lighting trigger method — door-switch vs controller vs sensor
- [ ] **C3** Define master ambient switch wiring — 3-way logic or smart switch bus
- [ ] **C4** Decide Bluetooth/app control integration — confirm platform (e.g., KNX, Victron Cerbo, custom ESP32, commercial smart switch)
- [ ] **C5** Define bed day/night mode lighting changeover — automatic (bed position sensor) or manual switch?

---

## D — Placement & Layout

- [ ] **D1** Finalise kitchen duplex outlet exact position on wall
- [ ] **D2** Finalise sitting area outlet positions relative to windows and cabinetry
- [ ] **D3** Finalise medicine cabinet internal layout — 3 or 4 charging points; USB-A/C mix
- [ ] **D4** Decide vacuum charging outlet location
- [ ] **D5** Decide electronics drawer location (near sitting/work zone) and ventilation strategy for charging heat
- [ ] **D6** Finalise exterior outlet positions — outdoor kitchen box, passenger rear, driver rear
- [ ] **D7** Finalise shore power inlet side (driver or passenger) and connector type (30A TT-30 / 50A 14-50 / CEE17 combo)
- [ ] **D8** Finalise roof penetration location and conduit routing path to battery zone

---

## E — Exterior Lighting Implementation

- [ ] **E1** Confirm rock light model and mounting positions (6 total: front / mid / rear each side)
- [ ] **E2** Confirm rock light blue mode — included in selected model or separate fixture
- [ ] **E3** Select front security flood type — confirm 4 × round lamps vs bar; mounting positions
- [ ] **E4** Confirm side flood mounting height and bracket approach on habitat GRP walls
- [ ] **E5** Confirm rear flood mounting point (rear wall, bumper bar, or box lid)
- [ ] **E6** Select IR emitter model and confirm placement covers camera FOV at all positions
- [ ] **E7** Confirm awning light model and hardwire connection point

---

## F — Global / Shore Power

- [ ] **F1** Confirm dual-voltage strategy — single dual-input inverter/charger vs separate units
- [ ] **F2** Confirm 220V washer outlet — dedicated circuit, shore-only interlock method
- [ ] **F3** Confirm one 220V general outlet location (if included beyond washer)

---

## Sequencing Guide

```
A (appliances) → B1 load table → B2-B6 sizing → B7-B10 distribution design
                                               → C (controls)
                                               → D (placement)
A + D → E (exterior lighting layout)
B5 + F → shore power architecture
```

Start with **A1–A6** (cooking + refrigeration) as these dominate the load table.

---

## Related Files

- [REQ-ELEC-001-electrical-requirements.md](REQ-ELEC-001-electrical-requirements.md) — full requirements
- [PLAN-electrical-layout.md](PLAN-electrical-layout.md) — battery + inverter placement
