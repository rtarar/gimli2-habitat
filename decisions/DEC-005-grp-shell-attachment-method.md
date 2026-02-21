# Decision: GRP Shell Cabinet & Furniture Attachment Method

**ID:** DEC-005
**Date:** 2026-02-21
**Status:** FINAL

## Decision Maker

- **Human:** Mithril (owner/builder)
- **AI Assistant:** Claude (structural guidance)

## Context

The Gimli2 habitat is built on a GRP (Glass Reinforced Plastic) shell. We need a reliable, non-invasive method to attach:
- Kitchen cabinets (upper and lower)
- Pantry
- U-shaped sofa/dinette seating

The shell must not be drilled through or punctured, as this would compromise the structural integrity and weatherproofing of the GRP monocoque. The attachment method must handle:
- Road vibration
- Lateral sway in transit
- Impact loads (people dropping into seating)
- Emergency braking forces

## Options Considered

### Option 1: Direct drilling into GRP shell

**Description:** Drill and bolt furniture directly into the GRP shell walls.

**Pros:**
- Simple, familiar construction method

**Cons:**
- Punctures shell weatherproofing
- Stress concentrations around holes in GRP
- Hard to relocate if layout changes
- Risk of delamination over time with vibration

### Option 2: Timber battens bonded to shell

**Description:** Epoxy timber battens to the interior GRP walls; screw furniture into battens.

**Pros:**
- No shell punctures
- Familiar to carpenters

**Cons:**
- Timber absorbs moisture, swells, and degrades
- Glue bond to GRP can fail if timber moves seasonally
- Lower long-term durability

### Option 3: Fiberglass rails bonded to GRP shell (SELECTED)

**Description:** Bond fiberglass flat bar or angle sections to the interior GRP walls using marine-grade adhesive sealant (e.g., Sikaflex 552 or 3M 5200). All furniture and cabinets screw into the rails, not the shell.

**Pros:**
- No shell punctures — weatherproofing fully preserved
- Fiberglass-to-fiberglass bond is chemically compatible and extremely strong
- Marine adhesives work in shear; slight glue gap (1–2 mm) absorbs road vibration
- Fiberglass holds screws very well; pre-drilling prevents cracking
- Rails can run long and continuous (more load distribution)
- L-shaped profile option adds resistance to pull-off, twist, and shear
- Proven in marine and vehicle construction
- No creep, fatigue, or moisture issues

**Cons:**
- Requires careful surface prep before bonding
- Cure time before loading (24–72 hrs depending on adhesive)
- More upfront planning to position rails correctly

## Decision

**Fiberglass rails bonded to the GRP shell** using marine-grade structural adhesive. All cabinets, pantry, and sofa framing attach via screws into these rails. The GRP shell is never drilled through.

## Rail Specifications

### Thickness
| Location | Rail Thickness | Rationale |
|---|---|---|
| Upper cabinets | ½" (12–13 mm) | Sufficient stiffness for overhead loads |
| Lower kitchen cabinets | ½"–⅝" (12–16 mm) | Base and counter-height rails |
| U-shaped sofa / seating | **⅝" (15–16 mm)** | Human impact and dynamic seating loads |

### Profile Shape
- **Flat rectangular strip** (½"+ × 2"–3" tall): simplest, easiest to align, suits most cabinet runs
- **L-shaped angle** (½"+ × 2"×2" legs): preferred behind upper cabinets, sofa backs, and pantry walls — resists pull-off, twist, and shear

### Rail Spacing
- Maximum 18–24" between horizontal rails
- For seating: closer spacing preferred ("ladder rungs on the wall")
- U-sofa corners: short vertical rails to create a rigid box frame

### Sofa Rail Layout (minimum)
1. Rail at seat height
2. Rail near floor
3. Short vertical rails at each corner

## Fastener Specification

- **Type:** Stainless steel or coated wood screws
- **Length:** 1"–1¼" into the rail
- **Practice:** Pre-drill all holes in fiberglass to prevent cracking

## Adhesive Specification

- **Product:** Sikaflex 552 or 3M 5200 (or equivalent marine structural adhesive sealant)
- **Glue gap target:** 1–2 mm (not razor-thin; allows shear flex and vibration damping)
- **Surface prep:** Both GRP shell and fiberglass rail must be clean, dry, and lightly abraded before bonding

## Visual Summary

```
[ Cabinet / Furniture ]
         │
    screws into
         │
[ Fiberglass Rail ]   ← ½"–⅝" thick flat or L-profile
         │
   bonded with
   Sikaflex 552
         │
[ GRP Shell Wall ]
```

No holes. No punctures. No shell compromise.

## Rationale

The fiberglass rail method is the standard approach in marine construction for exactly this loading scenario: dynamic loads, vibration, moisture, and structures that must not be punctured. Using fiberglass rail bonded to a fiberglass shell is chemically and mechanically ideal — same material family, compatible thermal expansion, and no moisture ingress risk. The marine adhesives specified are designed for this exact use case and will outlast the vehicle.

## Implications

- All furniture design must account for rail positions (rail locations determine screw points)
- Rail positions should be planned before any CAD furniture modeling is finalized
- Surface prep protocol must be documented before build phase begins
- No furniture may be screwed directly into the GRP shell under any circumstances

## Requirements Addressed

- Structural integrity of GRP monocoque preserved
- Furniture and seating safe for transit dynamic loads
- Long-term durability in variable climate/moisture environment

## Related Decisions

- DEC-003: Alde Heating Placement — shares the rear garage shell interior
- DEC-004: Electrical Placement — electrical conduit routing must coordinate with rail positions

## Notes

- ⅝" rails are recommended for any surface where people sit or lean dynamically
- Continuous long rails are stronger than short stub rails — maximize rail length where possible
- L-profile rails preferred wherever pull-off force is a concern (upper cabinets, sofa backs)
- Future phase: produce a cut list of rail lengths per zone once furniture layout is finalized in CAD
