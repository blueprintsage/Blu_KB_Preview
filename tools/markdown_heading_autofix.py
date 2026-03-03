\
#!/usr/bin/env python3
markdown_heading_autofix.py
Auto-fix orphan Markdown headings by inserting a placeholder line.

Orphan heading = a heading whose section contains no meaningful content
before the next heading (blank lines + HTML comments ignored).

Default placeholder inserted:
  > TODO (placeholder): <fill this section>

Usage:
  # dry run (no changes), exit 1 if any orphans found
  python tools/markdown_heading_autofix.py skills --check

  # apply fixes in-place
  python tools/markdown_heading_autofix.py skills --apply

Options:
  --placeholder "..."   Custom placeholder line (must be a single line)
  --ext .md             File extension to scan (default .md)
  --backup              Write a .bak copy beside each modified file

import argparse
import re
from pathlib import Path

HEADING_RE = re.compile(r'^\s*#{1,6}\s+\S')

def is_blank_or_comment(line: str) -> bool:
    s = line.strip()
    return s == "" or s.startswith("<!--") or s.endswith("-->") or s.startswith("-->")

def section_has_meaningful_content(lines) -> bool:
    for ln in lines:
        if HEADING_RE.match(ln):
            return False
        if is_blank_or_comment(ln):
            continue
        # any non-empty, non-comment, non-heading content counts
        return True
    return False

def find_orphan_headings(lines):
    idxs = [i for i,l in enumerate(lines) if HEADING_RE.match(l)]
    orphans = []
    for k,i in enumerate(idxs):
        j = idxs[k+1] if k+1 < len(idxs) else len(lines)
        content = lines[i+1:j]
        if not section_has_meaningful_content(content):
            orphans.append((i,j))
    return orphans

def apply_fixes(text: str, placeholder: str) -> tuple[str,int]:
    lines = text.splitlines()
    orphans = find_orphan_headings(lines)
    if not orphans:
        return text, 0

    # Insert placeholder line after each orphan heading.
    # Work from bottom to top so indices stay valid.
    inserts = 0
    for i,j in reversed(orphans):
        # Insert after the heading line, but after any immediate blank/comment lines? No:
        # we want placeholder to be the first content line.
        insert_at = i + 1
        # If there are already some blank/comment lines, insert before them? Either is fine.
        # We'll insert at i+1 so placeholder is immediately under heading.
        lines.insert(insert_at, placeholder)
        inserts += 1

    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), inserts

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default="skills", help="Root folder to scan (default: skills)")
    ap.add_argument("--check", action="store_true", help="Dry run; do not modify files. Exit 1 if orphans found.")
    ap.add_argument("--apply", action="store_true", help="Modify files in-place.")
    ap.add_argument("--placeholder", default="> TODO (placeholder): <fill this section>", help="Single-line placeholder to insert.")
    ap.add_argument("--ext", default=".md", help="File extension to scan (default: .md)")
    ap.add_argument("--backup", action="store_true", help="Write a .bak copy beside each modified file.")
    args = ap.parse_args()

    if not (args.check or args.apply):
        ap.error("Choose one: --check or --apply")

    placeholder = args.placeholder.strip("\n")
    if "\n" in placeholder:
        ap.error("--placeholder must be a single line")

    root = Path(args.root)
    if not root.exists():
        print(f"ERROR: root folder not found: {root}")
        return 2

    total_orphans = 0
    modified_files = 0

    for p in root.rglob(f"*{args.ext}"):
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            text = p.read_text(encoding="utf-8", errors="ignore")

        new_text, inserts = apply_fixes(text, placeholder)
        if inserts > 0:
            total_orphans += inserts
            if args.apply:
                if args.backup:
                    p.with_suffix(p.suffix + ".bak").write_text(text, encoding="utf-8")
                p.write_text(new_text, encoding="utf-8")
                modified_files += 1
            else:
                # check mode: report
                print(f"- {p.as_posix()}: {inserts} orphan heading(s)")

    if args.check:
        if total_orphans == 0:
            print("OK: no orphan headings found.")
            return 0
        print(f"FOUND: {total_orphans} orphan heading(s).")
        return 1

    # apply mode
    if total_orphans == 0:
        print("No changes needed.")
        return 0

    print(f"Fixed {total_orphans} orphan heading(s) across {modified_files} file(s).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
