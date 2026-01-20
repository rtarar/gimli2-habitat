# Gimli2 Habitat Interior Design

An AI-governed, requirements-driven interior design system for a physical habitat shell.

## Overview

This repository treats **physical habitat design as a governed, requirements-driven software system**. It provides a structured framework for AI-human collaboration on interior design while maintaining strict guardrails against:

- Circular reasoning
- Geometry drift
- Unstructured AI output
- Loss of design intent
- Conflicting decisions across iterations

## Core Principle: Immutable Habitat Shell

The habitat shell is provided as a **builder-supplied STEP file** and is **immutable**.

This STEP file defines the authoritative:
- Interior volume
- Wall geometry
- Windows and doors
- Mounting surfaces

**All interior design must conform to this geometry, not modify it.**

## Design Flow (One Direction Only)

```
Requirements → Decisions → Parametric Design → Geometry → Review
```

Reverse flow is forbidden. Observations from CAD tools must be converted into requirements, constraints, or decision updates—never direct geometry edits.

## Repository Structure

```
gimli2-habitat/
├── reference/              # Immutable habitat geometry (STEP file)
├── requirements/           # Design requirements and constraints
├── decisions/              # Decision log with rationale
├── kanban/                 # Work prioritization and tracking
├── zones/                  # Interior zone definitions
├── docs/                   # Project documentation
├── renders/                # Derived visualizations (GLB, images)
├── .ai/                    # AI governance artifacts
├── README.md               # This file
├── GOVERNANCE.md           # Source of truth and rules
├── AGENTS.md               # AI agent operating guidelines
└── habitat.yml             # Habitat reference metadata
```

## Separation of Responsibilities

| Concern             | Where it Lives                |
|---------------------|-------------------------------|
| Design intent       | Markdown / YAML               |
| Constraints         | `requirements/`               |
| Decisions           | `decisions/`                  |
| Geometry generation | Code / scripts                |
| Validation          | Fusion 360                    |
| Visualization       | `renders/` (derived outputs)  |

No tool may assume multiple roles.

## Workflow

1. **Requirements Discovery** - Elicit and document design requirements
2. **Prioritization** - Use Kanban to prioritize work with dependency awareness
3. **Decision Making** - Log decisions with rationale and traceability
4. **Design Generation** - Generate parametric designs that conform to constraints
5. **Validation** - Validate geometry in Fusion 360
6. **Review** - Generate renderings and review

## Multi-LLM Compatibility

This project is designed to work with multiple AI assistants:
- Claude
- GPT
- Gemini
- Grok

All agents must operate under the rules defined in `AGENTS.md`.

## Getting Started

1. Read `GOVERNANCE.md` to understand the rules
2. Read `AGENTS.md` to understand AI operating guidelines
3. Review `habitat.yml` for reference geometry metadata
4. Check `kanban/` for current work items

## Docker Environment

A Docker-based development environment is provided for running CadQuery scripts that process STEP files. This ensures consistent, reproducible execution without requiring local CadQuery/OpenCASCADE installation.

### Prerequisites

- Docker 20.10 or later
- Docker Compose v2 (optional)

### Quick Start

```bash
# Build the Docker image
./docker/build.sh

# Run the STEP extraction script
./docker/run.sh

# Start an interactive development shell
./docker/shell.sh
```

### Using Docker Compose

```bash
# Build
docker-compose build

# Run extraction script
docker-compose run --rm cadquery

# Interactive shell
docker-compose run --rm cadquery-dev
```

### Custom Parameters

```bash
# Custom tolerance
TOLERANCE=5.0 ./docker/run.sh
```

## Project Goals

1. Finalize interior design elements inside a fixed habitat shell
2. Elicit, refine, and track requirements through AI-human interaction
3. Prioritize work using Kanban and dependency awareness
4. Prevent cyclical or contradictory design changes
5. Generate up-to-date renderings on demand
6. Serve as a durable knowledge base across months of iteration
7. Remain compatible with multiple LLMs

## License

[To be determined]

---

*This project treats AI as a design consultant, not a geometry generator unless explicitly asked.*
