#!/usr/bin/env bash
# Build notes-3 volume PDFs (pandoc + XeLaTeX). No mermaid preprocess — concept notes are text/tables.
# Usage: ./scripts/build-notes3-pdfs.sh [all|csp|ethical-hacking|genai|infosec|ignou]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-all}"

build_one() {
  local notes_dir="$1"
  local vol_md="$2"
  local basename="${vol_md%.md}"
  local input="$notes_dir/$vol_md"
  local output="$notes_dir/pdf/${basename}.pdf"
  [[ -f "$input" ]] || { echo "Missing $input" >&2; return 1; }
  mkdir -p "$notes_dir/pdf"
  echo "Building $notes_dir/$vol_md ..."
  pandoc "$input" \
    -o "$output" \
    --from=markdown+tex_math_dollars+tex_math_single_backslash \
    --pdf-engine=xelatex \
    -V geometry:margin=0.9in \
    -V fontsize=11pt \
    -V documentclass=article \
    -V mainfont="DejaVu Serif" \
    -V monofont="DejaVu Sans Mono" \
    --toc \
    --toc-depth=2 \
    -V colorlinks=true \
    -V linkcolor=blue
  echo "Built: $output ($(du -h "$output" | cut -f1))"
}

if [[ "$TARGET" != "all" && "$TARGET" != "csp" && "$TARGET" != "genai" && "$TARGET" != "infosec" && "$TARGET" != "ethical-hacking" && "$TARGET" != "ignou" ]]; then
  echo "Usage: $0 [all|csp|genai|infosec|ethical-hacking|ignou]" >&2
  exit 1
fi

if [[ "$TARGET" == "all" || "$TARGET" == "ethical-hacking" ]]; then
  EH="$ROOT/courses/02-ethical-hacking/notes-3"
  for v in vol-01.md vol-02.md vol-03.md vol-04.md vol-05.md vol-06.md; do
    build_one "$EH" "$v"
  done
fi

if [[ "$TARGET" == "all" || "$TARGET" == "csp" ]]; then
  CSP="$ROOT/courses/01-cyber-security-and-privacy/notes-3"
  MIRROR="$ROOT/Cyber Security and Privacy/notes 3"
  mkdir -p "$MIRROR"
  for v in vol-01.md vol-02.md vol-03.md vol-04.md vol-05.md; do
    build_one "$CSP" "$v"
    cp "$CSP/pdf/${v%.md}.pdf" "$MIRROR/${v%.md}.pdf"
  done
fi

if [[ "$TARGET" == "all" || "$TARGET" == "genai" ]]; then
  GENAI="$ROOT/courses/03-generative-ai-llms/notes-3"
  for v in vol-01.md vol-02.md vol-03.md vol-04.md vol-05.md vol-06.md; do
    build_one "$GENAI" "$v"
  done
fi

if [[ "$TARGET" == "all" || "$TARGET" == "infosec" ]]; then
  INFOSEC="$ROOT/courses/05-information-security-cec/notes-3"
  for v in vol-01.md vol-02.md vol-03.md vol-04.md; do
    build_one "$INFOSEC" "$v"
  done
fi

if [[ "$TARGET" == "all" || "$TARGET" == "ignou" ]]; then
  IGNOU="$ROOT/courses/04-cyber-security-tools-ignou/notes-3"
  for v in vol-01.md vol-02.md vol-03.md vol-04.md; do
    build_one "$IGNOU" "$v"
  done
fi

echo "All requested notes-3 PDFs built."
