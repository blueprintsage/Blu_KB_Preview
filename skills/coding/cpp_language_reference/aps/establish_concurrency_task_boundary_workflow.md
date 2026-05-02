---
id: skill_cpp_language_4e__establish_concurrency_task_boundary_workflow
title: "Establish Concurrency Task Boundary Workflow"
type: ap
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "concurrency"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, ap]
---

# Establish Concurrency Task Boundary Workflow

## Use When
Concurrent code is growing from ad hoc thread creation.

## Core Move
Define task inputs, outputs, failure channel, cancellation/story, and shared-state boundary before choosing threads or locks.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use futures, queues, executors, coroutines, or framework tasks as appropriate.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
