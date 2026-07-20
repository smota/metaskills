# Build a release notes agent

## Starting prompt

```text
Use the agent-builder skill to design an agent that drafts release notes from GitHub issues, pull requests, and changelog fragments.
```

## Skill used

`agent-builder`

## Expected output structure

```text
agents/release-notes-agent/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
└── evals.md
```

## Before

Release notes are assembled manually from scattered issues, PRs, and commit notes. Tone and completeness vary by maintainer.

## After

The downstream project has a reusable agent definition that asks for the release range, gathers approved sources, drafts audience-specific notes, and runs a checklist before publishing.

## Assumptions to adapt

- Source of truth for changes: GitHub issues, PR labels, changelog fragments, or commit history.
- Release note audiences: users, developers, maintainers, security reviewers.
- Required approval workflow before publishing.

## Validation checklist

- [ ] Agent identifies source documents before drafting.
- [ ] Agent separates breaking changes, fixes, features, and docs.
- [ ] Agent flags missing issue/PR context instead of inventing it.
- [ ] Agent includes starter prompts for patch, minor, and major releases.
- [ ] Agent evals include at least one incomplete-input case.
