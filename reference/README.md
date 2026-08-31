# Domain reference documentation

Everything in this directory is **generated from the code that actually runs**, so
it cannot drift from the implementation. Regenerate it with:

```bash
python scripts/export_reference_docs.py
```

Do not edit these files by hand.

| Path | Contents | Generated from |
|---|---|---|
| `domains/<domain>.md` | Service functions, helper functions, their descriptions, the constraint composition attached to each, and the helper functions used to verify each constraint | `env/domains/<domain>/<domain>_assistant.py` |
| `prompts/<domain>_system_prompt.md` | The full system prompt the agent receives, including the per-action constraint descriptions | `env.task.task_initializer` with the defaults used for the main results |
| `schemas/<domain>_tools.json` | The tool (function-calling) schemas exposed to the agent | `env/domains/<domain>/<domain>_assistant.py` |

The seven domains are `bank`, `dmv`, `healthcare`, `library`, `online_market`,
`hotel`, and `university`.

The paper works the **bank** domain through in full in its appendix; this
directory covers all seven, and is the authoritative version whenever the two
disagree.

The prompts are rendered with the defaults `run_simulation.py` uses for the main
results (`--env_mode prompt`, `--default_constraint_option full`,
`--constraint_descr_format structured`, no function shuffling). Constraint
descriptions are task-dependent, so the prompt for an individual test case may
differ in which constraints are instantiated; the set of actions and the
structure are the same.
