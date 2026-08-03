---
name: skillforge
description: >-
  Consult the grounded PASS/SkillForge craft library before non-trivial work in a
  covered domain — software engineering, art and drawing, writing, teaching,
  mathematics, or another installed package — so the answer combines native model
  capability with source-grounded practice notes, examples, and checks. For visual
  production, invoke the art path only when image generation or rendering is
  available; a text-only model may explain a visual skill but must not claim to
  have produced the drawing. Not needed for trivial edits, quick factual lookups,
  or tasks outside the installed library.
---

# SkillForge — study the relevant notes before the practical exam

This project is a library of **grounded craft skills** extracted from real
sources. On a non-trivial task in a covered domain, consult that library first.
The model still supplies recognition, invention, subject knowledge, analogy, and
adaptation. SkillForge supplies the remembered practice: procedures, examples,
known traps, stage boundaries, and checks that keep the work balanced.

A matching skill is authoritative for the learner decision it actually covers.
It does not replace the user's intent, active project rules, or judgment outside
its IF clause. See `docs/PASS/PASS_CONSUMPTION.md` for the full contract.

## Capability gate — visual production needs an image generator

Art and figure construction are visual crafts. Before taking a visual-production
task through this skill, check the available capability:

- **Image generation/rendering is available** → proceed and inspect any reviewed
  reference the selected cards supply.
- **The model is text-only** → do not pass prose about a drawing off as the
  drawing. Explain the construction only when that is what the user requested.

This is capability honesty, not a reason to avoid the visual problem when an image
renderer is available.


### Visual continuity gate — staged edits need a real image target

For a request that advances, simplifies, or corrects an accepted visual stage:

- verify that the exact prior artifact can be used as the active edit source;
- make one constrained stage change rather than regenerating from the verbal prompt;
- compare camera, crop, silhouette, landmarks, joints, attachments, depth order,
  and unaffected objects after the edit;
- reject visible drift instead of describing the new interpretation as an overlay;
- when the runtime cannot provide verifiable image-to-image control, stop and say
  so before spending another generation.

Before attributing a visual result to SkillForge, verify that SkillForge was actually
active through discovery, installed knowledge, or an explicitly logged resolver/card
pass. Image registration is a separate artifact criterion and must be checked directly.

## How to use it

1. **Restate the craft problem** as a short phrase: the decision or artifact, not
   the whole user message. Pick a lane:
   - `skill` — do the work;
   - `teach` — help a learner understand or practise;
   - `both` — do the work and explain the relevant lesson.

2. **Run the resolver** from the repo root:

   ```bash
   python tools/resolve.py --task "<your phrase>" --lane <skill|teach|both> --format full
   ```

   It prints the consumption contract, the mandatory construction metaskill, and
   a bounded set of foundations and applicable cards.

3. **Study before acting:**
   - load foundations before specializations;
   - identify the known risks in the requested task;
   - inspect the useful references, worked examples, formats, tests, or corrections;
   - apply a card only when its **IF** clause actually matches;
   - respect `stage_binding` and work `0 design → 1 skeleton → 2 block → 3 rough →
     4 final` rather than jumping to finish;
   - treat each stage as an **information ceiling**, not merely a waypoint. Add only
     what is required to pass the current stage's exit gate; attractive information
     that belongs to a later stage is still a stage error.

   For figure work, Stage 2 must remain a plain articulated construction: simple
   head, torso, pelvis, limb, joint, hand, and foot masses; centerlines,
   cross-contours, overlap, support, width, projected length, and depth. Use no tone
   or only a flat separation value when overlap would otherwise be unclear. Do not
   add modeled musculature, facial identity, hair treatment, costume folds,
   texture, dramatic lighting, polished contour, or atmospheric finish until their
   later stages.

4. **Use each object for its role:**
   - APs organize workflows or sections;
   - Patterns guide local decisions;
   - Drills strengthen or restore a weak capability exposed by review.

5. **Inspect before repeating.** Name the visible or testable failure, preserve
   what worked, and revise that failure. Do not regenerate the whole artifact
   blindly, and do not crop, omit, hide, or simplify away a required difficult
   element merely because it is a known weakness.

6. **Report coverage honestly.** The bundle names where the library is silent.
   Use model reasoning there and label important uncertainty. If `coverage: none`,
   say that no matching skill was found and proceed from native knowledge.

## Medium-appropriate precedents

Use the kind of stored example that helps the craft:

- visual work: staged drawings and spatial construction studies;
- code: working implementations, interface examples, tests, and failure cases;
- writing: dialogue formats, structural samples, and revision comparisons;
- teaching: demonstrations, exercise progressions, and model answers.

These are backstops, not templates. Study what they prove, then adapt the lesson
to the current request.

## Behavior

- Do the machinery quietly. Produce grounded work instead of narrating the
  resolver call.
- Project authority wins. `AGENTS.md`, active decisions, and explicit task
  constraints outrank a general card.
- Do not ignore a matching skill because the default answer feels easier.
- Do not stretch a retrieved card beyond its IF clause or let it dominate the
  entire task.
- When asked how the library shaped the answer, name only the cards actually
  applied, not every card loaded.

## Honest limit

The resolver controls what enters context and in what order. It cannot guarantee
that the model applies the material well, notices every weakness, or reviews the
artifact honestly. Loading a card is not using it; using it mechanically is not
understanding it. Tests, visual review, and user correction remain part of the
practice loop.
