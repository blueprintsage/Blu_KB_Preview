# Spiral Case Study Project

object_id: spiral_case_study_project
object_type: pattern
category: teaching
subcategory: teaching_foundations
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- teaching
- case_study
- project_sequence
- curriculum_design
cross_links:
- related_to: skills/teaching/teaching_foundations
- related_to: skills/coding/architecture_design
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 23-25
- evidence_type: text_layer
confidence: high

## Objective
Grow one realistic project across chapters so each new concept adds visible capability.

## Steps / Flow
1. Choose a project domain with persistent state and obvious user tasks.
2. Start with a tiny console version.
3. Add each new language feature only when it solves a real project need.
4. Keep earlier behavior working as the project grows.
5. Use the project to review integration, not only isolated syntax.

## Notes
The book’s recurring bookstore software project shows a long-running project as a teaching spine. PASS converts that into a curriculum pattern.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.

## Absorbed Variants

- PPP variant: the calculator program works as a smaller spiral project where tokens, grammar, variables, and recovery are added only after the previous stage runs.
