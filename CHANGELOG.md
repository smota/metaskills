# Changelog

All notable changes to `metaskills` should be recorded here.

This project uses lightweight, human-readable release notes. Each release should explain what changed, why it matters, and which skills, examples, docs, or components were affected.

## Unreleased

- No changes yet.

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
