# Token Stream Boundary

object_id: pat_ppp_token_stream_boundary
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
- source_pages: 6
- evidence_type: text_layer
- transformation: paraphrased_learning_object

## Objective

Hide input mechanics behind a token-stream object so grammar code stays readable.

## Pattern Rule

IF parsing code mixes raw input with grammar decisions THEN introduce a token stream boundary with get/putback behavior.

## Steps / Flow

1. Define token type.
2. Create get operation.
3. Add one-token pushback if needed.
4. Keep grammar functions independent of raw input source.

## Success Check

- Grammar functions do not parse raw characters directly.
- The token boundary can be tested separately.

## Modernization

Modernize dated C++ syntax and tooling while preserving the transferable design or teaching move.

## Notes

Derived as a transformed PASS object from the source. Use the idea in your own words; do not copy source examples or prose verbatim.
