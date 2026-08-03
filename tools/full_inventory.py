#!/usr/bin/env python3
import os
import csv
import hashlib
import re
from pathlib import Path
from collections import defaultdict

SOURCES_ROOT = Path("D:/Repos/PASS/sources")
SORT_DIR = Path("D:/Repos/PASS/sort")
OUTPUT_CSV = SORT_DIR / "full_inventory.csv"

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
    except:
        return "ERROR"

def extract_metadata(filename):
    """Extract author, edition, year from filename."""
    lower_name = filename.lower()

    # Try to find year (4 digits)
    year_match = re.search(r'\b(19|20)\d{2}\b', filename)
    year = year_match.group(0) if year_match else ""

    # Try to find edition (ed, edition, etc.)
    edition_match = re.search(r'(\d+(?:st|nd|rd|th)?)\s+(?:ed|edition)', lower_name, re.IGNORECASE)
    edition = edition_match.group(0) if edition_match else ""

    # Try to find author (before dash or comma)
    author = ""
    if " - " in filename:
        author = filename.split(" - ")[0].strip()
    elif filename.count(",") > 0:
        author = filename.split(",")[0].strip()

    return {
        'author': author[:50],  # Limit to 50 chars
        'edition': edition,
        'year': year,
    }

def main():
    SORT_DIR.mkdir(parents=True, exist_ok=True)

    print("="*70)
    print("FULL LIBRARY INVENTORY")
    print("="*70)
    print("\nScanning all files in sources/...\n")

    files = []
    hashes = defaultdict(list)
    mobi_files = []
    zip_art_books = []

    supported_formats = {'.pdf', '.epub', '.mobi', '.zip'}

    for root, dirs, filenames in os.walk(SOURCES_ROOT):
        for filename in filenames:
            filepath = Path(root) / filename
            ext = filepath.suffix.lower()

            if ext not in supported_formats:
                continue

            try:
                size = filepath.stat().st_size
                sha = sha256_file(filepath)
                rel_path = filepath.relative_to(SOURCES_ROOT)

                # Extract metadata
                metadata = extract_metadata(filename)

                # Flag .mobi files
                if ext == '.mobi':
                    mobi_files.append(str(rel_path))

                # Flag zip art books
                if ext == '.zip':
                    zip_art_books.append(str(rel_path))

                file_info = {
                    'path': str(rel_path),
                    'filename': filename,
                    'extension': ext,
                    'size': size,
                    'sha256': sha,
                    'author': metadata['author'],
                    'edition': metadata['edition'],
                    'year': metadata['year'],
                }

                files.append(file_info)
                hashes[sha].append(str(rel_path))

            except Exception as e:
                print(f"ERROR reading {filepath}: {e}")

    # Find duplicates and mobi candidates for removal
    duplicates = {h: paths for h, paths in hashes.items() if len(paths) > 1}

    # Find .mobi files that have PDF/EPUB equivalents
    mobi_to_remove = []
    for mobi_path in mobi_files:
        base_name = Path(mobi_path).stem
        # Check if PDF or EPUB exists with same base name
        for file_info in files:
            if file_info['extension'] != '.mobi':
                if Path(file_info['path']).stem == base_name:
                    mobi_to_remove.append(mobi_path)
                    break

    # Write inventory
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['path', 'filename', 'extension', 'size', 'sha256', 'author', 'edition', 'year'])
        writer.writeheader()
        writer.writerows(files)

    # Report
    print(f"\n{'='*70}")
    print(f"INVENTORY RESULTS")
    print(f"{'='*70}")
    print(f"\nTotal files: {len(files)}")
    print(f"  PDFs:      {len([f for f in files if f['extension'] == '.pdf'])}")
    print(f"  EPUBs:     {len([f for f in files if f['extension'] == '.epub'])}")
    print(f"  MOBIs:     {len([f for f in files if f['extension'] == '.mobi'])}")
    print(f"  ZIPs:      {len([f for f in files if f['extension'] == '.zip'])}")

    print(f"\nDuplicate groups: {len(duplicates)}")
    if duplicates:
        dup_count = sum(len(paths) - 1 for paths in duplicates.values())
        print(f"  Duplicate files to remove: {dup_count}")

    print(f"\n.MOBI files: {len(mobi_files)}")
    print(f"  Can be removed (PDF/EPUB exists): {len(mobi_to_remove)}")
    if mobi_to_remove:
        for path in mobi_to_remove[:5]:
            print(f"    - {Path(path).name}")
        if len(mobi_to_remove) > 5:
            print(f"    ... and {len(mobi_to_remove) - 5} more")

    print(f"\nArt ZIP files: {len(zip_art_books)}")
    if zip_art_books:
        for path in zip_art_books[:5]:
            print(f"    - {Path(path).name}")
        if len(zip_art_books) > 5:
            print(f"    ... and {len(zip_art_books) - 5} more")

    print(f"\nFiles with metadata extracted:")
    with_author = len([f for f in files if f['author']])
    with_year = len([f for f in files if f['year']])
    with_edition = len([f for f in files if f['edition']])
    print(f"  With author:  {with_author}")
    print(f"  With year:    {with_year}")
    print(f"  With edition: {with_edition}")

    print(f"\nInventory saved: {OUTPUT_CSV}")
    print(f"Next: Classify unsorted files and generate manifest")

if __name__ == "__main__":
    main()
