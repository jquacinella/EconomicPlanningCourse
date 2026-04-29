# Morishima Track — PRD Addendum 2

**Project name:** `morishima-track`
**Owner:** [your name]
**Date:** April 2026
**Status:** Draft for handoff to Claude Code
**Supersedes:** None. Augments and modifies the original PRD (`morishima_track_PRD.md`) and Addendum 1 (`morishima_track_PRD_addendum1.md`).

---

## How to read this document

This is the second addendum to the original PRD. It introduces a notes layer to the project that lives alongside the book, is rendered as a sibling section of the public website, and is excluded from print artifacts. It also formalizes the cross-linking conventions between book and notes, the build pipeline changes, and the strip-for-publication workflow.

The substantive change is the introduction of an **Obsidian vault rendered by Quartz** as the notes-track infrastructure, complementing the **Quarto-rendered book** that's already in place. Same repo, two build pipelines, one stitched output site.

Where this document conflicts with prior PRDs, this document wins. Where this document is silent, prior PRDs stand. Specifically: the original PRD §6 stated that `notes/` should be gitignored as "personal reading notes." This addendum reverses that decision and treats notes as first-class committed content.

---

## 1. Decision

### 1.1 The two-track structure

The project now has two parallel content tracks rendered by two different tools:

- **Course track**: polished book content. `weeks/`, `controversies/`, `seminar-chinese-critique.qmd`, `201/`, `where-this-lands.qmd`, the appendices. Rendered by Quarto. Builds to HTML and PDF.
- **Notes track**: scratchpad, reading notes, questions, insights, methodological decisions, progress logs. Lives in `notes/` as an Obsidian vault. Rendered by Quartz. Builds to HTML only.

Both render to the same deployed site under different URL prefixes. The notes track is excluded from PDF and EPUB outputs.

### 1.2 Why Quartz rather than Quarto-only

Quartz is a static-site generator designed specifically to render Obsidian-style vaults to a web site. It's free and open-source, MIT-licensed, actively maintained, written in TypeScript, and used widely for digital-garden publishing. Repository: <https://github.com/jackyzha0/quartz>.

The author works in Obsidian as a daily writing tool. Obsidian uses wiki-link syntax (`[[page-name]]`), supports backlinks, tags, and graph view, and treats Markdown files as a vault rather than as articles requiring front matter. Rendering this experience faithfully on the web requires a tool that understands Obsidian conventions natively. Quarto is excellent at executable-document rendering but its link syntax, front-matter requirements, and execution model fight the lightweight scratch-flow that the notes track needs.

A Quarto-only alternative was considered (Quarto build profiles, with a `notes` profile that includes both book and notes; only `book` profile produces PDF). Rejected because it would force Quarto-syntax links and YAML front matter on the notes, breaking the Obsidian experience that's load-bearing for the author.

### 1.3 Implications

- The author writes notes in Obsidian as normal — wiki-links, no front matter required, drag-and-drop file organization, backlinks, graph view all work.
- The published notes section of the site looks like a digital garden. Wiki-links resolve. Backlinks render automatically. Tags work as topic indices.
- The book and notes cross-link via standard URL paths.
- The book PDF is unaffected. Notes never enter the print pipeline.
- A small script can strip "Author's notes" callouts from book chapters when producing a publication-ready manuscript.

---

## 2. Repository structure changes

### 2.1 The `notes/` directory becomes an Obsidian vault

