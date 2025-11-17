"""Test PO file loading and language detection"""
import sys
sys.path.insert(0, 'src')

import polib
from po_translator.utils.language import detect_language_details

print("Loading test PO file...")
po = polib.pofile('test_files/test_fr_en.po')
print(f"✓ Loaded {len(po)} entries\n")

print("Testing language detection:")
correct = 0
total = 0

for entry in po[:10]:
    if entry.msgid and entry.msgid.strip():
        lang, conf = detect_language_details(entry.msgid)
        total += 1
        if lang == 'fr':
            correct += 1
        
        text = entry.msgid[:40].ljust(40)
        print(f'  "{text}" → {lang} ({conf:.2f})')

accuracy = (correct / total * 100) if total > 0 else 0
print(f'\n✅ Detection: {correct}/{total} ({accuracy:.1f}% French)')

