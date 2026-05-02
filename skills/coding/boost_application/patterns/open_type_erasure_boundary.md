---
id: skill.skills__coding__boost_application__patterns__open_type_erasure_boundary__open_type_erasure_boundary
title: "Open Type Erasure Boundary"
kind: pattern
domain: coding
tags: [boost, any, type-erasure]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 24-27"
---

# Open Type Erasure Boundary

## Purpose

Use type erasure for plugin-like or heterogeneous boundaries where producers and consumers cannot agree on a closed variant list.

## Use When

A variable or collection must accept values from independent code paths without forcing all possible types into one central enum or variant.

## Pattern

1. Decide whether the boundary is genuinely open.
2. Hide storage behind a small accessor contract.
3. Perform extraction only at validated boundary points.
4. Fail clearly when the stored type does not match the requested type.
5. Avoid placing type-erased values in hot loops unless the flexibility is worth the runtime cost.

## Modern C++ Note

std::any is the standard choice for simple open type erasure; use stronger domain-specific wrappers when you need validation, serialization, or auditability.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
