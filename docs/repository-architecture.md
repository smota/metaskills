# Repository architecture

This document captures implementation details for maintainers. The main README is intentionally adopter-focused.

## Intent

`metaskills` is a source repository for installable/reusable skills, agent definitions, and toolsets that downstream projects can adopt. It is not a hosted agent platform, management system, or runtime.

## Asset ownership

Reusable assets own their supporting material. For example, an installable skill keeps its templates, checklists, references, and examples inside its own directory:

```text
skills/<skill-name>/
├── SKILL.md
├── README.md
├── templates/
├── checklists/
├── references/
└── examples/
```

This avoids repo-level template duplication and ensures package installers such as `npx skills add <repo> --skill <name>` install a complete, self-contained skill.

## Top-level structure

```text
skills/      Installable skill packages.
agents/      Native agent definitions and examples, when needed.
toolsets/    Tool integration guides, schemas, wrappers, and examples, when needed.
components/  External repositories linked as Git submodules plus .metaskills.md metadata.
examples/    Cross-skill examples that are not owned by one skill.
docs/        Repository architecture, conventions, and workflow runbooks.
```

## Component submodules

External repositories are linked under `components/` when they have their own lifecycle, history, or upstream contribution path.

Each component should have a sibling metadata file:

```text
components/<component-name>.metaskills.md
```

Supported modes:

- `reference-only` — pinned prior art or reference material; native assets must not require it at runtime or installation time.
- `development-companion` — used for upstream-compatible development and PRs.
- `tool-provider` — scripts, CLIs, schemas, or tests are intentionally called from the submodule.

See [`submodules.md`](./submodules.md) for workflow details.

## Tool-specific instruction files

`AGENTS.md` is the canonical tool-neutral instruction file for this repo. Tool-specific compatibility files such as `CLAUDE.md`, `CODEX.md`, `GEMINI.md`, and GitHub Copilot instructions point back to it.

## Current components

- [`components/agent-skill-creator`](../components/agent-skill-creator) — reference-only component for the `agent-builder` skill.
- [`components/skill-builder`](../components/skill-builder) — reference-only component for the `skill-creator` skill.
