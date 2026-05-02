# Typelist as Static Type Sequence

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
- typelists
- metaprogramming
- variadic_templates

## Pattern Rule
**IF** a design must transform, search, or generate code from types,  
**THEN** represent those types as a static sequence,  
**ELSE** the type relationships scatter across overloads and special cases.

## Do
- Use variadic templates for new code.
- Keep operations pure at the type level: length, lookup, append, replace, unique.
- Convert Loki-style typelists into modern packs during modernization.

## Don't
- Do not keep recursive cons-style typelists when a pack expression is simpler.
- Do not use type metaprogramming where a runtime container is the true model.

## Checklist
- The members are types, not values.
- The operations are compile-time decisions.
- Modern pack syntax can replace historical scaffolding.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 56, 57, 58, 59, 60
