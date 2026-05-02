# Operator Semantics Drill

**Object ID:** DRL-CPP-019  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** testing_validation  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** operators, api_design  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.145-205; evidence: text  

## Practice Task

Given a numeric class, decide which operators are appropriate and test expected behavior.

## Target Skill

Operator design.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. List mathematically expected operations.
2. Implement one safe operator.
3. Write examples/tests.
4. Reject surprising overloads.

## Success Check

- Operator matches user expectation.
- Tests document semantics.

## Common Failures

- Overloading for cleverness.
- Side effects in arithmetic operators.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
