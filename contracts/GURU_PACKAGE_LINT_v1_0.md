# GURU:PACKAGE_LINT — Spec — v1.0.0

CAPSULE HEADER v1.1 (NO-YAML)
capsule_id: blu__guru_package_lint
title: GURU:PACKAGE_LINT — Spec
date: 2026-03-05
updated: 2026-03-05
version: 1.0.0
status: active
topic: ops
type: spec
tags: [guru, lint, zip, naming]
sensitivity: high
visibility: shared
source: doc
domain: ops
schema: capsule_header_block_v1.1
body_schema: blu_modular_v1
END CAPSULE HEADER

module: blu__guru.packagelint.M01 | name="Purpose (HARD)"
Validate archive naming rules before output:

- Kernel ZIP: `<YYYY-MM-DD>_<HHMM>_<Name>_<version>.zip`
- Repo/KB/skills ZIP: `<YYYY-MM-DD>_<HHMM>_<Name>.zip`

On failure: emit `ERR:ZIP_NAME_NONUNIFORM` (or `ERR:KERNEL_ZIP_VERSION_MISSING` if you want a dedicated macro) and STOP.
/module
