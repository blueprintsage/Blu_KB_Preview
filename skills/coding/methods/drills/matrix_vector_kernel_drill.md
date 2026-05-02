# Matrix Vector Kernel Drill

**Object ID:** DRL-CPP-013  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** methods  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** numerics, matrix, loops  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.68-87; evidence: text  

## Practice Task

Compute b=A*x for a small matrix and hand-check the result.

## Target Skill

Numerical loop correctness.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Initialize a 2x2 or 3x3 matrix.
2. Initialize x.
3. Compute b with nested loops.
4. Hand-calculate expected result.
5. Compare.

## Success Check

- All entries match expected values.
- Initialization and computation are separate.

## Common Failures

- Wrong loop bounds.
- Using uninitialized sum.
- Mixing row/column order.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
