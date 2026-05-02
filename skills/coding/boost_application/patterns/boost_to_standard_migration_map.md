---
id: skill.skills__coding__boost_application__patterns__boost_to_standard_migration_map__boost_to_standard_migration_map
title: "Boost To Standard Migration Map"
kind: pattern
domain: coding
tags: [boost, modernization]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 12-14, 24-57"
---

# Boost To Standard Migration Map

## Purpose

Treat Boost utility types as historical bridges to standard-library equivalents, keeping the design role while modernizing the implementation.

## Use When

A codebase uses Boost.Any, Variant, Optional, Array, Tuple, Bind, or shared ownership helpers and needs a C++17+ audit.

## Pattern

1. Identify each Boost component by role rather than by header name.
2. Check whether the current standard library has an equivalent with acceptable semantics.
3. Prefer standard vocabulary types for new code unless Boost behavior is still materially stronger.
4. Keep Boost-specific code when portability, older compiler support, or missing standard coverage justifies it.
5. Document semantic differences before replacing APIs.

## Modern C++ Note

Common replacements include std::any, std::variant, std::optional, std::array, std::tuple, lambdas, std::function, and standard smart pointers.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
