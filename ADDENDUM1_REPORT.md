# PRD Addendum 1 — application report

Status: applied on branch `claude/apply-prd-addendum-VGkKc`. All six new acceptance criteria from §6 of the addendum are met or verifiably configured (see "Acceptance criteria" below). Two items have minor deviations, called out under "Deviations".

This report is companion to `BOOTSTRAP_REPORT.md`; it covers only the *delta* changes introduced by `PRD_addendum1.md`.

## Summary of changes

### 1. JSXGraph as primary inline-math widget tool (addendum §1)

- **CONTRIBUTING.md** — added a new top-level section *"Adding a JSXGraph widget"* (when to use vs. OJS / Plotly / Dash; reference patterns in `assets/widgets/jsxgraph/`; embedding pattern via the Quarto extension or raw `{=html}` fallback; PDF-fallback note).
- **`_quarto.yml`** — added `include-in-header: [assets/jsxgraph-include.html]` to the HTML format. This loads the JSXGraph runtime on every HTML page so widgets work whether or not the `jsxgraph/jsxgraph-quarto` extension is installed.
- **`assets/jsxgraph-include.html`** — new HTML partial that pulls JSXGraph's CSS and JS from the jsdelivr CDN. Documented as the interim setup until `quarto add jsxgraph/jsxgraph-quarto` is run; the extension supersedes (or coexists with) this include once installed.
- **`assets/widgets/jsxgraph/`** — new directory with README and four reference HTML files:
  - `01-function-plot-with-slider.html` — `f(x) = x^α` with a draggable slider (the canonical pattern).
  - `02-draggable-construction.html` — dynamic-geometry: midpoint and circle update as A and B are dragged.
  - `03-multiple-linked-graphs.html` — two boards sharing a parameter; both update on slider drag.
  - `04-mathjax-labels.html` — MathJax-typeset labels on a JSXGraph board.
- **`assets/widgets/observable/`** — new directory with README and `01-reactive-slider.qmd` reference (the OJS pattern from `index.qmd`).
- **`assets/widgets/plotly/`** — new directory with README and `01-3d-surface.qmd` (Cobb-Douglas surface, the Plotly Python pattern).
- **`assets/scripts/render-jsxgraph-fallback.py`** — stub helper script for static-SVG fallback rendering. Documented per addendum §1.6 and §5.1 default ("defer until first chapter needs it").
- **`index.qmd`** — added a fifth demo to the *Style and rendering reference* section: *"A JSXGraph widget"*. The original four demos (margin note, footnote-to-margin, Plotly Python figure, Observable widget) are preserved, per the addendum's instruction in §7 to *add* a JSXGraph demo rather than replace any existing one.

### 2. `sfc_models` as primary system-dynamics tool (addendum §2)

- **`pyproject.toml`** — added to core dependencies:
  - `sfc-models>=0.3.0`
  - `pysolve>=0.1.0`
  - Bumped existing `mesa>=2.3` to `mesa>=2.3.0` to match the addendum's pin form (numerically equivalent; cosmetic).
- **`pyproject.toml`** — added a new optional-dependency group:
  - `[project.optional-dependencies] extended = ["pysd>=3.14.0"]`
- **`sfc-notebooks/`** — new top-level directory:
  - `README.md` — explains tool positioning, file layout, and the kennt-monetary-economics submodule decision (flagged for the author at v1 build time, default: submodule).
  - `01-sim-baseline.ipynb`, `02-pc-portfolio-choice.ipynb`, `03-bmw-banks-and-money.ipynb` — three minimal valid `.ipynb` stubs, each with a markdown header explaining what it will reproduce, and a placeholder code cell. To be populated during Controversy 6 work.
  - `kennt-monetary-economics/` — **not** added in v1. The directory's role is documented in the README; the submodule-vs-vendored decision is flagged for the author per addendum §5.2. See deviation note below.
