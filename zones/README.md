# Interior Zones

This directory defines the conceptual zones within the habitat interior.

## Purpose

Zones are **abstraction layers** that:
- Organize the interior into functional areas
- Define spatial relationships
- Establish constraints before detailed design
- Guide placement of interior elements

## Zone Types

| Zone Type        | Description                                    |
|------------------|------------------------------------------------|
| FUNCTIONAL       | Areas with specific purpose (kitchen, sleep)   |
| CIRCULATION      | Movement paths and access routes               |
| KEEP_OUT         | Areas that must remain clear                   |
| UTILITY_CORRIDOR | Routing for electrical, plumbing, HVAC         |
| BUFFER           | Transition spaces between zones                |

## File Organization

```
zones/
├── README.md              # This file
├── functional/            # Functional zone definitions
├── circulation/           # Movement paths
├── keep-out/              # Restricted areas
├── utility/               # Utility routing corridors
└── templates/
    └── zone.yml           # Zone template
```

## Zone Schema

```yaml
id: ZONE-XXX
name: Human-readable name
type: functional | circulation | keep_out | utility_corridor | buffer
description: |
  Purpose and characteristics of this zone
bounds:
  # Defined relative to habitat coordinate system
  # Populated after STEP import
  type: pending | box | polygon | derived
  reference: habitat.yml coordinate system
adjacencies:
  required:
    - ZONE-XXX  # Must be adjacent to
  preferred:
    - ZONE-XXX  # Should be adjacent if possible
  forbidden:
    - ZONE-XXX  # Must NOT be adjacent to
constraints:
  min_area: null  # m²
  min_dimension: null  # mm (smallest side)
  ceiling_height: full | partial  # Does it need full height?
  floor_access: required | preferred | not_needed
  wall_access: required | preferred | not_needed
  natural_light: required | preferred | not_needed
  ventilation: required | preferred | not_needed
  privacy: high | medium | low | none
requirements:
  - REQ-XXX  # Requirements this zone addresses
status: concept | defined | validated
created: YYYY-MM-DD
notes: |
  Additional context
```

## Rules

1. **Define conceptually first** - Don't need exact geometry yet
2. **Establish relationships** - Adjacencies matter before dimensions
3. **Link to requirements** - Zones exist to satisfy requirements
4. **No overlapping functional zones** - Except circulation
5. **Validate against habitat** - Zones must fit within shell

## Zone Definition Process

1. Identify functional needs (from requirements)
2. Define zone conceptually (purpose, relationships)
3. After STEP import: validate fit within habitat
4. Refine bounds based on actual geometry
5. Use zones to guide interior element placement

## Relationship to Decisions

Zone definitions may require decisions when:
- Adjacency requirements conflict
- Space is insufficient for all desired zones
- Trade-offs between competing zone needs

Document these in `decisions/` with zone references.
