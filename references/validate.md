# VALIDATE

This guide is for optional, explicitly requested reference-backed work. The default
self-contained `SKILL.md` does not load this guide or call these tools.

Keep the original unchanged. Separate mixed passages before running checks.

```sh
python3 scripts/validate_ste.py input.txt --type procedural
python3 scripts/validate_ste.py input.txt --type descriptive
python3 scripts/validate_ste.py input.txt --type safety
```

The JSON report distinguishes deterministic findings from review candidates and
lists coverage limits. Exit 0 means no deterministic findings; 1 means at least
one deterministic finding; 2 means an input or setup error. Review candidates
can still be present with exit 0.

Read the cited generated rules and inspect every finding in context. Confirm
that any exempt quoted text really is a fixed quotation or label. Review
sentence boundaries and special word-count elements before declaring a length
violation. `--count-as-one 'Name of a manual'` can annotate a verified element
under rule 8.6; it does not approve the phrase's vocabulary or grammar.

Then review meaning, vocabulary, parts of speech, permitted forms, technical-term
categories, voice, instruction structure, safety wording, and consistency using
the relevant generated rules and dictionary. The deterministic script does not
perform these semantic checks. Avoid marking unknown words as forbidden.

Return findings with original excerpts/locations, applicable rule IDs, evidence
pages, and proposed corrections when requested. Clearly distinguish unassessed
requirements from those reviewed. Do not rewrite the whole text unless NORMALIZE
was also requested. Do not call a partial scan a full compliance validation.
