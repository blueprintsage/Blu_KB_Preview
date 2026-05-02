# File Transform Utility Drill

**Object ID:** DRL-CPP-003  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** input_output  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** file_io, pipeline  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.45-50; evidence: text  

## Practice Task

Write a program that reads x y pairs and emits x f(y) pairs.

## Target Skill

File I/O pipeline and loop validation.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Define CLI contract: infile outfile.
2. Open input and output.
3. Read records using the read result as loop condition.
4. Apply a pure transform function.
5. Write formatted output.

## Success Check

- Rejects missing filenames.
- Handles EOF cleanly.
- Output has the expected number of records.

## Common Failures

- Reading past EOF.
- No file-open validation.
- Transformation buried in I/O setup.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