```
notes/                                      [dir]   Obsidian vault, rendered by Quartz
├── .obsidian/                              [dir]   Obsidian workspace config
│   ├── app.json                            [file]  Editor settings, committed
│   ├── core-plugins.json                   [file]  Active core plugins, committed
│   ├── community-plugins.json              [file]  Community plugins list, committed
│   ├── snippets/                           [dir]   CSS snippets, committed
│   │   └── .gitkeep
│   ├── workspace.json                      Gitignored — local window state
│   ├── workspace-mobile.json               Gitignored
│   └── cache                               Gitignored
│
├── README.md                               [file]  What this vault is, how to use it
├── index.md                                [file]  Quartz landing page for the notes section
│
├── weeks/                                  [dir]
│   ├── week-01-multivariable/              [dir]
│   │   ├── index.md                        [file]  Per-week landing
│   │   ├── reading-notes.md                [stub]  Empty stub committed for v1
│   │   ├── questions.md                    [stub]
│   │   ├── insights.md                     [stub]
│   │   └── refs.md                         [stub]
│   ├── week-02-constrained/                [dir]   ... same pattern ...
│   ├── week-03-linear-algebra/
│   ├── week-04-eigenvalues/
│   ├── week-05-economic-opt/
│   ├── week-06-lp-duality/
│   ├── week-07-input-output/
│   ├── week-08-planning/
│   ├── week-09-diff-eq/
│   └── week-10-growth-stability/
│
├── controversies/                          [dir]
│   ├── controversy-01-cobb-douglas/        [dir]   ... same per-controversy pattern ...
│   ├── controversy-02-calculation/
│   ├── controversy-03-transformation/
│   ├── controversy-04-sraffa/
│   ├── controversy-05-okishio/
│   ├── seminar-chinese-critique/
│   ├── controversy-06-money/
│   └── controversy-07-climate/
│
├── 201-planning/                           [dir]   Notes for the 201 placeholder course
│   └── index.md                            [stub]
│
├── _book-aliases/                          [dir]   Wiki-link targets that point back to book chapters
│   ├── week-01.md                          [file]  See §4.2 of this addendum
│   ├── week-02.md
│   ├── ...
│   ├── controversy-01.md
│   └── ...
│
├── _meta/                                  [dir]
│   ├── workflow.md                         [file]  How to work in this repo (see Addendum 2 deliverable)
│   ├── progress.md                         [file]  Running log of where I am
│   ├── deferred.md                         [file]  Stuff to come back to later
│   ├── decisions.md                        [file]  Methodological choices and reasoning
│   └── glossary.md                         [stub]  Optional: shared vocabulary as the project grows
│
└── attachments/                            [dir]   Images, PDFs, screenshots referenced in notes
    └── .gitkeep
```

The per-week and per-controversy `index.md` files are landing pages for that unit's notes. Initial content is one sentence: "Notes for [Week N | Controversy N — Title]." The author fills them in as work progresses.

The four per-unit stub files (`reading-notes`, `questions`, `insights`, `refs`) are committed empty so the structure is in place when the author opens Obsidian for the first time. They can be deleted, renamed, or merged later — the structure is a starting suggestion, not a contract.

### 2.2 Quartz lives at the repo root

Quartz is added as a build dependency, not a vendored copy. The recommended pattern is to install Quartz as a sibling to the Quarto project rather than as a subdirectory of `notes/`. This keeps Quartz config out of the vault.

```
morishima-track/
├── _quarto.yml
├── notes/                              # The Obsidian vault (content)
├── quartz/                             # Quartz installation (build tool)
│   ├── quartz.config.ts                # Quartz configuration
│   ├── quartz.layout.ts                # Quartz layout overrides
│   ├── package.json                    # Node dependencies
│   └── content -> ../notes/            # Symlink to the vault
└── ...
```

The `quartz/content` symlink points at `../notes/`. This is Quartz's convention — it expects a `content/` directory inside its installation. The symlink lets the vault live wherever the author prefers (in this case, `notes/` at the repo root for visibility) while satisfying Quartz's expectations.

Note: symlinks work cleanly on macOS and Linux. On Windows, this requires either developer mode or junction points. The author is on macOS (M1 Max) so this is fine for v1.

### 2.3 The `_book-aliases/` directory

This directory contains wiki-link target files that point back to the book chapters. Each file is short:

```markdown
<!-- notes/_book-aliases/week-01.md -->
# Week 1 — Multivariable Calculus (book chapter)

This page is an alias. The polished chapter lives in the book.

- **Open in book**: <https://morishima-track.example.com/weeks/week-01-multivariable/>
- **Edit source**: <https://github.com/USERNAME/morishima-track/blob/main/weeks/week-01-multivariable.qmd>
- **Notes for this week**: [[weeks/week-01-multivariable/index|Week 1 notes]]
```

