# Heterodox Econ Courses + Research

A monorepo of computational-economics courses *and* research projects built as Quarto books with executable Python, interactive widgets, Hypothesis annotation, and Obsidian notes vaults. Each book has a polished render track and a working-notes track.

The deployed site lives at: **https://jquacinella.github.io/EconomicPlanningCourse/**

## Two registers: courses and research

The repo distinguishes between two registers. **Courses** (`courses/`) are paced curricula with implementation projects, intended for someone working through the material in order. **Research projects** (`research/`) are long-form, slow, publication-oriented, reading-and-reflection programs without fixed pacing or exercises.

## Courses

| Course | Status | Description |
|--------|--------|-------------|
| [The Calculation Course](courses/the_calculation_course/) | In progress | 10-week math arc (calculus → LP → IO → dynamics) + 7 heterodox controversies → climate-constrained planning |

## Research projects

| Project | Status | Description |
|---------|--------|-------------|
| [Marxian Formalization](research/marxian_formalization/) | Stub | Computational reconstruction of Zhang's Marxian formalization program — game theory, probability, cybernetics applied to Vol I |
| [Postcapitalism After AI](research/postcapitalism_after_ai/) | Stub | Reading and writing program on the late-2025 socialism / AI / postcapitalism debate (Morozov, Benanav, Weatherby, Mason) and its conceptual hinterland; absorbs the prior crypto-course material as one of six threads |

## Repository layout

```
EconomicPlanningCourse/
├── courses/
│   └── the_calculation_course/   ← The Calculation Course (book + notes + apps + data)
│
├── research/
│   ├── marxian_formalization/    ← Marxian Formalization research project (stub)
│   └── postcapitalism_after_ai/  ← Postcapitalism After AI research track (stub)
│
├── shared/
│   ├── _quarto-base.yml          ← Shared Quarto format/theme config (inherited by all books)
│   ├── assets/                   ← Shared CSS, fonts, images, scripts, widgets
│   └── extensions/               ← Shared Quarto extensions
│
├── site-root/
│   └── index.html                ← Catalog landing page (deployed at /)
│
├── quartz/                       ← Quartz install (renders all notes/ vaults)
│   └── content/                  ← Per-book symlinks → <path>/notes/
│
├── tests/                        ← Repo-level tests
├── .github/workflows/            ← CI/CD (render matrix + deploy)
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

Each course or research project directory has the same internal structure:

```
courses/<name>/   or   research/<name>/
├── _quarto.yml          ← Course book config (inherits from shared/_quarto-base.yml)
├── index.qmd            ← Course landing page
├── weeks/               ← Weekly chapters (.qmd)
├── controversies/       ← Controversy chapters (.qmd)  [calculation course only]
├── appendices/          ← Appendix chapters (.qmd)     [calculation course only]
├── notes/               ← Obsidian vault (scratch notes, rendered by Quartz)
│   ├── _meta/           ← workflow.md, progress.md, decisions.md, deferred.md
│   ├── _book-aliases/   ← Wiki-link targets pointing back to book chapters
│   └── weeks/           ← Per-week notes directories
├── notebooks/           ← Working Jupyter notebooks
├── apps/                ← Standalone Dash apps (deployed separately)
├── data/                ← Data files
├── pyproject.toml       ← Course-specific Python dependencies
└── .python-version      ← Python version pin
```

## Quick start

### The Calculation Course

```bash
git clone https://github.com/jquacinella/EconomicPlanningCourse.git
cd EconomicPlanningCourse/courses/the_calculation_course
uv sync                      # install Python dependencies
quarto preview               # serve the book at http://localhost:4444
```

For the notes track:

```bash
cd ../../quartz
bash setup.sh                # first time only — fetches Quartz v4
npm ci
npx quartz build --serve     # serve notes at http://localhost:8080
```

### Other courses or research projects

Same pattern — `cd courses/<name>` or `cd research/<name>` then `uv sync` and `quarto preview`.

### Day-to-day editing (live reload)

For active study and writing, use the live-reload dev servers — not `make preview`:

```bash
# Calculation Course book — live reload at http://localhost:4444
make dev

# Notes site — live reload at http://localhost:8080
make dev-notes
```

`make dev` runs `quarto preview` which watches `.qmd` files and rebuilds only the changed page on save. Code cells use `freeze: auto` caching so only cells whose source changed are re-executed — subsequent saves are near-instant.

### Full-site preview (one-shot, before pushing)

The landing page (`site-root/index.html`) uses root-relative links that only work when the full stitched `_site/` is served from its root. Use this to check the complete site before a push:

```bash
# Build everything (all courses + Quartz notes) and serve at http://localhost:9200
make preview

# Override the port:
make preview PORT=8080

# Build without serving:
make build

# Build only the Calculation Course:
make build-calc

# Clean all build outputs:
make clean
```

`make help` lists all targets. Prerequisites: `quarto`, `uv`, `node`/`npm` (with Quartz set up via `quartz/setup.sh`).

To edit the landing page, open `site-root/index.html` directly — it's self-contained HTML/CSS with no dependencies or framework. Add a new course card by copying one of the existing `<div class="course-card">` blocks and updating the title, description, links, and badge.

### Build all artifacts

```bash
# From inside a course directory:
quarto render                # all formats (HTML, PDF, EPUB)
quarto render --to html      # HTML only

# Print-targeted PDF (strips author-notes callouts first):
python ../../shared/assets/scripts/strip-author-notes.py
QUARTO_PROFILE=print quarto render build-print/ --to pdf
```

## Adding a new course or research project

Substitute `courses/<new>` for a course or `research/<new>` for a research project below.

1. `mkdir -p <courses|research>/<new>/{notes/_meta,notes/_book-aliases,notes/attachments,notebooks,data}` (courses also need `weeks/`; research projects often have `threads/` instead).
2. Copy `research/marxian_formalization/_quarto.yml` as a template; update title/subtitle, the `site-url`, and the preview port.
3. Create `<path>/index.qmd`, `pyproject.toml`, `.python-version`.
4. Create notes stubs: `notes/index.md`, `notes/README.md`, `notes/_meta/{workflow,progress,decisions,deferred,glossary}.md`.
5. Add a symlink in `quartz/content/`: `ln -s ../../<path>/notes <new>`.
6. Update `quartz/quartz.config.ts` `ignorePatterns` to include the new vault's `.obsidian` dir.
7. Update `quartz/setup.sh` `COURSE_LINKS` array.
8. Add the path to the matrix in `.github/workflows/render.yml`.
9. Add the path to the stitch loop in the `stitch-and-deploy` job.
10. Add a card to `site-root/index.html`.
11. Add a row to this README's courses or research table.
12. Update the `COURSES` / `RESEARCH` variables at the top of `Makefile`.

## License

- **Content** (chapter `.qmd` files, READMEs, syllabi): [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- **Code** (Python under `apps/`, `notebooks/`, embedded blocks; CI workflows; build config): MIT.

See [`LICENSE`](LICENSE) for the full text of both.

## Acknowledgments

See [`courses/the_calculation_course/index.qmd`](courses/the_calculation_course/index.qmd) for the full acknowledgments for the Calculation Course.
