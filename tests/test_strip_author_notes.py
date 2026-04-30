"""Round-trip tests for ``shared/assets/scripts/strip-author-notes.py``."""

from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = REPO_ROOT / "shared" / "assets" / "scripts" / "strip-author-notes.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("strip_author_notes", SCRIPT_PATH)
    assert spec and spec.loader, "could not load strip-author-notes.py"
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SAMPLE_CHAPTER = '''---
title: "Sample Chapter"
---

## Framing

Body paragraph one.

::: {.callout-note appearance="minimal" collapse="true" .author-notes}
## Author's notes for this chapter

- [Reading notes](/notes/sample/reading-notes/)
- [Open questions](/notes/sample/questions/)
:::

## Learning objectives

Body paragraph two.

::: {.callout-note}
## A regular callout that is NOT author notes
This should survive.
:::

## Bridge

Closing paragraph.
'''


def test_strip_removes_author_notes_block():
    mod = _load_module()
    stripped = mod.strip_author_notes(SAMPLE_CHAPTER)
    assert ".author-notes" not in stripped
    assert "Author's notes for this chapter" not in stripped


def test_strip_preserves_other_callouts():
    mod = _load_module()
    stripped = mod.strip_author_notes(SAMPLE_CHAPTER)
    assert "A regular callout that is NOT author notes" in stripped
    assert "## Framing" in stripped
    assert "## Learning objectives" in stripped
    assert "## Bridge" in stripped
    assert "Body paragraph one." in stripped
    assert "Body paragraph two." in stripped
    assert "Closing paragraph." in stripped


def test_strip_is_idempotent():
    mod = _load_module()
    once = mod.strip_author_notes(SAMPLE_CHAPTER)
    twice = mod.strip_author_notes(once)
    assert once == twice


def test_strip_no_op_when_no_author_notes():
    mod = _load_module()
    plain = "## Framing\n\nNo callouts here.\n"
    assert mod.strip_author_notes(plain) == plain


def test_process_writes_stripped_copies(tmp_path):
    mod = _load_module()
    src_root = tmp_path / "src"
    out_root = tmp_path / "out"
    chapter = src_root / "weeks" / "week-99-test.qmd"
    chapter.parent.mkdir(parents=True)
    chapter.write_text(SAMPLE_CHAPTER, encoding="utf-8")
    n = mod.process(src_root, out_root, [chapter])
    assert n == 1
    output = (out_root / "weeks" / "week-99-test.qmd").read_text(encoding="utf-8")
    assert ".author-notes" not in output
    assert "A regular callout that is NOT author notes" in output
    # original untouched
    assert ".author-notes" in chapter.read_text(encoding="utf-8")
