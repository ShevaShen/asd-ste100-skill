#!/usr/bin/env python3
"""Build private Issue 9 references. This is the only PDF-aware module."""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parents[1]
RULE_COUNTS = [14, 2, 7, 5, 5, 6, 3, 7, 4]
EXPECTED_RULES = {f'{s}.{n}' for s, total in enumerate(RULE_COUNTS, 1)
                  for n in range(1, total + 1)}
ENTRY = re.compile(r'^(.+?)\s*\((n|v|adj|adv|pron|art|prep|conj)\)(?:,|$)')
BUILD_VERSION = '1'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_jsonl(path, rows):
    path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')


def label(text):
    m = re.search(r'\bPage\s+([\w-]+)', text)
    return m.group(1) if m else None


def crop_text(page, box):
    return page.within_bbox(box).extract_text(x_tolerance=2, y_tolerance=3) or ''


def provenance(page, printed, box):
    return {'pdf_page': page.page_number, 'printed_page': printed,
            'bbox': [round(x, 3) for x in box]}


def bold(line):
    return any('bold' in c['fontname'].lower() for c in line['chars'])


def dictionary_anchors(page, left):
    region = page.within_bbox((left - 1, 90, left + 106, 715))
    lines = region.filter(lambda o: o.get('object_type') == 'char' and
                          'bold' in o.get('fontname', '').lower()).extract_text_lines()
    return parse_headword_lines(lines)


def parse_headword_lines(lines):
    """Parse bold left-column lines, including line-wrapped headwords."""
    anchors = []
    consumed = -1
    for i, line in enumerate(lines):
        if i <= consumed:
            continue
        text = line['text'].strip()
        match = ENTRY.match(text)
        j = i
        while not match and j + 1 < len(lines) and j < i + 3:
            if text.endswith(',') or lines[j + 1]['top'] - lines[j]['top'] > 14:
                break
            j += 1
            text = text[:-1] + lines[j]['text'] if text.endswith('-') else text + ' ' + lines[j]['text']
            match = ENTRY.match(text)
        if match:
            consumed = j
            anchors.append({'headword': match[1].strip(), 'pos': match[2],
                            'top': line['top'] - 1})
    return anchors


def dictionary_fragment(page, printed, left, top, bottom):
    bounds = [left - 1, left + 106, left + 235.5, left + 365.2, min(page.width, left + 493)]
    region = page.within_bbox((bounds[0], top, bounds[-1], bottom))
    words = region.extract_words(extra_attrs=['fontname'])
    # Some rows shift the meaning column five points left of its header.
    starts = [w['x0'] for w in words if left + 95 < w['x0'] < left + 112
              and 'bold' not in w['fontname'].lower()]
    if starts:
        bounds[1] = min(starts) - 0.5
    names = ['word_and_forms', 'meaning_or_alternatives', 'ste_examples', 'non_ste_examples']
    box = (bounds[0], top, bounds[-1], bottom)
    result = provenance(page, printed, box)
    result['columns'] = {name: crop_text(page, (a, top, b, bottom))
                         for name, a, b in zip(names, bounds, bounds[1:])}
    result['bold_word_text'] = region.filter(
        lambda o: o.get('object_type') == 'char' and o['x0'] < left + 106
        and 'bold' in o.get('fontname', '').lower()).extract_text() or ''
    result['raw_text'] = crop_text(page, box)
    return result


