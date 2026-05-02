# Modernize Loki-Era Template Code Workflow

## Object Type
ap

## Category
coding

## Subcategory
advanced_cpp

## Stage Binding
4 final

## Lane Fit
skill

## Foundation Role
advanced

## Tags
- modern_cpp
- templates
- migration

## Objective
Preserve the design lesson from pre-modern template code while replacing historical machinery with safer current C++.

## Steps / Flow
1. Identify the design intent: constraint, dispatch, ownership, generation, or storage.
2. Separate intent from the historical technique.
3. Replace compile-time checks with `static_assert`, traits, or concepts.
4. Replace typelist recursion with variadic packs where possible.
5. Replace custom ownership with standard smart pointers unless a custom axis is still required.
6. Keep custom machinery only when it expresses a constraint the standard tool does not.
7. Add a note explaining what changed and why.

## Success Check
- The modern version is smaller or safer.
- The original architectural idea remains visible.
- No behavior is preserved merely for nostalgia.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 32, 42, 56, 152, 178
