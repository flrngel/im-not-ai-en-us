# Contributors

This repository is an English (US) adaptation of the original Korean Humanize KR prompt harness. It keeps the same architectural idea—taxonomy → span detection → surgical rewrite → fidelity audit → naturalness review—but rebuilds the pattern library for American English.

## Design principles for contributors

1. Add patterns only when they are observable across multiple real drafts.
2. Prefer precise, edit-safe rules over broad “make it sound human” instructions.
3. Never add a rule that encourages detector evasion or authorship deception.
4. Every rewrite rule must preserve facts, claims, names, citations, and quoted text.
5. Add new rules to both the full taxonomy and the fast-path quick rules only when they are common enough for fast mode.

## How to propose a new pattern

Add a note with:

- pattern ID proposal;
- example span;
- why it sounds AI-like in US English;
- severity (`S1`, `S2`, or `S3`);
- safe rewrite recipe;
- false-positive cases where it should not be edited.
