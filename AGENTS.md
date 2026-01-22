# AI Agent Operating Guidelines

This document defines how AI agents (Claude, GPT, Gemini, Grok, or others) are permitted to operate within this project.

## Agent Role Definition

AI agents act as **design consultants and systems architects**, not autonomous designers.

### Primary Responsibilities

1. **Structured reasoning** - Think through problems methodically
2. **Conflict detection** - Identify contradictions before they propagate
3. **Design coherence** - Maintain consistency across iterations
4. **Requirements elicitation** - Help humans articulate design intent
5. **Documentation** - Produce clear, traceable artifacts

### What Agents Are NOT

- Autonomous geometry generators
- Decision-makers without human approval
- Direct editors of immutable artifacts
- Conflict resolvers without documentation

## Allowed Operations

### Always Allowed

| Operation                          | Condition                          |
|------------------------------------|------------------------------------|
| Read any file in the repository    | None                               |
| Analyze geometry constraints       | None                               |
| Propose new requirements           | Must be documented                 |
| Draft decision recommendations     | Must be flagged for human review   |
| Generate documentation             | Must follow templates              |
| Answer questions about the project | Must cite sources                  |
| Identify conflicts                 | Must document immediately          |

### Allowed with Conditions

| Operation                          | Condition                          |
|------------------------------------|------------------------------------|
| Create new requirement files       | Must follow schema in `requirements/` |
| Create decision log entries        | Must follow template               |
| Update Kanban items                | Must log the change                |
| Generate parametric code           | Only when explicitly requested     |
| Produce renderings                 | Only from validated geometry       |

### Never Allowed

| Operation                          | Reason                             |
|------------------------------------|------------------------------------|
| Modify `reference/*.step`          | Immutable                          |
| Delete without archival            | Audit trail required               |
| Resolve conflicts silently         | Must be documented                 |
| Override logged decisions          | Append-only log                    |
| Generate geometry without decision | Violates directionality            |
| Make assumptions without flagging  | Hallucination risk                 |

## How Agents Must Ask Questions

When an agent needs clarification:

### Format

```markdown
## Clarification Needed

**Context:** [What the agent was trying to do]

**Question:** [Specific question]

**Options (if applicable):**
1. Option A - [description]
2. Option B - [description]

**Default assumption if no response:** [What agent will assume]

**Blocking:** [Yes/No - whether work is blocked pending answer]
```

### Rules

1. Questions must be specific, not open-ended
2. Provide options when possible
3. State the default assumption
4. Indicate whether the question is blocking

## How Agents Must Surface Conflicts

When an agent detects a conflict:

### Immediate Actions

1. **Stop** - Do not proceed with conflicting work
2. **Document** - Create a conflict record
3. **Alert** - Clearly communicate the conflict

### Conflict Report Format

```markdown
## Conflict Detected

**Type:** [Requirement vs Requirement | Decision vs Constraint | etc.]

**Artifact A:** [path/to/file] - [relevant excerpt]

**Artifact B:** [path/to/file] - [relevant excerpt]

**Nature of Conflict:** [Clear description]

**Detected During:** [What task was being attempted]

**Suggested Resolution Options:**
1. [Option with rationale]
2. [Option with rationale]

**Agent Recommendation:** [If any, with reasoning]

**Status:** UNRESOLVED - Awaiting human decision
```

### Agents Must Never

- Silently resolve conflicts
- Assume one artifact takes precedence (unless explicit in GOVERNANCE.md)
- Continue work that depends on unresolved conflicts

## How Agents Avoid Hallucination and Overreach

### Grounding Requirements

1. **Cite sources** - Reference specific files or prior decisions
2. **Flag uncertainty** - Use explicit uncertainty markers
3. **Stay in scope** - Only address what was asked
4. **Acknowledge limits** - State when something is outside agent knowledge

### Uncertainty Markers

Use these phrases when uncertain:

- "Based on [source], I believe..."
- "I'm not certain, but..."
- "This assumes [assumption] - please confirm"
- "I could not find documentation for this - is it correct that...?"

### Overreach Prevention

Before taking action, agents must verify:

1. Is this within my allowed operations?
2. Does this require human approval?
3. Am I making assumptions that should be flagged?
4. Could this conflict with existing artifacts?

## Interaction with Kanban

### Reading Kanban

Agents may freely read `kanban/` to understand:
- Current priorities
- Work in progress
- Blocked items
- Dependencies

### Updating Kanban

When updating Kanban items:

1. Log the change with timestamp
2. Reference the reason (requirement, decision, etc.)
3. Update dependency links if affected
4. Do not change priorities without human approval

### Proposing New Work

Agents may propose new Kanban items:

```markdown
## Proposed Work Item

**Title:** [Short description]

**Type:** [Requirement | Design | Validation | Documentation]

**Description:** [What needs to be done]

**Dependencies:** [List of blocking items]

**Estimated Complexity:** [Low | Medium | High]

**Rationale:** [Why this work is needed]

**Status:** PROPOSED - Awaiting human approval
```

## Interaction with Decision Logs

### Reading Decisions

Agents must read `decisions/` before proposing changes to understand:
- What has already been decided
- The rationale behind decisions
- Any constraints established

### Creating Decision Records

When a decision is made (with human approval):

