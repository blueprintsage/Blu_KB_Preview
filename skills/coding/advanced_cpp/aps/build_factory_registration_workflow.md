# Build Factory Registration Workflow

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
- factory
- polymorphism
- workflow

## Objective
Create objects from runtime identifiers without scattering construction code.

## Steps / Flow
1. Define the product interface.
2. Choose a stable identifier type.
3. Register each creator in one registry.
4. Decide ownership of created objects.
5. Validate unknown identifiers at the factory boundary.
6. Keep construction separate from post-creation business behavior.
7. Add tests for duplicate registration and missing keys.

## Success Check
- All creators enter through one path.
- Unknown keys fail safely.
- Product ownership is explicit.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 187, 190, 194, 203
