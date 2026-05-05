# Route-First Acceptance Tests

object_id: route_first_acceptance_tests
object_type: blu_code_skill
category: testing
subcategory: commands
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- testing
- acceptance
- routing

## Objective
Test command systems in the same order they execute.

## Trigger
Any command or route fix.

## Steps / Flow
1. Test command root recognized.
2. Test each subcommand routes to expected owner.
3. Test state commit for mutating commands.
4. Test support call/output for read/render commands.
5. Test invalid subcommand fails closed.
6. Test ordinary-turn behavior separately.

## Acceptance Checks
- Tests identify route vs render failures.
- A passing renderer test is not accepted if command route is unproven.
- Regression samples are included in BluCode after breakage.

## Reference Inputs
- PASS testing_validation skills: acceptance tests before implementation
