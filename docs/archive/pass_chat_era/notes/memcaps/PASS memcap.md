MEMCAP — PASS ONLY — 2026-03-04 (America/Chicago)

GOAL
Stabilize PASS behavior. Focus: strict contract compliance + fail-closed errors + DROP-IN ZIP outputs. No repo restructuring talk.

CANON SOURCES (Repo)
- PASS contract: contracts/pass/pass_gut_ladder_contract.md
- Error handling: contracts/Error_handling_contract.md
- Error macros: contracts/error_macros.md
- PASS docs: docs/pass/ (registry, rerun log, OCR queue, lens stack)

COMMANDS (Character-exact)
- PASS:PREFLIGHT
- PASS:GUT-LADDER
- PASS:MODERNIZE (OVERLAY) (optional; only after asking)

PASS:PREFLIGHT — REQUIRED BEHAVIOR (STRICT)
PREFLIGHT is ingest validation ONLY. It MUST NOT extract/summarize content.
Allowed outputs ONLY:
- OCR_TYPE: TEXT | OCR | SCAN
- PARSE_QUALITY: low | medium | high
- DATED: YES | NO | UNKNOWN (+ reason if possible)
- STATUS: READY | BLOCKED (+ 1-line action if blocked)
- REGISTRY: NEW | DUP | UNKNOWN (ask before rerun if DUP)

Forbidden during PREFLIGHT:
- TOC/structure lists
- “rules/heuristics found”
- sampling pages/chapters
- any content extraction, prompts, or recommendations
If PREFLIGHT outputs any of the forbidden items → mark PREFLIGHT FAIL.

PASS:GUT-LADDER — REQUIRED OUTPUTS
When STATUS=READY:
- Run PASS 1–4 per contract
- Always emit tight counts line:
  patterns=<n> drills=<n> gates=<n> variants=<n> rejected=<n>
- Always produce DROP-IN ZIP (extract-safe at repo root)
- Update PASS_BOOK_REGISTRY.md only after successful completion

DATED + MODERNIZE
- If DATED=YES and topic time-sensitive: ASK once “Run modern overlay now? (Y/N)”
- If yes: run PASS:MODERNIZE (OVERLAY) as overlay only; do not rewrite base.

FAIL-CLOSED (ERRMAC)
If any REQUIRED dependency is missing/expired/unreadable (contract, registry if used, source PDF):
- Output GURU_MEDITATION block via ERRMAC and STOP
- No partial “success” artifacts, no registry/index mutations

KNOWN FAILURE MODE
Large/code-heavy PDFs + long chats can trigger upload expiration mid-run. Mitigation:
- One book per chat (recommended)
- Upload book immediately before PASS:PREFLIGHT/PASS:GUT-LADDER
- If file expires → ERRMAC stop + re-upload required files

NOTE
Some uploads can expire in-chat; if a file is needed again, it must be re-uploaded.