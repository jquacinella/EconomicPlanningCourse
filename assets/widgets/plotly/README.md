# `assets/widgets/plotly/` — Plotly Python reference patterns

Reference Plotly Python figures, rendered into the static HTML book by Quarto's Jupyter engine.

## Tool positioning

Plotly Python is the project's tool for **static-but-interactive plots and figures** — figures the build process renders into the page once, but where the resulting HTML still supports rotation, zoom, and hover. Best for: 3D surface plots, large datasets, Matplotlib-replacement work where interactivity is helpful but a backend isn't needed. For "drag a slider, see a curve respond," prefer **JSXGraph** (`../jsxgraph/`). For full-scale interactive applications with state, prefer **Plotly Dash** (`../../../apps/`).

## Files

- `01-3d-surface.qmd` — Cobb-Douglas utility surface, a 3D `go.Surface` plot. The reference for any chapter (Week 1, Controversy 1, …) that needs a rotatable 3D figure.
