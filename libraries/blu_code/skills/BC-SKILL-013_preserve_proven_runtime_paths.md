# BC-SKILL-002 — Preserve Proven Runtime Paths During Feature Expansion

## Trigger
Use when extending, patching, or debugging a live deterministic route that already has a passing runtime path, especially artifact-backed workflows and hosted-runtime bridges.

Use especially when adding adjacent functionality to:
- command families
- Program-owned routes
- ExecLib-backed deterministic lanes
- import/export workflows
- artifact generation or archive packaging paths

## Failure Pattern
A new feature is added beside a working feature, but the patch replaces, bypasses, or severs the proven runtime backend.

The command surface may still look valid, and routed success text may still print, while the actual runtime dependency is broken.

Common signature:
`no active export backend available in hosted runtime`

## Do
1. Identify the known-good runtime path before patching.
2. Preserve the proven execution bridge as a protected path.
3. Add new entrypoints beside the proven path instead of rewriting it.
4. Keep command routing, Program dispatch, ExecLib calls, and backend/tool execution separate in the patch.
5. Rerun the original PASS matrix after every adjacent feature patch.
6. Require real runtime proof for artifact claims:
   - archive file exists
   - download link exists
   - required archive members exist
   - roundtrip import works when import/export is in scope
7. Treat hosted artifact generation as a protected runtime dependency, not as replaceable command prose.
8. Add a regression test that the previously working command still works after the new feature is added.

## Do Not
- Do not infer backend success from a routed success line.
- Do not replace a working export backend while adding import validation.
- Do not collapse adjacent entrypoints into one generic handler unless the old PASS matrix still passes.
- Do not treat command-surface correctness as runtime proof.
- Do not ship import hardening until export still produces a real downloadable archive.
- Do not claim a feature is fixed unless its runtime dependency actually executed.

## Validation
A patch passes this skill only when:
- the original proven route still passes its old PASS case;
- the new route passes its new PASS case;
- artifact-backed output has a real file/link when claimed;
- no deterministic lane falls back to conversational prose;
- the regression signature is absent;
- the test report includes both old-path regression coverage and new-path coverage.

For `/memory` import/export specifically:
- `/memory export` must create a real zip archive.
- The archive must contain `memory.yml`, `MANIFEST.md`, and `README_RESTORE.md`.
- `/memory import` must load the packet as source only.
- `/memory import` must not imply hidden persistence or continuity commit.
- Import expansion must not alter the working export backend unless explicitly required.

## Example
Bad:
Adding `/memory import` rewires the shared memory handler and `/memory export` now returns:
`ERR: MEMORY.EXPORT_FAILED — no active export backend available in hosted runtime`

Good:
Adding `/memory import` leaves the existing `/memory export` backend untouched, then adds import validation beside it. The release test reruns `/memory export`, confirms the zip exists, confirms required archive files exist, and then tests import.

## Origin
Project: Blu memory integration  
Incident: r9.3.10 import expansion regressed a previously passing `/memory export` backend.  
Repair: r9.3.11 restored export while preserving import.
