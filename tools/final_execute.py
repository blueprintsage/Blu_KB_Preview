#!/usr/bin/env python3
import os
import csv
import shutil
from pathlib import Path

SOURCES_ROOT = Path("D:/Repos/PASS/sources")
SORT_DIR = Path("D:/Repos/PASS/sort")
MANIFEST_CSV = SORT_DIR / "manifest_final.csv"
APPLIED_LOG = SORT_DIR / "applied_log_comprehensive.csv"

def main():
    import sys
    dry_run = "--dry-run" in sys.argv or len(sys.argv) == 1

    print("="*70)
    print("FINAL EXECUTION - FULL LIBRARY REORGANIZATION")
    print("="*70)
    if dry_run:
        print("MODE: DRY RUN (no files will be moved)")
    else:
        print("MODE: REAL RUN (files WILL BE MOVED & RENAMED)")
    print("="*70)

    # Load manifest
    print("\nLoading manifest...")
    manifest = []
    with open(MANIFEST_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        manifest = list(reader)

    # Separate by action
    to_move = [m for m in manifest if m['action'] == 'MOVE']
    to_remove = [m for m in manifest if m['action'] == 'REMOVE']

    print(f"  Files to move:   {len(to_move)}")
    print(f"  Files to remove: {len(to_remove)}")

    # Show samples
    print(f"\nSample moves:")
    for item in to_move[:5]:
        old_name = Path(item['old_path']).name
        new_name = Path(item['new_path']).name
        print(f"  {old_name}")
        print(f"  → {item['new_path'].split('/')[0]}/{new_name}")

    if to_remove:
        print(f"\nSample removals:")
        for item in to_remove[:3]:
            print(f"  - {Path(item['old_path']).name}")

    if dry_run:
        print(f"\n{'='*70}")
        print(f"DRY RUN COMPLETE")
        print(f"To execute, run: python tools/final_execute.py --real")
        return 0

    # EXECUTE MOVES
    print(f"\n{'='*70}")
    print(f"EXECUTING...")
    print(f"{'='*70}\n")

    applied_log = []
    move_count = 0
    remove_count = 0
    error_count = 0

    # Remove files first
    print("Removing duplicates and MOBIs...")
    for item in to_remove:
        old_path = SOURCES_ROOT / item['old_path']
        if old_path.exists():
            try:
                old_path.unlink()
                remove_count += 1
                applied_log.append({
                    'old_path': item['old_path'],
                    'action': 'REMOVED',
                    'status': 'success',
                })
            except Exception as e:
                error_count += 1
                applied_log.append({
                    'old_path': item['old_path'],
                    'action': 'REMOVE',
                    'status': f'ERROR: {e}',
                })

    print(f"  {remove_count} files removed")

    # Move and rename files
    print("\nMoving and renaming files...")
    for i, item in enumerate(to_move):
        old_path_str = item['old_path']
        new_path_str = item['new_path']
        old_path = SOURCES_ROOT / old_path_str
        new_path = SOURCES_ROOT / new_path_str.replace('/', '\\')

        if not old_path.exists():
            error_count += 1
            applied_log.append({
                'old_path': old_path_str,
                'new_path': new_path_str,
                'action': 'MOVE',
                'status': 'ERROR: source not found',
            })
            continue

        try:
            # Create destination directory
            new_path.parent.mkdir(parents=True, exist_ok=True)

            # Check if destination exists
            if new_path.exists():
                print(f"  ⚠️  Skipping {Path(old_path_str).name} - destination exists")
                applied_log.append({
                    'old_path': old_path_str,
                    'new_path': new_path_str,
                    'action': 'SKIP',
                    'status': 'destination exists',
                })
                continue

            # Move file
            shutil.move(str(old_path), str(new_path))
            move_count += 1

            applied_log.append({
                'old_path': old_path_str,
                'new_path': new_path_str,
                'action': 'MOVE',
                'status': 'success',
            })

            if (i + 1) % 100 == 0:
                print(f"  {move_count} files moved...")

        except Exception as e:
            error_count += 1
            applied_log.append({
                'old_path': old_path_str,
                'new_path': new_path_str,
                'action': 'MOVE',
                'status': f'ERROR: {e}',
            })

    # Write log
    with open(APPLIED_LOG, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['old_path', 'new_path', 'action', 'status'])
        writer.writeheader()
        writer.writerows(applied_log)

    # Clean up empty folders
    print("\nCleaning up empty folders...")
    empty_count = 0
    for root, dirs, files in os.walk(SOURCES_ROOT, topdown=False):
        for dirname in dirs:
            folder_path = Path(root) / dirname
            try:
                if not any(folder_path.iterdir()):
                    folder_path.rmdir()
                    empty_count += 1
            except:
                pass

    print(f"  {empty_count} empty folders removed")

    # Report
    print(f"\n{'='*70}")
    print(f"EXECUTION COMPLETE!")
    print(f"{'='*70}")
    print(f"Files moved:      {move_count}")
    print(f"Files removed:    {remove_count}")
    print(f"Errors:           {error_count}")
    print(f"Empty folders:    {empty_count}")
    print(f"\nApplied log: {APPLIED_LOG}")
    print(f"\n✨ Library reorganization complete!")

    return 0

if __name__ == "__main__":
    exit(main())
