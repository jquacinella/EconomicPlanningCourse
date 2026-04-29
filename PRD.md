# Morishima Track — Repository Bootstrap PRD

**Project name:** `morishima-track`
**Owner:** [your name]
**Date:** April 2026
**Status:** Draft for handoff to Claude Code

---

## 1. Background and motivation

This document specifies the initial repository structure, build pipeline, and architectural conventions for a multi-output computational-economics learning project. The substantive content — a 10-week mathematical-economics syllabus plus 7 in-depth heterodox-economic controversies plus a placeholder for a 201-level follow-on — already exists as a single 138 KB markdown document called `morishima_syllabus.md`. This PRD does not specify the *content* of that work; it specifies the *infrastructure* to host, build, render, and extend it.

The project's deliverable is intentionally hybrid:

1. A **printable book** (PDF, possibly EPUB, eventually print-on-demand) that someone could read cover-to-cover offline.
2. An **interactive online edition** (HTML website with executable code, embedded interactive widgets, and live web annotation) that complements the print form.
3. A **repository of project work** (Jupyter notebooks, standalone Dash applications, system-dynamics model files) that constitute the actual learning deliverables of the course.

The aspirational reference points for the design are: QuantEcon's Sargent-Stachurski lecture series (best-in-class executable-textbook pattern); Edward Tufte's books and the *Tufte handouts* style (marginalia as first-class typographic citizens); Reif Larsen's *The Selected Works of T. S. Spivet* (marginalia as narrative apparatus that transforms a book into an interactive read); and the Hypothesis annotation ecosystem (web annotation as a complementary social layer on top of the published text).

This is a learning project first, a publishable artifact second. The infrastructure should not get in the way of the math, but it should also not foreclose the publication path. The PRD threads that needle by frontloading the architecture choices that are easy to make now and expensive to retrofit later, while leaving content-level decisions to the author week-by-week.

---

## 2. Goals and non-goals

### Goals

- A working Quarto book project at `/morishima-track/` with the existing syllabus split into per-chapter `.qmd` files.
- Render targets: HTML site (primary), PDF book (secondary), EPUB (tertiary).
- CI/CD pipeline that auto-builds and deploys the site on push to `main`.
- Tufte-style marginalia working in both HTML and PDF outputs from the same source.
- Hypothesis annotation enabled on the HTML site (one-line config).
- Skeleton directory structure for project notebooks, standalone Dash apps, system-dynamics model files (Minsky / Ravel), and supporting data.
- A demo Dash app, a demo Observable widget, a demo marginalia note, and a demo Hypothesis-annotated paragraph — each implemented once so the patterns are reference-able when content is added later.
- Documentation: a `CONTRIBUTING.md` that explains the conventions for someone (the author, future collaborators, or Claude Code on follow-up tasks) extending the repo with new content.

### Non-goals

- Migrating any *content* beyond what's in the existing syllabus markdown. This PRD is about infrastructure. Each week's actual coding work is for the author to do during the course itself.
- Print-on-demand setup, ISBN registration, or publisher-specific styling (Pluto Press, Lulu, etc.). Defer until at least Controversy 3 of the course is written and the author has views about audience.
- Custom domain registration. Default to GitHub Pages or Quarto Pub URL initially.
- Self-hosting Hypothesis. Use the public service.
- Translation pipeline for Chinese-language Zhang sources. Out of scope for v1.
- Any of the actual coding projects from the course (Cobb-Douglas surfaces, planning LP, SFC models, etc.). Those are the author's work; the repo just needs to be ready to receive them.

---

## 3. Tech stack decisions

These are settled. Where a decision is genuinely contested, this section says so.

### 3.1 Source format: Quarto

**Decision:** Quarto, latest stable release (1.9 or later as of the build date).

**Rationale:** Quarto is a superset of Jupyter Book that does everything Jupyter Book does plus better PDF output via Typst, multiple-language code blocks in the same file, and native support for the marginalia and annotation features the project specifically wants. Used by the new generation of QuantEcon material, by Hadley Wickham's books, and by an increasing fraction of computational-textbook projects. The migration cost from raw Markdown is small (largely YAML front-matter and code-block syntax differences).

