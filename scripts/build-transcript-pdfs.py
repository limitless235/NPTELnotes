#!/usr/bin/env python3
"""Build per-video transcript markdown + PDFs from scraped YouTube captions."""

from __future__ import annotations

import re
from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = Path("/tmp/transcripts/raw")
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

# Playlist PLyqSpQzTE6M-jkJEzbS5oHJUp2GWPsq6e (NPTEL Cyber Security and Privacy)
VIDEOS = [
    (1, "OYsY5B9pqYU", "Introduction — Course Welcome"),
    (3, "nadHKp3egDY", "Introduction — Part 02"),
    (4, "ZmCtYgj9kSo", "Introduction — Part 03"),
    (5, "WAImfXGwhOs", "Foundations — Part 01"),
    (6, "9oQb5DIuNKg", "Foundations — Part 02"),
    (7, "QDzGq_taOLM", "Foundations — Part 03"),
    (8, "1okOQCY6Bsk", "Security Management and GRC — Part 01"),
    (9, "YE0PooziW-0", "Security Management and GRC — Part 02"),
    (10, "1sN6NtaRoHE", "Security Management and GRC — Part 03"),
    (11, "j0QxAhDh48E", "Contingency Planning — Part 01"),
    (12, "IEHL64fnd6A", "Contingency Planning — Part 03"),
    (13, "bpxDDAT7yE0", "Contingency Planning — Part 02"),
    (14, "ozsxJCM4BGs", "Cybersecurity and Privacy — Supplementary Lecture"),
    (15, "8nEpUXaiZns", "Cybersecurity Policy — Part 01"),
    (16, "snROvNy3wf8", "Cybersecurity Policy — Part 02"),
    (17, "MZlDHGdqm3w", "Cybersecurity Policy — Part 03"),
    (18, "kZtw4L6LZS8", "Cybersecurity and Privacy — Extended Discussion"),
    (19, "v7KtPLhSMkU", "Risk Management — Part 01"),
    (20, "WtbyE4GE7Zc", "Risk Management — Part 02"),
    (21, "2TsAnaO75ck", "Risk Management — Part 03"),
    (22, "F5KwJEVGIxg", "Industry Perspective — Part 01"),
    (23, "ROHhs7PMIGw", "Industry Perspective — Part 02"),
    (24, "JPQiuqw6fvw", "Industry Perspective — Part 03"),
    (25, "3rkIe2ZkkfY", "Cybersecurity Technologies — Part 01"),
    (26, "ZQSXMurVEXA", "Cybersecurity Technologies — Part 02"),
    (27, "7-nnLNGBtLM", "Foundations of Privacy — Part 01"),
    (28, "TOki4KHyVWg", "Foundations of Privacy — Part 02"),
    (29, "s2vt-xAbgUk", "Foundations of Privacy — Part 03"),
    (30, "g_G2bFrkeHY", "Privacy Regulation — Part 01"),
    (31, "nBr733H_xH4", "Privacy Regulation — Part 02"),
    (32, "IKPp1yc0dnk", "Privacy Regulation — Part 03"),
    (33, "gt8j3cUCL-I", "Privacy Regulation in Europe — Part 02"),
    (34, "TSx88vrSfG0", "Privacy Regulation in Europe — Part 03"),
    (35, "fobfwNopJtc", "Privacy: The Indian Way — Part 01"),
    (36, "oIUjD7JmDoU", "Privacy: The Indian Way — Part 02"),
    (37, "8MDW4UP7Quc", "Privacy: The Indian Way — Part 03"),
    (38, "qtTFHNVUDBg", "Privacy Regulation in Europe — Part 01"),
    (39, "qXHNviJSQD8", "Information Privacy: Economics and Strategy — Part 01"),
    (40, "LwARGPiu2oc", "Information Privacy: Economics and Strategy — Part 02"),
    (41, "EjOF_cVzvNE", "Information Privacy: Economics and Strategy — Part 03"),
    (42, "All1JR-Avjw", "Privacy: Strategy and Safety — Part 01"),
    (43, "MlYAd9Ip6Nw", "Privacy: Strategy and Safety — Part 02"),
    (44, "y93i1XbphTM", "Privacy: Strategy and Safety — Part 03"),
    (45, "HXt6GvYxSqQ", "Cyber Security and Privacy — Capstone Discussion A"),
    (46, "nlsz8MggiAU", "Cyber Security and Privacy — Capstone Discussion B"),
    (48, "rMXMwrPaF0I", "Introduction — Part 01"),
]

