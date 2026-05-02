# Policy Composition Matrix

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
- testing
- combinatorics

## Pattern Rule
**IF** template policy dimensions create many possible concrete types,  
**THEN** define valid and invalid combinations explicitly,  
**ELSE** the library appears flexible while hiding unsafe mixtures.

## Do
- Identify orthogonal policy axes.
- Name incompatible combinations early.
- Provide aliases for common safe combinations.
- Test representative cross-products, not only the defaults.

## Don't
- Do not pretend all combinations are meaningful.
- Do not let a huge parameter list become the public teaching surface.

## Checklist
- Each axis has a reason to vary.
- Incompatible choices are rejected or documented.
- Defaults are safe for ordinary users.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 26, 27, 28, 29
