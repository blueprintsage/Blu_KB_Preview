---
id: skill_cpp_language_4e__design_matrix_like_value_type_workflow
title: "Design Matrix Like Value Type Workflow"
type: ap
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "abstraction/numerics"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, ap]
---

# Design Matrix Like Value Type Workflow

## Use When
A numeric type needs both performance and clean abstraction.

## Core Move
Define shape, storage, element requirements, slicing/view behavior, value/move semantics, and algorithm interoperability before implementing storage.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use mdspan/span/views or proven libraries where available.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
