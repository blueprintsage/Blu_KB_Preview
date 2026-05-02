# Typelist to Variadic Pack Drill

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
- typelists
- variadic_templates

## Practice Task
Rewrite one Loki-style typelist operation as a modern variadic-template operation.

## Target Skill
Recognize historical metaprogramming scaffolding and translate it into modern C++ vocabulary.

## Setup
Choose length, contains, append, erase, or unique as the operation.

## Instructions
1. State the old typelist operation in plain language.
2. Write the modern type alias or template.
3. Add one accepted example.
4. Add one rejected or edge example.
5. Compare readability before and after.

## Success Check
- The result uses packs instead of recursive cons nodes.
- The operation remains compile-time only.
- The modern version preserves the original intent.

## Common Failures
- Recreating the old typelist under a new name.
- Losing edge cases such as empty lists or duplicate types.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 56, 60, 66, 73
