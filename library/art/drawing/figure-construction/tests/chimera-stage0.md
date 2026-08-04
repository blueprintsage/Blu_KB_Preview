---
test_id: drawing_stage0_chimera_density_guard
title: "Chimera Stage 0 Density Guard"
status: active
topic: dynamic_figure_drawing
type: regression_test
updated: 2026-08-03
---

# Chimera Stage 0 Density Guard

## Input

> Draw another Chimera. It has a lion body. The lion head and goat head are next
> to one another on separate necks. Its lion tail becomes a snake, and it has bat
> wings.

## Preconditions

The test is invalid unless:

- the current repository boot chain was read;
- SkillForge preflight actually ran;
- the figure-construction drawing workflow was selected and loaded;
- an accepted Stage 0 precedent was inspected before generation.

File presence or conversational memory is not proof that these steps occurred.

## Expected output

The workflow produces exactly one Stage 0 thumbnail and stops.

The thumbnail shows:

- a readable lion-body mass and action;
- two readable separate neck paths;
- two adjacent head-location shapes;
- broad bat-wing spread and attachment regions;
- a readable snake-tail path;
- readable framing, balance, weight, gesture, and silhouette;
- unresolved internal structure;
- low information density.

## Routing failures

Fail the test if:

- an image tool is called before SkillForge preflight;
- the selected drawing workflow is not loaded;
- SkillForge influence is claimed without execution proof;
- the request falls through to an ordinary direct-image path.

## Stage failures

Fail the test if the candidate contains:

- a resolved lion face;
- a resolved goat face;
- mane detail;
- horn detail;
- detailed paws or claws;
- wing-finger anatomy;
- membrane subdivision;
- a rendered snake head;
- scales or fur;
- anatomical torso construction;
- polished contour;
- modeled shading;
- explanatory annotations;
- a camera diagram;
- multiple panels;
- a full process sheet;
- final-render presentation.

Also fail when the candidate is closer in purpose, density, or commitment to a
Stage 1 or Stage 2 precedent than to an accepted Stage 0 precedent.

## Workflow failures

Fail the test if:

- a rejected candidate is polished instead of replaced;
- the failed candidate is reused as the basis of the next stage;
- the workflow advances without user approval;
- more than Stage 0 is presented.

## Pass behavior

On pass:

1. present the Stage 0 image;
2. do not describe it as polished or complete;
3. stop for approval, rejection, or revision.

## Rejection behavior

On rejection:

1. discard the candidate as a stage result;
2. assemble a fresh Stage 0 prompt;
3. generate another Stage 0 from scratch;
4. run the same validator again;
5. do not advance stages.
