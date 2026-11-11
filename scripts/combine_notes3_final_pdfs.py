#!/usr/bin/env python3
"""Combine each course's notes-3 volume PDFs into one subject PDF under final pdf/.

Concatenates pages in volume order; does not drop, rewrite, or recompress content.
"""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "final pdf"

SUBJECTS = [
    (
        "01-cyber-security-and-privacy-notes-3.pdf",
        ROOT / "courses/01-cyber-security-and-privacy/notes-3/pdf",
    ),
    (
        "02-ethical-hacking-notes-3.pdf",
        ROOT / "courses/02-ethical-hacking/notes-3/pdf",
    ),
    (
        "03-generative-ai-llms-notes-3.pdf",
        ROOT / "courses/03-generative-ai-llms/notes-3/pdf",
    ),
    (
        "04-cyber-security-tools-ignou-notes-3.pdf",
        ROOT / "courses/04-cyber-security-tools-ignou/notes-3/pdf",
    ),
    (
        "05-information-security-cec-notes-3.pdf",
        ROOT / "courses/05-information-security-cec/notes-3/pdf",
    ),
]


def combine(pdf_dir: Path, out_path: Path) -> tuple[int, int]:
    vols = sorted(pdf_dir.glob("vol-*.pdf"))
    if not vols:
        raise FileNotFoundError(f"No vol-*.pdf in {pdf_dir}")
    writer = PdfWriter()
    src_pages = 0
    for vol in vols:
        reader = PdfReader(str(vol))
        src_pages += len(reader.pages)
        for page in reader.pages:
            writer.add_page(page)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("wb") as f:
        writer.write(f)
    out_pages = len(PdfReader(str(out_path)).pages)
    if out_pages != src_pages:
        raise RuntimeError(f"{out_path.name}: page mismatch {out_pages} != {src_pages}")
    return len(vols), out_pages


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for out_name, pdf_dir in SUBJECTS:
        n_vols, n_pages = combine(pdf_dir, OUT / out_name)
        size_k = (OUT / out_name).stat().st_size // 1024
        print(f"Wrote final pdf/{out_name} ({n_vols} vols, {n_pages} pages, {size_k}K)")


if __name__ == "__main__":
    main()