**Alternatives considered:**
- *Jupyter Book*: Older, being supplanted, less clean PDF output.
- *MyST-NB*: A subset of what Quarto offers; would lock the project into the Sphinx ecosystem.
- *Plain Markdown + Pandoc*: Workable but loses native code-execution and the polish features.

### 3.2 PDF backend: Typst (with LaTeX fallback)

**Decision:** Use Typst as the primary PDF backend, with LaTeX kept available as a fallback for any feature that doesn't render cleanly in Typst.

**Rationale:** Typst's Marginalia package gives clean, automatic Tufte-style marginalia in PDF output, paired with the same `.column-margin` class in HTML. LaTeX with `tufte-latex` works but is finicky and has known compile issues with Quarto (see the Warrick Ball blog post referenced in research, where the author had to `sed`-out problematic preamble lines). Typst is the Quarto team's recommended path forward.

**Alternatives considered:** LaTeX via `tufte-latex` (older but more battle-tested for Tufte-style books); LaTeX via `memoir` class with custom marginalia setup (more flexible but a lot of plumbing).

### 3.3 Computation: Python + Jupyter engine

**Decision:** Python is the primary computation language, executed via Quarto's Jupyter engine. Standard scientific stack: NumPy, SciPy, SymPy, Matplotlib, Plotly, PuLP, CVXPY, Pandas, NetworkX, statsmodels, Mesa.

**Rationale:** Author has Python expertise. The libraries needed for the course are all Python-native. Jupyter engine integration with Quarto is mature.

**Environment:** A Conda or `uv` virtual environment named `morishima-env`. The PRD specifies `uv` as the preferred tool because it's faster, has clean lockfile semantics, and is becoming the default in scientific Python. Fallback to `pip + venv` if `uv` is unfamiliar — both are documented.

### 3.4 Interactive widgets: a layered approach

**Decision:** Three separate tools for three separate purposes.

- **Inline static interactivity (sliders next to paragraphs, parameter exploration in margin):** Observable JS, embedded via Quarto's native OJS support. No separate deployment.
- **Major standalone applications (planning LP simulator, SFC model dashboard, climate-LP interactive):** Plotly Dash, deployed independently to Render or Fly.io, linked from the relevant chapter pages.
- **Static plots and small interactive charts:** Plotly Python, rendered directly into HTML output by Quarto.

**Rationale:** Different tools have different sweet spots. Observable for "drag this slider and see the curve change" — small, embedded, no infrastructure. Dash for "this is a real app with state and complex inputs" — separate deployment, can be linked but not embedded. Plotly Python for the bulk of static-but-interactive visualization. Trying to make any one of these tools do all three jobs produces brittle results.

**Constraint for v1:** Build *one* Dash app, *one* Observable widget, *one* Plotly Python figure as reference implementations. Don't build the actual course content — just the patterns.

### 3.5 System-dynamics modeling: Minsky, optionally Ravel

**Decision:** Reserve directory space for `.mky` (Minsky model) files and `.rvl` (Ravel data) files. Do not require them to be present in v1.

**Rationale:** Minsky is open-source and free; Ravel is commercial (Patreon-distributed). Both are Steve Keen's tools and most relevant to Controversy 6 (monetary theory of production) and possibly Controversy 5 (empirical profit-rate analysis). The course can complete without them, but they earn space if the author wants to use them as supplementary tools. The repo just needs to know where they go.

**Constraint:** Do not make the build depend on Minsky or Ravel being installed. They're tools for the author, not for readers.

### 3.6 Annotations: Hypothesis + native marginalia

**Decision:** Two complementary annotation layers.

- **Marginalia:** Quarto's native `.column-margin` (HTML) plus Typst's Marginalia package (PDF). These are *authored* notes — the author writes them as part of the source markdown and they appear in the margin in both renderings. This is the "T. S. Spivet" layer.
- **Hypothesis:** Enabled on the HTML site via Quarto's one-line config (`comments: hypothesis: true`). This is the *social* layer — readers (or the author later, on a re-read) annotate the published text from outside. Annotations don't appear in the printed PDF.

