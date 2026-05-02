# Object Factory Registration Map

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
- factory
- runtime_dispatch
- polymorphism

## Pattern Rule
**IF** clients choose concrete types from runtime data,  
**THEN** register creators in a factory keyed by stable identifiers,  
**ELSE** construction logic spreads through switch statements and conditionals.

## Do
- Keep the product interface separate from the creation registry.
- Validate unknown identifiers at the boundary.
- Prefer explicit registration over hidden static initialization when order matters.

## Don't
- Do not make the factory own business logic after construction.
- Do not use strings as keys without validation or collision rules.

## Checklist
- Concrete types register one creation path.
- Unknown keys fail safely.
- Ownership of returned objects is clear.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 187, 188, 190, 194, 198, 203
