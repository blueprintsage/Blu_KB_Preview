# Agent Packets

status: active
owner: docs/assistants/agents
last_reviewed: 2026-07-29

Role-scoped routing. One file per recurring kind of work. An agent packet says
what this role does, which docs to read first, and which rules bind it.

Pattern to follow:

```text
# <Role> Agent

## Use when
<the trigger>

## Required reads
<explicit paths>

## Rules
- <constraints specific to this role>
- <what this role must not do>
```

Keep them short. A packet longer than a page is a design doc wearing a costume.
