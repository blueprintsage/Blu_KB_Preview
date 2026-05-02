---
id: skill_cpp_language_4e__allocator_as_resource_strategy
title: "Allocator As Resource Strategy"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "memory and resources"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Allocator As Resource Strategy

## Use When
Memory locality, pooling, arena lifetime, or custom allocation matters.

## Core Move
Treat allocation as a policy of a component, not as scattered calls inside business logic.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Consider pmr resources and standard allocators before custom allocator machinery.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
