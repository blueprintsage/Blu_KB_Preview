# Turn Mistake Into Reusable Skill

object_id: turn_mistake_into_reusable_skill
object_type: blu_code_skill
category: skillforge
subcategory: memory
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- skillforge
- memory
- generalization

## Objective
Convert each kernel coding mistake into a reusable BluCode skill.

## Trigger
A change breaks, causes thrash, confuses Admin, or repeats a known pattern.

## Steps / Flow
1. Record the concrete symptom.
2. Extract the general rule beyond the specific subsystem.
3. Write an entry with trigger, steps, acceptance checks, and affected files.
4. Update `INDEX.md` in `blu_code` only.
5. Keep the rule code-agnostic unless the mistake is truly subsystem-specific.

## Acceptance Checks
- Entry is generalized enough to apply elsewhere.
- Index points to the new entry.
- The entry prevents future behavior, not just describes history.

## Reference Inputs
- PASS pattern abstraction: concrete cases to reusable applied patterns
