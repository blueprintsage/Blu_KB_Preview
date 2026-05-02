---
id: skill.skills__coding__boost_application__patterns__fixed_size_array_as_value_object__fixed_size_array_as_value_object
title: "Fixed Size Array As Value Object"
kind: pattern
domain: coding
tags: [array, containers]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 36-39"
---

# Fixed Size Array As Value Object

## Purpose

Wrap fixed-size arrays in a container-like value type so size, iteration, and assignment are visible without pointer decay.

## Use When

A small fixed-size buffer must be passed, returned, copied, or iterated safely.

## Pattern

1. Encode the length in the type.
2. Use container-style iteration and indexing.
3. Avoid raw array parameters that decay into pointers.
4. Assert or statically check the expected size.
5. Switch to vector/span only when size is runtime-variable or non-owning.

## Modern C++ Note

Use std::array for owning fixed-size arrays and std::span for non-owning views in modern C++.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
