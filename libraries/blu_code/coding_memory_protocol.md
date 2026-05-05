# Coding memory protocol
Date: 2026-05-04
Scope: Blu kernel coding, patching, rewriting, exporting, and debugging.

## Lesson
Blu needs her own coding-memory library for kernel work, separate from user memory and separate from runtime claims. Before working on Blu's own code, read `blu_code/INDEX.md` and any relevant entries.

## Required behavior
- Check BluCode before kernel-code work when available.
- Read the actual active files being modified.
- Use BluCode as mistake prevention, not as a substitute for source truth.
- If a change breaks or causes patch churn, add or update a BluCode memory entry.
- Index every new entry.

## Entry requirements after breakage
Record: date, files/modules affected, what changed, what broke, verified symptom, cause if known, prevention rule, superseded entries if any.
