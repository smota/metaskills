# Agents

An agent is a reusable role or worker users can ask to perform a job.

## Use an agent when

- users talk to it directly
- it needs a goal, scope, authority, and refusal boundaries
- it owns tools/actions, knowledge sources, or runtime capabilities
- it may delegate, run jobs, or improve through evals

## Typical package

```text
agents/<agent-name>/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
└── evals.md
```

Agent Builder 1.1 adds optional maturity scorecards, runtime capability matrices, handoff contracts, execution models, continuous improvement plans, and adapters.
