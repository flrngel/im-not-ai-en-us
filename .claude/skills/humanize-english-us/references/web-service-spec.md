# Humanize US Web Service Spec

Load this only when designing or implementing a browser-based version.

## Product concept

A web editor that helps users turn AI-sounding English drafts into natural US English while preserving meaning.

## Core screens

1. **Input**: paste text or upload `.txt` / `.md`; choose genre and intensity.
2. **Findings**: highlighted spans grouped by category A–J.
3. **Rewrite diff**: side-by-side original and edited text; each edit has a reason.
4. **Fidelity review**: protected spans and meaning warnings.
5. **Final copy**: clean output plus summary.

## Responsible-use language

Use:

- “Improve readability and naturalness.”
- “Review changes before using in high-stakes contexts.”
- “This tool does not determine authorship.”

Do not use:

- “Undetectable.”
- “Bypass AI detectors.”
- “Guaranteed human.”
- “Passes Turnitin/GPTZero/etc.”

## API design

### `POST /api/detect`

Input:

```json
{
  "text": "...",
  "genre": "business",
  "minSeverity": "S2"
}
```

Output: detection JSON matching `ai-tell-detector`.

### `POST /api/rewrite`

Input:

```json
{
  "text": "...",
  "findings": [],
  "genre": "business",
  "intensity": "standard",
  "preserveFormatting": true
}
```

Output:

```json
{
  "rewrite": "...",
  "diff": [],
  "changeRate": 0.18
}
```

### `POST /api/audit`

Input: original, rewrite, diff.

Output: fidelity audit.

### `POST /api/review`

Input: rewrite, original findings, options.

Output: naturalness review.

## Data model

```ts
type Finding = {
  id: string;
  category: string;
  severity: 'S1' | 'S2' | 'S3';
  span: string;
  start: number;
  end: number;
  reason: string;
  suggestedFix: string;
};

type Edit = {
  findingId: string;
  before: string;
  after: string;
  reason: string;
  meaningRisk: 'low' | 'medium' | 'high';
};
```

## Privacy

- Default: do not store user text after request completion.
- If history is enabled, require sign-in and explicit opt-in.
- Redact logs; never log full documents by default.
- Add delete-export controls for saved documents.

## Abuse prevention

- Rate-limit by account/IP.
- Block prompts requesting detector evasion, plagiarism concealment, impersonation, or policy circumvention.
- For academic/legal/medical/financial documents, show a human-review warning.

## Implementation notes

- The scanner can run locally for preview metrics, but AI-based rewriting should run server-side.
- Stream detection/rewrite progress for long documents.
- Make every edit reversible in the UI.
- Add a “show only high-risk edits” filter.
