#!/usr/bin/env python3
"""Fetch YouTube captions for NPTEL Ethical Hacking (Digimat video IDs) → markdown."""

from __future__ import annotations

import json
import re
import subprocess
import time
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import GenericProxyConfig

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "courses" / "02-ethical-hacking"
META_PATH = COURSE / "transcripts" / "playlist-metadata.json"
OUT_MD = COURSE / "transcripts" / "markdown"
RAW_DIR = COURSE / "transcripts" / "raw"
SOCKS = "socks5://127.0.0.1:9050"
COURSE_ID = "NPTEL 106105217 / noc26_cs157"
INSTRUCTOR = "Prof. Indranil Sengupta, IIT Kharagpur"


def slugify(title: str) -> str:
    s = title.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:90]


def fmt_ts(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def clean_snip(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(r"\[(?:music|Music|MUSIC|applause|laughter)\]", "", text, flags=re.I)
    return re.sub(r"\s+", " ", text).strip()


def paragraphs_from_snippets(snippets: list[dict]) -> list[tuple[str, str]]:
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
        except Exception as e:  # noqa: BLE001
            last_err = e
    raise last_err  # type: ignore[misc]


def to_markdown(meta: dict, snippets: list[dict], lang: str) -> str:
    lec = meta["lecture"]
    title = meta["title"]
    vid = meta["id"]
    url = f"https://www.youtube.com/watch?v={vid}"
    slug = slugify(title)
    paras = paragraphs_from_snippets(snippets)
    word_count = sum(len(p[1].split()) for p in paras)
    body = "\n\n".join(f"**[{ts}]** {text}" for ts, text in paras)
    return f"""---
title: "{title.replace('"', "'")}"
lecture: {lec:02d}
video_id: {vid}
language: {lang}
course: {COURSE_ID}
instructor: {INSTRUCTOR}
---

# Lecture {lec:02d}: {title}

| | |
|---|---|
| **Course** | {COURSE_ID} |
| **Instructor** | {INSTRUCTOR} |
| **Captions** | {lang} |
| **Words** | {word_count:,} |
| **Video** | [{vid}]({url}) |
| **Digimat** | [L{lec:02d}](http://www.digimat.in/nptel/courses/video/106105217/L{lec:02d}.html) |

Auto-generated YouTube captions, lightly cleaned. Verbatim lecture captions for transcript-grounded notes.

## Transcript

{body}
"""


def main() -> None:
    playlist = json.loads(META_PATH.read_text(encoding="utf-8"))
    OUT_MD.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    api = make_api()
    failures: list[str] = []
    successes: list[dict] = []

    for meta in playlist:
        lec = meta["lecture"]
        vid = meta["id"]
        title = meta["title"]
        slug = slugify(title)
        stem = f"{lec:02d}-{slug}"
        md_path = OUT_MD / f"{stem}.md"
        raw_path = RAW_DIR / f"{stem}.json"

        print(f"[{lec:02d}/62] {title} ({vid})", flush=True)
        snippets = None
        lang = "unknown"

        if raw_path.exists():
            payload = json.loads(raw_path.read_text(encoding="utf-8"))
            snippets, lang = payload["snippets"], payload["language"]
            print("  reused raw json", flush=True)
        else:
            for attempt in range(1, 8):
                try:
                    snippets, lang = fetch_transcript(api, vid)
                    raw_path.write_text(
                        json.dumps(
                            {"id": vid, "title": title, "lecture": lec, "language": lang, "snippets": snippets},
                            indent=2,
                        ),
                        encoding="utf-8",
                    )
                    print(f"  fetched {len(snippets)} snippets ({lang})", flush=True)
                    break
                except Exception as e:  # noqa: BLE001
                    print(f"  attempt {attempt} failed: {type(e).__name__}", flush=True)
                    restart_tor()
                    api = make_api()
                    time.sleep(3 + attempt * 2)
            if snippets is None:
                failures.append(f"{stem} ({vid})")
                continue
            time.sleep(2.5)

        md_path.write_text(to_markdown(meta, snippets, lang), encoding="utf-8")
        successes.append({"lecture": lec, "title": title, "id": vid, "slug": stem, "language": lang})

    readme = COURSE / "transcripts" / "README.md"
    rows = [
        "| Lec | Title | Captions | Markdown | Video |",
        "|-----|-------|----------|----------|-------|",
    ]
    for item in successes:
        url = f"https://www.youtube.com/watch?v={item['id']}"
        rows.append(
            f"| {item['lecture']:02d} | {item['title']} | {item['language']} "
            f"| [{item['slug']}.md](markdown/{item['slug']}.md) | [{item['id']}]({url}) |"
        )
    fail_md = ""
    if failures:
        fail_md = "\n## Missing\n\n" + "\n".join(f"- {f}" for f in failures) + "\n"
    readme.write_text(
        f"""# Ethical Hacking — lecture transcripts

**Course:** {COURSE_ID} · **Instructor:** {INSTRUCTOR}

Video IDs from [Digimat NPTEL 106105217](http://www.digimat.in/nptel/courses/video/106105217/106105217.html). Captions fetched via YouTube (Tor proxy), grouped into paragraphs.

**{len(successes)} / {len(playlist)}** lectures transcribed.

{chr(10).join(rows)}
{fail_md}
""",
        encoding="utf-8",
    )
    print("done", len(successes), "ok,", len(failures), "failed")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
