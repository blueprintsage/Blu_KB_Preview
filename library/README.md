# library/

status: active
owner: docs/domains/corpus
last_reviewed: 2026-07-30

Extracted skill objects. This is the product.

```
library/<package>/<topic-path...>/
  PAT_<slug>.md
  DRILL_<slug>.md
  AP_<slug>.md
INDEX.md          generated - do not hand-edit
```

**Placement is derived, not chosen here.** An object's path comes from its own
`library_path` frontmatter. Its first segment is the installable package; later
segments are human-readable topics. Every SkillForge install loads `metaskills`
first, then any selected package. To move a skill, edit that list and regenerate;
never move a file and leave the frontmatter behind, and never hand-edit an index.

Schema: `docs/PASS/PASS_SCHEMA.md`. Acceptance gate: `python tools/validate.py`
(see assignment PASS-TOOL-1 - the script does not exist yet).
