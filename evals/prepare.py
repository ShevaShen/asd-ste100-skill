#!/usr/bin/env python3
"""Export skill-only behavioral requests without revealing the grading rubric."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    skill = (ROOT / 'SKILL.md').read_bytes()
    cases_path = ROOT / 'evals' / 'cases.json'
    cases = json.loads(cases_path.read_text(encoding='utf-8'))['cases']
    requests = [
        {'case_id': case['id'], 'skill_sha256': hashlib.sha256(skill).hexdigest(),
         'cases_sha256': hashlib.sha256(cases_path.read_bytes()).hexdigest(),
         'instructions': skill.decode('utf-8'), 'prompt': case['prompt']}
        for case in cases
    ]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    # Refuse to overwrite a prior evaluation's requests accidentally.
    try:
        with args.out.open('x', encoding='utf-8') as stream:
            for request in requests:
                stream.write(json.dumps(request, ensure_ascii=False) + '\n')
    except FileExistsError:
        parser.exit(2, 'Output already exists; choose a new evaluation output path.\n')
    print(f'Prepared {len(requests)} requests without answer criteria: {args.out}')


if __name__ == '__main__':
    main()
