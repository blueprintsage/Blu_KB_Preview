# Recoverable Input Error Loop

object_id: pat_ppp_recoverable_input_error_loop
object_type: pattern
category: coding
subcategory: programming_principles_practice
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
confidence: high
tags:
- cpp
- programming_principles_practice
- pass
reference:
- source_title: Programming: Principles and Practice Using C++
- author: Bjarne Stroustrup
- publish_date: 2008
- media_type: textbook_pdf
- source_pages: 5,7,10
- evidence_type: text_layer
- transformation: paraphrased_learning_object

## Objective

Treat input failure as a loop state, not a crash-only condition.

## Pattern Rule

IF interactive input can fail THEN clear the bad state, discard or resync input, explain the problem, and continue only from a known boundary.

## Steps / Flow

1. Detect invalid input.
2. Report the boundary condition.
3. Discard to a recovery delimiter.
4. Resume at a known prompt.
5. Test repeated failures.

## Success Check

- The loop recovers without corrupting state.
- Repeated bad input does not hang.

## Modernization

Modernize dated C++ syntax and tooling while preserving the transferable design or teaching move.

## Notes

Derived as a transformed PASS object from the source. Use the idea in your own words; do not copy source examples or prose verbatim.
