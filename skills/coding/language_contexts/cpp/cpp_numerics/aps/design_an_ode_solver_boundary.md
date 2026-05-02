# Design An ODE Solver Boundary

**Object ID:** AP-CPP-019  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** language_contexts/cpp/cpp_numerics  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** ode, interfaces, solvers  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.290-350; evidence: text  

## Objective

Separate ODE problem representation from solver execution.

## Steps / Flow

1. Define state and derivative function contract.
2. Define solver interface.
3. Implement one concrete solver.
4. Run on a simple known problem.
5. Swap solver without rewriting problem definition.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.
