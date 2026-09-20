#!/usr/bin/env python3
"""Fetch YouTube captions for the Generative AI playlist and write markdown + PDFs."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import time
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import GenericProxyConfig

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "courses" / "03-generative-ai-llms"
OUT_MD = COURSE / "transcripts"
OUT_PDF = COURSE / "transcripts" / "pdf"
PLAYLIST = "https://www.youtube.com/playlist?list=PLgMDNELGJ1Ca_DduFvH6qfI1eapL48xOr"
SOCKS = "socks5://127.0.0.1:9050"
YT_DLP = shutil.which("yt-dlp") or str(Path.home() / ".local/bin/yt-dlp")


def slugify(title: str) -> str:
    s = title.lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:90]


def fmt_duration(seconds: int) -> str:
    h, rem = divmod(int(seconds or 0), 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def fmt_ts(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def clean_snip(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(r"\[(?:music|Music|MUSIC)\]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def paragraphs_from_snippets(snippets: list[dict]) -> list[tuple[str, str]]:
    """Group caption snippets into readable paragraphs with a leading timestamp."""
    paras: list[tuple[str, str]] = []
    buf: list[str] = []
    start = 0.0
    char_len = 0
    for snip in snippets:
        text = clean_snip(snip["text"])
        if not text:
            continue
        if not buf:
            start = float(snip["start"])
        buf.append(text)
        char_len += len(text) + 1
        end_sentence = bool(re.search(r"[.?!]$", text))
        if char_len >= 420 and end_sentence:
            paras.append((fmt_ts(start), " ".join(buf)))
            buf, char_len = [], 0
        elif char_len >= 700:
            paras.append((fmt_ts(start), " ".join(buf)))
            buf, char_len = [], 0
    if buf:
        paras.append((fmt_ts(start), " ".join(buf)))
    return paras


def restart_tor() -> None:
    subprocess.run(["sudo", "service", "tor", "restart"], check=False, capture_output=True)
    time.sleep(4)


def make_api() -> YouTubeTranscriptApi:
    return YouTubeTranscriptApi(
        proxy_config=GenericProxyConfig(http_url=SOCKS, https_url=SOCKS)
    )


def fetch_transcript(api: YouTubeTranscriptApi, video_id: str) -> tuple[list[dict], str]:
    last_err: Exception | None = None
    for languages in (["en"], ["en-US", "en-GB", "en"], None):
        try:
            fetched = api.fetch(video_id) if languages is None else api.fetch(video_id, languages=languages)
            snippets = [
                {"text": s.text, "start": float(s.start), "duration": float(s.duration)}
                for s in fetched
            ]
            lang = getattr(fetched, "language", None) or "unknown"
            return snippets, lang
        except Exception as e:  # noqa: BLE001 — retry across language prefs / circuits
            last_err = e
    raise last_err  # type: ignore[misc]


def to_markdown(meta: dict, snippets: list[dict], lang: str, index: int, slug: str) -> str:
    title = meta["title"]
    vid = meta["id"]
    url = f"https://www.youtube.com/watch?v={vid}"
    duration = fmt_duration(meta["duration"])
    paras = paragraphs_from_snippets(snippets)
    word_count = sum(len(p[1].split()) for p in paras)
    body = "\n\n".join(f"**[{ts}]** {text}" for ts, text in paras)
    return f"""---
title: "{title.replace('"', "'")}"
video_id: {vid}
index: {index:02d}
duration: {duration}
language: {lang}
playlist: {PLAYLIST}
---

# {title}

| | |
|---|---|
| **Lecture** | {index:02d} / 63 + intro |
| **Duration** | {duration} |
| **Captions** | {lang} |
| **Words** | {word_count:,} |
| **Video** | [{vid}]({url}) |
| **Playlist** | [Fundamentals of Generative AI and LLMs]({PLAYLIST}) |

Auto-generated YouTube captions, lightly cleaned (removed `[music]` tags, grouped into paragraphs). These are **verbatim lecture captions**, not edited notes.

## Transcript

