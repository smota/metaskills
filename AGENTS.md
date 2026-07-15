# AGENTS.md

This file is the canonical guidance for AI agents working in this repository.

## Repository intent

`metaskills` is a workspace for reusable skills, agent definitions, and toolsets used by other projects. It is not intended to become a management system, hosted AI platform, or central control plane.

Everything added here should help downstream repositories build or improve agents, skills, or tool-assisted development workflows.

## Multi-agent development model

Use this repository for multi-agent development in a way that preserves portability:

- Keep shared instructions in `AGENTS.md`.
- Keep tool-specific instruction files, i.e. `CLAUDE.md`, `CODEX.md`, `AGY.md`, `GEMINI.md`, `GITHUB_COPILOT.md`, and `.github/copilot-instructions.md`, as thin compatibility pointers back to `AGENTS.md`.
- Make each skill or toolset usable by another project without requiring this repository to run as a service.
- Prefer clear handoff notes, examples, and tests over hidden assumptions.
- When multiple agents contribute, record durable decisions in docs or the relevant asset README.

## Expected structure

```text
skills/      Reusable skill packages, prompts, procedures, and examples.
agents/      Agent role definitions, collaboration patterns, and example configurations.
toolsets/    Tool integration notes, wrappers, schemas, and usage guides.
templates/   Starter files that other projects can copy into their repository.
examples/    Minimal examples showing how downstream projects consume these assets.
docs/        Design notes, conventions, and decision records.
```

Create directories as needed. Do not add empty complexity just to satisfy the structure.

## Contribution standards

When adding a skill, agent, or toolset:

1. State the purpose and intended downstream use.
2. Document prerequisites and dependencies.
3. Include usage examples.
4. Define inputs, outputs, and success criteria where applicable.
5. Keep project-specific assumptions out of reusable assets.
6. Avoid secrets, credentials, private URLs, or environment-specific values.

## Naming conventions

- Use lowercase kebab-case for directories and reusable asset names.
- Prefer descriptive names over internal codenames.
- Keep compatibility files uppercase when ecosystem conventions expect them, such as `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `AGY.md`, `GEMINI.md`, and `GITHUB_COPILOT.md`.

## Boundaries

Do not turn this repository into:

- an issue tracker for downstream projects
- a deployment platform
- an agent hosting runtime
- a centralized AI operations product
- a place for proprietary customer or production data

If an asset only applies to one repository, keep it in that repository instead.

## Agent workflow

Before changing files:

1. Inspect the relevant files and current repository status.
2. Preserve existing user work.
3. Prefer small, reviewable changes.
4. Update documentation when changing conventions.
5. If adding executable tooling, include the minimal validation command in the relevant README.

After changing files:

1. Summarize what changed.
2. List any validation performed.
3. Call out follow-up work or gaps.
