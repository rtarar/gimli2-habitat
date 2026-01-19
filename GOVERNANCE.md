# Governance

This document defines the authoritative rules governing all design activities in this project.

## Source of Truth Hierarchy

The following hierarchy defines what is authoritative and in what order:

| Priority | Source                     | Description                              |
|----------|----------------------------|------------------------------------------|
| 1        | `reference/*.step`         | Immutable habitat geometry               |
| 2        | `habitat.yml`              | Reference metadata and constraints       |
| 3        | `requirements/*.yml`       | Documented design requirements           |
| 4        | `decisions/*.md`           | Logged decisions with rationale          |
| 5        | `zones/*.yml`              | Interior zone definitions                |
| 6        | Generated geometry         | Derived from above, always regenerable   |
| 7        | `renders/*`                | Visualization outputs, always regenerable|

Lower-priority sources must never contradict higher-priority sources.

## Immutable Artifacts

### The Habitat STEP File

The builder-supplied STEP file located in `reference/` is **immutable**.

**Allowed operations:**
- Read
- Measure
- Reference
- Derive interior constraints from

**Forbidden operations:**
- Edit
- Regenerate
- Override
- Replace without formal change control

### Change Control for Immutable Artifacts

If the habitat shell must change (e.g., builder revision):

1. Document the change request in `decisions/`
2. Obtain explicit human approval
3. Archive the old STEP file with timestamp
4. Import the new STEP file
5. Re-validate all dependent designs
6. Update `habitat.yml` with new metadata

## Directionality Rules

Design intent flows in **one direction only**:

```
Requirements → Decisions → Parametric Design → Geometry → Review
```

### Allowed Flows

| From                | To                    | Allowed? |
|---------------------|-----------------------|----------|
| Requirements        | Decisions             | ✅ Yes   |
| Decisions           | Parametric Design     | ✅ Yes   |
| Parametric Design   | Geometry              | ✅ Yes   |
| Geometry            | Review                | ✅ Yes   |
| Review              | Requirements (new)    | ✅ Yes   |

### Forbidden Flows

| From                | To                    | Allowed? |
|---------------------|-----------------------|----------|
| Geometry            | Decisions             | ❌ No    |
| CAD observation     | Direct geometry edit  | ❌ No    |
| Review              | Direct geometry edit  | ❌ No    |
| AI suggestion       | Geometry (without decision) | ❌ No |

### Converting Observations to Requirements

When reviewing geometry reveals issues:

1. **Do NOT** directly edit the geometry
2. **Do** create a new requirement documenting the issue
3. **Do** log a decision about how to address it
4. **Do** regenerate geometry from updated parameters

## Conflict Resolution Protocol

When conflicts are detected:

### Step 1: Halt

Stop all work on the conflicting items.

### Step 2: Document

Create an entry in `decisions/conflicts/` documenting:
- The conflicting artifacts
- The nature of the conflict
- When it was detected
- Who detected it (human or AI agent)

### Step 3: Escalate

Conflicts must be resolved by:
1. Consulting higher-priority sources of truth
2. If unresolved, escalating to human decision-maker
3. Logging the resolution with rationale

### Step 4: Resolve

Once resolved:
1. Update the lower-priority artifact to conform
2. Log the resolution in `decisions/`
3. Resume work

## Forbidden Operations (Global)

The following operations are **never allowed** without explicit human approval:

1. Modifying the habitat STEP file
2. Deleting requirements without archival
3. Overriding logged decisions silently
4. Generating geometry that violates constraints
5. Creating circular dependencies
6. Resolving conflicts without documentation

## Audit Trail

All changes must be traceable:

- Git commits must reference the requirement or decision driving the change
- Decision logs must reference the requirements they address
- Generated geometry must reference the parameters that produced it

## Version Control

- All artifacts are version-controlled in Git
- Immutable artifacts are never modified, only replaced with change control
- Decision logs are append-only (corrections are new entries, not edits)

---

*This governance model ensures design coherence over time, across multiple AI agents and human collaborators.*
