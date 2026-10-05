# ASD-STE100 writing skill

A self-contained AI writing skill for technical and operational English, informed
by ASD-STE100 Issue 9. It works across domains and separates rewriting from review.

**Load only [SKILL.md](SKILL.md).** Once loaded, the skill uses the conversation
and its own instructions. It needs no PDF, dictionary queries, reference files,
scripts, external services, or other tools.

This is an unofficial writing aid. It is not endorsed or certified by ASD and
does not establish full compliance with the official standard.

## Use

Put `SKILL.md` in a personal skill folder named `asd-ste100`, or supply its text
as instructions to your AI assistant. No software installation is required for
the self-contained workflow.

Choose an operation:

| Operation | Result |
| --- | --- |
| **NORMALIZE** | Drafts or rewrites text while preserving its technical meaning. |
| **VALIDATE** | Reviews the original text without rewriting it, with supported findings and uncertainties. |

Example requests:

> NORMALIZE this maintenance procedure using the ASD-STE100 writing skill.

> VALIDATE this system description. Keep the original unchanged and report specific findings.

> NORMALIZE this onboarding guide. Preserve the interface labels, requirements, and step order.

The guidance covers sentence construction, terminology, verb forms and voice,
procedures, descriptions, safety instructions, punctuation, counting conventions,
and consistency. It includes important exceptions and separates numbered rules
from additional recommendations.

## Limits

The complete official dictionary is **not included**. Approval of a word depends
on its meaning, part of speech, and permitted forms; familiar wording alone does
not establish approval. The skill reports material uncertainty instead of
inventing dictionary decisions. Treat its output as STE-guided writing, and
review technical meaning and safety requirements before use.

Obtain the authoritative standard from the
[official ASD-STE100 website](https://www.asd-ste100.org/STE_downloads.html).
The website is an attribution and source-acquisition link, not a runtime dependency.

## Optional development tools

The repository also includes local extraction and checking utilities for explicit
source audits. They are not needed by the skill:

- `scripts/build_reference.py`: builds private structured references from a
  separately obtained local Issue 9 PDF.
- `scripts/lookup.py`: queries that private corpus with page provenance.
- `scripts/validate_ste.py`: reports selected deterministic findings and
  sentence-count review candidates; it does not certify compliance.
- `references/`: maintenance design and optional reference-backed workflows.
- `tests/`: synthetic tests and opt-in corpus integration checks.

The source PDF and all generated reference data are excluded from Git. Do not
upload them in commits, issues, pull requests, releases, or test fixtures.

To build private references, use Python 3.10 or later and your own source file:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-build.txt
.venv/bin/python scripts/build_reference.py /path/to/ASD-STE100_ISSUE9.pdf
```

Output goes to ignored `references/generated/`. The PDF is read in place. This
does not regenerate or alter the self-contained skill.

The inspected source produced 2,195 dictionary entry records, differing from the
introduction's stated word totals. That difference remains unreconciled and is
surfaced in generated-data warnings. See [the design notes](references/design.md)
for extraction assumptions and limitations.

## Development checks

The regular test suite uses the Python standard library and synthetic examples:

```sh
python3 -m unittest discover -s tests -v
```

After deliberately building a local corpus, enable its integration checks:

```sh
STE_INTEGRATION=1 python3 -m unittest discover -s tests -v
```

These tests cover the optional tools and reference handling. They do not establish
that an AI assistant's output satisfies every writing or vocabulary requirement.
Contributions should use original examples and preserve the self-contained runtime.

## License and attribution

The project's original code and explanatory wording are available under the
[MIT License](LICENSE). The official ASD standard, dictionary, source examples,
logos, and trademarks are not licensed by this project. See [NOTICE.md](NOTICE.md).
