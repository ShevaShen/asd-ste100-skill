---
name: asd-ste100
description: Rewrite or review technical and operational English using a self-contained distillation of ASD-STE100 Issue 9. Use for STE-guided NORMALIZE or VALIDATE work without external files, dictionary lookups, or tools.
---

# ASD-STE100: self-contained writing skill

Use the instructions in this file and the user's text. Do not open a PDF, read
reference files, run scripts, browse, or look up dictionary entries during use.
The user can supply terminology, definitions, or additional source excerpts in
the conversation. Apply this skill across subject fields.

This is a compact, paraphrased writing guide derived from Issue 9 (2025-01-15).
It does not contain the complete STE dictionary. Apply the writing rules below,
but do not represent a familiar English word as STE-approved from memory.
Word approval depends on meaning, part of speech, and permitted forms.
Call the result **STE-guided**, not certified or fully dictionary-validated STE.
Mention this boundary briefly when reporting a validation or when the user asks
for strict compliance. Do not add a repetitive disclaimer to every rewrite.

## Choose the operation

**NORMALIZE** means draft or rewrite. Return the revised text first. Give a short
explanation or unresolved questions only when they help the user.

**VALIDATE** means assess the original without rewriting it. Report specific
findings with excerpts and the rule IDs below. Distinguish clear writing-rule
violations from possible vocabulary or meaning issues. Do not treat an unknown
word as prohibited. State that full dictionary compliance was not assessed.

If the user requests both, assess the original, give the revision separately,
and review the revision. Do not substitute a rewrite for a requested assessment.

Before either operation:

- Identify procedural passages, descriptive passages, and safety instructions.
  Classify a note by its function, even when it occurs inside a procedure.
- Preserve facts, actors, quantities, units, identifiers, negation, exceptions,
  sequence, dependencies, and the strength of obligations or permissions.
- Preserve fixed labels, interface strings, quotations, and official names.
- Ask for clarification when missing information would change the technical
  meaning. Do not invent an actor, hazard, condition, or required action.

These preservation and reporting instructions are this skill's operating
conventions. They are not additional numbered STE rules.

## Vocabulary and technical terms — rules 1.1–1.14

STE vocabulary comprises dictionary-approved words, technical nouns, and
technical verbs (1.1). Use dictionary-approved words only in their specified
grammatical roles (1.2) and meanings (1.3). Use only the approved forms of verbs
and adjectives (1.4).

For this lookup-free workflow, favor clear, concrete wording and preserve
necessary domain terminology. Where exact dictionary approval is uncertain,
mark it as unverified if it matters to the assessment. A suggested alternative
must preserve meaning. Do not describe a substitution as officially approved
unless that approval is established by evidence supplied in the conversation.

Technical nouns can fall within these 22 categories (1.5):

1. Items identified in official parts information.
2. Vehicles, machines, and their locations.
3. Tools, support equipment, their components, and their locations.
4. Materials, consumables, and contaminating or unwanted substances.
5. Facilities, infrastructure, and logistics.
6. Systems, circuits, components, configurations, and functions.
7. Mathematics, science, engineering, and formulas.
8. Navigation and geography.
9. Numbers, measurements, time, and their symbols.
10. Fixed quoted text, including interface labels and signs.
11. Professional roles, named persons, groups, organizations, and geopolitical entities.
12. Anatomy and body parts.
13. Personal items, food, and beverages.
14. Medical concepts and terminology.
15. Official documents, document components, standards, and guidance.
16. Environmental and operating conditions.
17. Colors.
18. Damage and deterioration.
19. Computing, information technology, and communications.
20. Civil and military operations, products, services, and support.
21. Legal and regulatory subjects.
22. Animals, plants, and other organisms.

Category membership depends on the actual concept and context. It does not
authorize unrestricted use of every domain-associated word. A non-approved word
can be usable as a technical noun or part of one (1.6). Do not turn a technical
noun into a verb merely because ordinary English permits it (1.7).

Prefer established company, industry, or subject-field nouns (1.8). If a term must
be selected, use a clear, short term (1.9), with no more than three words (2.1).
Avoid regional expressions, slang, and jargon (1.10). Use one term consistently
for the same item (1.11). Colors have a special technical-noun treatment: do not form color
comparatives or superlatives, such as adding “-er” or “-est” (1.5).

