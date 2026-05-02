# Parallel Arrays as Transition to Structures

object_id: parallel_arrays_as_transition_to_structures
object_type: pattern
category: coding
subcategory: structures/arrays
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- arrays
- structures
- beginner_programming
- data_modeling
cross_links:
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
Use parallel arrays only as a teaching bridge toward records, structs, or objects.

## Steps / Flow
1. Keep all parallel arrays the same length.
2. Use one index to refer to one logical entity across arrays.
3. Name the hidden record concept explicitly.
4. Refactor to a struct or class once fields belong together.
5. Reject parallel arrays when data can fall out of sync.

## Notes
The source teaches parallel arrays before structured data. PASS preserves the sequencing while marking the safer destination.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
