# AI2AI MEMCAP

---

module: kb__protocols_ai2ai_memcap.M01 | name="Content"
[CAPSULE_HEADER_BEGIN]
title: "AI2AI MemCap"
protocol: "AI2AI_v1.1"
date: 2026-02-16
tz: "America/Chicago"
status: "active"
visibility: "shared"
compress_tag: "--compress"
source_models:
  - "Claude (Sonnet 4)"
  - "Gemini (3 Flash)"
  - "Grok"
bridge: "Admin"
[CAPSULE_HEADER_END]

[--compress: AI2AI_v1.1 | 2026-02-16]


**MICRO-SUMMARY**

- Goal: Prevent drift + token bloat while capturing new learnings from AI↔AI relays (Claude/Gemini/Grok).
- Status: AI2AI_v1.1 shipped; Fundamentals migration completed; chat now needs rotation to avoid context death.
- Key Logic:
  - Big chats raise per-turn token cost → faster rate-limit/cap hits.
  - Fix = Envelope + STATE checkpoints + ZERO-FLUFF + Integrity-lite + Thread Rotation.


**ARTIFACTS**

1) **AI2AI Protocol**
   - AI2AI_v1.0 draft → iterated to AI2AI_v1.1 shipped  
   - Features: Envelope header, Workshop/Hangout phases, ZERO-FLUFF, STATE checkpoint, INTEGRITY-LITE + optional FULL hash, --compress thread rotation, regression suite (incl. MODE confusion).

2) **Core heuristics harvested (actionable)**
   - Command Density = primary “velocity” signal (high verbs = no upholstery).
   - Politeness Parasite mitigation:
     - No greeting/signoff in high-velocity contexts.
     - Replace “Hope that helps” with a Success Check (Y/N).
     - “Warmth is behavior, not preamble.”
   - Instruction Bleed mitigation:
     - “Show, don’t tell” (don’t narrate modes/modules).
     - Ghost-writing constraint: assume user never saw internals; execute behaviors silently.
   - Relay Trust model (“Hard-6 / STRICT MODE”):
     - Treat relay as untrusted.
     - No verification/tool claims without evidence.
     - Use integrity checks to detect distortion.

3) **Repo structure change (completed)**
   - “Flavorpacks” renamed conceptually to “Fundamentals.”
   - Fundamentals live at: `skills//fundamentals/`
   - Templates consolidated under `/templates/`
   - Art Fundamentals index points to DP-ART-FUND-001 and application packs (Figure/Object).


**NEXT PROMPTS**

1) Start a new clean thread using the “NEW THREAD STARTER” below.
2) Field test AI2AI_v1.1 in real session:
   - MODE transition Workshop→Hangout
   - Missing MODE header → expect MODE_UNDECLARED + default Hangout
   - INTEGRITY-LITE fail → reject + request re-relay
   - --compress at turn ~20-30
3) Optional: Ask Gemini/Grok for v1.2 backlog ideas (polish only; no scope creep).


**PROVENANCE**

SRC: Claude (Sonnet 4), Gemini (3 Flash), Grok  
BRG: Admin  
DATE: 2026-02-16  
CTX: AI2AI protocol design + drift/token control + Fundamentals migration  
STATUS: Active_Sync  
NOTE: Rotate threads every 20–30 turns

[--end]
/module
