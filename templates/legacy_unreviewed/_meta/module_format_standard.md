capsule_id: kb__templates_meta_module_format_standard_md__af8bd9
title: "module format standard"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', '-meta']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# Module Format Standard (Repo-wide)

---

## Capsule Header Standard (Required)

All markdown artifacts **except APs and DPs** must begin with a capsule header:

- `capsule_id`, `title`, `date`, `updated`, `version`, `status`, `topic`, `type`, `tags`, `sensitivity`, `visibility`, `source`, `domain`, `schema`, `body_schema`
- Header must be **outside modules** and followed by `---`.

APs and DPs may omit capsule headers.

---


module: module_format_standard.M01 | name="Rules"
**Rule 1 — Headers outside modules**
- Use `#` / `##` headings only outside modules (title, brief preface, separators).

**Rule 2 — Content inside modules**
- All substantive content must be inside:
  - `module: <capsule_id>.M## | name="..."`
  - `/module`

**Rule 3 — Stable IDs**
- Module IDs are stable and sequential (`M00` optional TOC/meta, then `M01+` content).

**Rule 4 — No nesting**
- Do not place a `module:` block inside another module block.

**Rule 5 — Human labels inside**
- Inside modules, use bold labels instead of headings:
  - `**Interfaces**`, `**Inputs**`, `**Outputs**`, `**Rules**`

/module

---

module: module_format_standard.M02 | name="MODULECHECK (PASS/FAIL)"
PASS requires:
- Every `module:` has a matching `/module`
- No nested modules
- Module IDs are stable + sequential (`M00`, `M01`, …)
- No substantive content outside modules (except: capsule header, `# Title`, brief preface, `---`)

FAIL handling:
- Reformat to comply before saving/committing.

/module
