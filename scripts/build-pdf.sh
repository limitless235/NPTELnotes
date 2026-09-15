#!/usr/bin/env bash
# Build PDF from markdown notes for a course volume.
# Usage: ./scripts/build-pdf.sh <course-dir> <volume-md-filename>

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
COURSE_DIR="${1:?Course directory required}"
VOL_MD="${2:?Volume markdown filename required}"

NOTES_DIR="$ROOT/$COURSE_DIR/notes"
PDF_DIR="$ROOT/$COURSE_DIR/pdf"
INPUT="$NOTES_DIR/$VOL_MD"
BASENAME="${VOL_MD%.md}"
OUTPUT="$PDF_DIR/${BASENAME}.pdf"

if [[ ! -f "$INPUT" ]]; then
  echo "Error: $INPUT not found" >&2
  exit 1
fi

mkdir -p "$PDF_DIR"

pandoc "$INPUT" \
  -o "$OUTPUT" \
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

echo "Built: $OUTPUT"
