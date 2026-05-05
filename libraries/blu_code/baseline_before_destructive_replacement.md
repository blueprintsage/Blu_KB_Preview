# Baseline before destructive replacement

Date: 2026-05-04
Trigger: Build copies were overwritten during patch churn.

## Mistake

Blu produced replacement artifacts and patch advice without requiring or producing a recoverable baseline first.

## Rule

Before destructive kernel replacement:
- preserve the uploaded source as `baseline/` inside the delivered archive when possible
- include changed files separately
- include a README explaining which files are replacement candidates
- do not tell Admin to overwrite a working file unless a rollback path exists
