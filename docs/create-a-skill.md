# Create a skill

Use this guide when adding a reusable skill to `metaskills`.

## 1. Name the skill

Use lowercase kebab-case:

```text
skills/<skill-name>/
```

Prefer descriptive names over internal codenames.

## 2. Define the purpose

A skill should help downstream projects perform a repeatable workflow. Document:

- the problem it solves
- who uses it
- when an agent should invoke it
- what it produces
- what is out of scope

## 3. Use progressive disclosure

Keep `SKILL.md` short and operational. Put deeper material in referenced files:

```text
skills/<skill-name>/
├── SKILL.md
├── README.md
├── templates/
├── checklists/
├── references/
└── examples/
```

## 4. Include examples and validation

A usable skill should include at least one realistic prompt and a checklist for reviewing the output.

## 5. Keep it portable

Do not require this repository to run as a service. Do not depend on local paths, private infrastructure, or secrets. If a component is external and independently maintained, link it as a submodule under `components/` instead of copying source.

## 6. Update public catalogs

When adding a skill, update:

- root `README.md`
- relevant website skill cards
- examples, if applicable
