---
capsule_id: <capsule_id>
title: "<capsule title>"
date: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
version: <x.y.z>
status: active  # draft|active|locked
topic: blu
type: spec
tags: [<tag1>, <tag2>]
sensitivity: <low|med|high|critical>
visibility: <shared|private>
source: doc
domain: <core|ops|teach|security>
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# <capsule title>

## Capsule Canon

module: <capsule_id>.M00 | name="Capsule Canon"
- Purpose:
  - <plain-language purpose>
- Owns:
  - <authoritative responsibilities>
- Does not own:
  - <explicit non-ownership boundaries>
- Notes:
  - <hosted/runtime constraints if relevant>
/module

## <human module header>

module: <capsule_id>.M01 | name="<human module header>"
- <rule or spec content>
/module

## <human module header>

module: <capsule_id>.M02 | name="<human module header>"
- <rule or spec content>
/module
