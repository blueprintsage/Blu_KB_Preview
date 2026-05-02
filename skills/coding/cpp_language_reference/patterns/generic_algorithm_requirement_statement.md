---
id: skill_cpp_language_4e__generic_algorithm_requirement_statement
title: "Generic Algorithm Requirement Statement"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "generic programming"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Generic Algorithm Requirement Statement

## Use When
You want one implementation to work across many data representations.

## Core Move
Write the algorithm against operations and semantic requirements, not against one concrete container or type.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use ranges, concepts, and iterator/category requirements where available.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
