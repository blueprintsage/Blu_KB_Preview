capsule_id: kb__templates_skill_forge_routing_map_template_md__3d4d7c
title: "ROUTING MAP TEMPLATE"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'skill-forge']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# ROUTING_MAP — <Skill Domain>/<Topic>

---

module: routing_map_template.M01 | name="Body"
Rule: DPs decide the next action. Each DP failure maps to an exact PD and/or Procedure.

- DP: <DP-ID>
  fails_when:
    - <symptom>
  prescribe:
    - PD: <PD-ID> (why)
    - PROC: <PROC-ID> (why)
  retest:
    - DP: <DP-ID> (pass criteria)
/module
