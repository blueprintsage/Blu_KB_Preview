---
id: skill_cpp_language_4e__audit_type_rich_interface_workflow
title: "Audit Type Rich Interface Workflow"
type: ap
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "types"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, ap]
---

# Audit Type Rich Interface Workflow

## Use When
An API is readable only with comments or argument names.

## Core Move
Inventory primitive parameters, name their roles, create domain types for ambiguous values, and update call sites to remove accidental swaps.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use strong aliases, enum class, and constrained constructors.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
