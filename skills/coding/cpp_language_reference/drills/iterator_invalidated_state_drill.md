---
id: skill_cpp_language_4e__iterator_invalidated_state_drill
title: "Iterator Invalidated State Drill"
type: drill
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "containers"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, drill]
---

# Iterator Invalidated State Drill

## Use When
Bugs appear after vector growth, erase, insert, or map mutation.

## Core Move
For each container operation in a code sample, mark which iterators, references, and pointers remain valid.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use stable containers only when stability is a real requirement.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
