# ODE Interface Sketch Drill

**Object ID:** DRL-CPP-023  
**Object Type:** drill  
**Category:** coding  
**Subcategory:** language_contexts/cpp/cpp_numerics  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** ode, interfaces, numerics  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.290-350; evidence: text  

## Practice Task

Sketch interfaces separating ODE problem definition from solver implementation.

## Target Skill

Numerical architecture.

## Setup

Use a small local C++ project and one source file.

## Instructions

1. Define problem function/state shape.
2. Define solver interface.
3. Show Euler/RK-style solver variants.
4. Keep equation out of solver core.

## Success Check

- Problem and solver are separable.
- Solver can be swapped.

## Common Failures

- Hardwiring equation in solver.
- No clear state type.

## Notes

Keep the drill short, repeatable, and measurable.

## Modernization

- Use current compiler/toolchain and modern C++ defaults.
