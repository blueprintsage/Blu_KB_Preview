# Calculator Parser Incremental Refinement

object_id: pat_ppp_calculator_parser_incremental_refinement
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
- source_pages: 6-7
- evidence_type: text_layer
- transformation: paraphrased_learning_object

## Objective

Grow a parser by running each small stage before adding grammar depth.

## Pattern Rule

IF a parser is being taught or built from scratch THEN stabilize lexing, grammar functions, evaluation, and error recovery as separate increments.

## Steps / Flow

1. Tokenize first.
2. Implement the smallest expression grammar.
3. Add precedence one rule at a time.
4. Add variables only after expression evaluation works.
5. Keep tests for each stage.

## Success Check

- Each parser stage runs before the next is added.
- Tests cover precedence and invalid input.

## Modernization

Modernize dated C++ syntax and tooling while preserving the transferable design or teaching move.

## Notes

Derived as a transformed PASS object from the source. Use the idea in your own words; do not copy source examples or prose verbatim.
