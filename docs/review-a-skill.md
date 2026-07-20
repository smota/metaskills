# Review a skill

Use this checklist before merging a new or changed skill.

## Fit

- [ ] The skill supports reusable agent, skill, or tool-assisted development workflows.
- [ ] It is useful beyond one private project.
- [ ] It does not turn `metaskills` into a hosted platform, runtime, or issue tracker.

## Documentation

- [ ] Purpose and intended downstream use are clear.
- [ ] Prerequisites and dependencies are documented.
- [ ] Inputs, outputs, and success criteria are documented.
- [ ] Examples are concrete enough to run or adapt.
- [ ] Safety boundaries and out-of-scope behavior are explicit.

## Packaging

- [ ] Required templates live inside the skill directory.
- [ ] Referenced files use relative paths that will work after installation.
- [ ] External references are linked, not copied, unless the content belongs natively in the skill.

## Trust and safety

- [ ] No secrets, credentials, private URLs, or production data are included.
- [ ] Tool permissions and risky actions are documented.
- [ ] Validation is possible with a lightweight checklist or command.

## Public readiness

- [ ] Root README catalog is updated if the skill is new.
- [ ] Website/public docs are updated if the skill is user-facing.
- [ ] Changelog or release notes mention the change when appropriate.
