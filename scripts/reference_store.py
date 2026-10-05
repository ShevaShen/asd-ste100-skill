"""PDF-free, integrity-checked access to private reference data."""
import hashlib
import json
from pathlib import Path

DEFAULT_DATA = Path(__file__).resolve().parents[1] / 'references' / 'generated'
FILES = {'index.json', 'pages.jsonl', 'rules.jsonl', 'dictionary.jsonl'}


class ReferenceError(ValueError):
    pass


class Store:
    def __init__(self, directory=DEFAULT_DATA):
        self.directory = Path(directory)
        try:
            self.manifest = json.loads((self.directory / 'manifest.json').read_text(encoding='utf-8'))
            if self.manifest['schema_version'] != 1 or self.manifest['issue'] != 9:
                raise ReferenceError('Unsupported reference schema or edition')
            if set(self.manifest['files']) != FILES:
                raise ReferenceError('Incomplete reference set')
            for name, expected in self.manifest['files'].items():
                actual = hashlib.sha256((self.directory / name).read_bytes()).hexdigest()
                if actual != expected:
                    raise ReferenceError(f'Integrity check failed for {name}; rebuild references')
        except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
            raise ReferenceError('Reference data is missing or invalid; run scripts/build_reference.py separately') from exc

    def rows(self, dataset):
        if dataset not in FILES:
            raise ReferenceError('Unknown dataset')
        with (self.directory / dataset).open(encoding='utf-8') as stream:
            for line in stream:
                yield json.loads(line)

    def index(self):
        return json.loads((self.directory / 'index.json').read_text(encoding='utf-8'))

    def rule(self, rule_id):
        return next((r for r in self.rows('rules.jsonl') if r['rule_id'] == rule_id), None)

    def word(self, word, pos=None):
        key = word.casefold()
        return [r for r in self.rows('dictionary.jsonl')
                if (r['lookup_key'] == key or key in [f.casefold() for f in r['listed_forms'] + r.get('aliases', [])])
                and (pos is None or r['pos'] == pos)]

    def evidence(self, rule_id):
        rule = self.rule(rule_id)
        if rule is None:
            raise ReferenceError(f'Missing rule {rule_id}')
        return {'rule_id': rule_id, 'source_sha256': self.manifest['source_sha256'],
                'pages': [{'pdf_page': f['pdf_page'], 'printed_page': f['printed_page']}
                          for f in rule['fragments']]}
