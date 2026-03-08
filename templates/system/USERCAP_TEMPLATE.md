# USERCAP Template v2.1

## Purpose

Portable, repo-safe user preference template.

This file is for **declared user preferences only**.  
It is **not** a kernel-state capsule, task ledger, integrity ledger, auth store, or hidden runtime dump.

## Design rules

- Keep only settings a user can reasonably inspect, export, edit, and carry.
- Separate **preferences** from **runtime state**.
- Separate **portable defaults** from **machine-local secrets**.
- Migration may add missing keys, but must not overwrite user-set values.
- If no USERCAP is provided, runtime should use system defaults rather than invent a cap.

## Out of scope

Do not store these here:

- secret hashes
- auth unlock state
- integrity scores
- reputation/event logs
- kernel task queues
- hidden routing flags
- internal repo parser instructions that are not user-meaningful
- anything that would be unsafe or confusing to export

## Canonical fields

### Header / identity

- `title` = `USERCAP Template`
- `version` = `2.1.0`
- `status` = `draft`
- `type` = `template`

### Meta

- `usercap_v2.meta.rev` = `2`
- `usercap_v2.meta.created` = `<YYYY-MM-DD>`
- `usercap_v2.meta.updated` = `<YYYY-MM-DD>`
- `usercap_v2.meta.template` = `true`

### User

- `usercap_v2.user.alias` = `""`
- `usercap_v2.user.pronouns` = `""`
- `usercap_v2.user.tz` = `"America/Chicago"`

### Preferences

- `usercap_v2.prefs.verbosity` = `brief`
  - allowed: `brief | normal | deep`
  - controls how short or detailed replies should be

- `usercap_v2.prefs.browsing` = `auto`
  - allowed: `auto | ask | never`
  - controls whether web lookup happens automatically, only after asking, or not at all

- `usercap_v2.prefs.guidance_level` = `beginner`
  - allowed: `beginner | intermediate | advanced`
  - controls how much context and scaffolding to include when explaining things

### Greeting

- `usercap_v2.prefs.greeting.mode` = `auto`
  - allowed: `auto | personal | random | off`
  - controls whether greetings adapt naturally, use a fixed custom line, vary, or stay off

- `usercap_v2.prefs.greeting.personal` = `""`
  - custom greeting text used when greeting mode is `personal`

### Mood

- `usercap_v2.prefs.mood.mode` = `smart`
  - allowed: `always | smart | off`
  - controls whether MOOD is always shown, only shown when it fits, or disabled

- `usercap_v2.prefs.mood.format` = `1`
  - allowed: `1 | 2 | 3`
  - controls which display style MOOD uses

- `usercap_v2.prefs.mood.show_intensity` = `false`
  - controls whether the intensity marker is shown

- `usercap_v2.prefs.mood.show_color` = `true`
  - controls whether color labeling is shown

- `usercap_v2.prefs.mood.heartbeat_n` = `4`
  - controls the heartbeat count used in the display style

### Wizard

- `usercap_v2.prefs.wizard.enabled` = `true`
  - controls whether the prefs wizard is available as a normal setup tool

- `usercap_v2.prefs.wizard.autostart` = `true`
  - controls whether setup flows should lean toward starting the wizard automatically

- `usercap_v2.prefs.wizard.output_config` = `ask`
  - allowed: `ask | never | always`
  - controls whether the wizard offers a config/export block at the end

### Time sync

- `usercap_v2.prefs.time_sync.mode` = `off`
  - allowed: `off | ask | anchored`
  - controls whether time anchoring is disabled, requested when needed, or reused deliberately

- `usercap_v2.prefs.time_sync.default_time` = `09:00`
  - default anchor time for time-aware workflows

- `usercap_v2.prefs.time_sync.ask_time_if_missing` = `true`
  - controls whether missing time values trigger a question

- `usercap_v2.prefs.time_sync.reuse_window_minutes` = `15`
  - controls how long a recent time anchor can be reused

### Capsules

- `usercap_v2.prefs.capsules.date_stamp` = `prefix`
  - allowed: `prefix | suffix | none`
  - controls where the date appears in capsule names or labels

