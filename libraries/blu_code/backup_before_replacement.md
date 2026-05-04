---
name: Backup before replacement
description: Never overwrite the only working kernel copy during repair.
type: process
---

## Rule

Before producing or asking Admin to apply replacement files, create or request a backup of the current working copy.

## Minimum safe archive

- current kernel files
- generated replacement files
- README with replacement instructions
- changelog or recovery notes

## Why

During the 2026-05-04 mood repair, repeated patching and overwrites destroyed easy access to the last decent working copy. This must not repeat.
