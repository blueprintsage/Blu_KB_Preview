#!/usr/bin/env python3
"""Execute sort/manifest2.csv. Dry-run by default.

Safety properties, in order of importance:
  - dry-run unless --execute is passed
  - never overwrites: a destination that already exists is hash-compared.
    Identical -> the incoming copy goes to trash/dupes/ (reversible quarantine).
    Different -> skipped and reported; two different scans are not a duplicate.
  - writes sort/applied_log2.csv (old,new) so every move can be reversed
  - counts files before and after; a mismatch is an error, not a warning

sources/ is gitignored. This log is the only undo that exists.

Usage:
    python tools/sort_apply2.py                # dry run
    python tools/sort_apply2.py --execute      # do it
"""
from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
MANIFEST = ROOT / "sort" / "manifest2.csv"
LOG = ROOT / "sort" / "applied_log2.csv"
DUPES = ROOT / "trash" / "dupes"


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def count_files(base: Path) -> int:
    return sum(1 for p in base.rglob("*") if p.is_file())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()
    live = args.execute

    rows = list(csv.DictReader(open(MANIFEST, encoding="utf-8")))
    before = count_files(SOURCES)

    moves: list[tuple[Path, Path]] = []
    dupes: list[tuple[Path, Path]] = []
    skipped: list[tuple[str, str]] = []

    for r in rows:
        src = SOURCES / r["old_path"]
        dst = SOURCES / r["new_path"]
        if not src.exists():
            skipped.append((r["old_path"], "source missing"))
            continue
        if dst.exists():
            if sha(src) == sha(dst):
                dupes.append((src, DUPES / src.name))
            else:
                skipped.append((r["old_path"],
                                "destination exists with DIFFERENT content"))
            continue
        moves.append((src, dst))

    tag = "" if live else "[dry-run] "
    print("%smanifest rows      : %d" % (tag, len(rows)))
    print("%splain moves        : %d" % (tag, len(moves)))
    print("%sexact dupes -> trash: %d" % (tag, len(dupes)))
    print("%sskipped            : %d" % (tag, len(skipped)))
    for p, why in skipped:
        print("     ! %-70s %s" % (p[:70], why))
    for s, d in dupes:
        print("     dupe: %s" % s.relative_to(SOURCES))

    if not live:
        print("\n%snothing was moved. Re-run with --execute." % tag)
        return 0

    DUPES.mkdir(parents=True, exist_ok=True)
    written = []
    for s, d in moves:
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(s), str(d))
        written.append((str(s.relative_to(SOURCES)), str(d.relative_to(SOURCES))))
    for s, d in dupes:
        shutil.move(str(s), str(d))
        written.append((str(s.relative_to(SOURCES)), "../trash/dupes/" + d.name))

    # APPEND, never truncate. This log is the only undo that exists for a
    # gitignored tree; a second run must not erase the first run's reversal
    # path. (It did once - recovered from git.)
    fresh = not LOG.exists()
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if fresh:
            w.writerow(["run", "old_path", "new_path"])
        stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        for old, new in written:
            w.writerow([stamp, old, new])

    after = count_files(SOURCES)
    print("\nmoved      : %d" % len(written))
    print("log        : %s" % LOG.relative_to(ROOT))
    print("files before/after in sources/: %d / %d  (%+d)" % (before, after, after - before))
    if after != before - len(dupes):
        print("!! COUNT MISMATCH — investigate before doing anything else")
        return 1
    print("count reconciles (difference == files quarantined as dupes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
