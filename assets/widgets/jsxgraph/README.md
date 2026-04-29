# `assets/widgets/jsxgraph/` — JSXGraph reference patterns

Standalone HTML reference implementations for JSXGraph widgets. Each file is a complete, runnable HTML page demonstrating one common pattern. These are **canonical examples** — the author (or Claude Code on follow-up tasks) consults them when adding a JSXGraph widget to a chapter.

They are committed to the repo and visible while working, but they are **not embedded in the rendered book**. The book uses the `jsxgraph/jsxgraph-quarto` extension to embed JSXGraph widgets directly inside `.qmd` files.

## Why JSXGraph

JSXGraph is the project's primary tool for "type a function, see a graph" interactives embedded inline in HTML output. It is dual-licensed under LGPL and MIT, ~200KB minified, has been actively maintained for over fifteen years (University of Bayreuth), and supports MathJax for typeset labels. No vendor or API-key dependency. See PRD Addendum 1 §1 for the full rationale.

JSXGraph is best for: function plots with parameter sliders, parametric curves, dynamic geometry constructions, wage–profit frontiers, eigenvector visualizations, indifference-curve / budget-line displays. It is **not** for 3D surfaces (use Plotly Python), complex non-mathematical UI (use Observable JS), or full standalone interactive applications (use Plotly Dash).

## Files

- `01-function-plot-with-slider.html` — function `f(x) = x^α` with a draggable slider for α. The canonical "type a function, drag a slider, see the curve respond" pattern.
- `02-draggable-construction.html` — dynamic geometry: drag a free point, watch dependent objects update.
- `03-multiple-linked-graphs.html` — two boards on the same page sharing a parameter; changing the parameter updates both.
- `04-mathjax-labels.html` — using MathJax to typeset axis and point labels.

## Using one of these in a chapter

1. Open the relevant reference file and copy the JSXGraph configuration block.
2. In your `.qmd` file, embed it via the Quarto extension's shortcode (see CONTRIBUTING.md, "Adding a JSXGraph widget").
3. If the chapter is a critical PDF target, also add a static SVG or PNG fallback using `assets/scripts/render-jsxgraph-fallback.py` (a stub in v1; see Open Question 5.1 in the addendum).

## License

JSXGraph itself is dual-licensed LGPL/MIT (see <https://jsxgraph.org>). The reference HTML files in this directory are CC-BY-SA-4.0, matching the book.
