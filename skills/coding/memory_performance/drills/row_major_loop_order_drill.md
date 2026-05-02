# Row-Major Loop Order Drill

**Object ID:** DRL-CPP-008  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** cache, matrix, performance  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.70-73; evidence: text  

## Practice Task

Write two nested loops over a matrix and identify which one is cache-friendly for row-major storage.

## Target Skill

Memory-layout performance.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Create MxN matrix access examples.
2. Make one row-major friendly.
3. Make one column-jumping.
4. Explain which index varies fastest.

## Success Check

- Correctly identifies row-major traversal.
- Can describe why the other jumps.

## Common Failures

- Treating all nested loops as equivalent.
- Ignoring storage order.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
