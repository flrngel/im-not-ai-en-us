# US English AI-Sounding Pattern Taxonomy v0.1

This is the single source of truth for English (US) naturalization. It lists common patterns that make drafts read like generic LLM output. A pattern is an editing cue, not proof of AI authorship.

## Severity

- **S1 critical**: strong cue; edit unless protected by genre, quote, citation, or required language.
- **S2 high**: edit when repeated or clustered.
- **S3 low**: weak cue; edit only when it compounds other signals.

## Protected spans

Never flag or edit inside:

- direct quotes;
- citation titles, URLs, DOIs, statutes, case names;
- product/model/organization names;
- numeric expressions, formulas, tables of data;
- legal, medical, financial, or technical terms that are required in context.

---

## A. Meta-disclaimers and throat-clearing

### A-1. AI self-reference [S1]
- Pattern: “As an AI language model,” “I don’t have personal experiences,” “I cannot browse the internet” left in user-facing prose.
- Fix: delete if irrelevant; replace with the actual limitation only if the final text needs it.
- False positives: chatbot transcript, policy analysis about AI systems.

### A-2. “It is important to note” framing [S2]
- Pattern: “It is important to note that…,” “It should be noted that…,” “Worth noting is that…”
- Fix: delete the frame and state the point directly.

### A-3. Empty era openers [S2]
- Pattern: “In today’s fast-paced digital world,” “In an era of rapid technological advancement.”
- Fix: start with the concrete subject.

### A-4. Preview-the-paper boilerplate [S2]
- Pattern: “This essay will explore,” “In this blog post, we will discuss.”
- Fix: either delete or replace with a direct thesis.

### A-5. Generic caveat wrapper [S3]
- Pattern: “While there are many factors to consider…” without naming them.
- Fix: name the factor if already present; otherwise simplify.

---

## B. Stock LLM vocabulary and prestige adjectives

### B-1. LLM-favored verbs [S2]
- Pattern: delve, explore, unpack, navigate, leverage, harness, unlock, empower, optimize, revolutionize, transform.
- Fix: choose the plain verb that matches the sentence: explain, use, improve, change, make faster, make easier.
- False positives: exact source titles; “leverage” in finance/physics; “optimize” in engineering/math.

### B-2. LLM-favored adjectives [S2]
- Pattern: robust, seamless, comprehensive, nuanced, transformative, groundbreaking, innovative, cutting-edge, pivotal, crucial.
- Fix: delete if empty; replace with a specific property if the draft already gives one.

### B-3. Academic-flavored filler nouns [S2]
- Pattern: landscape, implications, considerations, framework, paradigm, ecosystem, complexities, intricacies.
- Fix: use the concrete noun: market, effect, issue, method, system, details.

### B-4. “Valuable insights” family [S2]
- Pattern: “provide valuable insights,” “shed light on,” “play a crucial role,” “make a significant contribution.”
- Fix: state the actual insight/contribution if present; otherwise tighten.

### B-5. Density of prestige words [S2 document-level]
- Pattern: 5+ stock words per 500 words, especially in introductions and conclusions.
- Fix: prioritize deletion over synonym swapping.

---

## C. Mechanical structure and list cadence

### C-1. First/second/third formula [S1]
- Pattern: “First… Second… Third…” with near-identical sentence shapes.
- Fix: keep the list if useful but vary the transitions; convert some items into prose.

### C-2. Generic intro/body/conclusion signposting [S2]
- Pattern: “Introduction,” “Benefits,” “Challenges,” “Conclusion” headings in short prose.
- Fix: delete headings in essays/emails/blogs; make headings specific in reports.

### C-3. Bullet overuse [S2]
- Pattern: 3+ bullet blocks where prose would be natural.
- Fix: keep bullets only for scannable instructions or actual lists.

### C-4. One-sentence section summaries [S2]
- Pattern: “This section examines…” after every heading.
- Fix: remove and start the section.

### C-5. Symmetric paragraph template [S2]
- Pattern: each paragraph has topic sentence → explanation → generic implication.
- Fix: vary openings; merge or cut repeated implication sentences.

### C-6. Key-takeaway labels [S3]
- Pattern: “Key takeaway:”, “Bottom line:” repeated.
- Fix: keep one if the genre benefits; otherwise fold into prose.

---

## D. Generic abstraction and low-specificity claims

### D-1. “Various/numerous/wide range” [S2]
- Pattern: “various stakeholders,” “numerous benefits,” “a wide range of applications.”
- Fix: name the items if present; otherwise use “several” or remove the phrase.

### D-2. Empty benefit stacks [S2]
- Pattern: “improve efficiency, productivity, and innovation” without mechanism.
- Fix: keep only the benefits the draft supports.

### D-3. Generic actor nouns [S3]
- Pattern: “individuals,” “organizations,” “stakeholders,” “users” where a concrete group is known.
- Fix: restore the actual actor from context.

### D-4. Unsupported magnitude [S2]
- Pattern: “significant,” “substantial,” “major,” “dramatic” without evidence.
- Fix: delete or tie to stated evidence.

### D-5. Empty “both opportunities and challenges” [S2]
- Pattern: balanced but content-free duality.
- Fix: name the opportunity/challenge or cut.

---

