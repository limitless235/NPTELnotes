#!/usr/bin/env python3
"""Scrape YouTube transcripts for the CEC Information Security playlist and emit markdown + PDFs."""

from __future__ import annotations

import json
import re
import time
from pathlib import Path

from fpdf import FPDF
from playwright.sync_api import sync_playwright

PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLcWnLUJA-zgdEW1tOYLs7xsZ0lP8gx-6b"
ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "courses" / "05-information-security-cec"
OUT_MD = COURSE / "transcripts"
OUT_PDF = COURSE / "transcripts" / "pdf"
META_PATH = COURSE / "transcripts" / "playlist-metadata.json"

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
TS_RE = re.compile(r"^(?:(\d+):)?(\d{1,2}):(\d{2})$")
DUR_RE = re.compile(
    r"^(\d+\s+seconds|\d+\s+minutes?(?:,\s*\d+\s+seconds)?|\d+\s+hour(?:s)?(?:,\s*\d+\s+minutes?)?(?:,\s*\d+\s+seconds)?)$",
    re.I,
)
MODULE_NO_RE = re.compile(r"Module No\s*-\s*(\d+)", re.I)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[–—]", "-", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60] or "lecture"


def parse_module_name(description: str | None, title: str) -> str:
    if description:
        for line in description.splitlines():
            if line.lower().startswith("module name"):
                name = line.split("-", 1)[-1].strip(" -")
                if name:
                    return name
    if title.lower().startswith("introductory"):
        return "Introductory Video"
    return title


def parse_cues(raw: str) -> list[tuple[str, str]]:
    lines = [ln.strip() for ln in raw.splitlines()]
    i = 0
    while i < len(lines) and lines[i].lower() != "search transcript":
        i += 1
    if i < len(lines) and lines[i].lower() == "search transcript":
        i += 1
    cues: list[tuple[str, str]] = []
    while i < len(lines):
        if TS_RE.match(lines[i]):
            ts = lines[i]
            i += 1
            if i < len(lines) and DUR_RE.match(lines[i]):
                i += 1
            parts: list[str] = []
            while i < len(lines) and not TS_RE.match(lines[i]) and not DUR_RE.match(lines[i]):
                if lines[i]:
                    parts.append(lines[i])
                i += 1
            text = " ".join(parts).strip()
            text = re.sub(r"\s+", " ", text)
            if re.search(r"\b\d+(?:\.\d+)?[KMB]\s+\d+\w+\s+ago\b", text, re.I):
                break
            if text:
                cues.append((ts, text))
        else:
            i += 1
    return cues


def pdf_safe(text: str) -> str:
    text = "".join(ch if (ch == "\n" or (ch.isprintable() and ord(ch) < 0x3000)) else " " for ch in text)
    return re.sub(r"\s+", " ", text).strip()


def cues_to_paragraphs(cues: list[tuple[str, str]], target: int = 520) -> list[str]:
    """Join timestamped cues into readable paragraphs with no timestamps."""
    paras: list[str] = []
    cur: list[str] = []
    cur_len = 0
    for _ts, text in cues:
        t = pdf_safe(text)
        if not t or DUR_RE.match(t) or len(t) <= 1:
            continue
        if re.fullmatch(r"\[(?:music|applause|silence|inaudible)\]", t, re.I):
            if cur:
                paras.append(" ".join(cur))
                cur, cur_len = [], 0
            continue
        cur.append(t)
        cur_len += len(t) + 1
        ends_sentence = t[-1] in ".?!"
        if cur_len >= target and (ends_sentence or cur_len >= target + 180):
            paras.append(" ".join(cur))
            cur, cur_len = [], 0
    if cur:
        paras.append(" ".join(cur))
    return paras


