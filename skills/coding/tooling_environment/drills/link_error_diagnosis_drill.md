# Link Error Diagnosis Drill

**Object ID:** DRL-CPP-017  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** tooling_environment  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** linking, debugging, build  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.33,40-41; evidence: text  

## Practice Task

Separate a compile error from a link error using a two-file example.

## Target Skill

Build mental model.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Create declaration and definition files.
2. Compile each object.
3. Omit one object during link.
4. Observe link error.
5. Add missing object and rebuild.

## Success Check

- Can name compile vs link stage.
- Can fix missing symbol linkage.

## Common Failures

- Changing headers to fix link-only issue.
- Not knowing which stage failed.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
