# Static Assert Type Traits Drill

## Object Type
drill

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
- practice
- type_traits
- static_assert

## Practice Task
Add compile-time diagnostics to a template that assumes a type relationship.

## Target Skill
Make template requirements explicit before implementation details fail.

## Setup
Use an example that requires inheritance, convertibility, default construction, or nothrow movement.

## Instructions
1. Name the type requirement.
2. Select the matching standard trait or concept.
3. Add `static_assert` or a requires-clause.
4. Write one passing and one failing instantiation.
5. Improve the failure message.

## Success Check
- The caller sees the requirement directly.
- The failure happens at the template boundary.
- The runtime body does not need defensive fake checks.

## Common Failures
- Checking a stronger condition than needed.
- Letting the compiler emit a deep substitution trace as the only feedback.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 32, 38, 42
