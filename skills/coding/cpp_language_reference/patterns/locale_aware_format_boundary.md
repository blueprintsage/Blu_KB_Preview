---
id: skill_cpp_language_4e__locale_aware_format_boundary
title: "Locale Aware Format Boundary"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "locales and formatting"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Locale Aware Format Boundary

## Use When
Numbers, dates, money, or text collation crosses a locale boundary.

## Core Move
Separate internal representation from user-facing cultural formatting.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Modern formatting libraries help, but the boundary principle stays the same.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
