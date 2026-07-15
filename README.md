# metaskills

A repository of reusable skills for building agents, skills, and toolsets that are used inside other projects.

This repository is intentionally **not** a management platform, agent runtime, or standalone AI product. It is a workspace for designing, documenting, testing, and packaging portable development assets that can be copied, referenced, or installed by downstream projects.

## Purpose

`metaskills` provides shared building blocks for multi-agent development:

- agent instructions and operating guides
- reusable skill definitions
- toolset documentation and integration notes
- project templates for agent-enabled repositories
- examples that demonstrate how skills compose inside real projects

These assets should help other repositories bootstrap consistent agent behavior without turning this repository into the central place where those projects are managed.

## Repository layout

```text
.
├── AGENTS.md              # Workspace guidance for agents working in this repo
├── CLAUDE.md              # Claude-compatible pointer to AGENTS.md
├── CODEX.md               # Codex-compatible pointer to AGENTS.md
├── AGY.md                 # Agy-compatible pointer to AGENTS.md
├── GEMINI.md              # Gemini-compatible pointer to AGENTS.md
├── GITHUB_COPILOT.md      # GitHub Copilot-compatible pointer to AGENTS.md
├── .github/
│   └── copilot-instructions.md # GitHub Copilot repository instructions pointer
├── README.md              # Project overview
├── skills/                # Reusable skill packages and prompts
├── agents/                # Agent role definitions and examples
├── toolsets/              # Tooling guides, wrappers, and integration notes
├── templates/             # Starter files for downstream projects
├── examples/              # Small examples showing usage in consuming projects
└── docs/                  # Design notes and conventions
```

Directories may start empty. Add content when there is a reusable skill, agent pattern, or toolset that another project can consume.

## What belongs here

Add material when it is reusable across projects, such as:

- a skill that teaches an agent how to perform a repeatable task
- an agent role definition that can be adapted by another repository
- documentation for a toolset used by agent workflows
- repository setup templates such as `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `AGY.md`, `GEMINI.md`, GitHub Copilot instructions, or skill manifests
- examples that show how a consuming project should adopt a skill

## What does not belong here

Avoid adding:

- project-specific backlog, planning, or management state
- production app code for an AI platform
- customer data, secrets, credentials, or private operational details
- one-off instructions that only make sense in a single downstream repository

## Development principles

1. **Portable first** — write skills so they can be copied or referenced by other projects.
2. **Tool-neutral guidance** — prefer `AGENTS.md` as the canonical agent instruction file; keep tool-specific files as thin pointers.
3. **Composable assets** — skills, agents, and toolsets should be small enough to combine in downstream repositories.
4. **Explicit boundaries** — this repo helps build agents and skills; it does not operate them as a platform.
5. **Safe by default** — never commit secrets or environment-specific credentials.

## Getting started

1. Read [`AGENTS.md`](./AGENTS.md) for workspace conventions.
2. Add reusable assets under `skills/`, `agents/`, `toolsets/`, `templates/`, or `examples/`.
3. Document each asset with its purpose, expected inputs, expected outputs, and adoption instructions.
4. Keep downstream-project-specific notes in the downstream project, not here.

## Multi-agent development

This workspace is configured for multi-agent collaboration. `AGENTS.md` is the source of truth for agent behavior. Tool-specific files such as `CLAUDE.md`, `CODEX.md`, `AGY.md`, `GEMINI.md`, `GITHUB_COPILOT.md`, and `.github/copilot-instructions.md` exist for compatibility and point back to `AGENTS.md` so AI coding tools receive the same repository guidance.
