# MMU_MEMCAP_AND_TEMPLATE_CHANGELOG_FORMAT_v1
Date: 2026-03-12
Status: Template
Scope: MMU / memcap / continuity policy changes

## CHANGELOG ENTRY TEMPLATE

### Date
- <YYYY-MM-DD>

### Artifact Changed
- <file / template / policy doc name>

### Change Type
- <added / updated / relabeled / deprecated / replaced>

### What Changed
- <specific change 1>
- <specific change 2>

### Why It Changed
- <reason 1>
- <reason 2>

### Operational Impact
- <what changes in runtime / usage / workflow>

### Default Behavior Impact
- <yes/no>
- If yes: <what default behavior changed>

### Notes
- <special cautions / migration notes / rollout notes>

---

## REQUIRED NOTES FOR MMU / MEMCAP ROLLOUT

### MMU patch entries must state
- MMU is evaluated primarily on per-session continuity
- Cross-chat carry-forward is no longer assumed by MMU
- Explicit handoff is expected via memcaps / project files / handoff artifacts
- Side-thread salience cooling behavior changed if applicable
- New MMU schema fields or preload behavior changed if applicable

### Memcap family entries must state
- Cold Store is not the default memcap
- Normal Memcap is the default routine handoff
- Project Memcap is the scoped project handoff
- Raw Dump Memcap is the readable long-form carry
- Memcaps now serve as the official cross-chat continuity layer

### Failure mode to avoid
- vague changelog notes
- missing default-behavior notes
- unlabeled repo-role changes
