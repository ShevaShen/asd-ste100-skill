# VALIDATE: service-log export and approval conditions

This original fictional scenario was run through the actual self-contained skill in a fresh responding-agent context. The response was not hand-written as an ideal answer.

A [follow-up with the corrected skill](validate-export-followup.md) records two fresh runs of the same request. The initial response and review below are preserved unchanged.

## Reviewer assessment

The response stays within VALIDATE: it supplies no corrected procedure. It identifies the eight-sentence paragraph with 6.6, conditions after commands with 5.4, and mandatory material in notes with 5.5. It preserves quoted-label exceptions and the unknown-actor passive exception. Its timing and approval questions identify information that a process owner would need to resolve.

**Review correction:** the table overstates the 5.3 finding for “you should keep” and “the analyst should record”. Those can be recommendations, not mandatory instructions. Their presence in a procedure does not by itself justify a definite imperative-form violation. Keep these as meaning questions until their function is established. Likewise, the permission to close the ticket needs separate treatment from a commanded action. The original response is retained below without silently correcting it.

This is a reviewed model example with a known overstatement, not a gold-standard validation report. Exact dictionary approval and exhaustive rule coverage remain unassessed.

## Original request and draft

Use the loaded self-contained skill to VALIDATE ONLY the following draft. Do not rewrite it and do not supply a corrected procedure. Provide a substantive report that distinguishes clear writing-rule findings from meaning questions and vocabulary uncertainty. Cite specific rule IDs where the skill supports them, quote the relevant text, and explain practical consequences. Avoid inventing missing facts or dictionary approvals.

Context: This is an original fictional support process, not a real data-access policy. The audience is a duty analyst. “Tenant ID”, “data steward”, “service log”, and “request record” are established terms in this fictional organization. The quoted interface strings, including “Don't close; export running”, are exact labels and must not be edited. Assess all text below, including the description and notes.

Draft:

### Weekly service-log export

The service log contains operational events. It does not contain message bodies. Each export covers one tenant. The duty analyst owns the export request. The “Approve & Export” control starts the export. Files remain available for 24 hours. During incident INC-317, an export was deleted. The available evidence does not identify who or what deleted it.

1. Don't start until you have reviewed the request record; compare the Tenant ID with the support ticket and obtain approval from the data steward.
2. Select the last seven complete UTC days, excluding the current day, and start the export by selecting “Approve & Export” if the request record shows “Approved”.
3. While the “Don't close; export running” message is being displayed, you should keep the browser open until the download has completed.
4. If the export doesn't finish within 10 minutes, cancel it and notify the data steward, but do not submit a second export until the data steward authorizes it.
5. Save the downloaded file in the restricted case folder, verify that it opens, and send the folder link to the requester; never attach the file to an email.
6. The request record is to be updated by the duty analyst after the file has been checked, and the ticket can then be closed.

NOTE: You must compare the Tenant ID in the downloaded file with the approved request before sharing the folder link. If they do not match, do not share the link and notify the data steward.

NOTE: The download must be completed within 10 minutes. This time includes preparation, export processing, and the download itself.

NOTE: A file can remain available in the portal after it has been downloaded. The portal removes it 24 hours after export creation.

For the handover, the analyst should record the export creation time and any cancellation in the request record. A screenshot is optional. Requesters may receive the restricted folder link only after data-steward approval. Operators must not change the retention period.

## Actual first response

This is an **STE-guided validation of the original draft**. The draft has clear writing-rule violations and unresolved operational meaning. Full dictionary compliance was not assessed. No rewrite is supplied.

The opening paragraph is descriptive. The numbered steps are procedural. The first note contains required actions, the second contains a time limit and an explanation, and the third is descriptive. The closing paragraph mixes an instruction, a permission, an approval restriction, and a prohibition. No explicit hazard or governing safety-label convention is supplied, so the findings do not assume a missing warning or caution.

**Clear writing-rule findings**

