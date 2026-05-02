# Build Type-Level Selection Workflow

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
- type_traits
- compile_time
- workflow

## Objective
Move a type-dependent branch from runtime guessing into an explicit compile-time decision.

## Steps / Flow
1. State the exact type relation or property needed.
2. Check whether a standard trait already names it.
3. Use a constrained overload, tag dispatch, or `if constexpr`.
4. Put a `static_assert` near the boundary when invalid use is likely.
5. Add a tiny compile-time test for the intended accepted and rejected cases.

## Success Check
- Invalid type use fails before runtime.
- The diagnostic is near the caller-facing template.
- The runtime code no longer needs dummy type probes.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 38, 39, 40, 41, 42
