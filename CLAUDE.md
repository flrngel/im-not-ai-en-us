# Humanize US — Claude Code Project Guide

## Project overview

Humanize US is a Claude Code harness for converting AI-sounding English into natural, edited **US English** while preserving meaning. It uses a taxonomy of English-specific LLM writing cues, a span-grounded rewrite pass, a content-fidelity audit, and a naturalness review.

The project must never claim that output is “undetectable.” Treat AI-sounding patterns as editorial signals, not proof of authorship.

## Prime directives

1. **Fidelity first**: preserve facts, numbers, dates, citations, names, claims, quotes, logical order, and causality.
2. **Span-grounded edits**: do not rewrite untouched prose simply because it could be more stylish.
3. **US English target**: spelling, punctuation, idiom, and register should follow American English unless the user requests otherwise.
4. **Genre match**: preserve the user’s genre and audience.
5. **No over-polish**: a slightly imperfect human-edited draft is better than a glossy generic rewrite.
6. **No detector-evasion framing**: report naturalness and readability, not “bypass” status.

## Directory structure

```text
im-not-ai-en-us/
├── CLAUDE.md
├── README.md
├── .claude/
│   ├── agents/
│   │   ├── ai-tell-detector.md
│   │   ├── english-style-rewriter.md
│   │   ├── content-fidelity-auditor.md
│   │   ├── naturalness-reviewer.md
│   │   ├── humanize-monolith.md
│   │   ├── english-ai-tell-taxonomist.md
│   │   └── humanize-web-architect.md
│   ├── commands/
│   │   ├── humanize.md
│   │   └── humanize-redo.md
│   └── skills/humanize-english-us/
│       ├── SKILL.md
│       └── references/
│           ├── ai-tell-taxonomy.md
│           ├── quick-rules.md
│           ├── rewriting-playbook.md
│           ├── research-foundation.md
│           └── web-service-spec.md
├── scripts/
│   ├── us_english_scan.py
│   └── make_thumbnail.py
└── assets/
    └── social-preview.png
```

## Pipeline

```text
input
  ↓
[fast under ~5,000 words]
  humanize-monolith → final.md + summary.md

[strict for long/high-risk work]
  ai-tell-detector → english-style-rewriter
    → content-fidelity-auditor + naturalness-reviewer
    → accept | rewrite_round_2 | rollback_and_rewrite | hold_and_report
```

## Severity

- **S1 critical**: strong, high-confidence AI-sounding cue; remove unless genre demands it.
- **S2 high**: acceptable once or twice; problematic in clusters.
- **S3 low**: weak cue; only edit when several signals overlap.

## Quality grades

- **A**: S1 = 0, S2 ≤ 2, no fidelity issues, no over-polish.
- **B**: S1 = 0, S2 ≤ 4, minor style issues remain.
- **C**: S1 1–2 or over-polish/fidelity warning; needs another pass.
- **D**: serious meaning risk, heavy generic tone remains, or output changed too much.

## High-risk contexts

For legal, medical, financial, academic, admissions, hiring, disciplinary, or regulated texts:

- preserve citations and required wording exactly;
- do not add claims, sources, anecdotes, or examples;
- mark uncertain edits in `summary.md`;
- use strict mode by default;
- recommend human review if any meaning risk remains.

## References

- Main taxonomy: `.claude/skills/humanize-english-us/references/ai-tell-taxonomy.md`
- Fast rules: `.claude/skills/humanize-english-us/references/quick-rules.md`
- Rewrite recipes: `.claude/skills/humanize-english-us/references/rewriting-playbook.md`
- Research notes: `.claude/skills/humanize-english-us/references/research-foundation.md`
