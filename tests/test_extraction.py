"""Synthetic layout tests; they do not need pdfplumber or copyrighted fixtures."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_reference import parse_headword_lines, check_quality


class ExtractionTests(unittest.TestCase):
    def lines(self, *texts):
        return [{'text': text, 'top': 100 + i * 12} for i, text in enumerate(texts)]

    def test_wrapped_headword_is_one_entry(self):
        result = parse_headword_lines(self.lines('SAMPLE-', 'WORD (adj)'))
        self.assertEqual([(r['headword'], r['pos']) for r in result], [('SAMPLEWORD', 'adj')])
        self.assertEqual(result[0]['top'], 99)

    def test_wrapped_phrase_and_pos(self):
        result = parse_headword_lines(self.lines('SAMPLE', 'OF (prep)', 'test', '(adj)'))
        self.assertEqual([(r['headword'], r['pos']) for r in result], [('SAMPLE OF', 'prep'), ('test', 'adj')])

    def test_forms_are_not_headwords(self):
        lines = self.lines('SAMPLE (v),', 'SAMPLES,', 'SAMPLED,', 'SAMPLED')
        lines += [{'text': 'other (adj)', 'top': 180}]
        result = parse_headword_lines(lines)
        self.assertEqual([r['headword'] for r in result], ['SAMPLE', 'other'])

    def test_case_and_parenthetical_variant_preserved(self):
        result = parse_headword_lines(self.lines('SAMPLE (or VARIANT)', '(adj)', 'sample (adj)'))
        self.assertEqual([r['headword'] for r in result], ['SAMPLE (or VARIANT)', 'sample'])

    def test_incomplete_extraction_fails_quality(self):
        failures = check_quality([], [], [], ['Orphan continuation'])
        self.assertIn('Orphan continuation', failures)
        self.assertTrue(any('coverage' in failure for failure in failures))
        self.assertTrue(any('profile' in failure for failure in failures))


if __name__ == '__main__':
    unittest.main()
