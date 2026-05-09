# BC-SKILL-020 Mandatory Changelog for Kernel Archives

status: active
created: 2026-05-08
category: patch discipline

## Pattern

A kernel archive is built without a matching changelog entry.

## Rule

Every kernel archive, hotfix, release package, migration package, or component archive must include a current changelog entry. A package without a changelog entry is incomplete.

## Checks

- Does the archive include a changelog?
- Does it name changed components?
- Does it state behavioral impact?
- Does it list affected routes/contracts and tests?
- Does changelog truth match packaged files?

## Tests

- R-build archive without changelog fails package validation.
- ErrorMacros archive has its own changelog when packaged separately.