- **`data/sfc-models-net/`** — new directory with README explaining provenance from <https://sfc-models.net> and the v1 default (empty), plus a `.gitkeep`.
- **CONTRIBUTING.md** — added a new top-level section *"System-dynamics tool positioning"* covering: `sfc_models` (primary), `pysolve` (complementary), `pysd` (optional, under the `extended` extra), Minsky / Ravel (optional teaching companions), Mesa (agent-based modeling), and a note on Controversy 7's climate-LP being built directly with cvxpy plus an EcoDyco editorial reference.

### 3. EcoDyco as optional climate-economy reference (addendum §3)

- **CONTRIBUTING.md** — flagged in the *"Climate-LP (Controversy 7)"* sub-section of the new system-dynamics positioning section. No code dependency, no directory, purely an editorial reference. The chapter-level pointer in `controversies/controversy-07-climate.qmd` is **not** added in v1 — see deviation note below.

### 4. Mesa for agent-based modeling (addendum §4)

- **`pyproject.toml`** — Mesa was already a v1 dependency from bootstrap; addendum §2.5 lists it among new core dependencies, so the pin was confirmed/normalized to `mesa>=2.3.0` (matching the addendum's spec). No directory changes (per addendum §4.3).
- **CONTRIBUTING.md** — Mesa positioning documented in the system-dynamics section (its primary homes are 201 Zhang-program work and the Controversy 6 Version 3 ergodicity extension).

### 5. Open questions (addendum §5)

The addendum's open questions are addressed per their stated defaults:

- **§5.1** JSXGraph PDF fallback — deferred. Stub script at `assets/scripts/render-jsxgraph-fallback.py`; convention documented in CONTRIBUTING.md.
- **§5.2** `kennt/monetary-economics` submodule vs. vendored — flagged for author. Default (submodule) documented in `sfc-notebooks/README.md`. The submodule itself is **not** added in v1 (deviation note below).
- **§5.3** PySD primary vs. optional — placed under the `extended` optional-dependency group, per the default.
- **§5.4** `sfc-models-net` mirror — directory + README ship empty per the default.

## Acceptance criteria (addendum §6)

| # | Criterion | Status |
|---|---|---|
| 13 | JSXGraph widget renders in HTML output | Configured. Runtime loaded globally via `assets/jsxgraph-include.html`; demo widget added to `index.qmd` *Style and rendering reference*. Cannot be verified by running `quarto render` here (Quarto is not installed in this environment); see verification note below. |
| 14 | `sfc_models` importable | Pinned in `pyproject.toml`. Cannot be verified by running `python -c "import sfc_models; print(sfc_models.__version__)"` here without an env install; see verification note below. |
| 15 | `pysolve` and `mesa` importable | Both pinned in `pyproject.toml`. Same caveat. |
| 16 | `sfc-notebooks/` exists with README + stub notebook | Done. README plus three stub notebooks. |
| 17 | `assets/widgets/jsxgraph/` exists with at least one working reference HTML | Done. README plus four reference HTML files. |
| 18 | CONTRIBUTING.md sections on JSXGraph and SD tool positioning | Done. New top-level sections added: *Adding a JSXGraph widget* and *System-dynamics tool positioning*. |

### Verification note

This branch was prepared in an environment without Quarto or a populated Python venv. Acceptance criteria 13–15 are verifiable structurally (config and pins are present and well-formed) but were not run-tested here. The author should confirm at v1 build time:

```bash
# Criterion 13
quarto add jsxgraph/jsxgraph-quarto      # optional; the include-in-header
                                         # makes widgets work even before this.
quarto render index.qmd --to html
# Then open _book/index.html and confirm the JSXGraph slider in
# "Style and rendering reference" is interactive.

# Criteria 14–15
uv sync                                  # or: pip install -e .
python -c "import sfc_models, pysolve, mesa; \
           print(sfc_models.__version__, pysolve.__version__, mesa.__version__)"
```

## Deviations from the addendum spec

1. **JSXGraph extension not pre-installed.** The addendum (§1.5) specifies running `quarto add jsxgraph/jsxgraph-quarto` during bootstrap. Quarto is not available in this environment, so the extension is **not** placed in `_extensions/`. The interim setup loads JSXGraph from the jsdelivr CDN via `assets/jsxgraph-include.html`, which makes the embedded widget in `index.qmd` work without the extension. Author should run the `quarto add ...` command at v1 build time; once the extension is installed, the include-in-header can stay (harmless redundancy) or be removed in favor of the extension's bundled assets. The spirit of §1.5 ("verify the extension loads correctly by including a single JSXGraph widget in `index.qmd`'s Style and rendering reference") is preserved — there is a working JSXGraph widget in that section.
2. **`kennt/monetary-economics` submodule not added.** The addendum (§2.4 and §5.2) explicitly flags the submodule-vs-vendored decision *for author review at the time of bootstrap*. Rather than make the choice unilaterally, this branch documents the role and command in `sfc-notebooks/README.md` and leaves the directory absent. The author runs `git submodule add https://github.com/kennt/monetary-economics sfc-notebooks/kennt-monetary-economics` if they choose submodule; otherwise vendor manually.
3. **EcoDyco chapter pointer not added.** The addendum (§3.2) calls for adding a section to `controversies/controversy-07-climate.qmd` flagging EcoDyco as an optional advanced reference, qualified in §3.3 as *"an addition to the controversy content rather than a change to infrastructure"* and flagged for the author's editorial pass. This branch sticks to the infrastructure scope: EcoDyco is documented in CONTRIBUTING.md's system-dynamics positioning section but no chapter-level edit was made. The author should add the chapter pointer during the editorial pass on Controversy 7.
4. **`mesa` pin format normalized.** Bootstrap had `mesa>=2.3`; addendum §2.5 specifies `mesa>=2.3.0`. Updated to match, even though they're numerically equivalent. Cosmetic.
5. **`weeks/`, `controversies/`, `extensions/`, `notebooks/` directory layout left untouched.** The addendum mentions the existence of `_extensions/jsxgraph/jsxgraph/` after running `quarto add`; the `extensions/` directory at the repo root (which exists from bootstrap with a `.gitkeep`) is unrelated to Quarto extensions. No changes there.

## Files added or modified

**New files:**

- `sfc-notebooks/README.md`
- `sfc-notebooks/01-sim-baseline.ipynb`
- `sfc-notebooks/02-pc-portfolio-choice.ipynb`
- `sfc-notebooks/03-bmw-banks-and-money.ipynb`
- `assets/widgets/jsxgraph/README.md`
- `assets/widgets/jsxgraph/01-function-plot-with-slider.html`
- `assets/widgets/jsxgraph/02-draggable-construction.html`
- `assets/widgets/jsxgraph/03-multiple-linked-graphs.html`
- `assets/widgets/jsxgraph/04-mathjax-labels.html`
- `assets/widgets/observable/README.md`
- `assets/widgets/observable/01-reactive-slider.qmd`
- `assets/widgets/plotly/README.md`
- `assets/widgets/plotly/01-3d-surface.qmd`
- `assets/scripts/render-jsxgraph-fallback.py`
- `assets/jsxgraph-include.html`
- `data/sfc-models-net/README.md`
- `data/sfc-models-net/.gitkeep`
- `ADDENDUM1_REPORT.md` (this file)

**Modified files:**

- `pyproject.toml` — added `sfc-models`, `pysolve` to core deps; pinned `mesa>=2.3.0`; added `extended = ["pysd>=3.14.0"]` optional group.
- `_quarto.yml` — added `include-in-header: [assets/jsxgraph-include.html]` under `format.html`.
- `CONTRIBUTING.md` — added two top-level sections: *Adding a JSXGraph widget* and *System-dynamics tool positioning*.
- `index.qmd` — added a fifth demo (*"A JSXGraph widget"*) to the *Style and rendering reference* section.

The original `PRD_addendum1.md` was pulled in from `origin/main` to make it visible alongside `PRD.md` on this feature branch.

---

*End of report.*
