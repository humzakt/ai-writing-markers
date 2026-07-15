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

## 2. Space

> Hugging Face requires a **PRO** subscription to host Gradio (and Docker) Spaces on
> the free `cpu-basic` tier. **Static** Spaces are free for everyone. This repo ships
> both: a free static build in [`space-static/`](space-static/) (the one deployed) and
> a Gradio build in [`space/`](space/) for PRO accounts or local use.

### 2a. Static Space (free, deployed)

Pure HTML/JS; the checker runs in the browser and fetches `markers.json`. Deploy by
cloning the empty Space repo, adding the three files, and pushing:

```bash
huggingface-cli repo create ai-writing-markers --type space --space_sdk static -y

TMP=$(mktemp -d) && git clone https://huggingface.co/spaces/<hf-user>/ai-writing-markers "$TMP/s"
cd "$TMP/s"
cp /Users/humzakhawar/Desktop/ai-writing-markers/space-static/index.html .
cp /Users/humzakhawar/Desktop/ai-writing-markers/space-static/README.md .
cp /Users/humzakhawar/Desktop/ai-writing-markers/markers.json .
git rm style.css 2>/dev/null || true      # remove the HF template placeholder
git add -A && git commit -m "Deploy static AI writing markers checker"
git push origin main
```

Your Space page: `https://huggingface.co/spaces/<hf-user>/ai-writing-markers`

### 2b. Gradio Space (needs PRO)

Reuses `check.py` and `markers.json` from the repo root; assemble with the build script:

```bash
cd /Users/humzakhawar/Desktop/ai-writing-markers/space
bash build.sh

pip install -r requirements.txt   # optional local test
python app.py                     # http://127.0.0.1:7860

huggingface-cli repo create ai-writing-markers --type space --space_sdk gradio -y
git init -b main
git remote add space https://huggingface.co/spaces/<hf-user>/ai-writing-markers
git add app.py requirements.txt README.md markers.json check.py
git commit -m "AI writing markers Gradio Space"
git push space main
```

Notes:
- `markers.json` and `check.py` are git-ignored inside `space/` for GitHub (to avoid
  duplication) but are committed to the **Space** repo above so it runs standalone.

---

## Keeping them in sync

When you update `markers.json` or `check.py` in the repo root:

- **Dataset:** `git push hf main` again.
- **Static Space:** re-copy `markers.json` into the Space checkout and push (see 2a).
- **Gradio Space:** re-run `bash space/build.sh`, then commit and `git push space main`
  from inside `space/`.
