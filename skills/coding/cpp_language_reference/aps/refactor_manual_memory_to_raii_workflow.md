---
id: skill_cpp_language_4e__refactor_manual_memory_to_raii_workflow
title: "Refactor Manual Memory To Raii Workflow"
type: ap
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "memory/resources"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, ap]
---

# Refactor Manual Memory To Raii Workflow

## Use When
Manual memory management is mixed with business logic.

## Core Move
Locate new/delete or malloc/free pairs, choose an owning type, replace naked ownership, and verify destructor-driven cleanup.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use unique_ptr, shared_ptr, vector, string, optional, and pmr where fitting.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
