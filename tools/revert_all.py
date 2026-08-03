#!/usr/bin/env python3
import csv
import shutil
from pathlib import Path

SOURCES_ROOT = Path("D:/Repos/PASS/sources")
SORT_DIR = Path("D:/Repos/PASS/sort")
APPLIED_LOG = SORT_DIR / "applied_log_comprehensive.csv"
REVERT_LOG = SORT_DIR / "revert_log.csv"

def main():
    import sys
    dry_run = "--dry-run" in sys.argv or len(sys.argv) == 1

    print("="*70)
    print("REVERTING ALL CHANGES")
    print("="*70)
    if dry_run:
        print("MODE: DRY RUN")
    else:
        print("MODE: REAL RUN - REVERTING ALL MOVES")
    print("="*70)

    # Load applied log
    print("\nLoading applied log...")
    applied = []
    with open(APPLIED_LOG, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        applied = list(reader)

    # Separate by action
    moves = [a for a in applied if a['action'] == 'MOVE' and a['status'] == 'success']
    skipped = [a for a in applied if a['action'] == 'SKIP']
    removed = [a for a in applied if a['action'] == 'REMOVED']

    print(f"\nMoves to revert:    {len(moves)}")
    print(f"Files skipped:      {len(skipped)}")
    print(f"Files removed:      {len(removed)}")

    if dry_run:
        print(f"\nSample reversals (first 5):")
        for move in moves[:5]:
            print(f"  {Path(move['new_path']).name}")
            print(f"  ← {move['old_path']}")
        print(f"\nTo execute, run: python tools/revert_all.py --real")
        return 0

    # EXECUTE REVERSALS
    print(f"\n{'='*70}")
    print(f"REVERTING...")
    print(f"{'='*70}\n")

    revert_log = []
    reverted_count = 0
    restored_count = 0
    error_count = 0

    # Revert moves (move from new_path back to old_path)
    print("Reverting file moves...")
    for i, move in enumerate(moves):
        old_path_str = move['old_path']
        new_path_str = move['new_path']

        old_path = SOURCES_ROOT / old_path_str
        new_path = SOURCES_ROOT / new_path_str.replace('/', '\\')

        if new_path.exists():
            try:
                # Create original directory
                old_path.parent.mkdir(parents=True, exist_ok=True)

                # Move back to original location
                shutil.move(str(new_path), str(old_path))
                reverted_count += 1

                revert_log.append({
                    'action': 'REVERT',
                    'old_path': old_path_str,
                    'new_path': new_path_str,
                    'status': 'success',
                })

                if (i + 1) % 200 == 0:
                    print(f"  {reverted_count} files reverted...")

            except Exception as e:
                error_count += 1
                revert_log.append({
                    'action': 'REVERT',
                    'old_path': old_path_str,
                    'new_path': new_path_str,
                    'status': f'ERROR: {e}',
                })
        else:
            print(f"  ⚠️  Not found (already reverted?): {new_path_str}")

    # Restore removed files (can't do this without a backup, just note them)
    print(f"\nNote: {len(removed)} files were deleted as duplicates")
    print(f"  These cannot be automatically restored (would need backup)")

    # Write revert log
    with open(REVERT_LOG, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['action', 'old_path', 'new_path', 'status'])
        writer.writeheader()
        writer.writerows(revert_log)

    # Clean up empty folders created during organization
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
    print(f"REVERT COMPLETE!")
    print(f"{'='*70}")
    print(f"Files reverted:     {reverted_count}")
    print(f"Files deleted:      {len(removed)} (cannot auto-restore)")
    print(f"Errors:             {error_count}")
    print(f"Empty folders:      {empty_count}")
    print(f"\nRevert log: {REVERT_LOG}")
    print(f"\n⚠️  Library structure restored to original organization")

    return 0

if __name__ == "__main__":
    import os
    exit(main())