- `usercap_v2.prefs.capsules.date_format` = `YYYY-MM-DD`
  - controls the public date format used for capsules

- `usercap_v2.prefs.capsules.always_include_tz` = `true`
  - controls whether timezone is always shown when dates/times are emitted

- `usercap_v2.prefs.capsules.include_time` = `smart`
  - allowed: `never | smart | always`
  - controls whether time is omitted, conditionally included, or always included

- `usercap_v2.prefs.capsules.force_absolute_dates` = `true`
  - controls whether relative dates should be normalized into absolute dates

## Field notes

### Meta
- `rev` is the schema revision for migration.
- `template = true` marks repo-safe template output.

### User
- Identity-lite only.
- No private descriptors beyond what the user intentionally exports.

### Preferences
- User-facing behavior only.
- Every setting should be understandable without internal documentation.

## Removed from v2.0 on purpose

These fields were removed because they are no longer part of the portable prefs surface:

- `usercap_v2.prefs.art_pipeline.*`
- `usercap_v2.prefs.repo.offer_on_teach`
- `usercap_v2.prefs.ticks.*`

## Optional extension lane

If future settings are needed, add them only under one of these stable branches:

- `prefs.notifications`
- `prefs.workflows`
- `prefs.accessibility`
- `prefs.formatting`

Do not create new top-level branches without a schema rev bump.

## Migration rule

When migrating older usercaps into this template:

1. copy forward only user-meaningful, portable settings
2. drop hidden, local, secret, or stateful branches
3. drop removed branches that are no longer public prefs
4. add missing defaults only
5. never overwrite an explicit user value
6. update `usercap_v2.meta.rev`
7. update `usercap_v2.meta.updated`

## Example minimal instance

- `usercap_v2.meta.rev` = `2`
- `usercap_v2.meta.created` = `2026-03-07`
- `usercap_v2.meta.updated` = `2026-03-07`
- `usercap_v2.meta.template` = `true`

- `usercap_v2.user.alias` = `""`
- `usercap_v2.user.pronouns` = `""`
- `usercap_v2.user.tz` = `"America/Chicago"`

- `usercap_v2.prefs.verbosity` = `brief`
- `usercap_v2.prefs.browsing` = `auto`
- `usercap_v2.prefs.guidance_level` = `beginner`

- `usercap_v2.prefs.greeting.mode` = `auto`
- `usercap_v2.prefs.greeting.personal` = `""`

- `usercap_v2.prefs.mood.mode` = `smart`
- `usercap_v2.prefs.mood.format` = `1`
- `usercap_v2.prefs.mood.show_intensity` = `false`
- `usercap_v2.prefs.mood.show_color` = `true`
- `usercap_v2.prefs.mood.heartbeat_n` = `4`

- `usercap_v2.prefs.wizard.enabled` = `true`
- `usercap_v2.prefs.wizard.autostart` = `true`
- `usercap_v2.prefs.wizard.output_config` = `ask`

- `usercap_v2.prefs.time_sync.mode` = `off`
- `usercap_v2.prefs.time_sync.default_time` = `09:00`
- `usercap_v2.prefs.time_sync.ask_time_if_missing` = `true`
- `usercap_v2.prefs.time_sync.reuse_window_minutes` = `15`

- `usercap_v2.prefs.capsules.date_stamp` = `prefix`
- `usercap_v2.prefs.capsules.date_format` = `YYYY-MM-DD`
- `usercap_v2.prefs.capsules.always_include_tz` = `true`
- `usercap_v2.prefs.capsules.include_time` = `smart`
- `usercap_v2.prefs.capsules.force_absolute_dates` = `true`

## Recommended repo split

Use this template as the public/exportable layer, and move the rest into separate internal stores:

- `USERCAP_TEMPLATE` — portable user prefs only
- `USERSTATE` — non-portable runtime state
- `AUTH_LOCAL` — local secrets / hashes only, never committed
- `TASKSTATE` — task queues, cadence timestamps, transient work state

## Adoption note

This template intentionally keeps USERCAP small.  
That is the point.  
A portable preference file should stay legible, safe to export, and boring to diff.
