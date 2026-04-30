# `data/` — checked-in data files

Provenance is mandatory for every file in this directory.

## Provenance template

Each entry must include:

- **Filename**.
- **Source URL** (the canonical location it was retrieved from).
- **Retrieval date** (ISO-8601: YYYY-MM-DD).
- **License** (or licensing notes — public domain, CC-BY-4.0, "BEA public data", etc.).
- **Brief description** — what the file contains and where in the book it gets used.

Example:

```
- bea-io-2022.csv
  Source: https://www.bea.gov/data/industries/input-output-accounts-data
  Retrieved: 2026-04-30
  License: U.S. Government Work, no copyright (BEA public data)
  Description: 2022 use table at summary level. Used in Week 7's notebook to
  reproduce the QuantEcon Leontief example with current US data.
```

## Files

(none yet — this directory is empty in v1)

## Conventions

- Do not commit large binary files (> a few MB) directly. Use Git LFS, or document a retrieval script and exclude the file from the repo.
- Don't redistribute data with restrictive licensing without explicit permission. If you can't include the file, include a script that fetches it.
- For data used by a specific Dash app, store it under `apps/<app-name>/data/` not here. This directory is for data the *book* uses.
