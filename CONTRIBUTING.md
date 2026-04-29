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

## Hypothesis annotation: etiquette and groups

- Public Hypothesis annotations on the deployed site are visible to anyone. Treat them as you would a public comment thread.
- For early-draft annotation, create a private group at <https://hypothes.is/groups>. Add the group code to this file when one exists.
- Don't paste long technical content into Hypothesis annotations. Use a GitHub issue or a PR comment for sustained discussion.
