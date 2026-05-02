# Singleton Lifetime Smell Drill

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
- singleton
- lifetime

## Practice Task
Audit a singleton design and decide whether to remove it, scope it, or make its lifetime policy explicit.

## Target Skill
Recognize when singleton is solving uniqueness and when it is hiding dependency passing.

## Setup
Use a logger, config store, service registry, or random engine example.

## Instructions
1. Identify who needs the object.
2. Identify whether uniqueness is required.
3. Identify destruction-order dependencies.
4. Identify thread-safety requirements.
5. Choose dependency injection, scoped service, function-local static, or explicit singleton policy.

## Success Check
- The final design names lifetime and shutdown behavior.
- Tests can replace or isolate the dependency.
- No hidden global dependency remains by accident.

## Common Failures
- Using singleton because passing an object is inconvenient.
- Ignoring cross-singleton shutdown order.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 127, 132, 143, 146
