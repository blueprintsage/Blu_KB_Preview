---
id: skill_cpp_language_4e__compatibility_isolation_layer
title: "Compatibility Isolation Layer"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "compatibility"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Compatibility Isolation Layer

## Use When
A project must call old code without letting old idioms spread.

## Core Move
Fence legacy C, old C++, platform APIs, or ABI constraints behind a small typed C++ surface.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use adapters, RAII handles, typed wrappers, and modernization tests.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
