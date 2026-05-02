---
id: skill_cpp_language_4e__migrate_c_style_module_to_cpp_interface_workflow
title: "Migrate C Style Module To Cpp Interface Workflow"
type: ap
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "compatibility"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, ap]
---

# Migrate C Style Module To Cpp Interface Workflow

## Use When
A C or old-C++ subsystem must stay but should not shape new code.

## Core Move
Place the C-facing code behind a narrow adapter, translate data into C++ vocabulary types, and prevent raw ownership from escaping.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use span/string_view cautiously when lifetime is obvious.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
