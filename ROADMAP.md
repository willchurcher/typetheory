# Type Theory Learning Platform Roadmap

This document outlines the planned phases for building a web-based system for learning type theory through Jupyter notebooks. The goal is to allow rendered notebooks to be organized in a dependency graph, quiz users on each document, and eventually incorporate spaced repetition.

## Phase 1: Notebook Rendering & Display (v0.1)
1. **Notebook Collection**: Place notebooks in a `notebooks/` directory.
2. **HTML Rendering**: Use `nbconvert` or similar tooling to convert notebooks to HTML automatically.
3. **Web Interface**: Provide a lightweight FastAPI or Flask app that lists available notebooks and allows viewing the rendered HTML.
4. **Module Dependencies**: Maintain a small JSON/YAML file describing prerequisite relationships between notebooks to create a DAG of modules.

Checkpoint **A**: HTML rendering works, notebooks can be viewed, and prerequisites are enforced.

## Phase 2: LLM-Generated Quizzes (v0.2)
1. **Quiz Generation**: Send notebook content to an LLM (e.g., OpenAI GPT) to create quiz questions. Store these in `quizzes/`.
2. **Quiz Interface**: Add a web page for each notebook's quiz. Track user answers and scores (e.g., SQLite).
3. **Answer Evaluation**: Optionally send answers to the LLM for comparison with expected answers.

Checkpoint **B**: Quizzes generate correctly, scores persist, and progress can be viewed.

## Phase 3: Performance Tracking & Spaced Repetition (v0.3)
1. **History Database**: Keep a history of quiz attempts with timestamps.
2. **Scheduling**: Implement a spaced-repetition scheduler (e.g., SM-2) to determine when to review each notebook.
3. **Dashboard**: Show upcoming reviews and overall performance metrics.

Checkpoint **C**: Spaced repetition is functioning and performance data is recorded.

## Phase 4: Polishing & Deployment (v1.0)
1. **User Management**: Decide whether to support multiple users or stay single-user.
2. **Dockerization**: Provide Docker setup for easy deployment to free hosting services.
3. **CI/CD and Tests**: Add automated tests and setup a simple CI pipeline to run them.

Checkpoint **D**: Final feedback and testing before releasing v1.0.

## Possible Future Enhancements
- Interactive widgets inside notebooks.
- Enhanced tutoring features using LLMs.
- Notifications or integrations for reminders.

This roadmap should guide future contributors or coding agents in implementing the project incrementally.
