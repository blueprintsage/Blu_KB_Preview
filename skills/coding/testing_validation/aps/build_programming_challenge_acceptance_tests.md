# Build Programming Challenge Acceptance Tests

object_id: build_programming_challenge_acceptance_tests
object_type: ap
category: coding
subcategory: testing_validation
stage_binding: 3 workflow
lane_fit: both
foundation_role: workflow
tags:
- testing
- acceptance_tests
- programming_challenges
- beginner_programming
cross_links:
- related_to: skills/coding/testing_validation
- related_to: skills/teaching/teaching_foundations/beginner_programming
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 23-24
- evidence_type: text_layer
confidence: high

## Objective
Turn a programming exercise into concrete acceptance tests before implementation.

## Steps / Flow
1. Extract required inputs, outputs, and validation rules.
2. Create at least one normal case.
3. Create boundary cases around limits and empty input.
4. Create invalid-input cases when validation is required.
5. Run the implementation against the cases before declaring the exercise complete.

## Notes
Gaddis programming challenges commonly include validation rules and expected behavior. This AP makes those rules executable as tests.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.


## PASS Variant Absorption — Boost C++ Application Development Cookbook

- Absorbed variant: Boost.Test module shape
- Absorbed as: variant/refinement note
- Source handling: transformed idea only; no source prose copied.
- Modernization: treat Boost-era mechanics as either standard-library migration targets or Boost-specific tools when the standard library still lacks equivalent coverage.
