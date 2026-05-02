---
id: skill_cpp_language_4e__overload_set_as_concept_interface
title: "Overload Set As Concept Interface"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "functions and generic programming"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Overload Set As Concept Interface

## Use When
You are designing APIs for related operations over multiple types.

## Core Move
Treat overloads as a small language for the valid operations in a domain, not as a bag of convenience spellings.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use concepts and constrained overloads in modern code to keep error messages and overload resolution clean.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
