---
id: skill_cpp_language_4e__exception_guarantee_ladder
title: "Exception Guarantee Ladder"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "exception handling"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Exception Guarantee Ladder

## Use When
You need to reason about errors without leaking resources or corrupting state.

## Core Move
Classify operations by no-throw, strong guarantee, basic guarantee, or failure-transparent boundary before implementation.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use RAII, swap-based commit, noexcept where true, and expected-like result channels when exceptions are not the boundary style.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
