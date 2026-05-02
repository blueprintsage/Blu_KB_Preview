# Design A Safe CLI Input Boundary

**Object ID:** AP-CPP-006  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** testing_validation  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** cli, validation, errors  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.25-31,46-48; evidence: text  

## Objective

Create a reusable input boundary for small command-line numerical programs.

## Steps / Flow

1. List required and optional arguments.
2. Validate count before access.
3. Convert text through a checked path.
4. Report usage and errors clearly.
5. Return correct status codes.
6. Cover no-arg, bad-arg, and valid-arg tests.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.
