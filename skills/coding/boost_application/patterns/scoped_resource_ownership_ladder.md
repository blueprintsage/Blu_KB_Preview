---
id: skill.skills__coding__boost_application__patterns__scoped_resource_ownership_ladder__scoped_resource_ownership_ladder
title: "Scoped Resource Ownership Ladder"
kind: pattern
domain: coding
tags: [raii, boost, memory]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 82-104"
---

# Scoped Resource Ownership Ladder

## Purpose

Choose resource ownership wrappers by lifetime: local scope, shared method boundary, array ownership, callback storage, or container ownership.

## Use When

A resource is currently managed by manual new/delete, raw handles, or unclear pointer conventions.

## Pattern

1. Identify whether the resource leaves the current scope.
2. Use scoped ownership for strictly local lifetime.
3. Use shared ownership only when multiple owners are real.
4. Use dedicated pointer containers or value containers rather than containers of owning raw pointers.
5. Write the cleanup path as a normal consequence of object lifetime.

## Modern C++ Note

Prefer unique_ptr/shared_ptr, standard containers, and RAII objects; use Boost equivalents for legacy compatibility.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
