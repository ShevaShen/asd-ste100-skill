# Reference design

## Source inspection

The inspected Issue 9 document is dated 2025-01-15 and has 434 PDF pages.
Printed labels differ from PDF page numbers. Contents are on PDF page 29.
Part 1 has nine sections (PDF pages 45–128); the dictionary introduction starts
on page 131 and the word list occupies pages 149–434, including blank pages.
The introduction reports 875 approved and 1,274 non-approved words.

Rule summaries repeat the detailed rules. Detailed rule headings use bold type;
summary headings use regular type. Dictionary columns contain the headword and
part of speech, meaning/alternatives, STE examples, and non-STE examples.
Left margins alternate between pages. Uppercase **headwords**, not uppercase
example text, identify approved entries. Entries can wrap or continue on another
page. Approved entries can also give alternatives for unapproved meanings.

## Build boundary

`build_reference.py` alone imports the PDF dependency. It extracts page text,
identifies detailed rule headings using layout and typography, and divides the
dictionary by its actual header positions and bold headword anchors. A source
SHA-256 hash identifies the input. PDF pages are one-based; bounding boxes use
PDF points with a top-left origin. Each record retains printed page labels.

All generated files, including the manifest and index, live in
`references/generated/`. No source text belongs in tracked fixtures or docs.
The builder supports this inspected layout, not arbitrary PDFs or later issues.
It fails on structural mismatches and publishes only after quality checks pass.
It does not OCR or infer missing words. Keep the original outside the repository,
or in ignored `source/`, for deliberate rebuilds and source audits.

## Generated schema (version 1)

- `manifest.json`: edition, source hash, extraction version, dependency version,
  observed counts, quality diagnostics, and hashes of generated data files.
- `index.json`: section names, rule IDs, page ranges, and available datasets.
  Also includes dictionary introduction and general-recommendation page pointers.
- `pages.jsonl`: PDF page number, printed label, and extracted page text. This
  provides context when a row or column is ambiguous; lookup is by exact page.
- `rules.jsonl`: rule ID, section, heading text, and page/bounding-box excerpts.
  The excerpts preserve explanation and exceptions. Layout extraction can flatten
  example tables: consult the associated page record for additional context.
- `dictionary.jsonl`: stable entry ID, original headword, case-folded lookup key,
  part of speech, approved status, source column text, listed forms, and page
  fragments with bounding boxes. Column 2 remains `meaning_or_alternatives`:
  splitting it into authoritative senses or replacement pairs would require
  semantic review. `raw_text` retains full-width help text that spans columns.
  Entry IDs include approval status because some word/POS pairs have separate
  approved and non-approved entries. Explicit spelling variants are lookup aliases.

No inferred replacement is an approved automatic substitution. A dictionary hit
does not verify a word's meaning or part of speech in the user's sentence.
Missing words can be permissible technical terms. A glossary is contextual
evidence, not a bypass for word categories, meaning, or grammar.

## Quality and runtime boundary

Build checks require the expected edition, page count, all 53 rule IDs, a known
dictionary extraction profile, both approval classes, and complete provenance. Ambiguous fragments fail
the build instead of disappearing. Counts establish structural coverage, not
perfect transcription. Original help text and page context remain queryable.

The current extraction yields 878 approved and 1,317 non-approved entry records,
which differ from the introduction's word totals. A separate inspection of the
physical table rows checked headword boundaries, including wrapped entries.
The difference in counting remains **unreconciled**. Do not drop entries to force
agreement. The manifest preserves both totals and a warning, which runtime
commands propagate. Full transcription accuracy and completeness are not certified.

Runtime lookup uses only Python's standard library and generated files. Integrity
checks reject missing, changed, or incompatible datasets without opening a PDF.
NORMALIZE is an agent-guided semantic operation; the scripts do not implement
blind rewriting. VALIDATE reports the original text and never changes it.

The deterministic checks cover semicolons (8.1) and a conservative list of
contractions (4.2), outside identified quotation spans. Quoted syntax is not
enough to authorize an exemption: reviewers must confirm it is protected source
text. Sentence-length and paragraph-size findings are review candidates. Word
counting handles several explicit patterns, but plain text cannot reliably
identify every title, name, label, abbreviation, number expression, or list.
No output from the checker certifies full ASD-STE100 compliance.

The optional validator recognizes explicit bullet, number, and letter list markers.
A colon immediately before a marked vertical list ends the introductory counting
unit. Each marked item starts a new unit; an unmarked wrapped line remains part
of that item. List markers do not add words. Blank lines separate paragraphs,
and marked list items are separate units for paragraph-size review. Inline
colons, quoted punctuation, and punctuation inside parentheses do not create
spurious outer boundaries. Findings retain offsets into the unchanged input.
Unmarked lists and layouts without clear paragraph boundaries remain uncertain.
