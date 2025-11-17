"""Test module imports"""
import sys
sys.path.insert(0, 'src')

print("Testing imports...")

try:
    import polib
    print("✓ polib")
    
    import fasttext
    print("✓ fasttext")
    
    from po_translator.utils.language import detect_language_details
    print("✓ language detection")
    
    from po_translator.translator import Translator
    print("✓ translator")
    
    print("\n✅ ALL IMPORTS SUCCESSFUL")
    
except Exception as e:
    print(f"\n✗ Import failed: {e}")
    sys.exit(1)

