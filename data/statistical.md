# Statistical signals: perplexity and burstiness

Classical detectors (and the earliest, most transparent ones) lean on two numbers.

## Perplexity

How *surprised* a reference language model is by each next word. LLMs pick
high-probability words, so their output has **low perplexity**. Human writers reach for
words a model would not default to — memory, rhythm, specificity, humor — producing
**higher perplexity**. As a rough guide some 2026 write-ups cite: under ~20 reads as
almost certainly machine, above ~50 as almost certainly human. Treat those as
indicative, not gospel.

**You cannot compute true perplexity without a language model.** This repo's
`check.py` does not pretend to. It reports proxies — type-token ratio and
sentence-length uniformity — and labels them as proxies. Do not read the checker's
output as a perplexity score.

## Burstiness

Variation in sentence length and complexity across a passage. The common metric is the
**standard deviation of sentence length divided by the mean**.

- Human prose commonly scores **0.65–0.85**.
- Default AI prose often falls **below 0.30**, clustering around **15–22 words** per
  sentence, paragraph after paragraph.

`check.py` computes exactly this ratio, so its burstiness number is real (subject to the
naive sentence splitter's limits — Markdown tables will distort it).

## Why synonym-swapping fails

Replacing flagged words with synonyms barely moves perplexity (synonyms are also
high-probability) and does nothing to burstiness. Reordering sentences moves neither.
The only thing that works is rewriting at the distribution level.

## What actually raises both

- **Burstiness:** after a cluster of 3–4 medium sentences, drop one very short sentence
  (3–8 words), then one long one (35+). Fragments are allowed. Do it throughout — the
  metric is computed over the whole text, so one bursty paragraph in a flat document
  barely registers.
- **Perplexity:** specific nouns, concrete named examples, the word you would actually
  say to a colleague rather than the "safe" one, a real stance instead of hedging.

## The caveat that matters most

These same signals are why detectors are biased. Formal academic prose and
second-language writing are naturally low-perplexity and low-burstiness, so genuine
human work by those writers is disproportionately misflagged (Liang et al., *Patterns*
2023: 61.3% of real TOEFL essays flagged, vs 5.1% for native speakers). Low scores are a
reason to write with more variation, never a verdict on authorship.

Citations: [`../SOURCES.md`](../SOURCES.md).
