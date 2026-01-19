# AI Governance Artifacts

This directory contains artifacts for AI agent governance and coordination.

## Structure

```
.ai/
├── README.md              # This file
├── sessions/              # Session logs for multi-agent coordination
├── prompts/               # Reusable prompts for agents
└── context/               # Pre-loaded context for agent sessions
```

## Session Logs

When agents complete a session, they may log a summary:

```
sessions/
└── YYYY-MM-DD-agent-summary.md
```

This helps future agents understand recent activity.

## Prompts

Store reusable prompts here:

- `prompts/init-session.md` - Standard session initialization
- `prompts/conflict-check.md` - Conflict detection prompt
- `prompts/decision-draft.md` - Decision drafting assistance

## Context Files

Pre-load context for quick agent onboarding:

- `context/project-summary.md` - Current project state
- `context/recent-decisions.md` - Last N decisions
- `context/active-work.md` - Current kanban items
