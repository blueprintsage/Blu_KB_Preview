# BST Operation Invariant

object_id: bst_operation_invariant
object_type: pattern
category: coding
subcategory: structures/trees
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- binary_search_tree
- invariants
- data_structures
- recursion
cross_links:
- related_to: skills/coding/structures
- related_to: skills/coding/methods/recursion
reference:
- source_title: Starting Out with C++: From Control Structures through Objects
- author: Tony Gaddis
- publish_date: 2015
- edition: 8th
- media_type: textbook_pdf
- source_pages: 1186-1215
- evidence_type: text_layer
confidence: high

## Objective
Preserve the binary-search-tree ordering invariant across insertion, search, and deletion.

## Steps / Flow
1. State the ordering rule for left and right subtrees.
2. Use the rule to choose traversal direction.
3. When inserting, stop at the missing child position.
4. When deleting, handle leaf, one-child, and two-child cases separately.
5. After mutation, re-check the ordering invariant.

## Notes
The binary-tree chapter is captured as an invariant-preservation skill rather than a copied implementation.

## Modernization
Modernized into current C++ teaching practice without copying legacy source wording.
