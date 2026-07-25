# Interoperability and trust model

`metaskills` is intentionally file-based. A skill is a readable package of Markdown instructions, templates, examples, checklists, and references that can be copied into the repository where work happens.

## Compatible workflows

`metaskills` is vendor-neutral. The assets are useful with tools that can read repository files and follow project instructions, including:

- OpenAI/Codex-style coding agents
- Claude Code and Claude skills
- GitHub Copilot instructions and repository context
- Gemini CLI and Gemini project guidance
- other agent harnesses that support local skills, prompts, or instruction files

The repo includes thin compatibility pointers such as `CLAUDE.md`, `CODEX.md`, `GEMINI.md`, `GITHUB_COPILOT.md`, and `.github/copilot-instructions.md` so tool-specific entry points can refer back to `AGENTS.md`.

## What adoption looks like

1. Install or copy a skill into a downstream project.
2. Ask an agent to use the skill by name.
3. Review the generated agent, skill, toolset, or example files.
4. Keep the result in the downstream project repository.
5. Adapt the generated files to local conventions.

## What this project is not

`metaskills` is not:

- a hosted AI platform
- an agent runtime
- an issue tracker for downstream projects
- a deployment system
- a centralized AI operations product
- a management control plane

## Trust model

- **Inspectable:** Skills are plain files, not hidden hosted prompts.
- **Portable:** Assets should work without requiring this repository at runtime.
- **Version-controlled:** Teams can review changes in Git.
- **Adaptable:** Downstream projects own their generated files.
- **No secrets:** Contributions must not include credentials, private URLs, production data, or customer data.
- **Self-contained:** Required templates and examples live inside the asset that owns them.

## Security expectations

Contributors should document tool permissions, data boundaries, failure modes, and validation steps for any skill or toolset that can influence code, configuration, or external systems.
