---
id: skill_cpp_language_4e__class_default_control_rule
title: "Class Default Control Rule"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "construction/copy/move"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Class Default Control Rule

## Use When
A class owns resources, enforces invariants, or participates in polymorphism.

## Core Move
Declare or delete default operations to match ownership intent instead of accepting accidental generated behavior.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use rule-of-zero when members already express ownership; use explicit default/delete when the class policy matters.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
