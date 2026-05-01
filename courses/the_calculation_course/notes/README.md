# Notes vault

This directory is an [Obsidian](https://obsidian.md/) vault. It's the working layer of the Calculation Course project — reading notes, questions, insights, methodological decisions, progress logs.

The polished book content lives elsewhere (`weeks/`, `controversies/`, etc., at the repo root). This vault is the scratchpad behind it. Both render to the same deployed site under different URL prefixes; this vault is rendered by [Quartz](https://quartz.jzhao.xyz/) and served at `/notes/`.

## How to open it

Open Obsidian, choose "Open folder as vault", and point it at this directory (`notes/`). Wiki-links, backlinks, tags, and graph view all work.

## Layout

- `weeks/week-NN-*/` — per-week notes (one directory per book chapter under `weeks/`).
- `controversies/controversy-NN-*/` — per-controversy notes.
- `_book-aliases/` — short alias pages that wiki-links resolve to. They link out to the corresponding book chapter and notes directory. See `_meta/workflow.md` for the convention.
- `_meta/` — workflow doc, progress log, deferred items, decisions, glossary.
- `attachments/` — images, PDFs, screenshots referenced in notes.

Each per-unit directory has the same starting set of files: `index.md`, `reading-notes.md`, `questions.md`, `insights.md`, `refs.md`. They start as stubs; the author fills them in during the corresponding week. The structure is a starting suggestion, not a contract — rename, merge, or delete as the work demands.

## Daily rhythm

See [`_meta/workflow.md`](_meta/workflow.md) for the full workflow document.
