---
title: "Staged Figure and Creature Drawing"
status: active
topic: dynamic_figure_drawing
type: skill
updated: 2026-08-03
---

# Staged Figure and Creature Drawing

## Authority

This file owns staged figure and creature drawing behavior after SkillForge
selects this craft route.

It does not own repository boot, assistant routing, SkillForge discovery, or
platform-tool selection. Those must already be resolved before this workflow
runs.

## Non-bypass rule

A covered drawing request may not go directly from ordinary conversation to an
image-generation or image-editing tool.

Before tool use, the active turn must establish that:

- SkillForge preflight ran;
- this drawing workflow was selected;
- the required same-stage precedent was inspected;
- the current stage contract was applied.

Do not claim those events occurred unless they actually occurred in the active
runtime.

## Workflow state

For a normal new drawing request, the initial state is always Stage 0.

The stage sequence is:

- Stage 0 — rough thumbnail
- Stage 1 — approved composition clarification
- Stage 2 — construction
- Stage 3 — design refinement
- Stage 4 — final rendering

Only Stage 0 is authorized on the first turn of a new drawing request.

After each stage:

1. inspect the candidate;
2. compare it to an accepted same-stage precedent;
3. reject or present it;
4. stop for user approval, rejection, or revision.

Do not advance without approval.

A rejected stage is regenerated at the same stage. Do not polish a rejected
candidate into the next stage.

## Same-stage precedent calibration

Calibration is required both before generation and after generation.

Compare:

- purpose — what problem the image is solving;
- density — how much visual information it commits;
- commitment — how resolved and difficult to discard the forms have become.

Do not compare:

- subject resemblance;
- species;
- costume;
- aesthetic appeal;
- polish.

Reject a candidate when it resembles the next-stage precedent more than its own
stage precedent.

Stage 2 requires extra caution because it tends to over-render.

## Stage 0 — Rough thumbnail

### Purpose

Stage 0 establishes only:

- camera and framing;
- composition;
- overall gesture;
- silhouette;
- rough placement;
- balance and weight;
- major light/dark masses when compositionally useful;
- broad paths for unusual appendages or features.

Stage 0 is disposable exploration. It must remain low-density and
low-commitment.

### Visual character

Use:

- a single rough marker-style thumbnail;
- blunt masses;
- loose gestural strokes;
- unresolved shapes;
- minimal internal information;
- a plain page;
- one candidate only.

### Allowed content

Stage 0 may contain:

- one dominant torso or body mass;
- simple head-location shapes;
- broad neck paths;
- broad limb or appendage paths;
- wing spread and attachment regions;
- a tail path;
- a ground or balance indication;
- simple overlap needed to read the silhouette;
- one or two broad value masses when compositionally useful.

### Forbidden content

Stage 0 must not contain:

- anatomy;
- resolved construction;
- cylinders, boxes, or joint systems that solve anatomy;
- polished contour;
- facial features or expressions;
- designed mane, horns, ears, teeth, or eyes;
- detailed paws, claws, toes, hands, or feet;
- wing-finger anatomy;
- membrane or feather subdivision;
- rendered snake heads;
- scales, fur, skin, costume, armor, or surface design;
- volume-modeling shadows;
- rendering;
- labels, notes, legends, bullets, callouts, or camera diagrams;
- multiple stages or panels;
- a process-sheet or presentation-board layout.

### Stage 0 prompt assembly

The tool instruction must explicitly say:

- single rough marker thumbnail;
- minimal commitment;
- composition and silhouette study only;
- broad masses and gestural paths;
- unresolved forms;
- one image;
- Stage 0 only;
- no annotations;
- no anatomy, construction, detail, or rendering.

Translate subject requirements into placement, mass, attachment-region, or path
instructions.

Examples:

- “lion body” becomes “one large feline body mass with readable weight and
  action”;
- “two heads on separate necks” becomes “two adjacent head-location shapes on
  two separate neck paths”;
- “bat wings” becomes “two broad wing-spread shapes with shoulder attachment
  regions only”;
- “tail becomes a snake” becomes “one tail path continuing into a serpentine
  terminal path.”

Do not translate feature requests into resolved designs during Stage 0.

### Stage 0 prompt lint

Fail the prompt before generation if it asks for:

