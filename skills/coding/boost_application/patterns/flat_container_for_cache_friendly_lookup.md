---
id: skill.skills__coding__boost_application__patterns__flat_container_for_cache_friendly_lookup__flat_container_for_cache_friendly_lookup
title: "Flat Container For Cache Friendly Lookup"
kind: pattern
domain: coding
tags: [containers, performance]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 263-277"
---

# Flat Container For Cache Friendly Lookup

## Purpose

Use flat associative containers when sorted-vector locality beats node-based insertion flexibility.

## Use When

Lookup dominates mutation and data can be kept sorted compactly.

## Pattern

1. Estimate read/write ratio.
2. Prefer flat maps/sets for mostly-static or batch-updated data.
3. Insert in batches when possible.
4. Avoid flat containers for heavy random insertion/deletion.
5. Benchmark against unordered and node-based containers with realistic data.

## Modern C++ Note

Modern C++23 has flat_map/flat_set in the standard; Boost.Container remains useful for older standards.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
