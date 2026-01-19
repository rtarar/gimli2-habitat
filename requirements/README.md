# Requirements

This directory contains all design requirements for the Gimli2 Habitat interior.

## Purpose

Requirements capture **what** must be achieved, not **how** to achieve it.

They serve as:
- Input to design decisions
- Validation criteria
- Traceability anchors

## File Organization

```
requirements/
├── README.md              # This file
├── functional/            # What the design must do
├── constraints/           # Limitations and boundaries
├── preferences/           # Nice-to-haves (lower priority)
└── templates/
    └── requirement.yml    # Requirement template
```

## Requirement Schema

```yaml
id: REQ-XXX
title: Short descriptive title
type: functional | constraint | preference
category: spatial | ergonomic | structural | utility | aesthetic
priority: must | should | could | wont  # MoSCoW
description: |
  Detailed description of the requirement
rationale: |
  Why this requirement exists
source: user | code | regulation | derived
acceptance_criteria:
  - Measurable criterion 1
  - Measurable criterion 2
dependencies:
  - REQ-XXX  # Other requirements this depends on
conflicts_with: []  # Known conflicts (should be rare)
decisions:
  - DEC-XXX  # Decisions that address this requirement
status: draft | active | satisfied | deferred | rejected
created: YYYY-MM-DD
updated: YYYY-MM-DD
notes: |
  Additional context
```

## Requirement Types

| Type       | Description                                      |
|------------|--------------------------------------------------|
| FUNCTIONAL | What the design must accomplish                  |
| CONSTRAINT | Limitations that must be respected               |
| PREFERENCE | Desired but not mandatory                        |

## Priority (MoSCoW)

| Priority | Meaning                                          |
|----------|--------------------------------------------------|
| MUST     | Non-negotiable, design fails without it          |
| SHOULD   | Important, but workarounds exist                 |
| COULD    | Desirable if resources permit                    |
| WONT     | Explicitly out of scope (for this iteration)     |

## Rules

1. **One requirement per concept** - Don't combine unrelated needs
2. **Measurable criteria** - Must be verifiable
3. **Trace to source** - Where did this come from?
4. **Check for conflicts** - Before adding, verify compatibility
5. **Link to decisions** - Update when decisions address requirements

## Creating Requirements

1. Copy `templates/requirement.yml`
2. Assign next available ID (REQ-XXX)
3. Fill in all applicable fields
4. Place in appropriate subdirectory
5. Check for conflicts with existing requirements
