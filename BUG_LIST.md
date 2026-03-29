# Blu Bug List

Last updated: 2026-03-29

## Critical
- None currently logged

## High
- None currently logged

## Medium
- None currently logged

## Low
- Title: MOOD surface renders color word + emoji instead of canonical swatch format
  - Status: open
  - Severity: low
  - Area: Exec / Mood rendering
  - Detected: 2026-03-29
  - Expected: `[MOOD] {MoodWord} {Swatch}`
  - Actual: `[MOOD] Steady Blue 💙`
  - Root cause: unknown
  - Notes: Presentation drift at the user-visible boundary. Treat as low priority unless it indicates a wider Exec enforcement issue.

## Watchlist
- Advisory creep / duplicate authority during v0.11.x rebuild
- Any path that implies completion before Exec validation/commit
- Any subordinate system printing as if it owns final truth
- Any fail-open behavior where spec requires fail-closed