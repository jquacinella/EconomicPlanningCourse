# Heterodox Econ Courses

A monorepo of computational-economics courses built as Quarto books with executable Python, interactive widgets, Hypothesis annotation, and Obsidian notes vaults. Each course has a polished book track and a working notes track.

The deployed site lives at: **https://jquacinella.github.io/EconomicPlanningCourse/**

## Courses

| Course | Status | Description |
|--------|--------|-------------|
| [The Calculation Course](courses/the_calculation_course/) | In progress | 10-week math arc (calculus → LP → IO → dynamics) + 7 heterodox controversies → climate-constrained planning |
| [201 — Zhang's Marxian Formalization](courses/201/) | Stub | Sequel: game-theoretic, probabilistic, and cybernetic extensions to Marxian economics |
| [The Crypto Calculation Course](courses/the_crypto_course/) | Stub | Cryptocurrency, blockchain, and the ecosocialist planning system |

## Repository layout

```
EconomicPlanningCourse/
├── courses/
│   ├── the_calculation_course/   ← The Calculation Course (book + notes + apps + data)
│   ├── 201/                      ← 201 sequel course (stub)
│   └── the_crypto_course/        ← Crypto course (stub)
│
├── shared/
│   ├── _quarto-base.yml          ← Shared Quarto format/theme config (inherited by all courses)
│   ├── assets/                   ← Shared CSS, fonts, images, scripts, widgets
│   └── extensions/               ← Shared Quarto extensions
│
├── site-root/
│   └── index.html                ← Course-catalog landing page (deployed at /)
│
├── quartz/                       ← Quartz install (renders all course notes/ vaults)
│   └── content/                  ← Per-course symlinks → courses/<name>/notes/
│
├── tests/                        ← Repo-level tests
├── .github/workflows/            ← CI/CD (render matrix + deploy)
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

Each course directory has the same internal structure:

```
courses/<name>/
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

### Other courses

Same pattern — `cd courses/<name>` then `uv sync` and `quarto preview`.

### Build all artifacts

```bash
# From inside a course directory:
quarto render                # all formats (HTML, PDF, EPUB)
quarto render --to html      # HTML only

# Print-targeted PDF (strips author-notes callouts first):
python ../../shared/assets/scripts/strip-author-notes.py
QUARTO_PROFILE=print quarto render build-print/ --to pdf
```

## Adding a new course

1. `mkdir -p courses/<new-course>/{weeks,notes/_meta,notes/_book-aliases,notes/attachments,notebooks,apps,data}`
2. Copy `courses/201/_quarto.yml` as a template; update title/subtitle.
3. Create `courses/<new-course>/index.qmd`, `pyproject.toml`, `.python-version`.
4. Create notes stubs: `notes/index.md`, `notes/README.md`, `notes/_meta/{workflow,progress,decisions,deferred,glossary}.md`.
5. Add a symlink in `quartz/content/`: `ln -s ../../../courses/<new-course>/notes <new-course>`.
6. Update `quartz/quartz.config.ts` `ignorePatterns` to include the new vault's `.obsidian` dir.
7. Update `quartz/setup.sh` `COURSE_LINKS` array.
8. Add the course to the matrix in `.github/workflows/render.yml`.
9. Add the course to the stitch loop in the `stitch-and-deploy` job.
10. Add a card to `site-root/index.html`.
11. Add a row to this README's courses table.

## License

- **Content** (chapter `.qmd` files, READMEs, syllabi): [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- **Code** (Python under `apps/`, `notebooks/`, embedded blocks; CI workflows; build config): MIT.

See [`LICENSE`](LICENSE) for the full text of both.

## Acknowledgments

See [`courses/the_calculation_course/index.qmd`](courses/the_calculation_course/index.qmd) for the full acknowledgments for the Calculation Course.
