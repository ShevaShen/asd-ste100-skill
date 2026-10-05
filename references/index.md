# Runtime reference map

This guide is for optional, explicitly requested reference-backed work. The default
self-contained `SKILL.md` does not load this guide or call these tools.

Run `python3 scripts/lookup.py index` for the compact generated section map.
Start with the sections relevant to the operation and text; do not load the
entire corpus. Detailed records include explanations and source locators.
The index also points to dictionary introduction pages and the eight general
recommendations. Retrieve their page records when meanings, forms, or writing
practices require that context.

```sh
python3 scripts/lookup.py rule 1.5
python3 scripts/lookup.py section 8
python3 scripts/lookup.py word activate
python3 scripts/lookup.py word control --pos n
python3 scripts/lookup.py search 'passive voice' --limit 5
python3 scripts/lookup.py page 113
```

`word` is an exact, case-insensitive headword or listed-form lookup. It can return
multiple parts of speech. It does not stem words or infer senses. `search` is a
bounded literal substring search across rule and dictionary records.

Operation guides: [NORMALIZE](normalize.md), [VALIDATE](validate.md).
Maintenance and data contract: [design](design.md), [README](../README.md).
