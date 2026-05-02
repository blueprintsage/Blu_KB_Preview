---
id: skill.skills__coding__boost_application__patterns__portable_feature_probe_gate__portable_feature_probe_gate
title: "Portable Feature Probe Gate"
kind: pattern
domain: coding
tags: [portability, build]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 278-295"
---

# Portable Feature Probe Gate

## Purpose

Centralize compiler/platform/library feature detection so portability decisions do not scatter through the codebase.

## Use When

A library must support multiple compilers, platforms, Boost versions, or optional language features.

## Pattern

1. Write one feature probe per capability, not per compiler rumor.
2. Put platform macros behind readable project-level names.
3. Use feature tests to select implementation paths.
4. Fail loudly when a required feature is unavailable.
5. Delete compatibility branches once the supported platform matrix no longer needs them.

## Modern C++ Note

Prefer standardized feature-test macros and build-system checks when available; Boost.Config remains valuable for portability archaeology and cross-compiler support.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
