---
id: skill_cpp_language_4e__task_future_result_channel
title: "Task Future Result Channel"
type: pattern
source: "Bjarne Stroustrup - The C++ Programming Language, 4th ed. (2013), transformed PASS object"
source_band: "concurrency"
domain: coding/cpp
status: active
tags: [cpp, stroustrup, pattern]
---

# Task Future Result Channel

## Use When
A concurrent operation needs to return a value, exception, or completion state.

## Core Move
Represent asynchronous work by its eventual result or failure, not by shared mutable flags.

## Practice Rule
State the design intent in the type, interface, or ownership boundary before reaching for comments or conventions. Prefer a standard-library facility when it expresses the same intent clearly.

## Modernization Note
Use future/promise/async carefully; consider executors, coroutines, or project task systems in newer code.

## PASS Handling
This is a transformed learning object. It does not reproduce source prose or example code.
