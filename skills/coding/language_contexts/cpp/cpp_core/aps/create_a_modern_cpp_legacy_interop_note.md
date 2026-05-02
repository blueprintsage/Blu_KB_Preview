# Create A Modern C++ Legacy-Interop Note

**Object ID:** AP-CPP-022  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** language_contexts/cpp/cpp_core  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** interop, legacy, modern_cpp  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.9-13,59-67; evidence: text  

## Objective

Document when to keep legacy C/C++ interop patterns and when to modernize them.

## Steps / Flow

1. Identify interop requirement.
2. Keep C ABI or FILE* only where necessary.
3. Wrap legacy boundary in safe modern code.
4. Keep modern C++ inside the boundary.
5. Document ownership and error behavior.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.
