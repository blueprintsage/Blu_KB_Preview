# Aggregation Before Inheritance

object_id: aggregation_before_inheritance
object_type: pattern
category: coding
subcategory: architecture_design
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- oop
- aggregation
- inheritance
- composition
cross_links:
- related_to: skills/coding/architecture_design
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 842-1001
- evidence_type: text_layer
confidence: high

## Objective
Prefer whole-part collaboration when objects need each other but do not form an is-a hierarchy.

## Steps / Flow
1. Ask whether the relationship is is-a or has-a.
2. Use aggregation/composition for has-a relationships.
3. Keep ownership and lifetime explicit.
4. Reserve inheritance for substitutable specialized types.
5. Test by asking whether a derived object can safely stand in for the base.

## Notes
The source separates aggregation, inheritance, and polymorphism. PASS turns that distinction into a selection rule.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
