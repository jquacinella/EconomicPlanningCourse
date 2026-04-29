# Bootstrap report

Status: complete on branch `claude/implement-bootstrap-mjH1Y`. The infrastructure described in `PRD.md` §§4–9 is in place and the existing `morishima_syllabus.md` content has been extracted into per-chapter `.qmd` files per §6. No substantive content beyond what was in the syllabus has been added.

## What was built

### Repository skeleton (PRD §4)

All directories and files in the §4 tree exist. Empty directories carry `.gitkeep` placeholders. The original `morishima_syllabus.md` was left in place at the repo root; it can be removed once the author is satisfied with the extraction.

### Quarto book project (PRD §5)

`_quarto.yml` is generated to spec, with the chapter ordering, theme, marginalia configuration (`grid.margin-width: 350px`, `reference-location: margin`, `citation-location: margin`, `fig-cap-location: margin`), Hypothesis annotation (`comments.hypothesis: true`), Typst as the primary PDF engine with the LaTeX fallback documented as a comment, and `freeze: auto` execution.

### Content extraction (PRD §6)

Every section of the existing `morishima_syllabus.md` has been split into the per-chapter `.qmd` file specified in §4:

- `index.qmd` — extracts the "How to use this document" front matter, plus the new "Style and rendering reference" section required by §6 (a `.column-margin` div, a footnote pushed to the margin, a Plotly Python figure, an Observable JS slider+plot, a Hypothesis-annotatable paragraph with explicit instructions, and a link to the demo Dash app).
- `master-resources.qmd` — the master resource list, extracted as-is.
- `weeks/week-01-multivariable.qmd` through `weeks/week-10-growth-stability.qmd`.
- `post-course.qmd` — the post-course reading ladder.
- `controversies/controversy-01-cobb-douglas.qmd` through `controversy-07-climate.qmd`, plus `seminar-chinese-critique.qmd`.
- `201/placeholder.qmd` — the 201 placeholder, extracted as-is.
- `where-this-lands.qmd` — the closing reflection.
- `appendices/appendix-a-prereq.qmd`, `appendix-b-extra-depth.qmd`, `appendix-c-absorption.qmd`.

In each chapter, the source's `## Section` heading became the `title:` in YAML front matter, and the `**Framing.**`, `**Learning objectives.**`, `**Core concepts.**`, `**Resource schedule.**`, `**Mini project — TITLE.**`, `**Self-check.**`, `**Bridge.**` paragraph leads were promoted to proper `## Framing`, `## Learning objectives`, etc. headings as required by §6.

`description:` front matter was filled in for each chapter from a single sentence drawn from the framing paragraph.

`order:` front matter was set on each Week chapter (Weeks 1–10) and Controversy chapter (1–7 plus seminar). For other chapters it was omitted as the §6 template marks it optional.

### Marginalia migration (PRD §6)

Marginalia were **not** automatically converted, per PRD instructions. A `<!-- TODO: marginalia candidate -->` comment was inserted in three places where the source structure most clearly invites editorial sidebar treatment:

- `weeks/week-02-constrained.qmd`: the Chiang Ch 12 companion-reading note in the resource schedule.
- `weeks/week-05-economic-opt.qmd`: the Chiang & Wainwright Ch 9/11/12/13 companion-text note.
- `controversies/controversy-05-okishio.qmd` and `controversy-06-money.qmd`: the existing "Ergodicity sidebar" sections, marked as candidates for full-width sidebar / expanded marginal column treatment.

The sidebar text itself was kept inline. The author is the one to decide what becomes a margin note.

### Demo Dash app (PRD §7)

`apps/demo-budget-explorer/` is a real working Cobb-Douglas budget-line explorer, not a placeholder:

- Two sliders: α (Cobb-Douglas exponent on x) and M (income).
- Two number inputs for prices p₁ and p₂.
- Plot output: budget line, three indifference curves (one through the optimum), and the optimum point itself.
- Numerical readout: x*, y*, u*, and the envelope-theorem multiplier λ* = ∂u*/∂M.
- Locally runnable via `cd apps/demo-budget-explorer && pip install -r requirements.txt && python app.py`.
- Containerised via the included Dockerfile (Gunicorn against `app.server`, reads `$PORT`).
- Render-deployable via `render.yaml`.

