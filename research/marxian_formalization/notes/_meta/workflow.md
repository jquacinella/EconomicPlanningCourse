# How to work in this repo — Marxian Formalization research project

See the Calculation Course's `notes/_meta/workflow.md` for the full workflow document. The conventions are identical; only the content differs.

The two-track structure (book in `research/marxian_formalization/`, notes in `research/marxian_formalization/notes/`) works the same way. Build commands from inside `research/marxian_formalization/`:

- **Book:** `quarto preview` (serves at localhost:4445)
- **Notes:** `cd ../../quartz && npx quartz build --serve` (serves at localhost:8080, notes under `/notes/marxian_formalization/`)
