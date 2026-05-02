# Interface Before Implementation Class Teaching

object_id: pat_ppp_interface_before_implementation_class_teaching
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
- source_pages: 9
- evidence_type: text_layer
- transformation: paraphrased_learning_object

## Objective

Teach classes as responsibility boundaries before data containers.

## Pattern Rule

IF learners are building a class THEN identify valid operations, invariants, and error behavior before exposing representation.

## Steps / Flow

1. Name the type's responsibility.
2. List public operations.
3. Write invariants and invalid states.
4. Hide representation details.
5. Add helpers only when they support the interface.

## Success Check

- The class can reject invalid state.
- Users can rely on the interface without knowing fields.

## Modernization

Modernize dated C++ syntax and tooling while preserving the transferable design or teaching move.

## Notes

Derived as a transformed PASS object from the source. Use the idea in your own words; do not copy source examples or prose verbatim.
