---
title: AI Writing Markers
emoji: 🔎
colorFrom: green
colorTo: blue
sdk: static
app_file: index.html
pinned: false
license: mit
short_description: Scan text for documented AI-writing markers. Not a detector.
---

# AI Writing Markers (Static Space)

A client-side demo of [ai-writing-markers](https://github.com/humzakt/ai-writing-markers).
Everything runs in your browser: paste text and see which documented AI-writing markers
it contains, plus a real burstiness metric. No server, no data leaves your machine.

**This is not an AI detector.** Markers are weak signals, not proof of authorship.
Detection tools are biased against non-native and academic writing. Use results only
as a prompt for a closer human read.

This static Space is used because Hugging Face requires a PRO subscription to host
Gradio Spaces on the free tier. A Gradio version of the same tool lives in the
[`space/`](https://github.com/humzakt/ai-writing-markers/tree/main/space) folder of the
GitHub repo for anyone who prefers it.
