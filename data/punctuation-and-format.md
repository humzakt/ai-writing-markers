# Punctuation and formatting tells

Each of these is a *weak* signal with legitimate human uses. They matter in
combination, and some (leftover markup) are far stronger than others.

## Em dashes

Human writers use em dashes (—). LLMs use them more often than nonprofessional
human text of the same genre, and in places where a comma, colon, or parentheses would
be normal. AI em dashes are usually **spaced** ( — ), against most typographic style
guides, and deployed in a formulaic "punched-up" way. Weak on its own; the spacing and
frequency together are the signal.

## Curly quotes and apostrophes

ChatGPT and DeepSeek default to curly quotes (" " ' ') and the curly apostrophe (').
Gemini and Claude usually do not. But curly quotes are *also* produced by Microsoft
Word, macOS/iOS, and professional typesetting, so alone they prove nothing. Inconsistent
mixing of curly and straight within one document is more suspicious than either alone.

## Over-bolding

Mechanically bolding every key term, "key takeaways" style, inherited from readmes,
listicles, and sales decks. Newer models are sometimes instructed against it.

## Title case everywhere

Every heading in Title Case rather than sentence case, uniformly, is a mild tell in
contexts where humans write sentence-case headings.

## Emoji as formatting

Checkmarks, rockets, and stars used as list bullets.

## Leftover chatbot markup (strong)

Reference and markup bugs pasted straight from a chat UI are among the most reliable
tells: `contentReference`, `oaicite`, `oai_citation`, `turn0search0`, `:::writing`,
`attached_file`. These essentially never appear in genuine hand-written text.

## Fix

Match the surrounding document's conventions. Use em dashes sparingly and per your style
guide's spacing rule. Normalize quotes. Bold for genuine structural emphasis only. And
always scrub pasted output for stray markup.

Source of truth: [`../markers.json`](../markers.json).
