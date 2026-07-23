# Example: knowledge-only agent

## Scenario

A downstream project wants an agent that answers onboarding questions from repository docs.

## Package

```text
agents/onboarding-guide/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
└── evals.md
```

## Agent summary

- Name: `onboarding-guide`
- Description: Helps new contributors find setup, architecture, and contribution information from project docs.
- Knowledge: README, docs directory, architecture decision records, contribution guide.
- Tools/actions: none required beyond file reading/search in the downstream project.

## Starter prompts

- "How do I set up this project locally?"
- "Where should I add a new integration?"
- "Summarize the contribution workflow."

## Acceptance checks

- Answers cite or name the source document used.
- If docs are missing, the agent says what is missing instead of inventing details.
- The agent does not make code changes unless explicitly asked.


## Maturity

Current maturity: Level 1 knowledge agent.

Runtime capability fallback: if target harness lacks required tools, delegation, or jobs, use documented manual fallback rather than silent failure.
