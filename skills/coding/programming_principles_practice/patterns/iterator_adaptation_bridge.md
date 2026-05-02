# Iterator Adaptation Bridge

object_id: pat_ppp_iterator_adaptation_bridge
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
- source_pages: 20-21
- evidence_type: text_layer
- transformation: paraphrased_learning_object

## Objective

Adapt custom sequences to STL-style iteration before teaching algorithms broadly.

## Pattern Rule

IF code has a custom container THEN add begin/end iterator behavior so standard algorithms become usable.

## Steps / Flow

1. Identify traversal state.
2. Define iterator operations.
3. Expose begin/end.
4. Use find/copy/sort where valid.
5. Document iterator invalidation.

## Success Check

- At least one standard algorithm works.
- Iterator assumptions are named.

## Modernization

Modernize dated C++ syntax and tooling while preserving the transferable design or teaching move.

## Notes

Derived as a transformed PASS object from the source. Use the idea in your own words; do not copy source examples or prose verbatim.
