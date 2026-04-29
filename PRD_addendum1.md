# Morishima Track — PRD Addendum 1

**Project name:** `morishima-track`
**Owner:** [your name]
**Date:** April 2026
**Status:** Draft for handoff to Claude Code
**Supersedes:** None. Augments and modifies `morishima_track_PRD.md` (the original PRD).

---

## How to read this document

This is an addendum to the original PRD. It contains *delta* changes only — new decisions, modifications to prior decisions, and additions to the repository structure that emerged from subsequent design conversations. Where this document conflicts with the original PRD, this document wins. Where this document is silent, the original PRD stands.

The changes break into four substantive areas plus a small set of incidental additions:

1. **Embedded math widgets:** A primary tool decision (JSXGraph) replacing the previously-implicit assumption that Plotly Python and Observable JS would carry all interactive math.
2. **System-dynamics modeling:** A primary tool decision (`sfc_models`) replacing the previously-vague "reserve space for Minsky/Ravel" approach. This is the larger of the two changes by impact.
3. **Climate-LP optional dependency:** A note about EcoDyco as a reference framework for Controversy 7.
4. **Agent-based modeling for the 201 placeholder:** Confirmation that Mesa is the right tool and a note about where it should live in the repo.

Plus minor additions to dependencies, directory structure, and open questions.

---

## 1. Embedded math widgets — JSXGraph as primary

### 1.1 Decision

JSXGraph is the primary tool for "type a function, see a graph" interactives embedded inline in the rendered HTML book. Observable JS via Quarto's native OJS support remains the tool for structured visualizations with custom UI (e.g., a sectoral economy visualized as a network with toggleable layers). Plotly Python remains the tool for static-but-interactive charts rendered into the page by the build process. Plotly Dash remains the tool for major standalone applications.

### 1.2 Rationale

JSXGraph is dual-licensed under LGPL and MIT, fully open-source, and developed at the University of Bayreuth. It has a dedicated Quarto extension at `jsxgraph/jsxgraph-quarto` on GitHub. The library is small (200KB minified), has been actively maintained for over fifteen years, and has no vendor or API-key dependencies. It supports MathJax for typeset labels.

The rejected alternative is Desmos. The Desmos API requires a partnership API key for production use, and while their team has historically been generous with educational and non-commercial requests, the project would depend on their goodwill rather than on a license. For a project whose substantive content critiques private platform capture and argues for non-market coordination, embedding a closed-source private API into the rendering layer is a values mismatch. JSXGraph is less polished visually than Desmos but produces clean, professional, lightweight graphs and is unambiguously aligned with the project's ethics.

GeoGebra was also considered and rejected. The GPL-with-exceptions license is workable, but GeoGebra is owned by Byju's (which entered bankruptcy proceedings in early 2024), and the embedding pattern depends on hosted infrastructure rather than a self-contained library. Self-hosting the GeoGebra Math Apps Bundle is possible but adds operational complexity.

### 1.3 What JSXGraph is best for

JSXGraph is fundamentally a 2D library. It is excellent for: function plots with parameter sliders, parametric curves, dynamic geometry constructions (drag a point, watch the dependent objects update), wage-profit frontier plots in Controversy 4, eigenvector visualizations in Week 4, indifference-curve-and-budget-line visualizations in Week 2, and similar moments throughout the syllabus where the reader is supposed to type or drag and see a curve respond.

It is *not* well-suited for: 3D surface plots (it can do parametric 3D-projected drawings, but not rotating mesh surfaces — Plotly Python does this better and renders cleanly into the static HTML page); complex custom UI with non-mathematical controls (Observable JS handles this); and full-scale interactive applications with state and routing (Plotly Dash handles this).

For Week 1's Cobb-Douglas surface project specifically, the recommended split is: 3D surface plot rendered as a static interactive Plotly Python figure (rotation works inline), 2D contour plot with draggable parameters as a JSXGraph widget, gradient-vector-perpendicular-to-level-set demonstration as a JSXGraph widget. This division uses each tool for what it does best.

### 1.4 Repository changes

Add a directory under `assets/`:

```
assets/
└── widgets/
    ├── jsxgraph/                    [dir]   Reference implementations of JSXGraph patterns
    │   ├── README.md
    │   ├── 01-function-plot-with-slider.html
    │   ├── 02-draggable-construction.html
    │   ├── 03-multiple-linked-graphs.html
    │   └── 04-mathjax-labels.html
    ├── observable/                  [dir]   Reference Observable JS widgets
    │   ├── README.md
    │   └── 01-reactive-slider.qmd
    └── plotly/                      [dir]   Reference Plotly Python figures
        ├── README.md
        └── 01-3d-surface.qmd
```