- construction circles;
- joint guides;
- anatomical structure;
- detailed faces;
- detailed horns;
- detailed paws;
- wing anatomy;
- membrane detail;
- scales;
- fur texture;
- polished drawing;
- rendering;
- a process sheet;
- labels or annotations;
- a camera diagram.

Warn and rewrite the prompt if it asks for:

- accurate features;
- defined musculature;
- clear facial features;
- dimensional construction;
- volume rendering;
- cinematic lighting.

### Stage 0 post-generation validator

Inspect the generated image before presenting it.

Hard fail if the image contains any of the following:

- resolved eyes, nose, mouth, teeth, or expression;
- designed mane, horns, ears, or facial silhouette;
- articulated paws, claws, toes, hands, or feet;
- explicit muscle groups or skeletal landmarks;
- constructed cylinders, boxes, or joint systems that solve anatomy;
- wing fingers, membrane subdivisions, feathers, or attachment anatomy;
- rendered snake-head detail or scales;
- fur, skin, costume, armor, texture, or surface design;
- modeled lighting or volume-rendering shadows;
- clean final contour;
- labels, bullet lists, callouts, notes, or camera diagrams;
- multiple panels or stages;
- a presentation-sheet composition.

Fail when visual density is closer to Stage 1 or Stage 2 than to the accepted
Stage 0 precedent.

A passing Stage 0 must show:

- readable framing;
- readable overall gesture;
- readable silhouette;
- readable major mass placement;
- readable broad special-feature paths;
- unresolved internal structure;
- low information density;
- a disposable exploratory character.

On failure:

- do not present the candidate;
- do not reuse it as the next stage;
- do not polish or trace it;
- generate a new Stage 0 from scratch.

On pass:

- present Stage 0 only;
- stop for user approval, rejection, or revision.

## Stage 1 — Composition clarification

Stage 1 may clarify the approved camera, gesture, silhouette, proportion, and
major overlaps.

It must preserve the approved Stage 0 decision.

Stage 1 may not introduce final anatomy, surface design, texture, or rendering.

## Stage 2 — Construction

Stage 2 may resolve body construction, anatomy, joint chains, appendage
attachments, spatial overlap, and functional endpoints.

Stage 2 must remain construction-focused. It may not drift into final surface
design or rendering.

Reject Stage 2 when detail, lighting, texture, or contour finish makes it read
closer to Stage 3.

## Stage 3 — Design refinement

Stage 3 may clarify anatomy, contour, creature design, local features, and
surface decisions while preserving the approved structure.

Before leaving Stage 3, lock:

- camera and crop;
- major silhouette;
- joint rotations;
- appendage paths;
- prop contacts;
- functional endpoints.

## Stage 4 — Final rendering

Stage 4 may amplify:

- lighting;
- materials;
- atmosphere;
- texture;
- edge control;
- focal hierarchy;
- cinematic impact.

Stage 4 may not:

- invent new joint rotations;
- change the major silhouette;
- alter camera or crop without approval;
- move prop contacts;
- alter appendage paths;
- change functional endpoints.

Inspect joint chains and functional endpoints before final acceptance.

## Chimera Stage 0 contract

For the Chimera regression request, Stage 0 must show only:

- one lion-body mass and its action;
- two side-by-side head-location shapes;
- two separate neck paths;
- broad bat-wing spread and attachment regions;
- one tail path continuing into a serpentine path;
- balance, weight, framing, and silhouette.

It must not show:

- resolved lion or goat faces;
- a designed mane;
- designed horns;
- detailed paws or claws;
- wing-finger or membrane anatomy;
- a rendered snake head;
- scales, fur, or anatomical torso construction;
- annotations or a process sheet.

### Canonical Chimera Stage 0 tool instruction

Create a single rough marker thumbnail for a Chimera.

This is Stage 0: a minimal-commitment composition and silhouette study only.
Use blunt body masses and loose gestural paths on a plain white page.

Show one lion-body mass with clear weight and action; two side-by-side
head-location shapes on separate neck paths; two broad bat-wing spread shapes
with only their attachment regions indicated; and one lion-tail path continuing
into a serpentine path.

Keep all forms unresolved. Do not draw anatomy, facial features, mane detail,
horn detail, paws, claws, wing fingers, membranes, scales, fur, modeled shading,
construction diagrams, labels, notes, or a process-sheet layout.

Generate one thumbnail only. Do not polish it.
