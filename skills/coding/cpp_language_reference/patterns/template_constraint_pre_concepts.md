---
id: skill_cpp_language_4e__template_constraint_pre_concepts
title: "Template Constraint Pre Concepts"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "templates"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Template Constraint Pre Concepts

## Use When
A template error is hard to understand or accepts too many accidental types.

## Core Move
Document template requirements as if they were formal concepts, even when the codebase cannot use C++20 concepts yet.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Prefer concepts/requires in modern code; otherwise use traits, static_assert, and clear adapter points.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
