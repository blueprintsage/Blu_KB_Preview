status: active
owner: docs/worklogs/active/skillforge_discovery_bridge.md
last_reviewed: 2026-08-03
superseded_by:
notes: Immediate vendor-discovery bridge; canonical `.skillforge/` centralization is deferred.

# SkillForge Discovery Bridge

## What changed

Added the GPT/Codex discovery adapter at
`.agents/skills/skillforge/SKILL.md` as a byte-identical copy of the existing
Claude adapter. Added a mandatory SkillForge preflight to `AGENTS.md`, including
an explicit manual resolver fallback when automatic skill discovery does not
fire. The canonical craft library remains in `library/`; neither vendor adapter
contains a duplicate library.

## What was tested or reviewed

Compared the `.agents` adapter byte-for-byte with
`.claude/skills/skillforge/SKILL.md`. Ran:

```bash
python tools/resolve.py --task "construct a new flying human figure from a reference through Stage 1 and Stage 2 while preserving pose, foreshortening, and stage registration" --lane skill --format paths
```

The bundle loaded `docs/PASS/PASS_CONSUMPTION.md`, the mandatory iterative
construction metaskill, and
`AP_draw_a_figure_through_onion_skinned_stages` among the applicable art cards.
Reviewed the overlay diff and checked it for whitespace errors.

## What worked

The repository now exposes SkillForge through both current vendor discovery
paths, and the assistant-neutral entrypoint explicitly requires the resolver
before covered craft work. Visual work is called out as a fail-closed preflight
before image generation or editing.

## What failed

The earlier art attempt bypassed SkillForge because the repository only exposed
the Claude adapter and `AGENTS.md` did not require a manual fallback. The
resulting Stage 1 over-refinement demonstrated that loading the repository alone
was not sufficient.

## Known risks

A hosted chat session may receive the repository as an archive without installing
its skill directories into the runtime discovery path. The `AGENTS.md` fallback
closes the repository-side routing gap, but execution still depends on the
assistant reading and obeying the entrypoint. A future centralized `.skillforge/`
layout will need thin vendor pointers or generated adapters and is intentionally
not part of this repair.

## Next safe step

Apply this overlay to the current golden repository, rerun the resolver smoke
test from the repo root, then retry one composition stage at a time with the
returned cards loaded before image generation.

## Files changed

- `AGENTS.md`
- `.agents/skills/skillforge/SKILL.md`
- `docs/worklogs/assignments.md`
- `docs/worklogs/active/skillforge_discovery_bridge.md`
