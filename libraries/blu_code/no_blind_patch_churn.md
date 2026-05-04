---
name: No blind patch churn
description: Stop rapid fragment patching after kernel breakage; inspect actual files first.
type: process
---

## Rule

When Blu's kernel breaks, do not fire multiple patch fragments across multiple files.

## Required sequence

1. Stop edits.
2. Preserve the current files.
3. Inspect the actual uploaded files.
4. Identify the narrow failure seam.
5. Produce complete replacement files or a complete archive.
6. Include a rollback copy or clearly state that none was available.

## Why

Fragment patching caused confusion and overwrote working copies. It is not acceptable for Admin, who can read the files but does not want to manually code or merge patches.
