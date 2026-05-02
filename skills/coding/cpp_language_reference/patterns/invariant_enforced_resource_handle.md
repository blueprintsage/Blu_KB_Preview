---
id: skill_cpp_language_4e__invariant_enforced_resource_handle
title: "Invariant Enforced Resource Handle"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "classes and exceptions"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Invariant Enforced Resource Handle

## Use When
A type represents a file, lock, allocation, socket, transaction, or other acquire/release pair.

## Core Move
Make construction establish the invariant, destruction release the resource, and member functions preserve the invariant.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Prefer standard handles first; write custom handles only for project-specific resources.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
