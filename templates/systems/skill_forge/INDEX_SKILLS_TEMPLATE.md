# INDEX_SKILLS (Template v2)

## Rules
- Indexes are law: if a skill artifact isn’t listed, it doesn’t exist.
- Skills are canon outputs: APs + Drills + Pattern libraries.
- Libraries (reference) live elsewhere and should be indexed in INDEX_LIBRARIES.

## Artifact Types
- AP (Application Pack): function/procedure bound to Step Ladder
- DRL (Drills): human lesson sequences (subject file or per-drill files)
- PAT (Pattern library files): “one roof” collections + clusters

## Entries
### Application Packs
- id: AP-...
  name: ...
  domain: ...
  subject: ...
  status: active|draft|deprecated|merged
  path: skills/<domain>/<subject>/application_packs/AP-....md
  tags: [...]

### Drills
- id: DRLSET-<DOMAIN>-<SUBJECT>
  domain: ...
  subject: ...
  status: active|draft
  path: skills/<domain>/<subject>/drills/DRILLS-....md
  tags: [...]

### Pattern Libraries
- id: PATLIB-<DOMAIN>
  domain: ...
  status: active|draft
  path: skills/<domain>/patterns/PATTERNS-<DOMAIN>.md
  tags: ...
