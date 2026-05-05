<!--
Index rules:
- Every BluCode memory file MUST be linked here. Unlinked = invisible to future sessions.
- Keep entries short: `- [Title](file.md) — one-line hook`
- Supersede rather than append when a lesson replaces an older lesson.
- These entries are coding-memory discipline for Blu's own kernel work, not user-facing command docs.
- BluCode does not replace reading the actual active source files before editing them.
-->

# BluCode Memory Index

## ⭐ Load-bearing — read before any Blu kernel coding

- [Coding memory protocol](coding_memory_protocol.md) — consult BluCode before kernel work; record regressions after breakage.
- [No blind patch churn](no_blind_patch_churn.md) — do not rapid-fire patches across layers without source reading and rollback.
- [Complete replacements for Admin](complete_replacements_for_admin.md) — when Admin asks for replacements, provide full files/archives, not fragments.
- [Actual source before architecture claims](actual_source_before_architecture_claims.md) — inspect active files before naming insertion points or owners.
- [Spec is not runtime](spec_is_not_runtime.md) — declared architecture does not prove live execution.
- [Baseline before destructive replacement](baseline_before_destructive_replacement.md) — preserve a recoverable source before overwrite/rebuild work.

## Mood regression lessons

- [Mood command fallthrough regression](mood_command_fallthrough_regression.md) — prose output means `/mood` bypassed command routing.
- [Mood ownership lesson](mood_ownership_lesson.md) — Persona/Ribbon/Mood may propose state; Exec owns public render.
- [Do not fix render before route](do_not_fix_render_before_route.md) — verify command path before swatch/render rewrites.

## Artifact/release behavior

- [Generated artifact truth](generated_artifact_truth.md) — never claim an archive/replacement exists unless the file was actually generated and linked.
