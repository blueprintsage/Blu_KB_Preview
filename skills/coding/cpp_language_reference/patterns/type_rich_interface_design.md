---
id: skill_cpp_language_4e__type_rich_interface_design
title: "Type Rich Interface Design"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "types and declarations"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Type Rich Interface Design

## Use When
An API has many ints, bools, strings, or raw pointers whose meaning is easy to mix up.

## Core Move
Replace unstructured primitive parameter sets with named types that encode role, unit, ownership, or valid operations.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use enum class, strong typedefs, class wrappers, concepts, and narrow constructors.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
