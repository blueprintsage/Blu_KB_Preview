# Repo Documentation — Overview

This folder documents:
- What the repo contains
- How the folder structure works
- How changes are recorded (CHANGELOG + ledgers)
- How to add new assets safely (repo hygiene)

## Canon principles
- Capsule-uniform files: human header → `---` → machine `module_set:` block.
- Patterns are laws (if X then Y gates) and bind to Step Ladder stages.
- APs define execution systems; drills define human teaching sequences.
- Indexes are law: if it isn’t indexed, it doesn’t exist.

## Where key things live
- indexes/ : MASTER_INDEX and supporting domain indexes
- skills/  : APs, patterns, drills (core “working” content)
- libraries/: reference assets (only repo-safe or licensed-to-store assets)
- docs/    : manuals, ledgers, pass logs, process docs
- about/   : repo/system markers and freeze notes

## Change tracking
- CHANGELOG.md: human-readable, repo-level history
- docs/ledger/*.md: file hashes + statuses (prevents reprocessing)
- docs/pass_runs/: PASS:GUT outputs (repo-safe; no verbatim source)
