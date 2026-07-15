"""
Gradio demo for ai-writing-markers.

A transparency and self-editing aid, NOT an AI detector. It scans pasted text
against the markers catalogued in markers.json and reports what it finds, plus a
real burstiness metric.

Reuses the analysis logic from check.py so the Space and the CLI stay in sync.
"""

import gradio as gr

from check import analyze, burstiness_verdict, load_markers

MARKERS = load_markers()

EXAMPLE_AI = (
    "In today's fast-paced world, it is important to note that artificial "
    "intelligence stands as a testament to human ingenuity. Moreover, we must "
    "delve into the rich tapestry of innovation. Furthermore, these robust, "
    "seamless, and transformative solutions underscore the importance of "
    "leveraging cutting-edge technology."
)

EXAMPLE_HUMAN = (
    "The counseling office had two chairs and a broken clock. I waited anyway. "
    "Most students never make it that far, and I understood why the moment the "
    "receptionist asked, loudly, what was wrong with me. Stigma is not abstract "
    "here. It has a front desk."
)

DISCLAIMER = (
    "> **This is not an AI detector.** Markers are weak signals, not proof of "
    "authorship. Detection is biased against non-native and academic writing "
    "(up to ~61% false positives in one peer-reviewed study). Use results only "
    "as a prompt for a closer human read."
)


def scan(text):
    if not text or not text.strip():
        return "Paste some text to scan."

    res = analyze(text, MARKERS)
    s = res["stats"]

    lines = [DISCLAIMER, ""]
    lines.append("### Statistics")
    lines.append(f"- **Words:** {s['words']}  |  **Sentences:** {s['sentences']}")
    lines.append(
        f"- **Sentence length:** mean {s['mean_sentence_length']}, "
        f"min {s['min_sentence_length']}, max {s['max_sentence_length']}"
    )
    lines.append(
        f"- **Burstiness:** {s['burstiness']} — {burstiness_verdict(s['burstiness'])}"
    )
    lines.append(
        f"- **Type-token ratio:** {s['type_token_ratio']} "
        "(higher = more varied vocabulary)"
    )
    lines.append("")
    lines.append("### Marker hits by category")

    grand_total = 0
    for cat in res["categories"]:
        grand_total += cat["total_hits"]
        if cat["total_hits"]:
            terms = ", ".join(f"`{h['term']}` ×{h['count']}" for h in cat["hits"])
            lines.append(
                f"- **{cat['label']}** — {cat['total_hits']} "
                f"({cat['per_1000_words']}/1k words): {terms}"
            )
        else:
            lines.append(f"- **{cat['label']}** — 0")

    lines.append("")
    lines.append(f"**Total marker hits: {grand_total}.** "
                 "Clustering matters more than any single hit; a few in a long "
                 "document is ordinary human writing.")
    return "\n".join(lines)


with gr.Blocks(title="AI Writing Markers") as demo:
    gr.Markdown(
        "# AI Writing Markers\n"
        "Scan text for documented markers of AI-generated writing "
        "(overused vocabulary, formulaic transitions, cliché phrases, structural "
        "tells, punctuation habits, and burstiness). "
        "Source-backed and open: "
        "[GitHub](https://github.com/humzakt/ai-writing-markers)."
    )
    gr.Markdown(DISCLAIMER)
    with gr.Row():
        inp = gr.Textbox(
            label="Text to scan",
            placeholder="Paste an essay, paragraph, or draft here...",
            lines=12,
        )
        out = gr.Markdown(label="Report")
    with gr.Row():
        btn = gr.Button("Scan", variant="primary")
        clear = gr.ClearButton([inp, out])
    gr.Examples(
        examples=[[EXAMPLE_AI], [EXAMPLE_HUMAN]],
        inputs=inp,
        label="Try an example (AI-flavoured vs. human)",
    )
    btn.click(scan, inputs=inp, outputs=out)
    inp.submit(scan, inputs=inp, outputs=out)


if __name__ == "__main__":
    demo.launch()
