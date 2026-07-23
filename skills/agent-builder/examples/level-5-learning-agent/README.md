# Level 5 learning agent fixture

Current maturity: Level 5 learning agent.
Target maturity: Level 5 with tighter benchmark gates.

## Package shape

```text
agents/support-quality-agent/
├── README.md
├── AGENT.md
├── evals.md
├── agent-eval-suite.json
├── continuous-improvement-plan.md
├── feedback.jsonl
├── benchmark-report.md
├── CHANGELOG.md
├── runtime-capabilities.md
└── agent-validation-checklist.md
```

## Learning loop

1. Observe feedback or failed eval.
2. Classify: scope, knowledge, tool/action, safety, UX, orchestration, environment.
3. Add or update eval before instruction change when possible.
4. Patch `AGENT.md`, tools/actions, adapters, or contracts.
5. Run benchmark and record result.
6. Update `CHANGELOG.md` with what changed and why.

## Privacy

Feedback is local by default. Redact secrets, tokens, private credentials, customer data, and sensitive prompts.

## Fallback behavior

- No telemetry: use local `feedback.jsonl` or manual eval notes.
- No benchmark runner: compare eval results manually in `benchmark-report.md`.

## Validation

- Eval suite contains regression cases.
- Feedback entries are redacted.
- Changelog links changes to feedback/eval/benchmark evidence.
