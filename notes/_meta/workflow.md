# How to work in this repo

This is the workflow document. It explains how the project is organized, how to write into it day-to-day, and what to do when something feels off. If you've inherited this repo from someone else, read this first. If you're the original author returning after a break, this is the orientation that gets you back into the rhythm.

The repo holds a long-form computational-economics learning project — ten weeks of mathematics plus seven controversies plus a seminar plus a placeholder for a follow-on course. The output is meant to work as both a published book (PDF, eventually print) and an interactive online edition with executable code, embedded widgets, and a separate notes section that captures the messy work behind the polished chapters.

Knowing about that two-track structure is most of what you need to use the repo well.

## The two tracks

Two kinds of content live here, and they go in different places.

**Book content** is the polished output. It lives in `weeks/`, `controversies/`, `seminar-chinese-critique.qmd`, `201/`, the appendices, and a few top-level files like `index.qmd`. It's written in Quarto Markdown (`.qmd`), which is regular Markdown plus YAML front matter and executable code blocks. This is what gets rendered into the public-facing book — both the website and the PDF.

**Notes content** is the working layer. It lives in `notes/`, organized as an Obsidian vault. Plain Markdown (`.md`) with wiki-links, no front matter required. This is your scratchpad, your reading log, your place to write questions you haven't answered yet, your accumulating store of insights that connect across chapters. It renders to a separate section of the public site (under `/notes/`) so you can click around and see your own work, but it's excluded from the PDF and the print artifact.

The reason for the split is simple: the friction of writing publication-grade Quarto for every Wednesday-evening reading session is what kills self-directed projects. You need a place to scratch. Obsidian is that place. The fact that the scratchpad is also visible on the website is a bonus — it means you can search your own notes, share a specific page with someone, or come back in three months and find what you wrote.

## The directory map

A condensed view, with the parts you'll touch most often called out:

```
morishima-track/
├── weeks/                              ← Book chapters (polished, you edit weekly)
├── controversies/                      ← Book chapters (polished, you edit during the controversies)
├── 201/, appendices/, ...              ← More book content (polished)
├── index.qmd                           ← Book landing page
│
├── notes/                              ← Your Obsidian vault (scratch, you write here daily)
│   ├── weeks/week-NN-*/                ← Per-week notes
│   ├── controversies/controversy-NN-*/ ← Per-controversy notes
│   ├── _book-aliases/                  ← Pages that wiki-links resolve to
│   ├── _meta/                          ← Workflow, progress log, decisions, deferred
│   └── attachments/                    ← Images, screenshots, PDFs you reference
│
├── notebooks/                          ← Standalone Jupyter for major project work
├── apps/                               ← Standalone Dash applications, deployed separately
├── data/                               ← Data files (BEA tables, IO tables, etc.)
├── sfc-notebooks/                      ← Reference Godley-Lavoie SFC implementations
├── minsky-models/, ravel-files/        ← Optional, for Steve Keen's tools
├── assets/                             ← Images, CSS, helper scripts, widget references
├── extensions/                         ← Quarto extensions
├── quartz/                             ← Quartz install (renders notes/ to web)
│
├── _quarto.yml                         ← Book config (don't edit during study weeks)
├── pyproject.toml                      ← Python dependencies
└── .github/workflows/                  ← CI/CD (don't edit during study weeks)
```

The two directories you'll be in most are `weeks/` (or `controversies/` later) for book content and `notes/weeks/` for scratch.

## A typical week

Here's the rhythm. It's not rigid — adapt to what works for you — but the bones are roughly the same every week.

**Sunday evening: orient.** Open the syllabus chapter for the week ahead. Read the framing paragraph and the resource schedule. Open the corresponding notes directory in Obsidian. If `progress.md` exists in `_meta/`, write three or four sentences in it: what you're working on this week, what you mean to accomplish by next Sunday. Ten minutes. Don't skip this — it's how next Sunday's you will know what this Sunday's you was thinking.

**Days 1 through 5: study.** Work through the videos, readings, and exercises that the syllabus's resource schedule lays out. Almost everything you write goes into the notes directory for this week. The four files there serve different purposes:

- `reading-notes.md` for what you absorbed from a video, paper, or textbook section. Date-stamp entries. Quote things that will matter later. Don't worry about phrasing; nobody is grading.
- `questions.md` for things you don't understand yet. Just write them as you encounter them, even if vague. Going back to old questions and finding answers in your own notes is one of the best moments in self-study.
- `insights.md` for moments where something clicks. Connections between chapters. Patterns you've noticed. The intuition you wished someone had told you. These are the bits you'll want when you go to write the polished version.
- `refs.md` for stuff you want to come back to but can't fit in this week. Papers cited in something you're reading. Side topics you noticed. Books that look interesting. Don't pretend you're going to read them all; just record them.

