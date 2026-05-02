# Range-Based Loop for Whole Collection Walk

object_id: range_based_loop_for_whole_collection_walk
object_type: pattern
category: coding
subcategory: core_mechanics
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- modern_cpp
- range_for
- loops
- containers
cross_links:
- related_to: skills/coding/core_mechanics
- related_to: skills/coding/structures
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 406-487
- evidence_type: text_layer
confidence: high

## Objective
Use a range-based loop when every element of a collection should be visited in order and the index is not meaningful.

## Steps / Flow
1. Confirm the algorithm does not need the index.
2. Choose const reference for read-only large elements.
3. Choose reference when elements must be modified.
4. Use value only for cheap copies or deliberate snapshots.
5. Switch back to indexed loops when position matters.

## Notes
The edition highlights C++11 range-based loops. PASS stores the modern selection rule.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
