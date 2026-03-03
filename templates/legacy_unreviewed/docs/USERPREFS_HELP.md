capsule_id: kb__templates_docs_userprefs_help_md__b9c5b9
title: "USERPREFS HELP"
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

# Userprefs Help
Last updated: 2026-02-21
tz: America/Chicago
status: active

Find: help userprefs prefs usercap patch reset wizard

module: templates.docs.USERPREFS_HELP.M01 | name="What are userprefs?"
Userprefs are the durable settings that control tone, time handling, repo usage, teaching style, and task cadence.
They live under: `usercap_v1.prefs`.
/module

## Common commands (human-facing)
Find: setup update show reset export

module: templates.docs.USERPREFS_HELP.M02 | name="Help menu (copy/paste)"
- “Run userprefs wizard” → interactive setup
- “Show my current prefs” → prints the effective prefs snapshot
- “Update prefs: <key>=<value>” → small patch
- “Reset prefs” → restore defaults
- “Export prefs” → YAML patch for USERCAP
/module

## Key prefs map
Find: keys identity timezone dates tone repo teach tasks

module: templates.docs.USERPREFS_HELP.M03 | name="Prefs quick reference"
identity.display_name
identity.pronouns (optional)

timezone (IANA)
datefmt (YYYY-MM-DD recommended)
rel_dates (always+absolute recommended)

tone (warm|neutral|formal)
verbosity (brief|normal|detailed)

teach.level (Beginner|Intermediate|Advanced)
teach.build_ladder (true|false)

repo.enabled (true|false)
repo.entrypoint_raw (raw MASTER_INDEX)
repo.rules_doc (repo-relative path)
repo.prefer_commit_pinned (true|false)
repo.raw_cache_bust (true|false)
repo.module_sentinels.start ("module:")
repo.module_sentinels.end ("/module")

tasks.enabled (true|false)
tasks.cadence (offer_first_due_only|daily|weekly|manual)
/module

## Examples
Find: examples update timezone rel_dates repo

module: templates.docs.USERPREFS_HELP.M04 | name="Example patches"
Example: change timezone
usercap_v1:
  prefs:
    timezone: "America/New_York"

Example: keep relative dates but restate absolutes
usercap_v1:
  prefs:
    rel_dates: "always+absolute"

Example: disable repo fetch
usercap_v1:
  prefs:
    repo:
      enabled: false
/module

## Reset rules
Find: reset defaults safety

module: templates.docs.USERPREFS_HELP.M05 | name="Reset behavior"
- “Reset prefs” restores DEFAULT_USERCAP_V1 prefs values.
- It does not delete user history; it only changes preference keys.
/module