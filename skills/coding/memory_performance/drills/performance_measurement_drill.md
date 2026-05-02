# Performance Measurement Drill

**Object ID:** DRL-CPP-022  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** performance, benchmarking  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.260-290; evidence: text  

## Practice Task

Time two matrix traversal orders on a moderately sized array.

## Target Skill

Measure before optimizing.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Implement row-friendly traversal.
2. Implement column-jumping traversal.
3. Time both consistently.
4. Explain result with storage order.

## Success Check

- Measurement setup is repeatable.
- Explanation mentions data layout.

## Common Failures

- Benchmarking too tiny a case.
- Changing multiple variables at once.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
