# CLI Usage Test Drill

**Object ID:** DRL-CPP-029  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** testing_validation  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** testing, cli, errors  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.25-31,46-48; evidence: text  

## Practice Task

Write three tests for missing, invalid, and valid command-line input.

## Target Skill

Boundary testing.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Run with no args.
2. Run with non-numeric arg.
3. Run with valid arg.
4. Verify status and messages.

## Success Check

- All paths produce expected status.
- Invalid paths do not compute with garbage.

## Common Failures

- Only testing happy path.
- Printing errors to normal output only.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
