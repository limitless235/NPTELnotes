#!/usr/bin/env python3
"""Build GenAI exam PDF in final pdf/ keeping only scored weeks.

Drops week 4 (advanced VAEs), week 6 (advanced GANs), week 8 (U-Net /
guided diffusion / Stable Diffusion), and week 12 (multimodal / ethics).
Keeps weeks 1, 2, 3, 5, 7, 9, 10, 11. Week 11 RAG comes from condensed notes/
because notes-2/3 videos stop before a dedicated RAG module.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES3 = ROOT / "courses/03-generative-ai-llms/notes-3"
NOTES = ROOT / "courses/03-generative-ai-llms/notes"
OUT_DIR = ROOT / "final pdf"
MD_OUT = NOTES3 / "exam-syllabus-kept-weeks.md"
PDF_OUT = OUT_DIR / "03-generative-ai-llms-exam-kept-weeks.pdf"

# Official video-lecture week map (notes-2 / notes-3 Lxx ids)
WEEK_LECTURES: dict[int, list[int]] = {
    1: list(range(0, 10)),       # L00–L09 DL foundations (+ intro)
    2: list(range(10, 19)),      # L10–L18 Autoencoders
    3: list(range(19, 25)),      # L19–L24 VAE theory (KL → numerical)
    4: list(range(25, 31)),      # DROP: advanced VAEs + labs
    5: list(range(31, 38)),      # L31–L37 GAN foundations + DCGAN labs
    6: list(range(38, 44)),      # DROP: cGAN / Pix2Pix / CycleGAN / StyleGAN
    7: list(range(44, 49)),      # L44–L48 Diffusion foundations + forward lab
    8: list(range(49, 54)),      # DROP: U-Net, guidance, Stable Diffusion, reverse lab
    9: list(range(54, 59)),      # L54–L58 NLP / RNN / LSTM / encoder / RNN lab
    10: list(range(59, 64)),     # L59–L63 Decoder / BERT / GPT / prompts / LLM lab
}

KEEP_WEEKS = [1, 2, 3, 5, 7, 9, 10]  # week 11 appended separately
DROP_WEEKS = [4, 6, 8, 12]

WEEK_TITLES = {
    1: "Week 1 — Deep-learning foundations for GenAI (5 marks)",
    2: "Week 2 — Autoencoders (5 marks)",
    3: "Week 3 — Variational Autoencoders / KL & ELBO (5 marks)",
    5: "Week 5 — Generative Adversarial Networks foundations (5 marks)",
    7: "Week 7 — Diffusion models foundations (10 marks)",
    9: "Week 9 — NLP, RNNs, LSTMs (5 marks)",
    10: "Week 10 — Transformers, LLMs, prompt engineering (10 marks)",
    11: "Week 11 — Retrieval-Augmented Generation / LoRA (5 marks)",
}


def split_notes3_lectures() -> dict[int, str]:
    """Map lecture number → markdown body (without leading ## line duplication)."""
    out: dict[int, str] = {}
    for path in sorted(NOTES3.glob("vol-*.md")):
        text = path.read_text(encoding="utf-8")
        parts = re.split(r"(?m)^(?=## L\d+:)", text)
        for part in parts:
            m = re.match(r"## L(\d+):", part)
            if not m:
                continue
            n = int(m.group(1))
            body = part.strip()
            # drop trailing --- separators
            body = re.sub(r"\n---\s*$", "", body).strip()
            out[n] = body + "\n"
    return out


def week11_from_condensed() -> str:
    """Concept-style Week 11 from condensed notes vol-04 (L31–L33 only)."""
    text = (NOTES / "vol-04.md").read_text(encoding="utf-8")
    chunks = []
    for lid, title in [
        (31, "Retrieval-Augmented Generation Architecture"),
        (32, "Vector Databases and Document Chunking"),
        (33, "Fine-Tuning with LoRA and Parameter-Efficient Methods"),
    ]:
        pat = rf"(?ms)^## L{lid}:.*?(?=^## L\d+:|\Z)"
        m = re.search(pat, text)
        if not m:
            raise SystemExit(f"Missing condensed L{lid}")
        block = m.group(0)
        # strip mermaid diagrams for smaller PDF
        block = re.sub(r"```mermaid.*?```", "", block, flags=re.S)
        chunks.append(block.strip())
    return "\n\n---\n\n".join(chunks) + "\n"


def build_markdown(lectures: dict[int, str]) -> str:
    parts = [
        "# Generative AI & LLMs — Exam syllabus notes (kept weeks only)",
        "",
        "> NPTEL `noc26_cs95` · notes-3 concept packs, filtered to the exam mark map.",
        ">",
        "> **Kept:** Weeks 1, 2, 3, 5, 7, 9, 10, 11.",
        "> **Dropped (not in this PDF):** Weeks **4, 6, 8, 12**.",
        "",
        "## Exam mark map (as given)",
        "",
        "| Week | Marks | Theme |",
        "|------|------:|-------|",
        "| 1 | 5 | Deep-learning foundations for GenAI |",
        "| 2 | 5 | Autoencoders |",
        "| 3 | 5 | VAEs (KL, reparameterization, ELBO) |",
        "| 5 | 5 | GAN foundations + DCGAN |",
        "| 7 | 10 | Diffusion foundations (forward/reverse DDPM) |",
        "| 9 | 5 | NLP, RNN, LSTM |",
        "| 10 | 10 | Transformers, BERT/GPT, prompting |",
        "| 11 | 5 | RAG + LoRA / PEFT |",
        "",
        "## Dropped weeks (study only if needed — excluded here)",
        "",
        "| Week | Why dropped | Topics removed |",
        "|------|-------------|----------------|",
        "| **4** | Not in exam map | β-VAE, CVAE, latent interpolation, VAE/CVAE/β-VAE labs (video L25–L30) |",
        "| **6** | Not in exam map | cGAN, Pix2Pix, CycleGAN, StyleGAN/StyleGAN2, advanced GAN lab (L38–L43) |",
        "| **8** | Not in exam map | U-Net for DDPM, classifier / classifier-free guidance, Stable Diffusion, reverse-diffusion lab (L49–L53) |",
        "| **12** | Not in exam map | Multimodal VLMs, hallucinations/safety eval, bias/fairness/ethics |",
        "",
        "---",
        "",
    ]

    for week in KEEP_WEEKS:
        parts.append(f"# {WEEK_TITLES[week]}")
        parts.append("")
        for n in WEEK_LECTURES[week]:
            if n not in lectures:
                raise SystemExit(f"Missing notes-3 lecture L{n:02d} for week {week}")
            parts.append(lectures[n])
            parts.append("\n---\n")

    parts.append(f"# {WEEK_TITLES[11]}")
    parts.append("")
    parts.append(
        "_Week 11 is not a dedicated notes-2 video module in L00–L63; "
        "this section is the condensed syllabus notes for RAG / vector DBs / LoRA._"
    )
    parts.append("")
    parts.append(week11_from_condensed())
    text = "\n".join(parts).rstrip() + "\n"
    return text.replace("✓", "Yes").replace("✗", "No")


def build_pdf(md_path: Path, pdf_path: Path) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "pandoc",
            str(md_path),
            "-o",
            str(pdf_path),
            "--from=markdown+tex_math_dollars+tex_math_single_backslash",
            "--pdf-engine=xelatex",
            "-V",
            "geometry:margin=0.9in",
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
    lectures = split_notes3_lectures()
    md = build_markdown(lectures)
    MD_OUT.write_text(md, encoding="utf-8")
    print(f"Wrote {MD_OUT.relative_to(ROOT)} ({len(md.split())} words)")
    build_pdf(MD_OUT, PDF_OUT)
    pages = len(__import__("pypdf").PdfReader(str(PDF_OUT)).pages)
    print(f"Wrote {PDF_OUT.relative_to(ROOT)} ({pages} pages, {PDF_OUT.stat().st_size // 1024}K)")


if __name__ == "__main__":
    main()
