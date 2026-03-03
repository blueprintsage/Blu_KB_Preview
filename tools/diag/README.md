capsule_id: kb__tools_diag_readme_md__8229d6
title: "README"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['tools', 'diag']
sensitivity: medium
visibility: shared
source: repo
domain: tools
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# Blu Repo Diagnostics Tool

Find: diag lint module sentinel html markers

## What it checks (default)
- R001: no `<!-- MODULE -->` markers
- R002: no leading-space ` module:` / ` /module`
- R003: module open/close counts match
- R004: no markdown headers inside module blocks
- R005: no `{#heading-id}` tokens
- R006: no `<name>` placeholders (prefer `{name}`)

## Install
This tool is pure Python. It uses `pyyaml` to read the config.
If you don't have it: `pip install pyyaml`

## Run
From repo root:
- `python tools/diag/blu_repo_diag.py --root . --config tools/diag/blu_repo_diag_rules.yaml`

Optional auto-fix for leading-space tokens:
- `python tools/diag/blu_repo_diag.py --root . --config tools/diag/blu_repo_diag_rules.yaml --fix-whitespace`

## Extend
1) Add a rule key under `rules:` in `blu_repo_diag_rules.yaml`
2) Add scanner logic in `blu_repo_diag.py` (or keep it minimal and reuse existing scans)
3) Keep outputs deterministic: always print top 10 findings per rule.