`apps/_template/` is a copy-this-to-start scaffold with a placeholder echo app, the same Dockerfile pattern, and a stub `render.yaml`.

`apps/README.md` documents the full convention.

`weeks/week-02-constrained.qmd` includes the `:::{.callout-note}` "Interactive companion" block with a placeholder URL of `[budget-explorer.morishima-track.app](#)`, exactly as specified in §7.

### CI/CD (PRD §8)

- `.github/workflows/render.yml`: on push to `main`, sets up Python 3.11, installs uv, installs Quarto (pre-release for Typst support), runs `quarto render` for HTML, PDF (with `continue-on-error` because Typst features may need work), and EPUB; deploys `_book/` to `gh-pages` via `peaceiris/actions-gh-pages@v3`; uploads PDF/EPUB as release assets on tagged releases. The 30-minute job timeout is generous for the v1 skeleton and a comment notes that this budget will need revisiting as executable code is added.
- `.github/workflows/lint.yml`: on PR, runs `markdownlint-cli2-action` on `.qmd` and `.md` files (with `_book/` and `.quarto/` excluded), and `lycheeverse/lychee-action` for broken-link checking with the placeholder `*morishima-track.app` URL excluded so it doesn't fail the build before deployment exists.

### Documentation (PRD §9)

- `README.md` — one-paragraph description, Quick start, repository layout, license notice for content (CC-BY-SA-4.0) and code (MIT), acknowledgments paragraph naming Quarto, QuantEcon, Cockshott/Cottrell/Dapprich, Zhang and Yu, Keen, the 3B1B/MIT/Strang lineage, and the Cambridge UK tradition.
- `CONTRIBUTING.md` — covers all six required convention sections (new chapter, marginalia, code blocks, Dash apps, Observable widgets, data files), plus cross-referencing, building locally with common gotchas, and Hypothesis etiquette.
- `data/README.md`, `apps/README.md`, `minsky-models/README.md`, `ravel-files/README.md` per the PRD spec.

### Python project files

- `pyproject.toml` — uv-compatible, pins Python `>=3.11,<3.13`, lists the scientific stack from PRD §3.3 (NumPy, SciPy, SymPy, Matplotlib, Plotly, Pandas, NetworkX, statsmodels, PuLP, CVXPY, Mesa, Jupyter, JupyterLab, quantecon).
- `.python-version` — `3.11`.
- `uv.lock` is **not** generated. See "Open issues" below.

### Build configuration

- `.gitignore` — Python, Jupyter, macOS, Quarto, `_freeze/`, `_book/`, `.quarto/`, `_site/`, `notes/`, `ravel-files/*.rvl`.
- `.gitattributes` — text/binary normalization with binary tags for images, PDF, EPUB, fonts, `.mky`, `.rvl`.
- `assets/css/custom.scss` and `assets/css/custom-dark.scss` — initial `.column-margin` styling, otherwise empty.

### LICENSE

Single combined file with CC-BY-SA-4.0 for content and MIT for code, as recommended in PRD §9 and §11(3).

## Deviations from the PRD

1. **`uv.lock` is not generated.** The PRD repository structure (§4) lists `uv.lock` as a file to create. I did not run `uv lock` because (a) the bootstrap environment doesn't have `uv` installed by default, and (b) generating a lockfile requires resolving against a real PyPI snapshot, which would couple the repository's pinned versions to whatever versions happen to be current at build time. The author should run `uv lock` (or `uv sync`) once locally to generate it; the CI workflow handles either case (`uv sync --frozen` if a lockfile exists, `uv sync` otherwise).
2. **`assets/images/cover.png` is not present.** The `_quarto.yml` references it as `cover-image: assets/images/cover.png`. PRD §10 explicitly notes "Real cover image" is out of scope for acceptance, so this is a deliberate stub — Quarto will warn but render without it. The author can drop a cover image at that path when one exists.
3. **`pyproject.toml` includes a `bypass-selection = true` Hatch configuration** because there is no Python package at the project root — only `apps/` subdirectories with their own `requirements.txt`. This is a small accommodation to make `uv sync` against the project root work even though there's nothing to install at that level.
4. **`render.yml` does not abort on PDF or EPUB failure.** I added `continue-on-error: true` to the `quarto render --to pdf` and `--to epub` steps so a missing Typst feature doesn't block HTML deployment during early development. Once Typst rendering is verified locally on the author's machine the `continue-on-error` can be removed.
5. **No `quarto preview` or `quarto render` was actually executed in this environment.** The bootstrap was run in an environment without Quarto or `uv` installed; PRD §10 acceptance criteria 1–9 (which require `quarto render` to succeed locally on macOS, that the demo Observable widget responds to slider input, that the Dash app runs at `localhost:8050`, that GitHub Actions deploys successfully) are *not* verified by this bootstrap and remain the author's responsibility. The `python app.py` of the demo Dash app and the YAML files were syntax-validated only.