{body}
"""


def build_pdf(md_path: Path, pdf_path: Path) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "pandoc",
        str(md_path),
        "-o",
        str(pdf_path),
        "--from=markdown-tex_math_dollars-raw_tex",
        "--pdf-engine=xelatex",
        "-V",
        "geometry:margin=1in",
        "-V",
        "fontsize=11pt",
        "-V",
        "documentclass=article",
        "-V",
        "mainfont=DejaVu Serif",
        "-V",
        "monofont=DejaVu Sans Mono",
        "-V",
        "colorlinks=true",
        "-V",
        "linkcolor=blue",
        "-V",
        "linestretch=1.15",
    ]
    subprocess.run(cmd, check=True)


def load_playlist() -> list[dict]:
    raw = subprocess.check_output(
        [YT_DLP, "--flat-playlist", "--print", "%(id)s\t%(title)s\t%(duration)s", PLAYLIST],
        text=True,
    )
    videos = []
    for line in raw.strip().splitlines():
        vid, title, dur = line.split("\t")
        videos.append({"id": vid, "title": title.strip(), "duration": int(dur) if dur.isdigit() else 0})

    def sort_key(v: dict) -> tuple[int, int]:
        m = re.search(r"Lec\s*(\d+)", v["title"], re.I)
        if m:
            return (1, int(m.group(1)))
        return (0, 0)

    videos.sort(key=sort_key)
    return videos


def main() -> None:
    playlist = load_playlist()
    OUT_MD.mkdir(parents=True, exist_ok=True)
    OUT_PDF.mkdir(parents=True, exist_ok=True)
    raw_dir = OUT_MD / "raw"
    raw_dir.mkdir(exist_ok=True)

    api = make_api()
    failures: list[str] = []
    successes: list[dict] = []

    for i, meta in enumerate(playlist):
        title = meta["title"]
        vid = meta["id"]
        slug = slugify(title)
        stem = f"{i:02d}-{slug}"
        md_path = OUT_MD / f"{stem}.md"
        pdf_path = OUT_PDF / f"{stem}.pdf"
        raw_path = raw_dir / f"{stem}.json"

        print(f"[{i:02d}/{len(playlist)-1}] {title} ({vid})", flush=True)
        snippets = None
        lang = "unknown"
        if raw_path.exists():
            payload = json.loads(raw_path.read_text())
            snippets, lang = payload["snippets"], payload["language"]
            print("  reused raw json", flush=True)
        else:
            for attempt in range(1, 5):
                try:
                    snippets, lang = fetch_transcript(api, vid)
                    raw_path.write_text(
                        json.dumps(
                            {"id": vid, "title": title, "language": lang, "snippets": snippets},
                            indent=2,
                        )
                    )
                    print(f"  fetched {len(snippets)} snippets ({lang})", flush=True)
                    break
                except Exception as e:  # noqa: BLE001
                    print(f"  attempt {attempt} failed: {type(e).__name__}: {e}", flush=True)
                    restart_tor()
                    api = make_api()
                    time.sleep(2 * attempt)
            if snippets is None:
                failures.append(f"{stem} ({vid})")
                continue
            time.sleep(0.8)

        md_path.write_text(to_markdown(meta, snippets, lang, i, slug))
        try:
            build_pdf(md_path, pdf_path)
            print(f"  pdf {pdf_path.name} ({pdf_path.stat().st_size} bytes)", flush=True)
        except subprocess.CalledProcessError as e:
            print(f"  pdf FAILED {e}", flush=True)
            failures.append(f"pdf:{stem}")
            continue
        successes.append(
            {
                "index": i,
                "title": title,
                "id": vid,
                "slug": stem,
                "md": str(md_path.relative_to(COURSE)),
                "pdf": str(pdf_path.relative_to(COURSE)),
                "language": lang,
                "duration": meta["duration"],
            }
        )

    index_path = OUT_MD / "README.md"
    rows = [
        "| # | Lecture | Duration | Captions | PDF | Markdown | Video |",
        "|---:|---------|----------|----------|-----|----------|-------|",
    ]
    for item in successes:
        url = f"https://www.youtube.com/watch?v={item['id']}"
        rows.append(
            f"| {item['index']:02d} | {item['title']} | {fmt_duration(item['duration'])} "
            f"| {item['language']} | [{Path(item['pdf']).name}]({item['pdf'].replace('transcripts/', '')}) "
            f"| [{Path(item['md']).name}]({Path(item['md']).name}) | [{item['id']}]({url}) |"
        )
    fail_md = ""
    if failures:
        fail_md = "\n## Missing\n\n" + "\n".join(f"- {f}" for f in failures) + "\n"
    index_path.write_text(
        f"""# Generative AI lecture transcripts

YouTube playlist: [{PLAYLIST}]({PLAYLIST})

**{len(successes)} / {len(playlist)}** videos have caption PDFs. Source: YouTube auto-generated English captions, fetched for personal study.

PDFs are in [`pdf/`](pdf/).

{chr(10).join(rows)}
{fail_md}
"""
    )
    print("done", len(successes), "ok,", len(failures), "failed")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
