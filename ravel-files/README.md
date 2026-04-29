# `ravel-files/` — Steve Keen's Ravel files

[Ravel](https://www.patreon.com/hpcoder) is Steve Keen's commercial multidimensional-data exploration tool, extending Minsky's modelling apparatus toward what is effectively a pivot-table-meets-system-dynamics interface for empirical economic data. It is distributed via Patreon (commercial) rather than as open source.

It is most directly relevant to **Controversy 5** (empirical profit-rate measurement on BEA / BLS data) and **Controversy 6** (SFC modelling with empirical calibration). Optional throughout — the course can complete without it.

## Where to download

- Patreon: <https://www.patreon.com/hpcoder>
- Tutorials: Steve Keen's YouTube channel, *Ravel Tutorials* playlist.

## What goes in this directory

- `.rvl` files: Ravel project files. Treated as binary by `.gitattributes`.

## Important: redistribution

Ravel is a commercial tool. The author's working `.rvl` files may contain proprietary structure or third-party data with restrictive licensing. **`.rvl` files are gitignored by default** (see `.gitignore`), so they don't get checked in unless explicitly forced.

If you intentionally want to commit a `.rvl` file (for example, a model you've built that is fully derived from public-domain BEA data and that you want others to be able to open), use `git add -f path/to/model.rvl` and document its provenance and license terms in a companion `<model-name>.md` next to it. Default is: don't.

## Conventions

- Each `.rvl` should have a sibling `<name>.md` describing the model, its data sources, retrieval dates, and license terms.
- The build does not depend on Ravel being installed. Like Minsky, files here are author-side artifacts.

## Files

(none yet — this directory is empty in v1)
