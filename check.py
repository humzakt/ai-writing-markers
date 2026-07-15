#!/usr/bin/env python3
"""
ai-writing-markers checker.

Scans a text file for the markers catalogued in markers.json and prints a
report. This is a transparency and self-editing aid, NOT an AI detector.
Presence of markers is a weak signal, never proof of authorship.

Usage:
    python3 check.py path/to/file.txt
    python3 check.py path/to/file.md --json
    cat file.txt | python3 check.py -
"""

import argparse
import json
import os
import re
import sys
from statistics import mean, pstdev

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "markers.json")

# Categories matched as literal words/phrases rather than by a custom regex.
LEXICAL_CATEGORIES = {"vocabulary", "transitions", "phrases"}


def load_markers(path=DATA):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def split_sentences(text):
    # Deliberately simple: split on ., !, ? followed by whitespace.
    # Good enough for length statistics; not a full NLP tokenizer.
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def word_count(text):
    return len(re.findall(r"\b[\w'-]+\b", text))


def find_lexical(term, text, sentence_start=False):
    """Return list of matched surface strings for a word/phrase term."""
    escaped = re.escape(term).replace(r"\ ", r"\s+")
    if sentence_start:
        # Start of string or after sentence-ending punctuation / newline.
        pattern = r"(?:(?<=^)|(?<=[.!?]\s)|(?<=\n))" + escaped + r"\b"
    elif re.match(r"\w", term):
        pattern = r"\b" + escaped + r"\b"
    else:
        pattern = escaped
    return re.findall(pattern, text, flags=re.IGNORECASE | re.MULTILINE)


def rule_of_three_hits(text):
    # "a, b, and c" / "a, b and c" style triples.
    pat = r"\b[\w-]+,\s+[\w-]+,?\s+(?:and|or)\s+[\w-]+\b"
    return re.findall(pat, text, flags=re.IGNORECASE)


def analyze(text, markers):
    n_words = max(word_count(text), 1)
    sentences = split_sentences(text)
    lengths = [word_count(s) for s in sentences] or [0]

    results = {"categories": [], "stats": {}}

    for cat in markers["categories"]:
        cid = cat["id"]
        hits = []

        if cid in LEXICAL_CATEGORIES:
            for m in cat["markers"]:
                found = find_lexical(
                    m["term"], text, sentence_start=(m.get("position") == "sentence_start")
                )
                if found:
                    hits.append({"term": m["term"], "count": len(found)})

        elif cid in ("structural", "punctuation_format"):
            for m in cat["markers"]:
                rgx = m.get("regex")
                if not rgx:
                    continue
                try:
                    found = re.findall(rgx, text, flags=re.IGNORECASE | re.MULTILINE)
                except re.error:
                    continue
                if found:
                    hits.append({"term": m["term"], "count": len(found)})
            if cid == "structural":
                r3 = rule_of_three_hits(text)
                if r3:
                    hits.append({"term": "rule_of_three", "count": len(r3)})

        total = sum(h["count"] for h in hits)
        results["categories"].append(
            {
                "id": cid,
                "label": cat["label"],
                "total_hits": total,
                "per_1000_words": round(total / n_words * 1000, 2),
                "hits": sorted(hits, key=lambda h: -h["count"]),
            }
        )

    m_len = mean(lengths)
    burstiness = round(pstdev(lengths) / m_len, 3) if m_len else 0.0
    tokens = re.findall(r"\b[\w'-]+\b", text.lower())
    ttr = round(len(set(tokens)) / max(len(tokens), 1), 3)

    results["stats"] = {
        "words": n_words,
        "sentences": len(sentences),
        "mean_sentence_length": round(m_len, 1),
        "min_sentence_length": min(lengths),
        "max_sentence_length": max(lengths),
        "burstiness": burstiness,
        "type_token_ratio": ttr,
    }
    return results


def burstiness_verdict(b):
    if b >= 0.6:
        return "human-typical (>=0.65 is common in human prose)"
    if b >= 0.4:
        return "middling; consider more sentence-length variation"
    return "low; AI-typical. Vary sentence length aggressively"


def print_report(res):
    s = res["stats"]
    line = "=" * 64
    print(line)
    print("  ai-writing-markers report")
    print("  NOT an AI detector. Markers are weak signals, not proof.")
    print(line)
    print(f"  words: {s['words']}   sentences: {s['sentences']}")
    print(
        f"  sentence length  mean {s['mean_sentence_length']}  "
        f"min {s['min_sentence_length']}  max {s['max_sentence_length']}"
    )
    print(f"  burstiness: {s['burstiness']}  ->  {burstiness_verdict(s['burstiness'])}")
    print(f"  type-token ratio: {s['type_token_ratio']} (higher = more varied vocab)")
    print(line)

    grand_total = 0
    for cat in res["categories"]:
        grand_total += cat["total_hits"]
        header = f"  {cat['label']}: {cat['total_hits']} hit(s)"
        if cat["total_hits"]:
            header += f"  ({cat['per_1000_words']}/1k words)"
        print(header)
        for h in cat["hits"]:
            print(f"      - {h['term']}: {h['count']}")
    print(line)
    print(f"  total marker hits: {grand_total}")
    print("  Interpretation: clustering matters more than any single hit.")
    print("  A few hits in a long document is normal human writing.")
    print(line)


def main():
    ap = argparse.ArgumentParser(description="Scan text for AI-writing markers.")
    ap.add_argument("file", help="text/markdown file to scan, or - for stdin")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--markers", default=DATA, help="path to markers.json")
    args = ap.parse_args()

    if args.file == "-":
        text = sys.stdin.read()
    else:
        with open(args.file, "r", encoding="utf-8") as fh:
            text = fh.read()

    markers = load_markers(args.markers)
    res = analyze(text, markers)

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print_report(res)


if __name__ == "__main__":
    main()
