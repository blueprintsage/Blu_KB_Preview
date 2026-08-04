---
title: "Figure Construction"
status: active
topic: dynamic_figure_drawing
type: index
updated: 2026-08-03
---

# Figure Construction

## Purpose

Route non-trivial figure and creature drawing through the staged drawing
workflow before any image-generation or image-editing tool is called.

## Canonical workflow

Load:

1. `SKILL.md`
2. the same-stage precedent assets required by `SKILL.md`
3. the active regression case when testing

## Required entry behavior

For a new drawing request:

1. complete SkillForge preflight;
2. load and apply `SKILL.md`;
3. produce Stage 0 only;
4. inspect the result against a same-stage precedent;
5. present only a passing Stage 0;
6. stop for approval, rejection, or revision.

A rejection produces a new Stage 0. It does not authorize polishing or advancing
the rejected candidate.

## Assets

Canonical staged-process assets are under `assets/`.

Known Stage 0 calibration sources include:

- `assets/source_staged_figure_process_1.png`
- `assets/source_staged_dragon_process.png`
- `assets/source_staged_alien_process.png`
- accepted Warbot Stage 0 references
- accepted zero-G astronaut Stage 0 references
- other accepted current Stage 0 references

The workflow compares purpose, density, and commitment. It does not require
subject resemblance.

## Tests

- `tests/chimera-stage0.md`
