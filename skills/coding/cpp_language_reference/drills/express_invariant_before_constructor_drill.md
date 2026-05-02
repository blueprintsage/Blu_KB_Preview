---
id: skill_cpp_language_4e__express_invariant_before_constructor_drill
title: "Express Invariant Before Constructor Drill"
type: drill
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "classes"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, drill]
---

# Express Invariant Before Constructor Drill

## Use When
A class is being designed around valid/invalid states.

## Core Move
Write the invariant for a class in one sentence, then design constructors that either establish it or fail cleanly.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Pair with unit tests for rejected construction paths.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
