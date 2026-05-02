# Header Failure Drill

**Object ID:** DRL-CPP-002  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** testing_validation  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** headers, warnings, debugging  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.26-27,43-44; evidence: text  

## Practice Task

Intentionally omit a required declaration, observe the warning/error, then fix it.

## Target Skill

Compiler diagnostics and include discipline.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Start from a tiny function call.
2. Remove the direct include.
3. Build with warnings.
4. Record the diagnostic.
5. Restore the direct include.

## Success Check

- Can explain the missing declaration.
- Final build is warning-clean.

## Common Failures

- Treating successful link as correctness.
- Ignoring warnings.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
