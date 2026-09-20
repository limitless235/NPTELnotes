#!/usr/bin/env bash
# Build notes-2 volume PDFs.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
COURSE="courses/01-cyber-security-and-privacy"
NOTES="$ROOT/$COURSE/notes-2"
PDF="$NOTES/pdf"
MIRROR="$ROOT/Cyber Security and Privacy/notes 2"

mkdir -p "$PDF" "$MIRROR"

python3 "$ROOT/scripts/assemble-notes2.py"

build_one() {
  local vol="$1"
  local input="$NOTES/$vol.md"
  local build="$NOTES/.pdf-build/${vol}"
  echo "Building $vol ..."
  PREPROCESSED="$(python3 "$ROOT/scripts/preprocess-mermaid.py" "$input" "$build")"
  pandoc "$PREPROCESSED" \
    -o "$PDF/${vol}.pdf" \
    --resource-path="$build" \
    --from=markdown+tex_math_dollars+tex_math_single_backslash \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V fontsize=11pt \
    -V documentclass=article \
    -V mainfont="DejaVu Serif" \
    -V monofont="DejaVu Sans Mono" \
    --toc \
    --toc-depth=2 \
    -V colorlinks=true \
    -V linkcolor=blue \
    -V title="Cyber Security and Privacy — ${vol}"
  cp "$PDF/${vol}.pdf" "$MIRROR/${vol}.pdf"
  echo "Built: $PDF/${vol}.pdf"
}

for v in vol-01 vol-02 vol-03 vol-04 vol-05; do
  build_one "$v"
done

echo "All notes-2 PDFs built."
