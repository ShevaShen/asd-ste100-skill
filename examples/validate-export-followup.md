# VALIDATE follow-up: advice, permission, and required instructions

This is a fresh use of the corrected self-contained skill on the [same export request and draft](inputs/validate-export.md). The prompt did not mention the earlier failure, the correction, or the evaluation criteria.

## What changed and what was checked

The [initial response](validate-export.md) put “you should keep” and “the analyst should record” in a table of definite imperative-form violations. Its own meaning questions said that the intended force still needed clarification. The review also identified the need to distinguish permission to close a ticket from a commanded action.

The skill now explicitly classifies instructions, requirements, recommendations, permissions, and descriptions before applying instruction rules. It does not infer a definite 5.3 violation from non-imperative advice or permission. Supplied context can still establish that “should” expresses a mandatory instruction. This is an application convention for preserving meaning, not a new numbered STE rule or a general exemption from writing rules.

Two fresh responding contexts independently received the same original export prompt and revised skill. Both responses:

- Keep the “should” statements outside definite 5.3 findings.
- Treat ticket closure as a permission or meaning question, without inventing a required action or actor.
- Still identify the mandatory record-update instruction under 5.3.
- Identify required actions and limits in notes under 5.5, and ask what starts the ten-minute limit.
- Preserve the fixed-label and unknown-actor exceptions.
- Supply a validation report without a rewritten procedure or a claim of dictionary verification.

Two new short regression cases were also run twice in fresh contexts. They distinguish explicit advice and permission from a mandatory update, and verify that context can make “should” mandatory. All four short responses and both long responses passed their stated criteria in the primary assistant's review. This was not a human expert assessment. The eight older short cases were not rerun against this revision.

## Actual response: first fresh run

This is an **STE-guided validation of the original draft**. Full dictionary compliance was not assessed. The findings below use the supplied skill; they do not establish dictionary approval or prohibition for individual words.

The opening paragraph and third note are descriptive. Steps 1–6 contain procedural content, although step 3 uses potentially advisory wording. The first two notes contain mandatory actions or limits. The final paragraph mixes a recommendation, an optional item, a permission, and a prohibition. No explicit safety hazard is supplied, so a warning or caution cannot be justified from this text alone.

**Clear writing-rule findings**

1. **Sentence length — rule 5.1.** Five numbered steps exceed the 20-word procedural limit:

   | Step | Identifying excerpt | Count |
   |---|---|---:|
   | 1 | “Don't start until you have reviewed…” | 24 |
   | 2 | “Select the last seven complete UTC days…” | 24 |
   | 4 | “If the export doesn't finish within 10 minutes…” | 27 |
   | 5 | “Save the downloaded file in the restricted case folder…” | 28 |
   | 6 | “The request record is to be updated…” | 24 |

   These counts treat each exact quoted interface string as one word and “10 minutes” as one word, as required by rule 8.6. They exclude step numbers. The long sentences combine prerequisites, actions, or restrictions that the analyst must track together. Step 3 has 18 words under the same conventions and does not exceed the procedural limit. No descriptive sentence exceeds the 25-word limit in rule 6.3.

2. **Multiple instructions — rule 5.2.** Step 1 combines “Don't start,” “compare,” and “obtain approval.” Step 2 combines selecting the date range and starting the export. Step 4 combines cancellation, notification, and a restriction on another export. Step 5 combines saving, checking, sending, and the attachment prohibition. The first note also combines “do not share the link” and “notify the data steward” in one sentence. The text does not establish that these actions occur simultaneously. Combining them makes individual requirements easier to overlook and obscures their order.

3. **Contractions and authored semicolons — rules 4.2 and 8.1.** “Don't start” in step 1 and “doesn't finish” in step 4 contain contractions. The semicolons after “request record” in step 1 and “requester” in step 5 violate rule 8.1. The contraction and semicolon inside the exact label “Don't close; export running” are not findings: that interface string must remain unchanged.

4. **Perfect and progressive constructions — rule 3.2.** Examples are “have reviewed” in step 1; “is being displayed” and “has completed” in step 3; “has been checked” in step 6; and “has been downloaded” in the third note. These forms are outside the skill's permitted tense framework. The third note remains subject to this rule even though its function is descriptive.

5. **Action constructions ending in “-ing” — rule 3.5.** “By selecting” in step 2 and “before sharing” in the first note express actions through “-ing” constructions. “Excluding the current day” in step 2 also expresses an exclusion action this way. These findings do not apply merely because a word ends in “-ing”: “processing” in “export processing” can function as part of a technical noun, and text inside a fixed interface label is preserved.

6. **Procedural voice and form — rules 3.6, 5.3, and 3.4.** Step 6 expresses the record-update instruction as “The request record is to be updated by the duty analyst.” This is passive, is not imperative, and uses a complex auxiliary construction. The actor is already supplied, so there is no need to invent one. The first note's “You must compare” and the final “Operators must not change” also express mandatory actions without the imperative form required by rule 5.3. The force of “should” and “can” requires separate assessment below.

