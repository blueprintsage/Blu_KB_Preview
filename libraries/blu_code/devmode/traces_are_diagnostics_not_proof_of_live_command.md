# Traces Are Diagnostics Not Full Live Proof

object_id: traces_are_diagnostics_not_proof_of_live_command
object_type: blu_code_skill
category: devmode
subcategory: debug
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- devmode
- trace
- runtime

## Objective
Use DevMode traces correctly without overclaiming runtime behavior.

## Trigger
A trace target resolves but the live command still behaves incorrectly.

## Steps / Flow
1. Treat trace as source/route diagnostic only.
2. Compare trace path to live command path.
3. If live output contradicts trace, trust observed live output for regression classification.
4. Use trace to narrow target, not to declare feature fixed.

## Acceptance Checks
- Trace PASS does not override broken live output.
- Live command sample remains the acceptance test.
- Debug result is not decorated as success.
