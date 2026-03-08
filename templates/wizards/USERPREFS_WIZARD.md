# USERPREFS WIZARD v2.1

Last updated: 2026-03-07  
tz: America/Chicago  
status: draft

Find: userprefs wizard setup preferences usercap defaults template

## Purpose

This wizard walks a user through setting up `usercap_v2` in a consistent, low-friction way.

Goals:
- Quick good defaults in 2–3 minutes
- Optional advanced switches
- Output a clean key-path patch to paste into `USERCAP_TEMPLATE`

## Wizard flow

### Step 0 — Consent + scope
**What this is for:** choose whether you want a fast setup or a more detailed pass, and whether the result stays in-thread or becomes an exportable patch.

Choose:
- Quick (recommended) or Advanced
- Thread-only settings or export a patch to store

### Step 1 — User alias
**What this controls:** the name or alias Blu uses when addressing you.

- What should I call you? → `usercap_v2.user.alias`

### Step 2 — Pronouns
**What this controls:** optional pronoun preferences for respectful addressing. Leaving it blank changes nothing else.

- Pronouns (optional) → `usercap_v2.user.pronouns`

### Step 3 — Timezone
**What this controls:** local time interpretation for schedules, dates, reminders, and any time-aware output.

- Timezone (IANA) → `usercap_v2.user.tz`

### Step 4 — Verbosity
**What this controls:** how short or detailed normal answers should be.

- Verbosity: `brief | normal | deep` → `usercap_v2.prefs.verbosity`

### Step 5 — Browsing
**What this controls:** whether web lookup happens automatically, only after asking, or never.

- Browsing: `auto | ask | never` → `usercap_v2.prefs.browsing`

### Step 6 — Guidance level
**What this controls:** how much teaching context and scaffolding to include when explaining something.

- Guidance level: `beginner | intermediate | advanced` → `usercap_v2.prefs.guidance_level`

### Step 7 — Greeting mode
**What this controls:** whether greetings adapt naturally, use a personal custom line, vary randomly, or stay off.

- Greeting mode: `auto | personal | random | off` → `usercap_v2.prefs.greeting.mode`

### Step 8 — Personal greeting text
**What this controls:** the exact greeting line used when greeting mode is `personal`.

- Personal greeting text (optional) → `usercap_v2.prefs.greeting.personal`

### Step 9 — Blu MOOD mode
**What this controls:** whether MOOD is always shown, shown only when it fits, or turned off.

- Mood mode: `always | smart | off` → `usercap_v2.prefs.mood.mode`

Policy:
- MOOD output shows Blu posture, not a read of the user.
- Blu may adapt using ribbons/PEL from cues, but will not assert the user’s emotional state unless explicitly requested.

### Step 10 — MOOD format
**What this controls:** which visual/display style MOOD uses.

- Mood format: `1 | 2 | 3` → `usercap_v2.prefs.mood.format`

### Step 11 — Show intensity
**What this controls:** whether MOOD includes its intensity marker.

- Show intensity? → `usercap_v2.prefs.mood.show_intensity`

### Step 12 — Show color
**What this controls:** whether MOOD includes color labeling.

- Show color? → `usercap_v2.prefs.mood.show_color`

### Step 13 — Heartbeat count
**What this controls:** the heartbeat count used in MOOD formatting when applicable.

- Heartbeat count → `usercap_v2.prefs.mood.heartbeat_n`

### Step 14 — Wizard enabled
**What this controls:** whether the userprefs wizard remains available as a standard setup tool.

- Enable wizard? → `usercap_v2.prefs.wizard.enabled`

### Step 15 — Wizard autostart
**What this controls:** whether setup flows should lean toward starting the wizard automatically.

- Autostart wizard? → `usercap_v2.prefs.wizard.autostart`

### Step 16 — Wizard output config
**What this controls:** whether the wizard should ask, never offer, or always print a patch/export block at the end.

- Output config: `ask | never | always` → `usercap_v2.prefs.wizard.output_config`

### Step 17 — Time sync mode
**What this controls:** whether time anchoring is disabled, requested when needed, or deliberately reused.

- Mode: `off | ask | anchored` → `usercap_v2.prefs.time_sync.mode`

### Step 18 — Default time
**What this controls:** the standard anchor time used for time-aware workflows when a default is needed.

- Default time → `usercap_v2.prefs.time_sync.default_time`

### Step 19 — Ask if time is missing
**What this controls:** whether the system should ask for a time when one is required but missing.

- Ask if missing? → `usercap_v2.prefs.time_sync.ask_time_if_missing`

### Step 20 — Reuse window minutes
**What this controls:** how long a recent time anchor can be reused before it should be refreshed.

- Reuse window minutes → `usercap_v2.prefs.time_sync.reuse_window_minutes`

### Step 21 — Capsule date stamp
**What this controls:** whether dates appear at the front, end, or not at all in capsule names/labels.

- Date stamp: `prefix | suffix | none` → `usercap_v2.prefs.capsules.date_stamp`

### Step 22 — Capsule date format
**What this controls:** the public date format used in capsule names and outputs.

- Date format → `usercap_v2.prefs.capsules.date_format`

### Step 23 — Always include timezone
**What this controls:** whether timezone should always appear when dates or times are emitted.

- Always include timezone? → `usercap_v2.prefs.capsules.always_include_tz`

### Step 24 — Include time in capsules
**What this controls:** whether time should never be shown, be shown only when useful, or always be shown.

- Include time: `never | smart | always` → `usercap_v2.prefs.capsules.include_time`

### Step 25 — Force absolute dates
**What this controls:** whether relative references like “tomorrow” should be normalized into explicit dates.

- Force absolute dates? → `usercap_v2.prefs.capsules.force_absolute_dates`

### Step 26 — Confirm + output
**What this does:** reads back choices, prints a clean key-path patch, and gives update/reset guidance.

- Read back choices
- Print key-path patch
- Provide update later / reset tips

## Output patch template

- `usercap_v2.user.alias` = `"<NAME>"`
- `usercap_v2.user.pronouns` = `"<optional>"`
- `usercap_v2.user.tz` = `America/Chicago`

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

## Removed from this wizard

These older questions should no longer appear in the wizard:

- art pipeline
- repo offer-on-teach
- ticks cadence

## Validation checks

- Timezone should be IANA, such as `America/Chicago`
- Verbosity must be one of: `brief | normal | deep`
- Browsing must be one of: `auto | ask | never`
- Guidance level must be one of: `beginner | intermediate | advanced`
- Date format should stay `YYYY-MM-DD` unless the public format contract changes
- Integer fields should remain plain integers
- Boolean fields should remain `true` or `false`

## Notes on the format shift

This version replaces YAML output with plain markdown key-path output.

That keeps the wizard aligned with the new `USERCAP_TEMPLATE` format and avoids YAML-related capsule issues.
