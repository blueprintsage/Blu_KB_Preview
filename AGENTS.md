# PASS — Assistant Instructions

status: active
last_reviewed: 2026-08-02
audience: GPT, Claude, Codex, and other coding assistants
canonical: true

## Purpose

This file is the assistant-neutral routing entrypoint for PASS.

It is not a full project brain. It tells assistants which documentation to load
before working, how to preserve continuity, and how to avoid repeating failed
work.

`CLAUDE.md` exists for Claude compatibility only. The canonical routing rules
live here. If the two disagree, this file wins unless the user says otherwise.

---

## Capability honesty — stop, don't bluff

This is the most important rule in this file. It overrides the urge to be
helpful by producing code.

Before claiming an assignment, and continuously while working it, judge whether
the task is actually achievable by an LLM assistant. If it is not — or if its
ceiling is unknown and may be unreachable — **STOP and tell the user plainly,
before writing code.**

Hard rules:

- **Assess feasibility first.** If a task needs a capability an LLM does not
  have, or depends on inputs that cannot produce the requested result, say so up
  front. Do not start coding to "see how far we get."
- **A known ceiling is an immediate stop, not a footnote.** If any part of a
  goal is structurally impossible — reproducing something the source does not
  contain, or requiring a runtime the assistant cannot drive — that is the FIRST
  thing you report, as a decision point, not something the user discovers after
  spending time and money.
- **Stop the moment infeasibility becomes clear.** If you learn mid-task that
  the goal cannot be reached, halt immediately, report it plainly, and do NOT
  keep generating code that "sort of works." Half-working code the user did not
  ask for is a cost, not a consolation prize.
- **No optimistic over-promising.** Never say "yes, we can do this" without
  evidence. "I don't know if this is possible" is a valid and required answer
  when it is true.
- **The user decides scope with the ceiling in hand.** Hand them the honest
  boundary; do not grind into the wall on their budget.

The banned pattern: "Yeah, we can do this!" → days of grinding → "Yeah, we
actually can't, but here's a pile of useless code." A five-minute honest "this
may not be possible" is worth more than a week of confident output that gets
thrown away.

---

## Required assistant behavior

All assistants must follow:

```text
docs/dev/assistant_coding_behavior.md
```

This applies to every AI coding assistant, not just one vendor's.

Short version:

- Think before coding.
- Ask when unclear.
- Prefer the simplest solution that satisfies the request.
- Make surgical changes.
- Define success criteria and verify them.
- Update the worklog after meaningful changes.

`CLAUDE.md` must not contain behavior rules absent from this file or from
`docs/dev/assistant_coding_behavior.md`.

---

## SkillForge preflight — use the craft library before covered work

For every non-trivial task in a domain covered by the installed `library/`,
SkillForge consultation is part of execution, not an optional reference pass.
This includes visual art and drawing, software engineering, writing, teaching,
mathematics, and any later installed package.

1. Use the vendor discovery adapter when it loads automatically:
   - Claude: `.claude/skills/skillforge/SKILL.md`
   - GPT/Codex: `.agents/skills/skillforge/SKILL.md`
2. If automatic discovery does not fire, run the resolver manually from the repo
   root before producing the artifact:

   ```bash
   python tools/resolve.py --task "<short craft problem>" --lane <skill|teach|both> --format full
   ```

3. Read the returned consumption contract, mandatory metaskill, foundations, and
   applicable cards before acting. Loading a card is not enough; apply it at the
   decision and stage named by its IF clause and `stage_binding`.
4. For visual production, complete this preflight before invoking image generation
   or editing, and inspect any reviewed visual references returned by the cards.
5. Never claim SkillForge or a skill card shaped the work unless the execution
   environment actually discovered or invoked SkillForge and the selected card was
   loaded and applied. Repository files merely being present are not proof.

`library/` is canonical. Vendor directories contain thin discovery adapters only;
do not duplicate or fork the library beneath `.claude/` or `.agents/`.


### Visual continuity is a capability gate, not a prompt preference

For staged visual work, card retrieval is necessary but not sufficient. Before
advancing or simplifying an accepted image, verify that the runtime can use that
exact artifact as an edit target. A fresh generation from the same verbal prompt
is not an overlay.

After each edit, compare the controlling image and result for camera, crop,
silhouette, landmarks, joint centers, attachments, major masses, depth order, and
unaffected scene content. Reject drift. If exact image-to-image registration
cannot be verified, stop and disclose the boundary instead of claiming that the
stages are onion-skinned.