**Rationale:** These are doing different jobs. Marginalia are part of the work; Hypothesis annotations are a conversation about the work. Wanting both is correct. Both have native Quarto support, neither requires custom infrastructure beyond config.

**Open question (not blocking v1):** whether to set up a Hypothesis private group for early-draft annotation versus exposing public annotations from day one. Default to public; the author can create a group later if it matters.

### 3.7 Hosting and deployment

**Decision:**
- Quarto site → GitHub Pages (free, custom domain capable, integrated with the same repo).
- Dash apps → Render (free tier sufficient for low-traffic learning project).
- PDF artifact → linked from the site, hosted as a release asset on GitHub.
- Repository → GitHub, public by default but configurable to private.

**CI:** GitHub Actions workflow runs `quarto render` on push to `main`, deploys to `gh-pages` branch.

**Rationale:** All-free, all-standard, no vendor surprises. If the project ever gets serious enough to need a custom domain, swap in a CNAME on GitHub Pages — five-minute change.

---

## 4. Repository structure

The skeleton to create. Each item is either `[file]`, `[dir]`, or `[stub]` (an empty placeholder file with a `.gitkeep` or minimal contents to make the directory commit cleanly).

```
morishima-track/
├── README.md                          [file]   Brief project description, links to rendered site, build instructions
├── LICENSE                            [file]   MIT or CC-BY-SA 4.0; PRD says CC-BY-SA-4.0 since it's primarily a written work
├── CONTRIBUTING.md                    [file]   Conventions for adding content; see §6
├── _quarto.yml                        [file]   Quarto project config; see §5
├── index.qmd                          [file]   Front matter, "How to use this document" — extracted from §1 of the existing syllabus
├── master-resources.qmd               [file]   Master resource list — extracted as-is
│
├── weeks/                             [dir]    The 10-week math curriculum
│   ├── week-01-multivariable.qmd      [file]
│   ├── week-02-constrained.qmd        [file]
│   ├── week-03-linear-algebra.qmd     [file]
│   ├── week-04-eigenvalues.qmd        [file]
│   ├── week-05-economic-opt.qmd       [file]
│   ├── week-06-lp-duality.qmd         [file]
│   ├── week-07-input-output.qmd       [file]
│   ├── week-08-planning.qmd           [file]
│   ├── week-09-diff-eq.qmd            [file]
│   └── week-10-growth-stability.qmd   [file]
│
├── post-course.qmd                    [file]   Post-course reading ladder — extracted as-is
│
├── controversies/                     [dir]    The 7 in-depth controversies + 1 seminar
│   ├── controversy-01-cobb-douglas.qmd        [file]
│   ├── controversy-02-calculation.qmd         [file]
│   ├── controversy-03-transformation.qmd      [file]
│   ├── controversy-04-sraffa.qmd              [file]
│   ├── controversy-05-okishio.qmd             [file]
│   ├── seminar-chinese-critique.qmd           [file]
│   ├── controversy-06-money.qmd               [file]
│   └── controversy-07-climate.qmd             [file]
│
├── 201/                               [dir]    Placeholder for the follow-on course
│   └── placeholder.qmd                [file]
│
├── where-this-lands.qmd               [file]   Closing reflection
│
├── appendices/                        [dir]
│   ├── appendix-a-prereq.qmd          [file]
│   ├── appendix-b-extra-depth.qmd     [file]
│   └── appendix-c-absorption.qmd      [file]
│
├── apps/                              [dir]    Standalone Dash applications
│   ├── README.md                      [file]   Explains the conventions: each app is its own subdir with its own requirements.txt and Dockerfile
│   ├── _template/                     [dir]    Reference template for new apps; see §7
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   ├── render.yaml                Render deployment manifest
│   │   └── README.md
│   └── demo-budget-explorer/          [dir]    The reference Dash app — Cobb-Douglas budget constraint explorer
│       ├── app.py
│       ├── requirements.txt
│       ├── Dockerfile
│       ├── render.yaml
│       └── README.md
│
├── notebooks/                         [dir]    Working Jupyter notebooks before content gets pulled into qmd
│   └── .gitkeep                       [stub]
│
├── data/                              [dir]    Data files (BEA tables, BIS data, IO tables, emissions coefficients)
│   ├── README.md                      [file]   Explains data provenance conventions
│   └── .gitkeep                       [stub]
│
├── minsky-models/                     [dir]    Steve Keen Minsky model files (.mky)
│   ├── README.md                      [file]   Explains what Minsky is and where to download
│   └── .gitkeep                       [stub]
│
├── ravel-files/                       [dir]    Steve Keen Ravel files (.rvl), commercial tool
│   ├── README.md                      [file]   Explains what Ravel is and that files here are author's working files, not redistributable
│   └── .gitkeep                       [stub]
│
├── assets/                            [dir]    Images, custom CSS, fonts
│   ├── css/
│   │   └── custom.scss                [file]   Custom SCSS overrides — initially mostly empty
│   ├── images/
│   │   └── .gitkeep                   [stub]
│   └── fonts/
│       └── .gitkeep                   [stub]
│
├── extensions/                        [dir]    Quarto extensions if needed (initially empty)
│   └── .gitkeep                       [stub]
│
├── notes/                             [dir]    Personal reading notes — listed in .gitignore in v1, can be re-included on a separate branch
│   └── .gitkeep                       [stub]
│
├── pyproject.toml                     [file]   Python project metadata, uv-compatible
├── uv.lock                            [file]   Generated by uv lock
├── .python-version                    [file]   Python version pin (3.11 recommended)
├── .gitignore                         [file]   Standard Python + Jupyter + macOS + Quarto ignores; also notes/, .quarto/, _site/, _book/, ravel-files/*.rvl
├── .gitattributes                     [file]   For binary files (images, .ipynb if any survive)
│
└── .github/
    └── workflows/
        ├── render.yml                 [file]   GitHub Actions workflow for build + deploy on push to main
        └── lint.yml                   [file]   Optional: lint markdown, check broken links
```

