---
id: skill_cpp_language_4e__header_source_firewall
title: "Header Source Firewall"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "source files and programs"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Header Source Firewall

## Use When
Compile times, dependencies, or ABI boundaries are becoming fragile.

## Core Move
Keep headers minimal and stable; move implementation detail to source files or private modules.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use forward declarations, pimpl selectively, modules where practical, and include-what-you-use discipline.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