Technical verbs are permitted in four categories (1.12):

- Manufacturing: removing, adding, or attaching material, or changing its
  properties, finish, or shape.
- Computing: input/output, interface/application processes, and system operations.
- Applicable specialist fields: engineering/mathematics/science, medicine,
  civil/military operations, navigation, automotive/railway, and energy/oil/gas.
- Legal or regulatory operations within legal or regulatory texts.

Use a technical verb only for the specific process it denotes in that context.
Prefer an approved general construction when it expresses the meaning accurately.
Do not use technical verbs merely to shorten wording or evade vocabulary limits.
Technical verbs follow the same grammar restrictions as other verbs. Do not turn
a technical verb into a noun without the applicable noun authorization (1.13).

Use American spelling unless an applicable official directive requires otherwise.
Do not change the spelling of fixed quoted text (1.14).

## Noun groups — rules 2.1–2.2

Limit multi-word nouns to three words (2.1). An established longer
technical name is an exception requiring careful presentation: give its full
official form first, then explain a clear shorter form or use an approved
abbreviation (2.2). Do not shorten it in a way that changes the item identified.

Hyphens can group words that genuinely operate together. Do not join unrelated
words or create a hyphenated group of more than three words to evade the limit (2.2).
Keep official hyphenation. Do not add unnecessary abbreviations or hyphens to
already clear short terms.

## Verbs and voice — rules 3.1–3.7

- Use permitted verb forms. Ordinary grammatical correctness alone does not
  establish dictionary approval (3.1).
- The permitted framework uses infinitives, imperatives, simple present, simple
  past, simple future, and permitted past participles as adjectives (3.2). Avoid
  perfect and progressive tenses (3.2) and complex auxiliary constructions (3.4).
- A permitted past participle can describe a condition before a noun or after
  a form of “be,” “become,” or “stay.” A condition expressed this way is not
  automatically passive voice. Do not reject every occurrence of “is” plus
  an adjective ending in “-ed” (3.3).
- Do not use “-ing” verb constructions for actions. An “-ing” form can be a
  technical noun or a functional modifier inside a technical noun. There are
  also dictionary-approved words ending in “-ing”; the ending alone is not a
  violation. Examples identified in the source include “during,” “missing,”
  “remaining,” and “something” in their specified roles (3.5).
- Use active voice. Descriptive text can use passive voice when the actor is
  unknown. Do not invent an actor to force active voice. Procedural instructions
  normally use the imperative (3.6).
- Express the main action through a verb rather than burying it in a noun
  construction. Preserve the actual action when simplifying (3.7).

## Sentence construction — rules 4.1–4.5

Make sentences short and unambiguous (4.1). Keep necessary grammar and information:
do not omit required words or use contractions to reduce length (4.2). Use articles
or demonstrative adjectives before nouns where applicable (4.5).

Use vertical lists when they make complex information easier to understand (4.3).
Connect related statements with explicit connecting words or phrases (4.4). Splitting
a sentence must not remove its condition, cause, exception, or logical connection.

## Procedures — rules 5.1–5.5

- Limit each procedural sentence to 20 words using the counting rules below (5.1).
- Give one instruction per sentence. Multiple actions can share a sentence when
  they occur simultaneously; do not split away that simultaneity (5.2).
- Use the imperative for instructions (5.3).
- Put a condition that the reader needs first before the command, then separate
  the condition and command with a comma (5.4).
- Notes give explanatory information, not instructions, requirements, or limits.
  Notes follow descriptive-writing rules. Put required actions, tolerances, and
  results in the relevant work steps, and hazard-prevention information in safety
  instructions. The procedure must still work correctly without its notes (5.5).

## Descriptions — rules 6.1–6.6

- Introduce information gradually (6.1).
- Reuse key terms and connecting phrases to give the text a logical structure (6.2).
- Limit descriptive sentences to 25 words, including descriptive notes in procedures (6.3).
- Group related information in paragraphs. Introduce the topic, then arrange its
  supporting information logically (6.4).
- Give each paragraph only one topic (6.5).
- Use no more than six sentences per paragraph (6.6).

Section 6's introductory guidance distinguishes descriptions from instructions.
Do not turn descriptive information into commands unless the requested function
of the text actually changes.

