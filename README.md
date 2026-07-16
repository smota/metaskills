# metaskills

Installable skills for building better agents and skills in your own projects.

`metaskills` is for adopters who want practical, reusable agent-building workflows without adopting a new platform. Install a skill, use it in your project, and keep the generated assets in your own repo.

## Intent and Design Principles

**Intent:** `metaskills` is a workspace for reusable AI agent skills, agent definitions, and toolsets. It helps downstream projects easily adopt, build, or improve their own AI agents and tool-assisted workflows via self-contained packages, without requiring a centralized platform or hosted runtime.

**Design Principles:**
- **Portability and Independence:** Assets are fully self-contained (with their own `SKILL.md`, templates, and documentation) and usable without requiring this repo to run as a service.
- **Multi-Agent Compatibility:** `AGENTS.md` acts as the single source of truth for agent instructions. Ecosystem-specific files (like `GEMINI.md` or `CLAUDE.md`) are thin pointers back to it.
- **Modularity via Submodules:** External tools and referenced repositories are managed as Git submodules under `components/` to avoid copying source code.
- **Decentralization:** Templates are colocated with the skill that owns them. Repo-level template duplication and centralized complexity are strictly avoided. Project-specific assumptions must be kept out of reusable assets.
- **Clarity and Predictability:** The structure is standardized with explicit documentation, usage examples, and success criteria over hidden assumptions.

## Quick start

Install a skill with the `npx skills` CLI. It installs skills into the agent-specific location you choose, such as `.agents/skills`, `.claude/skills`, `.codex/skills`, or another supported target.

### macOS, Linux, Git Bash, or PowerShell

List the skills available from this repository:

```bash
npx skills add https://github.com/smota/metaskills --list --full-depth
```

Install one or more skills:

```bash
npx skills add https://github.com/smota/metaskills --skill agent-builder --full-depth
npx skills add https://github.com/smota/metaskills --skill skill-creator --full-depth
```

The installer prompts for the target agent when needed. To install without prompts, pass an explicit agent target, for example:

```bash
npx skills add https://github.com/smota/metaskills --skill agent-builder --agent claude-code --full-depth -y
```

### What gets installed

Each installed skill is self-contained and includes its own `SKILL.md`, README, templates, checklists, references, and examples. The exact install path depends on the selected target agent.

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
npx skills list
```

You can also inspect the agent-specific install directory selected during installation, for example:

```bash
find .agents/skills/agent-builder -maxdepth 2 -type f
find .agents/skills/skill-creator -maxdepth 2 -type f
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
2. Run the `npx skills add` install command from that project root.
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
