# Modernize Legacy Shell Build To CMake

**Object ID:** AP-CPP-003  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** tooling_environment  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** cmake, modernization, build  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.34-42; evidence: text  

## Objective

Convert old compile-script practice into a repo-ready modern C++ build.

## Steps / Flow

1. Identify the old command’s source files, include paths, libraries, and flags.
2. Create CMakeLists.txt with target-based settings.
3. Set a current language standard.
4. Add executable/library targets.
5. Perform out-of-source build.
6. Replace local-only script assumptions with documented build steps.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.
