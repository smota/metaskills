# Build a repository onboarding agent

## Starting prompt

```text
Use the agent-builder skill to create a knowledge-only onboarding agent for this repository.
```

## Skill used

`agent-builder`

## Expected output structure

```text
agents/repository-onboarding-agent/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
└── evals.md
```

## Before

New contributors must infer architecture, conventions, and safe commands from scattered docs and prior commits.

## After

The downstream project has a knowledge-focused agent that explains structure, points to canonical docs, suggests first tasks, and refuses to invent undocumented policies.

## Assumptions to adapt

- Canonical docs and architecture files.
- Safe local setup and validation commands.
- Maintainer preferences for onboarding tone and scope.

## Validation checklist

- [ ] Agent cites repository files for factual claims.
- [ ] Agent explains setup, structure, and contribution flow.
- [ ] Agent avoids making code changes unless explicitly extended with tool permissions.
- [ ] Agent includes starter prompts for new contributor, maintainer, and reviewer scenarios.
- [ ] Agent evals include missing-doc and outdated-doc cases.
