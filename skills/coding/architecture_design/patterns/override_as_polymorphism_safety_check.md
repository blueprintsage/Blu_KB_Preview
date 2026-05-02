# override as Polymorphism Safety Check

object_id: override_as_polymorphism_safety_check
object_type: pattern
category: coding
subcategory: architecture_design
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- modern_cpp
- override
- polymorphism
- inheritance
cross_links:
- related_to: skills/coding/architecture_design
- related_to: skills/coding/testing_validation
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 922-1001
- evidence_type: text_layer
confidence: high

## Objective
Mark intended overrides so the compiler catches signature drift in derived classes.

## Steps / Flow
1. Declare virtual behavior in the base class.
2. In each derived class, add override to functions meant to replace base behavior.
3. Let compiler errors reveal misspellings, cv-mismatch, or parameter drift.
4. Use final only when further overriding should be forbidden.
5. Keep base destructors virtual when deleting through base pointers.

## Notes
The source treats override and final as C++11 improvements. PASS retains the safety rule in current C++ terms.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
