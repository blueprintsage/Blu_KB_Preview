# Function Extraction Drill

**Object ID:** DRL-CPP-014  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** methods  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** functions, modularity  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.45-48,88-92; evidence: text  

## Practice Task

Take a monolithic example and split it into parse, process, and output functions.

## Target Skill

Modularity.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Identify responsibilities.
2. Extract one pure transform function.
3. Extract input validation.
4. Extract output function.
5. Keep main as orchestration.

## Success Check

- Main is short and readable.
- Each function has one responsibility.

## Common Failures

- Functions still mutate hidden globals.
- Names do not describe work.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
