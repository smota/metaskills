# Example: repository coding agent

## Scenario

A repository needs a coding assistant that follows local conventions and coordinates with other agents.

## Agent summary

- Name: `repo-coding-agent`
- Description: Implements small, reviewable code changes while preserving repository conventions.
- Knowledge: `AGENTS.md`, README, architecture docs, tests, package configuration.
- Tools/actions: file read/write, test runner, linter, Git status.

## Instructions excerpt

- Inspect relevant files before editing.
- Preserve user work and avoid unrelated changes.
- Prefer small commits with clear validation notes.
- Run the narrowest useful test first, then broader checks when risk justifies it.
- Summarize changed files, validation, and follow-up work.

## Starter prompts

- "Implement this issue using the repo conventions."
- "Refactor this module and update tests."
- "Review this PR for missing validation."

## Acceptance checks

- The agent names files changed.
- The agent reports tests or explains why they were not run.
- The agent does not claim unsupported validation.


## Maturity

Current maturity: Level 4 orchestrating agent.

Runtime capability fallback: if target harness lacks required tools, delegation, or jobs, use documented manual fallback rather than silent failure.
