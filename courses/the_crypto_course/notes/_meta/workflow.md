# How to work in this repo — Crypto Calculation Course

See the Calculation Course's `notes/_meta/workflow.md` for the full workflow document. The conventions are identical; only the course content differs.

The two-track structure (book in `courses/the_crypto_course/`, notes in `courses/the_crypto_course/notes/`) works the same way. Build commands from inside `courses/the_crypto_course/`:

- **Book:** `quarto preview` (serves at localhost:4444)
- **Notes:** `cd ../../quartz && npx quartz build --serve` (serves at localhost:8080, notes under `/notes/the_crypto_course/`)
