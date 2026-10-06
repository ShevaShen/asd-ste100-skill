This is an **STE-guided validation of the original draft**. Full dictionary compliance was not assessed. The report distinguishes supported writing-rule findings from questions about meaning and unverified vocabulary. No rewrite is supplied.

The opening paragraph is descriptive. The numbered steps are procedural, although step 3 contains advice whose intended force is unclear. The first two notes contain required actions or limits; the third note is descriptive. The closing paragraph mixes a recommendation, optional information, permission, and a prohibition.

### Clear writing-rule findings

| Location and excerpt | Rule | Finding and practical consequence |
|---|---|---|
| Opening paragraph, from “The service log contains operational events” through “The available evidence does not identify who or what deleted it” | **6.6** | The paragraph contains eight sentences, exceeding the six-sentence limit. Its length makes the separate facts harder to scan. |
| Same paragraph: log contents, export operation and availability, then “During incident INC-317…” | **6.5** | The paragraph combines several topics, including an incident account. The incident information interrupts the general description of the export process. |
| Step 1: “Don't start…”; step 4: “doesn't finish” | **4.2** | These authored contractions violate the rule against contractions. This finding does not apply to the exact quoted interface message. |
| Step 1: “request record; compare…”; step 5: “requester; never attach…” | **8.1** | These authored semicolons violate the punctuation rule. They also join distinct instructions that the analyst must track separately. |
| Steps 1, 2, 4, 5, and 6 | **5.1** | These procedural sentences exceed 20 words. Counts and counting assumptions appear below. |
| Step 1: “Don't start…; compare… and obtain approval…” | **5.2** | One sentence combines the start restriction, comparison, and approval action. Their sequence is difficult to follow as separate checks. |
| Step 2: “Select… and start the export…” | **5.2** | Selecting the date range and starting the export are separate actions, with no stated simultaneity. Combining them makes the approval condition easier to overlook. |
| Step 4: “cancel it and notify… but do not submit…” | **5.2** | Cancellation, notification, and the restriction on another export share one sentence. The draft does not establish that these actions occur simultaneously. |
| Step 5: “Save… verify… and send…; never attach…” | **5.2** | Saving, checking, sharing, and the attachment prohibition are combined. This increases the chance that an analyst skips a check or overlooks the prohibition. |
| Step 6: “The request record is to be updated by the duty analyst…” | **5.3**, **3.6**, **3.4** | The required update uses a passive, indirect auxiliary construction instead of an imperative. The actor is supplied, so uncertainty about the actor does not justify the passive construction. |
| Step 2: “…start the export… if the request record shows ‘Approved’” | **5.4** | The condition needed before starting the export appears after the command. An analyst could encounter the action before its prerequisite. |
| Step 1: “have reviewed”; step 3: “has completed”; step 6: “has been checked”; third note: “has been downloaded” | **3.2** | These are perfect-tense constructions, which the permitted tense framework excludes. The descriptive status of the third note does not exempt it from this rule. |
| Step 3: “is being displayed” | **3.2**, **3.6** | This is a progressive passive construction in procedural text. It expresses an ongoing action, rather than merely describing a condition with a past-participle adjective. |
| Step 2: “by selecting”; first note: “before sharing” | **3.5** | These “-ing” constructions express actions. They are not technical nouns or modifiers within technical nouns. |
| First note: “You must compare…” and “If they do not match…” | **5.5** | The note contains a mandatory comparison, a sharing restriction, and a notification action. The procedure cannot safely omit this note: step 5 otherwise directs sharing without this comparison. These requirements belong in the operative procedure. |
| First note: “You must compare…” | **5.3** | This is an explicit mandatory action rather than optional advice, but it is not imperative. |
| First note: “do not share the link and notify the data steward” | **5.2**, **4.1** | The sentence combines a prohibition and a positive action. Its construction also leaves room for a reader to misunderstand the scope of “do not,” particularly whether notification is required. |
| Second note: “The download must be completed within 10 minutes” | **5.5** | This is a required result and time limit inside a note. Treating notes as dispensable would remove an operational constraint. |
| Closing paragraph: “Operators must not change the retention period” | **5.3** | This is a mandatory procedural prohibition expressed as a declarative sentence instead of an imperative. |

The procedural sentence counts are **24 words in step 1, 24 in step 2, 27 in step 4, 28 in step 5, and 24 in step 6**. These counts apply rules **8.6–8.7**: each quoted interface string counts as one word, “10 minutes” counts as one word, and step numbers do not count. Established terms such as “Tenant ID” retain their constituent word counts; being an established technical term does not itself make the term one word. The semicolons do not end the sentences for counting purposes.

### Meaning questions and operational uncertainties

- **What does each ten-minute limit measure?** Step 4 says, “If the export doesn't finish within 10 minutes.” The second note says the download must finish within ten minutes, including “preparation, export processing, and the download itself.” The start point for either clock is not defined, and “export” could have a narrower scope than the overall process. Clarification is needed under **4.1** to determine when cancellation applies and what happens when the overall limit is exceeded.
- **Is keeping the browser open advice or a requirement?** Step 3 says, “you should keep the browser open,” while the exact interface message says, “Don't close; export running.” The draft does not establish whether the message and the advice cover the same period or whether closing the browser interrupts the download. The force of “should” is a meaning question, not a definite **5.3** violation.
- **Is the handover record optional advice or a required record?** “The analyst should record the export creation time and any cancellation” does not establish a mandatory action. No definite **5.3** violation follows from “should” alone. This matters because step 6 already requires an update but does not identify its required contents.
- **What does approval authorize?** Step 1 requires data-steward approval, step 2 requires the request record to show “Approved,” and the closing paragraph permits sharing only after data-steward approval. The draft does not expressly establish whether these are the same approval or whether the quoted status records that approval. This is a material clarity question under **4.1**; the report does not assume an additional approval is required.
- **What permits ticket closure?** In step 6, “after the file has been checked” does not identify the check, while “the ticket can then be closed” does not make all closure prerequisites explicit. It is unclear whether the file-opening check, Tenant ID comparison, sharing, and record update must all be complete. This warrants clarification under **4.1**. “Can” may express permission, so non-imperative wording alone does not establish a **5.3** violation for ticket closure.

### Vocabulary uncertainty and text that should be preserved

The supplied terms “Tenant ID,” “data steward,” “service log,” and “request record” are established terminology. They should not be rejected merely because this workflow lacks the full dictionary. Computing uses such as “export” and “download” can potentially qualify under the technical-noun and technical-verb provisions of **1.5** and **1.12**, but category membership does not establish every use or form as approved. Exact dictionary meanings, grammatical roles, and permitted forms remain unverified under **1.1–1.4**.

The quoted labels “Approve & Export,” “Approved,” and “Don't close; export running” must remain exact. The contraction and semicolon inside the last label are not authored-text violations.

“An export was deleted” is acceptable as descriptive passive voice under **3.6** because the following sentence explicitly says the actor is unknown. No actor should be invented. Similarly, “downloaded file,” “restricted case folder,” and “approved request” are not automatically passive-voice violations merely because they contain participles used as modifiers (**3.3**).

The third note provides descriptive information about availability and removal; it does not contain a hidden instruction. Its perfect tense is a finding, but its placement as a note is not itself a **5.5** violation. “A screenshot is optional” and “Requesters may receive…” express optionality and permission, respectively; neither should be converted into a mandatory instruction by interpretation.
