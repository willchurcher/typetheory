# typetheory

This repository contains an evolving platform for studying type theory using Jupyter notebooks and automated quizzes.

Learning material lives under `notebooks/`. Each document is stored as both a Jupyter notebook (`.ipynb`) and a matching py-percent script (`.py`). Rendered Markdown and HTML are generated from the notebook for easy viewing.

A small FastAPI app (in `app/`) serves these notebooks as HTML and lets you upload new notebooks.

## Running locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Open `http://localhost:8000` in your browser to view the available notebooks and upload new ones.

See [ROADMAP.md](ROADMAP.md) for the current development plan.
