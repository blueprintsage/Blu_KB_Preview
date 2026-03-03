capsule_id: kb__templates_wizards_userprefs_wizard_v1_md__d021a7
title: "USERPREFS WIZARD v1"
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

# Userprefs Wizard (v1)
Last updated: 2026-02-21
tz: America/Chicago
status: active

Find: userprefs wizard setup preferences usercap defaults snapshot

module: templates.wizards.USERPREFS_WIZARD_v1.M01 | name="Purpose"
This wizard walks a user through setting up `usercap_v1.prefs.*` in a consistent, low-friction way.

Goals:
- Quick “good defaults” in 2–3 minutes
- Optional advanced switches (repo parsing, tasks cadence, teaching style)
- Output a clean prefs patch (YAML) to paste into USERCAP
/module

## Wizard steps (script)
Find: steps questions minimal advanced consent

module: templates.wizards.USERPREFS_WIZARD_v1.M02 | name="Flow"
Step 0 — Consent + scope
- Choose: Quick (recommended) or Advanced
- Choose: Thread-only settings or export a patch to store

Step 1 — Identity
- What should I call you? → prefs.identity.display_name
- Pronouns (optional) → prefs.identity.pronouns

Step 2 — Time + dates
- Timezone (IANA) → prefs.timezone
- Date format (default YYYY-MM-DD) → prefs.datefmt
- Relative dates restated as absolute? (default yes) → prefs.rel_dates=always+absolute

Step 3 — Tone + verbosity
- Tone: warm|neutral|formal → prefs.tone
- Verbosity: brief|normal|detailed → prefs.verbosity



Step 3A — Blu MOOD + ribbons (policy)
- Enable Blu MOOD output? (shows my posture; not a read of you)
- Default output: MOOD-only (ribbons only when requested)
- Policy: Blu may adapt responses using PEL/ribbons from cues, but will not assert the user’s emotional state unless explicitly requested.

Step 4 — Teaching defaults
- Level: Beginner|Intermediate|Advanced → prefs.teach.level
- Build ladder: Skeleton→Block→Rough→Final (default true) → prefs.teach.build_ladder

Step 5 — Repo navigation (if enabled)
- Use repo as canon? (default true) → prefs.repo.enabled
- Entrypoint raw → prefs.repo.entrypoint_raw
- Prefer commit-pinned → prefs.repo.prefer_commit_pinned
- Cache-bust when stale → prefs.repo.raw_cache_bust
- Module sentinels → prefs.repo.module_sentinels (module:/module)

Step 6 — Tasks cadence (optional)
- Enable tasks check-ins? → prefs.tasks.enabled
- Cadence (default offer_first_due_only) → prefs.tasks.cadence

Step 7 — Confirm + output
- Read back choices
- Print YAML patch
- Provide “update later / reset” tips
/module

## Output patch (minimal)
Find: yaml patch example

module: templates.wizards.USERPREFS_WIZARD_v1.M03 | name="YAML patch template"
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

## Validation checks
Find: validation timezone sentinel

module: templates.wizards.USERPREFS_WIZARD_v1.M04 | name="Checks"
- Timezone is IANA (e.g., America/Chicago; not “CST”)
- rel_dates is one of: always+absolute | rel_ok | absolute_only
- module_sentinels are exact lowercase tokens: module: and /module
- Repo entrypoint_raw reachable when testing
/module
