# The Morishima Track

A computational-economics curriculum that walks from multivariable calculus through linear algebra, optimization, input-output analysis, and dynamic systems, into a sequence of in-depth heterodox-economics controversies, ending at a thirty-year climate-constrained planning model — built as a Quarto book with executable Python, marginalia, and Hypothesis annotation.

The book is delivered as three artifacts:

- An **HTML site** with executable code and Hypothesis annotation (deployed to GitHub Pages).
- A **PDF book** with Tufte-style marginalia (rendered via Typst).
- An **EPUB** for offline reading.

Plus a small set of **standalone interactive companions** (Plotly Dash apps deployed to Render).

## Quick start

```bash
git clone https://github.com/jquacinella/EconomicPlanningCourse.git.git
cd morishima-track
uv sync                      # installs Python dependencies
quarto preview               # serves the site at http://localhost:4444 with live reload
```

To build the book:

```bash
quarto render                # all formats (HTML, PDF, EPUB)
quarto render --to html      # one format only
```

The Cobb-Douglas demo Dash app is in `apps/demo-budget-explorer/`:

```bash
cd apps/demo-budget-explorer
pip install -r requirements.txt
python app.py                # http://localhost:8050
```

## Repository layout

- `index.qmd` — front matter and a developer-reference style guide.
- `master-resources.qmd` — the master link list.
- `weeks/` — the 10-week mathematics arc (Part I).
- `controversies/` — the seven heterodox controversies + the Chinese-critique seminar (Part II).
- `201/placeholder.qmd` — sketch of a follow-on course.
- `appendices/` — pre-course checklist, extra-depth pointers, absorption diagnostics.
- `apps/` — standalone Dash apps. Each subdirectory has its own `requirements.txt`, `Dockerfile`, and `render.yaml`.
- `notebooks/` — working Jupyter notebooks before content gets pulled into `.qmd`.
- `data/` — checked-in data files. Provenance is documented in `data/README.md`.
- `minsky-models/`, `ravel-files/` — reserved space for Steve Keen's Minsky and Ravel files.
- `assets/` — images, custom SCSS, fonts.
- `.github/workflows/` — CI/CD (render and deploy on push to main; lint on PR).

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for conventions on adding chapters, marginalia, code blocks, Dash apps, Observable widgets, and data files.

## License

- **Content** (everything textual: chapter `.qmd` files, READMEs, the syllabus): [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- **Code** (Python under `apps/`, `notebooks/`, and embedded blocks; CI workflows; build config): MIT.

See [`LICENSE`](LICENSE) for the full text of both.

## Acknowledgments

This project stands on a lot of people's work. Direct intellectual debts:

- **The Quarto team** at Posit for the publishing system that makes hybrid book / executable / interactive output a single coherent target.
- **The QuantEcon team** (Thomas Sargent, John Stachurski, and contributors) for the executable-textbook pattern this project tries to learn from.
- **Paul Cockshott, Allin Cottrell, and Jan Philipp Dapprich** for thirty years of work on the planning side of the calculation debate, without which most of Part II would have nothing to compute.
- **Xian Zhang** and **Bin Yu** for the Chinese-school critical engagement with the Japanese School that the seminar between Controversies 5 and 6 is built around.
- **Steve Keen** for the Minsky and Ravel tools, and for keeping endogenous-money and Minsky-style debt-dynamics modelling alive in a tractable form.
- **The 3Blue1Brown / MIT OCW / Strang lineage** of mathematical pedagogy that the Part I weekly schedule leans on heavily.
- **Anwar Shaikh, Joan Robinson, Piero Sraffa, and the Cambridge UK tradition** whose critical apparatus drives Controversies 1 and 4.

Errors and idiosyncrasies are the author's.
