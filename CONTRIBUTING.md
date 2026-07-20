# Contributing to metaskills

Thank you for helping make reusable agent-building practices easier to discover, inspect, and adopt.

`metaskills` is a repository of portable skills, agent definitions, toolsets, examples, and reference components. It is not a hosted runtime or central control plane. Contributions should help downstream repositories build or improve their own agents and skills.

## Good contributions

- New or improved installable skills under `skills/<skill-name>/`.
- Agent definitions or examples under `agents/` when they are reusable beyond one project.
- Tool integration notes, schemas, or wrappers under `toolsets/`.
- Concrete examples under `examples/`.
- Maintainer docs under `docs/`.
- Reference components under `components/` as Git submodules with sibling `.metaskills.md` metadata.

## Quality bar

Every reusable asset should include:

1. Purpose and intended downstream use.
2. Prerequisites and dependencies.
3. Usage examples.
4. Inputs, outputs, and success criteria where applicable.
5. Clear boundaries and safety notes.
6. No secrets, credentials, private URLs, production data, or environment-specific assumptions.
7. Templates and supporting files colocated with the asset that owns them.

## Propose a new skill

1. Create `skills/<skill-name>/` using lowercase kebab-case.
2. Add `SKILL.md` with progressive disclosure: short trigger guidance first, deeper instructions in referenced files.
3. Add `README.md` with purpose, inputs, outputs, examples, and validation.
4. Add templates/checklists/references under the skill directory as needed.
5. Add or update examples that show how the skill is used.
6. Update the root README skill catalog.

See [`docs/create-a-skill.md`](./docs/create-a-skill.md) and [`docs/review-a-skill.md`](./docs/review-a-skill.md).

## Propose an example

Examples should be complete enough to evaluate quickly:

- starting prompt or goal
- skill used
- expected generated structure
- before/after value
- validation checklist
- assumptions and out-of-scope notes

## Working with components

External repositories belong in `components/` as submodules when they have their own lifecycle. Do not copy external source into native assets. Add a sibling metadata file such as `components/<name>.metaskills.md` and declare the mode: `reference-only`, `development-companion`, or `tool-provider`.

See [`docs/submodules.md`](./docs/submodules.md).

## Pull request checklist

- [ ] The change supports reusable skills, agents, toolsets, examples, or docs.
- [ ] Purpose and intended downstream use are documented.
- [ ] Prerequisites/dependencies are documented.
- [ ] Usage examples are included or updated.
- [ ] Inputs, outputs, and success criteria are clear where applicable.
- [ ] Asset-specific templates live inside the owning asset directory.
- [ ] No secrets, credentials, private URLs, or production data are included.
- [ ] Validation steps were run or clearly marked as not applicable.

## Releases

See [`docs/release-process.md`](./docs/release-process.md) for release guidance.
