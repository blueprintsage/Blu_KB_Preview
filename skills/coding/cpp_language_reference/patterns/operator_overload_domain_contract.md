---
id: skill_cpp_language_4e__operator_overload_domain_contract
title: "Operator Overload Domain Contract"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "operators"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Operator Overload Domain Contract

## Use When
A user-defined type wants natural syntax without surprising readers.

## Core Move
Overload operators only when their meaning matches the domain model and preserves expected algebraic or access behavior.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Prefer named functions when the operation is not conventional or has expensive hidden effects.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
