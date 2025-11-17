# Automated Test Suite for PO Translator

## Directory Structure

```
automated_tests/
├── input/          # Test PO files (input)
├── output/         # Translated PO files (output)
├── reports/        # Test reports and logs
└── run_tests.py    # Main test runner
```

## Test Files

### Input Files
- `test_fr_en.po` - French to English (15 entries)
- `test_mixed.po` - Mixed language entries
- `test_with_variables.po` - Entries with variables
- `fr_translated_20251029.po` - Pre-translated file

### Output Files
Generated after running tests:
- `test_fr_en_output.po` - Translated output
- `test_mixed_output.po` - Translated output
- `test_with_variables_output.po` - Translated output

### Reports
- `test_report_YYYYMMDD_HHMMSS.md` - Detailed test report
- `test_log_YYYYMMDD_HHMMSS.log` - Full execution log

## Running Tests

```bash
# Set API key
$env:GEMINI_API_KEY="your-api-key-here"

# Run all tests
python automated_tests/run_tests.py

# Run specific test
python automated_tests/run_tests.py --file test_fr_en.po

# Skip translation (test detection only)
python automated_tests/run_tests.py --no-translate
```

## What Gets Tested

### 1. Import & Dependencies
- All Python modules
- Lingua-py (language detection)
- FastText (fallback)
- CustomTkinter (GUI)
- Gemini API (translation)

### 2. File Loading
- PO file parsing
- Entry extraction
- Module indexing
- Metadata preservation

### 3. Language Detection
- Source language detection
- Translation language detection
- Dictionary verification (100% accuracy)
- Context-aware detection
- Confidence scoring

### 4. Translation
- API connectivity
- Translation quality
- Variable preservation
- Caching system
- Error handling

### 5. Export & Validation
- PO file export
- Entry count verification
- Translation verification
- Field completeness check
- Format validation

## Test Validation

Each test validates:
- ✅ All entries exported
- ✅ Translations filled in msgstr
- ✅ Variables preserved (%(var)s, %s, {var})
- ✅ Metadata correct
- ✅ No data loss
- ✅ File format valid

## Expected Results

### Success Criteria
- ✅ 100% language detection accuracy (with verification)
- ✅ 100% translation success rate
- ✅ 100% variable preservation
- ✅ 100% export success
- ✅ All fields validated

### Performance Targets
- File loading: < 1s for 1000 entries
- Language detection: < 0.1s per entry (cached)
- Translation: ~4s per entry (API limited)
- Export: < 1s for 1000 entries

## Interpreting Results

### PASS ✓
All validations passed, feature working correctly

### WARN ⚠
Feature working but with limitations (e.g., no API key)

### FAIL ✗
Critical error, feature not working

## Production Readiness

Tests must pass before production release:
- ✅ All imports working
- ✅ File I/O working
- ✅ Language detection accurate
- ✅ Translation working (if API key provided)
- ✅ Export validated

