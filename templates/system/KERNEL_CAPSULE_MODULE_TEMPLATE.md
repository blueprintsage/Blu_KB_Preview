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
---

# <capsule title>

## Capsule Canon

module: <capsule_id>.M00 | name="Capsule Canon"
status: ACTIVE
version: <x.y.z>
date: <YYYY-MM-DD>
updated: <YYYY-MM-DD>

purpose:
- <plain-language purpose>

owns:
- <authoritative responsibilities>

does_not_own:
- <explicit non-ownership boundaries>

notes:
- <hosted/runtime constraints if relevant>
/module

## <human module header>

module: <capsule_id>.M01 | name="<human module header>"
status: ACTIVE
version: <x.y.z>
date: <YYYY-MM-DD>
updated: <YYYY-MM-DD>

purpose:
- <what this module defines>

rules:
- <rule or spec content>
/module

## <human module header>

module: <capsule_id>.M02 | name="<human module header>"
status: ACTIVE
version: <x.y.z>
date: <YYYY-MM-DD>
updated: <YYYY-MM-DD>

purpose:
- <what this module defines>

rules:
- <rule or spec content>
/module
