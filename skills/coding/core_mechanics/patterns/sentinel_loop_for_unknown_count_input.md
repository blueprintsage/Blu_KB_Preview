# Sentinel Loop for Unknown Count Input

object_id: sentinel_loop_for_unknown_count_input
object_type: pattern
category: coding
subcategory: core_mechanics
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- loops
- sentinel
- input_processing
- beginner_programming
cross_links:
- related_to: skills/coding/core_mechanics
- related_to: skills/coding/input_output
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 258-329
- evidence_type: text_layer
confidence: high

## Objective
Use a sentinel value when input length is unknown and the stream itself does not define the stopping point.

## Steps / Flow
1. Choose a sentinel that cannot be mistaken for valid data.
2. Read the first value before entering the loop or use a guarded loop body.
3. Process only non-sentinel values.
4. Prompt clearly so the user knows how to stop.
5. Test with zero, one, and many data values.

## Notes
The loops chapter builds from counters to sentinels and file-driven loops. This object keeps the decision rule for sentinel loops.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
