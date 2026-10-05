#!/usr/bin/env python3
"""Conservative deterministic findings and review candidates; never a certification."""
import argparse
import json
from pathlib import Path
import re
from reference_store import Store, ReferenceError

QUOTES = re.compile(r'"[^"\n]*"|“[^”\n]*”|‘[^’\n]*’|(?<!\w)\x27[^\x27\n]+\x27(?!\w)')
CONTRACTIONS = re.compile(
    r"\b(?:can't|won't|shan't|don't|doesn't|didn't|isn't|aren't|wasn't|weren't|"
    r"haven't|hasn't|hadn't|couldn't|wouldn't|shouldn't|mustn't|needn't|mightn't|"
    r"i'm|you're|we're|they're|i've|you've|we've|they've|i'll|you'll|he'll|she'll|we'll|they'll)\b",
    re.IGNORECASE)
TOKEN = re.compile(r"\w+(?:[-’'./]\w+)*", re.UNICODE)


def mask_quotes(text):
    # Preserve length and line positions for deterministic finding offsets.
    return QUOTES.sub(lambda m: ' ' * len(m[0]), text)


def word_count(text, count_as_one=()):
    """A count estimate: unsupported semantic elements need a human review."""
    for term in sorted(count_as_one, key=len, reverse=True):
        if term.strip():
            text = re.sub(r'(?<!\w)' + re.escape(term) + r'(?!\w)', ' ELEMENT ', text)
    text = QUOTES.sub(' QUOTED ', text)
    # Innermost first supports nested parentheses for the outer sentence count.
    while re.search(r'\([^()]*\)', text):
        text = re.sub(r'\([^()]*\)', ' PAREN ', text)
    # Recognize common units only; this list is an implementation aid, not an STE lexicon.
    units = r'(?:degrees?\s+(?:Celsius|Fahrenheit)|°\s*[CF]|kg|kilograms?|g|mm|cm|km|mA|m|kPa|Pa|psi|ohms?|Ω|volts?|V|liters?|L|knots?|a\.m\.|p\.m\.)'
    text = re.sub(r'\b\d+(?:[.,]\d+)*\s*' + units + r'(?!\w)', ' MEASURE ', text, flags=re.I)
    text = re.sub(r'\bNo\.\s*\d+[\w-]*', ' IDENTIFIER ', text)
    return len(TOKEN.findall(text))


def sentence_spans(text):
    """Candidate boundaries, with quotes, decimals and common abbreviations protected."""
    masked = list(mask_quotes(text))
    for m in re.finditer(r'\b(?:a\.m\.|p\.m\.|e\.g\.|i\.e\.|No\.|Mr\.|Dr\.)|(?<=\d)\.(?=\d)', text, re.I):
        for i in range(m.start(), m.end()):
            if masked[i] == '.':
                masked[i] = 'x'
    depth = 0
    for i, c in enumerate(text):
        if c == '(':
            depth += 1
        if depth and masked[i] in '.!?':
            masked[i] = 'x'
        if c == ')':
            depth = max(0, depth - 1)
    split_text = ''.join(masked)
    start = 0
    for m in re.finditer(r'[.!?](?=\s|$)|\n\s*\n', split_text):
        end = m.end()
        if text[start:end].strip():
            yield start, end
        start = end
    if text[start:].strip():
        yield start, len(text)


def validate(text, kind, store, count_as_one=()):
    if kind not in {'procedural', 'descriptive', 'safety'}:
        raise ValueError('Unknown passage type')
    findings = []
    unquoted = mask_quotes(text).replace('’', "'")

    def add(rule, start, end, message, level, **extra):
        findings.append({'rule_id': rule, 'level': level, 'start': start, 'end': end,
                         'line': text.count('\n', 0, start) + 1,
                         'column': start - text.rfind('\n', 0, start),
                         'excerpt': text[start:end], 'message': message,
                         'evidence': store.evidence(rule), **extra})

    for match in re.finditer(';', unquoted):
        add('8.1', match.start(), match.end(), 'Semicolon in unquoted text.', 'finding')
    for match in CONTRACTIONS.finditer(unquoted):
        add('4.2', match.start(), match.end(), 'Contraction in unquoted text.', 'finding')
    limit, rule = (25, '6.3') if kind == 'descriptive' else (20, '5.1')
    spans = list(sentence_spans(text))
    for start, end in spans:
        sentence = text[start:end]
        # Work-step numbers are not words; other number contexts remain intact.
        sentence = re.sub(r'^\s*(?:\d+[.)]|\(\d+\))\s+', '', sentence)
        count = word_count(sentence, count_as_one)
        if count > limit:
            add(rule, start, end, 'Estimated sentence length exceeds the limit; verify boundaries and special count elements.',
                'review', estimated_words=count, limit=limit,
                counting_evidence=[store.evidence(r) for r in ['8.4', '8.5', '8.6', '8.7']])
    # Parenthetical sentences are also counted independently (8.5).
    for parenthetical in re.finditer(r'\([^()]+\)', text):
        for a, b in sentence_spans(parenthetical[0][1:-1]):
            count = word_count(parenthetical[0][1:-1][a:b], count_as_one)
            if count > limit:
                add(rule, parenthetical.start() + 1 + a, parenthetical.start() + 1 + b,
                    'Estimated parenthetical sentence length exceeds the limit.', 'review',
                    estimated_words=count, limit=limit, counting_evidence=[store.evidence('8.5')])
    if kind == 'descriptive':
        for paragraph in re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)', text):
            count = len(list(sentence_spans(paragraph[0])))
            if count > 6:
                add('6.6', paragraph.start(), paragraph.end(),
                    'Estimated paragraph size exceeds six sentences; verify segmentation.',
                    'review', estimated_sentences=count)
    return {'operation': 'VALIDATE', 'issue': 9, 'type': kind,
            'status': 'findings' if any(f['level'] == 'finding' for f in findings) else 'no_deterministic_findings',
            'full_compliance_assessed': False, 'findings': findings,
            'coverage': {'deterministic': ['8.1: unquoted semicolons', '4.2: selected unambiguous contractions'],
                         'review_candidates': [f'{rule}: estimated length', '8.5: parenthetical length'] +
                         (['6.6: estimated paragraph size'] if kind == 'descriptive' else []),
                         'unassessed': ['vocabulary and meaning', 'parts of speech and inflections',
                                        'technical-term eligibility', 'voice and grammar',
                                        'instruction structure and safety meaning',
                                        'all other rules and recommendations']},
            'limitations': ['Quotes are only syntax-detected; confirm that they are protected source text.',
                            'Counts are estimates: lists, titles, names, labels, number expressions and abbreviations need review.',
                            'Plain text input only; markup and code need a separate contextual review.'],
            'count_as_one': list(count_as_one)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--type', required=True, choices=['procedural', 'descriptive', 'safety'])
    parser.add_argument('--count-as-one', action='append', default=[])
    args = parser.parse_args()
    try:
        store = Store()
        result = validate(args.input.read_text(encoding='utf-8'), args.type, store, args.count_as_one)
        result['reference_warnings'] = store.manifest['quality']['warnings']
    except (OSError, UnicodeError, ReferenceError, ValueError) as exc:
        parser.exit(2, f'Validation failed: {exc}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(result['status'] == 'findings')


if __name__ == '__main__':
    raise SystemExit(main())