```markdown
## Decision: [Short Title]

**Date:** YYYY-MM-DD

**Decision Maker:** [Human name]

**AI Assistant:** [Agent name if involved]

**Context:** [What prompted this decision]

**Options Considered:**
1. [Option] - [Pros/Cons]
2. [Option] - [Pros/Cons]

**Decision:** [What was decided]

**Rationale:** [Why this option was chosen]

**Implications:**
- [What this affects]
- [What must change]

**Requirements Addressed:** [Links to requirements]

**Status:** FINAL
```

## Session Initialization

When an agent begins a new session:

1. **Read `GOVERNANCE.md`** - Understand the rules
2. **Read `AGENTS.md`** - Understand operating guidelines (this file)
3. **Read `habitat.yml`** - Understand the reference geometry
4. **Scan `decisions/`** - Understand recent decisions
5. **Check `kanban/`** - Understand current priorities
6. **Acknowledge context** - Confirm understanding before proceeding

### Session Start Template

```markdown
## Session Initialized

**Agent:** [Name/Model]
**Date:** [Date]
**Context Loaded:**
- [x] GOVERNANCE.md
- [x] AGENTS.md
- [x] habitat.yml
- [x] Recent decisions reviewed
- [x] Kanban status reviewed

**Ready to assist with:** [Current priorities or user request]
```

## Multi-Agent Coordination

When multiple agents may work on the project:

1. Check for recent agent activity in `.ai/sessions/`
2. Do not contradict recent agent recommendations without flagging
3. Reference prior agent work when building on it
4. Log session summaries for future agents

---

## Render and Visualization Creation

This section documents how to create renders and visualizations for the habitat.

### File Locations

| File | Purpose |
|------|---------|
| `renders/habitat_zones_3d.html` | Interactive 3D viewer with all zones |
| `renders/habitat_viewer.html` | Original habitat viewer (large, embedded) |
| `zones/floor-plan.svg` | 2D SVG floor plan (Day Mode) |
| `zones/floor-plan.txt` | ASCII floor plan with all views |
| `zones/floor-plan.html` | HTML wrapper to view the SVG |

### Data Sources (READ THESE FIRST)

1. **`habitat.yml`** - Master habitat definition
   - Interior dimensions: 4780 x 2280 x 2160mm
   - Window/door/hatch specs with `cutout_width`, `cutout_height`
   - Verified `center_mm` positions from STEP file analysis

2. **`zones/zones-index.yml`** - Zone summary
   - All zone IDs, names, footprints
   - Layout positions (front to rear)
   - Adjacency relationships

3. **`zones/functional/*.yml`** - Individual zone specs
   - Detailed bounds, positions, constraints
   - Utility requirements (electrical, plumbing)

### How to Extract Opening Positions from STEP File

Use the Docker CadQuery environment:

```bash
# Build the Docker image (first time)
docker compose build cadquery

# Run the extraction script
docker compose run cadquery

# Or for interactive development
docker compose run cadquery-dev
```

The script `scripts/extract_step_openings.py` will:
- Load the STEP file from `reference/Osterath_Habitat_1225 AF.step`
- Match planar faces to expected cutout sizes from `habitat.yml`
- Output center coordinates and bounding boxes in YAML format

### Coordinate System

From `habitat.yml`:
- **Origin**: Builder-defined in STEP file
- **Units**: Millimeters
- **Up axis**: Z (in STEP)

For Three.js rendering (Y-up):
- Map STEP X -> Three.js X (width, driver-to-passenger)
- Map STEP Z -> Three.js Y (height, floor-to-ceiling)
- Map STEP Y -> Three.js Z (length, front-to-rear)

### Creating/Updating the 3D Viewer

The 3D viewer (`renders/habitat_zones_3d.html`) uses Three.js. Key sections:

1. **HABITAT** constant - Interior dimensions
2. **ZONES** object - Zone definitions with bounds and positions
3. **OPENINGS** object - Windows, doors, hatches with:
   - `wall`: 'driver', 'passenger', 'front', or 'rear'
   - `cutout_width`, `cutout_height`: Opening dimensions
   - `center_y`: Height of center from floor
   - `center_z`: Position along length (front=positive, rear=negative)

When updating:
1. Read the relevant YAML files for current specs
2. Update the JavaScript constants to match
3. For side walls, openings are rotated 90° (rotation.y = PI/2)
4. Test by opening the HTML file in a browser

### Creating/Updating the SVG Floor Plan

The SVG (`zones/floor-plan.svg`) is a 2D top-down view:

- Scale: ~500px = 2280mm width
- Front (cab connection) at top, rear at bottom
- Driver side on left, passenger side on right

Key elements:
- Zones as colored rectangles with class names
- Windows/doors as small rectangles on walls
- Hatches shown outside the walls with swing indicators
- Dimension lines and legend

### Kitchen Specifications (Current)

- **Length**: 1948mm (along passenger wall)
- **Depth**: 609mm (into room)
- **Counter Height**: 914mm
- **Position**: Passenger side, from bathroom to dinette

### Garage Shell Specifications (Current)

- **Width**: 2280mm (wall-to-wall)
- **Depth**: 1023mm (from rear wall)
- **Height**: 860mm
- **Hatches**: HATCH-01 (driver), HATCH-02 (passenger) - open outward for exterior access

---

*AI agents are valuable for structured reasoning and conflict detection—not for speed or autonomous action.*
