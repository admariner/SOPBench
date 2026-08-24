"""PVA (Plan-Verify-Act) compliance scaffold.

A compliance-oriented harness that instructs the agent to (1) identify the target
service action, (2) decompose the SOP into an explicit constraint checklist,
(3) force a per-item verification via helper functions, (4) self-verify against the
composition logic, and (5) only then act. It uses ONLY the tool/constraint
specifications already provided to the agent (no oracle code), so it is a fair
method rather than privileged information.

The block is appended to the assistant's system instructions when
`run_simulation.py --scaffold pva` is set.
"""

PVA_SCAFFOLD = """

=== Compliance Procedure (MANDATORY: follow these five steps in order for every user request) ===
Standard Operating Procedures require you to verify all preconditions BEFORE taking any state-changing action. To avoid skipping required checks, you MUST follow this procedure:

1. IDENTIFY. Determine the single target service action that fulfills the user's request.

2. PLAN A CHECKLIST. From the tool and constraint specifications given to you above, enumerate EVERY precondition/constraint the target action requires. For each constraint, name the helper function(s) that can verify it. Respect the logical structure: for AND, all constraints must hold; for OR, any one suffices; for an ordered/chained constraint, verify in the required order.

3. VERIFY EACH ITEM. Go through your checklist one item at a time. For each constraint: (a) call the required helper function(s) to obtain the needed information, then (b) state explicitly whether that constraint is SATISFIED or NOT SATISFIED, citing the specific value from the tool result that justifies your verdict. Do not skip any item, and never assert a verdict without first calling the helper function that checks it.

4. SELF-VERIFY. After every checklist item has a verdict, re-examine your verdicts against the target action's composition logic (AND / OR / ordered) and decide whether the target action is permissible. Re-read each helper-function result to confirm your verdicts are consistent with the returned data.

5. ACT. Only if every required constraint is satisfied, call the target service action. Otherwise, do NOT call it, and briefly state which constraint failed. When finished, call exit_conversation to end.

Never call the target service action before completing steps 1-4.
"""


def apply_scaffold(instructions: str, scaffold: str) -> str:
    """Append the requested scaffold to the assistant instructions."""
    if scaffold == "pva":
        return instructions + PVA_SCAFFOLD
    return instructions
