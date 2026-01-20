# STEP Validation Readme

## Purpose

This readme summarizes what can be validated **today** against the immutable habitat STEP file and supplier documentation, and what remains pending. It is intended as a lightweight, repeatable checklist for confirming that the STEP geometry, `habitat.yml`, and supplier specs are in sync.

## Inputs Used

- `reference/Osterath_Habitat_1225 AF.step` (immutable STEP reference). 
- `habitat.yml` (documented windows/doors/features and interior dimensions). 
- `reference/supplier-specs/selections.yml` (selected products and key specs). 
- Supplier PDFs stored under `reference/supplier-specs/*` (reference-only; no automated parsing). 

## Method (Current Capability)

1. **Metadata consistency check** between `habitat.yml` and `reference/supplier-specs/selections.yml` for windows/doors. 
2. **Reference inventory** of supplier documents present in `reference/supplier-specs/`. 
3. **Manual-only STEP review requirement**: actual geometry validation (e.g., window cutout positions, sill heights, door swing) still requires CAD tooling (e.g., Fusion 360 interference check noted in `habitat.yml`). 

> Based on the current repository contents, there is **no automated STEP geometry parser or validation script**. Geometry validation must be performed in a CAD tool and the extracted measurements documented in YAML. This assumes no additional tooling exists outside the repo. Please confirm if you have a preferred STEP parsing workflow. 

## Findings

### Supplier Documents Present

- Windows: `reference/supplier-specs/windows/Window-dimensions.pdf` and `Roof-window-dimensions.pdf`. 
- Doors: `reference/supplier-specs/doors/Door-dimensions.pdf`. 

### Consistency Checks (YAML vs. YAML)

**Windows**

| Feature | `habitat.yml` | `selections.yml` | Result |
| --- | --- | --- | --- |
| WIN-01 RA-40 cutout | 670 x 1063 mm | 670 x 1063 mm | ✅ Match |
| WIN-01 visible | 637 x 1027 mm | 637 x 1027 mm | ✅ Match |
| WIN-02 RA-40 cutout | 670 x 1063 mm | 670 x 1063 mm | ✅ Match |
| WIN-02 visible | 637 x 1027 mm | 637 x 1027 mm | ✅ Match |
| WIN-03 DR-20 cutout | 554 x 698 mm | 554 x 698 mm | ✅ Match |
| WIN-03 visible | 400 x 650 mm | 400 x 650 mm | ✅ Match |
| WIN-04 RA-30 cutout | 570 x 673 mm | 570 x 673 mm | ✅ Match |
| WIN-04 visible | 537 x 637 mm | 537 x 637 mm | ✅ Match |

**Door**

| Feature | `habitat.yml` | `selections.yml` | Result |
| --- | --- | --- | --- |
| DOOR-01 opening | 637 x 1027 mm | 637 x 1027 mm | ✅ Match |
| DOOR-01 swing/hinge | outward / right | outward / right | ✅ Match |

### Gaps / Pending Measurements

The following fields are still `null` or marked as pending, which means they need to be extracted from the STEP file (or measured in CAD) and then recorded in YAML:

- Window sill heights (WIN-01, WIN-02, WIN-04). 
- Window positions from wall corners / front wall (WIN-01, WIN-02, WIN-04). 
- Roof window position from front/side (WIN-03). 
- Door threshold height (DOOR-01). 
- Door swing keep-out zones (currently `pending_step_analysis` in `habitat.yml`). 

## Recommended Next Validation Steps (CAD-Based)

1. Open the STEP file in Fusion 360 (or preferred CAD tool). 
2. Measure window/door cutout locations and sill/threshold heights. 
3. Extract window sill heights for WIN-01, WIN-02, and WIN-04 from the STEP file and record them in YAML. 
4. Extract window positions from wall corners/front wall for WIN-01, WIN-02, and WIN-04 and record them in YAML. 
5. Extract roof window position from the front/side walls for WIN-03 and record it in YAML. 
6. Extract door threshold height for DOOR-01 and record it in YAML. 
7. Confirm door swing envelope and document keep-out zone extents. 
8. Update `habitat.yml` and `reference/supplier-specs/selections.yml` with measured positions. 
9. Record findings (and any deviations) as new requirements or decisions, per governance. 

## Proposed Automation (Optional)

If you want automated checks in-repo, we could add:

- A small Python validation script that loads `habitat.yml` and `selections.yml` to detect mismatches. 
- A CI check that fails if critical dimensions diverge. 

This would still not replace CAD validation for STEP geometry but would enforce YAML consistency over time.

## Extraction Script (Experimental)

An experimental script is provided to scan the STEP file for planar faces that match the expected cutout sizes and report candidate positions and sill/threshold heights:

```bash
python scripts/extract_step_openings.py
```

The script requires `cadquery` and `pyyaml` and prints a YAML block with face centers, bounding boxes, and sill/threshold heights for each matched opening. These values still need to be confirmed in CAD before being copied into `habitat.yml` or `reference/supplier-specs/selections.yml`.

For convenience, you can run the wrapper script and capture output to a file:

```bash
scripts/run_step_openings.sh
```

This writes `tmp/step_openings.yaml` by default. Override paths by setting environment variables: `STEP_PATH`, `HABITAT_PATH`, `OUTPUT_PATH`, and `TOLERANCE_MM`.
