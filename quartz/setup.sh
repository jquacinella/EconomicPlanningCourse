#!/usr/bin/env bash
# Fetch Quartz v4 into this directory without overwriting our overrides.
# Idempotent: re-running pulls latest Quartz v4 changes without clobbering
# the committed config files (quartz.config.ts, quartz.layout.ts, package.json,
# README.md, setup.sh, .gitignore, content/).
set -euo pipefail

QUARTZ_REPO="https://github.com/jackyzha0/quartz.git"
QUARTZ_BRANCH="v4"
TMPDIR="$(mktemp -d)"
HERE="$(cd "$(dirname "$0")" && pwd)"

# Files/directories we own and must never overwrite, even if Quartz upstream ships them.
# NOTE: package.json and package-lock.json come from upstream Quartz on
# purpose — they declare the `quartz` CLI bin and the v4 dependency tree
# that `npm ci` and `npx quartz build` rely on. Don't add them here.
PROTECTED=(
  quartz.config.ts
  quartz.layout.ts
  notes-overrides.tsx
  README.md
  setup.sh
  .gitignore
  content
)

cleanup() { rm -rf "$TMPDIR"; }
trap cleanup EXIT

echo "Cloning Quartz $QUARTZ_BRANCH from $QUARTZ_REPO ..."
git clone --depth=1 --branch "$QUARTZ_BRANCH" "$QUARTZ_REPO" "$TMPDIR/quartz"

echo "Overlaying Quartz files into $HERE (preserving overrides) ..."
cd "$TMPDIR/quartz"
# Don't bring upstream's git history along.
rm -rf .git
shopt -s dotglob nullglob
for path in *; do
  base="$(basename "$path")"
  skip=0
  for protected in "${PROTECTED[@]}"; do
    if [[ "$base" == "$protected" ]]; then skip=1; break; fi
  done
  if [[ $skip -eq 1 ]]; then
    echo "  preserve: $base"
    continue
  fi
  cp -R "$path" "$HERE/"
done

# Ensure the content/ directory exists with per-book symlinks.
# content/ is a real directory (not a symlink) containing one symlink per
# course or research project. Each symlink points at that book's notes/ vault
# relative to the quartz/ dir.
mkdir -p "$HERE/content"

declare -A COURSE_LINKS=(
  ["the_calculation_course"]="../../courses/the_calculation_course/notes"
  ["marxian_formalization"]="../../research/marxian_formalization/notes"
  ["postcapitalism_after_ai"]="../../research/postcapitalism_after_ai/notes"
)

for name in "${!COURSE_LINKS[@]}"; do
  target="${COURSE_LINKS[$name]}"
  link="$HERE/content/$name"
  if [[ -L "$link" ]]; then
    # Symlink already exists (committed to git or from a previous run) — leave it alone.
    echo "  exists: content/$name"
  else
    ln -s "$target" "$link"
    echo "  created symlink: content/$name -> $target"
  fi
done

echo "Done. Now run: npm ci && npx quartz build --serve"
