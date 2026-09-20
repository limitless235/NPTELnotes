#!/usr/bin/env bash
# Build notes-2 volume PDFs (mermaid preprocess + pandoc + XeLaTeX).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
COURSE="courses/05-information-security-cec"
NOTES_DIR="$ROOT/$COURSE/notes-2"
PDF_DIR="$NOTES_DIR/pdf"

mkdir -p "$PDF_DIR"

build_one() {
  local vol="$1"
  local input="$NOTES_DIR/${vol}.md"
  local build_dir="$NOTES_DIR/.pdf-build/${vol}"
  local output="$PDF_DIR/${vol}.pdf"
  echo "Building $vol ..."
  local preprocessed
  preprocessed="$(python3 "$ROOT/scripts/preprocess-mermaid.py" "$input" "$build_dir")"
  pandoc "$preprocessed" \
    -o "$output" \
    --resource-path="$build_dir" \
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
    -V linkcolor=blue
  echo "Built: $output"
}

for v in vol-01 vol-02 vol-03 vol-04; do
  build_one "$v"
done
echo "All notes-2 PDFs built."
