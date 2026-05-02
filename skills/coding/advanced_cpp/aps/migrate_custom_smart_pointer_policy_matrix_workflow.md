# Migrate Custom Smart Pointer Policy Matrix Workflow

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
- smart_pointers
- ownership
- migration

## Objective
Translate a custom smart pointer design into modern ownership vocabulary without losing important semantic axes.

## Steps / Flow
1. Identify ownership: unique, shared, weak, intrusive, copied, or observed.
2. Identify null behavior: allowed, checked, repaired, or forbidden.
3. Identify conversion behavior: implicit, explicit, or blocked.
4. Identify storage behavior: raw pointer, handle, offset, or external reference.
5. Replace ordinary cases with standard smart pointers.
6. Keep custom wrappers only for nonstandard axes.
7. Test conversions, destruction, and threaded use separately.

## Success Check
- Most ordinary ownership uses standard types.
- Any custom behavior has a named reason.
- Null and conversion rules are visible at the API boundary.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 152, 157, 166, 178, 185
