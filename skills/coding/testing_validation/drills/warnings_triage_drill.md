# Warnings Triage Drill

**Object ID:** DRL-CPP-028  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** testing_validation  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** warnings, debugging  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.43-44; evidence: text  

## Practice Task

Given a warning log, classify each warning as missing declaration, conversion, unused, or unsafe API.

## Target Skill

Diagnostic triage.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Read warning text.
2. Classify type.
3. Identify code location.
4. Fix one warning at a time.

## Success Check

- Every warning has an action.
- Final build is clean.

## Common Failures

- Batch-changing without cause.
- Ignoring warnings because binary runs.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
