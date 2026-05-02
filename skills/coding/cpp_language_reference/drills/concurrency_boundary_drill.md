---
id: skill_cpp_language_4e__concurrency_boundary_drill
title: "Concurrency Boundary Drill"
type: drill
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "threads and tasks"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, drill]
---

# Concurrency Boundary Drill

## Use When
A design uses mutexes everywhere with unclear ownership.

## Core Move
Rewrite shared mutable state into message/task/result boundaries where possible, then lock only what remains.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Prefer structured concurrency/task APIs when your platform provides them.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
