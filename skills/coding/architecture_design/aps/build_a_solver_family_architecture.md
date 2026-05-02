# Build A Solver Family Architecture

**Object ID:** AP-CPP-020  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** architecture_design  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** oop, solvers, factory  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.290-350; evidence: text  

## Objective

Model a family of numerical solvers using interfaces, concrete implementations, and selection boundaries.

## Steps / Flow

1. Identify shared solver responsibility.
2. Define interface/base contract.
3. Implement concrete solver variants.
4. Centralize selection/configuration.
5. Keep problem model separate from solver implementation.
6. Test with at least two solver choices.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.
