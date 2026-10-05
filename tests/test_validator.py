"""Synthetic fixtures only; no copied source examples."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_ste import validate, word_count, sentence_spans


class Evidence:
    def evidence(self, rule_id):
        return {'rule_id': rule_id, 'pages': []}


class ValidatorTests(unittest.TestCase):
    def scan(self, text, kind='procedural', terms=()):
        return validate(text, kind, Evidence(), terms)

    def test_punctuation_locations_and_input_preservation(self):
        text = 'Open the case.\nCheck it; close it.'
        report = self.scan(text)
        f = report['findings'][0]
        self.assertEqual((f['rule_id'], f['line'], f['column']), ('8.1', 2, 9))
        self.assertEqual(text[f['start']:f['end']], ';')
        self.assertFalse(report['full_compliance_assessed'])

    def test_quotes_and_apostrophes(self):
        text = 'Don’t erase the user’s label. Keep “don’t; erase” and \'we’re; ready\'.'
        findings = self.scan(text)['findings']
        self.assertEqual([(f['rule_id'], f['excerpt']) for f in findings], [('4.2', 'Don’t')])

    def test_no_global_pass(self):
        report = self.scan('Check the case.')
        self.assertEqual(report['status'], 'no_deterministic_findings')
        self.assertFalse(report['full_compliance_assessed'])
        self.assertIn('vocabulary and meaning', report['coverage']['unassessed'])

    def test_count_elements(self):
        self.assertEqual(word_count('Move the light-blue case (item 7) by 4 mm.'), 7)
        self.assertEqual(word_count('Select “Open case now” on the panel.'), 5)
        self.assertEqual(word_count('Consult Case Setup Guide before use.', ['Case Setup Guide']), 4)
        self.assertEqual(word_count('The value is 12 degrees Celsius.'), 4)

    def test_length_boundaries_and_kind(self):
        for kind, threshold in [('procedural', 20), ('safety', 20), ('descriptive', 25)]:
            self.assertFalse(self.scan(' '.join(['item'] * threshold) + '.', kind)['findings'])
            f = self.scan(' '.join(['item'] * (threshold + 1)) + '.', kind)['findings'][0]
            self.assertEqual(f['level'], 'review')
            self.assertEqual(f['limit'], threshold)

    def test_parenthetical_length_checked_separately(self):
        report = self.scan('Read this (' + ' '.join(['item'] * 21) + ').')
        self.assertEqual(len(report['findings']), 1)
        self.assertIn('parenthetical', report['findings'][0]['message'])

    def test_decimal_and_abbreviation(self):
        text = 'Set the value to 3.5 mm. Inspect No. 3 now.'
        self.assertEqual(len(list(sentence_spans(text))), 2)

    def test_paragraph_boundaries(self):
        report = self.scan('It is ready. ' * 7, 'descriptive')
        self.assertEqual([f['rule_id'] for f in report['findings']], ['6.6'])
        report = self.scan('It is ready. ' * 4 + '\n\n' + 'It is ready. ' * 4, 'descriptive')
        self.assertEqual(report['findings'], [])


if __name__ == '__main__':
    unittest.main()
