# Object-Based Vs Object-Oriented Design

**Object ID:** PAT-CPP-104  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** language_contexts/cpp/cpp_oop  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** oop, object_based, class_design, numerics  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.132-204, 277-320; evidence: text  

## Pattern Rule

**IF** a design uses classes only to package data and operations  
**THEN** treat it as object-based until substitution, hierarchy, or runtime polymorphism is actually needed  
**ELSE** force inheritance into every class merely because the language supports it  

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

This pattern separates useful class encapsulation from full object-oriented hierarchy design.

## Modernization

- Treat older C/C++ examples as mechanics demonstrations first.
- Prefer standard containers, RAII, type-safe interfaces, current build tooling, and explicit tests for production use.

## Variants


### Variant: Object-Based Numeric Type

**Variant Axis:** design depth  
**Use When:** small value-like or container-like types  
**IF** a class only needs invariants and operations  
**THEN** keep it concrete and simple  
**ELSE** invent a base class without substitutable behavior


### Variant: Object-Oriented Solver Family

**Variant Axis:** design depth  
**Use When:** multiple algorithms share an interface  
**IF** callers must choose among interchangeable methods  
**THEN** introduce an interface or base role  
**ELSE** duplicate orchestration for every solver

