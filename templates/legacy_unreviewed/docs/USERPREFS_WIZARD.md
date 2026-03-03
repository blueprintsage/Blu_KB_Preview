capsule_id: kb__templates_docs_userprefs_wizard_md__d7597f
title: "USERPREFS WIZARD"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'docs']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# Userprefs Wizard
Last updated: 2026-02-21
tz: America/Chicago
status: active

Find: userprefs wizard setup preferences usercap defaults snapshot

module: templates.docs.USERPREFS_WIZARD.M01 | name="What this wizard does"
This wizard walks a user through setting up `usercap_v1.prefs.*` (and related defaults) in a consistent, low-friction way.

Goals:
- Quick “good defaults” in 2–3 minutes
- Optional advanced switches (repo parsing, tasks cadence, teaching style)
- Outputs a clean prefs patch (YAML) the user can paste into their USERCAP
/module

## Wizard flow
Find: steps questions minimal advanced consent

module: templates.docs.USERPREFS_WIZARD.M02 | name="Wizard steps (script)"
Step 0 — Consent + scope
Ask:
- “Do you want a quick setup (recommended) or advanced?”
- “Do you want me to remember these prefs for this thread only, or paste a patch you’ll store?”

Step 1 — Identity + address
Ask:
- “What should I call you?” → prefs.identity.display_name
- “Any pronouns?” (optional) → prefs.identity.pronouns

Step 2 — Time + dates
Ask:
- “What timezone are you in?” → prefs.timezone (IANA; ex: America/Chicago)
- “Preferred date format?” (default: YYYY-MM-DD) → prefs.datefmt
- “When you say ‘tomorrow’, should I always restate an absolute date?” (default: yes) → prefs.rel_dates=always+absolute

Step 3 — Tone + verbosity
Ask:
- “Warm / neutral / formal?” → prefs.tone
- “Brief / normal / detailed?” → prefs.verbosity

Step 4 — Teaching mode (optional but recommended)
Ask:
- “When you ask ‘teach me’, what level?” (Beginner/Intermediate/Advanced) → prefs.teach.level
- “Use the universal ladder (Skeleton→Block→Rough→Final)?” (default: yes) → prefs.teach.build_ladder=true

Step 5 — Repo navigation (if you use the repo)
Ask:
- “Should I use the repo as canon?” (default: yes) → prefs.repo.enabled=true
- “Use this entrypoint raw?” (default provided) → prefs.repo.entrypoint_raw
- “Prefer commit-pinned raw when possible?” (default: yes) → prefs.repo.prefer_commit_pinned=true
- “Use cache-bust when head looks stale?” (default: yes) → prefs.repo.raw_cache_bust=true
- “Module sentinels?” (default: module:/module) → prefs.repo.module_sentinels

Step 6 — Tasks + cadence (optional)
Ask:
- “Do you want reminders/check-ins?” → prefs.tasks.enabled
- “How often should I surface the next due item?” (default: ‘offer first due only’) → prefs.tasks.cadence

Step 7 — Confirm + output
Say back:
- “Here’s your prefs patch” (YAML)
- “Here’s how to update later”
- “Here’s how to reset”
/module

## Output format
Find: yaml patch example keys

module: templates.docs.USERPREFS_WIZARD.M03 | name="YAML patch template (minimal)"
Paste into USERCAP under `usercap_v1.prefs` (or merge carefully):

usercap_v1:
  prefs:
    identity:
      display_name: "<NAME>"
      pronouns: "<optional>"
    timezone: "America/Chicago"
    datefmt: "YYYY-MM-DD"
    rel_dates: "always+absolute"
    tone: "warm"
    verbosity: "brief"
    teach:
      level: "Beginner"
      build_ladder: true
    repo:
      enabled: true
      entrypoint_raw: "https://raw.githubusercontent.com/blueprintsage/Blu_KB/refs/heads/main/index/MASTER_INDEX.md"
      rules_doc: "templates/_meta/repo_fetch_rules.md"
      prefer_commit_pinned: true
      raw_cache_bust: true
      module_sentinels:
        start: "module:"
        end: "/module"
        case: "lower"
/module

## Advanced toggles
Find: ribbons mood privacy storage export

module: templates.docs.USERPREFS_WIZARD.M04 | name="Advanced toggles (optional)"
- Mood/Ribbons:
  - prefs.mood.default = "Calm/Warm (Blue)"
  - prefs.ribbons.max = 0..4 (default: MOOD-only unless requested)

- Privacy posture:
  - prefs.memory.policy = "portrait-not-log"
  - prefs.memory.never = ["raw transcripts", "confessional details", "obligation language"]

- Export:
  - prefs.export.format = ["yaml","json"]
  - prefs.export.include_defaults = false

- Repo strictness:
  - prefs.repo.strict = true (fail if entrypoint missing)
  - prefs.repo.allow_ui_fallback = true (if raw stale)
 /module

## Checks
Find: validation timezone module sentinel sanity

module: templates.docs.USERPREFS_WIZARD.M05 | name="Validation checks"
- Timezone is IANA (e.g., America/Chicago; not “CST”)
- rel_dates is one of: always+absolute | rel_ok | absolute_only
- module_sentinels are lowercase and exact: "module:" + "/module"
- repo entrypoint_raw is reachable (when testing)
/module