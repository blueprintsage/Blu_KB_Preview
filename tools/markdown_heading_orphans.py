\
#!/usr/bin/env python3
markdown_heading_orphans.py
Flags headings that have no content before the next heading.

Usage:
  python markdown_heading_orphans.py <root_folder>

Example:
  python markdown_heading_orphans.py skills

import sys
from pathlib import Path
import re

HEAD = re.compile(r'^(#{1,6})\s+\S', re.M)

def is_blank_or_comment(line: str) -> bool:
    s=line.strip()
    return (s=="" or s.startswith("<!--") or s.startswith("-->"))

def main():
    root = Path(sys.argv[1] if len(sys.argv)>1 else ".")
    bad=[]
    for p in root.rglob("*.md"):
        text=p.read_text(encoding="utf-8", errors="ignore")
        lines=text.splitlines()
        heading_idxs=[i for i,l in enumerate(lines) if re.match(r'^\s*#{1,6}\s+\S', l)]
        for idx_i, i in enumerate(heading_idxs):
            j = heading_idxs[idx_i+1] if idx_i+1 < len(heading_idxs) else len(lines)
            # content lines between i+1 and j
            content = lines[i+1:j]
            # ignore blank/comment-only
            meaningful=[ln for ln in content if not is_blank_or_comment(ln) and not re.match(r'^\s*#{1,6}\s+\S', ln)]
            if len(meaningful)==0:
                bad.append((p.as_posix(), i+1, lines[i].strip()))
    if not bad:
        print("OK: no orphan headings found.")
        return 0
    print("Orphan headings found:")
    for fp, ln, h in bad:
        print(f"- {fp}:{ln}: {h}")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
