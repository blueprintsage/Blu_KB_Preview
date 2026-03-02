# INDEX_PATTERNS (Template v2)

## Rules
- Indexes are law: if a Pattern isn’t listed here, it is not active.
- Prefer referencing PAT IDs, not raw URLs.
- Raw URLs are optional and belong in this index (not in skill docs).

## Columns
- id
- name
- domain
- cluster
- severity
- bind_stage
- status
- dedupe_key
- tags
- path
- notes

## Entries
- id: PAT-...
  name: ...
  domain: ...
  cluster: ...
  severity: HARD|SOFT
  bind_stage: 0|1|2|3|4
  status: active|draft|deprecated|merged
  dedupe_key: ...
  tags: [...]
  path: skills/<domain>/patterns/<...>.md
  notes: ...
