#!/usr/bin/env python3
import os
import csv
import shutil
from pathlib import Path

SOURCES_ROOT = Path("D:/Repos/PASS/sources")
SORT_DIR = Path("D:/Repos/PASS/sort")
MANIFEST_CSV = SORT_DIR / "manifest_textbooks.csv"
APPLIED_LOG = SORT_DIR / "applied_log_final.csv"

def main():
    import sys
    dry_run = "--dry-run" in sys.argv or len(sys.argv) == 1

    print("=" * 70)
    print("FINAL ORGANIZATION - TEXTBOOKS & NEW FILES")
    print("=" * 70)
    if dry_run:
        print("MODE: DRY RUN (no files will be moved)")
    else:
        print("MODE: REAL RUN (files WILL BE MOVED)")
    print("=" * 70)

    # Load manifest
    print("\nLoading manifest...")
    manifest = []
    with open(MANIFEST_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        manifest = list(reader)

    print(f"  {len(manifest)} files to organize")

    # Execute moves
    applied_log = []
    move_count = 0
    error_count = 0

    for row in manifest:
        old_path_str = row['old_path']
        new_path_str = row['new_path']
        old_path = SOURCES_ROOT / old_path_str
        new_path = SOURCES_ROOT / new_path_str.replace('/', '\\')

        if not old_path.exists():
            print(f"  ⚠️  Source not found: {old_path_str}")
            continue

        try:
            if dry_run:
                print(f"  PLAN: {Path(old_path_str).name}")
                print(f"        → {'/'.join(new_path_str.split('/')[-2:])}")
            else:
                # Create destination directory
                new_path.parent.mkdir(parents=True, exist_ok=True)

                # Move file
                if new_path.exists():
                    print(f"  ⚠️  Destination exists, skipping: {new_path_str}")
                else:
                    shutil.move(str(old_path), str(new_path))
                    move_count += 1

                    if move_count % 5 == 0:
                        print(f"  {move_count} files moved...")

                applied_log.append({
                    'old_path': old_path_str,
                    'new_path': new_path_str,
                    'status': 'moved',
                })

        except Exception as e:
            error_count += 1
            print(f"  ❌ {old_path_str}: {e}")
            applied_log.append({
                'old_path': old_path_str,
                'new_path': new_path_str,
                'status': f'ERROR: {e}',
            })

    if dry_run:
        print(f"\nDRY RUN COMPLETE")
        print(f"To execute, run: python tools/sort_execute_final.py --real")
        return 0

    # Write log
    with open(APPLIED_LOG, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['old_path', 'new_path', 'status'])
        writer.writeheader()
        writer.writerows(applied_log)

    print(f"\n{move_count} files moved")

    # Clean up empty folders
    print("\nCleaning up empty folders...")
    empty_folders = []
    for root, dirs, files in os.walk(SOURCES_ROOT, topdown=False):
        for dirname in dirs:
            folder_path = Path(root) / dirname
            if not any(folder_path.iterdir()):
                try:
                    folder_path.rmdir()
                    empty_folders.append(str(folder_path.relative_to(SOURCES_ROOT)))
                    print(f"  Deleted: {folder_path.name}")
                except:
                    pass

    print(f"  {len(empty_folders)} empty folders removed")

    print(f"\n{'=' * 70}")
    print(f"ORGANIZATION COMPLETE!")
    print(f"{'=' * 70}")
    print(f"Files moved: {move_count}")
    print(f"Errors: {error_count}")
    print(f"Empty folders removed: {len(empty_folders)}")
    print(f"Applied log: {APPLIED_LOG}")

    return 0

if __name__ == "__main__":
    exit(main())
