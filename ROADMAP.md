# Type Theory Learning Platform Roadmap

This document outlines the planned phases for building a web-based system for learning type theory through Jupyter notebooks. The goal is to allow rendered notebooks to be organized in a dependency graph, quiz users on each document, and eventually incorporate spaced repetition.

## Document Setup (v0.0)

Before any web interface exists, we maintain the core learning material in a structured folder layout. Each document lives in a subdirectory of `notebooks/` and contains:

* `NAME.ipynb` – the canonical Jupyter notebook
* `NAME.py` – the same content in “py-percent” format for easier text diffs
* `NAME.md` – rendered Markdown output
* `NAME.html` – optional HTML rendering

The Markdown and HTML files are generated from the notebook using `nbconvert`. The `.ipynb` or `.py` file with the most recent git timestamp is treated as the authoritative source. Version control keeps all representations for review.

**Initial documents included:**

1. **definitions-overview** – relationships between basic definitions in type theory
2. **idea** – motivation for different type theories and why certain rules (like definitional equality) are introduced
3. **rule-hierarchy** – grouping of rules and the judgements they interact with

These provide a small corpus for testing the build process.

## Phase 1: Notebook Rendering & Display (v0.1)

1. **Notebook Collection**
   Place notebooks in the `notebooks/` directory using the structure from v0.0.
2. **Markdown/HTML Rendering**
   Use `nbconvert` (or similar tooling) to generate both `.md` and `.html` from each notebook automatically. Provide a script to update outputs whenever sources change.
3. **Web Interface**
   Build a lightweight FastAPI (or Flask) app that lists available notebooks and serves the rendered Markdown/HTML.
4. **Module Dependencies**
   Maintain a small JSON/YAML file describing prerequisite relationships between notebooks to form a DAG of modules.

**Checkpoint A:** HTML/Markdown rendering works, notebooks can be viewed, and prerequisites are enforced.

## Phase 2: LLM-Generated Quizzes (v0.2)

1. **Quiz Generation**
   Send notebook content to an LLM (e.g. OpenAI GPT) to create quiz questions. Store these in a `quizzes/` folder.
2. **Quiz Interface**
   Add a web page for each notebook’s quiz. Track user answers and scores (e.g. in SQLite).
3. **Answer Evaluation**
   Send user answers alongside expected answers to the LLM for grading and brief feedback.

**Checkpoint B:** Quizzes generate correctly, scores persist, and progress can be viewed.

## Phase 3: Performance Tracking & Spaced Repetition (v0.3)

1. **History Database**
   Keep a history of quiz attempts with timestamps and scores.
2. **Scheduling**
   Implement a spaced-repetition scheduler (e.g. SM-2) to determine when each notebook should be reviewed next.
3. **Dashboard**
   Show upcoming reviews and overall performance metrics.

**Checkpoint C:** Spaced repetition is functioning and performance data is recorded.

## Phase 4: Polishing & Deployment (v1.0)

1. **User Management**
   Decide whether to support multiple users or remain single-user.
2. **Dockerization**
   Provide Docker setup for easy deployment to free hosting services.
3. **CI/CD and Tests**
   Add automated tests and set up a simple CI pipeline to run them on each push.

**Checkpoint D:** Final feedback and testing before releasing v1.0.

## Possible Future Enhancements

* Interactive widgets inside notebooks (e.g. sliders, live code cells)
* Enhanced tutoring features using LLMs (e.g. step-by-step proofs)
* Notifications or integrations (e.g. calendar reminders for reviews)
* Collaborative editing and peer-review workflows

## Development Process

1. Edit notebooks using either the `.ipynb` file in JupyterLab or the corresponding `.py` percent file in a text editor.
2. Run the build script to regenerate Markdown/HTML outputs via `nbconvert`.
3. Commit all updated files so the repository tracks both sources and rendered artifacts.
4. Use feature branches or pull requests to review changes and maintain history of the learning material.

---

Let me know if you’d like any further tweaks or additions!
