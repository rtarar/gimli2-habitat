# Decision Log

This directory contains all design decisions made during the project.

## Purpose

The decision log provides:
- **Traceability** - Why things are the way they are
- **Conflict prevention** - Check before proposing contradictory changes
- **Knowledge persistence** - Context survives across sessions and agents

## File Organization

```
decisions/
├── README.md              # This file
├── DEC-001-title.md       # Individual decisions
├── DEC-002-title.md
├── conflicts/             # Unresolved conflicts
│   └── CONFLICT-001.md
└── templates/
    ├── decision.md        # Decision template
    └── conflict.md        # Conflict template
```

## Decision Naming

Format: `DEC-XXX-short-title.md`

- `DEC` - Decision prefix
- `XXX` - Three-digit sequential number
- `short-title` - Kebab-case description

## Decision Status

| Status    | Meaning                                      |
|-----------|----------------------------------------------|
| PROPOSED  | Under consideration, not yet approved        |
| FINAL     | Approved and in effect                       |
| SUPERSEDED| Replaced by a later decision                 |
| WITHDRAWN | Proposed but not approved                    |

## Rules

1. **Append-only** - Never edit past decisions; create new ones
2. **Reference requirements** - Link to the requirements addressed
3. **Document rationale** - Future readers need to understand why
4. **Check for conflicts** - Before proposing, verify no contradictions
5. **Human approval** - All FINAL decisions require human sign-off

## Using the Decision Log

### Before Proposing a Change

1. Search existing decisions for related topics
2. Verify your proposal doesn't contradict FINAL decisions
3. If conflict found, document in `conflicts/` before proceeding

### Creating a Decision

1. Copy `templates/decision.md`
2. Fill in all sections
3. Set status to PROPOSED
4. Get human approval
5. Update status to FINAL

### Superseding a Decision

1. Create new decision referencing the old one
2. Update old decision status to SUPERSEDED
3. Add note pointing to new decision
