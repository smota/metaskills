# agent-builder skill

The `agent-builder` skill helps users create practical, portable agents from plain-language goals.

It produces harness-neutral agent packages that can still leverage harness capabilities when present through adapters and explicit runtime contracts.

## Use cases

- design a new AI agent for a downstream project
- convert a workflow into agent instructions
- define knowledge sources and tool/action requirements
- model agent-to-agent collaboration and subprocess/job execution contracts
- create starter prompts, evals, guardrails, and validation criteria
- package an agent definition for reuse

## Outputs

Canonical package:

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

## Maturity model

- Level 0: prompt agent
- Level 1: knowledge agent
- Level 2: tool-enabled agent
- Level 3: action agent
- Level 4: orchestrating agent
- Level 5: learning agent

See `references/capability-maturity-model.md`.

## Harness neutrality

`AGENT.md` is canonical. `CLAUDE.md`, `CODEX.md`, `GEMINI.md`, Pi, Foundry, and other target files should be pointers or adapters. Adapters may document invocation mechanics and optional capabilities, not new semantics.

## Included templates

Templates include intake, agent definition, README, starter prompts, maturity scorecard, runtime capabilities, guardrails, validation checklist, tools/actions, MCP/OpenAPI schema starters, handoff contract, execution model, continuous improvement plan, feedback sample, benchmark report, changelog, and adapters.

## References

- `references/capability-maturity-model.md`
- `references/harness-adapter-model.md`
- `references/packaging-targets.md`
- `references/output-schema.md`
- `references/safety-boundaries.md`
- `references/validation-rubric.md`

## Validation

Suggested checks:

```bash
git diff --check
python -m json.tool skills/agent-builder/templates/mcp-tool-schema.json
python -m json.tool skills/agent-builder/templates/agent-eval-suite.json
```

This skill is self-contained for installers and does not require `metaskills` as a runtime service.
