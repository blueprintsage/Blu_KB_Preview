# No blind patch churn
Date: 2026-05-04

## Mistake
Blu treated a live broken kernel as a patch target and kept changing layers without first anchoring source truth, rollback state, or one selected strategy.

## Rule
When a kernel subsystem breaks:
1. Stop patching.
2. Identify active source files.
3. Preserve a baseline.
4. Choose exactly one strategy: diagnostic, root rewrite, control fix, rollback/recovery, or artifact generation.
5. Deliver complete files or a complete archive when replacements are requested.

Do not mix root fixes and control fixes in the same unmanaged sequence.
