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

## Original examples, generated with the skill

These longer fictional scenarios were submitted to separate responding agents
that loaded the actual `SKILL.md`. Each agent saw only its scenario and the skill,
with no intended answer or grading rubric. The complete documents include the
source, actual response, and a separate reviewer assessment. The migration
example includes a real clarification turn and the resulting final procedure.

| Example | What it exercises | Complete source and response |
| --- | --- | --- |
| Configuration deployment | Approvals, optional evidence, verified exports, exact interface labels, acceptance limits, failure handling, and permission to resume service. | [Full NORMALIZE example](examples/normalize-deployment.md) |
| Service-log export | Description and procedure rules, required material in notes, conflicting timing definitions, approval scope, passive-voice exceptions, and VALIDATE-only behavior. | [Full validation report and follow-up](examples/validate-export-followup.md) |
| Collector migration | Ambiguous component references, upload versus test failure, rollback scope, window expiry, and mandatory records after an early stop. | [Full clarification exchange](examples/clarify-migration.md) |

### Deployment: preserve the conditions that make the procedure work

The source describes an update from DG-4.8.1 to DG-4.8.2 at station H-17. Dispatch
is already disabled. The operator needs approval, an empty queue, and a verified
export before applying the update. The screenshot is optional; the completion
record is mandatory. The complete example retains all of that context.

**Source excerpt**

> The existing settings are to be exported by clicking “Export settings”; attach the resulting file to change record CHG-2041 before applying the update. The file name must be H-17-DG-4.8.1.json. NOTE: The exported file must open successfully and contain exactly 12 routing rules. If either check fails, stop and contact the release owner. You must not apply DG-4.8.2 without this verified export.

**Actual response excerpt**

> 6. Click “Export settings” to export the existing settings. Make sure that the file name is H-17-DG-4.8.1.json. Attach the exported file to change record CHG-2041 before you apply the update.
>
> 7. Verify that the exported file opens successfully. Verify that the exported file contains exactly 12 routing rules. If either check fails, stop the procedure. If either check fails, contact the release owner. Do not apply DG-4.8.2 without this verified export.

The export checks become required steps. Later, the response preserves permission
to enable dispatch only after both checks pass:

> If the active-configuration check or the test fails, keep dispatch disabled. If either fails, contact the release owner. You may enable normal dispatch only when both the active-configuration check and the test pass.

The [complete response](examples/normalize-deployment.md) also preserves the
90-second readiness limit, 30-second test limit, and exact “DON'T CLOSE; WAIT”
label. Review limitation: it relies on the initial disabled-dispatch state from
the supplied context without repeating that prerequisite.

### Validation: review the draft without producing a replacement

The export scenario contains six work steps, three notes, a descriptive opening,
and a handover paragraph. It includes an eight-sentence paragraph, instructions
joined with semicolons, approval conditions after commands, and required checks
hidden in notes. It also contains a fixed label with a semicolon, which must stay
unchanged, and an incident whose deletion actor is unknown.

**Source excerpt**

> NOTE: You must compare the Tenant ID in the downloaded file with the approved request before sharing the folder link. If they do not match, do not share the link and notify the data steward.

**Actual finding under rule 5.5**

> The first note requires a Tenant ID comparison before sharing and specifies what to do after a mismatch. Without this note, step 5 permits the analyst to send the link without that comparison.

The [full report](examples/validate-export-followup.md) separates writing findings, meaning
questions, and vocabulary uncertainty. It asks what starts the ten-minute clock
and whether three references to approval mean one authorization or several.
It does not supply a rewritten procedure or invent dictionary approval.

**Observed failure and follow-up:** the initial response labeled some “should”
wording as a definite imperative-form violation before establishing its force.
The skill now classifies advice, permission, and requirements before applying
instruction rules. Two fresh runs of the same export request avoided that
overstatement, while still identifying mandatory instructions. Four new short
regression responses also passed their criteria. The [follow-up evidence](examples/validate-export-followup.md)
preserves the original failure and both new reports. These checks do not establish
that every other finding or dictionary decision is correct.

### Clarification: resolve the component and failure path before rewriting

The migration draft says:

> Before restarting it, disconnect COL-E1 from RLY-7. Connect COL-E2, load relay package RP-2.4, and select “Restart service”. If the transfer fails, return it to the previous version and tell the change owner. Do not enable live delivery during a rollback.

**Actual first response**

> I need these technical details before I can produce a definitive procedure:
>
> 1. Which component and service does “Restart service” restart? Does “Before restarting it” refer to the same restart?
> 2. What does “the transfer” refer to? What conditions indicate that the transfer failed?
> 3. Which component must return to its previous version? Specify the version and the required rollback actions, including the required collector connections.
> 4. If RLY-7 does not show “Acknowledged” for TEST-451 within 30 seconds, what must the operator do?
> 5. If the procedure cannot finish by 13:15 UTC, what must the operator do?

The fictional follow-up identifies the relay as the restart target and defines
upload failure, rollback connections, test-failure handling, and window expiry.
The resulting procedure keeps upload rollback separate from a failed test,
requires authorization before live delivery, and records the outcome even after
an early stop. Read the [complete exchange and final procedure](examples/clarify-migration.md).

[Initial execution metadata](examples/manifest.json) records the skill hash, prompt and
response hashes, context boundaries, and unavailable model metadata. The
[follow-up record](evals/results/2026-10-06-recommendations.json) identifies the
revised skill and its focused checks. Responses
were reviewed by the primary assistant, not a human expert. Exact responses are
retained in [examples/outputs/](examples/outputs/). These are fictional writing
examples, not validated operating instructions or certified STE.

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

### Skill behavior

[Behavioral cases](evals/cases.json) cover recommendations versus requirements,
unknown actors, conditional instructions, fixed labels, VALIDATE-only requests,
clarification, and individual description/safety rule citations. They specify meaning-preservation criteria rather than one
required answer string. See the [evaluation procedure and recorded results](evals/README.md).

The [complete 2026-10-06 regression](evals/results/2026-10-06-full-regression.json)
ran all ten cases twice against the recommendation-classification revision:
**20/20 responses passed their stated criteria**, each in a fresh context.
Exact model/settings remain unavailable, and grading is assistant-only.

These evaluations exercise an assistant using the actual `SKILL.md`. They are
separate from the Python tests and are not a full compliance benchmark.

### Optional Python tools

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

The optional validator recognizes marked vertical lists, including bullets and
numbered or lettered items. It counts introductory clauses and items separately,
keeps wrapped continuations together, and preserves original finding offsets.
Unmarked lists and ambiguous layouts still require contextual review.

## License and attribution

The project's original code and explanatory wording are available under the
[MIT License](LICENSE). The official ASD standard, dictionary, source examples,
logos, and trademarks are not licensed by this project. See [NOTICE.md](NOTICE.md).