def format_duration(seconds: int) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def scrape_one(page, video_id: str) -> str:
    page.goto(f"https://www.youtube.com/watch?v={video_id}", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    try:
        page.locator("#description-inline-expander").first.click(timeout=4000)
        page.wait_for_timeout(800)
    except Exception:
        pass
    for sel in (
        "ytd-video-description-transcript-section-renderer button",
        "button[aria-label='Show transcript']",
    ):
        loc = page.locator(sel)
        if loc.count():
            try:
                loc.last.evaluate("el => el.click()")
                break
            except Exception:
                continue
    raw = ""
    for _ in range(12):
        page.wait_for_timeout(1000)
        raw = page.evaluate(
            """() => {
              const panel = document.querySelector(
                'ytd-engagement-panel-section-list-renderer #content'
              );
              return panel ? panel.innerText : '';
            }"""
        ) or ""
        if "Search transcript" in raw and len(raw) > 400:
            break
    if "Search transcript" not in raw:
        body = page.inner_text("body")
        idx = body.find("Search transcript")
        if idx >= 0:
            raw = body[idx:]
    return raw


class TranscriptPDF(FPDF):
    def __init__(self, header_title: str):
        super().__init__(format="A4")
        self.header_title = header_title
        self.set_auto_page_break(auto=True, margin=18)
        self.add_font("DejaVu", "", str(FONT_DIR / "DejaVuSerif.ttf"))
        self.add_font("DejaVu", "B", str(FONT_DIR / "DejaVuSerif-Bold.ttf"))
        self.add_font("DejaVuSans", "", str(FONT_DIR / "DejaVuSans.ttf"))

    def header(self):
        self.set_font("DejaVuSans", "", 8)
        self.set_text_color(90, 90, 90)
        self.set_x(self.l_margin)
        self.cell(150, 8, self.header_title, align="L")
        self.cell(0, 8, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(200, 200, 200)
        self.line(self.l_margin, 12, 210 - self.r_margin, 12)
        self.ln(4)
        self.set_x(self.l_margin)

    def footer(self):
        self.set_y(-12)
        self.set_font("DejaVuSans", "", 7)
        self.set_text_color(120, 120, 120)
        self.cell(
            0,
            8,
            "Personal study transcript. Video rights remain with CEC / SWAYAM / the instructors.",
            align="C",
        )


def write_pdf(path: Path, meta: dict, cues: list[tuple[str, str]]) -> None:
    title = meta["module_name"]
    pdf = TranscriptPDF(f"Information Security  ·  {meta['label']}")
    pdf.add_page()
    pdf.set_text_color(20, 20, 20)
    pdf.set_font("DejaVu", "B", 16)
    pdf.multi_cell(0, 9, title)
    pdf.ln(1)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("DejaVuSans", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 6, meta["label"])
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, 6, f"Duration: {format_duration(meta['duration'])}")
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, 6, f"Video: {meta['url']}")
    if meta.get("expert"):
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, 6, meta["expert"])
    pdf.ln(2)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("DejaVuSans", "", 8)
    pdf.set_text_color(90, 90, 90)
    pdf.multi_cell(
        0,
        5,
        "Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture. "
        "Follow the video link above; this file is not an official CEC/SWAYAM publication.",
    )
    pdf.ln(3)
    pdf.set_draw_color(180, 180, 180)
    pdf.line(12, pdf.get_y(), 198, pdf.get_y())
    pdf.ln(4)

    paragraphs = cues_to_paragraphs(cues)
    if not paragraphs:
        pdf.set_font("DejaVu", "", 11)
        pdf.set_text_color(150, 0, 0)
        pdf.multi_cell(0, 7, "Transcript could not be retrieved for this video.")
    else:
        pdf.set_font("DejaVu", "", 11)
        pdf.set_text_color(25, 25, 25)
        for para in paragraphs:
            if pdf.get_y() > 262:
                pdf.add_page()
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(0, 6.4, para, align="J")
            pdf.ln(3.2)

    pdf.output(str(path))


def write_markdown(path: Path, meta: dict, cues: list[tuple[str, str]]) -> None:
    lines = [
        f"# {meta['module_name']}",
        "",
        f"**{meta['label']}**  ",
        f"Duration: {format_duration(meta['duration'])}  ",
        f"Video: {meta['url']}",
        "",
    ]
    if meta.get("expert"):
        lines += [meta["expert"], ""]
    lines += [
        "> Auto-generated YouTube transcript for personal study. "
        "Spoken wording belongs to the original lecture (CEC / SWAYAM).",
        "",
        "---",
        "",
    ]
    if not cues:
        lines.append("_Transcript could not be retrieved for this video._")
    else:
        for ts, text in cues:
            lines.append(f"**[{ts}]** {text}")
            lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def enrich(item: dict) -> dict:
    title = item.get("title") or ""
    desc = item.get("description") or ""
    m = MODULE_NO_RE.search(title)
    if m:
        num = int(m.group(1))
        label = f"Module {num:02d}"
        stem_num = f"{num:02d}"
    else:
        num = 0
        label = "Introductory Video"
        stem_num = "00"
    module_name = parse_module_name(desc, title)
    expert = ""
    coordinator = ""
    for line in desc.splitlines():
        low = line.lower()
        if low.startswith("subject expert"):
            expert = line.strip()
        elif low.startswith("course coordinator"):
            coordinator = line.strip()
    extra = "  \n".join(x for x in (coordinator, expert) if x)
    return {
        **item,
        "module_num": num,
        "label": label,
        "module_name": module_name,
        "expert": extra,
        "stem": f"M{stem_num}-{slugify(module_name)}",
    }


