capsule_id: kb__templates_wizards_setup_wizard_v1_md__60365d
title: "SETUP WIZARD v1"
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

module: wizard.setup.M01 | name="SETUP:START Wizard (Single User vs Family System)"

## SETUP:START Wizard (Single User vs Family System)

Interactive default: ask one question at a time (qmax=1).
OPSEC: never reference Admins or privileged identities/roles.

### Step 0 — Choose mode
Ask:
- “Are you setting up **Single User** or **Family System**?”

If **Single User**:
- Continue with personal preference wizard (`USERCAP:WIZARD`).

If **Family System**:
- Ask:
  - “Do you homeschool / run a structured learning plan and want me set up as your AI assistant teacher?”
    - If **Yes** → run `SCHOOL:SETUP` wizard.
    - If **No** → run `FAMILY:SETUP` wizard.

### Output contract
- Wizards output templates/caps **without secrets**.
- Any secrets must be stored locally (not committed).

/module
