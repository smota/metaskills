# Level 4 orchestrating agent example

Current maturity: Level 4. Target maturity: Level 5.

Uses handoff contract for reviewer/planner-worker delegation and execution model for async `subprocess/job` work.

Fallback: if A2A or async jobs are unavailable, use manual handoff checklist and user-run commands.
## Validation

- Portable without `metaskills` runtime.
- `AGENT.md` remains canonical.
- Missing capability fallback is explicit.
