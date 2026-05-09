# BC-SKILL-015 Error Macro Catalog Law

status: active
created: 2026-05-08
category: validation/tests

## Pattern

Components invent local failure prose, causing duplicated, drifting, or inconsistent errors.

## Rule

Every deterministic failure must carry a stable `error_code` and compact `failure_reason`. Canonical user-facing error wording belongs in `/libraries/error_macros/ERROR_MACROS_CATALOG.md`.

Any component patch that adds or changes terminal failure codes must update the ERMAC catalog in the same package. ErrorMacros should be packaged as a separate archive when practical.

## Checks

- Does the packet include `error_code`?
- Is the code present in the ERMAC catalog?
- Did the component avoid inventing new prose?

## Tests

- RepoBoot source-binding failure emits `ERR.REPOBOOT.SOURCE_BINDING_FAILED`.
- Terminal packet invalid emits a stable Exec error code.
- Auth exact-render failure does not paraphrase.
