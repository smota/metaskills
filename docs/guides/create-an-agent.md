# Create an agent

Use the `agent-builder` skill when you want a portable agent package for another project.

## Start

Install or update `agent-builder` in the adopting repo:

```bash
npx skills add https://github.com/smota/metaskills --skill agent-builder --full-depth
```

Then ask your coding agent:

```text
Use the agent-builder skill to design an agent that <goal>.
```

## Decide maturity level

Pick the smallest useful level:

| Level | Name | Use when |
| --- | --- | --- |
| 0 | Prompt agent | Instructions and boundaries are enough |
| 1 | Knowledge agent | Source-aware answers are needed |
| 2 | Tool-enabled agent | Read-oriented MCP/OpenAPI tools are needed |
| 3 | Action agent | Mutating actions are needed |
| 4 | Orchestrating agent | Handoffs or subprocess/job execution are needed |
| 5 | Learning agent | Feedback, evals, benchmarks, and versioned improvement are needed |

See [Agent maturity](../concepts/agent-maturity.md).

## Package shape

```text
agents/<agent-name>/
├── README.md
├── AGENT.md
├── starter-prompts.md
├── knowledge-sources.md
├── tools-actions.md
├── runtime-capabilities.md
├── capability-maturity-scorecard.md
├── agent-guardrails-matrix.md
├── agent-validation-checklist.md
├── evals.md
└── CHANGELOG.md
```

Optional advanced files:

```text
handoff-contract.md
execution-model.md
continuous-improvement-plan.md
feedback.jsonl
benchmark-report.md
adapters/
```

## Validate

- `AGENT.md` is canonical.
- Harness adapters do not override canonical behavior.
- Runtime capabilities are marked required, optional, unavailable, or unknown.
- Every missing capability has fallback.
- Tools/actions include schema, auth, permission tier, confirmation, rollback, audit, and failure behavior.
- Level 4+ agents include handoff and execution contracts.
- Level 5 agents include evals, feedback, benchmark, and changelog workflow.

## Release in adopter project

Commit generated files in the adopter repo after review:

```bash
git diff --check
git add agents/<agent-name>
git commit -m "Add <agent-name> agent"
```