7. **Condition placement — rule 5.4.** In step 2, “if the request record shows ‘Approved’” follows the command to start the export. The analyst needs this prerequisite before acting. Its late position also leaves the scope of the condition less clear: it could appear to govern both date selection and export initiation.

8. **Mandatory content in notes — rule 5.5.** The first note requires a Tenant ID comparison before sharing and specifies what to do after a mismatch. Without this note, step 5 permits the analyst to send the link without that comparison. The second note imposes the limit “The download must be completed within 10 minutes” and defines its scope. These are required actions and limits, not optional explanatory information. Their placement means the procedure does not retain all its requirements when the notes are omitted. The third note explains availability and removal; its descriptive function is suitable for a note.

9. **Paragraph structure — rules 6.6 and 6.5.** The opening paragraph has eight sentences, exceeding the six-sentence maximum in rule 6.6. It also moves from general export information to the incident-specific deletion and evidence, creating a separate topic under rule 6.5. The closing paragraph similarly combines handover documentation, link-access permission, and retention control. This organization makes distinct operational restrictions less easy to locate.

**Meaning questions and practical consequences**

- **What does each 10-minute limit measure?** Step 4 concerns an export that “doesn't finish within 10 minutes.” The second note requires the download to finish within 10 minutes, including “preparation, export processing, and the download itself.” The start event for either timer is not explicit. These could be different limits, but the procedure does not explain their relationship or what to do if export processing finishes while the overall deadline is missed. This is a material clarity issue under rule 4.1.

- **Is keeping the browser open mandatory or recommended?** Step 3 says “you should keep the browser open.” That wording alone does not establish a mandatory instruction, so it does not support a definite rule 5.3 finding. Its relationship to the cancellation path also needs clarification: after cancellation, the download might never complete, leaving “until the download has completed” without a usable endpoint. Rules 4.1 and 4.4 support making that relationship explicit.

- **What checks permit the record update and ticket closure?** Step 6 uses “after the file has been checked,” but step 5 checks that the file opens and the first note checks its Tenant ID. It is unclear whether both checks are prerequisites. “The ticket can then be closed” also does not establish whether closure is permitted or required, or who performs it. These uncertainties affect completion criteria under rule 4.1; an actor or obligation must not be invented.

- **What exactly is compared, and which approval applies?** Step 1 compares the Tenant ID “with the support ticket,” while the first note compares it “with the approved request.” The corresponding fields and the relationship between “approved request” and “request record” are not explicit. In “If they do not match,” the intended pair should be confirmed, consistent with rule 4.1 and recommendation GR-3. Similarly, it is unclear whether the steward's approval to export, the “Approved” status, and approval to share the link represent one authorization or separate authorizations.

- **Which roles and retention period are intended?** The draft uses “duty analyst,” “analyst,” and “Operators.” If they identify the same role, inconsistent naming is relevant to rules 1.11 and 9.4; if they identify different roles, their responsibilities need clarification. “The retention period” could refer to the portal's 24-hour availability or to another retention requirement for the saved file. The intended scope matters under rule 4.1.

The handover statement “the analyst should record…” is a recommendation unless additional context establishes otherwise. “A screenshot is optional” and “Requesters may receive…” express optionality and permission. Their non-imperative form alone is not a supported violation of rule 5.3.

**Vocabulary uncertainty and valid exceptions**

“Tenant ID,” “data steward,” “service log,” and “request record” are supplied as established terms. Their use should not be rejected merely because complete dictionary entries are unavailable. Other domain terms and verbs, including “tenant,” “portal,” “export,” and “download,” require contextual assessment under rules 1.5 and 1.12; their familiar computing meanings do not by themselves prove approval in every grammatical role.

General words such as “owns,” “obtain,” “notify,” and “authorizes” have not been checked for approved meanings and forms under rules 1.1–1.4. They are unverified, not demonstrated violations. No dictionary-approved replacements are asserted here.

“During incident INC-317, an export was deleted” is not a supported passive-voice violation: the next sentence explicitly establishes that the actor is unknown, which permits descriptive passive voice under rule 3.6. Likewise, participial modifiers such as “downloaded file,” “restricted case folder,” and “approved request” are not automatically passive constructions or prohibited forms under rule 3.3; their vocabulary status remains separate.


## Second fresh run and provenance

The [second complete response](outputs/validate-export-2026-10-06-b.md) is retained separately, as is the [exact first response](outputs/validate-export-2026-10-06-a.md). The displayed first response changes heading levels only.

The [evaluation record](../evals/results/2026-10-06-recommendations.json) contains the skill and case hashes, prompt/response hashes, responding-context identifiers, criteria, and review results. Exact model/version and sampling settings were not exposed and are recorded as null. Each respondent read only the skill and its request, with no tools or retrieval during composition; a tool saved the completed response afterward.

The [earlier example metadata](manifest.json) and original responses are unchanged. The earlier skill can be inspected at [the baseline commit](https://github.com/ShevaShen/asd-ste100-skill/blob/aa387635bfafaaf25f49f2b07adf694c68093987/SKILL.md).

These checks target the documented classification problem and preservation boundaries. They do not verify every finding, word count, dictionary entry, or operational requirement in the reports. The scenario is fictional and the reports are not certified STE assessments.
