---
id: skill.skills__coding__boost_application__patterns__optional_result_without_sentinel_pointer__optional_result_without_sentinel_pointer
title: "Optional Result Without Sentinel Pointer"
kind: pattern
domain: coding
tags: [boost, optional, api-design]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 33-36"
---

# Optional Result Without Sentinel Pointer

## Purpose

Represent a possibly-missing result as an explicit optional value instead of returning null pointers, magic numbers, or out-parameter flags.

## Use When

A function can fail to produce a value but the absence is expected, local, and not exceptional.

## Pattern

1. Return an optional result rather than a raw pointer.
2. Require callers to check presence before dereferencing.
3. Keep absence separate from default values.
4. Use exceptions only when the failure is exceptional or needs stack unwinding.
5. Document whether absence means retry, skip, or stop.

## Modern C++ Note

Use std::optional in modern C++; combine with expected/result types when you need an error payload as well as absence.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
