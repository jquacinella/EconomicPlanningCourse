# How to work in this repo — Postcapitalism After AI research track

See the Calculation Course's `notes/_meta/workflow.md` for the full workflow document. The conventions are identical; only the content differs.

The two-track structure (book in `research/postcapitalism_after_ai/`, notes in `research/postcapitalism_after_ai/notes/`) works the same way. Build commands from inside `research/postcapitalism_after_ai/`:

- **Book:** `quarto preview` (serves at localhost:4446)
- **Notes:** `cd ../../quartz && npx quartz build --serve` (serves at localhost:8080, notes under `/notes/postcapitalism_after_ai/`)
