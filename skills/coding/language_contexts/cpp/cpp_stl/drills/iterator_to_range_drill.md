# Iterator To Range Drill

**Object ID:** DRL-CPP-021  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** language_contexts/cpp/cpp_stl  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** ranges, iterators, modern_cpp  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.230-260; evidence: text  

## Practice Task

Modernize a raw iterator loop into a range-based loop or algorithm.

## Target Skill

Modern traversal.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Start with iterator loop.
2. Convert to range-for if simple.
3. Convert to algorithm/range if expressive.
4. Check behavior unchanged.

## Success Check

- Code is shorter and same behavior.
- No accidental copies of heavy elements.

## Common Failures

- Changing mutation semantics.
- Using range-for where index is needed.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