UNAVAILABLE = [
    (2, "2d5fKqo6zDc", "Introduction — Part 01 (region-unavailable on YouTube)"),
    (47, "Ir7JJgyKqME", "Untitled playlist entry (unavailable)"),
]

COURSE = "Cyber Security and Privacy"
INSTRUCTOR = "Prof. Saji K. Mathew, IIT Madras"
COURSE_ID = "NPTEL 106106248"
PLAYLIST = "https://www.youtube.com/playlist?list=PLyqSpQzTE6M-jkJEzbS5oHJUp2GWPsq6e"


def slug(title: str) -> str:
    s = title.lower()
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:80]


def clean_transcript(raw: str) -> str:
    text = raw.replace("\ufeff", "")
    text = re.sub(r"^# Content from .+\n+", "", text)
    text = re.sub(r"\[(?:music|applause|laughter)\]", "", text, flags=re.I)
    lines = [ln.strip() for ln in text.splitlines()]
    lines = [ln for ln in lines if ln and not ln.startswith("Content written to file:")]

    # Caption dumps often wrap mid-sentence. Join until terminal punctuation.
    chunks: list[str] = []
    buf: list[str] = []
    terminal = re.compile(r"""[.?!]["')\]]*$""")
    for ln in lines:
        buf.append(ln)
        if terminal.search(ln) or ln.endswith(":"):
            chunks.append(" ".join(buf))
            buf = []
    if buf:
        chunks.append(" ".join(buf))

    merged = " ".join(chunks)
    merged = re.sub(r"[ \t]+", " ", merged)
    merged = re.sub(r"\s+([,.;:?!])", r"\1", merged)
    merged = re.sub(r"\b(um|uh|Uh|Um)\b[,.]?", "", merged)
    merged = re.sub(r" {2,}", " ", merged).strip()

    # Split into readable paragraphs of ~4 sentences.
    sentences = re.split(r"(?<=[.?!])\s+", merged)
    paragraphs: list[str] = []
    group: list[str] = []
    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue
        group.append(sent)
        if len(group) >= 4:
            paragraphs.append(" ".join(group))
            group = []
    if group:
        paragraphs.append(" ".join(group))
    return "\n\n".join(paragraphs)


def markdown_for(index: int, video_id: str, title: str, body: str) -> str:
    url = f"https://www.youtube.com/watch?v={video_id}"
    return (
        f"# Lecture {index:02d}: {title}\n\n"
        f"**Course:** {COURSE} ({COURSE_ID})  \n"
        f"**Instructor:** {INSTRUCTOR}  \n"
        f"**Video:** [{video_id}]({url})  \n"
        f"**Playlist:** [Cybersecurity and Privacy]({PLAYLIST})\n\n"
        "> Study transcript prepared from publicly available YouTube captions.  \n"
        "> Lecture rights belong to NPTEL / IIT Madras. For personal study only.\n\n"
        "---\n\n"
        f"{body}\n"
    )


class TranscriptPDF(FPDF):
    def __init__(self, heading: str):
        super().__init__(format="A4")
        self.heading = heading
        self.set_auto_page_break(auto=True, margin=18)
        self.add_font("DejaVu", "", str(FONT_DIR / "DejaVuSerif.ttf"))
        self.add_font("DejaVu", "B", str(FONT_DIR / "DejaVuSerif-Bold.ttf"))
        self.add_font("DejaVuSans", "", str(FONT_DIR / "DejaVuSans.ttf"))

    def header(self) -> None:
        if self.page_no() == 1:
            return
        self.set_font("DejaVuSans", "", 8)
        self.set_text_color(90, 90, 90)
        self.cell(0, 8, self.heading, align="L")
        self.ln(10)
        self.set_text_color(0, 0, 0)

    def footer(self) -> None:
        self.set_y(-12)
        self.set_font("DejaVuSans", "", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Page {self.page_no()}  ·  Personal study transcript  ·  {COURSE_ID}", align="C")


def write_pdf(path: Path, index: int, video_id: str, title: str, body: str) -> None:
    url = f"https://www.youtube.com/watch?v={video_id}"
    heading = f"{COURSE}  ·  Lecture {index:02d}"
    pdf = TranscriptPDF(heading)
    pdf.add_page()
    usable = pdf.w - pdf.l_margin - pdf.r_margin

    def block(text: str, h: float) -> None:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(usable, h, text)

    pdf.set_font("DejaVu", "B", 16)
    block(f"Lecture {index:02d}", 8)
    pdf.set_font("DejaVu", "B", 14)
    block(title.replace("—", "-"), 8)
    pdf.ln(2)
    pdf.set_font("DejaVuSans", "", 10)
    pdf.set_text_color(40, 40, 40)
    meta = (
        f"{COURSE}  |  {COURSE_ID}\n"
        f"{INSTRUCTOR}\n"
        f"Video: {url}"
    )
    block(meta, 5)
    pdf.ln(2)
    pdf.set_font("DejaVuSans", "", 9)
    pdf.set_text_color(90, 90, 90)
    block(
        "Study transcript from publicly available YouTube captions. "
        "Course content and video rights belong to NPTEL / IIT Madras. For personal study only.",
        5,
    )
    pdf.set_text_color(0, 0, 0)
    pdf.ln(4)
    pdf.set_draw_color(180, 180, 180)
    y = pdf.get_y()
    pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
    pdf.ln(6)
    pdf.set_font("DejaVu", "", 11)
    for para in body.split("\n\n"):
        block(para.replace("—", "-").replace("–", "-"), 6)
        pdf.ln(2)
    path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(path))


