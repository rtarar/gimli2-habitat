# Kanban Workflow

This directory manages work prioritization and tracking for the Gimli2 Habitat project.

## Board Structure

Work items flow through these stages:

```
BACKLOG → READY → IN_PROGRESS → REVIEW → DONE
```

### Stage Definitions

| Stage       | Description                                      |
|-------------|--------------------------------------------------|
| BACKLOG     | Identified work, not yet prioritized             |
| READY       | Prioritized, dependencies resolved, ready to start |
| IN_PROGRESS | Actively being worked on                         |
| REVIEW      | Work complete, awaiting validation/approval      |
| DONE        | Validated, approved, and archived                |

## File Organization

```
kanban/
├── README.md           # This file
├── backlog.yml         # Items in BACKLOG
├── ready.yml           # Items READY to start
├── in-progress.yml     # Items IN_PROGRESS
├── review.yml          # Items in REVIEW
├── done/               # Archived completed items
│   └── YYYY-MM/        # Organized by month
└── templates/
    └── work-item.yml   # Template for new items
```

## Work Item Schema

Each work item follows this structure:

```yaml
- id: WI-001
  title: Short descriptive title
  type: requirement | design | validation | documentation
  description: |
    Detailed description of the work
  created: YYYY-MM-DD
  created_by: name
  priority: critical | high | medium | low
  dependencies:
    - WI-000  # Must complete first
  blocks:
    - WI-002  # Cannot start until this completes
  requirements:
    - REQ-001  # Related requirements
  decisions:
    - DEC-001  # Related decisions
  assigned_to: null | name
  status: backlog | ready | in_progress | review | done
  notes: |
    Additional context
```

## Rules

### Adding Items

1. New items start in BACKLOG
2. Include all known dependencies
3. Reference related requirements/decisions
4. AI agents may propose items (status: PROPOSED)

### Moving Items

1. Items move forward only (no regression without documentation)
2. Cannot move to READY if dependencies unresolved
3. Cannot move to DONE without review approval
4. Log all status changes with timestamp and reason

### Priority Definitions

| Priority | Definition                                          |
|----------|-----------------------------------------------------|
| CRITICAL | Blocks all other work, must resolve immediately     |
| HIGH     | Important for current milestone                     |
| MEDIUM   | Should complete this iteration                      |
| LOW      | Nice to have, can defer                             |

### Dependencies

- Dependencies must be explicit
- Cannot start work with unresolved dependencies
- Circular dependencies are forbidden (see GOVERNANCE.md)
- AI agents must check dependencies before proposing actions

## Metrics (Future)

Track for continuous improvement:
- Cycle time per item type
- Blocked time
- Throughput per week
- Dependency chains length
