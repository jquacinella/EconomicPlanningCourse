# `minsky-models/` — Steve Keen's Minsky model files

[Minsky](https://sourceforge.net/projects/minsky/) is Steve Keen's open-source system-dynamics modelling tool, designed specifically for monetary economics with built-in stock-flow-consistent accounting (Godley tables) on a graphical canvas.

It is most directly relevant to **Controversy 6** (monetary theory of production) and the Minsky-Keen debt dynamics in Version 3 of that controversy's capstone project. Optionally also for **Controversy 5** (the ergodicity sidebar's distributional debt simulations).

## Where to download

- Project page: <https://sourceforge.net/projects/minsky/>
- Tutorials: Steve Keen's YouTube channel, especially the playlist *Minsky Tutorials*. <https://www.youtube.com/@ProfSteveKeen>
- Documentation: bundled with the application.

Minsky is free, open source (GPL), and runs on Linux, macOS, and Windows.

## What goes in this directory

- `.mky` files: Minsky model files. These are XML, so they diff reasonably well in git.
- Optional companion `.md` notes describing the model and its calibration.

## Conventions

- Each model goes in its own subdirectory if it has supporting files (CSV inputs, exported plots), otherwise just at this level.
- Document any non-obvious calibration choices in a `<model-name>.md` next to the `.mky`.
- The build does not depend on Minsky being installed. Files here are author-side artifacts; the rendered book may reference exported screenshots of a Minsky model, but the rendering pipeline never tries to open the `.mky` itself.

## Files

(none yet — this directory is empty in v1)
