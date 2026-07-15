# Phrases, transitions, and structural tells

Vocabulary is the surface. The stronger, harder-to-fake tells are structural.

## Formulaic transitions

LLMs stack connectors between nearly every sentence, especially at the start:
`Moreover`, `Furthermore`, `Additionally` (flagged most when it opens a sentence),
`Consequently`, `Notably`, `Importantly`, `In conclusion`. Human writers let logical
order carry much of the flow and reach for a connective only when the logic genuinely
turns. Delete most of them.

## Stock shells

Fixed multi-word templates that recur regardless of topic: `it is important to note
that`, `it is worth noting that`, `in today's fast-paced world`, `when it comes to`,
`navigating the landscape of`, `a testament to`, `plays a pivotal role`, `the
transformative power of`. Cut the shell and state the point.

## Copula avoidance

LLMs dodge plain `is`/`are`: "the temple **stands as** a counter-symbol,"
"the report **serves as** a reminder." Where "is" is true, use it.

## The Rule of Three

LLMs overuse triples — "adjective, adjective, adjective" or "short phrase, short
phrase, and short phrase" — to make shallow analysis look thorough. One triple is
fine; a document built on them is a tell.

## Negative parallelisms

"Not only X but Y," "It's not X, it's Y," "no X, no Y, just Z." Cheap emphasis that
LLMs lean on. Vary or cut.

## Vague attribution and overgeneralization

"Studies show," "experts agree," "research suggests" with no citation. Either cite it
or drop the appeal to authority.

## Outline-like conclusions

Endings that pivot to a canned "challenges and future prospects" summary, restating the
body in parallel bullets. Real conclusions say something the body did not.

## Inline-header lists and over-bolding

Chat output loves the "**Bold header:** description" list item and bolding every key
term in a "key takeaways" style. Fine in a slide deck; a tell in prose.

Source of truth: [`../markers.json`](../markers.json). Citations:
[`../SOURCES.md`](../SOURCES.md), primarily Wikipedia's
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
