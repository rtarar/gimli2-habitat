# Gimli2 — Expedition Truck + Habitat Program

Gimli2 is an expedition-truck build program to create a durable, long-duration overland platform optimized for full-time living and remote work. The base vehicle is a Mercedes-Benz 1225 AF (NG80 chassis), being converted into a self-supported global-travel rig with an integrated habitat module (approximately 16 ft). The objective is a vehicle that can reliably handle corrugations, poor roads, and mixed climates while remaining serviceable, safe, and practical for extended international travel.

This repository documents the end-to-end systems engineering of the truck + habitat: structural/subframe integration, entry systems, cabinetry and interior construction, water/grey tanks and plumbing, thermal/heating (diesel/hydronic), and a 24V Victron-based electrical architecture with a large LiFePO₄ bank and a roof solar array (on the order of ~1.2 kW) to support off-grid living. The build is managed with disciplined governance (canonical artifacts, decision logs, and versioning) to prevent design drift across tools, vendors, and iterations—and to preserve a high-quality record suitable for future publication.

---

## What We’re Building

- **Base vehicle:** Mercedes-Benz 1225 AF (NG80 chassis)
- **Habitat module:** ~16 ft expedition habitat for full-time living + remote work
- **Primary design goals:** reliability, serviceability, off-grid autonomy, safety, and documentation completeness
- **Core systems in scope:**
  - Structure & integration (subframe, pass-through, reinforcements)
  - Electrical (24V Victron ecosystem, LiFePO₄ bank, solar, monitoring)
  - Plumbing (fresh + grey, filtration, pumps, winterization considerations)
  - Thermal (diesel/hydronic heating strategy; insulation approach)
  - Interior (cabinetry materials, mounting strategy, durability on corrugations)
  - Security & networking (as required for remote work and travel)

---

## How This Repo Is Organized

This repo is designed so newcomers can understand the project, and contributors can make changes without causing “design drift.”

- `docs/specs/` — Requirements, constraints, acceptance criteria, design targets
- `docs/architecture/` — System architecture, schematics, interface-control notes
- `docs/decisions/` — Decision log / ADR-style records (what we chose and why)
- `docs/vendor/` — Vendor comms, quotes, procurement decisions, lead times
- `cad/` — CAD exports (STEP/DXF), profiles, reference geometry
- `build-log/` — Build log entries, photos/notes, “what changed in the real world”

> The enforceable rules for how changes are proposed and recorded live in `PROJECT_CONSTITUTION.md`.

---

## Working Agreements (High Level)

- Major design choices must be recorded in the decision log before they are treated as “real.”
- Drawings and specs must carry a version and “Last updated” date when modified.
- Unknowns are explicitly marked `TBD` with an owner/action to resolve them.

---

## Habitat Floor Plan

The habitat module interior layout (Day Mode with lift bed raised):

![Gimli2 Habitat Floor Plan](zones/floor-plan.svg)

**Key dimensions:**
- Interior: 4780mm (L) × 2280mm (W) × 2160mm (H)
- Kitchen: 1948mm length × 609mm depth × 914mm counter height (**driver side**)
- Floor-to-ceiling cabinets opposite kitchen (**passenger side**)
- Bathroom: toilet on **passenger side**, shower on driver side
- Garage shell: wall-to-wall (2280mm), 860mm high, with exterior hatches on both sides
- U-shaped dinette with rear bench seating on garage shell top

> **Layout Note (Swapped Configuration):** The kitchen is located on the **driver side** (left when facing rear), with floor-to-ceiling storage cabinets on the **passenger side** (right when facing rear). In the bathroom, the toilet is on the **passenger side** below WIN-04, and the shower is on the **driver side** adjacent to entry.

### Interactive 3D Viewer

To explore the habitat in 3D, open the interactive viewer:

```bash
open renders/habitat_zones_3d.html
```

The 3D viewer includes:
- All functional zones (color-coded)
- Day/Night mode toggle (shows bed raised vs lowered)
- Wireframe view option
- Windows, doors, and hatches
- Click zones to highlight

---

## Current Status (Update as Needed)

- [ ] Baseline architecture and subsystem boundaries captured
- [ ] Electrical one-line and parts list stabilized (24V Victron)
- [ ] Plumbing and tank layout finalized (fresh/grey, filtration, winterization)
- [ ] Thermal/insulation strategy selected and documented
- [ ] Entry and exterior integration decisions (steps/ladder, carriers, hatches)
- [ ] Interior cabinetry material and mounting strategy confirmed

---

## Contributing

If you want to contribute, open an issue describing:
1) the problem or improvement,
2) the affected subsystem(s),
3) the tradeoffs you see,
4) any links to relevant artifacts (specs, drawings, vendor data).

Proposed changes that impact architecture, safety, or procurement should include a decision entry in `docs/decisions/`.
