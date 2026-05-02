# Const Reference Performance Drill

**Object ID:** DRL-CPP-015  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** performance, const, references  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; p.90; evidence: text  

## Practice Task

Compare signatures that pass a large vector by value vs const reference.

## Target Skill

Copy cost awareness.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Write two function signatures.
2. Reason about copy behavior.
3. Benchmark or inspect compiler behavior if possible.
4. Choose the correct signature for read-only use.

## Success Check

- Can explain why const reference avoids copying.
- No accidental mutation.

## Common Failures

- Optimizing before understanding semantics.
- Using reference when ownership is needed.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
