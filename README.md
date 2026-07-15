# metaskills

Installable skills for building better agents and skills in your own projects.

`metaskills` is for adopters who want practical, reusable agent-building workflows without adopting a new platform. Install a skill, use it in your project, and keep the generated assets in your own repo.

## Quick start

Install a skill with `npx skill` by pointing `SKILL_BASE_URL` at this repository.

### macOS, Linux, or Git Bash

```bash
SKILL_BASE_URL=https://github.com/smota/metaskills/tree/main \
npx skill skills/agent-builder
```

```bash
SKILL_BASE_URL=https://github.com/smota/metaskills/tree/main \
npx skill skills/skill-creator
```

### PowerShell

```powershell
$env:SKILL_BASE_URL = "https://github.com/smota/metaskills/tree/main"
npx skill skills/agent-builder
npx skill skills/skill-creator
```

### What gets installed

`npx skill` installs each skill into your current project's `.codebuddy/skills/` directory:

```text
.codebuddy/skills/agent-builder/
.codebuddy/skills/skill-creator/
```

Each installed skill is self-contained and includes its own `SKILL.md`, README, templates, checklists, references, and examples.

## Available skills

### [`agent-builder`](./skills/agent-builder/)

Build portable agents from a plain-language goal.

Use it when you want to create an agent, copilot, coding assistant, tool-enabled assistant, or knowledge-focused assistant for another project.

What it helps produce:

```text
agents/<agent-name>/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
└── evals.md
```

Key capabilities:

- turns a natural-language idea into an agent specification
- defines name, description, instructions, and boundaries
- identifies knowledge sources
- designs tools/actions and safety notes
- creates starter prompts
- adds validation and acceptance criteria
- packages the result for downstream projects

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

Use it when you want to turn a workflow, prompt, document, transcript, script, or existing sub-agent into an installable skill.

What it helps produce:

```text
skills/<skill-name>/
├── SKILL.md
├── README.md
├── templates/
├── checklists/
├── references/
└── examples/
```

Key capabilities:

- creates production-ready skill packages
- keeps skills efficient with progressive disclosure
- generates eval specs and pass/fail cases
- plans improvements from feedback or failed evals
- benchmarks versions or alternatives
- supports optional learning logs
- supports optional privacy-safe telemetry plans

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

## Choosing a skill

| If you want to... | Use |
| --- | --- |
| Build an agent for a downstream project | [`agent-builder`](./skills/agent-builder/) |
| Define an agent's knowledge, tools, and starter prompts | [`agent-builder`](./skills/agent-builder/) |
| Turn a workflow into an installable skill | [`skill-creator`](./skills/skill-creator/) |
| Improve or benchmark an existing skill | [`skill-creator`](./skills/skill-creator/) |
| Add optional learning or telemetry guidance to a skill | [`skill-creator`](./skills/skill-creator/) |

## Verify installation

After installing, check that the skill package exists:

```bash
find .codebuddy/skills/agent-builder -maxdepth 2 -type f
find .codebuddy/skills/skill-creator -maxdepth 2 -type f
```

You should see files such as:

```text
SKILL.md
README.md
templates/
checklists/
references/
examples/
```

## Use in a downstream project

1. Open the project where you want the skill available.
2. Run the `npx skill` install command from that project root.
3. Ask your coding agent to use the installed skill by name.
4. Keep generated agents or skills in your project repo.
5. Re-run the install command when you want the latest version.

## What this repo is not

`metaskills` is not a hosted AI platform, agent runtime, management system, or central control plane. It is a small collection of reusable skills and references that help other projects build their own agents and skills.

## More documentation

- [Repository architecture](./docs/repository-architecture.md) — structure, asset ownership, and implementation details.
- [Component submodule workflow](./docs/submodules.md) — how external inspiration/reference repos are linked.

## Inspirations and references

These skills are inspired by and reference the following projects and capabilities:

- [Microsoft 365 Copilot Agent Builder](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents) — natural-language agent creation, configure/review workflow, knowledge sources, actions, and starter prompts.
- [FrancyJGLisboa/agent-skill-creator](https://github.com/FrancyJGLisboa/agent-skill-creator) — plain-English workflow-to-skill strategy, validation, security scanning, evals, and cross-platform skill packaging.
- [Claude Skill Creator](https://claude.com/plugins/skill-creator) — Create, Eval, Improve, and Benchmark lifecycle for skill development.
- [metaskills/skill-builder](https://github.com/metaskills/skill-builder) — production-ready skill structure, progressive disclosure, and sub-agent-to-skill conversion guidance.