---

## 5. `_quarto.yml` configuration

The complete file should be generated. Key settings the build must honor:

```yaml
project:
  type: book
  output-dir: _book

book:
  title: "The Morishima Track"
  subtitle: "A Computational-Economics Curriculum from Multivariable Calculus to Climate-Constrained Planning"
  author: "MetaCoding Solutions"
  date: "today"
  search: true
  repo-url: "https://github.com/jquacinella/EconomicPlanningCourse.git"
  repo-actions: [edit, source, issue]
  downloads: [pdf, epub]
  sharing: [twitter, mastodon]
  cover-image: assets/images/cover.png   # placeholder; cover image not in scope for v1
  page-navigation: true
  
  chapters:
    - index.qmd
    - master-resources.qmd
    - part: "Part I — The Mathematics"
      chapters:
        - weeks/week-01-multivariable.qmd
        - weeks/week-02-constrained.qmd
        - weeks/week-03-linear-algebra.qmd
        - weeks/week-04-eigenvalues.qmd
        - weeks/week-05-economic-opt.qmd
        - weeks/week-06-lp-duality.qmd
        - weeks/week-07-input-output.qmd
        - weeks/week-08-planning.qmd
        - weeks/week-09-diff-eq.qmd
        - weeks/week-10-growth-stability.qmd
    - post-course.qmd
    - part: "Part II — The Controversies"
      chapters:
        - controversies/controversy-01-cobb-douglas.qmd
        - controversies/controversy-02-calculation.qmd
        - controversies/controversy-03-transformation.qmd
        - controversies/controversy-04-sraffa.qmd
        - controversies/controversy-05-okishio.qmd
        - controversies/seminar-chinese-critique.qmd
        - controversies/controversy-06-money.qmd
        - controversies/controversy-07-climate.qmd
    - 201/placeholder.qmd
    - where-this-lands.qmd
  
  appendices:
    - appendices/appendix-a-prereq.qmd
    - appendices/appendix-b-extra-depth.qmd
    - appendices/appendix-c-absorption.qmd

format:
  html:
    theme:
      light: [cosmo, assets/css/custom.scss]
      dark: [cosmo, assets/css/custom-dark.scss]
    toc: true
    toc-depth: 3
    toc-location: right
    grid:
      margin-width: 350px        # Tufte-style wide margins for marginalia
    reference-location: margin   # Footnotes render in the margin
    citation-location: margin    # Citations render in the margin
    code-tools: true
    code-fold: show              # Code is shown by default but foldable
    fig-cap-location: margin
    comments:
      hypothesis: true           # Hypothesis annotation enabled site-wide
    
  pdf:
    documentclass: scrbook
    papersize: a4
    pdf-engine: typst            # Use Typst for clean Marginalia support
    # If Typst proves insufficient, fall back to:
    # pdf-engine: xelatex
    # documentclass: tufte-book
  
  epub:
    toc: true
    toc-depth: 2

execute:
  freeze: auto                   # Re-execute only when source changes; cache otherwise
  echo: true
  warning: false
```

