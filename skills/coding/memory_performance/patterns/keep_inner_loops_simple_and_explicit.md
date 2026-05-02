# Keep Inner Loops Simple And Explicit

**Object ID:** PAT-CPP-102  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** performance, loops, numerics, profiling  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.244-276; evidence: text  

## Pattern Rule

**IF** a numeric hot path spends most time inside a small loop  
**THEN** keep that loop direct, readable, and measurement-friendly before adding abstraction  
**ELSE** bury the cost inside layered calls that cannot be inspected  

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

This pattern preserves the course’s low-level performance lesson while avoiding premature micro-optimization.

## Modernization

- Treat older C/C++ examples as mechanics demonstrations first.
- Prefer standard containers, RAII, type-safe interfaces, current build tooling, and explicit tests for production use.

## Variants


### Variant: Teaching Mechanics

**Variant Axis:** instructional form  
**Use When:** the goal is to expose what the machine is doing  
**IF** students need to understand memory traversal or arithmetic cost  
**THEN** write the loop explicitly and inspect it  
**ELSE** jump straight to a library abstraction


### Variant: Production Code

**Variant Axis:** production form  
**Use When:** the operation is standard and already well-covered by a library  
**IF** a standard algorithm or optimized library routine expresses the operation  
**THEN** prefer the tested library and benchmark only if needed  
**ELSE** hand-roll a loop without reason

