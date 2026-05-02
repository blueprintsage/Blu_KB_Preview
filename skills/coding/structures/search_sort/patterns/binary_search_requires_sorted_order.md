# Binary Search Requires Sorted Order

object_id: binary_search_requires_sorted_order
object_type: pattern
category: coding
subcategory: structures/search_sort
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- binary_search
- searching
- sorting
- preconditions
cross_links:
- related_to: skills/coding/structures
- related_to: skills/coding/testing_validation
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 488-529
- evidence_type: text_layer
confidence: high

## Objective
Make sorted order an explicit precondition before using binary search.

## Steps / Flow
1. State the ordering key.
2. Verify or construct sorted order before searching.
3. Compare against the middle item.
4. Discard the half that cannot contain the target.
5. Test found, not-found, first, last, and empty cases.

## Notes
The search/sort chapters pair algorithm choice with data preconditions. PASS keeps the precondition as the skill.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
