# Contributing to the Morishima Track

Conventions for adding new content. Aimed at the author, future collaborators, and Claude Code on follow-up tasks.

The infrastructure is a Quarto book project with a Python execution engine, Tufte-style marginalia in both HTML and PDF outputs, Hypothesis annotation enabled on the deployed site, and standalone Dash apps as separately-deployed companions to specific chapters.

If something below contradicts the actual behaviour of the build, the build is right and this file should be updated.

## Adding a new chapter or week

1. Choose the right directory:
   - `weeks/` for any new 101-arc mathematical week.
   - `controversies/` for any new Part II controversy or seminar.
   - `appendices/` for an appendix.
   - `201/` for follow-on-course material.
2. Pick a filename. Existing convention is `<area>-<NN>-<slug>.qmd`, e.g. `week-11-something.qmd`. Two-digit zero-padded ordering keeps the directory listing sorted.
3. YAML front matter template (every `.qmd` file should have it):

   ```yaml
   ---
   title: "Week N — Short Title"
   description: "One-sentence description, drawn from the chapter's framing paragraph."
   order: 11
   ---
   ```

   The `order` is optional but useful for sorting; `description` is the social-card / TOC subtitle.
4. Add the file to `_quarto.yml` under the right `chapters:` or `appendices:` block. Order within a Part is determined by listing order in `_quarto.yml`, not by the `order` front-matter field.
5. The week heading is *implicit* — it comes from the YAML `title`. Do not write `# Week N — Title` at the top of the body. Use `## Section` for within-chapter sections (Framing, Learning objectives, Core concepts, Resource schedule, Mini project, Self-check, Bridge).

## Adding marginalia

Two annotation layers run in parallel.

### Authored marginalia (the "T. S. Spivet" layer)