def extract(document):
    pages, rules, entries, sections, issues = [], [], [], {}, []
    active_rule = None
    active_entry = None
    for page in document.pages:
        text = page.extract_text(x_tolerance=2) or ''
        printed = label(text)
        pages.append({'pdf_page': page.page_number, 'printed_page': printed, 'text': text})
        if printed and re.fullmatch(r'1-[1-9]-\d+', printed):
            section = int(printed.split('-')[1])
            section_data = sections.setdefault(section, {'section': section, 'title': None, 'pdf_pages': []})
            section_data['pdf_pages'].append(page.page_number)
            heading = re.search(r'Section\s+\d+\s*[-–]\s*(.+)', text)
            if heading:
                section_data['title'] = heading[1].strip()
            if active_rule and active_rule['section'] != section:
                active_rule = None
            lines = page.crop((40, 70, 575, 715)).extract_text_lines()
            anchors = []
            stop = 715
            for i, line in enumerate(lines):
                if line['text'].startswith('General recommendations') and printed != '1-9-1':
                    stop = line['top'] - 1
                    break
                match = re.match(r'^Rule (\d+\.\d+)\s+(.+)', line['text'])
                if match and bold(line):
                    statement = [match[2]]
                    for following in lines[i + 1:]:
                        if not bold(following) or following['text'].startswith('Rule '):
                            break
                        statement.append(following['text'])
                    anchors.append((line['top'] - 1, match[1], ' '.join(statement)))
            points = [(70, None, None)] + anchors + [(stop, None, None)]
            for (top, rule_id, statement), (bottom, _, _) in zip(points, points[1:]):
                if rule_id:
                    active_rule = {'rule_id': rule_id, 'section': section,
                                   'statement': statement, 'fragments': []}
                    rules.append(active_rule)
                if active_rule and bottom > top and 'Blank Page' not in text:
                    box = (40, top, 575, bottom)
                    fragment = provenance(page, printed, box)
                    fragment['text'] = crop_text(page, box)
                    active_rule['fragments'].append(fragment)
            if stop != 715:
                active_rule = None

        if not printed or not re.fullmatch(r'2-1-[A-Z]\d+', printed) or 'Blank Page' in text:
            page.close()
            continue
        headers = [w for w in page.extract_words() if w['text'] == 'Word' and w['top'] < 90]
        if len(headers) != 1:
            raise ValueError(f'Unrecognized dictionary header on PDF page {page.page_number}')
        left = headers[0]['x0']
        anchors = dictionary_anchors(page, left)
        if not anchors:
            issues.append(f'No dictionary anchors on page {page.page_number}')
        if anchors and anchors[0]['top'] > 108:
            prefix = dictionary_fragment(page, printed, left, 90, anchors[0]['top'])
            if prefix['raw_text'].strip():
                if active_entry is None:
                    issues.append(f'Orphan continuation on page {page.page_number}')
                else:
                    active_entry['fragments'].append(prefix)
        for i, anchor in enumerate(anchors):
            bottom = anchors[i + 1]['top'] if i + 1 < len(anchors) else 715
            key = (anchor['headword'].casefold(), anchor['pos'])
            approved = re.sub(r'\(or .*?\)', '', anchor['headword']).isupper()
            if (active_entry is None or
                    (active_entry['headword'], active_entry['pos']) != (anchor['headword'], anchor['pos'])):
                active_entry = {'entry_id': f'{key[0]}:{key[1]}:{"approved" if approved else "nonapproved"}',
                                'headword': anchor['headword'], 'lookup_key': key[0],
                                'pos': key[1], 'approved': approved,
                                'fragments': []}
                entries.append(active_entry)
            active_entry['fragments'].append(dictionary_fragment(page, printed, left, anchor['top'], bottom))
        page.close()
    for entry in entries:
        entry['columns'] = {name: '\n'.join(f['columns'][name] for f in entry['fragments']).strip()
                            for name in entry['fragments'][0]['columns']}
        # Retain full source columns. Forms are a search aid, not synthesized inflections.
        first = '\n'.join(f['bold_word_text'] for f in entry['fragments'])
        after = re.split(r'\((?:n|v|adj|adv|pron|art|prep|conj)\)', first, maxsplit=1)
        forms = []
        if entry['approved'] and entry['pos'] in {'v', 'adj'} and len(after) == 2:
            for form in re.split(r'[,\n()]', after[1]):
                cleaned = re.sub(r'^also\s+', '', form.strip())
                if re.fullmatch(r'[A-Z][A-Z -]*', cleaned):
                    forms.append(cleaned)
        entry['listed_forms'] = list(dict.fromkeys(forms))
        entry['aliases'] = []
        variant = re.fullmatch(r'(.+?)\s+\(or (.+?)\)', entry['headword'])
        if variant:
            entry['aliases'] = [variant[1], variant[2]]
    return pages, rules, entries, list(sections.values()), issues