## E. Rhythm and sentence-shape uniformity

### E-1. Low sentence-length variation [S2 document-level]
- Pattern: many sentences of similar medium length, especially 18–28 words.
- Fix: mix short emphasis sentences, longer explanatory sentences, and occasional fragments where genre allows.

### E-2. Paragraph monotony [S2]
- Pattern: every paragraph is 3–4 similar sentences.
- Fix: allow variation: one tight paragraph, one longer paragraph, one transition sentence.

### E-3. No human pressure points [S3]
- Pattern: no concrete nouns, contrast, tension, aside, or priority signal.
- Fix: add no new facts; instead foreground the clearest existing claim.

### E-4. Over-smooth transitions [S3]
- Pattern: every sentence flows too neatly from the last.
- Fix: remove some transitions; let adjacent sentences carry the relationship.

### E-5. All-short-sentence staccato [S2]
- Pattern: “Concise” prompt created only short sentences.
- Fix: combine where logic belongs together.

---

## F. Over-hedging and modal stacking

### F-1. Modal pileup [S1]
- Pattern: “may potentially be able to,” “could possibly help,” “might perhaps.”
- Fix: choose one level of uncertainty.

### F-2. Unnecessary “can help” [S2]
- Pattern: repeated “can help,” “may help,” “has the potential to.”
- Fix: use direct verbs when the claim is already supported.

### F-3. Vague attribution [S3]
- Pattern: “many experts believe,” “some argue,” “research suggests” with no source in a source-sensitive context.
- Fix: preserve if source exists; otherwise avoid pretending the claim is sourced.

### F-4. Soft conclusion [S3]
- Pattern: “it seems likely that” before an obvious conclusion.
- Fix: state the conclusion plainly or keep uncertainty if evidence is limited.

---

## G. Passive, nominalized, and bureaucratic prose

### G-1. Passive with hidden actor [S2]
- Pattern: “The decision was made,” “the report was conducted,” “changes were implemented.”
- Fix: restore actor if known; otherwise use a tighter passive.

### G-2. Nominalization chain [S2]
- Pattern: “the implementation of the optimization of the process.”
- Fix: turn nouns back into verbs.

### G-3. “Utilization/implementation/application” bloat [S2]
- Pattern: “the utilization of X,” “the implementation of Y.”
- Fix: “using X,” “doing Y,” “putting Y in place.”

### G-4. Abstract subject + vague verb [S2]
- Pattern: “This development highlights/provides/underscores/brings…”
- Fix: make the real subject do the real action.

### G-5. Corporate/bureaucratic prepositional pile [S3]
- Pattern: “in relation to,” “with regard to,” “in the context of.”
- Fix: “about,” “for,” “in,” or deletion.

---

## H. Connector and transition overuse

### H-1. Formal connector chain [S2]
- Pattern: paragraph starts in sequence with “Furthermore,” “Moreover,” “Additionally,” “Consequently,” “Ultimately.”
- Fix: delete most; use plain transitions only where needed.

### H-2. Redundant causal labels [S3]
- Pattern: “therefore” where causality is obvious.
- Fix: delete.

### H-3. Repeated contrast labels [S3]
- Pattern: “however”/“on the other hand” every paragraph.
- Fix: use “but,” “still,” or sentence order.

### H-4. Over-explained summary/conclusion [S2]
- Pattern: “In summary,” “To conclude,” “Ultimately,” stacked in final paragraph.
- Fix: delete labels and let the conclusion do the work.

---

## I. Punctuation, formatting, and visual cues

### I-1. Em-dash habit [S2]
- Pattern: multiple em dashes used for emphasis in ordinary prose.
- Fix: use a comma, colon, parentheses, or sentence break. Keep one or two if effective.

### I-2. Colon subtitle formula [S2]
- Pattern: “Main idea: Why it matters” across many headings.
- Fix: write specific headings without repeated formula.

### I-3. Excessive bolding [S2]
- Pattern: bold keywords every sentence.
- Fix: keep bold only for headings, UI copy, or one important term.

### I-4. Emoji/checkmark list markers [S1 outside social/marketing]
- Pattern: ✅ 🚀 💡 ⚠️ in professional, academic, or essay text.
- Fix: remove or replace with plain bullets.

### I-5. Table overuse [S3]
- Pattern: table used where a short paragraph is clearer.
- Fix: keep tables for comparisons; otherwise prose.

---

## J. Over-balanced rhetoric

### J-1. Repeated “not only…but also” [S2]
- Pattern: formula used more than once.
- Fix: use one clause or a plainer sentence.

### J-2. Mirrored binaries [S2]
- Pattern: “X or Y?”, “A vs. B,” “for leaders…, for teams…” repeated.
- Fix: vary sentence structure or make one side the main point.

### J-3. Three-part crescendo [S2]
- Pattern: “faster, smarter, and more efficient” / “clarity, confidence, and control.”
- Fix: keep the strongest item or use a concrete pair.

### J-4. Over-neat concession [S3]
- Pattern: “While X is true, Y is also important” repeated.
- Fix: make the contrast specific or use a direct “but.”

### J-5. Generic rhetorical question [S3]
- Pattern: “So, what does this mean for the future?”
- Fix: answer directly unless the genre benefits from the question.