Each `.html` reference in `assets/widgets/jsxgraph/` is a complete standalone HTML page demonstrating one JSXGraph pattern. These are the canonical examples Claude Code (or the author) consults when adding new widgets to chapters. They are not embedded in the book directly but they are committed to the repo and visible when working.

### 1.5 Quarto integration

Install the JSXGraph Quarto extension during bootstrap:

```bash
quarto add jsxgraph/jsxgraph-quarto
```

This places the extension in `_extensions/jsxgraph/jsxgraph/`. Verify the extension loads correctly by including a single JSXGraph widget in `index.qmd`'s "Style and rendering reference" section (originally specified in §6 of the main PRD), as one of the four required demos. Replace the originally-specified Observable widget *or* add a JSXGraph demo as a fifth required demo — author's choice. The PRD's spirit (one working example of each pattern, committed) is preserved.

### 1.6 PDF rendering implications

JSXGraph widgets are HTML-only. They will not render in the PDF book. This is acceptable because the PDF is a secondary output and a static fallback by design. For chapters with critical JSXGraph widgets, the source `.qmd` should include a static PNG or SVG fallback rendered by a small Python script during the build, placed in the margin or inline so the PDF reader still sees the relevant figure. This is the same pattern used by interactive textbooks that need to ship static print editions.

Implementation detail: include a Python helper at `assets/scripts/render-jsxgraph-fallback.py` (stub for v1) that takes a JSXGraph configuration and produces a static SVG. v1 ships this as a TODO; the author can implement it when needed.

### 1.7 Modification to original PRD

This section §1 of the addendum **replaces** §3.4 of the original PRD ("Interactive widgets: a layered approach"), which specified Observable / Dash / Plotly Python. The new layering is:

- Inline math interactives → JSXGraph (new, primary).
- Inline structured visualizations with custom UI → Observable JS via Quarto OJS (unchanged).
- Static interactive plots and figures → Plotly Python (unchanged).
- Major standalone applications → Plotly Dash (unchanged).

---

## 2. System-dynamics modeling — `sfc_models` as primary

### 2.1 Decision

The `sfc_models` Python package by Brian Romanchuk is the primary system-dynamics tool for the project, specifically for the stock-flow consistent macroeconomic models in Controversy 6. The original PRD's positioning of Minsky and Ravel as "reserved directory space" is updated: they are repositioned as **optional teaching companions** rather than primary tooling.

`pysolve` (by kennt) is included as a complementary constraint solver.

`PySD` is included as an optional dependency for interoperability with the broader system-dynamics literature (loading models published in Vensim or XMILE format).

Mesa is confirmed as the agent-based modeling tool for the 201 placeholder course's Zhang-program work, and is added to the v1 dependencies.

### 2.2 Rationale

`sfc_models` is the de facto Python tool for stock-flow consistent macroeconomics in the post-Keynesian tradition. It implements the major models from Godley and Lavoie's *Monetary Economics* (SIM, PC, LP, BMW, OPEN, REG) under the `sfc_models.gl_book` subpackage, with validation against the textbook's eViews implementations. Apache 2.0 licensed. Available on PyPI. Brian Romanchuk presented the package at the First International Conference of Modern Monetary Theory in Kansas City in September 2017, which means it has been used and tested by the relevant academic community for nearly a decade. The author of this project has followed Romanchuk on social media and is comfortable with the architectural choices the package makes.

The key architectural feature of `sfc_models` is high-level sector specification: rather than writing the underlying equations directly, the user specifies economic sectors (households, firms, government, banks) and the package generates the equations. This matches how the Godley-Lavoie textbook actually presents the models pedagogically.

For Controversy 6 specifically, this means Versions 1 through 3 of the capstone project (baseline SIM, endogenous bank credit, Minsky-Keen fragility) can build on tested, validated baselines from `sfc_models.gl_book` rather than being implemented from scratch. The interesting work — Version 4, the planned-economy transformation that replaces banking with the Cockshott-Cottrell-Dapprich token apparatus — is then where the author's actual contribution lives. This division concentrates effort where it matters.

### 2.3 What gets built with what

For Controversy 6:

- *Version 1 (baseline SIM):* import directly from `sfc_models.gl_book.SIM`, simulate, plot.
- *Version 2 (endogenous bank credit):* extend Version 1 by adding a banking sector, using the package's sector-extension API.
- *Version 3 (Minsky-Keen financial fragility):* further extend Version 2, adding leverage dynamics and crisis triggers.
- *Version 4 (planned-economy transformation):* this is the original work. Built on top of the planning-LP machinery from Week 8 plus an intertemporal multi-period extension. Replaces `sfc_models`'s banking sector with a labor-token apparatus. Compared head-to-head against Versions 1-3 on the same underlying technology.

The ergodicity-economics extension to Version 3 (mentioned in the original syllabus) — simulating N firms with idiosyncratic leverage shocks — uses Mesa for the agent-based component layered over the `sfc_models` backbone.

