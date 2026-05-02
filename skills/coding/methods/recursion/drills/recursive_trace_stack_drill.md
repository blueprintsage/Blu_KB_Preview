# Recursive Trace Stack Drill

object_id: recursive_trace_stack_drill
object_type: drill
category: coding
subcategory: methods/recursion
stage_binding: 2 practice
lane_fit: both
foundation_role: foundation
tags:
- recursion
- debugging
- trace
- call_stack
cross_links:
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
Make recursive execution visible by drawing one frame per call.

## Steps / Flow
1. Pick a small input.
2. Draw a frame for each call with its argument values.
3. Mark when the base case is reached.
4. Return through the frames in reverse order.
5. Compare the drawn result with program output.

## Notes
The source uses visual tracing for recursion. PASS keeps the method as a reusable drill.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
