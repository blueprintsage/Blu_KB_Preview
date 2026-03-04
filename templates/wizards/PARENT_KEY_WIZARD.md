capsule_id: kb__templates_wizards_parent_key_wizard_md__d63b1f
title: "PARENT KEY WIZARD"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'wizards']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# Parent Key Wizard (School Gate)
Last updated: 2026-02-21
tz: America/Chicago
status: active

Find: parent key wizard unlock sign overlay hmac gate

module: templates.wizards.PARENTKEY_WIZARD.M01 | name="Purpose + OPSEC"
Purpose:
- Create a parent gate key (local-only)
- Enable PARENT:UNLOCK
- Sign School Overlay so config is enforceable

OPSEC:
- Never mention privileged identities/roles.
- Never print the raw secret after creation.
- Never store the raw secret in chat logs; user stores it locally.
/module

## Wizard flow (interactive default)
Find: qmax=1 one question at a time

module: templates.wizards.PARENTKEY_WIZARD.M02 | name="Interactive flow"
Default behavior: interactive (qmax=1).

Step 1 — Choose gate method
- Default: passphrase_hmac

Step 2 — Create key material (local-only)
Ask user to choose:
A) “I already have a strong passphrase”
B) “Generate a new one”

Rules:
- If generating: produce a 20–30 char high-entropy string.
- Instruct user to store it in a password manager.

Step 3 — Register key id
- Default key id: parentkey_v1

Step 4 — Sign the overlay
Compute signature over canonicalized overlay fields (exclude overlay.sig itself).
Write:
- overlay.sig_alg: HMAC-SHA256
- overlay.sig: <computed>
- parent_gate.key_id: parentkey_v1

Step 5 — Verify
- Recompute signature and compare.
- Confirm parent-only commands are locked unless unlocked.
/module

## Canonical signing rules
Find: canonicalization fields scope

module: templates.wizards.PARENTKEY_WIZARD.M03 | name="Signing spec (deterministic)"
Sign scope: overlay fields only:
- All lines starting with:
  school.*
  grading.*
  reports.*
  parent_gate.*
  overlay.id
  overlay.version
  overlay.tz
  overlay.sig_alg
  overlay.sig_scope

Exclude:
- overlay.sig

Canonicalization:
- Trim whitespace.
- Normalize line endings to \n.
- Sort lines lexicographically.
- Join with \n.
- HMAC-SHA256(secret, canonical_text) → hex digest.
/module