#!/usr/bin/env python3
import csv
from pathlib import Path
from collections import defaultdict

SORT_DIR = Path("D:/Repos/PASS/sort")
INVENTORY_CSV = SORT_DIR / "inventory.csv"
MANIFEST_CSV = SORT_DIR / "manifest.csv"

# Existing target taxonomy
EXISTING_PROG_LANGS = [
    "API", "Algorithms", "Android", "Assembly", "C", "C#", "C++",
    "Dot Net", "Game", "Git", "Java", "Perl", "Python", "SQL",
    "Visual Studio", "Windows", "iOS"
]

# Classification rules (filename keywords -> destination)
RULES = [
    # Programming languages (existing dirs first)
    ("python", "!Programming Books/Python", "high"),
    ("java", "!Programming Books/Java", "high"),
    ("c++", "!Programming Books/C++", "high"),
    ("cpp", "!Programming Books/C++", "high"),
    ("c#", "!Programming Books/C#", "high"),
    ("csharp", "!Programming Books/C#", "high"),
    ("kotlin", "!Programming Books/Android", "high"),
    ("android", "!Programming Books/Android", "high"),
    ("ios", "!Programming Books/iOS", "high"),
    ("swift", "!Programming Books/iOS", "high"),
    ("golang", "!Programming Books/Java", "low"),  # Go isn't a category, but might be confused with Java
    ("go web", "!Programming Books/Game", "low"),
    ("perl", "!Programming Books/Perl", "high"),
    ("assembly", "!Programming Books/Assembly", "high"),
    ("sql", "!Programming Books/SQL", "high"),
    ("git", "!Programming Books/Git", "high"),
    ("github", "!Programming Books/Git", "high"),

    # Web/Framework topics
    ("angular", "!Programming Books/Game", "low"),
    ("react", "!Programming Books/Game", "low"),
    ("vue", "!Programming Books/Game", "low"),
    ("node", "!Programming Books/Game", "low"),
    ("web development", "!Programming Books/Game", "low"),
    ("asp.net", "!Programming Books/Dot Net", "high"),
    ("dotnet", "!Programming Books/Dot Net", "high"),
    (".net", "!Programming Books/Dot Net", "high"),

    # DevOps/Infrastructure
    ("kubernetes", "!Programming Books/API", "low"),
    ("docker", "!Programming Books/API", "low"),
    ("aws", "!Programming Books/API", "low"),
    ("azure", "!Programming Books/Windows", "low"),
    ("devops", "!Programming Books/API", "low"),
    ("github", "!Programming Books/Git", "high"),

    # Architecture/Design Patterns
    ("patterns", "!Programming Books/C++", "low"),
    ("refactoring", "!Programming Books/C++", "low"),
    ("clean code", "!Programming Books/C++", "low"),
    ("design pattern", "!Programming Books/C++", "low"),
    ("enterprise", "!Programming Books/C++", "low"),

    # Embedded/Hardware
    ("microcontroller", "!Programming Books/Assembly", "high"),
    ("arduino", "!Programming Books/Assembly", "high"),
    ("raspberry", "!Programming Books/Assembly", "high"),
    ("embedded", "!Programming Books/Assembly", "high"),

    # General/Foundational
    ("pragmatic", "!Programming Books/C++", "low"),
    ("effective", "!Programming Books/C++", "low"),

    # Linux-related
    ("linux", "Linux", "high"),
    ("ubuntu", "Linux", "high"),
    ("bash", "Linux", "high"),
    ("shell", "Linux", "high"),

    # AI/ML/Data
    ("machine learning", "!Programming Books/Algorithms", "high"),
    ("deep learning", "!Programming Books/Algorithms", "high"),
    ("neural", "!Programming Books/Algorithms", "high"),
    ("chatgpt", "!Programming Books/Algorithms", "low"),
    ("ai", "!Programming Books/Algorithms", "high"),
    ("data science", "!Programming Books/Algorithms", "high"),

    # Business/Crypto
    ("cryptocurrency", "Business", "high"),
    ("bitcoin", "Business", "high"),
    ("trading", "Business", "high"),
    ("investing", "Business", "high"),
    ("business", "Business", "high"),

    # For Dummies books
    ("for dummies", "!Programming Books/Algorithms", "low"),  # Default to Algorithms, will be refined
]

def classify_file(filename, source_folder):
    """Classify a file based on its filename."""
    lower_name = filename.lower()

    # Special handling for cover images
    if lower_name.endswith('.jpg') and 'cover' in source_folder.lower():
        return ("Covers/", "high", "Cover image from pack")

    # Check rules
    for keyword, dest, conf in RULES:
        if keyword in lower_name:
            return (dest, conf, f"Matched keyword: {keyword}")

    # Refine "For Dummies" classification by topic
    if "for dummies" in lower_name:
        if any(x in lower_name for x in ["programming", "python", "java", "code", "coding"]):
            return ("!Programming Books/Algorithms", "low", "For Dummies - programming topic")
        elif any(x in lower_name for x in ["business", "crypto", "trading", "investing"]):
            return ("Business", "low", "For Dummies - business topic")
        elif any(x in lower_name for x in ["office", "excel", "word", "windows"]):
            return ("!Programming Books/Windows", "low", "For Dummies - office/Windows")
        else:
            return ("Unsorted", "low", "For Dummies - unclear topic")

    # Default to Unsorted
    return ("Unsorted", "low", "No matching category")

def main():
    print("Reading inventory...")
    files = []
    with open(INVENTORY_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        files = list(reader)

    print(f"Classifying {len(files)} files...")

    manifest = []
    dest_counts = defaultdict(int)

    for file_info in files:
        path = file_info['path']
        source_folder = path.split('\\')[0]
        filename = path.split('\\')[-1]

        dest, confidence, reason = classify_file(filename, source_folder)

        new_path = f"{dest}/{filename}"
        manifest.append({
            'old_path': path,
            'new_path': new_path,
            'confidence': confidence,
            'reason': reason,
        })
        dest_counts[dest] += 1

    # Write manifest
    with open(MANIFEST_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['old_path', 'new_path', 'confidence', 'reason'])
        writer.writeheader()
        writer.writerows(manifest)

    # Report
    print(f"\n=== CLASSIFICATION COMPLETE ===")
    print(f"Manifest saved: {MANIFEST_CSV}")
    print(f"\nFiles by destination:")
    for dest in sorted(dest_counts.keys()):
        conf_info = ""
        high_conf = sum(1 for m in manifest if m['new_path'].startswith(dest) and m['confidence'] == 'high')
        low_conf = sum(1 for m in manifest if m['new_path'].startswith(dest) and m['confidence'] == 'low')
        conf_note = f" ({high_conf} high, {low_conf} low)" if low_conf > 0 else ""
        print(f"  {dest}: {dest_counts[dest]}{conf_note}")

    # Show samples
    print(f"\n=== SAMPLE CLASSIFICATIONS (first 20) ===")
    for i, row in enumerate(manifest[:20], 1):
        print(f"{i:2}. [{row['confidence'].upper():4}] {row['old_path']}")
        print(f"    → {row['new_path']}")
        print(f"       {row['reason']}\n")

if __name__ == "__main__":
    main()