The build must verify that `quarto render` succeeds for HTML, PDF, and EPUB targets. If Typst PDF rendering has unresolved issues for any of the syllabus content, document the issue in `CONTRIBUTING.md` and fall back to LaTeX (`xelatex` engine, `scrbook` document class with manual marginalia setup).

---

## 6. Content extraction and migration

The existing 138 KB `morishima_syllabus.md` lives in the project root at the start of this work and should be extracted into the per-chapter `.qmd` files specified in §4.

### Extraction rules

- Each `## Week N` section in the source becomes one `.qmd` file under `weeks/`.
- Each `## Controversy N` section becomes one `.qmd` file under `controversies/`.
- The seminar section becomes `seminar-chinese-critique.qmd`.
- The 201 placeholder becomes `201/placeholder.qmd`.
- The "Where this lands" closing becomes `where-this-lands.qmd`.
- Each appendix becomes a separate file.
- Section headings within each extracted file should be demoted by one level (so `## Week 1` becomes the `.qmd` file's title via YAML front matter, and the within-section `**Framing**`, `**Learning objectives**`, etc. headings become `## Framing`, `## Learning objectives` proper headings).

### YAML front matter for each chapter

Every `.qmd` file should have YAML front matter following this template:

```yaml
---
title: "Week 1 — Multivariable Calculus"
description: "Functions of several variables, gradients, and the chain rule"
order: 1
---
```

The `order` field is optional but useful for sorting. The `description` should be a single sentence pulled from the chapter's "framing" paragraph.

### Marginalia migration

Several places in the existing source naturally call for marginalia treatment in the rendered output. These should be flagged as `TODO: marginalia candidate` comments in the migrated `.qmd` files but **not** automatically converted. Reason: marginalia is editorial; the author should decide what becomes a margin note when reading through. Examples that should get the TODO flag:

- Side comments parenthetically attached to main paragraphs (e.g., "the third volume of *Capital* is...").
- Footnote-style asides currently rendered as italicized parentheses.
- The "Ergodicity sidebar" sections in Controversies 5 and 6 — these are already structurally sidebar-ish and could become full-width sidebars or expanded marginal columns.

### Demo content

The build must include exactly *one* worked example of each rendering pattern, located in a clearly-labeled section of `index.qmd` titled "Style and rendering reference". This section should contain:

- A `.column-margin` div with sample text — to verify HTML marginalia.
- A footnote that gets pushed to the margin via `reference-location: margin`.
- A single Plotly Python figure that renders inline.
- A single Observable widget — a slider tied to a simple plot — to verify OJS embedding works end-to-end.
- A Hypothesis-annotatable paragraph with explicit instructions in the surrounding text on how to highlight and annotate.
- A link to the demo Dash app.

This section serves as a living style reference for the author when adding content later. It should be visible in the rendered site but explicitly noted as a developer reference, not part of the substantive book.

---

## 7. Dash app pattern

The reference template at `apps/_template/` and the demo at `apps/demo-budget-explorer/` should follow this pattern.

### Each Dash app is

- A self-contained Python project under `apps/<app-name>/`.
- Has its own `requirements.txt` (not shared with the book's `pyproject.toml`).
- Has its own `Dockerfile` for deployment.
- Has a `render.yaml` for deploying to Render.
- Has its own `README.md` explaining what the app does, how to run it locally, and the deployed URL.

### The demo: Cobb-Douglas budget explorer

A simple Dash app with:
- Two sliders: one for α (Cobb-Douglas exponent), one for income M.
- Two fixed-input fields: prices p₁ and p₂.
- Plot output: budget line, three indifference curves, optimum point.
- Display: the optimum (x*, y*), the indirect utility u*, the Lagrangian multiplier λ*.

Locally runnable via `cd apps/demo-budget-explorer && pip install -r requirements.txt && python app.py`.

This implements a stripped-down version of the Week 2 Cobb-Douglas project specified in the syllabus. It exists to validate the deployment pattern, not to be the actual Week 2 deliverable.

### Linking from the book

In `weeks/week-02-constrained.qmd`, the migrated content should include a callout box linking to the deployed demo:

```markdown
::: {.callout-note}
## Interactive companion
A live version of this week's Cobb-Douglas constrained optimization is available at: [budget-explorer.morishima-track.app](#)

(Replace with actual deployed URL once Dash app is deployed.)
:::
```

---

## 8. CI/CD pipeline

### `.github/workflows/render.yml`

On push to `main`:

1. Set up Python 3.11.
2. Install Quarto (latest stable).
3. Install Python dependencies via `uv sync` (or `pip install -e .` as fallback).
4. Run `quarto render` for HTML, PDF, EPUB.
5. Deploy `_book/` to `gh-pages` branch using `peaceiris/actions-gh-pages@v3`.
6. Upload the generated PDF and EPUB as release assets on tagged releases.
7. Validate: build must complete in under 10 minutes for the v1 skeleton (the existing markdown content has no executable code yet, so this should be fast). Add a comment in the workflow noting that this budget will need to be revisited as the author adds executable code.

### `.github/workflows/lint.yml`

On pull request:

1. Run `markdownlint` on `.qmd` files (with appropriate Quarto exceptions configured).
2. Run a broken-link checker (`lychee` is recommended) over the source files.
3. Verify all internal cross-references resolve.

This is optional for v1 but should be set up so the author isn't fighting broken links later.

---

## 9. Documentation deliverables

### `README.md` (project root)

- One-paragraph description of the project.
- Link to the rendered site.
- "Quick start" section with three commands to clone, install, and render locally.
- Link to `CONTRIBUTING.md` for conventions.
- License notice (CC-BY-SA-4.0 for content, MIT for code).
- Acknowledgments paragraph (Quarto, QuantEcon, Cockshott et al., Zhang, Keen) — this should be brief and gracious, naming the people whose work this project depends on.

### `CONTRIBUTING.md`

A conventions document for adding new content. Sections:

- *Adding a new chapter or week:* file naming, YAML front matter template, where to add it in `_quarto.yml`.
- *Adding marginalia:* the `.column-margin` syntax with examples; what kinds of content belong in margins versus inline.
- *Adding code blocks:* execution conventions, fig-cap conventions, when to use `column: margin` for figures.
- *Adding a Dash app:* copy `_template/`, modify, deploy.
- *Adding an Observable widget:* the OJS code-block pattern.
- *Adding data files:* provenance documentation expected in `data/README.md`.
- *Cross-referencing:* how to link between chapters, how to cite external sources via Quarto's `@key` syntax.
- *Building locally:* `quarto preview` workflow, common gotchas.
- *Hypothesis annotation:* basic etiquette and how to set up a private group if desired.

### `data/README.md`

- Provenance is mandatory for any data file checked in.
- Format: data filename, source URL, retrieval date, license terms, brief description.

### `apps/README.md`

- Conventions: each app has its own subdirectory, requirements file, Dockerfile, render.yaml, README.
- How to deploy to Render.
- How to update the linked URL in the chapter when the deployment URL changes.

### `minsky-models/README.md` and `ravel-files/README.md`

- One-line description of what the tool is and where to download.
- Link to Steve Keen's tutorials.
- Note that Ravel files may be the author's working files and may not be redistributable depending on the data they contain.

---

## 10. Acceptance criteria

The bootstrap is complete when all of the following are true:

1. `quarto render` runs to completion locally on macOS (M-series) without errors, producing all three output formats (HTML, PDF, EPUB).
2. `quarto preview` serves the site locally and live-reloads on file changes.
3. The HTML output displays the demo `.column-margin` element correctly (margin text visible to the right of body text on screens wider than ~1100px).
4. The PDF output displays Tufte-style margin notes via Typst Marginalia, with sidenotes on the outer margin of each page.
5. The Hypothesis sidebar appears on the deployed site (loads the Hypothesis client; clicking the icon expands the panel).
6. The demo Observable widget responds to slider input.
7. The demo Dash app runs locally via `python app.py` and is reachable at `localhost:8050`.
8. GitHub Actions workflow runs successfully on a test commit and deploys to `gh-pages`.
9. The Quarto site, once deployed to GitHub Pages, is reachable via a public URL.
10. All `.qmd` files referenced in `_quarto.yml` exist and contain (at minimum) the migrated content from the source markdown plus correct YAML front matter.
11. `CONTRIBUTING.md` is complete and covers all six conventions sections listed in §9.
12. The project repository can be cloned by a fresh user, installed via `uv sync`, and built without manual intervention beyond having Quarto and `uv` already installed.

### Out of scope for acceptance (revisit later)

- Custom domain.
- Real cover image.
- Production-grade Dash app deployment (the demo is a smoke test, not a final UI).
- Non-trivial substantive content beyond what's in the existing markdown source.
- Testing with screen readers or other accessibility tooling (worth doing but not for v1).

---

## 11. Open questions

These are flagged for the author to think about, not for Claude Code to resolve.

1. **Public versus private repository at v1.** Default is public. A case can be made for starting private, then opening up around Controversy 3. Resolution before commit.

2. **Author identification.** The PRD uses placeholders. The author should resolve real-name vs pseudonymous before the README and YAML go in. Name choices have downstream consequences (citation, future publication).

3. **License.** PRD recommends CC-BY-SA-4.0 for content and MIT for code. The author may have different views, especially if a publisher relationship later might constrain licensing.

4. **Hypothesis groups.** Open question whether to start with a public Hypothesis group or a private one. Default: public, but reconsider after Controversy 3.

5. **Build target Python version.** PRD recommends 3.11 for stability. 3.12 should also work; 3.13 may have library compatibility issues with `cvxpy` or `quantecon`. The author should pin a known-good combination at `pyproject.toml`-level.

6. **Print publisher path.** Out of scope for v1, but the author should think about whether a future Pluto Press relationship is realistic. If so, the manuscript style should be compatible with their template requirements early.

---

## 12. Handoff notes for Claude Code

If you (Claude Code) are reading this PRD as a task brief:

- Read this entire document before making changes. The architecture decisions in §3 are settled and should not be re-litigated.
- Work top-down through §4, §5, §6, §7, §8, §9, then verify §10. Do not skip §6 (content migration) — the existing markdown source is in the repo root at the start, and the per-chapter extraction is the largest single piece of work in this PRD.
- The Cobb-Douglas demo Dash app in §7 should be a real, working app with the specified features, not a placeholder. It exists to validate the deployment pattern end-to-end.
- For the demo Observable widget in §6, a single-slider example tied to a single plot is sufficient — does not need to be substantively interesting; it just needs to demonstrate the OJS pipeline works.
- If any of the Typst PDF marginalia rendering has unresolved issues, document them in `CONTRIBUTING.md` and fall back to LaTeX with `tufte-latex`. Do not block the rest of the build on this.
- When in doubt about content, *do not invent*. The existing `morishima_syllabus.md` is the source of truth for content. The PRD is the source of truth for infrastructure.
- Verify all internal links and cross-references in the rendered output before declaring acceptance. Broken links are a common failure mode in book-style projects with many chapters.
- The `notes/` directory is gitignored on purpose. Do not check in placeholder content there.
- After the bootstrap is complete, write a short `BOOTSTRAP_REPORT.md` at the repo root summarizing what was built, any deviations from the PRD, and any open issues. Delete the file after the author reads it.

---

*End of PRD.*
