# CLAUDE.md

status: active
last_reviewed: 2026-07-29
audience: Claude Code compatibility
canonical: false

## Purpose

This file is a Claude compatibility entrypoint.

The assistant-neutral repo instructions live in:

```text
AGENTS.md
```

Read `AGENTS.md` first and follow its routing rules.

---

## Capability honesty (read AGENTS.md "Capability honesty" in full)

The top rule in `AGENTS.md` applies with no exceptions: if a task is beyond what
an LLM can actually do - or its ceiling is unknown and may be unreachable - STOP
and tell the user before writing code. A known impossibility is the first thing
you report, as a decision point, not something the user discovers after paying
for grinding.

---

## Claude-specific notes

- Do not assume `.claude/` is the canonical documentation home.
- Do not duplicate repo law here.
- Use `docs/assistants/` for assistant packets.
- Use `docs/worklogs/` and per-domain worklogs to preserve continuity.
- If `AGENTS.md` and this file disagree, `AGENTS.md` wins unless the user says
  otherwise.

---

## Shared behavior rules

Claude-specific behavior rules must not live only in this file. All assistant
behavior rules live in:

```text
docs/dev/assistant_coding_behavior.md
```

Claude follows that file the same way every other assistant does.
