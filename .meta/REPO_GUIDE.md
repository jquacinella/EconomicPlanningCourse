# EconomicPlanningCourse Repository Guide

> **For AI assistants and developers**: This document provides deep context about the repository organization, build system, deployment, and common issues. Read this alongside the main README.md.

**Last updated**: 2026-04-30

---

## Table of Contents

1. [Quick Reference](#quick-reference)
2. [Architecture Overview](#architecture-overview)
3. [Build & Deployment Pipeline](#build--deployment-pipeline)
4. [Key Configuration Files](#key-configuration-files)
5. [Common Issues & Solutions](#common-issues--solutions)
6. [Important Gotchas](#important-gotchas)
7. [Debugging Workflows](#debugging-workflows)
8. [Historical Context](#historical-context)

---

## Quick Reference

### Deployed Site Structure

```
https://jquacinella.github.io/EconomicPlanningCourse/
├── /                           ← Landing page (site-root/index.html)
├── /courses/
│   ├── /the_calculation_course/  ← Quarto book
│   ├── /201/                     ← Quarto book
│   └── /the_crypto_course/       ← Quarto book
└── /notes/                      ← Quartz notes site
    ├── /the_calculation_course/
    ├── /201/
    └── /the_crypto_course/
```

### File System → Deployment Mapping

```
Repository                                  Deployed URL
─────────────────────────────────────────  ──────────────────────────────────────────────
courses/the_calculation_course/_book/      → /courses/the_calculation_course/
quartz/public/                             → /notes/
site-root/index.html                       → /index.html
```

### Critical Commands

```bash
# Local development (live reload)
make dev              # Book at :4444
make dev-notes        # Notes at :8080

# Full site preview (before deploying)
make preview          # All at :9200

# Build for deployment (mimics CI)
make build            # Builds everything into _site/

# Clean all artifacts
make clean
```

---

## Architecture Overview

### Monorepo Structure

This is a **multi-course monorepo** where:
- Each course is a **Quarto book** (rendered to HTML/PDF/EPUB)
- Each course has an **Obsidian notes vault** (rendered by Quartz)
- All courses share common assets, themes, and configuration
- Everything deploys to a single GitHub Pages site

### Two Parallel Tracks

Each course has two tracks that are built and deployed independently:

1. **Book track** (Quarto)
   - Source: `courses/<name>/*.qmd`
   - Builder: Quarto
   - Output: `courses/<name>/_book/`
   - Deployed to: `/courses/<name>/`

2. **Notes track** (Quartz)
   - Source: `courses/<name>/notes/*.md`
   - Builder: Quartz (static site generator)
   - Output: `quartz/public/`
   - Deployed to: `/notes/`

### Linking Between Tracks

Course pages link to notes using:
```markdown
[Reading notes]({{< var notes-base >}}/the_calculation_course/weeks/week-01-multivariable/reading-notes)
```

Where `notes-base` is defined in `courses/<name>/_variables.yml`:
```yaml
notes-base: "https://jquacinella.github.io/EconomicPlanningCourse/notes"
```

**CRITICAL**: Quartz generates URLs **without trailing slashes**. Always link to notes without trailing slashes or you'll get 404s.

---

## Build & Deployment Pipeline

### GitHub Actions Workflow (`.github/workflows/render.yml`)

The deployment has **3 jobs** that run in sequence:

#### Job 1: `render-books` (matrix strategy)

Renders each course book independently:

```yaml
matrix:
  course: [the_calculation_course, 201, the_crypto_course]
```

For each course:
1. Checkout code
2. Set up Python (version from `.python-version`)
3. Install `uv` and sync dependencies (`uv sync`)
4. Set up Quarto
5. Render book: `uv run quarto render --to html`
6. Verify output exists: check for `_book/index.html`
7. Upload artifact: `book-<course>` containing `_book/`

#### Job 2: `build-notes`

Builds the unified notes site with Quartz:

1. Checkout code
2. Set up Node.js 22 (Quartz v4 requirement)
3. Run `quartz/setup.sh` to fetch Quartz
4. Install dependencies: `npm ci`
5. Build: `npx quartz build`
6. Verify output: check for `quartz/public/index.html`
7. Upload artifact: `notes-site` containing `quartz/public/`

#### Job 3: `stitch-and-deploy`

Combines all artifacts and deploys to GitHub Pages:

1. Download all `book-*` artifacts to `_artifacts/books/`
2. Download `notes-site` artifact to `_artifacts/notes/`
3. **Stitch** everything into `_site/`:
   ```bash
   cp site-root/index.html _site/index.html
   cp -r _artifacts/books/book-<course>/. _site/courses/<course>/
   cp -r _artifacts/notes/. _site/notes/
   ```
4. Upload `_site/` as Pages artifact
5. Deploy to GitHub Pages

### Deployment Timeline

- **Trigger**: Push to `main` branch
- **Duration**: ~5-10 minutes (3 courses render in parallel)
- **Propagation**: GitHub Pages CDN ~5 minutes
- **Cache TTL**: 600 seconds (10 minutes)

---

## Key Configuration Files

### Quarto Configuration

#### `shared/_quarto-base.yml`
Base configuration inherited by all courses. Defines:
- Shared theme (dark/light mode)
- Grid layout (sidebar, body, margin widths)
- Common includes (JSXGraph, fonts, etc.)
- PDF/EPUB settings

#### `courses/<name>/_quarto.yml`
Per-course configuration. **CRITICAL** settings:

```yaml
project:
  type: book
  output-dir: _book

# THIS IS REQUIRED for GitHub Pages subdirectory deployment!
website:
  site-url: "https://jquacinella.github.io/EconomicPlanningCourse/courses/<name>"

book:
  title: "..."
  chapters: [...]

format:
  html:
    include-in-header:
      - ../../shared/assets/jsxgraph-include.html
      - ../../shared/assets/font-picker.html
      - ../../shared/assets/notes-links.html  # Runtime URL rewriting
```

**Why `website.site-url` is required**:
- Without it, Quarto assumes the book is at the domain root
- Generates incorrect links for navigation, search, etc.
- **Never remove this**, even though it seems unused!

#### `courses/<name>/_variables.yml`
Quarto variables accessible in `.qmd` files via `{{< var name >}}`:

```yaml
notes-base: "https://jquacinella.github.io/EconomicPlanningCourse/notes"
```

### Quartz Configuration

#### `quartz/content/`
Symlinks to course notes directories:

```bash
the_calculation_course -> ../../courses/the_calculation_course/notes
201 -> ../../courses/201/notes
the_crypto_course -> ../../courses/the_crypto_course/notes
```

**Quartz reads these symlinks** to find content. They're created by `quartz/setup.sh`.

#### `quartz/quartz.config.ts`
Quartz site configuration. Important settings:
- `baseUrl`: must match GitHub Pages URL
- `ignorePatterns`: patterns to exclude (e.g., `.obsidian/`)

### JavaScript Runtime Fixes

#### `shared/assets/notes-links.html`
Injected into every book page. Rewrites notes links at runtime:

```javascript
// On localhost → rewrites to http://localhost:8080
// On GitHub Pages → leaves production URL intact
```

This enables `make dev` + `make dev-notes` to work with relative notes links.

---

## Common Issues & Solutions

### Issue 1: Notes Links Return 404

**Symptom**: Clicking notes links from course pages → 404

**Cause**: Trailing slash mismatch
- Quartz generates URLs without trailing slashes: `/reading-notes`
- Course links had trailing slashes: `/reading-notes/`

**Solution**: Remove trailing slashes from all notes links in `.qmd` files:

```bash
find courses/<name> -name "*.qmd" -exec sed -i 's|notes-base >}}/\([^)]*\)/)|notes-base >}}/\1)|g' {} +
```

**Prevention**: Always link to notes without trailing slashes

---

### Issue 2: Course Navigation Broken After Deploy

**Symptom**: Internal links within course book don't work on GitHub Pages

**Cause**: Missing `website.site-url` in `_quarto.yml`

**Solution**: Add to each course's `_quarto.yml`:

```yaml
website:
  site-url: "https://jquacinella.github.io/EconomicPlanningCourse/courses/<name>"
```

**Prevention**: Never remove `website:` section from `_quarto.yml`

---

### Issue 3: Landing Page Links Broken Locally

**Symptom**: Landing page links don't work with `quarto preview`

**Cause**: Landing page uses root-relative links (`/courses/...`) which only work when served from repo root

**Solution**: 
- For local development: use `make preview` (serves stitched site at :9200)
- Don't use `quarto preview` for landing page testing

---

### Issue 4: Notes Changes Not Appearing

**Symptom**: Changed `.md` files in `courses/<name>/notes/` but Quartz doesn't show updates

**Possible causes**:
1. Quartz dev server not watching files → restart `make dev-notes`
2. Symlinks not working → verify `ls -la quartz/content/`
3. File in `.obsidian/` or ignored pattern → check `quartz.config.ts`

**Debug**:
```bash
# Check symlinks
ls -la quartz/content/

# Rebuild from scratch
cd quartz
rm -rf public .quartz-cache
npx quartz build
```

---

### Issue 5: "Module not found" or Python Errors

**Symptom**: Quarto render fails with Python import errors

**Cause**: Course dependencies not installed or `uv` not synced

**Solution**:
```bash
cd courses/<name>
uv sync         # NOT uv sync --frozen (we don't have uv.lock yet)
```

---

## Important Gotchas

### Gotcha 1: Trailing Slashes

**Rule**: Quartz generates URLs without trailing slashes. Always link WITHOUT trailing slashes.

❌ Wrong:
```markdown
[Reading notes]({{< var notes-base >}}/path/to/page/)
```

✅ Correct:
```markdown
[Reading notes]({{< var notes-base >}}/path/to/page)
```

### Gotcha 2: site-url is Not Optional

Even though `website.site-url` seems unused (it's a book, not a website), **it's required** for GitHub Pages subdirectory deployments.

Without it:
- Search doesn't work
- Navigation generates wrong URLs  
- RSS feeds break
- Social metadata incorrect

### Gotcha 3: Quarto Variable Expansion

Variables defined in `_variables.yml` are expanded at **render time**, not runtime.

```yaml
# _variables.yml
notes-base: "https://..."
```

```markdown
# .qmd file
[Link]({{< var notes-base >}}/path)
```

This becomes a hardcoded URL in the HTML. The JavaScript in `notes-links.html` then rewrites it at runtime for localhost.

### Gotcha 4: Git Symlinks

Symlinks in `quartz/content/` are committed to git. They work on:
- ✅ Linux/macOS
- ✅ GitHub Actions (Ubuntu)
- ⚠️ Windows (requires `core.symlinks=true`)

### Gotcha 5: Quartz Takes Time

Initial Quartz build is slow (~20s). Incremental builds are fast (~1s per file).

Don't kill the dev server too early - let it finish first build.

---

## Debugging Workflows

### Debug: "Link works locally but not on GitHub Pages"

1. Check trailing slashes:
   ```bash
   grep -r "notes-base.*/)$" courses/<name>/**/*.qmd
   ```

2. Check `site-url` configuration:
   ```bash
   grep "site-url" courses/<name>/_quarto.yml
   ```

3. Check deployed URL manually:
   ```bash
   curl -I https://jquacinella.github.io/EconomicPlanningCourse/[path]
   ```

4. Check GitHub Actions logs:
   - Go to repo → Actions → latest workflow
   - Check "Stitch outputs into _site/" step
   - Verify files were copied correctly

### Debug: "Quarto render fails"

1. Check Python environment:
   ```bash
   cd courses/<name>
   uv sync
   uv run python --version
   ```

2. Try rendering one file:
   ```bash
   uv run quarto render weeks/week-01-multivariable.qmd
   ```

3. Check for syntax errors in frontmatter:
   ```bash
   head -20 weeks/week-01-multivariable.qmd
   ```

### Debug: "Quartz build fails"

1. Check symlinks:
   ```bash
   ls -la quartz/content/
   file quartz/content/the_calculation_course  # should say "symbolic link"
   ```

2. Rebuild Quartz:
   ```bash
   cd quartz
   bash setup.sh  # re-fetches Quartz if needed
   npm ci
   npx quartz build
   ```

3. Check for invalid Markdown:
   - Unclosed code fences
   - Invalid wikilinks
   - Special characters in filenames

### Debug: "GitHub Actions failing"

1. Check workflow logs for exact error
2. Common issues:
   - Missing `_book/index.html` → Quarto render failed
   - Missing `quartz/public/index.html` → Quartz build failed
   - Artifact upload failed → Check path exists

3. Reproduce locally:
   ```bash
   make clean
   make build  # Mimics CI build
   ```

---

## Historical Context

### Past Issues (Resolved)

#### 2026-04-30: Trailing Slash Issue
- **Problem**: Notes links returning 404 on deployed site
- **Root cause**: Quartz generates URLs without trailing slashes, but course `.qmd` files had trailing slashes in links
- **Solution**: Used sed to remove trailing slashes from all notes links
- **Files affected**: 18 `.qmd` files (10 weeks + 8 controversies)
- **Commit**: "fix: remove trailing slashes from notes links to match Quartz URL structure"

#### 2026-04-30: Missing site-url
- **Problem**: Internal course navigation not working on GitHub Pages
- **Root cause**: Commit 666be70 removed `website.site-url` from `_quarto.yml` thinking it was unused
- **Solution**: Restored `website.site-url` to all three course configurations
- **Lesson**: `site-url` is required even for book projects deployed to subdirectories

### Design Decisions

#### Why Quarto + Quartz?

- **Quarto**: Great for technical writing with code execution, math, cross-references
- **Quartz**: Great for interconnected notes, wikilinks, graph view
- Together: Polished "textbook" + flexible "working notes"

#### Why Monorepo?

- Shared assets (CSS, JS, fonts)
- Consistent theme across courses
- Single deployment to GitHub Pages
- Easier to maintain than separate repos

#### Why Not Docusaurus/MkDocs/etc?

- Need executable Python code blocks → Quarto
- Need Obsidian-style wikilinks and graph view → Quartz
- Need both structured (book) and unstructured (notes) → two tools

---

## Reference Links

- **Deployed site**: https://jquacinella.github.io/EconomicPlanningCourse/
- **Quarto docs**: https://quarto.org/docs/
- **Quartz docs**: https://quartz.jzhao.xyz/
- **Uv docs**: https://docs.astral.sh/uv/

---

## For Future AI Assistants

When working on this repo:

1. **Always check the README first** for basic commands and structure
2. **Read this guide** for gotchas, debugging, and historical context
3. **Check `.github/workflows/render.yml`** to understand the deployment pipeline
4. **Test locally** with `make preview` before pushing
5. **Verify deployed URLs** with `curl -I` after deployment
6. **Document new issues** by updating this guide

Common first tasks:
- Fixing links → Check trailing slashes, `site-url` config
- Adding content → Edit `.qmd` files in `courses/<name>/weeks/`
- Adding notes → Edit `.md` files in `courses/<name>/notes/`
- Debugging build → Check logs in `.github/workflows/render.yml`

---

**End of guide**. See `.meta/old_setup/` for historical PRDs and reports from the initial setup phase.