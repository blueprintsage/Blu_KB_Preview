# Split Class Interface And Implementation

**Object ID:** AP-CPP-015  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** architecture_design  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** classes, modularity, headers  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.145-220; evidence: text  

## Objective

Organize a growing class so users see the contract before internals.

## Steps / Flow

1. Identify public API.
2. Place declarations where users can see them.
3. Move implementation details away from interface.
4. Keep representation private.
5. Build a small caller using only the interface.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.
