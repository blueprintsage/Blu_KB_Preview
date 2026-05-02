---
id: skill_cpp_language_4e__choose_container_algorithm_iterator_workflow
title: "Choose Container Algorithm Iterator Workflow"
type: ap
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "standard library"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, ap]
---

# Choose Container Algorithm Iterator Workflow

## Use When
A data structure choice was made before workload was understood.

## Core Move
Define access pattern, mutation pattern, ordering need, stability need, then choose container and standard algorithms together.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Prefer measurement for performance-sensitive choices.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
