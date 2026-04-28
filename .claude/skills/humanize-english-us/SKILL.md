---
name: humanize-english-us
description: Rewrite AI-sounding English into natural US English through span-grounded detection, surgical editing, fidelity audit, and naturalness review.
---

# Humanize US Skill

This skill edits AI-sounding English into natural **US English**. It is an editorial system, not a detector-bypass system.

## Trigger phrases

Use this skill when the user asks for any of:

- “humanize this”
- “make this sound less AI-written”
- “rewrite in natural American English”
- “remove AI tone”
- “make it sound like a human edited it”
- “less ChatGPT-ish”
- “more natural, same meaning”

Do not trigger when the user asks for a brand-new article, fiction, translation, or fact-heavy rewrite unless they also ask to preserve an existing draft.

## Inputs

```json
{
  "input_text": "...",
  "genre_hint": "business | academic | blog | op-ed | email | web-copy | public | null",
  "intensity": "conservative | standard | assertive",
  "min_severity": "S1 | S2 | S3",
  "mode": "fast | strict | auto"
}
```

## Phase 0 — setup

1. Create `_workspace/{YYYY-MM-DD-NNN}/`.
2. Save input as `01_input.txt` exactly.
3. Infer genre if missing:
   - business memo: direct, professional, action-oriented;
   - academic/report: formal, citation-sensitive, no invented claims;
   - blog/op-ed: conversational but not slangy;
   - email: concise, relationship-aware;
   - web copy: benefit-led, concrete, low filler;
   - public statement: polished, careful, reputationally safe.
4. Decide mode:
   - fast: under ~5,000 words, low risk;
   - strict: long text, citations, regulated/high-stakes content, user requests strict, or major structural work.

## Fast mode

Call `humanize-monolith` with:

- `input_path`: `_workspace/{run_id}/01_input.txt`
- `quick_rules_path`: `.claude/skills/humanize-english-us/references/quick-rules.md`
- parsed options.

Expected outputs:

- `final.md`
- `summary.md`

Fast mode must still run its own fidelity self-check and must not exceed the change-rate guardrails.

## Strict mode

### Phase 1 — detect

Call `ai-tell-detector`.

Output: `_workspace/{run_id}/02_detection.json`

### Phase 2 — rewrite

Call `english-style-rewriter` with the original text and detection findings.

Output:

- `_workspace/{run_id}/03_rewrite.md`
- `_workspace/{run_id}/03_rewrite_diff.json`

### Phase 3 — parallel review

Call both:

- `content-fidelity-auditor`
- `naturalness-reviewer`

Outputs:

- `_workspace/{run_id}/04_fidelity_audit.json`
- `_workspace/{run_id}/05_naturalness_review.json`

### Phase 4 — decision

| Condition | Action |
|---|---|
| No fidelity issues; grade A/B | accept |
| Residual S1/S2 but no meaning risk | rewrite_round_2 |
| Any meaning drift | rollback_and_rewrite |
| Change rate > 50%, high-stakes uncertainty, or repeated failure | hold_and_report |

Maximum rewrite rounds: 3.

## Output format to user

Return:

1. The final edited text.
2. A compact table: detected categories before/after.
3. Grade (`A`, `B`, `C`, `D`) and one-sentence explanation.
4. 3–5 before/after examples.
5. Any fidelity caveats.

Avoid long process narration. Do not say “detector-proof,” “undetectable,” or “will pass AI detection.”
