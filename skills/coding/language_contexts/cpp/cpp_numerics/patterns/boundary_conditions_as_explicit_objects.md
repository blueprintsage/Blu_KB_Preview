# Boundary Conditions As Explicit Objects

**Object ID:** PAT-CPP-106  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** language_contexts/cpp/cpp_numerics  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** pde, boundary_conditions, architecture, numerics  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.321-349; evidence: text  

## Pattern Rule

**IF** boundary behavior affects correctness or changes between simulations  
**THEN** represent boundary conditions as explicit responsibilities  
**ELSE** bury boundary rules in scattered conditionals inside the solver loop  

## Do

- Keep the rule tied to a concrete programming pressure.
- Prefer modern C++ defaults unless the goal is to expose mechanics.
- Separate the reusable design lesson from dated syntax.

## Don't

- Do not preserve legacy technique as a production recommendation.
- Do not add abstraction before the responsibility boundary is clear.
- Do not copy the source phrasing or examples as content.

## Checklist

- Is the condition explicit?
- Is the modern production form clear?
- Is the educational mechanics form labeled when needed?
- Is the boundary testable?

## Notes

This pattern adds a missing PDE-specific boundary-condition skill to the existing solver and class-boundary material.

## Modernization

- Treat older C/C++ examples as mechanics demonstrations first.
- Prefer standard containers, RAII, type-safe interfaces, current build tooling, and explicit tests for production use.

## Variants


### Variant: Fixed Boundary Rule

**Variant Axis:** boundary variability  
**Use When:** one rule is used throughout the exercise  
**IF** the rule is stable  
**THEN** keep it named and localized  
**ELSE** spread the rule through unrelated loops


### Variant: Swappable Boundary Rule

**Variant Axis:** boundary variability  
**Use When:** the user or experiment changes boundary behavior  
**IF** boundary behavior varies independently  
**THEN** make it configurable or polymorphic  
**ELSE** change solver internals for every boundary case

