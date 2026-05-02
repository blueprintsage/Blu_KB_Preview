# Argv Memory Model Sketch

**Object ID:** DRL-CPP-006  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** core_mechanics  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** pointers, cli  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.56-57; evidence: text  

## Practice Task

Draw argv as an array of character pointers, then explain argv[0] and argv[1].

## Target Skill

Pointer and CLI mental model.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Sketch char** argv.
2. Label the array entries.
3. Label the strings pointed to by entries.
4. Explain why argv is char**.

## Success Check

- Correctly distinguishes pointer table from strings.
- Can explain argv[0].

## Common Failures

- Calling argv a single string.
- Losing the array-of-pointers model.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
