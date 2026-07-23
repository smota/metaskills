# Level 0 prompt agent fixture

Current maturity: Level 0 prompt agent.
Target maturity: Level 1 knowledge agent.

## Package shape

```text
agents/concise-reviewer/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── capability-maturity-scorecard.md
├── agent-validation-checklist.md
└── evals.md
```

## AGENT.md excerpt

- Job: review prose for clarity and concision.
- Tools/actions: none.
- Knowledge sources: user-provided text only.
- Refuse: legal, medical, or security claims not present in source.

## Starter prompt

"Review this README section for clarity and return only concrete edits."

## Fallback behavior

If source text is missing, ask user to provide text. Do not invent context.

## Validation

- Passes without MCP/OpenAPI tools/actions.
- Passes without subagents or subprocess/job support.
- `AGENT.md` remains canonical and harness-neutral.
