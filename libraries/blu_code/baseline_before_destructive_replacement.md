# Baseline before destructive replacement
Date: 2026-05-04

## Mistake
Blu produced replacement artifacts and patch advice without requiring or producing a recoverable baseline first.

## Rule
Before destructive kernel replacement:
- preserve uploaded source as `baseline/` inside the delivered archive when possible
- include changed files separately
- include a README explaining replacement vs reference vs memory-library status
- do not tell Admin to overwrite a working file unless a rollback path exists
