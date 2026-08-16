# metaskills

[![License](https://img.shields.io/github/license/smota/metaskills)](./LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/smota/metaskills?include_prereleases)](https://github.com/smota/metaskills/releases)
[![GitHub stars](https://img.shields.io/github/stars/smota/metaskills?style=social)](https://github.com/smota/metaskills/stargazers)

Portable, installable skills for building better AI agents, workflows, and agent capabilities directly inside your own repositories.

`metaskills` is for adopters who want practical, reusable agent-building workflows without adopting a new platform. Install a skill, use it in your project, and keep the generated assets in your own repo. MetaSkills 1.2 adds `harness-validator`, a read-only, evidence-first audit for the instructions, environment, security, work control, continuity, verification, observability, recovery, and orchestration around AI coding agents.

Website: <https://movetheneedle.info/metaskills/> · Source: <https://github.com/smota/metaskills>

## AI summary

MetaSkills is an open-source toolkit of installable skills that help developers build better AI agents, reusable workflows, and agent capabilities directly inside their own repositories. It helps agents grow from prompt-only helpers to knowledge, tool-enabled, action, orchestrating, and learning agents while keeping a portable file-based core. It is useful for OpenAI/Codex-style agents, Claude, GitHub Copilot, Gemini, Pi, Microsoft Foundry, and other tools that can read local instruction files. It is not a hosted runtime or agent management platform.

## Who it is for

- AI engineers building custom agents or agent workflows.
- Open-source maintainers documenting reusable project practices.
- Developer tooling builders packaging repeatable agent capabilities.
- Prompt and agent framework creators who want inspectable examples.
- Teams adopting OpenAI/Codex, Claude, GitHub Copilot, Gemini, or similar coding agents.

## Why this matters

Agent-building knowledge is often trapped in one-off prompts, private chats, or an individual developer's habits. `metaskills` turns that knowledge into portable, inspectable, version-controlled files: skills, templates, checklists, examples, and agent definitions that teams can review, adapt, and improve in Git.

## Quick start

List the skills available from this repository:

```bash
npx skills add https://github.com/smota/metaskills --list --full-depth
```

Install one or more skills:

```bash
npx skills add https://github.com/smota/metaskills --skill agent-builder --full-depth
npx skills add https://github.com/smota/metaskills --skill skill-creator --full-depth
npx skills add https://github.com/smota/metaskills --skill harness-validator --full-depth
```

Install without prompts by passing a target agent, for example:

```bash
npx skills add https://github.com/smota/metaskills --skill agent-builder --agent claude-code --full-depth -y
```

Each installed skill is self-contained and includes its own `SKILL.md`, README, templates, checklists, references, and examples. The exact install path depends on the selected target agent.

## Skill catalog

| Skill | Use when | Produces | Install command |
| --- | --- | --- | --- |
| [`agent-builder`](./skills/agent-builder/) | You want to create an agent, copilot, coding assistant, tool-enabled assistant, knowledge-focused assistant, or orchestrating agent for another project. | `agents/<agent-name>/README.md`, `AGENT.md`, maturity scorecard, runtime capabilities, tools/actions, handoff/job contracts, adapters, evals. | `npx skills add https://github.com/smota/metaskills --skill agent-builder --full-depth` |
| [`skill-creator`](./skills/skill-creator/) | You want to turn a workflow, prompt, document, transcript, script, or existing sub-agent into an installable skill. | `skills/<skill-name>/SKILL.md`, README, templates, checklists, references, examples. | `npx skills add https://github.com/smota/metaskills --skill skill-creator --full-depth` |
| [`harness-validator`](./skills/harness-validator/) | You want to audit whether a project gives AI coding agents a reliable, safe, observable, and recoverable working environment. | A read-only, evidence-backed maturity report with blockers, conflicts, gaps, over-detail findings, and prioritized improvements. | `npx skills add https://github.com/smota/metaskills --skill harness-validator --full-depth` |

## Examples

- [Build a release notes agent](./examples/build-release-notes-agent/)
- [Create a support triage skill](./examples/create-support-triage-skill/)
- [Build a database migration review agent](./examples/database-migration-review-agent/)
- [Build a repository onboarding agent](./examples/repository-onboarding-agent/)

See the [examples index](./examples/) for a quick comparison.

## Available skills

### [`agent-builder`](./skills/agent-builder/)

Build portable agents from a plain-language goal.

It helps:

- turn a natural-language idea into an agent specification
- choose a maturity level from Level 0 prompt agent to Level 5 learning agent
- define name, description, instructions, and boundaries
- identify knowledge sources
- design tools/actions with MCP/OpenAPI safety contracts
- document runtime capabilities, harness adapters, and fallback behavior
- model agent-to-agent handoffs and subprocess/job execution when needed
- create starter prompts, evals, feedback loops, benchmarks, and acceptance criteria
- package the result for downstream projects

Try prompts like:

```text
Use the agent-builder skill to design an agent that drafts release notes from GitHub issues and changelog fragments.
```

```text
Create a knowledge-only onboarding agent for this repository.
```

```text
Design a tool-enabled agent that reviews database migrations before release.
```

### [`skill-creator`](./skills/skill-creator/)

Create, evaluate, improve, benchmark, and evolve reusable skills.

It helps:

- create production-ready skill packages
- keep skills efficient with progressive disclosure
- generate eval specs and pass/fail cases
- plan improvements from feedback or failed evals
- benchmark versions or alternatives
- support optional learning logs
- support optional privacy-safe telemetry plans

Try prompts like:

```text
Use the skill-creator skill to turn this support triage workflow into a reusable skill.
```

```text
Evaluate this existing skill and suggest improvements with acceptance criteria.
```

```text
Create a benchmark plan comparing v1 and v2 of this skill.
```

### [`harness-validator`](./skills/harness-validator/)

Audit an AI coding-agent harness without modifying the target project.

It helps:

- assess nine capability categories from instructions through orchestration
- distinguish documented claims from executable, enforced, and maintained evidence
- surface non-averaged safety and reliability blockers
- identify conflicts, missing capabilities, stale evidence, and over-detailed controls
- recommend the smallest effective improvements by risk, confidence, and effort
- produce Markdown and validated JSON reports

Try prompts like:

```text
Use harness-validator to audit this repository for long-running coding-agent work. Do not edit anything.
```

```text
Assess whether this autonomous pull-request loop has safe permissions, recoverable state, independent verification, stopping conditions, and cost budgets.
```

## Use in a downstream project

1. Open the project where you want the skill available.
2. Run the `npx skills add` install command from that project root.
3. Ask your coding agent to use the installed skill by name.
4. Review the generated files.
5. Keep generated agents or skills in your project repo.
6. Re-run the install command when you want the latest version.

## Interoperability and trust

`metaskills` is file-based and vendor-neutral. It can support OpenAI/Codex-style coding agents, Claude, GitHub Copilot, Gemini, and other agent harnesses that can read project instructions. See [Interoperability and trust model](./docs/reference/interoperability.md).

## What this repo is not

`metaskills` is not a hosted AI platform, agent runtime, management system, deployment platform, issue tracker for downstream projects, or central control plane. It is a small collection of reusable skills and references that help other projects build their own agents and skills.

## Contributing

Contributions are welcome when they improve reusable skills, agents, toolsets, examples, components, or docs.

Start with:

- [Contributing guide](./CONTRIBUTING.md)
- [Create a skill](./docs/guides/create-a-skill.md)
- [Review a skill](./docs/guides/review-a-skill.md)
- [Release process](./docs/guides/release-process.md)
- [GitHub discoverability checklist](./docs/reference/github-discoverability.md)

## Repository structure

```text
skills/      Installable skill packages.
agents/      Native agent definitions and examples, when needed.
toolsets/    Tool integration guides, schemas, wrappers, and examples, when needed.
components/  External repositories linked as Git submodules plus .metaskills.md metadata.
examples/    Cross-skill examples that are not owned by one skill.
docs/        Repository architecture, conventions, and workflow runbooks.
```

## More documentation

- [Documentation index](./docs/) — adopter, builder, and contributor navigation.
- [Repository architecture](./docs/reference/repository-architecture.md) — structure, asset ownership, and implementation details.
- [Component submodule workflow](./docs/reference/submodules.md) — how external inspiration/reference repos are linked.
- [Interoperability and trust model](./docs/reference/interoperability.md) — compatibility, boundaries, and safety model.

## Inspirations and references

These skills are inspired by and reference the following projects and capabilities:

- [Microsoft 365 Copilot Agent Builder](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents) — natural-language agent creation, configure/review workflow, knowledge sources, actions, and starter prompts.
- [FrancyJGLisboa/agent-skill-creator](https://github.com/FrancyJGLisboa/agent-skill-creator) — plain-English workflow-to-skill strategy, validation, security scanning, evals, and cross-platform skill packaging.
- [Claude Skill Creator](https://claude.com/plugins/skill-creator) — Create, Eval, Improve, and Benchmark lifecycle for skill development.
- [metaskills/skill-builder](https://github.com/metaskills/skill-builder) — production-ready skill structure, progressive disclosure, and sub-agent-to-skill conversion guidance.
