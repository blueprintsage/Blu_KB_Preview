# Audit Manual Memory Code

**Object ID:** AP-CPP-009  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** memory, audit, raii  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.75-83; evidence: text  

## Objective

Review legacy manual allocation code for leaks, mismatches, and modernization path.

## Steps / Flow

1. List allocation family for each resource.
2. List matching deallocation requirement.
3. Check early-exit paths.
4. Flag mixed malloc/new families.
5. Replace with RAII where possible.
6. Document remaining legacy constraints.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.