def main() -> None:
    out_root = ROOT / "courses" / "01-cyber-security-and-privacy" / "transcripts"
    md_dir = out_root / "markdown"
    pdf_dir = out_root / "pdf"
    md_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir.mkdir(parents=True, exist_ok=True)

    built = []
    missing = []
    for index, video_id, title in VIDEOS:
        raw_path = RAW_DIR / f"{video_id}.txt"
        if not raw_path.exists():
            missing.append((index, video_id, title))
            continue
        body = clean_transcript(raw_path.read_text(encoding="utf-8", errors="replace"))
        if len(body) < 200:
            missing.append((index, video_id, title))
            continue
        stem = f"{index:02d}-{slug(title)}"
        md_path = md_dir / f"{stem}.md"
        pdf_path = pdf_dir / f"{stem}.pdf"
        md_path.write_text(markdown_for(index, video_id, title, body), encoding="utf-8")
        write_pdf(pdf_path, index, video_id, title, body)
        built.append((index, title, md_path.name, pdf_path.name, video_id))
        print(f"built {stem} ({len(body)} chars)")

    index_lines = [
        f"# Per-video transcripts — {COURSE}",
        "",
        f"**Course:** {COURSE_ID}  ",
        f"**Instructor:** {INSTRUCTOR}  ",
        f"**Playlist:** {PLAYLIST}",
        "",
        "One cleaned study transcript (markdown + PDF) per available YouTube lecture. "
        "Captions were scraped from the public NPTEL playlist and lightly cleaned "
        "(line-wrap repair, filler-word reduction). These are **not** official NPTEL transcripts.",
        "",
        "## Disclaimer",
        "",
        "Lecture content and video rights belong to NPTEL, IIT Madras, and Prof. Saji K. Mathew. "
        "Files here are for **personal study**. Do not treat them as a substitute for the official videos.",
        "",
        "## Lectures",
        "",
        "| # | Title | Markdown | PDF | YouTube |",
        "|---|-------|----------|-----|---------|",
    ]
    for index, title, md_name, pdf_name, video_id in built:
        url = f"https://www.youtube.com/watch?v={video_id}"
        index_lines.append(
            f"| {index:02d} | {title} | [{md_name}](markdown/{md_name}) | [{pdf_name}](pdf/{pdf_name}) | [{video_id}]({url}) |"
        )
    index_lines += [
        "",
        "## Unavailable playlist entries",
        "",
        "YouTube hid 2 playlist items at scrape time:",
        "",
        "| # | ID | Note |",
        "|---|----|------|",
    ]
    for index, video_id, note in UNAVAILABLE:
        index_lines.append(f"| {index:02d} | `{video_id}` | {note} |")
    if missing:
        index_lines += ["", "## Missing after scrape", ""]
        for index, video_id, title in missing:
            index_lines.append(f"- Lecture {index:02d} `{video_id}` — {title}")
    index_lines += [
        "",
        "## Rebuild",
        "",
        "```bash",
        "python3 scripts/build-transcript-pdfs.py",
        "```",
        "",
        "Requires scraped caption files in `/tmp/transcripts/raw/<video-id>.txt` and the `fpdf2` package.",
        "",
    ]
    (out_root / "README.md").write_text("\n".join(index_lines), encoding="utf-8")
    print(f"done: {len(built)} transcripts, {len(missing)} missing")


if __name__ == "__main__":
    main()
