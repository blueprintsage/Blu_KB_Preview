# Design Function Signatures For Data Flow

**Object ID:** AP-CPP-010  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** architecture_design  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** api_design, functions, const  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.88-91; evidence: text  

## Objective

Choose value, reference, const reference, and pointer parameters based on intent.

## Steps / Flow

1. Classify each parameter as input, output, inout, optional, or owning.
2. Use value for cheap copies.
3. Use const reference for large read-only objects.
4. Use mutable reference for required mutation.
5. Use pointer/optional contract when absence matters.
6. Name functions to expose mutation.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.


## PASS Variant Absorption — Boost C++ Application Development Cookbook

- Absorbed variant: Boost.Tuple to structured binding migration
- Absorbed as: variant/refinement note
- Source handling: transformed idea only; no source prose copied.
- Modernization: treat Boost-era mechanics as either standard-library migration targets or Boost-specific tools when the standard library still lacks equivalent coverage.
