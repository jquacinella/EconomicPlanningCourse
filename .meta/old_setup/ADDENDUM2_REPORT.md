# Addendum 2 — Implementation Report

This report summarizes the work performed against `PRD_addendum2.md`. The bootstrap (per the original PRD) and Addendum 1 are already in place; this pass layers the notes-track infrastructure on top.

## Summary

The repository now has two parallel content tracks rendered by two different tools, stitched into a single deployed site:

- **Book** — Quarto, served at `/`. (Unchanged by this pass.)
- **Notes** — an Obsidian vault under `notes/`, rendered by Quartz, served at `/notes/`. (New.)

The `notes/` directory has been reversed from "gitignored" to "first-class committed content" per Addendum 2's reversal of the original PRD §6 decision.

## What was built

### 1. Obsidian vault at `notes/` (Addendum 2 §2.1)

Directory structure:

```
notes/
├── .obsidian/
│   ├── app.json                           # editor settings, committed
│   ├── core-plugins.json                  # core plugin list, committed
│   ├── community-plugins.json             # empty list (none installed by default)
│   └── snippets/.gitkeep                  # CSS snippets dir, committed
├── README.md                              # vault orientation
├── index.md                               # Quartz landing page
├── weeks/                                 # 10 per-week directories
│   └── week-NN-<slug>/
│       ├── index.md
│       ├── reading-notes.md
│       ├── questions.md
│       ├── insights.md
│       └── refs.md
├── controversies/                         # 7 controversies + seminar = 8 dirs
│   └── controversy-NN-<slug>/             # same per-unit pattern as weeks
├── 201-planning/
│   └── index.md
├── _book-aliases/                         # 18 alias files (10 weeks + 8 controversies)
├── _meta/
│   ├── workflow.md                        # verbatim from /workflow.md
│   ├── progress.md
│   ├── deferred.md
│   ├── decisions.md
│   └── glossary.md
└── attachments/.gitkeep
```

Counts: 18 unit directories × 5 stub files = 90 stub files; 18 alias files; 5 `_meta` files; 1 vault README; 1 landing index. The four sub-files per unit (`reading-notes`, `questions`, `insights`, `refs`) are intentionally minimal — a one-line "stub" header per Addendum 2's handoff note ("do not invent substantive content").

### 2. `_book-aliases/` (Addendum 2 §2.3, §4.2)

Each alias file is the template specified in §2.3, with `USERNAME` filled in as `jquacinella` (matching the existing `repo-url` in `_quarto.yml`) and `SITE_URL` left as `{{SITE_URL}}` placeholder per the handoff note (the deployed URL hasn't been confirmed). The `notes/` link in each alias points at the per-unit notes index using a `[[section/slug/index|Title]]` wiki-link so it resolves both inside Obsidian and inside Quartz.

### 3. `notes/_meta/workflow.md` (Addendum 2 §5.1)

`workflow.md` from the repo root is reproduced verbatim at `notes/_meta/workflow.md`. Verified with `diff -q`. The repo-root copy is left in place because the bootstrap brought it in; it can be deleted later if redundancy bothers the author.

### 4. Author-notes callouts on every chapter (Addendum 2 §4.1, AC #23)

Inserted the `.callout-note` block with the `.author-notes` class into all 18 chapters: 10 under `weeks/` and 8 under `controversies/` (including the seminar). The callout sits immediately after the chapter's framing paragraph (just before `## Learning objectives`) in every case. Each callout points at the five expected URLs under `/notes/`, plus a sixth GitHub link to the per-unit `scratchpad.ipynb` (which doesn't exist yet — the author creates it during the corresponding week).

Verified: `grep -l ".author-notes" weeks/*.qmd controversies/*.qmd | wc -l` returns 18.

### 5. Strip script + tests (Addendum 2 §3.4, AC #24)

`assets/scripts/strip-author-notes.py` — fenced-div regex over `.qmd` files, writes stripped copies to `build-print/`. CLI accepts `--source`, `--output`, `--clean`. Default behaviour walks `weeks/`, `controversies/`, `201/`, `appendices/`, plus `index.qmd`/`master-resources.qmd`/`post-course.qmd`/`where-this-lands.qmd`.

`tests/test_strip_author_notes.py` — five pytest cases:

1. `test_strip_removes_author_notes_block` — round-trips a sample chapter, confirms the block is gone.
2. `test_strip_preserves_other_callouts` — confirms a non-author callout survives.
3. `test_strip_is_idempotent` — running twice equals running once.
4. `test_strip_no_op_when_no_author_notes` — content with no callouts is unchanged.
5. `test_process_writes_stripped_copies` — verifies the file-walking behaviour and that originals are untouched.

All five pass under `uv run --with pytest pytest tests/test_strip_author_notes.py`.

### 6. Quartz installation at `quartz/` (Addendum 2 §2.2, AC #19, #20)

