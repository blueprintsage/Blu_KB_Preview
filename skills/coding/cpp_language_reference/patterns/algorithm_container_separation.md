---
id: skill_cpp_language_4e__algorithm_container_separation
title: "Algorithm Container Separation"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "standard algorithms"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Algorithm Container Separation

## Use When
Loops are duplicating traversal and transformation logic across code.

## Core Move
Keep data ownership in containers and behavior in algorithms operating over ranges or iterators.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Prefer standard algorithms/ranges; keep hand loops for genuinely clearer control flow.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
