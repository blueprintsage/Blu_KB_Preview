# Solver Family Classification Drill

**Object ID:** DRL-CPP-024  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** architecture_design  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** oop, factory, solvers  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.290-350; evidence: text  

## Practice Task

Classify solver examples as base interface, concrete solver, problem model, or factory.

## Target Skill

OOP architecture recognition.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Read a solver design snippet.
2. Mark each role.
3. Explain dependency direction.
4. Identify where runtime choice belongs.

## Success Check

- Roles are correctly assigned.
- No class owns too many roles.

## Common Failures

- Putting all logic in base class.
- Factory doing solver work.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
