# skill-creator skill

The `skill-creator` skill helps create, evaluate, improve, benchmark, and evolve reusable AI agent skills.

It is designed for this repository's vision: portable skills used by downstream projects, not a hosted management platform.

## Modes

- **Create** — build a new skill from a workflow, idea, docs, prompt, or sub-agent.
- **Eval** — define lightweight pass/fail eval cases.
- **Improve** — revise skills based on feedback, failures, or eval results.
- **Benchmark** — compare versions or alternatives.
- **Learn** — optionally record durable lessons and improvement history.
- **Telemetry** — optionally define privacy-safe local signals that guide improvement.

## Installable package contents

```text
skills/skill-creator/
├── SKILL.md
├── README.md
├── templates/
├── checklists/
├── security/
│   └── guardrails-matrix.md
├── references/
└── examples/
```

## References

- [`references/claude-skill-creator-notes.md`](./references/claude-skill-creator-notes.md)
- [`references/skill-builder-notes.md`](./references/skill-builder-notes.md)
- [`references/progressive-disclosure.md`](./references/progressive-disclosure.md)
- [`references/learning-workflow.md`](./references/learning-workflow.md)
- [`references/telemetry-guidance.md`](./references/telemetry-guidance.md)

## Component reference

`components/skill-builder` is a `reference-only` submodule. It informs this skill's structure but is not required for installation or runtime.
