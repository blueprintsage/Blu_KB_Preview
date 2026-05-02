# Design a Policy-Based Component Workflow

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
- policy_based_design
- architecture
- workflow

## Objective
Turn a class with many independent behavior switches into a small host plus focused policies.

## Steps / Flow
1. Write the host’s stable responsibility in one sentence.
2. List each behavior that varies independently.
3. Convert each variation point into a policy concept with a minimal required surface.
4. Provide safe defaults for ordinary use.
5. Add aliases for common combinations.
6. Test invalid combinations as deliberately as valid ones.
7. Modernize the implementation with concepts, traits, or standard utilities where they reduce ceremony.

## Success Check
- The host owns orchestration.
- Policies do not know unrelated policies.
- The public alias for the common case is easy to read.
- Invalid policy mixes fail early.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 16, 20, 26, 28
