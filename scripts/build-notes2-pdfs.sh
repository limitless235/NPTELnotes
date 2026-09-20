#!/usr/bin/env bash
# Build notes-2 volume PDFs (transcript-grounded Generative AI notes).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
COURSE="courses/03-generative-ai-llms"
NOTES_DIR="$ROOT/$COURSE/notes-2"
PDF_DIR="$NOTES_DIR/pdf"

mkdir -p "$PDF_DIR"

build_one() {
  local vol="$1"
  local input="$NOTES_DIR/$vol"
  local basename="${vol%.md}"
  local output="$PDF_DIR/${basename}.pdf"
  echo "Building $vol ..."
  local build_dir="$NOTES_DIR/.pdf-build/$basename"
  local preprocessed
  preprocessed="$(python3 "$ROOT/scripts/preprocess-mermaid.py" "$input" "$build_dir")"
  pandoc "$preprocessed" \
    -o "$output" \
    --resource-path="$build_dir" \
    --from=markdown+tex_math_dollars+tex_math_single_backslash+raw_tex \
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

python3 "$ROOT/scripts/assemble-notes2-volumes.py"

for v in vol-01.md vol-02.md vol-03.md vol-04.md vol-05.md vol-06.md; do
  build_one "$v"
done

echo "All notes-2 PDFs built."
