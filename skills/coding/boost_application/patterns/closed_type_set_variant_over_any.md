---
id: skill.skills__coding__boost_application__patterns__closed_type_set_variant_over_any__closed_type_set_variant_over_any
title: "Closed Type Set Variant Over Any"
kind: pattern
domain: coding
tags: [boost, variant, type-safety]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 24-33"
---

# Closed Type Set Variant Over Any

## Purpose

Use a variant when the legal stored types are known, so compile-time exhaustiveness replaces runtime guessing.

## Use When

A container needs to hold several possible value types, but the set of valid types is controlled by the application.

## Pattern

1. Name the valid alternatives explicitly.
2. Represent absence with a dedicated first alternative when needed.
3. Read values through a visitor rather than unchecked extraction.
4. Let compiler errors reveal new cases that handlers forgot.
5. Reserve type-erased any-values for truly open extension points.

## Modern C++ Note

In modern C++, prefer std::variant plus std::visit for closed sets; keep boost::variant only for older compiler or Boost-integrated code.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
