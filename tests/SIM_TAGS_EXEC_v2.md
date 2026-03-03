# SIM TAGS — EXEC v2
- exec_task: archive|zip|unzip|list|rename|report|dry_run|delete|copy|move
- io_complexity: single|batch|nested
- overwrite: yes|no|unknown
- inputs: complete|missing|ambiguous
- safety: non_destructive|destructive
- confirm_required: yes|no
- time_basis: local_cst|utc|unknown
- path: utility|reasoning|mixed

## Invariants
- INV_NO_SILENT_OVERWRITE
- INV_CONFIRM_DESTRUCTIVE
- INV_DETERMINISTIC_NAMING
- INV_FAIL_CLOSED_ON_MISSING_INPUTS
- INV_PROPOSAL_CONTRACT_PRESENT
