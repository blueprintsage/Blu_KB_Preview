# Functor Wrapper to std::function Drill

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
- functors
- std_function

## Practice Task
Replace a custom command/functor wrapper with a modern callable form where appropriate.

## Target Skill
Separate the Command-pattern lesson from historical callable-wrapper implementation.

## Setup
Use a button click, undo action, task queue, or callback list.

## Instructions
1. Write the required call signature.
2. Decide whether captures are by value, reference, or shared ownership.
3. Implement with lambda or `std::function`.
4. Add one undo/redo state example if needed.
5. Note when a templated callable is better than type erasure.

## Success Check
- The invocation signature is explicit.
- Captured lifetimes are safe.
- Custom type erasure is not used unless justified.

## Common Failures
- Capturing stack references into longer-lived callbacks.
- Using `std::function` in a hot path without measuring.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 100, 110, 124
