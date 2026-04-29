# `sfc-notebooks/` — Stock-flow consistent reference notebooks

Working notebooks alongside **Controversy 6** (monetary theory of production). These reproduce baseline Godley–Lavoie models from `sfc_models.gl_book` and serve as the scaffolding on which the controversy's capstone versions are built.

## Tool positioning

`sfc_models` (Brian Romanchuk, Apache 2.0, on PyPI) is the **primary** system-dynamics tool for this project. See `CONTRIBUTING.md` (System-dynamics tool positioning) for the full picture. In short:

- `sfc_models` — primary; high-level sector specification, validated against Godley & Lavoie's *Monetary Economics*.
- `pysolve` — complementary constraint solver (used by `sfc_models` and available directly).
- `pysd` — optional, under the `extended` extra; for loading externally-published Vensim/XMILE models.
- Minsky / Ravel — optional teaching companions, not primary tooling. See `minsky-models/` and `ravel-files/`.

## Notebooks

- `01-sim-baseline.ipynb` — stub. Will reproduce SIM (the simplest Godley–Lavoie model). Populated during Controversy 6, Version 1.
- `02-pc-portfolio-choice.ipynb` — stub. Portfolio choice (PC) model.
- `03-bmw-banks-and-money.ipynb` — stub. Banks-and-money (BMW) model. Backbone for Controversy 6, Version 2.

Each stub is intentionally minimal in v1; the author fills them in when working through the relevant version of the Controversy 6 capstone.

## `kennt-monetary-economics/` (optional submodule)

The intent is to add <https://github.com/kennt/monetary-economics> as a git submodule here, providing a canonical reference set of Godley–Lavoie implementations (kennt's `pysolve`-based notebooks). This is **flagged for the author to decide at v1 build time**:

- *Submodule* (PRD default): clean dependency tracking, easy to update, requires `git submodule update --init` after clone.
- *Vendored*: full local control, no external repo dependency, but harder to track upstream.

If you want to add it as a submodule now:

```bash
git submodule add https://github.com/kennt/monetary-economics sfc-notebooks/kennt-monetary-economics
```

In v1 the directory is left absent until the author decides.
