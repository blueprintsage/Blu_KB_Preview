# Find Classes from Problem Responsibilities

object_id: find_classes_from_problem_responsibilities
object_type: ap
category: coding
subcategory: architecture_design
stage_binding: 3 workflow
lane_fit: both
foundation_role: workflow
tags:
- oop
- class_design
- problem_analysis
- responsibilities
cross_links:
- related_to: skills/coding/architecture_design
- related_to: skills/teaching/teaching_foundations
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 742-841
- evidence_type: text_layer
confidence: high

## Objective
Derive a small class model from a problem statement without over-modeling.

## Steps / Flow
1. Underline nouns as candidate objects or data.
2. Underline verbs as candidate responsibilities.
3. Group responsibilities around the object that should own them.
4. Reject classes that only hold one trivial value unless they protect an invariant.
5. Sketch public operations before private fields.

## Notes
The source teaches finding classes and responsibilities after procedural foundations. PASS keeps the analysis workflow.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
