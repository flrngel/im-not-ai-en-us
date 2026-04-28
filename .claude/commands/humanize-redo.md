---
description: Re-run the most recent Humanize US result with targeted instructions
argument-hint: [adjustment, e.g. "less casual", "only fix the intro", "keep headings", "more concise"]
---

# /humanize-redo — targeted second pass

Find the newest `_workspace/{run_id}/` in the current repo and rerun only the necessary part of the `humanize-english-us` pipeline.

## User instruction

$ARGUMENTS

## Behavior

1. Locate the most recent run directory. If none exists, tell the user to start with `/humanize`.
2. Parse the instruction:
   - **range**: intro, conclusion, paragraph number, selected heading;
   - **category**: stock vocabulary, hedging, list structure, passives, formatting;
   - **tone**: less casual, more direct, more formal, more concise;
   - **rollback**: revert a named edit or all assertive edits;
   - **format**: preserve headings, preserve bullets, remove bullets.
3. Use the previous output and summary as context.
4. Run the smallest safe pass.
5. Save versioned output: `03_rewrite_v2.md`, `final_v2.md`, `summary_v2.md`.
6. Stop at round 3. After that, recommend human review.

## Safety line

Do not add facts or examples to make prose more “human.” Ask for source material if the draft needs concrete detail.
