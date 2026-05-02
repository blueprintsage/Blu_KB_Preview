# RAII resource handle

## Object Type
pattern

## Category
coding

## Subcategory
memory_performance

## Stage Binding
2 block

## Lane Fit
skill

## Foundation Role
foundation

## Tags
- cpp
- modern_cpp
- pattern_recognition
- stroustrup

## Cross Links
- related_to: skills/coding/language_contexts/cpp/
- supports: skills/coding/

## Pattern Rule
**IF** a resource must be acquired and released,  
**THEN** bind it to object lifetime,  
**ELSE** leaks and partial cleanup paths multiply.

## Do
- Apply the rule at the smallest useful scope.
- Prefer standard, type-safe C++ expression.
- Preserve the primary skill goal.

## Don't
- Convert the rule into ceremony.
- Let a secondary concern override the main design intent.

## Checklist
- The condition is present.
- The action improves correctness, clarity, or performance.
- The fallback prevents overuse.

## Variants

### Variant: Legacy Codebase
**IF** the same pattern appears in pre-C++11 or C-style code  
**THEN** preserve behavior while modernizing the interface  
**ELSE** use the modern base form directly

## Reference
- Source: The C++ Programming Language, 4th Edition
- Author: Bjarne Stroustrup
- Publish Date: 2013
- Evidence Type: text


## PASS Variant Absorption — Boost C++ Application Development Cookbook

- Absorbed variant: Boost scope-exit cleanup as RAII variant
- Absorbed as: variant/refinement note
- Source handling: transformed idea only; no source prose copied.
- Modernization: treat Boost-era mechanics as either standard-library migration targets or Boost-specific tools when the standard library still lacks equivalent coverage.

## Absorbed Variants

- PPP variant: teach RAII through a tiny container/resource handle before relying on the standard library, so cleanup becomes a property of object lifetime rather than a memorized cleanup step.
