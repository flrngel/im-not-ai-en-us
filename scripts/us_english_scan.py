#!/usr/bin/env python3
"""Surface scanner for Humanize US.

This script does not detect authorship. It reports editable surface cues:
stock LLM phrases, connector density, sentence-length variation, bullets,
headings, passive markers, nominalizations, and punctuation habits.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Iterable

STOCK_TERMS = [
    "delve", "delving", "navigate", "leverage", "harness", "unlock", "empower",
    "optimize", "revolutionize", "transformative", "groundbreaking", "cutting-edge",
    "robust", "seamless", "comprehensive", "nuanced", "pivotal", "crucial",
    "landscape", "ecosystem", "framework", "paradigm", "intricacies", "complexities",
    "valuable insights", "shed light", "play a crucial role", "significant contribution",
    "important to note", "today's fast-paced", "digital landscape", "wide range of",
    "various stakeholders", "numerous benefits", "opportunities and challenges",
]

FRONT_CONNECTORS = [
    "furthermore", "moreover", "additionally", "therefore", "consequently",
    "ultimately", "in conclusion", "in summary", "on the other hand", "however",
]

PASSIVE_RE = re.compile(
    r"\b(?:is|are|was|were|be|been|being)\s+([a-z]+ed|made|done|seen|known|built|written|created|implemented|conducted)\b",
    re.IGNORECASE,
)

NOMINALIZATION_RE = re.compile(r"\b[a-z]{5,}(?:tion|sion|ment|ness|ity|ance|ence|ization|isation)\b", re.IGNORECASE)
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])")
WORD_RE = re.compile(r"\b[\w'-]+\b")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+", re.MULTILINE)
BULLET_RE = re.compile(r"^\s*(?:[-*+] |\d+[.)] |✅|🚀|💡|⚠️)", re.MULTILINE)


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def sentences(text: str) -> list[str]:
    chunks = [s.strip() for s in SENTENCE_RE.split(text.strip()) if s.strip()]
    return chunks if chunks else ([text.strip()] if text.strip() else [])


def count_phrases(text: str, phrases: Iterable[str]) -> Counter[str]:
    low = text.lower()
    counts: Counter[str] = Counter()
    for phrase in phrases:
        pattern = r"\b" + re.escape(phrase.lower()) + r"\b"
        n = len(re.findall(pattern, low))
        if n:
            counts[phrase] = n
    return counts


def front_connector_count(sents: list[str]) -> int:
    count = 0
    for s in sents:
        start = re.sub(r"^[\"'“”‘’\s]+", "", s.lower())
        if any(start.startswith(c) for c in FRONT_CONNECTORS):
            count += 1
    return count


def stdev(values: list[int]) -> float:
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return math.sqrt(sum((v - mean) ** 2 for v in values) / (len(values) - 1))


def scan(text: str) -> dict:
    w = words(text)
    sents = sentences(text)
    sent_lengths = [len(words(s)) for s in sents]
    avg = sum(sent_lengths) / len(sent_lengths) if sent_lengths else 0.0
    sd = stdev(sent_lengths)
    cv = (sd / avg) if avg else 0.0
    stock = count_phrases(text, STOCK_TERMS)
    connector_fronts = front_connector_count(sents)
    passive = PASSIVE_RE.findall(text)
    nominalizations = NOMINALIZATION_RE.findall(text)
    bullets = BULLET_RE.findall(text)
    headings = HEADING_RE.findall(text)
    em_dashes = text.count("—")
    word_count = len(w)
    per_1000 = lambda n: round((n / word_count) * 1000, 2) if word_count else 0.0

    warnings = []
    if per_1000(sum(stock.values())) > 12:
        warnings.append("High stock-phrase density")
    if len(sents) >= 6 and cv < 0.35:
        warnings.append("Low sentence-length variation")
    if connector_fronts >= 3:
        warnings.append("Many sentence-opening formal connectors")
    if em_dashes > 2:
        warnings.append("Em-dash overuse")
    if len(bullets) >= 6 and len(bullets) > len(sents) / 2:
        warnings.append("Bullet-heavy structure")

    return {
        "word_count": word_count,
        "sentence_count": len(sents),
        "avg_sentence_words": round(avg, 2),
        "sentence_length_stdev": round(sd, 2),
        "sentence_length_cv": round(cv, 3),
        "stock_phrase_counts": dict(stock.most_common()),
        "stock_phrases_per_1000_words": per_1000(sum(stock.values())),
        "front_connectors": connector_fronts,
        "front_connectors_per_1000_words": per_1000(connector_fronts),
        "passive_markers": len(passive),
        "passive_markers_per_1000_words": per_1000(len(passive)),
        "nominalizations": len(nominalizations),
        "nominalizations_per_1000_words": per_1000(len(nominalizations)),
        "bullet_lines": len(bullets),
        "headings": len(headings),
        "em_dashes": em_dashes,
        "warnings": warnings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan US English text for surface AI-sounding cues.")
    parser.add_argument("path", type=Path, help="Text or Markdown file to scan")
    parser.add_argument("--json", action="store_true", help="Print raw JSON")
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    result = scan(text)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    print("Humanize US surface scan")
    print("-" * 32)
    for key in [
        "word_count", "sentence_count", "avg_sentence_words", "sentence_length_stdev",
        "sentence_length_cv", "stock_phrases_per_1000_words", "front_connectors",
        "passive_markers", "nominalizations", "bullet_lines", "headings", "em_dashes",
    ]:
        print(f"{key}: {result[key]}")
    if result["stock_phrase_counts"]:
        print("\nstock phrases:")
        for phrase, count in result["stock_phrase_counts"].items():
            print(f"  {phrase}: {count}")
    if result["warnings"]:
        print("\nwarnings:")
        for warning in result["warnings"]:
            print(f"  - {warning}")


if __name__ == "__main__":
    main()
