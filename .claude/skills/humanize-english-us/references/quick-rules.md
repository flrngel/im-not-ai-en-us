# Quick Rules — Humanize US Fast Path v0.1

Slim rulebook for `humanize-monolith`. Use this for fast, conservative edits. The full taxonomy is `ai-tell-taxonomy.md`.

**Protected spans:** quotes, citations, URLs, DOIs, legal/statutory text, numbers, dates, formulas, product/model/org names, technical terms required by context.

**Change guard:** >30% changed = warn and self-review; >50% changed = stop/rollback.

## A. Meta and throat-clearing

| ID | Pattern | Severity | Safe fix |
|---|---|---:|---|
| A-1 | “As an AI language model…” | S1 | Delete unless transcript/policy context |
| A-2 | “It is important to note…” | S2 | Delete frame; state point directly |
| A-3 | “In today’s fast-paced digital world…” | S2 | Start with the concrete subject |
| A-4 | “This essay/post will explore…” | S2 | Delete or use direct thesis |

## B. Stock LLM vocabulary

| ID | Pattern | Severity | Safe fix |
|---|---|---:|---|
| B-1 | delve, navigate, leverage, harness, unlock, empower | S2 | Plain verb: explain/use/improve/change |
| B-2 | robust, seamless, comprehensive, nuanced, transformative, pivotal | S2 | Delete or replace with specific property already present |
| B-3 | landscape, ecosystem, framework, paradigm, intricacies | S2 | Concrete noun if clear; otherwise simplify |
| B-4 | “provide valuable insights,” “shed light on,” “play a crucial role” | S2 | State actual contribution or tighten |

## C. Structure

| ID | Pattern | Severity | Safe fix |
|---|---|---:|---|
| C-1 | First/second/third formula | S1 | Vary transitions; convert some list items to prose |
| C-2 | Generic intro/benefits/challenges/conclusion headings | S2 | Remove or make headings specific |
| C-3 | Too many bullets | S2 | Keep only useful lists |
| C-4 | “This section examines…” | S2 | Delete |

## D. Generic abstraction

| ID | Pattern | Severity | Safe fix |
|---|---|---:|---|
| D-1 | various/numerous/wide range | S2 | Name items if present; otherwise cut/soften |
| D-2 | efficiency/productivity/innovation stacks | S2 | Keep supported benefits only |
| D-4 | significant/substantial/major/dramatic without evidence | S2 | Delete or tie to stated evidence |
| D-5 | opportunities and challenges boilerplate | S2 | Name specifics or cut |

## E. Rhythm

| ID | Pattern | Severity | Safe fix |
|---|---|---:|---|
| E-1 | Similar sentence lengths throughout | S2 | Mix short and longer sentences, genre permitting |
| E-2 | Same paragraph shape repeatedly | S2 | Vary paragraph length/opening |
| E-5 | All short staccato sentences | S2 | Combine where logic belongs together |

## F. Hedging

| ID | Pattern | Severity | Safe fix |
|---|---|---:|---|
| F-1 | “may potentially be able to” | S1 | One uncertainty marker only |
| F-2 | Repeated “can help” / “has the potential to” | S2 | Direct verb when supported |
| F-3 | “research suggests” without source in source-sensitive text | S3 | Avoid fake sourcing; preserve real citations |

## G. Passive and nominalization

| ID | Pattern | Severity | Safe fix |
|---|---|---:|---|
| G-1 | Passive hides known actor | S2 | Restore actor if known |
| G-2 | Nominalization chain | S2 | Turn nouns into verbs |
| G-3 | utilization/implementation/application of | S2 | use / do / put in place |
| G-4 | abstract subject + “highlights/provides/underscores” | S2 | Real subject + real action |

## H. Connectors

| ID | Pattern | Severity | Safe fix |
|---|---|---:|---|
| H-1 | Furthermore/Moreover/Additionally chain | S2 | Delete most; use plain transition if needed |
| H-2 | Redundant therefore/consequently | S3 | Delete |
| H-4 | In summary/To conclude/Ultimately stacked | S2 | Delete labels |

## I. Formatting

| ID | Pattern | Severity | Safe fix |
|---|---|---:|---|
| I-1 | Em-dash overuse | S2 | Comma/colon/parentheses/sentence break |
| I-2 | Repeated colon headings | S2 | Specific headings |
| I-3 | Excessive bold | S2 | Remove most bold |
| I-4 | Emoji/checkmark bullets in professional prose | S1 | Remove |

## J. Balanced rhetoric

| ID | Pattern | Severity | Safe fix |
|---|---|---:|---|
| J-1 | Repeated “not only…but also” | S2 | Plainer sentence |
| J-2 | Mirrored binaries repeated | S2 | Vary structure |
| J-3 | Three-part crescendo | S2 | Keep strongest item or concrete pair |
