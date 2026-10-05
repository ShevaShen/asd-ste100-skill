import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from reference_store import Store, ReferenceError, FILES


class StoreTests(unittest.TestCase):
    def fixture(self, root):
        entry = {'entry_id': 'invented:v', 'lookup_key': 'invented', 'pos': 'v', 'listed_forms': ['INVENTEDS']}
        for name in FILES:
            value = json.dumps(entry) + '\n' if name == 'dictionary.jsonl' else '{}\n'
            (root / name).write_text(value)
        manifest = {'schema_version': 1, 'issue': 9, 'source_sha256': 'synthetic',
                    'files': {n: hashlib.sha256((root / n).read_bytes()).hexdigest() for n in FILES}}
        (root / 'manifest.json').write_text(json.dumps(manifest))

    def test_missing_data_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ReferenceError):
                Store(d)

    def test_modified_data_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root)
            (root / 'dictionary.jsonl').write_text('changed')
            with self.assertRaises(ReferenceError):
                Store(root)

    def test_exact_and_form_lookup_without_pdf(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root)
            store = Store(root)
            self.assertEqual(len(store.word('INVENTED')), 1)
            self.assertEqual(len(store.word('inventeds', 'v')), 1)
            self.assertEqual(store.word('invented', 'n'), [])
            self.assertEqual(store.word('invent'), [])


if __name__ == '__main__':
    unittest.main()
