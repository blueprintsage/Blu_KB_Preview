---
id: skill_cpp_language_4e__standard_container_before_custom_storage
title: "Standard Container Before Custom Storage"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "standard library containers"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Standard Container Before Custom Storage

## Use When
You are tempted to write manual dynamic arrays, lists, maps, or storage pools.

## Core Move
Choose a standard container and adapt the design before building a custom data structure.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use vector, array, deque, map/unordered_map, string, optional, variant, and span/view as the first vocabulary.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
