# PASS Source Registry

status: active
owner: docs/domains/corpus
last_reviewed: 2026-07-30

**This file is the duplicate guard.** Before creating a `source_id` or a
`ledger/<source_id>/` folder, hash the file and search this table for that hash.
If the hash is here, the book has already been processed — stop, and read its row.

```bash
sha256sum "sources/<file>"                       # git bash
```
```powershell
Get-FileHash "sources\<file>" -Algorithm SHA256  # powershell
```

Format and the full decision table: `docs/PASS/PASS_LEDGER.md` → REGISTRY.md.

`status`: `queued` · `in-progress` · `complete` · `low-yield` · `abandoned`

`units` is done/total, where "done" counts `processed` + `empty` + `blocked`.
Ground truth for counts is each source's `UNITS.md`; this table is a summary and
can go stale. If they disagree, the ledger wins.

| source_id | title | author | sha256 (first 12) | status | units | objects | closed |
|---|---|---|---|---|---|---|---|
| burne_hogarth_dynamic_figure_drawing_ocr | Dynamic Figure Drawing | Burne Hogarth | b0d97d495ca3 | in-progress | 4/7 | 44 | |
| gen1_art_fundamentals_4step | PASS Gen 1 Universal Step 0 + Four-Stage Workflow | Blu + Admin | d53b1c8b031f | complete | 1/1 | 2 | 2026-07-31 |
| gcbc_think_like_swe | Good Code, Bad Code: Think Like a Software Engineer | Tom Long | 35e22cad8052 | complete | 11/11 | 122 | 2026-07-31 |
| effective_cpp_3e | Effective C++, 3rd ed. | Scott Meyers | 4f983195c37c | complete | 9/9 | 80 | 2026-08-01 |
| cpp_core_guidelines | C++ Core Guidelines | Stroustrup & Sutter (eds.) | be29ae459bc2 | queued | | | |
| programmers_brain | The Programmer's Brain: What Every Programmer Needs to Know About Cognition | Felienne Hermans | 52063e7300c1 | in-progress | 2/13 | 10 | |
| guided_staged_visual_validation_2026_08_03 | Guided Staged Visual Validation: Warbot and Zero-G Astronaut | Blu + Admin | 401381d45142 | complete | 1/1 | 3 | 2026-08-03 |