| Location and excerpt | Rule | Finding and practical consequence |
|---|---|---|
| Opening paragraph, from “The service log contains operational events” through “The available evidence does not identify who or what deleted it” | 6.6 | The paragraph contains eight sentences. The limit is six. Export information and the incident account are harder to scan in one paragraph. |
| Step 1: “Don't start” and step 4: “doesn't finish” | 4.2 | These are contractions in authored instructions. The fixed interface label containing “Don't” is a separate case and is not included in this finding. |
| Step 1: “request record; compare” and step 5: “requester; never attach” | 8.1 | Semicolons join authored instructions. The semicolon inside the exact interface label is not a finding. |
| Steps 1, 2, 4, 5, and 6 | 5.1 | These sentences exceed the 20-word procedural limit. Counts appear below. The long sentences combine prerequisites, actions, or restrictions that the analyst must track together. |
| Step 1: “compare … and obtain approval”; step 2: “Select … and start”; step 4: “cancel it and notify … but do not submit”; step 5: “Save … verify … send … never attach”; step 6: “updated … and … closed” | 5.2 | Each sentence contains multiple instructions or directed actions. The text does not establish that these actions occur simultaneously. Several actions have an explicit or apparent sequence, which is difficult to follow within a single sentence. |
| Step 2: “start the export … if the request record shows ‘Approved’” | 5.4 | The approval condition comes after the command that it governs. The analyst encounters the action before its prerequisite. |
| Step 1: “until you have reviewed”; step 3: “has completed”; step 6: “has been checked”; third note: “has been downloaded” | 3.2 | These are perfect-tense constructions, outside the permitted framework. The third note remains subject to this rule even though it is descriptive. |
| Step 3: “is being displayed” | 3.2, 3.5 | This is a progressive action construction. It is outside the quoted interface string, so preserving the string does not exempt this surrounding grammar. |
| Step 2: “by selecting”; first note: “before sharing” | 3.5 | These “-ing” constructions express actions. Their sequence and dependency information still needs to be preserved in any later revision. |
| Step 3: “you should keep”; step 6: “The request record is to be updated”; first note: “You must compare”; closing paragraph: “the analyst should record” | 5.3 | These procedural instructions do not use the imperative. Whether “should” expresses advice or a requirement is a separate meaning question below. |
| Step 6: “is to be updated by the duty analyst” and “the ticket can then be closed” | 3.6 | These are procedural passive constructions. The update actor is explicitly known. The closing actor is not stated and must not be invented. |
| Step 6: “is to be updated” | 3.4 | This is a complex auxiliary construction. It also obscures the direct action within an indirect statement of what is to happen. |
| First note: “You must compare … before sharing” and “If they do not match, do not share the link and notify the data steward” | 5.5 | The note contains required checks, a prohibition, and a notification action. The procedure cannot safely omit this note because it controls whether sharing is permitted. |
| First note: “do not share the link and notify the data steward” | 5.2 | The sentence combines a prohibition and a required action. The mismatch condition governs both and must remain connected to both. |
| Second note: “The download must be completed within 10 minutes” | 5.5 | A required time limit is placed in a note. Its explanatory second sentence does not make the limit optional. |
| Second note: “must be completed” | 3.6 | This required procedural result is expressed in passive voice. The applicable actor or process needs to be established before changing its wording. |

For the length findings, the original sentences count as follows:

| Step | Word count |
|---|---:|
| 1 | 24 |
| 2 | 24 |
| 4 | 27 |
| 5 | 28 |
| 6 | 24 |

These counts apply rules 8.6–8.7: each exact interface quotation counts as one word, “10 minutes” counts as one word, and step numbers are excluded. Established multi-word terms such as “Tenant ID” and “data steward” are not automatically single counting units. The semicolons do not divide the original sentences into separate sentences.

**Meaning questions that need resolution**

- **What does the ten-minute limit measure?** Step 4 says, “If the export doesn't finish within 10 minutes,” while the second note includes “preparation, export processing, and the download itself.” The start point and the event that counts as completion are unclear. These statements might define different limits or one shared limit. Under rule 4.1, this ambiguity matters because it changes when the analyst must cancel and notify.
- **Which approval permits which action?** Step 1 requires approval “from the data steward,” step 2 requires the request record to show “Approved,” and the closing paragraph permits sharing “only after data-steward approval.” It is unclear whether these are evidence of one approval or separate approvals. Rules 4.1 and 9.4 support clarifying the relationship and using consistent wording if they refer to the same authorization.
- **What does “checked” include, and when can the ticket close?** Step 5 requires verification that the file opens. The first note requires a Tenant ID comparison. Step 6 permits closure after “the file has been checked.” Under rule 4.1, the unspecified check and closing actor leave the closure prerequisites unclear.
- **How strong is “should”?** “You should keep the browser open” and “the analyst should record” could express recommendations or intended requirements. Their force must be established before any revision to imperative wording. Changing advice into an obligation would change the process.
- **Which identifiers must match?** “If they do not match” follows a comparison of “the Tenant ID in the downloaded file” with “the approved request.” The intended comparison is understandable in outline, but the corresponding request field is not explicit. Rule 4.1 and recommendation GR-3 support identifying the comparison operands. The supplied facts do not establish the field name.

**Vocabulary uncertainty and justified exceptions**

The supplied terms “Tenant ID,” “data steward,” “service log,” and “request record” have established status in this fictional organization. Rule 1.8 supports retaining established terminology. That does not establish dictionary approval for every surrounding word or verb form under rules 1.1–1.4.

Computing uses of “export” and “download” may qualify as technical nouns or technical verbs under rules 1.5 and 1.12. Their exact use still needs contextual assessment. Words such as “obtain,” “verify,” and “authorizes” are unverified here, not declared prohibited. No alternative is asserted to be dictionary-approved.

“During incident INC-317, an export was deleted” is descriptive passive voice with an explicitly unidentified actor. Rule 3.6 permits that exception. “Downloaded file” is a participial modifier, not automatically a passive-voice violation under rule 3.3. Likewise, the ending in “export processing” does not alone establish an action-form violation under rule 3.5.

The exact labels “Approve & Export,” “Approved,” and “Don't close; export running” must remain unchanged. Their internal wording and punctuation are not authored-text findings. No descriptive sentence exceeds the 25-word limit in rule 6.3.

## Evidence

See [execution metadata and file hashes](manifest.json). Display headings are nested and application writing-block wrappers are omitted here; the response wording is unchanged. Exact responses are retained in [outputs/](outputs/), and original prompts in [inputs/](inputs/). Reviewer assessments were written by the primary assistant after execution, not by a human expert.
