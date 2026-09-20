#!/usr/bin/env python3
"""Concatenate notes-2 lecture files into printable volume markdown."""
from __future__ import annotations

from pathlib import Path

NOTES = Path(__file__).resolve().parents[1] / "courses/03-generative-ai-llms/notes-2"

VOLUMES = [
    {
        "file": "vol-01.md",
        "title": "Volume 01 — Deep Learning Foundations for Generative AI",
        "span": "Intro + Lec 01–09",
        "start": 0,
        "end": 9,
    },
    {
        "file": "vol-02.md",
        "title": "Volume 02 — Autoencoders",
        "span": "Lec 10–18",
        "start": 10,
        "end": 18,
    },
    {
        "file": "vol-03.md",
        "title": "Volume 03 — KL Divergence and Variational Autoencoders",
        "span": "Lec 19–30",
        "start": 19,
        "end": 30,
    },
    {
        "file": "vol-04.md",
        "title": "Volume 04 — Generative Adversarial Networks",
        "span": "Lec 31–43",
        "start": 31,
        "end": 43,
    },
    {
        "file": "vol-05.md",
        "title": "Volume 05 — Diffusion Models",
        "span": "Lec 44–53",
        "start": 44,
        "end": 53,
    },
    {
        "file": "vol-06.md",
        "title": "Volume 06 — NLP, Transformers, and LLMs",
        "span": "Lec 54–63",
        "start": 54,
        "end": 63,
    },
]


def lecture_files() -> list[Path]:
    files = [p for p in NOTES.glob("L*.md") if p.name[1:3].isdigit()]
    files.sort(key=lambda p: int(p.name[1:3]))
    return files


def assemble(vol: dict, lectures: list[Path]) -> None:
    chunk = [p for p in lectures if vol["start"] <= int(p.name[1:3]) <= vol["end"]]
    parts = [
        f"# {vol['title']}\n",
        f"**{vol['span']}** · Transcript-grounded notes (notes-2)\n",
        "These notes follow the official NPTEL lecture videos. "
        "They are not the condensed 36-lecture mapping in `notes/`.\n",
        "---\n",
    ]
    index_rows = [
        f"# {vol['title'].replace('Volume', 'Volume')} Index\n",
        f"**{vol['span']}** · [Full notes]({vol['file']})\n",
        "| # | Lecture | File |",
        "|---|---------|------|",
    ]
    for p in chunk:
        body = p.read_text(encoding="utf-8").strip() + "\n"
        parts.append(body)
        parts.append("\n\\newpage\n")
        title = body.splitlines()[0].lstrip("# ").strip()
        num = p.name[1:3]
        index_rows.append(f"| {num} | {title} | [{p.name}]({p.name}) |")
    out = NOTES / vol["file"]
    out.write_text("\n".join(parts), encoding="utf-8")
    index_name = vol["file"].replace(".md", ".index.md")
    (NOTES / index_name).write_text("\n".join(index_rows) + "\n", encoding="utf-8")
    print(f"wrote {out.name} ({len(chunk)} lectures, {out.stat().st_size} bytes)")


def main() -> None:
    lectures = lecture_files()
    if len(lectures) != 64:
        raise SystemExit(f"expected 64 lecture files, found {len(lectures)}")
    for vol in VOLUMES:
        assemble(vol, lectures)


if __name__ == "__main__":
    main()
