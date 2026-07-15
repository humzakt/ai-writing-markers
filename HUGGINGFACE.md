# Publishing to Hugging Face

This repo is ready to publish in two forms:

1. A **Dataset** — the marker catalogue (`markers.json` + docs) as a reusable dataset.
2. A **Space** — a live Gradio demo of the checker (in [`space/`](space/)).

Both are separate git repos on Hugging Face. You need a **write** token:
https://huggingface.co/settings/tokens

```bash
huggingface-cli login   # paste your write token once
```

Replace `<hf-user>` below with your Hugging Face username.

---

## 1. Dataset

The root `README.md` already carries the dataset-card front-matter (license, tags,
task category), so the repo is directly publishable.

```bash
cd /Users/humzakhawar/Desktop/ai-writing-markers

# create the dataset repo on the Hub
huggingface-cli repo create ai-writing-markers --type dataset -y

# push this repo's contents to it (second remote, keeps GitHub 'origin' intact)
git remote add hf https://huggingface.co/datasets/<hf-user>/ai-writing-markers
git push hf main
```

Your dataset page: `https://huggingface.co/datasets/<hf-user>/ai-writing-markers`

> The `space/` folder rides along harmlessly in the dataset repo. If you'd rather it
> not, delete it from the dataset checkout after pushing.

---

## 2. Space (Gradio demo)

The Space reuses `check.py` and `markers.json` from the repo root, so assemble it
first with the build script (copies those two files into `space/`):

```bash
cd /Users/humzakhawar/Desktop/ai-writing-markers/space
bash build.sh

# optional local test
pip install -r requirements.txt
python app.py            # opens http://127.0.0.1:7860

# create the Space and push
huggingface-cli repo create ai-writing-markers --type space --space_sdk gradio -y
git init -b main
git remote add space https://huggingface.co/spaces/<hf-user>/ai-writing-markers
git add app.py requirements.txt README.md markers.json check.py
git commit -m "AI writing markers Gradio Space"
git push space main
```

Your Space page: `https://huggingface.co/spaces/<hf-user>/ai-writing-markers`

Notes:
- The Space `README.md` front-matter sets `sdk: gradio`; the Hub picks a current
  Gradio version automatically. Pin `sdk_version:` there if you want a fixed build.
- `markers.json` and `check.py` are git-ignored inside `space/` for GitHub (to avoid
  duplication) but are committed to the **Space** repo above so it runs standalone.

---

## Keeping them in sync

When you update `markers.json` or `check.py` in the repo root:

- **Dataset:** `git push hf main` again.
- **Space:** re-run `bash space/build.sh`, then commit and `git push space main` from
  inside `space/`.
