# Specialization Modern C++ Rule

## Object Type
pattern

## Category
coding

## Subcategory
language_contexts/cpp/cpp_core

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
**IF** older idioms appear in specialization,  
**THEN** prefer the modern standard-library or language facility,  
**ELSE** legacy style persists.

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
