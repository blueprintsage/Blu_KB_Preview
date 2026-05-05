# Spec Is Not Runtime Debug Order

object_id: spec_not_runtime_debug_order
object_type: blu_code_skill
category: source_truth
subcategory: debugging
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- runtime
- debugging
- route_first

## Objective
Separate written contracts from observed hosted behavior.

## Trigger
A behavior is wrong even though source/spec appears correct.

## Steps / Flow
1. Record the exact observed output.
2. Classify whether it proves route fallthrough, wrong owner, missing state, skipped support, skipped renderer, or invalid print.
3. Do not claim the gate/library ran unless output or real trace proves it.
4. Fix the earliest proven failed step first.

## Acceptance Checks
- Observed output is quoted exactly.
- The fix targets the earliest failed step.
- No downstream rewrite is attempted before route/owner proof.

## Notes
Direct Mood lesson: swatch mapping was not the first failure when `/mood` printed conversational prose.
