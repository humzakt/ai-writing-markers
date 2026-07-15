# What Wikipedia's editors learned

Since 2023, volunteers at [WikiProject AI
Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) have reviewed
thousands of flagged articles and drafts and written the most evidence-based public
guide to spotting AI text: [Signs of AI
writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). A few of their
hard-won principles are worth copying, because they keep you honest.

## Method beats vibes

- **Check the date first.** Text present before 30 November 2022 (ChatGPT's release) is
  almost never LLM-generated; anything clearly pre-2018 can be ruled out entirely. Since
  March 2026, Wikipedia's WP:LLM guideline prohibits LLM-generated article content with
  narrow exceptions.
- **Don't trust detectors.** The guide explicitly warns against AI-detection tools for
  their error rates. A 2025 study it cites found even heavy LLM users correctly
  identified AI text only ~90% of the time; casual readers did barely better than
  chance.
- **The signs point to deeper problems.** Editors caution: don't just scrub the surface
  markers, because that only makes detection harder. The real issues are unsourced or
  fabricated claims, source-to-text mismatches, and invented citations. Markers are a
  doorway to those, not the problem itself.

## The catalogue (condensed)

**Content:** undue emphasis on significance/legacy/broader trends; canned emphasis on
notability and media coverage; superficial analysis dressed up as depth; vague
attribution and overgeneralized opinion; outline-like "challenges and future prospects"
conclusions.

**Language:** high density of "AI vocabulary" (delve, tapestry, testament, underscore,
pivotal, robust...); avoidance of plain `is`/`are` copulas; negative parallelisms;
overuse of the Rule of Three; forced "elegant variation."

**Style:** title case everywhere; over-bolding; inline-header vertical lists; emoji as
formatting; unusual table use; spaced em dashes; curly quotes.

**Communication and markup (strong tells):** chatbot pleasantries addressed to the user
("Certainly! Here is..."); knowledge-cutoff disclaimers; unfilled placeholder text;
and leftover reference markup (`contentReference`, `oaicite`, `turn0search0`).

**Citations:** broken external links, invalid DOIs/ISBNs, and DOIs that resolve to
unrelated articles — often because the model fabricated them.

## Fabricated sources are the real danger

The Cleanup project notes that most bad AI content is not simply "unsourced." It cites
real but unrelated sources, invents plausible-looking ones, or attaches a legitimate
source to a claim it does not support. When you find AI text, verify the citations
before anything else.

Full guide (CC BY-SA):
https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
