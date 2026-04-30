# Standalone Dash applications

Each major interactive companion to a chapter lives here as its own self-contained Python project. The book links to deployed instances; each subdirectory holds the source.

## Conventions

Every app under `apps/<app-name>/` must contain:

- `app.py` — the Dash application entrypoint. Running `python app.py` should serve the app at `localhost:8050`.
- `requirements.txt` — pinned Python dependencies for the app. **Not** shared with the book's `pyproject.toml`; each app gets its own.
- `Dockerfile` — production container image. Should expose port 8050 (or read `$PORT`).
- `render.yaml` — Render deployment manifest. The free tier of Render is sufficient for low-traffic learning-project use.
- `README.md` — what the app does, how to run it locally, the deployed URL once one exists.

A reference template lives at `apps/_template/`. To start a new app:

```bash
cp -r apps/_template apps/<your-new-app>
cd apps/<your-new-app>
# edit README.md, app.py, requirements.txt, render.yaml
```

## Running locally

```bash
cd apps/<app-name>
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
# open http://localhost:8050
```

## Deploying to Render

1. Push the repository to GitHub (the Render blueprint reads from there).
2. In the Render dashboard, create a new Blueprint instance and point it at `apps/<app-name>/render.yaml`.
3. Render reads the manifest, builds the Docker image, and deploys.
4. Once a deployed URL exists, **update the linked URL** in the relevant chapter's `.qmd` file. The PRD uses a placeholder of the form `[<app-slug>.calculation-course.app](#)`; replace `(#)` with the actual Render URL.

If Render is unavailable, Fly.io and Railway both work with the same Dockerfile — you'd just need a different deployment manifest.

## The reference demo

`apps/demo-budget-explorer/` is the Cobb-Douglas budget-explorer app from the Week 2 syllabus, implemented as a smoke test for the deployment pattern. It is **not** the actual Week 2 deliverable; it exists to validate that the `book → linked Dash app` pipeline works end-to-end.
