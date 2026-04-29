# Quartz — notes-track build tool

This directory hosts the [Quartz v4](https://quartz.jzhao.xyz/) installation that renders the Obsidian vault at `../notes/` to a static site under `/notes/` on the deployed book site.

Quartz is *not* vendored into this repo. The committed files are:

- `quartz.config.ts` — our customizations (site title, base URL, plugin order, etc.).
- `quartz.layout.ts` — our layout overrides.
- `package.json` — a thin shim with the install/build scripts the author and CI invoke.
- `content` → `../notes/` — symlink that points Quartz at the vault. Quartz expects its content to live at `./content/`; the symlink keeps the vault visible at the repo root while satisfying that convention.
- `setup.sh` — fetches Quartz itself into this directory.
- `.gitignore` — excludes `node_modules/`, `public/`, `.quartz-cache/`, and the bits of Quartz that get fetched on first install.

## First-time setup (per machine)

```bash
cd quartz
bash setup.sh           # clones jackyzha0/quartz into this dir, preserving overrides
npm ci                  # installs Node deps
```

`setup.sh` is idempotent. It clones the [Quartz v4](https://github.com/jackyzha0/quartz/tree/v4) tree into a temp directory, copies any files that aren't already present here (so our `quartz.config.ts`, `quartz.layout.ts`, etc. win), and cleans up.

## Daily use

```bash
cd quartz
npx quartz build --serve     # http://localhost:8080, watches ../notes/
```

## Build (one-shot)

```bash
cd quartz
npx quartz build             # output: ./public/
```

The CI workflow (`.github/workflows/render.yml`) runs `npm ci && npx quartz build` after Quarto's render step and then stitches `quartz/public/` into the deploy directory under `_site/notes/`.

## Symlink note

The `content` symlink works on macOS and Linux out of the box. On Windows you need either developer mode enabled or a junction point. The author works on macOS, so this is fine for v1.

## Customizing further

Theme, plugin order, search behavior, and explorer config all live in `quartz.config.ts` and `quartz.layout.ts`. After editing, restart `npx quartz build --serve`. See [Quartz docs](https://quartz.jzhao.xyz/configuration) for the full surface.
