---
id: skill_cpp_language_4e__thread_lock_scope_pairing
title: "Thread Lock Scope Pairing"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "threads and locks"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Thread Lock Scope Pairing

## Use When
Shared state must be protected by a mutex or similar synchronization primitive.

## Core Move
Tie lock acquisition to scope and keep the protected region visually small.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use scoped locks, lock guards, unique locks, and higher-level ownership boundaries.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
