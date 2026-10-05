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
3. Save the unedited responses. Record the date, exact model/version and settings
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

## Recorded smoke evaluation

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
recommends fresh contexts per case for future evaluations. No claim is made that
the Python unit suite automatically runs or reproduces this model evaluation.
