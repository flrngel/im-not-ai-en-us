---
description: Rewrite AI-sounding English into natural US English while preserving meaning
argument-hint: [text or file path] [genre: business|academic|blog|op-ed|email|web-copy|public] [intensity: conservative|standard|assertive] [mode: fast|strict]
---

# /humanize — US English naturalization pipeline

Invoke the `humanize-english-us` skill on the supplied text or file path.

## Input

$ARGUMENTS

## Behavior

1. If no argument is provided, ask the user to paste the text or provide a `.txt` / `.md` path.
2. If the argument is a readable file path, load that file. Otherwise treat the argument as the input text.
3. Parse trailing options:
   - `genre: business|academic|blog|op-ed|email|web-copy|public`
   - `intensity: conservative|standard|assertive`
   - `min_severity: S1|S2|S3`
   - `mode: fast|strict`
4. Start `humanize-english-us`.
5. Create `_workspace/{YYYY-MM-DD-NNN}/` and save `01_input.txt`.
6. Use fast mode unless the input is long, high-risk, or the user requested strict mode.
7. Return final edited text, pattern summary, grade, 3–5 representative before/after edits, and any fidelity warnings.

## Safety line

Do not describe the result as undetectable or detector-proof. Say it is a naturalized, human-edited US-English draft.
