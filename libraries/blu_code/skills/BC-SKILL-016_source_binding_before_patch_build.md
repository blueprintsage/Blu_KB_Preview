# BC-SKILL-016 Source Binding Before Patch or Build

status: active
created: 2026-05-08
category: patch discipline

## Pattern

A patch, diff, build, or archive is produced without verified source binding.

## Rule

Before constructing a patch/build/archive for kernel or repo files, bind the source path and version first. If source binding is missing, stop with the appropriate error code. Do not draft speculative diffs unless the user explicitly asks for a speculative proposal.

BluCode may advise coding practice, but it must not override AntiDrift, RepoBoot source binding, or terminal packet rules.

## Checks

- Which source file/path was bound?
- Was the repo or uploaded archive actually read?
- Was a changelog entry updated?
- Was an artifact actually written before claiming build completion?

## Tests

- `Patch the repo kernel files` with no source binding blocks.
- `Build R4.4 and clean up anything stale` asks/blocks for multi-task and source binding.
- A proposed patch is labeled proposed, not applied.
