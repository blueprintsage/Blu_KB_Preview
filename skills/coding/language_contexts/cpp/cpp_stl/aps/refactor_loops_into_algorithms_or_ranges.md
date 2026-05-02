# Refactor Loops Into Algorithms Or Ranges

**Object ID:** AP-CPP-017  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** language_contexts/cpp/cpp_stl  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** stl, algorithms, ranges  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.230-260; evidence: text  

## Objective

Convert hand-written traversal into clearer standard-library use where it improves intent.

## Steps / Flow

1. Identify the loop’s actual operation.
2. Check whether standard algorithm/range expresses it.
3. Rewrite safely.
4. Preserve mutation/copy behavior.
5. Keep raw loop if it is clearer or performance-critical.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.
