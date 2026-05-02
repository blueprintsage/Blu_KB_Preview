# Bounds Risk as Default Array Assumption

object_id: bounds_risk_as_default_array_assumption
object_type: pattern
category: coding
subcategory: testing_validation
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- arrays
- bounds
- validation
- safety
cross_links:
- related_to: skills/coding/structures
- related_to: skills/coding/testing_validation
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
Treat every raw array index as unsafe until the valid range is proven.

## Steps / Flow
1. Name the legal index range.
2. Check loop start and stop values against that range.
3. Avoid deriving indexes from unchecked input.
4. Prefer containers with safer access where appropriate.
5. Test first, last, and just-outside indexes.

## Notes
The arrays chapter stresses that C++ raw arrays do not protect against out-of-range access. PASS modernizes that into a default safety posture.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
