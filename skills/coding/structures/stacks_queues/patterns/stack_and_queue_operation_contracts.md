# Stack and Queue Operation Contracts

object_id: stack_and_queue_operation_contracts
object_type: pattern
category: coding
subcategory: structures/stacks_queues
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- stacks
- queues
- adt
- data_structures
cross_links:
- related_to: skills/coding/structures
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 1094-1151
- evidence_type: text_layer
confidence: high

## Objective
Teach stacks and queues through the operation contract before implementation details.

## Steps / Flow
1. Define the allowed operations.
2. Name the ordering rule: LIFO for stack, FIFO for queue.
3. State empty/full behavior.
4. Choose static, dynamic, or STL-backed representation.
5. Test operation sequences rather than isolated calls only.

## Notes
The source presents stacks and queues as ADTs with implementation variants. PASS keeps the contract-first pattern.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
