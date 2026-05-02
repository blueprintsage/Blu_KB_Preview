---
id: skill_cpp_language_4e__constexpr_as_compile_time_contract
title: "Constexpr As Compile Time Contract"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "constant expressions"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Constexpr As Compile Time Contract

## Use When
A rule is deterministic and should fail before runtime.

## Core Move
Use compile-time evaluation to make constants, tables, and validation rules executable by the compiler.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Modernize C++11 constexpr to broader C++14/17/20 constexpr where project support allows.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
