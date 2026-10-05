"""Opt-in corpus checks; no source text is stored as fixtures."""
import os
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from reference_store import Store


@unittest.skipUnless(os.environ.get('STE_INTEGRATION') == '1', 'set STE_INTEGRATION=1 after building')
class IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.store = Store()

    def test_complete_rule_coverage_and_provenance(self):
        rules = list(self.store.rows('rules.jsonl'))
        self.assertEqual(len(rules), 53)
        for r in rules:
            self.assertTrue(r['statement'])
            self.assertTrue(r['fragments'])
            for f in r['fragments']:
                self.assertTrue(f['printed_page'].startswith(f"1-{r['section']}-"))
                self.assertTrue(45 <= f['pdf_page'] <= 128)
                self.assertLess(f['bbox'][1], f['bbox'][3])

    def test_context_indexes(self):
        index = self.store.index()
        self.assertEqual({r['id'] for r in index['general_recommendations']},
                         {f'GR-{n}' for n in range(1, 9)})
        self.assertIn(131, index['dictionary_introduction_pdf_pages'])

    def test_dictionary_coverage(self):
        entries = list(self.store.rows('dictionary.jsonl'))
        self.assertEqual(sum(e['approved'] for e in entries), self.store.manifest['counts']['approved'])
        self.assertEqual(sum(not e['approved'] for e in entries), self.store.manifest['counts']['nonapproved'])
        if len(entries) != 2149:
            self.assertTrue(self.store.manifest['quality']['warnings'])
        self.assertEqual(len({e['entry_id'] for e in entries}), len(entries))
        for e in entries:
            self.assertTrue(e['columns']['word_and_forms'])
            self.assertTrue(e['columns']['meaning_or_alternatives'])
            for f in e['fragments']:
                self.assertTrue(f['printed_page'].startswith('2-1-'))

    def test_approval_meaning_and_forms_are_distinct(self):
        entries = self.store.word('get', 'v')
        self.assertEqual({e['approved'] for e in entries}, {True, False})
        self.assertTrue(self.store.word('interchangeable', 'adj'))
        self.assertTrue(self.store.word('downstream of', 'prep'))
        self.assertTrue(self.store.word('precautionary', 'adj'))
        self.assertTrue(self.store.word('adapted', 'v'))
        self.assertTrue(self.store.word('better', 'adj'))
        self.assertTrue(self.store.word('were', 'v'))
        self.assertTrue(self.store.word('matte', 'adj'))

    def test_runtime_without_pdf_dependency(self):
        proc = subprocess.run([sys.executable, '-S', str(ROOT / 'scripts/lookup.py'), 'rule', '8.1'],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn('printed_page', proc.stdout)


if __name__ == '__main__':
    unittest.main()
