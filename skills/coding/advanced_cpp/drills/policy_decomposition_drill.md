# Policy Decomposition Drill

## Object Type
drill

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
- practice
- policy_based_design
- architecture

## Practice Task
Take one class with three behavior flags and turn it into a host plus three policy axes.

## Target Skill
Separate independent design decisions without creating a do-it-all interface.

## Setup
Use a small example such as a logger, allocator wrapper, serializer, or smart pointer sketch.

## Instructions
1. Name the stable host job.
2. Identify three independent behavior choices.
3. Write the required surface for each policy.
4. Provide one default and one alternate for each.
5. Write two aliases showing meaningful combinations.

## Success Check
- Each policy has one reason to change.
- The host still enforces the invariant.
- The aliases read like real design choices.

## Common Failures
- Turning every line into a policy.
- Letting policies own orchestration.
- Forgetting invalid combinations.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 16, 26, 28
