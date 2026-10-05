#!/usr/bin/env python3
"""Query generated references without opening or requiring the source PDF."""
import argparse
import json
from reference_store import Store, ReferenceError


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('index')
    rule = commands.add_parser('rule')
    rule.add_argument('id')
    section = commands.add_parser('section')
    section.add_argument('number', type=int, choices=range(1, 10))
    word = commands.add_parser('word')
    word.add_argument('word')
    word.add_argument('--pos', choices=['n', 'v', 'adj', 'adv', 'pron', 'art', 'prep', 'conj'])
    page = commands.add_parser('page')
    page.add_argument('number', type=int)
    search = commands.add_parser('search')
    search.add_argument('query')
    search.add_argument('--limit', type=int, default=10)
    args = parser.parse_args()
    try:
        store = Store()
        if args.command == 'index':
            result = store.index()
        elif args.command == 'rule':
            result = store.rule(args.id)
        elif args.command == 'word':
            result = store.word(args.word, args.pos)
        elif args.command == 'section':
            result = [r for r in store.rows('rules.jsonl') if r['section'] == args.number]
        elif args.command == 'page':
            result = next((r for r in store.rows('pages.jsonl') if r['pdf_page'] == args.number), None)
        else:
            if not args.query.strip() or not 1 <= args.limit <= 100:
                raise ReferenceError('Search requires nonempty text and a limit from 1 to 100')
            result = []
            for dataset in ['rules.jsonl', 'dictionary.jsonl']:
                for r in store.rows(dataset):
                    if args.query.casefold() in json.dumps(r, ensure_ascii=False).casefold():
                        result.append({'dataset': dataset, 'id': r.get('rule_id', r.get('entry_id')),
                                       'pages': sorted({f['pdf_page'] for f in r['fragments']})})
                    if len(result) == args.limit:
                        break
                if len(result) == args.limit:
                    break
    except ReferenceError as exc:
        parser.exit(2, f'{exc}\n')
    print(json.dumps({'issue': 9, 'reference_warnings': store.manifest['quality']['warnings'],
                      'result': result}, ensure_ascii=False, indent=2))
    return 0 if result else 1


if __name__ == '__main__':
    raise SystemExit(main())
