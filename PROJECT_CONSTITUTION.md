# Gimli2 Project Constitution

This document is enforceable. It defines how Gimli2 is governed, how decisions are recorded, and what constitutes "source of truth." If there is a conflict between informal discussion and this constitution, this constitution wins.

---

## 1) Purpose

Gimli2 exists to design and build a Mercedes-Benz 1225 AF (NG80) expedition truck with an integrated ~16 ft habitat suitable for long-duration international overland travel, full-time living, and remote work.

### Non-goals
- Not a "concept-only" project: designs must converge toward buildable, serviceable outcomes.
- Not a vendor brochure: marketing language is secondary to engineering clarity.
- Not a single-tool workflow: artifacts must remain usable across CAD, documentation, and vendor environments.

---

## 2) Source of Truth Hierarchy

When facts conflict, resolve them using this order:

1. **Uploaded authoritative documents / measured reality** (photos with measurements, OEM manuals, signed vendor drawings, installed-as-built notes)
2. **Repository canonical artifacts** (current branch contents)
3. **Current discussion context** (the latest thread that created/modified an artifact)
4. **Memory/recall** (helpful for continuity but not a specification)

Anything that matters must be promoted into a canonical artifact; otherwise it is not a commitment.

---

## 3) Canonical Artifacts and Where They Live

The following are the only places considered canonical:

| Location | Contents |
|----------|----------|
| `docs/specs/` | Requirements, constraints, acceptance criteria, dimensional envelopes, targets |
| `docs/architecture/` | System architecture, schematics, subsystem boundaries, interface control notes |
| `docs/decisions/` | Decision log entries / ADR-style records |
| `docs/vendor/` | Vendor communications, quotes, procurement records, lead times |
| `reference/` | STEP files, supplier specs, immutable reference geometry |
| `cad/` | STEP/DXF exports, profiles, derived geometry |
| `build-log/` | As-built notes, photos, measurements, deviations from plan |
| `habitat.yml` | Habitat reference metadata (dimensions, features, openings) |

If something is "important," it must exist in one of the above locations.

---

## 4) Decision Logging Rules (Mandatory)

### 4.1 What requires a decision entry
A decision entry is required for:
- Architecture choices (subsystem boundaries, interfaces)
- Safety-critical choices (structure, fuel, electrical protection, egress)
- Procurement commitments (major components, irreversible purchases)
- Dimensional commitments (cutouts, hatch/window placements, tank volumes)
- Any change that affects more than one subsystem

### 4.2 Decision format
Every decision entry MUST include:

```yaml
Decision ID: G2-DEC-###  # sequential
Title: [descriptive title]
Date: YYYY-MM-DD
Status: TENTATIVE | CONFIRMED | REJECTED | SUPERSEDED
Owner: [name/role]
Context: [problem statement]
Decision: [what was decided]
Rationale: [why this choice]
Alternatives: [what else was considered]
Impacts: [downstream changes required]
Open Questions: [if any]
```

### 4.3 Status rules
| Status | Meaning |
|--------|---------|
| `TENTATIVE` | Under evaluation; not a commitment |
| `CONFIRMED` | Accepted; now part of the build plan |
| `REJECTED` | Considered and explicitly not chosen |
| `SUPERSEDED` | Replaced by a newer decision (must reference the newer ID) |

A design is not "real" until it is `CONFIRMED` in the decision log.

---

## 5) Change Control (Mandatory)

### 5.1 What counts as a "change"
Any modification to a `CONFIRMED` decision, a canonical spec, or a released drawing is a change.

### 5.2 How changes are made
1. Create a new decision entry that references the original decision ID
2. Mark the old decision `SUPERSEDED`
3. Update impacted canonical artifacts (specs, architecture, CAD references)
4. Add a "Last updated" line to each updated document

### 5.3 No silent edits
Do not "quietly" change core parameters (dimensions, voltages, component classes, tank volumes, etc.). If it matters, it is logged.

---

## 6) Versioning and "Last updated" Conventions

All canonical artifacts MUST include:
- `Version: vX.Y` (increment as appropriate)
- `Last updated: YYYY-MM-DD`
- If applicable, a reference to relevant decision IDs (e.g., `Related: G2-DEC-012, G2-DEC-018`)

CAD exports should include version in filename when practical (e.g., `subframe-cutout_v1.2.step`).

---

## 7) Quality Bar for Specs and Numbers

- Prefer measured values; cite the source (measurement, OEM manual, vendor drawing)
- If a value is unknown, mark it `TBD` and assign an owner/action to resolve it
- Avoid implied commitments in narrative text—commitments live in specs and decisions

---

## 8) Repository Discipline

- Do not duplicate the same "source of truth" in multiple places
- If duplication is necessary (e.g., excerpt in README), the canonical version must be referenced and linked
- Keep artifacts short and scannable; deep detail goes into appendices or dedicated subsystem docs

---

## 9) Definition of Done (for any subsystem update)

A subsystem update is "done" when:
- [ ] The spec/constraint is recorded in `docs/specs/`
- [ ] The architecture impact (if any) is captured in `docs/architecture/`
- [ ] The decision (if any) is logged in `docs/decisions/`
- [ ] Affected drawings/files are updated and versioned
- [ ] Open TBDs are explicitly listed with owners/actions

---

## 10) AI Agent Operating Rules

AI agents (Claude, GPT, Gemini, Grok, etc.) operate as **design consultants**, not autonomous designers.

### Agents MUST:
- Follow this constitution
- Reference canonical artifacts, not memory
- Log decisions when making commitments
- Ask for clarification rather than assume
- Treat the STEP file as immutable geometry

### Agents MUST NOT:
- Modify reference geometry
- Make commitments without decision entries
- Override human decisions
- Generate geometry without explicit request

See `AGENTS.md` for detailed AI operating guidelines.

---

## 11) Habitat Shell Rules

The habitat shell is provided as a **builder-supplied STEP file** and is **immutable**.

### The STEP file defines:
- Interior volume
- Wall geometry
- Windows and doors
- Mounting surfaces

### Design flow (one direction only):
```
Requirements → Decisions → Parametric Design → Geometry → Review
```

Reverse flow is forbidden. Observations from CAD tools must be converted into requirements, constraints, or decision updates—never direct geometry edits.

---

## 12) Amendment Process

This constitution may be amended by:
1. Creating a decision entry (`G2-DEC-###`) proposing the change
2. Marking it `CONFIRMED` after review
3. Updating this document with version increment

---

*Version: v1.0*
*Last updated: 2025-01-19*
