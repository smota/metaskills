# Harness assessment checklist

Apply each check only when justified by the project's risk, lifetime, architecture, and autonomy level. Record evidence rather than awarding credit for artifact names.

## 1. Intent, instructions, and knowledge routing

- [ ] Purpose, architecture, conventions, hard constraints, and verification entry points are discoverable.
- [ ] Hard requirements are distinguishable from preferences and historical notes.
- [ ] Global instructions route readers to applicable topic guidance.
- [ ] Important decisions are durable rather than chat-only.
- [ ] Duplicate, stale, contradictory, and irrelevant instructions are detected.
- [ ] A fresh session can explain, run, and verify the project.
- [ ] Local guidance is near relevant code without duplicating global rules.

## 2. Tools, environment, and initialization

- [ ] Dependencies and runtime/tool versions are reproducible.
- [ ] Clean setup succeeds in an isolated environment.
- [ ] Standard start, test, lint, type-check, and aggregate-check commands exist.
- [ ] A passing smoke test proves the test runner works.
- [ ] Required capabilities use least privilege.
- [ ] Startup requires no undocumented repair.
- [ ] Templates or generated scaffolding are validated.
- [ ] Project initialization is distinct from per-session startup.

## 3. Security, permissions, and governance

- [ ] Secrets are isolated and redacted.
- [ ] Filesystem, shell, network, database, and connector permissions follow least privilege.
- [ ] Issues, docs, logs, webpages, and connector data are treated as untrusted prompt-injection inputs.
- [ ] Destructive operations are sandboxed, reversible, or approval-gated.
- [ ] Deploying, publishing, migrating, deleting, and spending require authorization.
- [ ] Privacy, retention, licensing, and dependency/tool provenance are governed.
- [ ] Actions are attributable through an audit trail.
- [ ] Retries cannot repeat unsafe side effects.

## 4. Scope, task decomposition, and work control

- [ ] Work items have stable identity, observable behavior, state, dependencies, and executable acceptance evidence.
- [ ] Active work is small enough to finish and verify.
- [ ] New activation is gated unless parallel work is demonstrably isolated.
- [ ] Blocked-task semantics cannot deadlock the scheduler.
- [ ] Opportunistic refactoring is separate from required scope.
- [ ] One authoritative work-state surface exists.
- [ ] Progress measures verified outcomes, not files or lines changed.

## 5. State, continuity, and authority

- [ ] Completed, active, blocked, and next work persist durably.
- [ ] Decisions preserve both choice and rationale.
- [ ] Verification results and known failures survive sessions.
- [ ] Handoff claims reconcile against Git and current command results.
- [ ] A fresh session can identify an executable next action.
- [ ] Concurrent writes have ownership, isolation, and merge semantics.
- [ ] Repository files and external trackers have field-level authority and reconciliation rules.
- [ ] Regressions or requirement changes can invalidate and reopen passing state.
- [ ] Evidence is bound to commit, requirement version, environment, verifier, and timestamp.

## 6. Verification, completion, and test strength

- [ ] Every acceptance criterion maps to an assertion or reviewable evidence.
- [ ] Static, runtime, integration, and E2E depth is selected by change risk.
- [ ] Startup and readiness are tested.
- [ ] Cross-component claims traverse real boundaries.
- [ ] User-visible outcomes, side effects, partial failures, cleanup, and error propagation are checked where applicable.
- [ ] Architectural invariants and recurring review findings become executable checks where feasible.
- [ ] The harness or checker—not worker confidence—grants completion.
- [ ] Failures explain what failed, why it matters, and likely repair direction.
- [ ] Flakes, retries, environments, and baselined failures are visible.
- [ ] Representative tests are periodically challenged by deliberate faults or mutation testing.

## 7. Observability and evaluator quality

- [ ] Lifecycle, critical path, data flow, exceptions, and abnormal resource behavior are observable.
- [ ] Task traces connect scope, execution, verification, and termination.
- [ ] Logs and traces use stable diagnostic schemas.
- [ ] Evaluator rubrics cite observable evidence.
- [ ] Evaluator independence is graded across role, context, evidence source, permissions, model, and deterministic oracle.
- [ ] Evaluator disagreement or rationalization is inspectable.
- [ ] Signals optimize diagnostic value rather than volume.
- [ ] Sensitive data is redacted.

## 8. Clean state, maintenance, and recovery

- [ ] Applicable checks pass at handoff, or exceptions are explicitly baselined.
- [ ] Progress and evidence match repository state.
- [ ] Debug and temporary artifacts are absent or intentionally retained.
- [ ] Standard startup still works.
- [ ] Cleanup and retry operations are idempotent.
- [ ] Rollback, backup, partial-failure repair, and disaster recovery match project risk.
- [ ] Harness artifacts have owners and update triggers.
- [ ] Exceptions have owner, reason, expiry, and no-regression conditions.
- [ ] Harness components are periodically benchmarked, simplified, or removed.
- [ ] Stale guidance is treated as riskier than explicit absence.

## 9. Autonomy, orchestration, and economics

- [ ] Autonomous loops have a goal, verifier, and stopping condition.
- [ ] Time, turns, tokens, cost, concurrency, and external-call budgets are bounded.
- [ ] Loop type matches the task: turn, goal, schedule, or event.
- [ ] Parallel work uses isolated workspaces and collision-free state.
- [ ] Graphs are used only when branching, rollback, parallelism, approvals, or valuable intermediate state justify them.
- [ ] Node roles, routing, rollback, shared-state schema, and merge semantics are explicit.
- [ ] Graph documentation matches executable routing.
- [ ] Metrics are anchored to outcomes, ground truth, or human spot checks.
- [ ] Human review capacity and code comprehension are monitored.
- [ ] Cheap deterministic checks precede expensive model evaluation.
- [ ] Orchestration demonstrates measured value over a simpler alternative.

## Cross-category review

- [ ] Conflicts and contradictions are listed with an explicit resolution or owner.
- [ ] Missing capabilities are separated from not-applicable capabilities.
- [ ] Redundant or over-detailed controls are identified.
- [ ] Evidence limitations and commands not run are disclosed.
- [ ] Recommendations are prioritized by risk reduction, confidence, and effort.