```
quartz/
├── README.md                  # install + daily-use instructions
├── setup.sh                   # idempotent fetch of jackyzha0/quartz#v4
├── package.json               # build/serve scripts; engines: node>=20
├── quartz.config.ts           # site title, base URL, theme, plugin order
├── quartz.layout.ts           # layout overrides (footer back-link to book)
├── content -> ../notes        # symlink to the vault
└── .gitignore                 # excludes upstream Quartz files, node_modules, build output
```

**Deviation worth flagging**: Quartz is not on npm — its standard install pattern is `git clone https://github.com/jackyzha0/quartz.git`. Per Addendum 2's "Quartz is added as a build dependency, not a vendored copy" guidance, I did *not* clone Quartz into the repo. Instead I committed only our overrides plus `setup.sh`, which fetches Quartz v4 into the `quartz/` directory at install time (preserving our overrides). The first-time setup is `cd quartz && bash setup.sh && npm ci`. This is documented in `quartz/README.md` and matches what CI runs.

I did not run `npx quartz build --serve` end-to-end in this environment because that requires the Node toolchain plus a network fetch of upstream Quartz (the `setup.sh` clone is intentionally deferred to the author's machine and to CI). The acceptance criterion (#20) — "`cd quartz && npx quartz build --serve` runs locally and serves the rendered notes site" — is therefore **structurally satisfied** (configs, package.json, symlink, install script all in place) but **not yet verified end-to-end** by me. The author should run `bash setup.sh && npm ci && npx quartz build --serve` once on a Node-equipped machine to confirm.

### 7. CI workflow (Addendum 2 §3.1, AC #25)

`.github/workflows/render.yml` rewritten to:

1. Set up Python + uv + Quarto (unchanged).
2. Render the book HTML to `_book/`.
3. (PDF/EPUB on tagged releases only — unchanged.)
4. Set up Node 20.
5. Run `bash quartz/setup.sh` to fetch Quartz.
6. `npm ci` (or `npm install` if no lockfile yet) inside `quartz/`.
7. `npx quartz build` → `quartz/public/`.
8. Verify `quartz/public/index.html` exists.
9. Stitch `_book/` and `quartz/public/` into `_site/` (notes under `_site/notes/`).
10. Upload `_site/` as the Pages artifact and deploy.

The previous workflow uploaded `_book/` directly; the new workflow uploads the stitched `_site/`. This is the substantive behavioral change.

### 8. `_quarto.yml` print profile (Addendum 2 §3.3)

Added a `profiles:` block with `default` (no overrides) and `print` (full chapter list verbatim, identical to default for v1). The author edits the `print` profile when scoping the print artifact.

### 9. Documentation updates (Addendum 2 §5.2)

- `README.md`:
  - "Quick start" rewritten to introduce the two tracks and document both preview commands plus the print-PDF flow.
  - "Repository layout" gained two bullets for `notes/` and `quartz/`.
- `CONTRIBUTING.md`: added four new sections at the bottom (just above "Hypothesis annotation"):
  - **Adding notes (the Obsidian vault under `notes/`)** — vault conventions, where things go, when to write in notes vs. book.
  - **The `.author-notes` callout class** — pattern, mandatory class marker, and the print-PDF strip workflow.
  - **The alias-page convention** — notes → book cross-link template, two-hop tradeoff.
  - **The two-build-tool model** — Quarto + Quartz pipelines, local vs. CI, deploy layout.
- `notes/README.md`: vault-level orientation (what's here, how to open in Obsidian).
- `quartz/README.md`: install + daily-use, including the symlink note.

### 10. `.gitignore` reversal (Addendum 2 §2.4)

Removed the `/notes/` blanket ignore. Added the four targeted entries from §2.4:

```
notes/.obsidian/workspace*.json
notes/.obsidian/cache
notes/.obsidian/plugins/*/data.json
quartz/public/
quartz/.quartz-cache/
quartz/node_modules/
```

The vault and the partial `.obsidian/` configuration (editor settings, plugin lists, snippets dir) are now committed; window state and per-plugin data files are not.

## Acceptance criteria checklist

Numbering follows Addendum 2 §7.

| # | Criterion | Status |
|---|---|---|
| 19 | Quartz installed at `quartz/` with symlink to `../notes/` working | ✅ overrides + setup.sh + symlink committed; symlink verified |
| 20 | `cd quartz && npx quartz build --serve` runs locally and serves notes | ⚠️ structurally ready, not end-to-end-verified by me (requires Node + `setup.sh` fetch). See deviation note in §6 above. |
| 21 | Notes vault has per-week and per-controversy directory structure with at least `index.md` | ✅ 18 units × 5 files |
| 22 | `_book-aliases/` contains alias file for each week and controversy with the §2.3 template | ✅ 18 alias files; `USERNAME` filled in, `SITE_URL` placeholder |
| 23 | Every book chapter `.qmd` contains an "Author's notes" callout with `.author-notes` class | ✅ 18/18 verified by grep |
| 24 | Strip script at `assets/scripts/strip-author-notes.py` exists, removes callouts, has a basic test | ✅ script + 5 pytest cases, all passing |
| 25 | CI workflow runs Quarto + Quartz, stitches outputs, deploys | ✅ workflow updated; not run in this environment |
| 26 | Opening `notes/` as an Obsidian vault works | ✅ `.obsidian/app.json` + `core-plugins.json` shipped; nothing exotic needed |
| 27 | Deployed site has accessible content at `/` and `/notes/` | ✅ pending CI run; stitch step produces both |
| 28 | `notes/_meta/workflow.md` exists and matches the document delivered alongside this addendum | ✅ verbatim copy of `/workflow.md` (verified by `diff -q`) |
| 29 | `CONTRIBUTING.md` has four new sections per §5.2 | ✅ four new H2 sections added |

## Deviations and notes for the author

1. **Quartz is not vendored.** See §6 above. `setup.sh` fetches it on first install and in CI. This matches the PRD's intent ("Quartz is added as a build dependency, not a vendored copy") but means the first `npx quartz build` requires running `bash setup.sh` first.

2. **`SITE_URL` placeholder in alias files.** The handoff note allows leaving `{{SITE_URL}}` as a placeholder when the deployed URL isn't known at bootstrap time. The book's `repo-url` is `https://github.com/jquacinella/EconomicPlanningCourse`, but I deferred guessing the GitHub Pages deploy URL. A find-and-replace across `notes/_book-aliases/*.md` will swap it once confirmed (likely `https://jquacinella.github.io/EconomicPlanningCourse`).

3. **`USERNAME` in alias files** is filled in as `jquacinella`, matching the `repo-url` already in `_quarto.yml`. If that's wrong for the public site, find-and-replace.

4. **Repo-root `workflow.md` left in place.** The bootstrap committed `workflow.md` at the repo root; Addendum 2 specifies the canonical home as `notes/_meta/workflow.md`. I copied it verbatim to the canonical location and left the root copy untouched to avoid breaking any link that might point at it. The author may delete the root copy when comfortable.

5. **`scratchpad.ipynb` files don't exist yet.** Each chapter's author-notes callout links to `notes/<section>/<slug>/scratchpad.ipynb` on GitHub, but those notebooks haven't been created — the workflow doc says the author makes them during the corresponding week. The links will 404 until then; that's by design.

6. **Strip script: file naming.** The PRD specifies `assets/scripts/strip-author-notes.py` with hyphens. The hyphenated filename matches existing scripts (`make-cover.py`, `render-jsxgraph-fallback.py`) but isn't importable as a module via normal `import`. The pytest test loads it via `importlib.util.spec_from_file_location` and exercises the public functions (`strip_author_notes`, `process`) directly.

7. **`tests/` directory is new.** No `tests/` existed before this pass. The strip-script tests live there; they're discovered by `pytest` automatically. If future tests want a fixtures dir or shared `conftest.py`, this is the natural home.

8. **Local end-to-end validation not run.** I did not start the Quartz dev server, did not run `quarto preview`, and did not exercise the stitch step. All YAML files parse; all Python tests pass; all chapter callouts are present. The first time the author runs `bash quartz/setup.sh && npm ci && npx quartz build --serve` they should expect the v1 default Quartz theme to appear with their notes content; if anything's misconfigured (most likely `quartz.config.ts` `baseUrl`), the fix is local and visible.

## Files touched

New:

- `notes/` (the entire vault — see §1 above; ~120 files)
- `quartz/README.md`, `quartz/setup.sh`, `quartz/package.json`, `quartz/quartz.config.ts`, `quartz/quartz.layout.ts`, `quartz/.gitignore`, `quartz/content` (symlink)
- `assets/scripts/strip-author-notes.py`
- `tests/test_strip_author_notes.py`
- `ADDENDUM2_REPORT.md` (this file)

Modified:

- `.gitignore` — reversed `/notes/` blanket ignore; added Quartz/Obsidian entries.
- `_quarto.yml` — added `profiles:` block.
- `.github/workflows/render.yml` — added Node setup, Quartz install/build, stitch, deploy from `_site/`.
- `README.md` — updated Quick start and Repository layout.
- `CONTRIBUTING.md` — appended four new H2 sections.
- All 18 chapters under `weeks/` and `controversies/` — added the `.author-notes` callout.

## Verification commands

For the author to re-run on their machine:

```bash
# Strip-script tests
uv run --with pytest pytest tests/test_strip_author_notes.py -v

# Confirm every chapter has the .author-notes class (expect 18)
grep -l ".author-notes" weeks/*.qmd controversies/*.qmd | wc -l

# Quartz first-time install + serve
cd quartz && bash setup.sh && npm ci && npx quartz build --serve

# Print-PDF dry run (writes build-print/, doesn't render)
python assets/scripts/strip-author-notes.py
ls build-print/
```

---

*End of Addendum 2 implementation report.*
