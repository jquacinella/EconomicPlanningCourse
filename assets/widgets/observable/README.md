# `assets/widgets/observable/` — Observable JS reference patterns

Reference Observable JS (OJS) widgets, embedded via Quarto's native OJS support.

## Tool positioning

OJS is the project's tool for **inline structured visualizations with custom UI** — typically a small reactive control plus a plot, where the control is non-trivial (e.g., dropdown selectors, multi-input forms, network-graph layer toggles). For "type a function, drag a slider, see a curve respond," prefer **JSXGraph** (`../jsxgraph/`). For static-but-interactive figures (3D surfaces, large data plots), prefer **Plotly Python** (`../plotly/`).

## Files

- `01-reactive-slider.qmd` — a minimal reactive `viewof Inputs.range` tied to a Plot. The pattern reproduced from `index.qmd`'s "Style and rendering reference" section.
