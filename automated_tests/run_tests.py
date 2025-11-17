#!/usr/bin/env python3
"""
Comprehensive Automated Test Suite for PO Translator
Tests all functionality with multiple files and full validation
"""
import sys
import os
import time
import argparse
from datetime import datetime
from pathlib import Path

# Setup path
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR / 'translator_odoo' / 'src'))

# Setup UTF-8 encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Setup logging
import logging
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
log_file = ROOT_DIR / 'automated_tests' / 'reports' / f'test_log_{timestamp}.log'
log_file.parent.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)-5s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler(log_file, mode='w', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('test_runner')

class TestReport:
    """Generate comprehensive test report"""
    def __init__(self):
        self.tests = []
        self.start_time = time.time()
        self.errors = []
        self.warnings = []
        
    def add_test(self, name, status, details="", data=None):
        """Add test result"""
        self.tests.append({
            'name': name,
            'status': status,
            'details': details,
            'data': data or {},
            'timestamp': time.time() - self.start_time
        })
    
    def add_error(self, error):
        """Add error"""
        self.errors.append(error)
        
    def add_warning(self, warning):
        """Add warning"""
        self.warnings.append(warning)
    
    def generate_markdown(self):
        """Generate markdown report"""
        duration = time.time() - self.start_time
        passed = len([t for t in self.tests if t['status'] == 'PASS'])
        failed = len([t for t in self.tests if t['status'] == 'FAIL'])
        warned = len([t for t in self.tests if t['status'] == 'WARN'])
        
        report = []
        report.append("# PO Translator - Automated Test Report")
        report.append("")
        report.append(f"**Test Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Duration**: {duration:.2f} seconds")
        report.append(f"**Status**: {'✅ PASSED' if failed == 0 else '❌ FAILED'}")
        report.append("")
        report.append(f"## Summary")
        report.append("")
        report.append(f"- **Total Tests**: {len(self.tests)}")
        report.append(f"- **Passed**: {passed} ✓")
        report.append(f"- **Failed**: {failed} ✗")
        report.append(f"- **Warnings**: {warned} ⚠")
        report.append(f"- **Success Rate**: {passed/len(self.tests)*100:.1f}%")
        report.append("")
        
        report.append("## Test Results")
        report.append("")
        for i, test in enumerate(self.tests, 1):
            symbol = "✓" if test['status'] == 'PASS' else "✗" if test['status'] == 'FAIL' else "⚠"
            report.append(f"### {i}. {symbol} {test['name']} ({test['timestamp']:.2f}s)")
            report.append(f"**Status**: {test['status']}")
            if test['details']:
                report.append(f"**Details**: {test['details']}")
            if test['data']:
                report.append("**Data**:")
                for key, value in test['data'].items():
                    report.append(f"- {key}: {value}")
            report.append("")
        
        if self.warnings:
            report.append("## Warnings")
            report.append("")
            for warning in self.warnings:
                report.append(f"- ⚠ {warning}")
            report.append("")
        
        if self.errors:
            report.append("## Errors")
            report.append("")
            for error in self.errors:
                report.append(f"- ✗ {error}")
            report.append("")
        
        report.append("## Conclusion")
        report.append("")
        if failed == 0:
            report.append("✅ **ALL TESTS PASSED** - Application is production ready!")
        else:
            report.append(f"❌ **{failed} TESTS FAILED** - Please fix errors before production")
        
        return "\n".join(report)

def test_file(filepath, api_key=None, translate=True, translate_all=False):
    """Test a single PO file"""
    logger.info("="*80)
    logger.info(f"Testing file: {filepath}")
    logger.info("="*80)
    
    report = TestReport()
    filename = os.path.basename(filepath)
    output_file = ROOT_DIR / 'automated_tests' / 'output' / filename.replace('.po', '_output.po')
    
    try:
        from po_translator.core import POMerger
        from po_translator.translator import Translator
        from po_translator.utils.language import detect_language_details
        import polib
        
        # Load file
        logger.info(f"Loading {filename}...")
        merger = POMerger()
        start = time.time()
        merged = merger.merge_files([filepath])
        entries = list(merged.values())
        load_time = time.time() - start
        
        report.add_test(
            f"Load {filename}",
            "PASS",
            f"Loaded {len(entries)} entries in {load_time:.2f}s",
            {'entries': len(entries), 'load_time': f'{load_time:.2f}s'}
        )
        
        # Analyze entries
        translated_count = sum(1 for e in entries if e.msgstr and e.msgstr.strip() and e.msgid != e.msgstr)
        untranslated_count = len(entries) - translated_count
        
        report.add_test(
            "Analyze entries",
            "PASS",
            f"Translated: {translated_count}, Untranslated: {untranslated_count}",
            {
                'total': len(entries),
                'translated': translated_count,
                'untranslated': untranslated_count,
                'translation_rate': f'{translated_count/len(entries)*100:.1f}%'
            }
        )
        
        # Test language detection
        logger.info("Testing language detection...")
        detection_stats = {'correct': 0, 'wrong': 0, 'unknown': 0, 'dictionary_matches': 0}
        
        for entry in entries[:min(10, len(entries))]:
            lang, conf = detect_language_details(entry.msgid, expected_language='fr')
            
            if conf == 1.0:
                detection_stats['dictionary_matches'] += 1
            
            if lang == 'fr':
                detection_stats['correct'] += 1
            elif lang:
                detection_stats['wrong'] += 1
            else:
                detection_stats['unknown'] += 1
        
        sample_size = min(10, len(entries))
        accuracy = detection_stats['correct'] / sample_size * 100
        
        report.add_test(
            "Language detection",
            "PASS" if accuracy >= 80 else "WARN",
            f"Accuracy: {accuracy:.1f}% ({detection_stats['correct']}/{sample_size})",
            detection_stats
        )
        
        # Translation test
        if translate and api_key:
            logger.info("Testing translation...")
            translator = Translator()
            translator.set_api_key(api_key)
            translator.configure_languages(source='fr', target='en', auto_detect=True)
            
            untranslated = [e for e in entries if not e.msgstr or not e.msgstr.strip() or e.msgid == e.msgstr]
            # Translate all or just sample
            test_count = len(untranslated) if translate_all else min(5, len(untranslated))
            
            translation_stats = {'successful': 0, 'failed': 0, 'variables_preserved': 0}
            
            for entry in untranslated[:test_count]:
                module = merger.indexer.get_module(entry.msgid)
                success = translator.auto_translate_entry(entry, module, force=False)
                
                if success:
                    translation_stats['successful'] += 1
                    
                    # Check variable preservation
                    import re
                    src_vars = set(re.findall(r'%\([^)]+\)s|%s|\{[^}]+\}|\$\{[^}]+\}', entry.msgid))
                    trans_vars = set(re.findall(r'%\([^)]+\)s|%s|\{[^}]+\}|\$\{[^}]+\}', entry.msgstr))
                    
                    if src_vars == trans_vars:
                        translation_stats['variables_preserved'] += 1
                else:
                    translation_stats['failed'] += 1
            
            stats = translator.get_stats()
            translation_stats.update({
                'api_calls': stats['api_calls'],
                'cache_hits': stats['cache_hits'],
                'cache_hit_rate': stats['cache_hit_rate']
            })
            
            report.add_test(
                "Translation",
                "PASS" if translation_stats['successful'] == test_count else "FAIL",
                f"Translated {translation_stats['successful']}/{test_count} entries",
                translation_stats
            )
        elif translate and not api_key:
            report.add_test("Translation", "WARN", "No API key provided")
            report.add_warning("Set GEMINI_API_KEY to test translation")
        
        # Export and validate
        logger.info(f"Exporting to {output_file}...")
        merger.export_to_file(str(output_file))
        
        if output_file.exists():
            file_size = output_file.stat().st_size
            
            # Verify export
            exported_po = polib.pofile(str(output_file))
            
            # Validate all fields
            validation_stats = {
                'total_entries': len(exported_po),
                'entries_match': len(exported_po) == len(entries),
                'has_metadata': bool(exported_po.metadata),
                'has_translations': sum(1 for e in exported_po if e.msgstr and e.msgstr.strip()),
                'has_comments': sum(1 for e in exported_po if e.comment),
                'has_occurrences': sum(1 for e in exported_po if hasattr(e, 'occurrences') and e.occurrences),
            }
            
            # Check each field
            field_checks = []
            for entry in exported_po:
                if entry.msgid:
                    field_checks.append({
                        'msgid': bool(entry.msgid),
                        'msgstr': bool(entry.msgstr and entry.msgstr.strip()),
                        'comment': bool(entry.comment),
                    })
            
            validation_stats['fields_complete'] = sum(1 for f in field_checks if f['msgid'] and f['msgstr'])
            validation_stats['fields_total'] = len(field_checks)
            validation_stats['completeness'] = f"{validation_stats['fields_complete']/validation_stats['fields_total']*100:.1f}%"
            
            report.add_test(
                "Export file",
                "PASS",
                f"Exported {len(exported_po)} entries ({file_size} bytes)",
                validation_stats
            )
            
            # Detailed validation
            all_valid = (
                validation_stats['entries_match'] and
                validation_stats['has_metadata'] and
                len(exported_po) > 0
            )
            
            report.add_test(
                "Validate export",
                "PASS" if all_valid else "FAIL",
                f"Validation {'passed' if all_valid else 'failed'}",
                validation_stats
            )
        else:
            report.add_test("Export file", "FAIL", "Output file not created")
            report.add_error(f"Export failed: {output_file}")
        
        return report
        
    except Exception as e:
        logger.error(f"Test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        report.add_test(f"Test {filename}", "FAIL", str(e))
        report.add_error(str(e))
        return report

def run_all_tests(api_key=None, translate=True, translate_all=False):
    """Run tests on all input files"""
    print("\n" + "="*80)
    print("PO TRANSLATOR - COMPREHENSIVE AUTOMATED TEST SUITE")
    print("="*80)
    print()
    
    input_dir = ROOT_DIR / 'automated_tests' / 'input'
    po_files = list(input_dir.glob('*.po'))
    
    if not po_files:
        logger.error(f"No .po files found in {input_dir}")
        logger.info("Please add test files to automated_tests/input/")
        return
    
    logger.info(f"Found {len(po_files)} test files")
    logger.info(f"API Key: {'Provided' if api_key else 'Not provided'}")
    logger.info(f"Translation: {'Enabled' if translate else 'Disabled'}")
    print()
    
    all_reports = []
    
    for i, po_file in enumerate(po_files, 1):
        logger.info(f"\n[{i}/{len(po_files)}] Testing {po_file.name}...")
        report = test_file(str(po_file), api_key, translate, translate_all)
        all_reports.append((po_file.name, report))
        print()
    
    # Generate combined report
    logger.info("="*80)
    logger.info("GENERATING FINAL REPORT")
    logger.info("="*80)
    
    report_file = ROOT_DIR / 'automated_tests' / 'reports' / f'test_report_{timestamp}.md'
    
    combined_report = []
    combined_report.append("# PO Translator - Comprehensive Test Report")
    combined_report.append("")
    combined_report.append(f"**Test Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    combined_report.append(f"**Files Tested**: {len(po_files)}")
    combined_report.append(f"**Total Duration**: {time.time() - all_reports[0][1].start_time:.2f} seconds")
    combined_report.append("")
    
    # Summary table
    combined_report.append("## Test Summary")
    combined_report.append("")
    combined_report.append("| File | Tests | Passed | Failed | Warnings | Status |")
    combined_report.append("|------|-------|--------|--------|----------|--------|")
    
    total_passed = 0
    total_failed = 0
    total_warned = 0
    
    for filename, report in all_reports:
        passed = len([t for t in report.tests if t['status'] == 'PASS'])
        failed = len([t for t in report.tests if t['status'] == 'FAIL'])
        warned = len([t for t in report.tests if t['status'] == 'WARN'])
        status = "✅ PASS" if failed == 0 else "❌ FAIL"
        
        total_passed += passed
        total_failed += failed
        total_warned += warned
        
        combined_report.append(f"| {filename} | {len(report.tests)} | {passed} | {failed} | {warned} | {status} |")
    
    combined_report.append(f"| **TOTAL** | **{total_passed + total_failed + total_warned}** | **{total_passed}** | **{total_failed}** | **{total_warned}** | **{'✅' if total_failed == 0 else '❌'}** |")
    combined_report.append("")
    
    # Detailed results for each file
    combined_report.append("## Detailed Results")
    combined_report.append("")
    
    for filename, report in all_reports:
        combined_report.append(f"### {filename}")
        combined_report.append("")
        combined_report.append(report.generate_markdown())
        combined_report.append("")
        combined_report.append("---")
        combined_report.append("")
    
    # Overall conclusion
    combined_report.append("## Overall Conclusion")
    combined_report.append("")
    
    if total_failed == 0:
        combined_report.append("### ✅ ALL TESTS PASSED")
        combined_report.append("")
        combined_report.append(f"- {total_passed} tests passed successfully")
        combined_report.append(f"- {total_warned} warnings (non-critical)")
        combined_report.append("- 0 failures")
        combined_report.append("")
        combined_report.append("**The application is PRODUCTION READY!** 🚀")
    else:
        combined_report.append("### ❌ TESTS FAILED")
        combined_report.append("")
        combined_report.append(f"- {total_passed} tests passed")
        combined_report.append(f"- {total_failed} tests failed")
        combined_report.append(f"- {total_warned} warnings")
        combined_report.append("")
        combined_report.append("**Please fix errors before production release.**")
    
    # Save report
    report_file.write_text("\n".join(combined_report), encoding='utf-8')
    logger.info(f"\nReport saved to: {report_file}")
    logger.info(f"Log saved to: {log_file}")
    
    # Print summary
    print("\n" + "="*80)
    print("FINAL SUMMARY")
    print("="*80)
    print(f"Files tested: {len(po_files)}")
    print(f"Total tests: {total_passed + total_failed + total_warned}")
    print(f"Passed: {total_passed} ✓")
    print(f"Failed: {total_failed} ✗")
    print(f"Warnings: {total_warned} ⚠")
    print()
    
    if total_failed == 0:
        print("✅ ALL TESTS PASSED - PRODUCTION READY!")
    else:
        print(f"❌ {total_failed} TESTS FAILED - FIX REQUIRED")
    
    print(f"\nDetailed report: {report_file}")
    print("="*80)

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Run automated tests for PO Translator')
    parser.add_argument('--file', help='Test specific file only')
    parser.add_argument('--no-translate', action='store_true', help='Skip translation tests')
    parser.add_argument('--translate-all', action='store_true', help='Translate ALL entries (not just 5 samples)')
    parser.add_argument('--api-key', help='Gemini API key (or use GEMINI_API_KEY env var)')
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.environ.get('GEMINI_API_KEY')
    
    if args.file:
        # Test single file
        filepath = ROOT_DIR / 'automated_tests' / 'input' / args.file
        if not filepath.exists():
            logger.error(f"File not found: {filepath}")
            return 1
        
        report = test_file(str(filepath), api_key, not args.no_translate, args.translate_all)
        
        # Save report
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = ROOT_DIR / 'automated_tests' / 'reports' / f'test_report_{args.file}_{timestamp}.md'
        report_file.write_text(report.generate_markdown(), encoding='utf-8')
        
        return 0 if not report.errors else 1
    else:
        # Test all files
        run_all_tests(api_key, not args.no_translate, args.translate_all)
        return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        logger.info("\n\nTests interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"\n\nUnexpected error: {e}")
        import traceback
        logger.error(traceback.format_exc())
        sys.exit(1)