## Open issues for the author

1. **Substitute author name.** Every `[author name placeholder]` in `README.md`, `LICENSE`, `pyproject.toml`, and `_quarto.yml` should be replaced with the author's actual choice (PRD §11(2)).
2. **Substitute repository URL.** `_quarto.yml`'s `repo-url: "https://github.com/[username]/morishima-track"` should be replaced with the actual GitHub URL.
3. **Run `uv lock` once locally** to generate `uv.lock`.
4. **Verify the build locally on macOS** per PRD §10 acceptance criteria 1–7. In particular, confirm that Typst PDF rendering of the `.column-margin` divs gives the expected sidenote layout. If not, switch `pdf-engine: typst` to `pdf-engine: xelatex` and `documentclass: scrbook` to `documentclass: tufte-book`, then document the workaround in `CONTRIBUTING.md` per the PRD §6.5 fallback path.
5. **Once the Dash app is deployed**, replace `[budget-explorer.morishima-track.app](#)` in `weeks/week-02-constrained.qmd` with the real URL.
6. **Set up GitHub Pages.** Enable Pages in the repo settings, source = `gh-pages` branch. The `render.yml` workflow will populate it on the first push to `main`.
7. **Consider whether to delete `morishima_syllabus.md`.** It's the source-of-truth file; now that everything is extracted, leaving it at the repo root is harmless but redundant. The PRD does not require its removal.

## Files added

```
.gitignore
.gitattributes
.python-version
LICENSE
README.md
CONTRIBUTING.md
BOOTSTRAP_REPORT.md
_quarto.yml
pyproject.toml
index.qmd
master-resources.qmd
post-course.qmd
where-this-lands.qmd
weeks/week-01-multivariable.qmd
weeks/week-02-constrained.qmd
weeks/week-03-linear-algebra.qmd
weeks/week-04-eigenvalues.qmd
weeks/week-05-economic-opt.qmd
weeks/week-06-lp-duality.qmd
weeks/week-07-input-output.qmd
weeks/week-08-planning.qmd
weeks/week-09-diff-eq.qmd
weeks/week-10-growth-stability.qmd
controversies/controversy-01-cobb-douglas.qmd
controversies/controversy-02-calculation.qmd
controversies/controversy-03-transformation.qmd
controversies/controversy-04-sraffa.qmd
controversies/controversy-05-okishio.qmd
controversies/seminar-chinese-critique.qmd
controversies/controversy-06-money.qmd
controversies/controversy-07-climate.qmd
201/placeholder.qmd
appendices/appendix-a-prereq.qmd
appendices/appendix-b-extra-depth.qmd
appendices/appendix-c-absorption.qmd
apps/README.md
apps/_template/{app.py,requirements.txt,Dockerfile,render.yaml,README.md}
apps/demo-budget-explorer/{app.py,requirements.txt,Dockerfile,render.yaml,README.md}
notebooks/.gitkeep
data/{README.md,.gitkeep}
minsky-models/{README.md,.gitkeep}
ravel-files/{README.md,.gitkeep}
assets/css/{custom.scss,custom-dark.scss}
assets/images/.gitkeep
assets/fonts/.gitkeep
extensions/.gitkeep
.github/workflows/render.yml
.github/workflows/lint.yml
```

The `notes/` directory is not committed (it's gitignored).

PRD §12 instructs that this report be deleted after the author reads it.
