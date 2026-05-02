# Choose a Dispatch Strategy Workflow

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
- visitor
- multimethods
- dispatch

## Objective
Pick virtual dispatch, visitor, double dispatch, or a table-driven dispatcher deliberately.

## Steps / Flow
1. Count the number of runtime objects that influence the operation.
2. Decide whether types, operations, or both change frequently.
3. Use normal virtual functions for one object and stable operations.
4. Use Visitor for stable types with changing operations.
5. Use acyclic Visitor when the type set is more open.
6. Use double dispatch or a multimethod table when two runtime types decide behavior.
7. Document missing-combination behavior.

## Success Check
- The chosen strategy matches the change axis.
- Missing handlers are testable.
- Dispatch cost is appropriate for the hot path.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 219, 230, 242, 260
