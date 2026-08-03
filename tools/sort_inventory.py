#!/usr/bin/env python3
import os
import hashlib
import csv
from pathlib import Path
from collections import defaultdict

SOURCES_ROOT = Path("D:/Repos/PASS/sources")
SORT_DIR = Path("D:/Repos/PASS/sort")
OUTPUT_CSV = SORT_DIR / "inventory.csv"

# Folders to inventory (the unsorted piles)
SCOPE_FOLDERS = [
    "!Programming Books/Unsorted",
    "100 For Dummies Series Books Collection",
    "100 For Dummies Series Books Collection Pack-2",
    "100 For Dummies Series Books Collection Pack-3",
    "20 For Dummies Books Collection Pack-1",
    "20 For Dummies Books Collection Pack-2",
    "HUMBLE BUNDLE - Linux Geek",
    "Humble Book Bundle Coder's Bookshelf by No Starch",
    "Textbooks",
    "ChatGPT",
]

def sha256_file(filepath, chunk_size=65536):
    """Compute SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return f"ERROR: {e}"

def walk_scope():
    """Walk all files in scope folders."""
    files = []
    for folder in SCOPE_FOLDERS:
        folder_path = SOURCES_ROOT / folder
        if not folder_path.exists():
            print(f"WARNING: Folder not found: {folder_path}")
            continue

        for root, dirs, filenames in os.walk(folder_path):
            for filename in filenames:
                filepath = Path(root) / filename
                try:
                    size = filepath.stat().st_size
                    ext = filepath.suffix.lower()
                    sha256 = sha256_file(filepath)
                    rel_path = filepath.relative_to(SOURCES_ROOT)
                    files.append({
                        'path': str(rel_path),
                        'size': size,
                        'extension': ext,
                        'sha256': sha256,
                    })
                except Exception as e:
                    print(f"ERROR reading {filepath}: {e}")

    return files

def main():
    # Create sort dir if needed
    SORT_DIR.mkdir(parents=True, exist_ok=True)

    print("Scanning scope folders...")
    files = walk_scope()

    # Write CSV
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['path', 'size', 'extension', 'sha256'])
        writer.writeheader()
        writer.writerows(files)

    # Find duplicates
    hashes = defaultdict(list)
    for file_info in files:
        hashes[file_info['sha256']].append(file_info['path'])

    duplicates = {h: paths for h, paths in hashes.items() if len(paths) > 1}

    # Report
    print(f"\n=== INVENTORY COMPLETE ===")
    print(f"Total files: {len(files)}")
    print(f"Output: {OUTPUT_CSV}")

    if duplicates:
        print(f"\nDuplicate groups (same SHA256): {len(duplicates)}")
        for sha, paths in sorted(duplicates.items()):
            print(f"\n  SHA256: {sha}")
            for path in paths:
                print(f"    {path}")
    else:
        print("\nNo exact duplicates found.")

if __name__ == "__main__":
    main()
