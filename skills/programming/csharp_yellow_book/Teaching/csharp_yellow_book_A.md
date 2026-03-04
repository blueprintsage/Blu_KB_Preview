---
title: "C# Programming Yellow Book (Rob Miles, 7th ed., 2015) — Teaching (Lane A)"
source: "C# Programming Yellow Book (Rob Miles, 7th ed., 2015)"
run_date: 2026-03-04
---

# Teaching (Lane A)

This is the human instruction lane for applying the Lane B patterns.

## How to use this pack
1) Pick a small console program you can finish in 20–60 minutes.
2) Apply **AP-001** as your skeleton.
3) As you code, enforce patterns:
   - Input/validation: PAT-002/003/018
   - Structure/refactor: PAT-005/009/010
   - Debugging: PAT-024/023/CSYB-AP-002
4) Finish with PAT-040 (3-case check).

## Drills
### CSYB-DRILL-001 — Input parsing drill
Write a console app that asks for an integer age. Use TryParse; on failure, reprompt up to 3 times then exit with a message.

### CSYB-DRILL-002 — Loop selection drill
Implement the same task (sum numbers until user enters blank) once with while and once with for (fixed count version). Explain why each loop fits/doesn’t.

### CSYB-DRILL-003 — Refactor drill
Take a 40-line Main method that does prompting, parsing, computing, and printing; split into 3–5 methods with single responsibilities.

### CSYB-DRILL-004 — Exception hygiene drill
Wrap only the file-open line in try/catch, catch the specific exception type, and produce an actionable error message.

### CSYB-DRILL-005 — Class invariant drill
Design a BankAccount class with a Balance that can’t go negative. Enforce invariant in constructor and Withdraw method; test edge cases.

## Application Protocols
### CSYB-AP-001 — Console Program Skeleton
A repeatable structure: (1) Print title (2) Prompt+Read (3) Parse/Validate (4) Compute (5) Print labeled output (6) Exit.

### CSYB-AP-002 — Minimal Repro Debug Protocol
When stuck: (1) Freeze failing behavior (2) Delete unrelated code (3) Keep smallest input that fails (4) Use debugger to inspect state (5) Fix and add a regression input.

## Quick checklist (exit ticket)
- What input can break this program?
- Where is the single source of truth for each constant?
- What is the smallest repro for the last bug you hit?
