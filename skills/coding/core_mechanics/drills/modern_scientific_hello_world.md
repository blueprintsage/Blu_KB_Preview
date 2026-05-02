# Modern Scientific Hello World

**Object ID:** DRL-CPP-001  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** core_mechanics  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** cli, math, conversion  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.25-31; evidence: text  

## Practice Task

Build a small program that reads one numeric argument, computes sin(x), and prints the result.

## Target Skill

CLI input, numeric conversion, function call, output.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Create main with argc/argv.
2. Validate exactly one numeric argument.
3. Convert using a checked modern conversion path.
4. Call std::sin.
5. Print result with clear formatting.

## Success Check

- Invalid input is rejected.
- Valid input prints expected numeric result.
- Compiler warnings are clean.

## Common Failures

- Using atof blindly.
- No argument count check.
- Missing cmath include.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
