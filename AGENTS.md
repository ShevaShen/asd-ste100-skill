# Project development

- `SKILL.md` is the complete self-contained runtime skill. NORMALIZE and VALIDATE
  use only that file and conversation content, without reference lookups or tools.
- Preserve technical meaning and distinguish writing guidance from verified
  dictionary compliance. Do not claim ASD endorsement or certification.
- The public release includes original code and independently worded guidance.
  Never commit the official PDF, extracted pages, dictionary, or generated corpus.
- Source audits and extraction are optional maintenance work; see `references/design.md`.
- After code changes, run `python3 -m unittest discover -s tests -v`.
- Keep examples synthetic. Preserve provenance when deliberately updating guidance.
