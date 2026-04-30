# How to work in this repo — 201 course

See the Calculation Course's `notes/_meta/workflow.md` for the full workflow document. The conventions are identical; only the course content differs.

The two-track structure (book in `courses/201/`, notes in `courses/201/notes/`) works the same way. Build commands from inside `courses/201/`:

- **Book:** `quarto preview` (serves at localhost:4444)
- **Notes:** `cd ../../quartz && npx quartz build --serve` (serves at localhost:8080, notes under `/notes/201/`)
