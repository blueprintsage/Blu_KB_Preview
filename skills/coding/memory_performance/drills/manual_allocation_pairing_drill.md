# Manual Allocation Pairing Drill

**Object ID:** DRL-CPP-009  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** memory, allocation, raii  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.75-81; evidence: text  

## Practice Task

Given allocation snippets, match them to the correct deallocation snippets.

## Target Skill

Memory ownership hygiene.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. List malloc/calloc/new/new[].
2. List free/delete/delete[].
3. Pair each correctly.
4. Mark invalid mixed pairs.

## Success Check

- All pairs correct.
- Mixed families rejected.

## Common Failures

- free(new T).
- delete malloc'd memory.
- delete instead of delete[].

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