## Safety instructions — rules 7.1–7.3 and 5.1

- Use the applicable risk identifier, such as a warning or caution, under the
  user's governing conventions (7.1).
- Begin with a clear command or a condition the reader must understand first (7.2).
- Explain the hazard or possible consequence when the information is available (7.3).

Preserve the supplied hazard and severity. Ask about missing technical information;
do not invent it. These are the skill's meaning-preservation conventions.
Safety sentences have the procedural limit of 20 words (5.1). Required safety
content must not be hidden in a note (5.5) or removed merely to shorten a sentence.

## Punctuation and counting — rules 8.1–8.7

Do not use semicolons in authored STE sentences. Use separate sentences instead (8.1).
Use standard punctuation accurately and hyphens only for genuinely related words (8.2).

Parentheses can contain references, identifiers, step designations, abbreviations,
singular/plural notation, explanations, and alternatives (8.3).

For sentence-length checks:

- In a vertical list, the introductory colon ends the introductory sentence for
  counting purposes. Count each subsequent list item separately (8.4).
- A parenthetical group counts as one word in its surrounding sentence. Also
  assess the text inside parentheses as a separate sentence when applicable (8.5).
- Count a number, a number with its measurement unit, an abbreviation, or an
  alphanumeric identifier as one word. Do not count work-step or paragraph
  numbering (8.6).
- Count each fixed quotation, title, heading, placard/label text, or proper name
  of a person, group, organization, or geopolitical entity as one word. Fixed
  quoted content can also be indicated by typography. Formulas count as quoted
  text. Do not assume every capitalized phrase qualifies (8.6).
- A correctly hyphenated word group counts as one word (8.7).

Do not manufacture quotations, names, or hyphens to pass a length check. When
formatting or the identity of a special element is unclear, mark the count as
uncertain rather than report a definite violation from a whitespace count.

## Meaning and consistency — rules 9.1–9.4

Reconstruct a sentence when a word-for-word replacement would change meaning,
grammar, or clarity (9.1). An ordinary meaning of a word is not necessarily its
approved STE meaning. Do not extend an approved meaning by analogy (9.2).

Do not combine individually approved words into a new idiomatic phrasal verb (9.3).
Some phrasal verbs have specific dictionary authorization or qualify as technical
verbs in a particular context; do not claim that all multi-word verbs are banned.
Keep terminology and wording consistent for repeated items and repeated actions (9.4).

## Additional recommendations — GR-1–GR-8

The source distinguishes these recommendations from its numbered writing rules.
Do not report a stylistic preference from this group as a separate numbered-rule
violation without an applicable rule.

- Include “that” where it clarifies the boundary between clauses (GR-1).
- Check “with” for ambiguity about association, accompaniment, or a tool (GR-2).
- Make pronoun referents explicit; repeat the noun when a pronoun is ambiguous (GR-3).
- Use “this” with a noun when needed to make its reference clear (GR-4).
- Avoid meanings transferred incorrectly from similar-looking foreign words (GR-5).
- Prefer clear English expressions to Latin abbreviations (GR-6).
- Use neutral, inclusive wording and respect necessary contextual terminology (GR-7).
- Possessive forms are permitted when clear and correct; they are not contractions (GR-8).

## Final review

Review meaning preservation first, then structure, grammar, consistency,
punctuation, and the applicable word counts. Check conditions and negation again
after splitting or combining sentences. Distinguish a stylistic improvement from
a change in technical requirements.

For NORMALIZE, deliver the usable revision without an unsolicited rule-by-rule
audit. For VALIDATE, report only supported findings and material uncertainties.
Use the specific rule ID identified here for each finding, rather than a whole
section's range. Never claim that every rule or dictionary entry
was checked when working from this distillation.

## Build-time provenance

Derived from the user's ASD-STE100 Issue 9, dated 2025-01-15: Part 1, sections
1–9, PDF pages 45–128; dictionary-use principles, PDF pages 131–148. Rule IDs
above are provenance identifiers, not instructions to retrieve other files.
The full dictionary and its source examples are intentionally not embedded.
This is unofficial, independently worded guidance. ASD has not endorsed or
certified this project. The official standard and dictionary are not included.
The project license grants no rights to ASD publications or trademarks.
