#!/usr/bin/env python3
"""Assemble Info Sec notes-exam volumes into one PDF under final pdf/."""

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "courses/05-information-security-cec/notes-exam"
OUT_MD = SRC / "exam-readable-combined.md"
OUT_PDF = ROOT / "final pdf" / "05-information-security-cec-exam-readable.pdf"
VOLS = ["vol-01.md", "vol-02.md", "vol-03.md", "vol-04.md"]


def assemble() -> Path:
    parts = [
        "# Information Security (CEC) — Exam-readable notes\n",
        "\n",
        "> Full concept coverage rewritten for understanding and answer writing.\n",
        "> Clearer than transcript notes-2; denser than ultra-short notes-3.\n",
        ">\n",
        "> Companion calculations: `final pdf/05-information-security-cec-numericals.pdf`\n",
        "\n",
        "## How to use in exams\n",
        "\n",
        "1. Read **In one line** to orient.\n",
        "2. Memorize **Definitions** tables — these are write-ready.\n",
        "3. Use **Concepts explained** for 5–10 mark explanations.\n",
        "4. Expand **How to answer** bullets into paragraphs on the sheet.\n",
        "\n",
        "---\n",
        "\n",
    ]
    for name in VOLS:
        body = (SRC / name).read_text(encoding="utf-8").strip() + "\n"
        # Drop duplicate top-level title noise when combining: keep volume H1 as H1
        parts.append(body)
        parts.append("\n\\newpage\n\n")
    OUT_MD.write_text("".join(parts), encoding="utf-8")
    return OUT_MD


def build_pdf(md: Path) -> None:
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "pandoc",
            str(md),
            "-o",
            str(OUT_PDF),
            "--from=markdown+tex_math_dollars+tex_math_single_backslash",
            "--pdf-engine=xelatex",
            "-V",
            "geometry:margin=0.85in",
            "-V",
            "fontsize=11pt",
            "-V",
            "documentclass=article",
            "-V",
            "mainfont=DejaVu Serif",
            "-V",
            "monofont=DejaVu Sans Mono",
            "--toc",
            "--toc-depth=2",
            "-V",
            "colorlinks=true",
            "-V",
            "linkcolor=blue",
        ],
        check=True,
    )


def main() -> None:
    md = assemble()
    print(f"Wrote {md.relative_to(ROOT)} ({len(md.read_text().split())} words)")
    build_pdf(md)
    from pypdf import PdfReader

    pages = len(PdfReader(str(OUT_PDF)).pages)
    print(f"Wrote {OUT_PDF.relative_to(ROOT)} ({pages} pages, {OUT_PDF.stat().st_size // 1024}K)")


if __name__ == "__main__":
    main()
