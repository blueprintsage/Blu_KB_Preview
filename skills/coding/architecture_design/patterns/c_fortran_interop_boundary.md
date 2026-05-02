# C And Fortran Interop Boundary

**Object ID:** PAT-CPP-103  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** architecture_design  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** interop, c, fortran, numerics, architecture  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.8-13, 244-276; evidence: text  

## Pattern Rule

**IF** a C++ program must call C or Fortran numerical code  
**THEN** isolate layout, calling convention, ownership, and error handling at a narrow boundary  
**ELSE** let foreign-language assumptions leak through the application model  

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

Merged as a distinct architecture pattern because the repo already had general hybrid-language guidance, but not the boundary hygiene for C/Fortran numerical interop.

## Modernization

- Treat older C/C++ examples as mechanics demonstrations first.
- Prefer standard containers, RAII, type-safe interfaces, current build tooling, and explicit tests for production use.

## Variants


### Variant: C Library Boundary

**Variant Axis:** foreign interface  
**Use When:** calling C APIs  
**IF** the dependency is C-style  
**THEN** wrap pointers, lengths, ownership, and status codes behind a small C++ adapter  
**ELSE** spread raw API calls throughout the application


### Variant: Fortran Kernel Boundary

**Variant Axis:** foreign interface  
**Use When:** calling Fortran numerics  
**IF** the dependency expects Fortran-style layout or conventions  
**THEN** document array order, indexing assumptions, and linkage in one adapter layer  
**ELSE** hide layout conversion in unrelated business logic