When the author writes `Continuing from [[week-01]] but going deeper` in a scratch note, Obsidian resolves the wiki-link to this alias page (because Obsidian's wiki-link resolution searches the whole vault), and the alias page links out to the book chapter. Two clicks instead of one, but it preserves the Obsidian experience.

Open question §6.1 below addresses whether this two-hop pattern is worth replacing with a Quartz link transformer that rewrites `[[week-01]]` directly to the book URL. Default: keep the alias pattern for v1.

### 2.4 Reversal of `.gitignore` for `notes/`

The original PRD §4 specified `notes/` as gitignored. This addendum reverses that decision. The notes directory is committed.

`.gitignore` entries to keep:

```gitignore
# Obsidian local state
notes/.obsidian/workspace*.json
notes/.obsidian/cache
notes/.obsidian/plugins/*/data.json

# Quartz build artifacts
quartz/public/
quartz/.quartz-cache/
quartz/node_modules/
```

The `notes/.obsidian/` directory is partially committed: editor settings, plugin lists, CSS snippets are in version control; window positions and caches are not.

---

## 3. Build pipeline changes

### 3.1 Two-tool build

The CI workflow runs Quarto first, then Quartz, stitching outputs into a single deploy directory.

```yaml
# .github/workflows/render.yml (revised sketch)
name: Render and deploy

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install uv
        uses: astral-sh/setup-uv@v3
      
      - name: Install Python dependencies
        run: uv sync
      
      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
      
      - name: Render book with Quarto
        run: |
          quarto render
          # Output: _book/
      
      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Build notes with Quartz
        working-directory: ./quartz
        run: |
          npm ci
          npx quartz build
          # Output: quartz/public/
      
      - name: Stitch outputs
        run: |
          mkdir -p _site
          cp -r _book/* _site/
          cp -r quartz/public _site/notes
      
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_site
```

The deploy directory layout:

```
_site/                          # Final stitched site, deployed to GitHub Pages
├── index.html                  # Book landing page
├── weeks/                      # Book chapters (Quarto)
├── controversies/
├── search.json                 # Quarto search index
└── notes/                      # Quartz-rendered notes (different look)
    ├── index.html              # Notes landing
    ├── weeks/
    ├── controversies/
    ├── _meta/
    └── ...
```

### 3.2 Local development

For day-to-day work the author runs whichever tool corresponds to what they're editing.

- Editing a chapter `.qmd` file: `quarto preview` running in one terminal. Watches the chapter sources, rebuilds book pages, serves at `localhost:4567`.
- Editing notes in Obsidian: open the vault, edit. To preview Quartz rendering: `cd quartz && npx quartz build --serve` in another terminal. Watches the vault, rebuilds notes pages, serves at `localhost:8080`.
- Both at once: run both commands in separate terminals.

The local URLs differ from the deployed URLs (different ports, no `/notes/` prefix on the local Quartz build). This is fine for day-to-day editing. The author should periodically check that cross-links work in the deployed site.

### 3.3 Build profile for print artifact

Quarto's profile system handles the "publication-ready PDF that excludes some chapters" use case.

```yaml
# Add to _quarto.yml
profiles:
  default:
    # All chapters, current configuration. No change.
  
  print:
    book:
      chapters:
        # Whichever subset is appropriate for print at the time.
        # Initially same as default; the author edits this when ready to
        # produce a print-targeted manuscript. Example for later use:
        # - weeks/week-05-economic-opt.qmd
        # - weeks/week-06-lp-duality.qmd
        # - controversies/...
    format:
      pdf:
        # Print-specific styling overrides go here later.
```

To produce the print PDF: `QUARTO_PROFILE=print quarto render --to pdf`. v1 ships the `print` profile identical to default; the author edits it when ready.

### 3.4 Author-notes stripping for print

Add a script `assets/scripts/strip-author-notes.py` that processes `.qmd` files and removes any callout block matching the author-notes pattern (see §4.1 below). The script reads source files, writes processed copies to a temporary directory, and is intended to be invoked as part of a print build pipeline.

```python
# assets/scripts/strip-author-notes.py (sketch)
"""
Remove ::: {.callout-note appearance="minimal" ...} blocks tagged as
author-notes from .qmd source files. Output to ./build-print/.

Usage:
    python assets/scripts/strip-author-notes.py
    QUARTO_PROFILE=print quarto render build-print/ --to pdf
"""
```

v1 ships this as a working script with tests. The implementation is straightforward (~50 lines) — a regex over the file content matching a fenced div block with the `author-notes` class attribute.

---

## 4. Cross-linking conventions

### 4.1 Book → notes (the "Author's notes" callout)

Each book chapter (every `.qmd` under `weeks/` or `controversies/`) gets a single callout near the top, immediately after the chapter's framing paragraph. Convention:

```markdown
::: {.callout-note appearance="minimal" collapse="true" .author-notes}
## Author's notes for this week

- [Reading notes](/notes/weeks/week-01-multivariable/reading-notes/)
- [Open questions](/notes/weeks/week-01-multivariable/questions/)
- [Insights and connections](/notes/weeks/week-01-multivariable/insights/)
- [References to revisit](/notes/weeks/week-01-multivariable/refs/)
- [Scratchpad notebook](https://github.com/USERNAME/morishima-track/blob/main/notes/weeks/week-01-multivariable/scratchpad.ipynb)
:::
```

Three things to note:

- The `.author-notes` class is what the strip script identifies. **This class must be on every author-notes callout for stripping to work**. The CONTRIBUTING.md should make this explicit.
- The callout is `collapse="true"` so it's hidden by default in the rendered HTML — non-author readers don't see notes prominently, and clicking the header expands the callout to show the links.
- The links use absolute paths (`/notes/...`) so they work both locally during preview and after deployment.

For controversies, the same pattern with paths under `/notes/controversies/`. For the seminar, paths under `/notes/controversies/seminar-chinese-critique/`. For the 201 placeholder, paths under `/notes/201-planning/`.

The bootstrap pass should add this callout to every chapter file. Initially it links to stub files that exist but are empty. The author fills them in during the corresponding week.

### 4.2 Notes → book (the alias pattern)

Within the Obsidian vault, the author writes wiki-links freely:

```markdown
<!-- in notes/weeks/week-02-constrained/insights.md -->
The bordered Hessian connects directly to the second-order conditions
from [[week-01]]. Going to need this again in [[controversy-04]] when
working through the wage-profit frontier.
```

The wiki-links `[[week-01]]` and `[[controversy-04]]` resolve in Obsidian to files in `notes/_book-aliases/`. Each alias file is a single-page redirect-style document that links out to the book chapter and the corresponding notes-track index. See §2.3 above for the alias page template.

In the Quartz-rendered output, clicking the link takes the reader to the alias page, which then links out to the book. Two-hop, intentionally.

### 4.3 Notes → notes

Internal notes-to-notes wiki-links work natively in Obsidian and Quartz. No special convention needed. The author writes `Came back to this in [[insights]]` and Quartz resolves it via wiki-link search.

---

## 5. Documentation deliverables

### 5.1 `notes/_meta/workflow.md`

A standalone workflow document, distinct from the project README and CONTRIBUTING.md. Describes how to actually work in the repo on a daily basis: when to write what where, the rhythm of a week, how the notes-and-book separation plays out in practice, what to do when something breaks.

This document is a separate deliverable produced alongside this addendum (see the second file accompanying this PRD).

### 5.2 Updates to existing docs

`README.md` (project root): add a paragraph under "Quick start" explaining that the project has both a book section and a notes section, with the deployed URLs of each.

`CONTRIBUTING.md`: add new sections covering:
- Adding notes (the Obsidian vault conventions, where to put what).
- The `.author-notes` callout class (mandatory for the strip script).
- The alias-page convention for cross-linking from notes to book.
- The two-build-tool model and how to preview each.

`notes/README.md`: a brief vault-level orientation. What's here, how it's organized, how to open it in Obsidian.

`quartz/README.md` (new): explains the Quartz installation, the symlink, common operations.

### 5.3 Updates to `.gitignore`

Add the entries listed in §2.4 above.

---

## 6. Open questions added

These augment §11 of the original PRD and §5 of Addendum 1.

### 6.1 Wiki-link rewriting

Default: keep the alias-page pattern (notes wiki-link to alias page, alias page links out to book). The two-hop is acceptable. If the author finds it annoying after a few weeks of use, write a small Quartz transformer that rewrites `[[week-01]]` directly to the book URL when found in notes content. Defer this decision to after Week 3 or 4 of actual use.

### 6.2 Quartz theme customization

v1 ships with the default Quartz theme. The author may want to adjust typography, color scheme, or layout to match the Quarto book's visual identity. Defer to post-bootstrap.

### 6.3 Notes search

Quartz includes search by default for content within the notes section. Quarto includes search for the book. These are separate search indices. Whether to merge them (so a single search box on the deployed site covers both) is a non-trivial implementation question. Defer to post-bootstrap.

### 6.4 Backlink display in book chapters

When a notes file links to a book chapter via the alias pattern, the alias page has the backlink. The book chapter itself doesn't show that it's been referenced from notes. Whether to add some kind of "References from notes" footer to book chapters is a question to revisit if the author finds it useful after some weeks of work.

---

## 7. Acceptance criteria additions

These augment §10 of the original PRD and §6 of Addendum 1.

19. Quartz is installed at `quartz/` with the symlink to `../notes/` working.
20. `cd quartz && npx quartz build --serve` runs locally and serves the rendered notes site.
21. The notes vault has the per-week and per-controversy directory structure with at least `index.md` files (stubs acceptable).
22. The `_book-aliases/` directory contains an alias file for each week and controversy, with the template described in §2.3.
23. Every book chapter `.qmd` contains an "Author's notes" callout with the `.author-notes` class and links to the corresponding notes pages.
24. The `.author-notes` strip script at `assets/scripts/strip-author-notes.py` exists and removes the callouts when run against a chapter file. Includes a basic test that round-trips a sample.
25. The CI workflow runs both Quarto and Quartz builds, stitches outputs, deploys to GitHub Pages.
26. Opening `notes/` as an Obsidian vault works: wiki-links resolve, backlinks render, graph view shows the structure.
27. The deployed site has accessible content at both `/` (book) and `/notes/` (notes).
28. `notes/_meta/workflow.md` exists and matches the document delivered alongside this addendum.
29. `CONTRIBUTING.md` has been updated with the four new sections specified in §5.2.

---

## 8. Handoff notes for Claude Code

If you (Claude Code) are reading this addendum as a task brief alongside the original PRD and Addendum 1:

- Read the original PRD, then Addendum 1, then this addendum, in that order. Where they conflict, the latest wins.
- The largest single piece of work is setting up the Quartz installation and the symlinked vault structure. Test that `npx quartz build` works locally before committing the build pipeline changes.
- The `_book-aliases/` files should all be created during bootstrap with the template from §2.3, with `USERNAME` and the deployed URL placeholder filled in once the author confirms them. If those values aren't known at bootstrap time, leave them as `{{USERNAME}}` and `{{SITE_URL}}` placeholders and note this in the bootstrap report.
- The "Author's notes" callout (§4.1) must be added to every existing chapter file. Use the chapter's actual slug for the URLs (e.g., `/notes/weeks/week-03-linear-algebra/...`).
- Reverse the `notes/` gitignore from the original PRD. Notes are now committed.
- The `notes/_meta/workflow.md` file is a separate deliverable accompanying this addendum. Place it at that path verbatim from the source provided.
- Six per-week and seven per-controversy notes directories need creating, plus the seminar and 201-planning directories. Each gets the full sub-file structure (`index.md`, `reading-notes.md`, `questions.md`, `insights.md`, `refs.md`). The four sub-files are committed as empty stubs (one-line "Notes for [unit]" content is acceptable; do not invent substantive content).
- The Obsidian `.obsidian/` config files should be created with reasonable defaults (community plugins not installed by default; the author can add them later). At minimum `app.json` with sensible editor settings.
- The strip-author-notes script must actually work, with a small unit test verifying round-trip behavior on a sample chapter.
- The CI workflow update is non-trivial. Test it on a feature branch before merging to main; the existing build is presumably working and shouldn't be broken by this change.
- After the bootstrap is complete, append to `BOOTSTRAP_REPORT.md` (or create `ADDENDUM2_REPORT.md`) summarizing what was built and any deviations.

---

*End of PRD Addendum 2.*