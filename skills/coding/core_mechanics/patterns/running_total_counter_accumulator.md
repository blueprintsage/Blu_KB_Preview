# Running Total Counter Accumulator

object_id: running_total_counter_accumulator
object_type: pattern
category: coding
subcategory: core_mechanics
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- loops
- accumulators
- counters
- state_update
cross_links:
- related_to: skills/coding/core_mechanics
- related_to: skills/coding/testing_validation
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
Separate count, total, and derived average so loop state stays readable and testable.

## Steps / Flow
1. Initialize counters and totals before the loop.
2. Update the count only for accepted records.
3. Update the total with the value being accumulated.
4. Compute averages after the loop unless a running average is required.
5. Test empty input separately to avoid division by zero.

## Notes
The source uses counters, running totals, and averages as core loop applications. This object generalizes the pattern.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
