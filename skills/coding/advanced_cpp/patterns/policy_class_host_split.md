# Policy Class Host Split

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
- host_class
- interfaces

## Pattern Rule
**IF** reusable behavior needs class-specific coordination,  
**THEN** keep primitives in policies and invariants in the host,  
**ELSE** policies become hidden owners of the design.

## Do
- Let policies expose narrow operations or associated types.
- Let the host call those operations in the correct order.
- Keep ownership, lifetime, and error behavior visible at the host boundary.

## Don't
- Do not let a policy silently print, allocate globally, or mutate unrelated state.
- Do not treat policy inheritance as permission to leak internals.

## Checklist
- The host can explain the whole object contract.
- A policy can be swapped without changing unrelated behavior.
- Policy-specific enrichments are optional, not required.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 20, 21, 22, 23
