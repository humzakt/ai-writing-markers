---
license: mit
language:
- en
language_creators:
- expert-generated
annotations_creators:
- expert-generated
multilinguality:
- monolingual
source_datasets:
- original
pretty_name: AI Writing Markers
tags:
- ai-detection
- ai-generated-text
- llm
- llm-detection
- gpt
- chatgpt
- machine-generated-text
- writing
- writing-style
- text-analysis
- linguistics
- stylometry
- academic-integrity
- content-moderation
- lexicon
- word-list
- burstiness
- perplexity
- wikipedia
- ai-cleanup
task_categories:
- text-classification
task_ids:
- acceptability-classification
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: markers.jsonl
---

# ai-writing-markers

A curated, source-backed catalogue of textual markers associated with AI-generated
(LLM) writing, plus a small dependency-free Python checker that scans your text for
them.

Use it to **audit and edit your own drafts**, to teach what "AI voice" looks like,
or as a machine-readable dataset ([`markers.json`](markers.json)) for other tools.

> [!WARNING]
> **This is not an AI detector.** These markers are *weak* signals, not proof of
> authorship. Independent studies report false-positive rates from roughly 5% to
> over 60% on genuine human writing, with non-native English speakers and formal
> academic prose hit hardest (Liang et al., *Patterns* 2023). Never use these
> markers, or any tool built on them, as the sole basis for an accusation of
> misconduct. Treat every result as a prompt for a closer human read.

## Why this exists

Most "AI detectors" are opaque and unreliable. The useful, honest thing a tool
*can* do is point at the concrete patterns that make writing *read* as
machine-generated so a human can decide whether to change them. Those patterns are
well documented, especially by Wikipedia's [WikiProject AI
Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup), whose
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
field guide is the single best public reference on the subject. This repo distills
that guide and other 2026 sources into a structured, cited dataset.

## What's inside

| File | Purpose |
|------|---------|
| [`markers.json`](markers.json) | The dataset. 6 categories, 87+ markers, each with notes and source ids. Source of truth. |
| [`markers.jsonl`](markers.jsonl) | Flattened, one-row-per-marker view (powers the HF dataset viewer). Generated from `markers.json`. |
| [`check.py`](check.py) | Zero-dependency CLI that scans a file against `markers.json`. |
| [`SOURCES.md`](SOURCES.md) | Every source, with links. |
| [`data/`](data/) | Human-readable explainers per category. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to add or correct a marker. |
| [`space/`](space/) | Gradio app for a Hugging Face Space (needs PRO to host). |
| [`space-static/`](space-static/) | Static, client-side Space (free to host) — the deployed one. |
| [`HUGGINGFACE.md`](HUGGINGFACE.md) | How to publish as an HF Dataset and Space. |

## Marker categories

1. **Overused vocabulary** — words like `delve`, `tapestry`, `underscore`, `pivotal`,
   `robust`, `leverage`. Overused sets drift by model era (e.g. `delve` peaked in
   2023–early 2024 and faded by 2025), so `markers.json` tags each with an `era`.
2. **Formulaic transitions / signposting** — `moreover`, `furthermore`,
   `additionally` (especially opening a sentence), `in conclusion`.
3. **Cliche phrases and stock shells** — `it is important to note that`,
   `in today's fast-paced world`, `a testament to`, `navigating the landscape`.
4. **Structural and rhetorical tells** — the Rule of Three, negative parallelisms
   ("not only X but Y"), vague attribution ("studies show"), outline-like
   "challenges and future prospects" conclusions, bold-header inline lists,
   relentless hedging.
5. **Punctuation and formatting tells** — spaced em dashes, curly quotes, mechanical
   over-bolding, title-case headings, emoji-as-bullets, and leftover chatbot markup
   (`contentReference`, `oaicite`, `turn0search0`).
6. **Statistical signals** — low **perplexity** (predictable word choice) and low
   **burstiness** (uniform sentence length), the two metrics classical detectors
   lean on.

## Also on Hugging Face

- **Live demo (Space):** https://huggingface.co/spaces/humzakt/ai-writing-markers — a
  browser-only checker; paste text and scan, nothing leaves your machine.
- **Dataset:** https://huggingface.co/datasets/humzakt/ai-writing-markers — the marker
  catalogue as a reusable dataset.

The deployed Space is **static** (client-side JS), because Hugging Face requires a PRO
plan to host Gradio Spaces on the free tier. A Gradio version lives in [`space/`](space/);
the static one is in [`space-static/`](space-static/). See [`HUGGINGFACE.md`](HUGGINGFACE.md)
for publishing steps.

## Install

No dependencies. Python 3.8+.

```bash
git clone https://github.com/humzakt/ai-writing-markers.git
cd ai-writing-markers
```

## Usage

```bash
# Scan a file
python3 check.py essay.md

# Pipe from stdin
cat essay.txt | python3 check.py -

# Machine-readable output
python3 check.py essay.md --json
```

Example (an intentionally AI-flavoured sentence):

```text
$ echo "In today's fast-paced world, we must delve into the rich tapestry of innovation." | python3 check.py -
  Overused vocabulary: 2 hit(s)
      - delve: 1
      - tapestry: 1
  Cliche phrases and stock shells: 2 hit(s)
      - in today's fast-paced world: 1
      - rich tapestry: 1
```

### Reading the report

- **burstiness** = standard deviation of sentence length / mean. Human prose is
  commonly 0.65–0.85; AI prose often falls below 0.30. Raise it by mixing very short
  sentences (3–8 words) with long ones (35+).
- **per-1000-words density** matters more than raw counts. A handful of hits in a
  long document is ordinary human writing; a dense cluster in a short passage is the
  real signal.
- **perplexity cannot be measured here.** True perplexity needs a reference language
  model. The checker reports proxies (type-token ratio, sentence-length uniformity)
  and says so.

### Known limitations

- Best on plain prose. On Markdown, tables and `**bold**` labels will legitimately
  trip the boldface and structural checks, and the naive sentence splitter treats a
  table as one long "sentence," which skews burstiness. Strip formatting first for
  the cleanest read.
- String matching is literal and case-insensitive; it does not understand meaning,
  so it cannot judge tone, hedging quality, or factual grounding.
- The dataset reflects English LLM output as of mid-2026 and will age.

## How to actually improve a draft

Swapping flagged words for synonyms does **not** work; synonyms are also
high-probability, and it does nothing for burstiness. What works:

1. Vary sentence length deliberately, throughout, not in one paragraph.
2. Replace generic claims with specific, named detail and examples.
3. Cut stock shells and state the point directly.
4. Take an actual position instead of hedging both ways.
5. Break parallel structures and the Rule of Three.

See each file in [`data/`](data/) for the reasoning and citations behind a category.

## License

Code: [MIT](LICENSE). Data (`markers.json`, `data/`): CC0-1.0 (public domain).
The underlying observations are drawn from public sources credited in
[`SOURCES.md`](SOURCES.md); Wikipedia content is CC BY-SA.

## Contributing

Markers evolve with models. PRs that add, retire, or re-date markers are welcome,
as long as each change cites a source. See [`CONTRIBUTING.md`](CONTRIBUTING.md).