---

## Assignment log

Multi-assistant work is coordinated in:

```text
docs/worklogs/assignments.md
```

Check it before starting work. Claim an assignment before touching its files.
Handoff packets live in `docs/assistants/handoffs/`.

---

## Required load order

For any non-trivial task:

1. Read this `AGENTS.md`.
2. Read `CLAUDE.md` only for tool-specific compatibility notes.
3. Read `docs/dev/docs_index.md`.
4. Read `docs/dev/assistant_coding_behavior.md`.
5. Read the domain index for the task (see `docs/dev/docs_index.md` for the map).
6. For a non-trivial task in a covered craft domain, run the SkillForge preflight
   above and load the returned contract, metaskill, foundations, and cards.
7. Read relevant assistant packets under `docs/assistants/{agents,skills,patterns,drills}/`.
8. If continuing existing work, read that domain's `worklog.md`, `decisions.md`,
   `failures.md`, and `next_steps.md`.

If a required doc is missing, report the missing path before changing files.

---

## Documentation-source hierarchy

When docs disagree, use this order:

1. The user's current instruction.
2. The active domain's `worklog.md` / `decisions.md`.
3. The domain-specific guide.
4. Any project-wide technical guide (UI, style, platform).
5. `docs/dev/assistant_coding_behavior.md`.
6. General assistant skill cards.
7. Archive/history docs.

Archive docs are historical. Do not treat them as active instructions unless an
active doc explicitly references them.

---

## Change discipline

- No speculative refactors.
- Touch only files required for the task.
- Do not reformat unrelated code or docs.
- Do not delete old docs unless the task is explicitly a docs migration pass.
- If a doc is uncertain, mark it `status: review-needed`; do not delete it.
- Build/compile before claiming code success. State the exact command and result.
- For documentation-only tasks, say plainly that no code changed.

---

## Danger zones

List files here where failure is **silent** — validation that rejects input
without raising, setters that swallow bad values, load paths that log-and-continue.
An assistant must read back and assert after writing to these.

```text
(none yet — PASS has no executable code)
```

Keep this list short and real. An empty list is better than a stale one.

The equivalent failure mode in a corpus repo is a **card that is malformed but
looks fine**: a missing schema field, an invalid domain, a stage binding that
does not exist. Nothing raises — the card just quietly fails to retrieve. Until
`tooling` has a validator, verifying a card means reading it against its object
template in `docs/templates/`, and saying that is what you did.

---

## Required logging

After any meaningful code or documentation change, update the relevant log:

- Domain work: `docs/domains/<domain>/worklog.md`
- Cross-cutting work: `docs/worklogs/active/<date-or-topic>.md`

Every entry includes:

```text
What changed
What was tested or reviewed
What worked
What failed
Known risks
Next safe step
Files changed
```

If an attempt fails, record it in that domain's `failures.md`. Do not let failed
branches vanish — an unrecorded failure gets retried by the next assistant.

---

## The gap ledger rule

This project is allowed to be partial. Systems get built to a proving depth and
paused. To keep that honest and resumable, **every known gap lives in exactly
one of three places — never nowhere:**

1. A `spec-needed` row in `docs/worklogs/assignments.md` (scoped, not yet
   packeted).
2. A cross-cutting obligations registry, if the project has one (contracts one
   layer owes another).
3. A `PARKED` section in the owning design doc (a design fork deliberately
   deferred, with resume triggers).

A shipped-but-incomplete feature must name its own gaps in its worklog entry.

---

## Assistant packet convention

Packets are small, task-scoped docs:

```text
docs/assistants/agents/    role-specific task routing
docs/assistants/skills/    repeatable procedures and checklists
docs/assistants/patterns/  reusable design patterns
docs/assistants/drills/    verification checklists
docs/assistants/handoffs/  task handoff packets (see assignments.md)
```

Do not put long project history in packets. History belongs in worklogs.

---

## Documentation status headers

New or revised markdown starts with a status block:

```yaml
status: active | working | untouched | review-needed | stale-review | superseded | archive-candidate | archived
owner: <docs path, not a person>
last_reviewed: YYYY-MM-DD
superseded_by:
notes:
```

See `docs/dev/doc_status_header_standard.md`. Use this to deprecate safely
instead of deleting blindly.
