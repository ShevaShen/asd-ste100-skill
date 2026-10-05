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

    def test_vertical_list_intro_and_items_count_separately(self):
        text = ('Before you start, inspect these parts:\n'
                '- Inspect the blue cable near the rear cover\n'
                '- Inspect the green connector below the display\n'
                '- Inspect the narrow seal around the front panel')
        self.assertEqual(len(list(sentence_spans(text))), 4)
        self.assertEqual(self.scan(text)['findings'], [])

    def test_list_marker_styles_and_numbering_do_not_add_words(self):
        for marker in ['- ', '* ', '+ ', '• ', '1. ', '2) ', '(3) ', 'a. ', 'B) ', '(c) ']:
            with self.subTest(marker=marker):
                text = 'Inspect these parts:\n' + marker + ' '.join(['item'] * 20)
                self.assertEqual(len(list(sentence_spans(text))), 2)
                self.assertEqual(self.scan(text)['findings'], [])

    def test_long_item_remains_a_finding_with_original_offsets(self):
        text = 'Inspect:\n- ' + ' '.join(['item'] * 21) + '\n- Check the cover.'
        findings = self.scan(text)['findings']
        self.assertEqual(len(findings), 1)
        f = findings[0]
        self.assertEqual((f['line'], f['column'], f['estimated_words']), (2, 1, 21))
        self.assertEqual(f['excerpt'], text[f['start']:f['end']])
        self.assertEqual(f['excerpt'], '- ' + ' '.join(['item'] * 21))

    def test_long_intro_is_not_hidden_by_a_list(self):
        text = ' '.join(['item'] * 21) + ':\n- Check the cover.'
        f = self.scan(text)['findings'][0]
        self.assertEqual(f['estimated_words'], 21)
        self.assertTrue(f['excerpt'].endswith(':'))

    def test_wrapped_item_stays_together(self):
        text = 'Inspect:\n- ' + ' '.join(['item'] * 12) + '\n  ' + ' '.join(['item'] * 9) + '\n- Close it.'
        self.assertEqual(len(list(sentence_spans(text))), 3)
        findings = self.scan(text)['findings']
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]['estimated_words'], 21)

    def test_inline_colon_and_wrapped_prose_are_not_list_boundaries(self):
        text = 'The setting is this: ' + ' '.join(['item'] * 10) + '\n' + ' '.join(['item'] * 11)
        self.assertEqual(len(list(sentence_spans(text))), 1)
        self.assertEqual(len(self.scan(text)['findings']), 1)

    def test_nested_lists_blank_lines_and_crlf(self):
        text = 'Inspect:\r\n\r\n1. Check the cover\r\n   a) Check No. 3 at 2.5 mm\r\n   b) Check the seal\r\n2. Close the cover'
        self.assertEqual(len(list(sentence_spans(text))), 5)
        self.assertEqual(self.scan(text)['findings'], [])

    def test_quote_and_parenthetical_punctuation_are_protected(self):
        text = 'Read “Menu: 1. Open (” (the label has a colon: keep it).\n- Check the seal.'
        self.assertEqual(len(list(sentence_spans(text))), 2)
        text = 'Read the note (one option:\n- item\n- item) before work.'
        self.assertEqual(len(list(sentence_spans(text))), 1)

    def test_quote_after_inline_colon_is_not_erased_for_list_detection(self):
        text = 'The message is: “wait”\n- Check the seal.'
        spans = [text[a:b] for a, b in sentence_spans(text)]
        self.assertEqual(spans, ['The message is: “wait”', '- Check the seal.'])

    def test_many_short_list_items_do_not_form_one_large_paragraph(self):
        text = 'The system has these parts:\n' + '\n'.join('- A small unit.' for _ in range(8))
        self.assertEqual(self.scan(text, 'descriptive')['findings'], [])

    def test_long_paragraph_inside_one_list_item_is_still_reported(self):
        text = 'Description:\n- ' + 'It is ready. ' * 7 + '\n- It is green.'
        findings = self.scan(text, 'descriptive')['findings']
        self.assertEqual([f['rule_id'] for f in findings], ['6.6'])
        self.assertEqual(findings[0]['line'], 2)


if __name__ == '__main__':
    unittest.main()
