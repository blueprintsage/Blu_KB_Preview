# GURU:HEADER_LINT — Spec — v1.0.0

CAPSULE HEADER v1.1 (NO-YAML)
capsule_id: blu__guru_header_lint
title: GURU:HEADER_LINT — Spec
date: 2026-03-05
updated: 2026-03-05
version: 1.0.0
status: active
topic: ops
type: spec
tags: [guru, lint, headers, versions]
sensitivity: high
visibility: shared
source: doc
domain: ops
schema: capsule_header_block_v1.1
body_schema: blu_modular_v1
END CAPSULE HEADER

module: blu__guru.headerlint.M01 | name="Purpose (HARD)"
Prevent stale headers by enforcing:
- title + header block present when required
- `updated` is current when body changes
- `version` bumped appropriately (SemVer)
- exceptions honored (per Uniformity Standard)
On failure: emit `ERR:HEADER_VERSION_STALE` and STOP.
/module