You also have `scratchpad.ipynb` — a Jupyter notebook for working calculations. Use this freely. Don't try to make it presentable. Run code, plot things, mess around. The point is to figure things out, not to produce a finished artifact.

Use Obsidian's wiki-links liberally. `[[week-01]]` resolves to a book-alias page that points at Week 1's polished chapter. `[[insights]]` resolves to whichever insights file is most recently in scope. `[[refs]]` ditto. You don't have to think about file paths; Obsidian's link autocomplete handles it.

Tag liberally too if you find that helpful — `#confused`, `#reread`, `#publishable` for things you might want in the polished chapter eventually. Tags become indices in Obsidian and indices on the rendered notes site.

**Day 6: project day.** The mini-project specified in the syllabus. Two routes:

The simpler one — work it out in `scratchpad.ipynb`, get it running ugly, then port the working version into the corresponding `.qmd` file in `weeks/` (or `controversies/`). Cleaning up as you go: better variable names, docstrings, prose framing between code blocks, fig captions where useful. The code blocks live inside the `.qmd` and Quarto runs them at build time, so what's in the chapter is the live, working code with its outputs.

The faster one — go directly into the `.qmd` file. Faster but riskier; you're trying to do exploration and presentation at the same time, which is hard. Use this when you know what the project should look like, probably from Week 5 or 6 onward.

If the project is large enough that putting it all inline would bloat the chapter, put the full version in `notebooks/week-NN-project.ipynb` and link to it from the chapter via a callout. Everyone wins: the chapter stays readable, the full project is preserved, the link points readers to the deeper work.

**Day 7 (optional): consolidate.** Read through the week's `.qmd` end to end. Does it make sense? Did the prose between code blocks survive your editing? Are the marginalia placed where they earn their keep? This is when the public-facing version becomes good. Skipping this is fine — the chapter remains a living document until the day you decide it's not.

## How book and notes link to each other

Each book chapter has a small collapsed callout near the top labeled "Author's notes for this week." It's hidden by default — non-author readers don't see notes prominently — but clicking the header expands it to show links to the corresponding notes pages: reading notes, questions, insights, refs, plus a link to the scratchpad notebook on GitHub.

This callout is the bridge from book to notes. Anyone reading the chapter can click into your scratch work if they want. You can use it yourself when re-reading: "what was I thinking when I wrote this?" — click, see the original questions and insights.

Going the other way, when you write notes referring to book content, use wiki-links. `[[week-01]]` in your notes resolves to a small alias page in `notes/_book-aliases/` that links out to the polished chapter. Two clicks instead of one, but it preserves the Obsidian experience: wiki-links work everywhere, autocomplete works, backlinks accumulate naturally.

If the two-hop pattern bugs you after a few weeks of use, there's a Quartz plugin option to rewrite the wiki-links directly to book URLs. Worth deferring until you've actually felt the friction.

## Building locally

Two tools, two preview commands. Run whichever corresponds to what you're editing.

**For book chapters:** `quarto preview` from the repo root. This watches the `.qmd` files and rebuilds on save. Open `localhost:4567` in a browser to see the result.

**For notes:** `cd quartz && npx quartz build --serve`. This watches the `notes/` directory (via the symlink at `quartz/content`) and rebuilds the notes site. Open `localhost:8080`.

You can run both at once in different terminals if you're working on both tracks.

The first time you set up the repo on a new machine, you'll need to install dependencies for both. For Python: `uv sync` from the repo root. For Quartz: `cd quartz && npm ci`. Then both preview commands work.

Quarto re-executes code blocks by default. To avoid waiting for a long-running computation on every save, use the `freeze: auto` option in the chapter's YAML — Quarto then caches outputs and only re-runs cells when the source has changed. This is set globally in `_quarto.yml` already, so most of the time you don't think about it.

## Committing work

Commit small, commit often, and write honest messages. The audience is future-you, not a code review.

Useful commit-message patterns:

- "Week 3 reading notes: through Strang lecture 5"
- "Week 3 scratchpad: tried RREF by hand, finally working"
- "Week 3 chapter draft: implementation section in progress"
- "stuck on chain rule for partials, returning tomorrow"

