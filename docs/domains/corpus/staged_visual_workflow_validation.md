# Staged Visual Workflow Validation — 2026-08-03

status: accepted guided findings
owner: docs/domains/corpus

## Decision

Adopt approval-gated staged visual production as the default for open-ended drawing requests:

`Stage 0 only → approval → Stage 1–4 walkthrough → approval → standalone Stage 4 → drift inspection`.

Before and after every stage, compare the artifact with the approved same-stage visual precedent and the next-stage ceiling. Reject a stage that resembles the next stage more closely than its own.

## Positive calibration sources

- `source_staged_figure_process_1.png`: framework → blocking → rough form → final line art.
- `source_staged_dragon_process.png`: nonhuman articulated framework → primitive block → organic development → rendered final.
- `source_staged_alien_process.png`: organic invented anatomy across the same four functions.
- `precedent_stage0_dragon_marker_thumbnail.png`: approved Stage 0 marker-density target.

## Guided validation cases

### Warbot

Successes: simple Stage 1 locator, strong Stage 3, compelling Stage 4, high overall continuity.

Failures to retain: Stage 2 borrowed too much Stage 3 information; standalone finals changed subject-to-frame scale and crop; firing effects did not reliably follow the muzzle axis.

### Zero-gravity astronaut

Successes: difficult camera and zero-gravity action remained globally coherent; Stage 4 amplification improved impact, lighting, depth, and atmosphere.

Failures to retain: Stage 2 remained slightly over-rendered; the standalone final introduced localized left-leg drift across hip, knee, ankle, and foot.

## Operational distinction

- Global drift changes the picture and is rejected.
- Local drift damages a part and may be repaired without discarding successful presentation.
- A full standalone Stage 4 render is not the same operation as extracting or enlarging a process-sheet panel.
