# Multimethod Dispatch Strategy

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
- multimethods
- double_dispatch
- runtime_dispatch

## Pattern Rule
**IF** one virtual dispatch is not enough to choose behavior,  
**THEN** make the second dispatch strategy explicit,  
**ELSE** type checks scatter across the codebase.

## Do
- Use simple double dispatch for small, stable matrices.
- Use tables or maps when combinations are dynamic.
- Decide whether argument order is symmetric.
- Measure if dispatch speed is the real constraint.

## Don't
- Do not replace clear virtual design with a multimethod engine prematurely.
- Do not hide failed registrations as no-ops.

## Checklist
- The behavior truly depends on two runtime types.
- Missing combinations fail clearly.
- Symmetry and conversion rules are documented.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 242, 243, 244, 254, 260, 272
