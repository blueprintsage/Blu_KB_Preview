# Type-to-Type Mapping

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
- type_traits
- templates
- compile_time

## Pattern Rule
**IF** a function must choose behavior from a type without constructing that type,  
**THEN** use a type tag or standard type trait,  
**ELSE** runtime dummy objects leak into a compile-time decision.

## Do
- Prefer `std::type_identity`, traits, or constrained overloads in modern C++.
- Keep tag objects empty and unowned.
- Use type tags to make overload intent explicit.

## Don't
- Do not allocate or default-construct just to select a type path.
- Do not use tag dispatch when a concept or overload is clearer.

## Checklist
- The decision really belongs at compile time.
- No dummy runtime state is required.
- The selected overload is readable from the call site or wrapper.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 39, 40, 41
