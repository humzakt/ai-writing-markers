#!/usr/bin/env bash
# Assemble the self-contained Hugging Face Space.
#
# The Space reuses the checker and dataset from the repo root instead of keeping
# duplicate copies in git. Run this before testing or pushing the Space.
set -euo pipefail
cd "$(dirname "$0")"

cp ../markers.json ../check.py .
echo "Space assembled in $(pwd):"
ls -1 app.py requirements.txt README.md markers.json check.py

cat <<'NOTE'

Next steps:
  pip install -r requirements.txt   # local test deps
  python app.py                     # test locally at http://127.0.0.1:7860
  # then push this folder to your HF Space (see ../HUGGINGFACE.md)
NOTE
