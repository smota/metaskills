# Changelog

All notable changes to `metaskills` should be recorded here.

This project uses lightweight, human-readable release notes. Each release should explain what changed, why it matters, and which skills, examples, docs, or components were affected.

## Unreleased

- No changes yet.

## 1.2 - 2026-08-16

### Added

- `harness-validator`, a read-only skill for auditing whether a project gives AI coding agents a reliable, safe, observable, and recoverable working environment.
- A complete 78-check assessment across nine categories: knowledge routing, environment, security, scope control, continuity, verification, observability, recovery, and orchestration economics.
- All-14-lecture traceability to the Learn Harness Engineering course, including explicit handling of conflicts, gaps, and over-detailed controls.
- Markdown and machine-readable assessment templates, a strict JSON validator, and a complete-template generator.
- Seven fixture-backed behavioral contract evals and fourteen deterministic package/validator tests.

### Changed

- Updated the public skill catalog, install examples, and skill documentation for MetaSkills 1.2.
- Made applicability, evidence provenance, non-averaged blockers, and smallest-effective recommendations explicit in harness reviews.

### Validation

- `python -m unittest tests.test_harness_validator -q`
- `python skills/harness-validator/scripts/validate_assessment.py skills/harness-validator/templates/assessment.json`
- `python skills/harness-validator/scripts/run_evals.py skills/harness-validator`
- Agent Skill Creator package validation, Python compilation, JSON parsing, and diff checks.

## 1.1 - 2026-07-23

### Added

- Agent Builder capability maturity model with Level 0-5 guidance.
- Harness-neutral agent packaging guidance with runtime capability matrices.
- Harness adapter templates for Pi, Claude, Codex, Gemini, and Microsoft Foundry.
- Agent-to-agent handoff and subprocess/job execution contract templates.
- Continuous improvement, feedback, benchmark, and maturity fixture templates.
- Public contribution pathway and review docs.
- Example use cases for building agents and skills.
- Interoperability and trust documentation.
- Website metadata guidance through `llms.txt` and sitemap updates.

### Changed

- Expanded `agent-builder` templates, checklists, examples, and validation rubric to support maturity-based agent evolution.
- Strengthened MCP/OpenAPI tool-action safety templates with permissions, confirmation, rollback, audit, and fallback expectations.

## Release checklist

Before publishing a GitHub release:

- [ ] Update this changelog.
- [ ] Confirm README install commands still work.
- [ ] Confirm skill catalog reflects the current `skills/` directory.
- [ ] Validate examples do not contain private or environment-specific data.
- [ ] Verify website links point to the current GitHub repo and examples.
