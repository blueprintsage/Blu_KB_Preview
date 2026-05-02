# Memory Leak Review Drill

**Object ID:** DRL-CPP-031  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** memory, audit, raii  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.74-83; evidence: text  

## Practice Task

Review a snippet for all allocation paths and release paths.

## Target Skill

Manual memory audit.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Mark each allocation.
2. Mark matching release.
3. Find early returns/exceptions.
4. Modernize to RAII where possible.

## Success Check

- Every path is accounted for.
- Modern replacement proposed.

## Common Failures

- Only checking normal path.
- Mixing allocation families.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
