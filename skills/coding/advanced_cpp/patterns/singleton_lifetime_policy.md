# Singleton Lifetime Policy

## Object Type
pattern

## Category
coding

## Subcategory
advanced_cpp

## Stage Binding
3 rough

## Lane Fit
skill

## Foundation Role
advanced

## Tags
- singleton
- lifetime
- threading
- modernization

## Pattern Rule
**IF** a unique process-wide object is truly required,  
**THEN** define creation, destruction, and thread-safety policies up front,  
**ELSE** global access turns into hidden coupling.

## Do
- Prefer dependency injection or scoped services first.
- Use function-local statics only when lifetime is simple.
- Document shutdown behavior and cross-singleton dependencies.

## Don't
- Do not use singleton to avoid passing a dependency.
- Do not rely on destruction order across translation units.

## Checklist
- Uniqueness is required, not convenient.
- Shutdown behavior is safe.
- Test seams exist despite global reach.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 127, 128, 132, 136, 143, 146
