---
id: skill_cpp_language_4e__design_generic_algorithm_with_constraints_workflow
title: "Design Generic Algorithm With Constraints Workflow"
type: ap
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "generic programming"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, ap]
---

# Design Generic Algorithm With Constraints Workflow

## Use When
You need reusable logic across containers or value types.

## Core Move
Start from two concrete algorithms, lift the common operation set, write requirements, then implement with constraints and tests over multiple types.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use concepts/ranges in C++20+ projects.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
