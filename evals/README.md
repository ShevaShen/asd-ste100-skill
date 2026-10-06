# Evaluate the skill's behavior

These original cases exercise an assistant using the actual `SKILL.md`, rather
than testing Python functions. They focus on meaning and operation boundaries:

| Case | Main risk |
| --- | --- |
| `should-versus-must` | Turning a recommendation into a requirement or weakening an obligation. |
| `unknown-actor` | Inventing an actor or a causal relationship. |
| `conditional-instruction` | Losing a necessary condition, conjunction, identifier, or strict threshold. |
| `fixed-labels` | Changing literal interface strings to satisfy spelling or punctuation guidance. |
| `validate-only` | Rewriting when asked only to assess, or overstating verification. |
| `clarification-needed` | Resolving an ambiguous referent without evidence. |
| `description-rule-ids` | Reporting paragraph topics and sentence limits without the individual 6.5 and 6.6 IDs. |
| `safety-rule-ids` | Guessing safety rule IDs or inventing hazard severity. |
| `validate-advice-permission` | Calling advice or permission a definite imperative-form violation while missing an actual required instruction. |
| `validate-required-should` | Treating “should” as optional despite an explicit mandatory meaning in the supplied context. |

## Repeat the evaluation

1. Generate requests from the skill version being tested:

   ```sh
   python3 evals/prepare.py --out local/evals/requests.jsonl
   ```

   The export includes the skill text, case prompt, and input hashes. It excludes
   the grading criteria. It does not call a model or require credentials.
2. Submit each exported request to a fresh assistant context. Supply `instructions`
   as its skill instructions and `prompt` as the user request. Do not supply
   expected answers, rubrics, repository context, or previous outputs. Disable
   retrieval and tools after the skill is loaded.
3. Repeat each case in another fresh context. Save the unedited responses. Record the date, exact model/version and settings
   when available, and the skill/case hashes. Do not infer unavailable metadata.
4. Review each response against every invariant and failure example in
   [`cases.json`](cases.json). Use semantic judgment, not a required answer string.
   Correct unchanged text can be a valid NORMALIZE result. A clarification question
   can be the correct result when a safe definitive rewrite is impossible.
5. Mark a case failed if any invariant fails. Record the specific reason. Keep
   initial failures alongside reruns and identify any change to the skill.

Exact labels, quantities, and rule IDs are inspectable directly. Modality,
causality, conditions, and invented facts need contextual review. Do not use a
keyword score as a substitute for those judgments. A human reviewer or a separate
reviewing assistant should evaluate results; the responding assistant must not
grade itself. Treat unresolved judgments as unresolved, not passed.

For stronger evidence, use multiple independent runs and more than one model.
Passing these cases does not prove universal meaning preservation, dictionary
approval, or compliance with every requirement of the standard.

## Recorded evaluations

### Complete ten-case regression — 2026-10-06

The [full regression record](results/2026-10-06-full-regression.json) covers
**all ten cases, each run twice in a fresh context: 20 responses from 20 contexts**.
Both repetitions passed every case's stated invariants in the primary assistant's
semantic review. No responses were discarded, and neither the skill nor the
criteria changed during the evaluation.

The tested revision is [d6915e9](https://github.com/ShevaShen/asd-ste100-skill/commit/d6915e9a494f9195b4987f86661c875d36aef7ec),
with skill SHA-256
`a2cca8fc98faf927a4b8439c392ec9f766276e58488a257162532352254d89a9`.
This includes the recommendation-classification correction and reruns the eight
older cases that the earlier focused follow-up did not cover.

| Case | Repetition A | Repetition B |
| --- | --- | --- |
| `should-versus-must` | Pass | Pass |
| `unknown-actor` | Pass | Pass |
| `conditional-instruction` | Pass | Pass |
| `fixed-labels` | Pass | Pass |
| `validate-only` | Pass | Pass |
| `clarification-needed` | Pass | Pass |
| `description-rule-ids` | Pass | Pass |
| `safety-rule-ids` | Pass | Pass |
| `validate-advice-permission` | Pass | Pass |
| `validate-required-should` | Pass | Pass |

The record retains every exact response, its hash, prompt and case hashes,
responding-context identifiers, and review reasons. Respondents saw only the
frozen skill and their own prompt, without grading criteria or previous outputs.
They used no retrieval or tools during composition; a tool saved each completed
response afterward.

**Limits remain:** exact model/version and sampling settings were not exposed
and are recorded as null. Grading is assistant-only, with no human expert
assessment or deliberate cross-model comparison. Fresh contexts do not make model
errors statistically independent. These small cases test specific invariants;
they do not certify STE compliance or establish reliability on longer documents.

### Recommendation classification follow-up — 2026-10-06

The [focused follow-up report](results/2026-10-06-recommendations.json) records
four short responses: two repetitions each of `validate-advice-permission` and
`validate-required-should`. All four passed their stated invariants. The
[long export follow-up](../examples/validate-export-followup.md) records two more
fresh responding contexts using the unchanged export prompt. Both passed the
seven targeted preservation and classification checks.

The correction prevents advice and permission from becoming definite 5.3
findings merely because they are not imperative. It still permits a 5.3 finding
when the context establishes a mandatory instruction, including wording with
“should”. The old responses and their documented overstatement remain available.

All six runs used separate responding contexts and were reviewed by the primary
assistant, not a human expert. Model/version and sampling settings were unavailable.
This focused follow-up did not rerun the eight older cases on the new revision;
their results below apply to their recorded skill hashes. Passing the targeted
checks does not validate every finding in the longer reports.

### Fresh contexts and repeated runs

The [fresh-context report](results/2026-10-05-fresh-contexts.json) records two
repetitions of all eight cases: **16 responses from 16 fresh responding contexts**.
All 16 passed their stated invariants in the primary assistant's semantic review.
The responding agents did not see the rubric or one another's outputs.

The report preserves exact responses, skill and case hashes, individual prompt
hashes, and responding-agent identifiers. Exact backend model/version and sampling
settings were unavailable and are recorded as null, not inferred. Respondents
used no retrieval or tools while composing; they saved their completed response
with a tool afterward. These are manual model evaluations, not Python tests.

The [longer examples](../examples/manifest.json) use separate fresh contexts and
are reviewed separately. In particular, the export report overstates an
imperative-form finding about recommendations; its reviewer notes preserve that
limitation. Passing the smaller cases does not establish correctness on longer
documents.

The user inspected the earlier recorded responses but did not independently rerun
the evaluation. That inspection is not counted as another run or human expert
validation. The new runs were executed by responding agents and graded by the
primary assistant. Two repetitions with one unknown model configuration do not
establish cross-model reliability.

### Earlier batched smoke evaluation

The [2026-10-05 report](results/2026-10-05.json) preserves actual responses and
review decisions for two runs:

- Initial skill: 5/6 cases passed. The VALIDATE-only response preserved scope but
  cited broad rule ranges instead of the specific applicable rule IDs.
- After adding precise rule labels and citation guidance: 6/6 cases passed.

Each run used a new responding agent that read only `SKILL.md`, then answered the
six prompts as a batch without further tools. It did not see the rubric. The
primary agent reviewed the outputs against criteria written before execution.
This is assistant-reviewed evidence, not a human expert assessment.

The two runs had independent contexts, but the six cases **within** each run
shared one context. Exact model/version and sampling settings were not exposed.
These constraints limit reproducibility and independence. The procedure above
uses fresh contexts per case, as recorded in the newer report above. No claim is made that
the Python unit suite automatically runs or reproduces this model evaluation.
