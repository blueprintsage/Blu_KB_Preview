# USERPREFS HELP v2.1

Last updated: 2026-03-07  
tz: America/Chicago  
status: draft

Find: help userprefs prefs usercap patch reset wizard template

## What are userprefs?

Userprefs are durable settings that control response style, time handling, greeting behavior, MOOD display, and capsule formatting.

They now live as portable preference fields under `usercap_v2.prefs.*`.

## Common requests

- “Run userprefs wizard”
- “Show my current prefs”
- “Update prefs: <key>=<value>”
- “Reset prefs”
- “Export prefs”

## Prefs reference

### User

- `usercap_v2.user.alias`
- `usercap_v2.user.pronouns` (optional)
- `usercap_v2.user.tz` (IANA recommended)

### Core preferences

- `usercap_v2.prefs.verbosity` (`brief | normal | deep`)
- `usercap_v2.prefs.browsing` (`auto | ask | never`)
- `usercap_v2.prefs.guidance_level` (`beginner | intermediate | advanced`)

### Greeting

- `usercap_v2.prefs.greeting.mode` (`auto | personal | random | off`)
- `usercap_v2.prefs.greeting.personal`

### Mood + ribbons policy

- `usercap_v2.prefs.mood.mode` (`always | smart | off`)
- `usercap_v2.prefs.mood.format` (`1 | 2 | 3`)
- `usercap_v2.prefs.mood.show_intensity` (`true | false`)
- `usercap_v2.prefs.mood.show_color` (`true | false`)
- `usercap_v2.prefs.mood.heartbeat_n` (integer)

Policy:
- MOOD output reflects Blu posture, not the user.
- Blu may adapt responses using PEL/ribbons from cues, but will not assert the user’s emotional state unless explicitly requested.
- Ribbons steer response style internally; they are not claims about the user.

### Wizard

- `usercap_v2.prefs.wizard.enabled` (`true | false`)
- `usercap_v2.prefs.wizard.autostart` (`true | false`)
- `usercap_v2.prefs.wizard.output_config` (`ask | never | always`)

### Time sync

- `usercap_v2.prefs.time_sync.mode` (`off | ask | anchored`)
- `usercap_v2.prefs.time_sync.default_time` (`HH:MM`)
- `usercap_v2.prefs.time_sync.ask_time_if_missing` (`true | false`)
- `usercap_v2.prefs.time_sync.reuse_window_minutes` (integer)

### Capsules

- `usercap_v2.prefs.capsules.date_stamp` (`prefix | suffix | none`)
- `usercap_v2.prefs.capsules.date_format` (`YYYY-MM-DD`)
- `usercap_v2.prefs.capsules.always_include_tz` (`true | false`)
- `usercap_v2.prefs.capsules.include_time` (`never | smart | always`)
- `usercap_v2.prefs.capsules.force_absolute_dates` (`true | false`)

## Removed from this surface

These older portable-pref ideas are no longer part of the current public prefs surface:

- `usercap_v2.prefs.art_pipeline.*`
- `usercap_v2.prefs.repo.offer_on_teach`
- `usercap_v2.prefs.ticks.*`

## Example updates

Change timezone:
- `usercap_v2.user.tz` = `America/New_York`

Reduce verbosity:
- `usercap_v2.prefs.verbosity` = `brief`

Turn off browsing:
- `usercap_v2.prefs.browsing` = `never`

Disable MOOD display:
- `usercap_v2.prefs.mood.mode` = `off`

## Notes on the format shift

This version removes YAML patches and expresses settings as plain markdown key-path fields.

That keeps the template portable, human-readable, and safer for repo/capsule handling.
