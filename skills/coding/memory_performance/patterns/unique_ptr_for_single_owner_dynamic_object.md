# unique_ptr for Single Owner Dynamic Object

object_id: unique_ptr_for_single_owner_dynamic_object
object_type: pattern
category: coding
subcategory: memory_performance
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- modern_cpp
- unique_ptr
- memory_management
- raii
cross_links:
- related_to: skills/coding/memory_performance
- related_to: skills/coding/testing_validation
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 530-581
- evidence_type: text_layer
confidence: high

## Objective
Use single-owner smart pointers when dynamic allocation is necessary and ownership should not be shared.

## Steps / Flow
1. Avoid dynamic allocation unless lifetime requires it.
2. Use automatic storage or containers first.
3. When a heap object has one owner, store it in unique_ptr.
4. Transfer ownership with move semantics rather than raw pointer copying.
5. Expose non-owning access without transferring deletion responsibility.

## Notes
Gaddis introduces unique_ptr as a C++11 memory-safety upgrade. PASS merges that into modern RAII guidance.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
