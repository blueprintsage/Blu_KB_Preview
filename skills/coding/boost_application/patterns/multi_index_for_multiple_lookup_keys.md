---
id: skill.skills__coding__boost_application__patterns__multi_index_for_multiple_lookup_keys__multi_index_for_multiple_lookup_keys
title: "Multi Index For Multiple Lookup Keys"
kind: pattern
domain: coding
tags: [containers, boost]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 250-277"
---

# Multi Index For Multiple Lookup Keys

## Purpose

Use a multi-index container when one collection needs several coherent lookup orders without duplicating storage.

## Use When

The same records must be queried by ID, name, timestamp, rank, or composite keys.

## Pattern

1. List the required access patterns before choosing the container.
2. Declare each index by its query semantics.
3. Keep mutation rules visible because one change can affect many indexes.
4. Use a simpler unordered/map/vector pair if only one lookup matters.
5. Test invariants that span all indexes.

## Modern C++ Note

Boost.MultiIndex remains a strong tool; the standard library still lacks a direct equivalent.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
