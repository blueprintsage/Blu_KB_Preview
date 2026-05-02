---
id: skill.skills__coding__boost_application__aps__build_multi_index_repository_workflow__build_multi_index_repository_workflow
title: "Build Multi Index Repository Workflow"
kind: ap
domain: coding
tags: [boost, workflow]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 18-338"
---

# Build Multi Index Repository Workflow

## Purpose

Build an in-memory repository with multiple lookup paths without duplicating record storage.

## Use When

A project needs an end-to-end workflow rather than a single local idiom.

## Pattern

1. Name the record type.
2. List query access paths.
3. Choose ordered, hashed, sequenced, or composite indexes.
4. Define mutation rules.
5. Write lookup and update helpers.
6. Test that all indexes reflect one mutation.

## Modern C++ Note

Default to modern C++ vocabulary and wrap Boost-specific dependencies behind clear project boundaries.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
