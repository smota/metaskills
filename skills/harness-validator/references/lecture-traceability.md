# Lecture traceability and design rationale

The skill synthesizes all fourteen English lectures from [Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/en/). The course is a conceptual foundation, not a universal compliance standard.

| Lecture | Main lesson | Validator capability |
| --- | --- | --- |
| 01. Strong Models Don't Mean Reliable Execution | Attribute failure across specification, context, environment, verification, and state. | Failure attribution and executable Definition of Done. |
| 02. What a Harness Actually Is | A harness combines instructions, tools, environment, state, and feedback. | Five-subsystem coverage and least-privilege review. |
| 03. Repository as Single Source of Truth | Durable knowledge belongs in an authoritative, discoverable system. | Fresh-session, authority, and ACID-style state checks. |
| 04. Split Instructions Across Files | Entry instructions should route rather than become an encyclopedia. | Progressive disclosure, relevance, contradiction, and staleness checks. |
| 05. Keeping Context Alive Across Sessions | Persist progress, decisions, results, and Git state. | Cold-resume and rebuild-cost review. |
| 06. Initialization Before Work | Prove setup infrastructure before feature work. | Clean setup, startup, runner smoke, readiness, and next-work checks. |
| 07. Clear Task Boundaries | WIP=1 is a safe default; done means verified behavior. | Atomic scope, activation gates, overreach, and verified completion. |
| 08. Feature Lists as Primitives | Scope needs identity, behavior, verification, state, and evidence. | Machine-readable work state and harness-owned pass transitions. |
| 09. Prevent Premature Victory | Completion must be external and executable. | Layered termination gates and checker-independence grading. |
| 10. Full Pipeline Verification | Cross-component claims require real-boundary evidence. | Risk-based pipeline tests and executable architecture invariants. |
| 11. Runtime Observability | Distinguish what was written from what actually ran. | Runtime/process signals, task traces, contracts, and rubrics. |
| 12. Clean Session Handoff | Completion requires verified work and a restartable state. | Build/test/progress/cleanup/startup and idempotency checks. |
| 13. Loop Engineering | Loops require goal, verification, stop, budgets, isolation, and external state. | Loop suitability, budgets, ratchets, and verification-debt review. |
| 14. Graph Engineering | Graphs require explicit routing, state, rollback, merge, and outcome anchors. | Graph suitability, replayability, recovery, and orchestration-tax review. |

## Tensions the validator must surface

- **WIP=1 vs. parallel agents:** apply WIP=1 per isolated worker or dependency branch; require merge rules for parallelism.
- **Repository authority vs. external state:** declare authority per field and define reconciliation, freshness, and failure behavior.
- **Passing state vs. regressions:** bind evidence to versions and support invalidation or reopening.
- **All-green handoff vs. known flakes:** allow only explicit baselines with owner, reason, expiry, and no-regression comparison.
- **Separate initialization vs. small projects:** require readiness outcomes, not a ceremonial initialization session.
- **Independent checker vs. same model:** report the degree of independence; role labels alone are insufficient.
- **Minimal instructions vs. completeness:** measure discovery and routing success rather than line count.
- **Full E2E vs. cost and flakiness:** apply E2E by risk and boundary crossing while preserving faster diagnostic layers.
- **Strict constraints vs. autonomy:** enforce invariants and prohibited outcomes rather than arbitrary implementation detail.
- **Clean state vs. high-throughput merging:** make economic exceptions explicit; never silently bypass evidence.

## Course gaps extended by this skill

The checklist adds conditional coverage for prompt injection, secret handling, supply-chain trust, requirements traceability, risk and criticality, rollback and disaster recovery, non-functional quality, governance, evidence provenance, human comprehension, portability, flaky or weak tests, and economic sustainability.

## Heuristics, not mandates

Do not hard-fail a project because it lacks a particular filename or tool. Course examples such as instruction line counts, maximum global rules, three-minute rebuild targets, context-window thresholds, one-session feature size, graph-adoption counts, or reported percentage gains are diagnostic prompts only. Validate discoverability, reproducibility, continuity, verification strength, safety, and measured coordination value instead.
