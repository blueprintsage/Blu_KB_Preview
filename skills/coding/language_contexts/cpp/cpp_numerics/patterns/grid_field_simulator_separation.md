# Grid Field Simulator Separation

**Object ID:** PAT-CPP-105  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** language_contexts/cpp/cpp_numerics  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** pde, grid, simulation, architecture  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.321-349; evidence: text  

## Pattern Rule

**IF** a numerical simulator has mesh structure, stored values, and time/update logic  
**THEN** separate grid, field, and simulator responsibilities  
**ELSE** let one object own geometry, data, update policy, and boundary behavior all at once  

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

This keeps numerical architecture readable and testable as models grow.

## Modernization

- Treat older C/C++ examples as mechanics demonstrations first.
- Prefer standard containers, RAII, type-safe interfaces, current build tooling, and explicit tests for production use.

## Variants


### Variant: Small Teaching Example

**Variant Axis:** scale  
**Use When:** introducing the idea  
**IF** the model is tiny  
**THEN** name the roles even if they live in one file  
**ELSE** pretend the roles do not exist


### Variant: Growing Simulator

**Variant Axis:** scale  
**Use When:** the model has multiple fields, dimensions, or update rules  
**IF** responsibilities change at different rates  
**THEN** split the roles into separate types or modules  
**ELSE** keep expanding one monolithic simulator

