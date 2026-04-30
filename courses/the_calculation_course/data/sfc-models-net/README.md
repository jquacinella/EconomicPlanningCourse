# `data/sfc-models-net/` — optional mirror of canonical eViews files

Provenance: <https://sfc-models.net> — Brian Romanchuk's canonical site for stock-flow-consistent macroeconomic model files in eViews format. These are the reference implementations against which `sfc_models.gl_book` was validated.

## Status (v1)

**Empty by design.** The directory and this README ship in v1 as a *placeholder* against possible later use. Nothing is mirrored yet.

## When to populate

The author should populate this directory only if, during work on Controversy 7, having local copies of the canonical eViews files proves necessary for archival or reproducibility purposes. Otherwise leave it empty — the canonical reference is the upstream site, and `sfc_models.gl_book` already provides validated Python implementations for the common Godley–Lavoie models.

## If populated

Each mirrored file must include:

- Original filename and source URL on <https://sfc-models.net>.
- Retrieval date (ISO-8601).
- A note on license / redistribution terms (these are typically free to mirror but always check at retrieval time).

Per the standard `data/` convention (see `../README.md`), prefer scripts that fetch on demand over committing large binaries directly.
