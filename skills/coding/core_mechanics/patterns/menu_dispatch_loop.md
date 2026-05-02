# Menu Dispatch Loop

object_id: menu_dispatch_loop
object_type: pattern
category: coding
subcategory: core_mechanics
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- menus
- control_flow
- input_validation
- program_structure
cross_links:
- related_to: skills/coding/testing_validation
- related_to: skills/coding/methods
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 180-405
- evidence_type: text_layer
confidence: high

## Objective
Keep a menu-driven program readable by separating display, validation, and action dispatch.

## Steps / Flow
1. Display menu choices from one function or block.
2. Read the user choice.
3. Validate the choice before dispatch.
4. Use a switch or clear if-chain to call one action per option.
5. Loop until the explicit quit option is selected.

## Notes
The decision and function chapters use menu-driven programs to combine branching, validation, and modular actions.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
