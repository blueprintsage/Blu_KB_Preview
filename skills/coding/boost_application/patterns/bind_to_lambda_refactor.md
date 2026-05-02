---
id: skill.skills__coding__boost_application__patterns__bind_to_lambda_refactor__bind_to_lambda_refactor
title: "Bind To Lambda Refactor"
kind: pattern
domain: coding
tags: [boost, lambda, modernization]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 41-48"
---

# Bind To Lambda Refactor

## Purpose

Replace old placeholder-heavy bind expressions with lambdas when the lambda states intent more clearly.

## Use When

A legacy codebase uses boost::bind or std::bind to reorder parameters, bind state, or adapt callbacks.

## Pattern

1. Identify what arguments are reordered, ignored, or captured.
2. Rewrite the expression as a lambda with explicit parameter names.
3. Capture expensive objects by reference only when lifetime is proven.
4. Preserve noexcept/return-type behavior when it matters.
5. Keep bind only for rare generic adapters where it is more compact and clear.

## Modern C++ Note

Modern C++ lambdas usually beat bind for readability, diagnostics, and local reasoning.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
