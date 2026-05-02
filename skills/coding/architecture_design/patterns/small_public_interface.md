# Small public interface

## Object Type
pattern

## Category
coding

## Subcategory
architecture_design

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
**IF** designing a class,  
**THEN** expose only stable operations,  
**ELSE** every public member becomes permanent coupling.

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


### Variant absorbed: Do-it-all interface failure
Adds a warning from policy-based design: broad configurable interfaces create syntactically valid but semantically invalid combinations. Split independent choices instead. Source: Modern C++ Design, pp. 17-18.


## PASS Variant Absorption — Boost C++ Application Development Cookbook

- Absorbed variant: Boost.Variant visitor exhaustiveness
- Absorbed as: variant/refinement note
- Source handling: transformed idea only; no source prose copied.
- Modernization: treat Boost-era mechanics as either standard-library migration targets or Boost-specific tools when the standard library still lacks equivalent coverage.
