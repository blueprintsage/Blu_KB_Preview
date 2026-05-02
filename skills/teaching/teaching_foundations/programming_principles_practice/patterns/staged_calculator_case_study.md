# Staged Calculator Case Study

object_id: pat_ppp_staged_calculator_case_study
object_type: pattern
category: teaching
subcategory: teaching_foundations/programming_principles_practice
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
- source_pages: 6-7
- evidence_type: text_layer
- transformation: paraphrased_learning_object

## Objective

Teach program construction by repeatedly improving one small interpreter-like program.

## Pattern Rule

IF learners need to understand program growth THEN use one staged case study where tokens, grammar, errors, variables, and cleanup arrive as needed.

## Steps / Flow

1. Start with a tiny working calculator.
2. Introduce tokens as named input units.
3. Write grammar rules before implementation details.
4. Map each grammar rule to a function.
5. Add variables and error recovery after the core loop works.

## Success Check

- Each stage runs before the next is added.
- Refactoring is visible, not hidden.

## Modernization

Modernize dated C++ syntax and tooling while preserving the transferable design or teaching move.

## Notes

Derived as a transformed PASS object from the source. Use the idea in your own words; do not copy source examples or prose verbatim.
