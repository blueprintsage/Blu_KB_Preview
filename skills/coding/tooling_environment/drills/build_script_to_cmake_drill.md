# Build Script To CMake Drill

**Object ID:** DRL-CPP-016  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** tooling_environment  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** cmake, build, modernization  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.33-42; evidence: text  

## Practice Task

Modernize a shell compile script into a minimal CMake project.

## Target Skill

Build modernization.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Start with one g++ command.
2. Create CMakeLists.txt.
3. Set C++ standard.
4. Add executable target.
5. Build in an out-of-source directory.

## Success Check

- Project builds cleanly.
- No hard-coded local-only compile script is required.

## Common Failures

- Global compiler flags only.
- No target definition.
- In-source build clutter.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
