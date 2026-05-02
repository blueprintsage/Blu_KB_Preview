---
id: skill_cpp_language_4e__header_dependency_reduction_drill
title: "Header Dependency Reduction Drill"
type: drill
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "source files"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, drill]
---

# Header Dependency Reduction Drill

## Use When
Build time or rebuild blast radius is too large.

## Core Move
Pick one header and remove includes that can become forward declarations, private implementation, or module imports.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use automated include analysis where available.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
