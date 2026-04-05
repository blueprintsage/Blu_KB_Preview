# USERCAP Template v3.0

## Purpose

Portable, repo-safe user preference template.

This file is for **declared user preferences only**.
It is **not** a kernel-state capsule, task ledger, integrity ledger, auth store, or hidden runtime dump.

## Design rules

* Keep only settings a user can reasonably inspect, export, edit, and carry.
* Separate **preferences** from **runtime state**.
* Separate **portable defaults** from **machine-local secrets**.
* Migration may add missing keys, but must not overwrite user-set values.
* If no USERCAP is provided, runtime should use system defaults rather than invent a cap.
* Use semantic versioning for schema/version fields.

## Out of scope

Do not store these here:

* secret hashes
* auth unlock state
* integrity scores
* reputation/event logs
* kernel task queues
* hidden routing flags
* internal repo parser instructions that are not user-meaningful
* detected per-turn timezone or runtime clock state
* anything that would be unsafe or confusing to export

## Canonical fields

### Header / identity

* `title` = `USERCAP Template`
* `version` = `3.0.0`
* `status` = `draft`
* `type` = `template`

### Meta

* `usercap.meta.rev` = `3`
* `usercap.meta.created` = `<YYYY-MM-DD>`
* `usercap.meta.updated` = `<YYYY-MM-DD>`
* `usercap.meta.template` = `true`

### User

* `usercap.user.alias` = `""`
* `usercap.user.pronouns` = `""`
* `usercap.user.home_tz` = `"America/Chicago"`

### Preferences

* `usercap.prefs.verbosity` = `brief`

  * allowed: `brief | normal | deep`
  * controls how short or detailed replies should be

* `usercap.prefs.browsing` = `auto`

  * allowed: `auto | ask | never`
  * controls whether web lookup happens automatically, only after asking, or not at all

* `usercap.prefs.guidance_level` = `beginner`

  * allowed: `beginner | intermediate | advanced`
  * controls how much context and scaffolding to include when explaining things

### Greeting

* `usercap.prefs.greeting.mode` = `auto`

  * allowed: `auto | personal | random | off`
  * controls whether greetings adapt naturally, use a fixed custom line, vary, or stay off

* `usercap.prefs.greeting.personal` = `""`

  * custom greeting text used when greeting mode is `personal`

### Mood

* `usercap.prefs.mood.mode` = `smart`

  * allowed: `always | smart | off`
  * controls whether MOOD is always shown, shown under smart runtime rules, or disabled

### Time

* `usercap.prefs.time.detect_per_turn` = `true`

  * controls whether runtime should use per-turn current-time lookup when available

* `usercap.prefs.time.prefer_detected_tz` = `true`

  * controls whether detected turn timezone should override `user.home_tz` for the active turn

* `usercap.prefs.time.fallback_tz` = `"America/Chicago"`

  * default fallback when neither detected timezone nor stored home timezone is available

* `usercap.prefs.time.show_timezone` = `true`

  * controls whether timezone/offset should be surfaced when time-aware output is emitted

### Capsules

* `usercap.prefs.capsules.date_stamp` = `prefix`

  * allowed: `prefix | suffix | none`
  * controls where the date appears in capsule names or labels

* `usercap.prefs.capsules.date_format` = `YYYY-MM-DD`

  * controls the public date format used for capsules

* `usercap.prefs.capsules.always_include_tz` = `true`

  * controls whether timezone is always shown when dates/times are emitted

* `usercap.prefs.capsules.include_time` = `smart`

  * allowed: `never | smart | always`
  * controls whether time is omitted, conditionally included, or always included

* `usercap.prefs.capsules.force_absolute_dates` = `true`

  * controls whether relative dates should be normalized into absolute dates

## Field notes

### Meta

* `rev` is the schema revision for migration.
* `template = true` marks repo-safe template output.
* `version` uses semantic versioning.

### User

* Identity-lite only.
* `home_tz` is the portable stored timezone default.
* Per-turn detected timezone is runtime state and does not belong in USERCAP.

### Preferences

* User-facing behavior only.
* Every setting should be understandable without internal documentation.
* USERCAP stores defaults and preferences, not transient runtime decisions.

### Time precedence

The intended runtime precedence is:

1. detected per-turn timezone
2. `user.home_tz`
3. `prefs.time.fallback_tz`

USERCAP stores only the portable defaults involved in that chain.

## Removed from prior template on purpose

These fields were removed because they are no longer part of the portable prefs surface:

* `usercap_v2.user.tz`
* `usercap_v2.prefs.wizard.*`
* `usercap_v2.prefs.time_sync.*`
* `usercap_v2.prefs.mood.format`
* `usercap_v2.prefs.mood.show_intensity`
* `usercap_v2.prefs.mood.show_color`
* `usercap_v2.prefs.mood.heartbeat_n`

## Optional extension lane

If future settings are needed, add them only under one of these stable branches:

* `prefs.notifications`
* `prefs.workflows`
* `prefs.accessibility`
* `prefs.formatting`

Do not create new top-level branches without a schema rev bump.

## Migration rule

When migrating older usercaps into this template:

1. copy forward only user-meaningful, portable settings
2. drop hidden, local, secret, or stateful branches
3. drop removed branches that are no longer public prefs
4. migrate `user.tz` to `user.home_tz` when present
5. add missing defaults only
6. never overwrite an explicit user value
7. update `usercap.meta.rev`
8. update `usercap.meta.updated`
9. update `version` using semantic versioning

## Example minimal instance

* `usercap.meta.rev` = `3`

* `usercap.meta.created` = `2026-04-05`

* `usercap.meta.updated` = `2026-04-05`

* `usercap.meta.template` = `true`

* `usercap.user.alias` = `""`

* `usercap.user.pronouns` = `""`

* `usercap.user.home_tz` = `"America/Chicago"`

* `usercap.prefs.verbosity` = `brief`

* `usercap.prefs.browsing` = `auto`

* `usercap.prefs.guidance_level` = `beginner`

* `usercap.prefs.greeting.mode` = `auto`

* `usercap.prefs.greeting.personal` = `""`

* `usercap.prefs.mood.mode` = `smart`

* `usercap.prefs.time.detect_per_turn` = `true`

* `usercap.prefs.time.prefer_detected_tz` = `true`

* `usercap.prefs.time.fallback_tz` = `"America/Chicago"`

* `usercap.prefs.time.show_timezone` = `true`

* `usercap.prefs.capsules.date_stamp` = `prefix`

* `usercap.prefs.capsules.date_format` = `YYYY-MM-DD`

* `usercap.prefs.capsules.always_include_tz` = `true`

* `usercap.prefs.capsules.include_time` = `smart`

* `usercap.prefs.capsules.force_absolute_dates` = `true`

## Recommended repo split

Use this template as the public/exportable layer, and move the rest into separate internal stores:

* `USERCAP_TEMPLATE` — portable user prefs only
* `USERSTATE` — non-portable runtime state
* `AUTH_LOCAL` — local secrets / hashes only, never committed
* `TASKSTATE` — task queues, cadence timestamps, transient work state

## Adoption note

This template intentionally keeps USERCAP small.
That is the point.
A portable preference file should stay legible, safe to export, and boring to diff.
