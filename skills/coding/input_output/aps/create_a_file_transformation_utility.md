# Create A File Transformation Utility

**Object ID:** AP-CPP-004  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** input_output  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** file_io, pipeline, cli  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.45-50; evidence: text  

## Objective

Build a command-line tool that reads xy records, transforms y, and writes xy records.

## Steps / Flow

1. Define usage: program infile outfile.
2. Open and validate files.
3. Write a pure transform function.
4. Read one record at a time.
5. Format output intentionally.
6. Close/let RAII close resources.
7. Test with a tiny known input.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.