For Controversy 7's climate-LP work:

- The 30-year decarbonization LP itself is built using cvxpy directly, not `sfc_models`. SFC and LP are different modeling paradigms.
- Optional reference: EcoDyco (see §3 of this addendum).

For Week 9 (differential equations):

- The Solow-model project remains a from-scratch implementation using `scipy.integrate.solve_ivp`. `sfc_models` is overkill for a single-equation continuous-time model.

For Week 10 (growth and stability):

- The Goodwin model phase-plane simulator remains a from-scratch implementation. The reasons are pedagogical — the point of the Week 10 project is to *build* the phase-plane analysis tooling, not to import it.

### 2.4 Repository changes

Add to the project root:

```
sfc-notebooks/                            [dir]   Reference implementations of Godley-Lavoie models
├── README.md                             [file]  Explains: these are working notebooks alongside Controversy 6
├── 01-sim-baseline.ipynb                 [stub]  Stub notebook; populated during Controversy 6 work
├── 02-pc-portfolio-choice.ipynb          [stub]
├── 03-bmw-banks-and-money.ipynb          [stub]
└── kennt-monetary-economics/             [submodule]  Optional git submodule cloning kennt/monetary-economics
    └── (managed externally)
```

The `kennt-monetary-economics/` subdirectory is added as a git submodule pointing at <https://github.com/kennt/monetary-economics>, which is the canonical reference implementation set for Godley-Lavoie. The author should evaluate whether to include this as a submodule (clean dependency tracking, easy to update) or vendor it (full local control, no external repo dependency). The PRD specifies submodule by default; flag for author review at the time of bootstrap.

Add to `data/`:

```
data/
└── sfc-models-net/                       [dir]   (optional) Mirror of canonical eViews files
    ├── README.md                         [file]  Explains provenance from <https://sfc-models.net>
    └── .gitkeep                          [stub]
```

The `sfc-models-net/` mirror is optional and only added if the author decides during Controversy 6 that having local copies of the canonical eViews files matters for archival purposes. v1 ships the directory and README empty.

### 2.5 Dependency changes

Add to `pyproject.toml`:

```toml
[project]
dependencies = [
    # ... existing dependencies ...
    "sfc-models>=0.3.0",          # Stock-flow consistent macroeconomic modeling
    "pysolve>=0.1.0",             # Constraint solver, complementary to sfc_models
    "mesa>=2.3.0",                # Agent-based modeling, for 201 placeholder work
]

[project.optional-dependencies]
extended = [
    "pysd>=3.14.0",               # System-dynamics interoperability (Vensim/XMILE loading)
]
```

The `extended` extra is opt-in. PySD has a heavier dependency footprint (it pulls in parsimonious, networkx-with-extras, and others), and the author may not need it depending on whether the project ever loads externally-published SD models.

### 2.6 Minsky and Ravel — repositioned

Per the original PRD, the directories `minsky-models/` and `ravel-files/` exist with READMEs explaining what the tools are. This is unchanged. What changes is the framing:

- Minsky is positioned as an *optional teaching companion* for Controversy 6. The recommended use: after implementing a Godley-Lavoie model in `sfc_models`, optionally rebuild the same model in Minsky to see how the visual representation differs from code. This is a one-paragraph exercise in the chapter, not a primary deliverable. Continuous-time SD; Keen's specialty.
- Ravel is positioned as an *optional data-analysis companion*, mainly for Controversy 5's BEA profit-rate empirical work and Controversy 7's emissions-data work. Commercial software (cheap, Patreon-distributed). Author's working files only; do not redistribute.

The CONTRIBUTING.md should explain this positioning so future readers don't expect the project to depend on these tools.

### 2.7 Modification to original PRD

This section §2 of the addendum **replaces** §3.5 of the original PRD ("System-dynamics modeling: Minsky, optionally Ravel"). The new framing leads with `sfc_models` as primary, with Minsky/Ravel as optional companions.

---

## 3. Climate-economy modeling — EcoDyco as optional reference

### 3.1 Note

For Controversy 7's 30-year decarbonization LP project, the primary implementation remains as specified in the syllabus: a multi-sector economy with technology matrix A, labor coefficients l, emissions coefficients e, built using cvxpy. This is the right scope for a course project.

For readers who want to see what a more sophisticated climate-economy SFC model looks like, EcoDyco is the natural reference. It's an open-source thermodynamic stock-flow consistent model published in *Scientific Reports* in 2023 by Gaël Giraud's group, integrating thermodynamic potentials and primary resource constraints into macroeconomic dynamics. The paper is "Macroeconomic dynamics in a finite world based on thermodynamic potential."

### 3.2 Repository changes

Add a section to `controversies/controversy-07-climate.qmd` (during content migration) flagging EcoDyco as an optional advanced reference. No code dependency. No directory needed. This is purely an editorial reference.

