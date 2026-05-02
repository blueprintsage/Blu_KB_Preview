---
id: skill_cpp_language_4e__c_library_quarantine
title: "C Library Quarantine"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "C standard library compatibility"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# C Library Quarantine

## Use When
The fastest or only available tool is a C API.

## Core Move
Allow C library functions only at narrow boundaries and translate results into C++ vocabulary types quickly.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Prefer standard C++ alternatives when equally clear; quarantine raw buffers and errno-style results.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
