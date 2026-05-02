---
id: skill.skills__coding__boost_application__drills__variant_visitor_exhaustiveness_drill__variant_visitor_exhaustiveness_drill
title: "Variant Visitor Exhaustiveness Drill"
kind: drill
domain: coding
tags: [boost, drill]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 18-338"
---

# Variant Visitor Exhaustiveness Drill

## Purpose

Practice forcing handlers for every known alternative in a closed type set.

## Use When

A learner needs hands-on practice applying the corresponding Boost/modern C++ decision.

## Pattern

1. Define a variant with three alternatives.
2. Write a visitor that handles all of them.
3. Add a fourth alternative.
4. Observe the compile failure or missing handler.
5. Repair the visitor deliberately.

## Modern C++ Note

Use modern standard facilities where they express the same idea more directly; keep Boost forms when they teach portability or remain the strongest tool.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
