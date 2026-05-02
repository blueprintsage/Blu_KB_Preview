# Enriched Policy Interface

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
- policy_based_design
- interfaces
- compile_time

## Pattern Rule
**IF** only some policy implementations support an extra capability,  
**THEN** make that capability optional and use it only where selected,  
**ELSE** every policy is forced to carry dead interface weight.

## Do
- Treat enriched operations as additive.
- Keep the required policy surface small.
- Let missing optional operations fail at compile time when the caller asks for them.

## Don't
- Do not make all policies implement fake no-op features.
- Do not rely on optional functions without documenting the required policy shape.

## Checklist
- Required and optional surfaces are separate.
- Optional use has a clear fallback or compile-time failure.
- The host still works with minimal policies.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 23, 24, 25
