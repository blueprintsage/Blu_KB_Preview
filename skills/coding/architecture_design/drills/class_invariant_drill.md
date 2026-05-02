# Class Invariant Drill

**Object ID:** DRL-CPP-018  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** architecture_design  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** classes, invariants, oop  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.145-190; evidence: text  

## Practice Task

Design a small numeric type whose constructor guarantees valid state.

## Target Skill

Class design.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Choose a tiny domain type.
2. Make representation private.
3. Validate in constructor.
4. Add public methods that preserve invariant.

## Success Check

- Invalid state cannot be created through public API.
- Methods preserve the invariant.

## Common Failures

- Public data allows invalid mutation.
- Constructor leaves object half-initialized.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
