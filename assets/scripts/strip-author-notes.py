"""Strip ``.author-notes`` callout blocks from Quarto chapter sources.

Reads every ``.qmd`` file under the configured chapter directories
(``weeks/``, ``controversies/``, ``201/``, ``appendices/``, plus the
top-level ``index.qmd`` etc.) and writes a copy with every fenced div
that carries the ``author-notes`` class removed. Output lands in
``build-print/`` mirroring the source layout.

Intended workflow::

    python assets/scripts/strip_author_notes.py
    QUARTO_PROFILE=print quarto render build-print/ --to pdf

The original chapter files are never modified.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path
from typing import Iterable

# A fenced div opens with ``::: {.callout-note ... .author-notes ...}`` (the
# attribute order is irrelevant) and closes with the next ``:::`` that sits at
# the start of its line and is followed by either end-of-line or end-of-file.
# We greedily match across lines but stop at the first closing fence.
AUTHOR_NOTES_PATTERN = re.compile(
    r"""
    ^:::\s*\{[^}]*\.author-notes[^}]*\}\s*\n  # opening fence with .author-notes class
    .*?                                       # body (non-greedy, multiline)
    ^:::\s*$\n?                               # closing fence on its own line
    """,
    re.MULTILINE | re.DOTALL | re.VERBOSE,
)

DEFAULT_INCLUDES = (
    "weeks",
    "controversies",
    "201",
    "appendices",
)
DEFAULT_TOP_LEVEL = (
    "index.qmd",
    "master-resources.qmd",
    "post-course.qmd",
    "where-this-lands.qmd",
)


def strip_author_notes(text: str) -> str:
    """Return ``text`` with all ``.author-notes`` fenced divs removed."""
    return AUTHOR_NOTES_PATTERN.sub("", text)


def iter_qmd(roots: Iterable[Path]) -> Iterable[Path]:
    for root in roots:
        if root.is_file() and root.suffix == ".qmd":
            yield root
        elif root.is_dir():
            yield from sorted(root.rglob("*.qmd"))


def process(source_root: Path, output_root: Path, files: Iterable[Path]) -> int:
    count = 0
    for src in files:
        rel = src.relative_to(source_root)
        dst = output_root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        original = src.read_text(encoding="utf-8")
        stripped = strip_author_notes(original)
        dst.write_text(stripped, encoding="utf-8")
        count += 1
    return count


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("."),
        help="Project root (default: current directory).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("build-print"),
        help="Output directory (default: build-print/).",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove the output directory before writing.",
    )
    args = parser.parse_args(argv)

    source = args.source.resolve()
    output = args.output.resolve()

    if args.clean and output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)

    roots = [source / d for d in DEFAULT_INCLUDES if (source / d).is_dir()]
    roots += [source / f for f in DEFAULT_TOP_LEVEL if (source / f).is_file()]

    files = list(iter_qmd(roots))
    n = process(source, output, files)
    print(f"Stripped author-notes from {n} .qmd file(s); wrote to {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
