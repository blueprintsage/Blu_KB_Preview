---
id: skill_cpp_language_4e__explicit_conversion_boundary
title: "Explicit Conversion Boundary"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "conversions"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Explicit Conversion Boundary

## Use When
A type wraps a primitive, unit, handle, or string-like representation.

## Core Move
Make conversions explicit unless implicit use is unsurprising, safe, and lossless in the domain.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use explicit constructors/operators, named factories, and strong types.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
