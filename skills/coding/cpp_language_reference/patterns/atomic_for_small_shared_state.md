---
id: skill_cpp_language_4e__atomic_for_small_shared_state
title: "Atomic For Small Shared State"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "memory model"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Atomic For Small Shared State

## Use When
A flag, counter, or pointer publication is shared across threads.

## Core Move
Use atomics only for narrow, well-understood shared-state protocols; use locks or tasks for compound invariants.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Modern atomics still require memory-order discipline; default to simple ordering unless measured need proves otherwise.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
