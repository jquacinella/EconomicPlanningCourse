"""Render a static SVG fallback for a JSXGraph widget.

Stub. Implement when the first chapter with critical JSXGraph content needs a
PDF-readable static figure. JSXGraph widgets are HTML-only; the PDF book is a
secondary output and a static fallback by design.

Intended interface (subject to revision when first implemented):

    python assets/scripts/render-jsxgraph-fallback.py \\
        --config path/to/widget.json \\
        --output path/to/figure.svg

Where ``--config`` is a JSON description of the widget (function expression,
parameter values to freeze, axis bounds) and ``--output`` is the target SVG.
The expected approach: evaluate the configured curves in numpy, render with
matplotlib as SVG, and emit. Matplotlib is already a project dependency
(see ``pyproject.toml``).

See PRD Addendum 1, §1.6 (PDF rendering implications) and §5.1 (Open question
on whether to implement now or defer). Default per the addendum: **defer**.
"""

from __future__ import annotations

import sys


def main() -> int:
    sys.stderr.write(
        "render-jsxgraph-fallback.py: stub — not yet implemented.\n"
        "See PRD Addendum 1 §1.6 and §5.1.\n"
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
