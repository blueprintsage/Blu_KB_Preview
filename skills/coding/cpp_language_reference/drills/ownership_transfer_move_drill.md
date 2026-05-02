---
id: skill_cpp_language_4e__ownership_transfer_move_drill
title: "Ownership Transfer Move Drill"
type: drill
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "copy and move"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, drill]
---

# Ownership Transfer Move Drill

## Use When
A type currently leaks ownership through raw pointers.

## Core Move
Given a resource-owning type, decide which of copy, move, and destruction are allowed, deleted, or defaulted.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Prefer rule-of-zero with standard ownership members.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