### 3.3 Modification to original PRD

This is an *addition* to the controversy content rather than a change to infrastructure. Flag for the author to review during the editorial pass on Controversy 7.

---

## 4. Agent-based modeling — Mesa confirmed for 201

### 4.1 Decision

Mesa is the agent-based modeling tool for the 201 placeholder's Zhang-program work, specifically for the producer-competition prisoner's-dilemma model and the multi-firm leverage-dynamics simulation referenced in the ergodicity sidebar of Controversy 6.

### 4.2 Rationale

Mesa is the standard Python framework for agent-based modeling. Apache 2.0 licensed, mature, well-documented, integrates cleanly with the rest of the scientific Python stack. NetLogo is the historical alternative but it's a separate language with its own runtime; Mesa lets agent-based work live alongside the rest of the project's Python code.

For the ergodicity-economics extension to Controversy 6 Version 3 (the optional fan-chart-of-N-firms simulation flagged in the syllabus), Mesa is the right tool.

For the 201 placeholder course's Zhang-program work (producer competition, realization uncertainty, primitive accumulation), Mesa is the right tool.

### 4.3 Repository changes

Mesa is added to `pyproject.toml` core dependencies (specified above in §2.5). No directory changes needed for v1; Mesa-based work happens in chapter notebooks and 201 follow-up work, both of which already have homes.

### 4.4 Modification to original PRD

Mesa was mentioned in the original PRD's §3.3 ("Computation: Python + Jupyter engine") as part of the standard scientific stack but was not committed to as a v1 dependency. This addendum upgrades that positioning.

---

## 5. Open questions added

These augment §11 of the original PRD.

### 5.1 JSXGraph fallback rendering

Whether to implement the static-SVG fallback for JSXGraph widgets in PDF output now (v1) or defer until a chapter actually needs it. Default: defer. Stub the helper script at `assets/scripts/render-jsxgraph-fallback.py` and document the convention in CONTRIBUTING.md, but don't implement until the first chapter needs it. The author should reconsider when reaching the first chapter with critical JSXGraph content.

### 5.2 `kennt/monetary-economics` as submodule vs vendored

Default to git submodule. If submodule update workflow proves annoying, the author can vendor (clone the contents into the project directly) at any point. Flag for the author to decide at v1 build time.

### 5.3 PySD as primary or optional dependency

Default to optional (under the `extended` extra). The author should re-evaluate if Controversy 7 ends up needing to load externally-published SD models. PySD is fine to add later; the cost of pulling it into core dependencies upfront is low but not zero.

### 5.4 `sfc-models-net` data mirror

Default to empty directory + README. The author should populate during Controversy 6 work only if local copies of canonical eViews files prove necessary for the project.

---

## 6. Acceptance criteria additions

These augment §10 of the original PRD.

13. JSXGraph widget renders correctly in HTML output via the Quarto extension (one widget visible in the "Style and rendering reference" section, responsive to interaction).
14. `sfc_models` is importable in the Python environment (`python -c "import sfc_models; print(sfc_models.__version__)"` succeeds).
15. `pysolve` and `mesa` are importable in the Python environment.
16. The `sfc-notebooks/` directory exists with README and at least one stub notebook.
17. The `assets/widgets/jsxgraph/` directory exists with at least one working reference HTML file.
18. CONTRIBUTING.md includes a section on adding JSXGraph widgets to chapters and a section on the system-dynamics tool positioning (`sfc_models` primary, Minsky/Ravel optional).

---

## 7. Handoff notes for Claude Code

If you (Claude Code) are reading this addendum as a task brief alongside the original PRD:

- Read the original PRD first, then read this addendum. Where they conflict, this addendum wins.
- The two largest concrete changes are: (a) install JSXGraph and its Quarto extension, configure the relevant section of `_quarto.yml`; (b) install `sfc_models`, `pysolve`, and `mesa` as core Python dependencies.
- The `sfc-notebooks/` directory is new and needs creation.
- The `assets/widgets/jsxgraph/` directory is new and needs creation, with at least one working JSXGraph reference HTML file (a slider-controlled function plot is sufficient).
- The original PRD specified Observable JS as the demo widget in `index.qmd`'s "Style and rendering reference" section. With JSXGraph now committed as primary for math interactives, *add a JSXGraph demo as a fifth required demo* alongside the four originally specified. Do not remove the Observable demo; both tools have legitimate roles.
- Update CONTRIBUTING.md to include the new conventions sections (JSXGraph widgets, system-dynamics tool positioning).
- Verify all six new acceptance criteria (§6 above) before declaring the bootstrap complete.
- The `BOOTSTRAP_REPORT.md` should explicitly note any deviations from this addendum as well as from the original PRD.

---

*End of PRD Addendum 1.*