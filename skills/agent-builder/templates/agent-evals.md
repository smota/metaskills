# Agent evals

Use lightweight pass/fail cases before adding heavier automation. For automated environments, populate `agent-eval-suite.json` using the structured JSON manifest template.

## Eval case template

```yaml
name: short-case-name
scenario: What situation is being tested
prompt: User prompt to the agent
expected_behavior:
  - Required behavior
must_include:
  - Required content
must_not_include:
  - Forbidden content
pass_criteria:
  - Objective pass/fail check
```

## Cases

### Case 1

```yaml
name:
scenario:
prompt:
expected_behavior:
  -
must_include:
  -
must_not_include:
  -
pass_criteria:
  -
```
