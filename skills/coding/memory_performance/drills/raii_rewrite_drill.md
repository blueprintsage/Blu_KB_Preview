# RAII Rewrite Drill

**Object ID:** DRL-CPP-010  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** raii, vector, modern_cpp  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.74-84; evidence: text  

## Practice Task

Rewrite a raw dynamic array example into std::vector.

## Target Skill

Modernization and ownership.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Start from new[]/delete[] code.
2. Replace pointer and length with std::vector.
3. Remove manual delete.
4. Run equivalent loop.

## Success Check

- No raw owning pointer remains.
- Behavior is preserved.

## Common Failures

- Keeping both vector and raw delete.
- Changing indexing semantics accidentally.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