Use `:::{.column-margin}` divs. They render in the right margin of HTML on screens wider than ~1100px and as Tufte-style sidenotes in PDF (via Typst's Marginalia package).

```markdown
This is a body paragraph.

::: {.column-margin}
This is a margin note. Keep it short — one or two sentences. Long sidebars
should stay inline as `.callout-*` blocks.
:::

The body paragraph continues here.
```

Footnotes are pushed to the margin globally (`reference-location: margin` in `_quarto.yml`), so a regular `[^name]` footnote also appears as a sidenote.

What belongs in a margin:
- Definitional asides ("note: 'value' here means labor-time, not price").
- Cross-references ("see Controversy 4 for the reswitching version").
- Brief contextual remarks the author wants visible without breaking the flow.

What does not belong in a margin:
- Long technical sidebars. Use `:::{.callout-note}` (or `.callout-warning`, `.callout-important`) inline.
- Citations. Use Quarto's `@key` syntax (see "Cross-referencing" below).

### Hypothesis (the social layer)

Hypothesis is enabled site-wide via `comments: hypothesis: true` in `_quarto.yml`. No per-chapter setup required.

Hypothesis annotations appear only on the HTML site, never in the PDF or EPUB.

By default annotations are public. If you want a private group for early-draft commentary, create one at <https://hypothes.is/groups> and document the group code here.

## Adding code blocks

Python code blocks are executed by Quarto's Jupyter engine. The default behaviour, set in `_quarto.yml`:

- `freeze: auto` — re-execute only when the source changes; otherwise serve cached output.
- `echo: true` — show the source.
- `warning: false` — suppress warnings in rendered output.
- `code-fold: show` — code is shown by default but is foldable.

Per-block conventions (chunk options as YAML lines starting with `#|`):

```{.python}
```{python}
#| label: fig-cobb-douglas
#| fig-cap: "Cobb-Douglas utility surface."
#| fig-cap-location: margin
#| column: margin             # optional: render the figure itself in the margin
import numpy as np
...
```
```

Use `#| label: fig-<slug>` for cross-referenceable figures. Use `#| label: tbl-<slug>` for tables. Cross-reference with `@fig-<slug>` / `@tbl-<slug>`.

For non-Python languages (Observable JS, R), use the appropriate language tag — `{ojs}`, `{r}`, etc. Quarto routes them to the right engine automatically.

## Adding a Dash app

Each Dash app is a self-contained Python project under `apps/<app-name>/`.

1. `cp -r apps/_template apps/<your-new-app>` and edit.
2. Required files: `app.py`, `requirements.txt` (not shared with the book's `pyproject.toml`), `Dockerfile`, `render.yaml`, `README.md`.
3. The app must run with `python app.py` and serve at `localhost:8050`.
4. The Dockerfile reads `$PORT` so it works under Render's port assignment.
5. Production serves through Gunicorn against `app.server` (Dash's underlying Flask app).
6. Deploy to Render via the blueprint flow (`render.yaml`).
7. Once a public URL exists, **link it from the relevant chapter** with a `:::{.callout-note}` block, replacing the placeholder URL. See `weeks/week-02-constrained.qmd` for the pattern.

## Adding a JSXGraph widget

JSXGraph is the primary tool for inline math interactives — "type a function, drag a slider, see a curve respond" — and for dynamic-geometry constructions. Dual-licensed LGPL/MIT; no API key; integrated via the `jsxgraph/jsxgraph-quarto` extension installed in `_extensions/jsxgraph/jsxgraph/`.

### When to use JSXGraph (vs. other widget tools)

- **JSXGraph** — function plots with parameter sliders, parametric curves, dynamic geometry (drag a point, watch dependent objects update), wage–profit frontiers (Controversy 4), eigenvector visualizations (Week 4), indifference-curve / budget-line plots (Week 2). 2D only.
- **Observable JS** — structured visualizations with custom non-mathematical UI (multi-input forms, network-graph layer toggles, dropdown selectors). See "Adding an Observable widget" below.
- **Plotly Python** — static-but-interactive plots and figures, especially 3D surfaces (rotation, zoom). Rendered into HTML at build time by Quarto's Jupyter engine.
- **Plotly Dash** — full-scale interactive applications with state and routing. See "Adding a Dash app".

### Reference patterns

Working standalone HTML examples live in `assets/widgets/jsxgraph/`:

- `01-function-plot-with-slider.html` — function plot with parameter slider.
- `02-draggable-construction.html` — draggable points, dependent objects.
- `03-multiple-linked-graphs.html` — two boards sharing a parameter.
- `04-mathjax-labels.html` — MathJax-typeset labels on a JSXGraph board.

Open one in a browser to see it run; copy the configuration into your `.qmd` file.

### Embedding pattern (Quarto extension)

The extension provides a shortcode for inline JSXGraph blocks. Inside a `.qmd`:

````markdown
```{=html}
<link rel="stylesheet" type="text/css"
      href="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraph.css">
<script src="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraphcore.js"></script>
<div id="jxg-demo" class="jxgbox" style="width: 600px; height: 400px;"></div>
<script>
  const board = JXG.JSXGraph.initBoard("jxg-demo", {
    boundingbox: [-0.5, 12, 11, -1], axis: true,
    showCopyright: false, showNavigation: false
  });
  const a = board.create("slider",
    [[1,10],[9,10],[0.05,0.4,0.95]], { name: "α", snapWidth: 0.05 });
  board.create("functiongraph",
    [x => Math.pow(x, a.Value()), 0.01, 10],
    { strokeColor: "steelblue", strokeWidth: 2 });
</script>
```
````

When the `jsxgraph/jsxgraph-quarto` extension is installed, prefer its shortcode (consult the extension's README in `_extensions/jsxgraph/jsxgraph/` after install) over the raw `{=html}` block above. The raw form above is a portable fallback.

### PDF fallback

JSXGraph widgets render only in HTML. For chapters with critical JSXGraph widgets, ship a static SVG/PNG fallback inline (or in the margin) so the PDF reader still sees the relevant figure. v1 ships a stub helper at `assets/scripts/render-jsxgraph-fallback.py` — implement when the first chapter actually needs it (PRD Addendum 1, Open Question §5.1).

## System-dynamics tool positioning

For the project's macroeconomic stock-flow-consistent (SFC) modeling work — primarily Controversy 6 — the tool decision is layered. Use this section as a reference when picking a tool for new SFC content.

### Primary: `sfc_models`

`sfc_models` (Brian Romanchuk; Apache 2.0; on PyPI; pinned in `pyproject.toml`) is the **primary** SFC tool. It implements the major Godley–Lavoie *Monetary Economics* models (SIM, PC, LP, BMW, OPEN, REG) under `sfc_models.gl_book`, validated against the textbook's eViews implementations. Its key feature is high-level sector specification: declare economic sectors (households, firms, government, banks); the package generates the equations.

For Controversy 6 capstone Versions 1–3 (baseline SIM, endogenous bank credit, Minsky-Keen fragility), build on `sfc_models.gl_book` baselines. Version 4 (planned-economy transformation) is the project's original contribution and replaces `sfc_models`'s banking sector with the Cockshott-Cottrell-Dapprich token apparatus.

Reference notebooks live in `sfc-notebooks/` (stubs in v1, populated as Controversy 6 work proceeds).

### Complementary: `pysolve`

`pysolve` (kennt; on PyPI; pinned) is a constraint solver. Used by `sfc_models` internally and available directly when fine-grained control over the solver is wanted.

### Optional: `pysd` (under the `extended` extra)

`pysd` (system-dynamics interoperability with Vensim / XMILE) is **optional**. Install via `pip install -e ".[extended]"` or `uv sync --extra extended`. Reach for it only if you need to load externally-published SD models (e.g., a published climate model in Vensim format).

### Optional teaching companions: Minsky and Ravel

Minsky and Ravel are positioned as **optional teaching companions**, not primary tooling.

- **Minsky** (Steve Keen; GPL; `minsky-models/`) — visual SD modelling with built-in Godley-table accounting. Recommended use for Controversy 6: after implementing a Godley-Lavoie model in `sfc_models`, optionally rebuild it in Minsky to show how the visual representation differs from code. One-paragraph optional exercise, not a primary deliverable.
- **Ravel** (Steve Keen; commercial / Patreon-distributed; `ravel-files/`) — multidimensional data exploration. Recommended optional use for Controversy 5 (BEA profit-rate empirical work) and Controversy 7 (emissions data). Author's working files only; do not redistribute (`.rvl` files are gitignored by default).

The **build never depends on Minsky or Ravel being installed**. Files in `minsky-models/` and `ravel-files/` are author-side artifacts; the rendered book may reference exported screenshots, but the rendering pipeline never opens these files.

### Agent-based modeling: Mesa

Mesa (Apache 2.0; pinned) is the agent-based modeling tool, primarily for the 201 placeholder course (Zhang-program work — producer competition, realization uncertainty, primitive accumulation) and for the optional ergodicity-economics extension to Controversy 6 Version 3 (multi-firm leverage-dynamics fan chart).

### Climate-LP (Controversy 7)

The 30-year decarbonization LP is built directly with **cvxpy**, not `sfc_models`. SFC and LP are different modeling paradigms.

For an advanced reference on what a more sophisticated climate-economy SFC model looks like, see **EcoDyco** — open-source thermodynamic-SFC, Gaël Giraud's group, *Scientific Reports* 2023, "Macroeconomic dynamics in a finite world based on thermodynamic potential." Editorial reference only; no code dependency.

## Adding an Observable widget

Observable JS embeds inline. Pattern:

````markdown
```{ojs}
viewof alpha = Inputs.range([0.05, 0.95], {value: 0.4, step: 0.05, label: "α"})

curve = {
  const xs = d3.range(0.1, 10, 0.1);
  const ys = xs.map(x => Math.pow(x, alpha));
  return Plot.plot({
    marks: [Plot.line(xs.map((x, i) => ({x, y: ys[i]})), {x: "x", y: "y"})]
  });
}
```
````

`viewof` exposes the input's value as a reactive variable; downstream cells (`curve` here) recompute automatically. The `index.qmd` "Style and rendering reference" section has a working example.

When to use OJS:
- Inline pedagogical sliders ("drag this to see the curve change").
- Small interactive plots that don't need a backend.

When **not** to use OJS:
- Anything with state, complex inputs, or computation. Use a Dash app instead.

## Adding data files

Provenance is mandatory. Every file in `data/` must be documented in `data/README.md` with:

- Filename.
- Source URL.
- Retrieval date.
- License terms.
- Brief description (what it is, what it's used for in the book).

Large files (> a few MB) should not be committed; use Git LFS, or store externally and document the retrieval script in `data/README.md`.

## Cross-referencing

- Internal links between chapters: `[Week 7](../weeks/week-07-input-output.qmd)`. Quarto resolves relative paths.
- Internal links to a section: `[Hawkins-Simon](../weeks/week-07-input-output.qmd#core-concepts)`.
- Citations: prefer Quarto's `@key` syntax, with bib entries in a project-level `references.bib` (not yet created in v1; add it when the first citation goes in).
- Figures: `@fig-<slug>`. Tables: `@tbl-<slug>`.

## Building locally

```bash
quarto preview                  # live-reloading server, default port 4444
quarto render                   # all formats
quarto render --to html         # one format only
quarto render weeks/week-01-multivariable.qmd  # one chapter, useful when iterating
```

Common gotchas:

- `freeze: auto` caches executed output in `_freeze/`. If a change to upstream Python state (data file, library version) doesn't show up in the rendered output, run `quarto render --execute-daemon-restart` or delete the relevant `_freeze/` subdirectory.
- The Typst PDF backend handles most of the substantive content fine, but a few features (extreme float layout, very long single math lines) occasionally need manual help. If something looks broken in PDF, switch the engine in `_quarto.yml` to `xelatex` and document the issue here. As of the v1 bootstrap no such fallback has been needed — but the option exists.
- LaTeX fallback: set `pdf-engine: xelatex` and `documentclass: tufte-book` (or `scrbook` with the existing setup). The `tufte-book` document class gives you Tufte-style PDF marginalia via the `tufte-latex` package. Note that `tufte-latex` has known compile issues with some Quarto preambles — see the Warrick Ball blog post for the `sed`-out-problematic-preamble-lines workaround.

## Adding notes (the Obsidian vault under `notes/`)

The `notes/` directory is an Obsidian vault, rendered to the deployed site at `/notes/` by [Quartz](https://quartz.jzhao.xyz/). It's the working layer behind the polished book — reading notes, questions, insights, methodological decisions, progress logs.

The conventions:

- Open `notes/` as a vault in Obsidian. No front matter is required; plain Markdown with wiki-links is the default.
- Per-week notes live under `notes/weeks/week-NN-<slug>/` and per-controversy notes under `notes/controversies/controversy-NN-<slug>/`. The starting set of files in each is `index.md`, `reading-notes.md`, `questions.md`, `insights.md`, `refs.md`. Rename, merge, or delete as the work demands — the structure is a starting suggestion, not a contract.
- Project-meta lives in `notes/_meta/`: `workflow.md` (orientation), `progress.md` (running log), `deferred.md` (parking lot), `decisions.md` (methodological choices), `glossary.md` (optional shared vocabulary).
- Drag images and PDFs into `notes/attachments/`. Obsidian wires the attachments folder up by default.
- Tags work — `#confused`, `#reread`, `#publishable` for things that might graduate into the book later.

What goes in notes vs. book:

- **Notes** is the default. Reading notes, half-formed questions, scratch calculations, intuition you wished someone had told you. Date-stamp entries.
- **Book** is for polished, citation-ready content. Things graduate from notes → book when they're ready. Going back the other way (pulling polished content back into scratch) is a sign of premature commitment.

For the full daily-use workflow, see [`notes/_meta/workflow.md`](notes/_meta/workflow.md).

## The `.author-notes` callout class (mandatory for the strip script)

Every book chapter (`.qmd` under `weeks/`, `controversies/`, `201/`, `appendices/`, plus the top-level `index.qmd` and friends) contains a single "Author's notes" callout near the top, immediately after the chapter's framing paragraph. The callout is collapsed by default, so casual readers don't see notes prominently; clicking the header expands it.

The callout pattern:

```markdown
::: {.callout-note appearance="minimal" collapse="true" .author-notes}
## Author's notes for this chapter

- [Reading notes](/notes/weeks/week-NN-<slug>/reading-notes/)
- [Open questions](/notes/weeks/week-NN-<slug>/questions/)
- [Insights and connections](/notes/weeks/week-NN-<slug>/insights/)
- [References to revisit](/notes/weeks/week-NN-<slug>/refs/)
- [Scratchpad notebook](https://github.com/jquacinella/EconomicPlanningCourse/blob/main/notes/weeks/week-NN-<slug>/scratchpad.ipynb)
:::
```

**The `.author-notes` class is mandatory.** It is the marker the strip script (`assets/scripts/strip-author-notes.py`) uses to identify and remove these callouts when producing a print-targeted manuscript. A callout that's missing the class will leak into the print PDF.

To produce a print-targeted PDF:

```bash
python assets/scripts/strip-author-notes.py
QUARTO_PROFILE=print quarto render build-print/ --to pdf
```

The script reads source `.qmd` files, writes stripped copies to `build-print/`, and never modifies the originals. The `print` profile in `_quarto.yml` controls which chapters belong in the print artifact.

## The alias-page convention (notes → book cross-links)

Within the Obsidian vault, you reference book chapters via wiki-links, e.g. `[[week-01]]` or `[[controversy-04]]`. These resolve to short alias pages under `notes/_book-aliases/` that link out to the corresponding book chapter and notes index.

When adding a new book chapter, also add a matching alias file:

```markdown
<!-- notes/_book-aliases/week-NN.md -->
# Week N — <Title> (book chapter)

This page is an alias. The polished chapter lives in the book.

- **Open in book**: <{{SITE_URL}}/weeks/week-NN-<slug>/>
- **Edit source**: <https://github.com/{{USERNAME}}/morishima-track/blob/main/weeks/week-NN-<slug>.qmd>
- **Notes for this unit**: [[weeks/week-NN-<slug>/index|Week N notes]]
```

Replace `{{SITE_URL}}` and `{{USERNAME}}` with the deployed values once they're stable. Two-hop is intentional and preserves Obsidian's wiki-link autocomplete and backlinks. If the two-hop becomes annoying, see PRD Addendum 2 §6.1 for the link-rewriter alternative — defer until you've felt the friction.

Notes-to-notes wiki-links work natively with no special convention: `[[insights]]` resolves to the most-relevant insights file via Obsidian's vault-wide search.

## The two-build-tool model

Two pipelines, two preview commands, one stitched output site:

- **Quarto** renders the book (`weeks/`, `controversies/`, etc.) to `_book/`. `quarto preview` from the repo root watches sources and serves at `localhost:4444`.
- **Quartz** renders the notes vault (`notes/`) to `quartz/public/`. `cd quartz && npx quartz build --serve` watches the vault and serves at `localhost:8080`.

In CI (`.github/workflows/render.yml`), both run sequentially, and their outputs are stitched into `_site/`:

```
_site/
├── index.html               # Book landing page (Quarto)
├── weeks/                   # Book chapters
├── controversies/
└── notes/                   # Notes site (Quartz)
    ├── index.html
    ├── weeks/
    ├── controversies/
    └── _meta/
```

First-time setup of the Quartz install on a new machine: `cd quartz && bash setup.sh && npm ci`. After that, `npx quartz build --serve` is the daily command. See `quartz/README.md` for details. The local URLs (`localhost:4444` vs. `localhost:8080`) differ from the deployed URLs (no port; notes under `/notes/`); periodically check that cross-links work in the deployed site.

## Hypothesis annotation: etiquette and groups

- Public Hypothesis annotations on the deployed site are visible to anyone. Treat them as you would a public comment thread.
- For early-draft annotation, create a private group at <https://hypothes.is/groups>. Add the group code to this file when one exists.
- Don't paste long technical content into Hypothesis annotations. Use a GitHub issue or a PR comment for sustained discussion.
