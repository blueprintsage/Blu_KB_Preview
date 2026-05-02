---
id: skill.skills__coding__boost_application__patterns__embedded_parser_for_small_languages__embedded_parser_for_small_languages
title: "Embedded Parser For Small Languages"
kind: pattern
domain: coding
tags: [boost, parsing]
source: transformed_from_pass
source_trace: "Antony Polukhin, Boost C++ Application Development Cookbook, pages 72-81"
---

# Embedded Parser For Small Languages

## Purpose

Use parser-combinator style for small structured input languages instead of hand-rolling fragile string splits.

## Use When

Configuration, commands, expressions, or protocol fragments need more structure than simple token conversion.

## Pattern

1. Define the grammar close to the domain concept.
2. Keep parse actions separate from validation when possible.
3. Return a typed parse result rather than raw tokens.
4. Add small examples for accepted and rejected inputs.
5. Escalate to a dedicated parser only when the grammar grows beyond local readability.

## Modern C++ Note

Boost.Spirit remains useful for embedded parsers, though modern alternatives may be easier for teams that do not already know expression-template parsers.

## PASS Handling

This object is a transformed learning object. It preserves the idea and decision shape, not source prose or recipe text.
