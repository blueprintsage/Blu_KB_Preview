---
id: skill_cpp_language_4e__direct_mapping_plus_abstraction
title: "Direct Mapping Plus Abstraction"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "C++ design philosophy"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Direct Mapping Plus Abstraction

## Use When
You need performance-sensitive C++ but still want APIs that read in problem-domain terms.

## Core Move
Use low-level operations only behind typed abstractions so the code can stay close to the machine without leaking machine detail everywhere.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
In newer C++, pair this with RAII, spans/views, constexpr, concepts, and standard-library handles.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
