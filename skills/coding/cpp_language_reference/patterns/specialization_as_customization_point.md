---
id: skill_cpp_language_4e__specialization_as_customization_point
title: "Specialization As Customization Point"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "specialization"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Specialization As Customization Point

## Use When
A generic component needs optimized or exceptional behavior for a few types.

## Core Move
Use specialization to customize type-specific behavior while preserving the generic algorithm contract.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Prefer constrained overloads, customization point objects, or tag_invoke-style designs when they make extension safer.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
