# Decision: Import Osterath Habitat STEP File

**ID:** DEC-001
**Date:** 2025-01-19
**Status:** FINAL

## Decision Maker

- **Human:** User
- **AI Assistant:** Claude

## Context

The project requires a builder-supplied STEP file as the immutable reference geometry for all interior design work. The Osterath habitat STEP file was received and needed to be imported into the project.

## Options Considered

### Option 1: Import as-is

**Description:** Import the STEP file directly into the reference directory without modification.

**Pros:**
- Maintains exact builder geometry
- No risk of introducing errors
- Clear provenance

**Cons:**
- None identified

### Option 2: Convert to different format

**Description:** Convert STEP to another format (e.g., IGES, Parasolid)

**Pros:**
- Potentially smaller file size
- Compatibility with specific tools

**Cons:**
- Risk of geometry loss
- Loss of provenance
- Unnecessary complexity

## Decision

Import the Osterath Habitat STEP file (`Osterath_Habitat_1225 AF.step`) as-is into the `reference/` directory. This file becomes the immutable source of truth for all interior design work.

## Rationale

The STEP file is the industry-standard format for CAD interchange and maintains full geometric fidelity. Importing as-is preserves the exact builder intent and provides clear traceability.

## Implications

- All interior designs must conform to this geometry
- The STEP file must never be modified (per GOVERNANCE.md)
- Dimensions and features must be extracted and documented in habitat.yml
- WI-002, WI-003, WI-004 are now unblocked and can proceed

## Requirements Addressed

- Foundation for all subsequent design work

## Related Decisions

- None (first decision)

## File Details

- **Filename:** `Osterath_Habitat_1225 AF.step`
- **Size:** 1.4 MB
- **Provider:** Osterath
- **Revision:** 1225 AF
- **Import Date:** 2025-01-19

## Next Steps

1. Open STEP file in Fusion 360
2. Measure interior dimensions
3. Identify windows, doors, and features
4. Populate habitat.yml with extracted data
5. Mark WI-001 as complete

## Notes

This is the foundational decision for the project. All subsequent interior design work depends on this reference geometry.
