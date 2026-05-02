---
id: skill.skills__coding__boost_application__patterns__base_from_member_initialization_order_guard__base_from_member_initialization_order_guard
title: "Base From Member Initialization Order Guard"
kind: pattern
domain: coding
tags: [oop, initialization]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 104-107"
---

# Base From Member Initialization Order Guard

## Purpose

Handle cases where a base class needs a helper object that would otherwise be initialized too late.

## Use When

A derived member must be available during base-class construction.

## Pattern

1. Notice when base construction depends on derived-owned state.
2. Move the dependency into an earlier base subobject or wrapper.
3. Make initialization order visible in the class declaration.
4. Prefer simpler composition when possible.
5. Test constructor failure paths because order bugs can be subtle.

## Modern C++ Note

Modern C++ still obeys base/member initialization order; this is a design problem, not just a Boost-specific trick.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
