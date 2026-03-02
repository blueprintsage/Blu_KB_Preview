# Repo Layout Canon (Preview + Release)

## Non-negotiables
- Kernel capsules are LOCAL-ONLY (never stored in this repo).
- Repo is for systems, skills, libraries, docs, templates, schemas, contracts, burn-ins, tests, reports, indexes.
- Indexes are law: if it isn’t indexed, it doesn’t exist.

## Top-level folders
- about/    : about/version/licensing notes (stable, boring)
- avatars/  : avatar images only
- docs/     : all human-readable documentation
  - docs/repo/     : repo policies, layout canon, indexing rules
  - docs/systems/  : manuals per system (Skill Forge, PASS, Identity Lore)
- systems/  : “core systems” specs/logic (Skill Forge / PASS / Identity Lore)
- skills/   : canon skill outputs (Patterns / Application Packs / Drills)
- libraries/: reference content (notes/examples/refsheets), mined into skills
- templates/: fill-in templates (protocol templates, doc templates, etc.)
- schemas/  : formal schemas
- contracts/: enforcement contracts (gates, patch contracts, promotion rules)
- burnins/  : burn-in suites by domain/system
- tests/    : smokes + regressions + fixtures
- reports/  : SIM reports + promotion logs
- indexes/  : all indexes live here (organized + deterministic)
- tools/    : helper scripts (optional)

## Preview-only folders (never promote)
- incoming/ : quarantine staging
- sandbox/  : experiments
- trash/    : explicit delete bucket

## Placement rules (fast)
- If it’s a rule → contracts/ or systems/ (never libraries/)
- If it’s a reusable skill artifact → skills/
- If it’s reference/examples → libraries/
- If it’s a blank form → templates/
- If it’s a test → tests/
- If it’s a run record → reports/
- If it’s a registry/listing → indexes/

## Link policy
- Internal links should prefer repo-relative paths.
- Raw URLs may be recorded in indexes when needed, but paths are source of truth.
