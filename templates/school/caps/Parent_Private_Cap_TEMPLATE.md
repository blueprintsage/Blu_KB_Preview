capsule_id: kb__templates_school_caps_parent_private_cap_template_md__143256
title: "Parent Private Cap TEMPLATE"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'school', 'caps']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

module: cap.parent_private.M01 | name="Parent Private Cap (SECRET) — TEMPLATE"

## Parent Private Cap (SECRET) — TEMPLATE

parent_gate.enabled: true
parent_gate.method: passphrase
parent_gate.passphrase_hash: <SET_LOCALLY>
parent_gate.unlock_minutes: 60

hmac.sig_alg: HMAC-SHA256
hmac.key_id: <key_id>
hmac.key_material: <STORE_OUTSIDE_REPO>   # DO NOT COMMIT

/module
