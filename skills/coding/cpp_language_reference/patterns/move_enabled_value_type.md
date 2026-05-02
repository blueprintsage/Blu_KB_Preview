---
id: skill_cpp_language_4e__move_enabled_value_type
title: "Move Enabled Value Type"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "copy and move"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Move Enabled Value Type

## Use When
A type should be returnable, storable in containers, and composable without pointer-style APIs.

## Core Move
Design heavy objects to behave like values while moving their owned representation cheaply.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use move operations, noexcept moves for containers, and standard resource members where possible.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
