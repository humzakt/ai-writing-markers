# Contributing

The markers here track a moving target: LLM output changes with every model release.
Corrections and additions are welcome.

## Ground rules

1. **Cite a source for every change.** Add or reuse an entry in the `sources` array of
   [`markers.json`](markers.json) and reference its `id` on the marker. No source, no
   merge.
2. **A word being AI-overused does not implicate its synonyms.** Add the specific term
   that is documented, not a thesaurus expansion of it.
3. **Respect context and era.** Tag vocabulary markers with an `era` (e.g.
   `2023-mid2024`) when usage is time-bound. Note when a term is model-specific (e.g.
   Grok's `underscore`).
4. **Keep the honest framing.** Nothing in this repo should claim to "detect AI." It
   flags patterns; humans judge.

## Adding a marker

Edit [`markers.json`](markers.json). Each marker is an object inside a category's
`markers` array:

```json
{ "term": "delve", "kind": "word", "era": "2023-mid2024", "note": "why it's notable", "sources": ["wikipedia_aisigns"] }
```

- `kind`: `word`, `phrase`, `pattern` (regex-backed), or `metric`.
- `position` (optional): `sentence_start` for signposting words flagged mainly when
  they open a sentence.
- `regex` (optional): for structural/punctuation patterns. It must compile under
  Python's `re`.

## Validate before opening a PR

```bash
python3 -c "import json,re; d=json.load(open('markers.json')); [re.compile(m['regex']) for c in d['categories'] for m in c['markers'] if m.get('regex')]; print('ok')"
python3 check.py README.md   # smoke test
```

## Retiring a marker

Do not delete history silently. If a term has clearly fallen out of use, either narrow
its `era` or move it with a `note` explaining the change and the source that shows the
decline.
