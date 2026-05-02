# Reduce Problem Then Call Self

object_id: reduce_problem_then_call_self
object_type: pattern
category: coding
subcategory: methods/recursion
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- recursion
- problem_solving
- base_case
- algorithm_design
cross_links:
- related_to: skills/coding/methods
- related_to: skills/coding/testing_validation/debugging
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 1152-1185
- evidence_type: text_layer
confidence: high

## Objective
Design recursive functions by proving the problem gets smaller and has a stop case.

## Steps / Flow
1. Write the base case first.
2. Define the smaller version of the same problem.
3. Do one unit of work before or after the recursive call.
4. Ensure each call moves toward the base case.
5. Trace a small input to verify termination and result assembly.

## Notes
The recursion chapter emphasizes reducing a problem and tracing calls. PASS stores the design rule.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
