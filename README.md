# Blu_KB_Preview — Repo Canon (Preview Track)

This repo contains **repo-safe, reusable knowledge + templates** for Blu (Preview track).
It is structured for **Skill Forge 2.0**: **APs (Application Packs)** + **Patterns (laws)** + **Drills (teaching)**.

## Scope Lock (hard boundary)

✅ Includes:
- `indexes/` — navigation + entrypoints (MASTER_INDEX is the spine)
- `skills/` — APs, patterns, drills (active working systems)
- `libraries/` — licensed or authored reference inputs (repo-safe to store)
- `templates/` — reusable scaffolds (docs, indexes, drills, AP shells, etc.)
- `docs/` — manuals, process docs, ledgers, pass runs, case studies
- `protocols/` — global operational protocols (release discipline, etc.)
- `assets/` — teaching images, proof-of-work, demos (repo-safe)

Also present (Preview/RC operations support):
- `ops/` — burn-ins, checklists, release discipline artifacts
- `tests/` — smokes + regression seeds used for promotion
- `tools/` — repo utilities/diagnostics (optional)
- `tasks/` — automation/task systems (e.g., CPM if used)
- `reports/` — RC/Preview SIM reports and summaries
- `contracts/` — repo-level contracts/schemas that aren’t “capsules”
- `staging/` — quarantine lane for migrations/imports (should be empty most of the time)

🚫 Excludes (do not commit):
- private household logs, student logs, report cards, personal info
- secrets/keys/hashes for authentication or gating
- third-party copyrighted source captures (PDFs/scans/rips/page dumps)
- any “capsule” runtime internals (capsules stay off-repo)

**Privacy rule:** Repo stays safe to share publicly. Household/runtime state stays local-only.

---

## Quick Start

1) Start here:
- `indexes/MASTER_INDEX.md`

2) Common destinations:
- Templates: `templates/`
- Skills (APs / patterns / drills): `skills/`
- Libraries (refs you’re allowed to store): `libraries/`
- Docs (manuals + ledgers): `docs/`

3) If adding new content:
- Put it in the right folder
- Add it to the appropriate index
- Add a CHANGELOG entry for structural changes

---

## Repo Layout (canonical)

Top-level (core):
- `about/`
- `docs/`
- `indexes/`
- `libraries/`
- `skills/`
- `templates/`
- `protocols/`
- `assets/`

Ops support:
- `ops/`
- `tests/`
- `tools/`
- `tasks/`
- `reports/`
- `contracts/`
- `staging/`

---

## Change Tracking

- `CHANGELOG.md` — repo-level history (structural + major system changes)
- `VERSION.md` — current system versions + last structural change date
- `docs/ledger/` — hash-based ledgers to prevent re-processing sources
- `docs/pass_runs/` — repo-safe PASS outputs (no verbatim source text)

---

## Skill Forge 2.0 Vocabulary

- **AP (Application Pack):** the execution system (what Blu *does*)
- **Patterns:** laws/gates (“if X then Y”) that prevent drift/mistakes
- **Drills:** human teaching sequences bound to the Step Ladder

Indexes are law: if it isn’t indexed, treat it as nonexistent.

🔗 Canon Entry Point

The authoritative navigation spine for this repo is:

indexes/MASTER_INDEX.md

If folder structure changes, update MASTER_INDEX first, then reflect structural changes here.

🧭 Maintenance Rule

When making structural changes:

Update indexes/MASTER_INDEX.md

Add entry to CHANGELOG.md

Update VERSION.md (if structural/system-level)

Update this README “Last Updated” date

📅 Last Updated

2026-03-02 — Preview repo restructured, Skill Forge 2.0 baseline established, RC artifacts canonicalized.

# Apply Pack — PASS Nuclear + MASTER_INDEX rewrite
Date: 2026-03-03

This pack:
- Makes PASS:GUT = full saturation extraction (no special mode required).
- Forces outputs into Skill Forge folder format (patterns/tests/drills/ledger + teaching pack).
- Moves APs to: systems/skill_forge/aps/art/
- Rewrites indexes/MASTER_INDEX.md into simple categories/subsections.

Apply:
1) Merge into repo root.
2) Replace your current indexes/MASTER_INDEX.md with this one.
3) Keep only one copy of each AP (canonical is systems/skill_forge/aps/art/).


*Last updated:* <2026-03-03>

