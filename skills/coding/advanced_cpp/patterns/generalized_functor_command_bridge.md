# Generalized Functor Command Bridge

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
- functors
- command_pattern
- std_function

## Pattern Rule
**IF** dispatch should not depend on the concrete receiver type,  
**THEN** store behavior as a callable abstraction,  
**ELSE** invokers become coupled to every command target.

## Do
- Use lambdas, `std::function`, or templates for modern callable storage.
- Name ownership and capture lifetimes.
- Keep undo/redo state separate from invocation plumbing.

## Don't
- Do not hand-roll callable wrappers unless type erasure cost or ABI rules require it.
- Do not capture dangling references.

## Checklist
- Invocation signature is explicit.
- Captured state lifetime is safe.
- The invoker does not know receiver details.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 100, 101, 103, 110, 124


## PASS Variant Absorption — Boost C++ Application Development Cookbook

- Absorbed variant: Boost.Any as open type-erasure boundary
- Absorbed as: variant/refinement note
- Source handling: transformed idea only; no source prose copied.
- Modernization: treat Boost-era mechanics as either standard-library migration targets or Boost-specific tools when the standard library still lacks equivalent coverage.
