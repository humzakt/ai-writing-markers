# Overused vocabulary

Detectors and human reviewers both notice that certain words appear in LLM output far
more often than in comparable human writing. A 2024 *Scientific Reports* analysis found
`delve` rose more than 25x in some academic fields after ChatGPT's release. Paul Graham
half-joked that a single `delve` is now a near-tell.

Key facts to keep in mind:

- **One instance means nothing.** These are ordinary English words. The signal is
  *clustering*: three or four in a short passage.
- **The set drifts by model era.** Wikipedia's editors track this explicitly:
  - *2023 – mid-2024 (GPT-4 era):* additionally, boasts, bolstered, crucial, delve,
    emphasizing, enduring, garner, intricate/intricacies, interplay, key, landscape,
    meticulous, pivotal, underscore, tapestry, testament, valuable, vibrant.
  - *mid-2024 – mid-2025 (GPT-4o era):* align with, bolstered, crucial, emphasizing,
    enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore,
    vibrant.
  - `delve` peaked early and dropped off sharply through 2025.
- **Models differ.** Grok over-produces pseudo-scientific words (causal, empirical,
  correlate) and still overuses `underscore` in 2026. Gemini and Claude differ again.
- **Synonyms are not implicated.** `delve` being overused does not make `explore`
  overused. Do not blind-swap; that just trades one generic word for another.

## Fix

Prefer the plain word. Replace inflated verbs (`leverage` → `use`, `utilize` → `use`)
and abstract nouns (`the landscape of X` → name the actual thing) with concrete,
specific language. Replace adjectives with evidence: "transformative" says nothing;
"cut onboarding from three days to two hours" does.

Source of truth for the term list: [`../markers.json`](../markers.json). Citations in
[`../SOURCES.md`](../SOURCES.md).
