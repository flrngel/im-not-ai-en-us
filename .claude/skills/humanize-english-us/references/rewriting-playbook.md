# US English Rewriting Playbook

Use this after detection. The goal is a natural, human-edited US-English draft with the same meaning.

## 0. Prime directives

1. **Do not add facts.** If the draft lacks evidence or concrete detail, tighten the language and flag the gap.
2. **Do not change claims.** “Can” is not the same as “will”; “some” is not “most.”
3. **Do not erase uncertainty that matters.** Reduce stacked hedges, not valid caution.
4. **Prefer deletion over synonym swapping.** AI-ish prose often has too many words, not the wrong thesaurus word.
5. **Preserve genre.** Academic prose can be formal; business prose can be direct; email can be warm.
6. **Keep one human imperfection.** Avoid making every sentence maximally polished.

## 1. Core recipes

### A. Throat-clearing

| AI-sounding draft | Better US English |
|---|---|
| It is important to note that the policy applies to contractors. | The policy applies to contractors. |
| In today’s fast-paced digital landscape, teams need better tools. | Teams need better tools. |
| This article will explore three reasons costs are rising. | Costs are rising for three reasons. |
| As an AI language model, I cannot… | Delete, unless it is a transcript. |

### B. Stock vocabulary

| Pattern | Safer move |
|---|---|
| delve into | look at / examine / explain |
| leverage | use / draw on / take advantage of |
| unlock | make possible / open up / enable |
| empower | give someone the ability/tools to |
| robust | strong / reliable / well-tested, only if supported |
| seamless | smooth / connected / without extra steps, only if supported |
| transformative | delete unless the change is actually transformative |
| crucial/pivotal | important / central, or delete if obvious |
| landscape/ecosystem | market / field / system / context |
| complexities/intricacies | details / trade-offs / moving parts |

### C. Mechanical lists

- Keep bullets for instructions, requirements, checklists, comparisons, or dense specs.
- Convert decorative bullets into prose.
- Break the “first/second/third” pattern by using one direct sentence, one transition, and one short emphasis sentence.

Example:

```text
First, AI can reduce manual tasks. Second, it can improve decision-making. Third, it can enhance collaboration.
```

Better:

```text
AI can reduce manual work and make decisions easier to compare. It can also help teams share the same information instead of chasing updates across tools.
```

Only use this if the combined sentence preserves all original claims.

### D. Generic abstraction

- “Various stakeholders” → name the stakeholders if already named; otherwise “the people involved.”
- “Numerous benefits” → “several benefits,” or cut.
- “A wide range of applications” → “many uses,” or name the uses if present.
- “Significant impact” → “impact,” unless a metric supports “significant.”

Do not invent examples to make the draft more concrete. Put missing-concreteness notes in `summary.md`.

### E. Rhythm

Use rhythm to make the prose feel edited, not theatrical.

- Add short sentences only where they sharpen a point.
- Combine choppy short sentences when logic belongs together.
- Remove some transitions so the paragraph breathes.
- Avoid fake personality: no jokes, slang, personal anecdotes, or metaphors unless the source draft already has them.

### F. Hedging

| Draft | Better |
|---|---|
| may potentially be able to reduce costs | may reduce costs / can reduce costs |
| could possibly help teams improve | could help teams improve |
| has the potential to streamline | could streamline / streamlines, depending on certainty |
| it seems likely that demand will grow | demand is likely to grow |

### G. Passive and nominalizations

| Draft | Better |
|---|---|
| The implementation of the system was completed by the team. | The team implemented the system. |
| The utilization of automation can improve accuracy. | Automation can improve accuracy. |
| A decision was made to delay the launch. | The team decided to delay the launch. |
| This development underscores the importance of planning. | This makes planning more important. |

Keep passive voice when the actor is unknown, legally sensitive, or less important than the action.

### H. Connectors

- Delete “Furthermore,” “Moreover,” and “Additionally” when adjacent sentences already show addition.
- Use “but” instead of repeated “however” in less formal genres.
- Remove “in conclusion” from final paragraphs unless it is a speech or school essay where signposting is expected.

### I. Formatting

- Use em dashes sparingly. If a draft has more than two per page, convert most to commas, colons, parentheses, or sentence breaks.
- Remove decorative emoji from professional, academic, public, legal, medical, and financial text.
- Remove bold from ordinary body prose. Keep bold for UI labels, headings, or one critical term.
- Convert tables to prose unless comparison is the point.

### J. Balanced rhetoric

| Pattern | Better move |
|---|---|
| not only X but also Y | X and Y / X also Y |
| faster, smarter, and more efficient | choose strongest, or keep two if distinct |
| opportunity and challenge | name each side or cut |
| What does this mean for the future? | State the implication directly |

## 2. Genre tuning

| Genre | Natural target | Avoid |
|---|---|---|
| Business memo | direct, concrete, action-oriented | hype, vague “innovation” language |
| Academic/report | formal, precise, citation-sensitive | casual slang, unsupported simplification |
| Blog | clear, conversational, lightly varied | corporate gloss, over-structured lists |
| Op-ed | assertive, rhythmic, specific | fake neutrality, “both sides” padding |
| Email | concise, warm, useful | excessive polish, long preambles |
| Web copy | benefit-led, plain, scannable | buzzwords, exaggerated claims |
| Public statement | careful, credible, controlled | over-casual tone, invented detail |

## 3. Diff and change-rate guidance

- `<5% changed`: likely under-edited unless the source was already good.
- `5–30%`: preferred range.
- `30–50%`: review for over-editing and meaning drift.
- `>50%`: stop; use strict mode and explain why.

## 4. Summary notes

When the rewrite cannot safely fix a problem, say so:

- “The draft is vague here; I did not invent examples.”
- “This claim needs a source if used in academic or public-facing copy.”
- “The sentence can be tightened further, but that would change the claim.”
