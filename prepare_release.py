#!/usr/bin/env python3
"""
Prepare project for v1.0 release
Cleans up test files, organizes documentation, and prepares for git push
"""
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).parent

print("=" * 80)
print("PREPARING PO TRANSLATOR v1.0 FOR RELEASE")
print("=" * 80)
print()

# Files to keep
KEEP_DOCS = {
    'README.md',
    'QUICK_START.md',
    'INSTALL_PYTHON312.md',
    'UPGRADE_REPORT.md',
    'V1_COMPLETE_SUMMARY.md',
    'FINAL_V1_STATUS.md',
}

# Files to remove (test files)
REMOVE_FILES = [
    'test_clean_accuracy.py',
    'test_complete_info.py',
    'test_detection_issue.py',
    'test_full_extraction.py',
    'test_imports.py',
    'test_integrated_detection.py',
    'test_lingua_vs_fasttext.py',
    'test_model_extraction.py',
    'test_module_extraction.py',
    'test_po_loading.py',
    'validate_app.py',
    'automated_test.py',
    'test_output_automated.po',
    'app.log',
    '.config',
]

# Documentation to remove (temporary)
REMOVE_DOCS = [
    'test_all_buttons.md',
    'PREMIUM_THEME_GUIDE.md',
]

print("1. Cleaning up test files...")
removed_count = 0
for filename in REMOVE_FILES:
    filepath = ROOT / filename
    if filepath.exists():
        try:
            if filepath.is_file():
                filepath.unlink()
                print(f"   ✓ Removed {filename}")
                removed_count += 1
        except Exception as e:
            print(f"   ✗ Could not remove {filename}: {e}")

print(f"   Removed {removed_count} test files")
print()

print("2. Cleaning up temporary documentation...")
removed_docs = 0
for filename in REMOVE_DOCS:
    filepath = ROOT / filename
    if filepath.exists():
        try:
            filepath.unlink()
            print(f"   ✓ Removed {filename}")
            removed_docs += 1
        except Exception as e:
            print(f"   ✗ Could not remove {filename}: {e}")

print(f"   Removed {removed_docs} temporary docs")
print()

print("3. Organizing documentation...")
docs_dir = ROOT / 'docs'
docs_dir.mkdir(exist_ok=True)

# Move documentation to docs folder
docs_to_move = ['PREMIUM_THEME_GUIDE.md', 'test_all_buttons.md']
for doc in docs_to_move:
    src = ROOT / doc
    if src.exists():
        dst = docs_dir / doc
        try:
            shutil.move(str(src), str(dst))
            print(f"   ✓ Moved {doc} to docs/")
        except:
            pass

print()

print("4. Cleaning automated_tests output...")
output_dir = ROOT / 'automated_tests' / 'output'
if output_dir.exists():
    for file in output_dir.glob('*.po'):
        try:
            file.unlink()
            print(f"   ✓ Removed {file.name}")
        except:
            pass

reports_dir = ROOT / 'automated_tests' / 'reports'
if reports_dir.exists():
    for file in reports_dir.glob('*'):
        if file.is_file():
            try:
                file.unlink()
                print(f"   ✓ Removed {file.name}")
            except:
                pass

print()

print("5. Cleaning cache and logs...")
cache_files = list(ROOT.glob('*.log')) + list(ROOT.glob('*.cache'))
for file in cache_files:
    try:
        file.unlink()
        print(f"   ✓ Removed {file.name}")
    except:
        pass

print()

print("6. Cleaning __pycache__ directories...")
pycache_count = 0
for pycache in ROOT.rglob('__pycache__'):
    try:
        shutil.rmtree(pycache)
        pycache_count += 1
    except:
        pass
print(f"   ✓ Removed {pycache_count} __pycache__ directories")
print()

print("=" * 80)
print("PROJECT CLEANED FOR RELEASE")
print("=" * 80)
print()
print("Next steps:")
print("1. Review changes: git status")
print("2. Add files: git add .")
print("3. Commit: git commit -m '[REL] v1.0.0 - Production ready with Lingua-py and premium theme'")
print("4. Push: git push origin main")
print("5. Create release tag: git tag -a v1.0.0 -m 'Release v1.0.0'")
print("6. Push tag: git push origin v1.0.0")
print()

