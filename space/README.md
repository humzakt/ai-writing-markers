---
title: AI Writing Markers
emoji: 🔎
colorFrom: green
colorTo: blue
sdk: gradio
app_file: app.py
pinned: false
license: mit
short_description: Scan text for documented AI-writing markers. Not a detector.
---

# AI Writing Markers (Hugging Face Space)

Interactive demo of [ai-writing-markers](https://github.com/humzakt/ai-writing-markers).
Paste text and see which documented AI-writing markers it contains, plus a real
burstiness metric.

**This is not an AI detector.** Markers are weak signals, not proof of authorship.
Detection tools are biased against non-native and academic writing. Use results only
as a prompt for a closer human read.

This Space reuses `check.py` and `markers.json` from the main repository, so the demo
and the CLI stay in sync. Configuration reference:
https://huggingface.co/docs/hub/spaces-config-reference