A week shouldn't be one giant commit. Three to ten small commits per week is normal. Push to GitHub at the end of every study session — the deployed site rebuilds, and you have an offsite backup of your work.

If a build fails on push, that's information about your code or content, not a problem with the workflow. Look at the GitHub Actions log, fix the underlying issue, push again. Don't add CI complexity to work around a real bug.

## When it's time to publish

The book PDF is produced by running `quarto render --to pdf` from the repo root. This uses the default profile and renders all the book chapters. The notes never enter the print pipeline — they aren't in the chapter list.

When you decide a print-targeted version of the book is needed (for example, removing early weeks or polishing for a publisher), the workflow has two steps:

1. **Strip author-notes callouts.** Run `python assets/scripts/strip-author-notes.py`. This produces a `build-print/` directory with copies of every `.qmd` minus the "Author's notes" callouts. The original chapter files are untouched.

2. **Render with the print profile.** `QUARTO_PROFILE=print quarto render build-print/ --to pdf`. The `print` profile in `_quarto.yml` defines which chapters belong in the print artifact — start identical to default, edit when you have a clear publication scope.

The point of this two-step pattern is that the public website always shows the full project (including author-notes callouts and the notes section), while the print artifact shows only the publication-targeted version. Same source, different outputs.

## Files in `_meta/`

Four files in `notes/_meta/` deserve specific mention.

**`workflow.md`** is this document. Update it if the workflow itself changes meaningfully — for example, if you abandon Obsidian for some other tool, or if the build pipeline changes shape. It exists to onboard a future reader (yourself or someone else) to the repo's conventions.

**`progress.md`** is a running log. Date-stamped entries, three or four sentences each. What you worked on, what you finished, what got stuck. The entries are short on purpose. The value is in the accumulation — three months from now you'll be able to scroll back and see exactly how you got here.

**`deferred.md`** is for things you noticed but can't address now. Tooling annoyances. Side topics. Refactoring you'd like to do. Format: a bullet list with brief context. When you have a free Saturday and want to scratch a process itch, this is where the candidates live.

**`decisions.md`** is for methodological choices and their reasoning. "Skipped 18.03's Fourier unit because the syllabus says it's optional." "Decided to merge `insights.md` and `reading-notes.md` from Week 5 onward because I never used both." "Switched from `pulp` to `cvxpy` for Week 8's project because the dual variables come back cleaner." Anytime you make a choice that future-you might want to second-guess, write down why you made it. Costs you a minute, saves you an hour later.

## When something feels off

A few specific failure modes and what to do about them.

**You're consistently behind schedule.** This is information, not failure. After Week 3, look honestly at what you've actually completed. If the syllabus's pacing isn't matching reality, adjust. Spreading Week 4 over two calendar weeks is a perfectly reasonable response. The course is yours.

**You haven't written notes in a while but you've been doing the work.** Common pattern. Set aside thirty minutes and reconstruct. Even a paragraph in `progress.md` saying "I worked through linear algebra in the second half of last week without writing notes; the main thing I learned is X" is better than nothing. Don't try to retroactively reconstruct everything; just capture the substance.

**The build is broken on GitHub but works locally.** Almost always a missing dependency or a path issue. Check the Actions log; look for the first error. Common culprits: a Python package you installed locally isn't in `pyproject.toml`, or a file path with the wrong case (macOS is case-insensitive by default, Linux isn't).

**You want to make a tooling change mid-week.** Note it in `_meta/deferred.md` and come back to it on a non-study weekend. Mid-week tooling changes consume study time you can't replace.

**You're not sure whether something belongs in notes or in the chapter.** Default to notes. Most things start there; the best ones graduate. Going the other way — pulling something out of a polished chapter and back into scratch — is a sign you committed too early.

**You finished a week and you're not sure if you "got it."** Re-read your own questions file. If you can answer most of the questions you wrote, you got it. If a few are still open, leave them in `refs.md` for later — material from later weeks often resolves earlier confusions. Mathematics and political economy both work that way.

## Closing note

The repo will accumulate value over the months you work in it. Notes you wrote in Week 2 will inform a paragraph you write in Controversy 3. A question from Week 5 will get answered while you're reading Cockshott in Week 8. A scratchpad calculation from Week 9 will turn into a clean figure in Controversy 7's chapter.

Trust this. Don't try to be tidy upfront. Write into the notes track freely; pull the best of it into the book track when it's ready; let the cross-references emerge as you work. The two-track structure exists to support exactly this kind of accumulation.

The book is the artifact. The notes are how the book gets made.

Now go to Week 1.