def main() -> None:
    items = json.loads(META_PATH.read_text()) if META_PATH.exists() else json.loads(
        Path("/tmp/playlist-meta.json").read_text()
    )
    OUT_MD.mkdir(parents=True, exist_ok=True)
    OUT_PDF.mkdir(parents=True, exist_ok=True)

    records = [enrich(it) for it in items]
    records.sort(key=lambda r: r["module_num"])

    META_PATH.parent.mkdir(parents=True, exist_ok=True)
    META_PATH.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    failures: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox", "--disable-dev-shm-usage"],
        )
        context = browser.new_context(
            locale="en-US",
            viewport={"width": 1280, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            ),
        )
        page = context.new_page()
        for i, rec in enumerate(records, 1):
            md_path = OUT_MD / f"{rec['stem']}.md"
            pdf_path = OUT_PDF / f"{rec['stem']}.pdf"
            print(f"[{i}/{len(records)}] {rec['stem']} ({rec['id']})", flush=True)
            cues: list[tuple[str, str]] = []
            try:
                raw = scrape_one(page, rec["id"])
                cues = parse_cues(raw)
                if len(cues) < 3:
                    time.sleep(2)
                    raw = scrape_one(page, rec["id"])
                    cues = parse_cues(raw)
                rec["cue_count"] = len(cues)
                rec["char_count"] = sum(len(t) for _, t in cues)
                print(f"    cues={len(cues)} chars={rec['char_count']}", flush=True)
                if len(cues) < 3:
                    failures.append(rec["stem"])
            except Exception as exc:
                print(f"    ERROR {exc}", flush=True)
                failures.append(rec["stem"])
            write_markdown(md_path, rec, cues)
            write_pdf(pdf_path, rec, cues)
            time.sleep(1.2)
        browser.close()

    META_PATH.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("failures", failures)
    print("done", len(records))


CUE_MD_RE = re.compile(r"^\*\*\[(.+?)\]\*\*\s*(.*)$")


def parse_markdown_cues(path: Path) -> list[tuple[str, str]]:
    cues: list[tuple[str, str]] = []
    for ln in path.read_text(encoding="utf-8").splitlines():
        m = CUE_MD_RE.match(ln)
        if m:
            cues.append((m.group(1), m.group(2)))
    return cues


def regen_pdfs_from_markdown() -> None:
    records = json.loads(META_PATH.read_text())
    by_stem = {r["stem"]: r for r in records}
    OUT_PDF.mkdir(parents=True, exist_ok=True)
    md_files = sorted(OUT_MD.glob("M*.md"))
    for i, md_path in enumerate(md_files, 1):
        rec = by_stem.get(md_path.stem)
        if rec is None:
            rec = {
                "module_name": md_path.stem,
                "label": md_path.stem[:3],
                "duration": 0,
                "url": "",
                "expert": "",
            }
            for ln in md_path.read_text(encoding="utf-8").splitlines()[:12]:
                if ln.startswith("# "):
                    rec["module_name"] = ln[2:].strip()
                elif ln.startswith("**") and "Module" in ln:
                    rec["label"] = ln.strip("* ").strip()
                elif ln.startswith("Video:"):
                    rec["url"] = ln.split(" ", 1)[-1].strip()
        cues = parse_markdown_cues(md_path)
        pdf_path = OUT_PDF / f"{md_path.stem}.pdf"
        print(f"[{i}/{len(md_files)}] {md_path.stem} paras={len(cues_to_paragraphs(cues))}", flush=True)
        write_pdf(pdf_path, rec, cues)
    print("regenerated", len(md_files), "pdfs")


if __name__ == "__main__":
    import sys

    if "--from-markdown" in sys.argv:
        regen_pdfs_from_markdown()
    else:
        main()