def check_quality(pages, rules, entries, issues):
    failures = list(issues)
    if len(pages) != 434:
        failures.append(f'Expected 434 PDF pages, got {len(pages)}')
    ids = [r['rule_id'] for r in rules]
    if set(ids) != EXPECTED_RULES or len(ids) != len(EXPECTED_RULES):
        failures.append(f'Rule coverage mismatch: missing={sorted(EXPECTED_RULES-set(ids))}; duplicates={len(ids)-len(set(ids))}')
    counts = Counter(e['approved'] for e in entries)
    # The inspected table has separate approved/nonapproved senses and POS rows.
    # Preserve these rows; never discard records to match the introduction's totals.
    if counts not in ({True: 875, False: 1274}, {True: 878, False: 1317}):
        failures.append(f'Unexpected dictionary profile: approved={counts[True]}, nonapproved={counts[False]}')
    keys = [e['entry_id'] for e in entries]
    if len(keys) != len(set(keys)):
        failures.append('Duplicate dictionary keys')
    for record in rules + entries:
        if not record['fragments'] or any(not f['printed_page'] for f in record['fragments']):
            failures.append('Missing provenance')
    return failures


def build(source, output):
    import pdfplumber
    source = Path(source).expanduser().resolve()
    output = Path(output).resolve()
    # Source-derived output is deliberately constrained to ignored locations.
    if output != ROOT / 'references' / 'generated':
        raise ValueError('Output must be this project\'s references/generated directory')
    with pdfplumber.open(source) as document:
        cover = document.pages[0].extract_text() or ''
        if 'ISSUE 9, JANUARY 2025' not in cover or 'ASD-STE100' not in cover:
            raise ValueError('Not the inspected ASD-STE100 Issue 9 edition')
        data = extract(document)
    pages, rules, entries, sections, issues = data
    failures = check_quality(pages, rules, entries, issues)
    if failures:
        raise ValueError('Extraction quality checks failed: ' + '; '.join(failures))
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.generated-', dir=output.parent) as temp:
        temp = Path(temp)
        write_jsonl(temp / 'pages.jsonl', pages)
        write_jsonl(temp / 'rules.jsonl', rules)
        write_jsonl(temp / 'dictionary.jsonl', entries)
        recommendations = []
        for p in pages:
            if p['pdf_page'] >= 123 and (p['printed_page'] or '').startswith('1-9-'):
                for match in re.finditer(r'^GR-([1-8])\s+(.+)', p['text'], re.MULTILINE):
                    recommendations.append({'id': 'GR-' + match[1], 'title': match[2],
                                            'pdf_page': p['pdf_page'], 'printed_page': p['printed_page']})
        write_json(temp / 'index.json', {'schema_version': 1, 'issue': 9, 'sections': sections,
                   'dictionary_introduction_pdf_pages': [p['pdf_page'] for p in pages
                                                         if (p['printed_page'] or '').startswith('2-0-')],
                   'general_recommendations': recommendations,
                   'rules': [{'rule_id': r['rule_id'], 'section': r['section'],
                              'pdf_page': r['fragments'][0]['pdf_page'],
                              'printed_page': r['fragments'][0]['printed_page']} for r in rules],
                   'datasets': ['pages.jsonl', 'rules.jsonl', 'dictionary.jsonl']})
        files = sorted(temp.iterdir())
        manifest = {'schema_version': 1, 'issue': 9, 'issue_date': '2025-01-15',
                    'build_version': BUILD_VERSION, 'pdfplumber_version': pdfplumber.__version__,
                    'source_sha256': digest(source), 'source_name': source.name,
                    'counts': {'pages': len(pages), 'rules': len(rules), 'dictionary': len(entries),
                               'approved': sum(e['approved'] for e in entries),
                               'nonapproved': sum(not e['approved'] for e in entries)},
                    'source_declared_word_counts': {'approved': 875, 'nonapproved': 1274},
                    'quality': {'structural_checks': 'passed', 'transcription': 'machine-extracted; semantic review required',
                                'warnings': ([] if len(entries) == 2149 else [
                                    'Extracted entry counts differ from source-declared word counts. '
                                    'Table rows were inspected, but the counting difference remains unreconciled. '
                                    'Treat this corpus as a reference aid, not a certified transcription.'])},
                    'files': {p.name: digest(p) for p in files}}
        write_json(temp / 'manifest.json', manifest)
        output.mkdir(parents=True, exist_ok=True)
        # Publish the manifest last: interrupted builds fail runtime integrity checks.
        for p in files + [temp / 'manifest.json']:
            os.replace(p, output / p.name)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', nargs='?', default=os.environ.get('ASD_STE100_SOURCE'))
    args = parser.parse_args()
    if not args.source:
        parser.error('Provide a PDF path or set ASD_STE100_SOURCE')
    try:
        result = build(args.source, ROOT / 'references' / 'generated')
    except (OSError, ValueError, ImportError) as exc:
        parser.exit(2, f'Build failed: {exc}\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
