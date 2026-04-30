# `_template` — copy-this-to-start

Reference scaffold for a new Dash app. Copy the directory:

```bash
cp -r apps/_template apps/<your-new-app>
cd apps/<your-new-app>
```

Then:

1. Edit this `README.md` to describe what your app does.
2. Edit `app.py` to implement it.
3. Add any additional Python dependencies to `requirements.txt`.
4. Adjust `Dockerfile` only if you need to (system packages, ports).
5. Rename the `name:` field in `render.yaml` to a unique slug.
6. Run locally: `pip install -r requirements.txt && python app.py`, then open <http://localhost:8050>.
7. Deploy to Render via the blueprint flow. Once you have a URL, link it from the relevant chapter `.qmd` file.

## What this template does

The placeholder app is a one-input echo: type into a textbox and the rendered output below it updates. It exists only to verify that the Dash + Render pipeline runs locally and in a container.

## Conventions to keep

- Each Dash app is self-contained (its own `requirements.txt`, no shared imports from the book).
- The Dockerfile reads `$PORT` so it works under Render's port assignment.
- Production serves through Gunicorn against `app.server` (Dash's underlying Flask app).
