---
id: skill_cpp_language_4e__value_category_ownership_boundary
title: "Value Category Ownership Boundary"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "copy and move"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Value Category Ownership Boundary

## Use When
A type owns resources or is expensive to copy.

## Core Move
Treat lvalues as stable named objects and rvalues as transferable resources; design overloads around that distinction.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use move constructors, move assignment, forwarding references only where needed, and avoid over-forwarding APIs.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
