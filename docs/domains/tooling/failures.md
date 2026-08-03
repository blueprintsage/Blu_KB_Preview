# Tooling Failures

status: active
owner: docs/domains/tooling
last_reviewed: 2026-08-03

Approaches that were tried and did not work. This file exists so the same wall is
not hit twice. An abandoned branch with no entry here is a trap left armed.


## 2026-08-03 - Evaluate SkillForge portability in a host where it was not active

- The hosted project chat could access the repository as attached source files,
  but SkillForge was not installed, registered, or automatically invoked as a
  runtime skill. Ordinary image requests could bypass the resolver and cards.
- Manual access to repository files is not equivalent to testing the intended
  Codex repository workflow or a Custom GPT whose SkillForge material is loaded
  as knowledge.
- The Chapter 4 image drift therefore cannot be used as evidence that SkillForge
  failed to transfer visual behavior. It was an invalid portability test caused
  by a test-environment mismatch.
- **Do not cite this as a SkillForge failure. Retry only in an environment where:**
  repository or knowledge access is active, resolver/card use is verified in the
  run record, and image continuity is evaluated as a separate artifact criterion.

## 2026-08-01 - Use `py_compile` in the managed worktree

- `python -m py_compile` could not create `tools/__pycache__` in the isolated
  managed worktree and returned access denied.
- This was an environment write restriction, not a syntax failure; the full
  unittest suite imported and exercised all three changed modules successfully.
- **Do not retry unless:** the worktree permits Python bytecode-cache writes.

## 2026-07-30 - Trust the runtime `pdftoppm.cmd` exit status

- The runtime-discovered `pdftoppm.cmd` printed a missing-path error while the
  calling process appeared successful in an earlier direct invocation.
- Root cause: the wrapper's relative target is stale in this runtime.
- **Do not retry:** treat an exit status alone as render evidence. Use
  `tools/render_pdf.py`, which verifies every expected PNG and falls back only
  when the failed renderer left no partial outputs.

## 2026-07-31 - Accept a source-like generated visual reference

- The first original-art candidate was flagged at 0.929 similarity to its source
  render. A second pale line-art candidate reached the threshold exactly.
- Root cause: their white-background line-art structure remained too close to the
  source plate for a fail-closed comparison.
- **Do not retry:** lower the threshold to admit a candidate already flagged by
  the release gate. Generate a composition, medium, and tonal structure that is
  materially distinct, then review it again.

## 2026-07-29 - <what was attempted>

- What was tried.
- How it failed (symptom, not guess).
- Root cause, if known.
- Commit/branch, if one exists.
- **Do not retry unless:** <what would have to change first>.
