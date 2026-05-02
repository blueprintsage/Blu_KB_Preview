---
id: skill.skills__coding__boost_application__patterns__move_emulation_as_legacy_bridge__move_emulation_as_legacy_bridge
title: "Move Emulation As Legacy Bridge"
kind: pattern
domain: coding
tags: [boost, move, modernization]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 48-53"
---

# Move Emulation As Legacy Bridge

## Purpose

Treat Boost.Move-era patterns as compatibility bridges, not as preferred design for modern compilers.

## Use When

A library must support pre-C++11 toolchains or a legacy codebase has emulated move-only types.

## Pattern

1. Separate the move-only ownership rule from the emulation mechanism.
2. Modernize to deleted copy operations and real move constructors where possible.
3. Check moved-from invariants explicitly.
4. Keep emulation macros isolated behind compatibility headers.
5. Do not mix old emulation idioms with modern move semantics casually.

## Modern C++ Note

Use native move constructors, move assignment, and std::move in C++11+ code.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
