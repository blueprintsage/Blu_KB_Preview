---
id: skill_cpp_language_4e__iterator_pair_as_range_boundary
title: "Iterator Pair As Range Boundary"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "iterators"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Iterator Pair As Range Boundary

## Use When
An algorithm should not care what owns the data.

## Core Move
Represent traversal as a boundary over a sequence rather than exposing the container’s internals.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Modern code often upgrades this to ranges/spans/views for safer boundaries.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
