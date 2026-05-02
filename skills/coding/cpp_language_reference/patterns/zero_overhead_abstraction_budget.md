---
id: skill_cpp_language_4e__zero_overhead_abstraction_budget
title: "Zero Overhead Abstraction Budget"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "C++ design philosophy"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Zero Overhead Abstraction Budget

## Use When
You are designing a library primitive that may live inside hot paths.

## Core Move
Accept an abstraction only when unused parts cost nothing and used parts are comparable to careful hand-written code.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Modern C++ keeps this rule; validate with profiling and generated-code inspection only where it matters.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
