# Compile-Time Convertibility Gate

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
- static_checking

## Pattern Rule
**IF** a generic operation assumes a type relationship,  
**THEN** encode that relationship with traits, constraints, or `static_assert`,  
**ELSE** the error appears later and farther from the cause.

## Do
- Use standard traits such as `std::is_convertible` and `std::is_base_of`.
- Prefer concepts when the requirement is part of the public template contract.
- Put the diagnostic near the template boundary.

## Don't
- Do not let a deep substitution failure be the first explanation.
- Do not overconstrain types beyond the real operation need.

## Checklist
- The required relationship is named.
- Invalid use fails before runtime.
- The diagnostic tells the caller what to change.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 42, 43, 44
