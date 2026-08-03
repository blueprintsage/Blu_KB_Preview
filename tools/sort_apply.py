#!/usr/bin/env python3
import os
import csv
import shutil
from pathlib import Path
from collections import defaultdict

SOURCES_ROOT = Path("D:/Repos/PASS/sources")
TRASH_DUPES = Path("D:/Repos/PASS/trash/dupes")
SORT_DIR = Path("D:/Repos/PASS/sort")
MANIFEST_CSV = SORT_DIR / "manifest.csv"
INVENTORY_CSV = SORT_DIR / "inventory.csv"
APPLIED_LOG = SORT_DIR / "applied_log.csv"

def load_inventory():
    """Load inventory to get sha256 hashes."""
    hashes = {}
    with open(INVENTORY_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hashes[row['path']] = row['sha256']
    return hashes

def find_duplicates(hashes):
    """Find exact duplicates (same SHA256)."""
    sha_to_paths = defaultdict(list)
    for path, sha in hashes.items():
        sha_to_paths[sha].append(path)
    duplicates = {sha: paths for sha, paths in sha_to_paths.items() if len(paths) > 1}
    return duplicates

def main():
    import sys
    dry_run = "--dry-run" in sys.argv or len(sys.argv) == 1

    print("=" * 70)
    print("PHASE 4 - EXECUTE SORT")
    print("=" * 70)
    if dry_run:
        print("MODE: DRY RUN (no files will be moved)")
    else:
        print("MODE: REAL RUN (files WILL BE MOVED)")
    print("=" * 70)

    # Load data
    print("\nLoading manifest and inventory...")
    manifest = []
    with open(MANIFEST_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        manifest = list(reader)

    hashes = load_inventory()
    duplicates = find_duplicates(hashes)

    print(f"  Manifest: {len(manifest)} moves planned")
    print(f"  Duplicate groups: {len(duplicates)}")

    # Check for collisions (skip files already at destination or where dest exists)
    print("\nChecking for destination conflicts...")
    skipped_already_there = []
    skipped_dest_exists = []
    filtered_manifest = []

    for row in manifest:
        old_path_str = row['old_path']
        new_path_str = row['new_path']
        old_path = SOURCES_ROOT / old_path_str
        new_path = SOURCES_ROOT / new_path_str

        # Skip if file is already at destination (already organized)
        if old_path == new_path:
            skipped_already_there.append(old_path_str)
            continue

        # Skip if source doesn't exist (should not happen, but be safe)
        if not old_path.exists():
            skipped_dest_exists.append((old_path_str, new_path_str, "source not found"))
            continue

        # If destination already exists, skip (treat as duplicate to trash)
        if new_path.exists():
            skipped_dest_exists.append((old_path_str, new_path_str, "destination already exists"))
            continue

        filtered_manifest.append(row)

    if skipped_already_there:
        print(f"  ℹ️  {len(skipped_already_there)} files already in correct location")

    if skipped_dest_exists:
        print(f"  ⚠️  {len(skipped_dest_exists)} files skipped (destination exists, likely duplicates)")
        for old, new, reason in skipped_dest_exists[:5]:
            print(f"     {Path(old).name} → {Path(new).name}")
        if len(skipped_dest_exists) > 5:
            print(f"     ... and {len(skipped_dest_exists) - 5} more")

    print(f"  ✓ Ready to move {len(filtered_manifest)} files.")

    # Categorize moves
    normal_moves = []
    duplicate_moves = []

    for row in filtered_manifest:
        old_path_str = row['old_path']
        new_path_str = row['new_path']

        # Check if this file is a duplicate
        sha = hashes.get(old_path_str, "")
        if sha in duplicates and len(duplicates[sha]) > 1:
            # This is a duplicate - send to trash/dupes
            filename = Path(old_path_str).name
            new_path_str = f"trash/dupes/{filename}"
            duplicate_moves.append((old_path_str, new_path_str, sha))
        else:
            normal_moves.append((old_path_str, new_path_str))

    print(f"\n  Normal moves: {len(normal_moves)}")
    print(f"  Duplicate moves (→ trash/dupes): {len(duplicate_moves)}")

    # Plan all moves
    all_moves = [(old, new, False) for old, new in normal_moves] + \
               [(old, new, True) for old, new, _ in duplicate_moves]

    # Show samples
    print(f"\n=== SAMPLE MOVES (first 20) ===")
    for i, (old, new, is_dup) in enumerate(all_moves[:20], 1):
        marker = "[DUP] " if is_dup else "[MOV] "
        print(f"{i:2}. {marker}{Path(old).name[:50]}")
        print(f"    → {new}")

    if len(all_moves) > 20:
        print(f"\n... and {len(all_moves) - 20} more moves")

    print(f"\n{'DRY RUN' if dry_run else 'READY TO EXECUTE'}")

    if dry_run:
        print("\nTo execute for real, run: python tools/sort_apply.py --real")
        return 0

    # ===== REAL RUN =====
    print("\n" + "=" * 70)
    print("EXECUTING MOVES...")
    print("=" * 70)

    applied_log = []
    move_count = 0
    error_count = 0

    for old_path_str, new_path_str, is_dup in all_moves:
        old_path = SOURCES_ROOT / old_path_str
        new_path = SOURCES_ROOT / new_path_str

        try:
            # Create destination directory
            new_path.parent.mkdir(parents=True, exist_ok=True)

            # Move file
            shutil.move(str(old_path), str(new_path))

            applied_log.append({
                'old_path': old_path_str,
                'new_path': new_path_str,
                'status': 'moved',
            })
            move_count += 1

            if move_count % 100 == 0:
                print(f"  {move_count} files moved...")

        except Exception as e:
            error_count += 1
            applied_log.append({
                'old_path': old_path_str,
                'new_path': new_path_str,
                'status': f'ERROR: {e}',
            })
            print(f"  ❌ {old_path_str}: {e}")

    # Write log
    with open(APPLIED_LOG, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['old_path', 'new_path', 'status'])
        writer.writeheader()
        writer.writerows(applied_log)

    # Report
    print(f"\n=== EXECUTION COMPLETE ===")
    print(f"Files moved: {move_count}")
    print(f"Errors: {error_count}")
    print(f"Applied log: {APPLIED_LOG}")

    if error_count == 0:
        print("\n✓ All files moved successfully!")
    else:
        print(f"\n⚠️  {error_count} errors occurred. Check {APPLIED_LOG}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
