# PDE Responsibility Map Drill

**Object ID:** DRL-CPP-034  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** language_contexts/cpp/cpp_numerics  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** pde, architecture, responsibility_map, numerics  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.321-349; evidence: text  

## Practice Task

Map a PDE simulator into separate responsibilities before sketching classes.

## Target Skill

Separating numerical model structure from implementation objects.

## Setup

Use a small PDE scenario with a grid, field values, time stepping, coefficients, and boundary behavior.

## Instructions

1. List the data responsibilities.
2. List the algorithm responsibilities.
3. List the boundary and configuration responsibilities.
4. Assign each responsibility to grid, field, simulator, solver, or boundary-condition roles.
5. Identify any role that is doing too much.

## Success Check

- Grid, field, simulator, and boundary behavior are not collapsed into one object.
- Dependencies point from high-level orchestration to lower-level data structures.
- The design can be tested in pieces.

## Common Failures

- Putting all PDE logic in one solver class.
- Hiding boundary conditions in ad hoc branches.
- Letting storage layout decide the public model.

## Notes

This drill was merged as a distinct practice object after duplicate lecture-level material was rejected or absorbed.

## Modernization

- Use a current compiler/toolchain and modern C++ defaults unless the exercise is explicitly about legacy mechanics.
