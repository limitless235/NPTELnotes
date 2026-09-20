#!/usr/bin/env bash
# Build notes-2 volume PDFs (mermaid preprocess + pandoc + XeLaTeX).
# Usage: ./scripts/build-notes2-pdfs.sh [all|csp|genai|infosec]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-all}"

build_one() {
  local notes_dir="$1"
  local vol_md="$2"
  local basename="${vol_md%.md}"
  local input="$notes_dir/$vol_md"
  local output="$notes_dir/pdf/${basename}.pdf"
  local build_dir="$notes_dir/.pdf-build/$basename"
  echo "Building $notes_dir/$vol_md ..."
  mkdir -p "$notes_dir/pdf"
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

if [[ "$TARGET" != "all" && "$TARGET" != "csp" && "$TARGET" != "genai" && "$TARGET" != "infosec" ]]; then
  echo "Usage: $0 [all|csp|genai|infosec]" >&2
  exit 1
fi

if [[ "$TARGET" == "all" || "$TARGET" == "csp" ]]; then
  python3 "$ROOT/scripts/assemble-notes2.py"
  CSP="$ROOT/courses/01-cyber-security-and-privacy/notes-2"
  MIRROR="$ROOT/Cyber Security and Privacy/notes 2"
  mkdir -p "$MIRROR"
  for v in vol-01.md vol-02.md vol-03.md vol-04.md vol-05.md; do
    build_one "$CSP" "$v"
    cp "$CSP/pdf/${v%.md}.pdf" "$MIRROR/${v%.md}.pdf"
  done
fi

if [[ "$TARGET" == "all" || "$TARGET" == "genai" ]]; then
  python3 "$ROOT/scripts/assemble-notes2-volumes.py"
  GENAI="$ROOT/courses/03-generative-ai-llms/notes-2"
  for v in vol-01.md vol-02.md vol-03.md vol-04.md vol-05.md vol-06.md; do
    build_one "$GENAI" "$v"
  done
fi

if [[ "$TARGET" == "all" || "$TARGET" == "infosec" ]]; then
  INFOSEC="$ROOT/courses/05-information-security-cec/notes-2"
  for v in vol-01.md vol-02.md vol-03.md vol-04.md; do
    build_one "$INFOSEC" "$v"
  done
fi

echo "All notes-2 PDFs built."
