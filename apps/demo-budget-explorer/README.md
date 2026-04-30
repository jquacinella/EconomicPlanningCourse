# `demo-budget-explorer` — Cobb-Douglas budget explorer

Reference Dash app for the Calculation Course project. Implements a stripped-down version of the Week 2 constrained-utility-maximization mini project as a smoke test for the standalone-app deployment pattern.

## What it does

Solves the consumer problem

```
max  u(x, y) = x^α · y^(1-α)
s.t. p₁·x + p₂·y = M,    x, y ≥ 0
```

interactively. Two sliders for α (Cobb-Douglas exponent on x) and M (income); two number inputs for the prices p₁ and p₂. The plot shows the budget line, three indifference curves (one through the optimum), and the optimum point itself. The numerical readout prints x*, y*, u*, and the envelope-theorem multiplier λ* = ∂u*/∂M.

## Running locally

```bash
cd apps/demo-budget-explorer
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
# open http://localhost:8050
```

## Deployment URL

Once deployed to Render, the URL goes here. Replace this paragraph with the actual link, and update the `::: {.callout-note}` block in `weeks/week-02-constrained.qmd` to match.

## Why this app exists

It exists to validate the deployment pattern end-to-end:

- A Dash app under `apps/<name>/` runs locally with `python app.py`.
- The Dockerfile here reads `$PORT` and serves through Gunicorn against `app.server`.
- The `render.yaml` deployment manifest is enough to deploy via Render's blueprint flow.
- The book's `weeks/week-02-constrained.qmd` links to the deployed instance.

It is **not** the actual Week 2 deliverable from the syllabus. The author is expected to do that work as part of the course; this app's role is to be a known-good reference the author can copy patterns from.
