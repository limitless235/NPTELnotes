#!/usr/bin/env python3
"""Condense notes-2 lecture markdown into concept-focused notes-3 volumes.

Keeps: learning objectives, key-term tables, distinctions, exam/takeaway bullets.
Drops: long narrative, mermaid, lab steps, command dumps, case dumps unless short.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def strip_mermaid(text: str) -> str:
    return re.sub(r"```mermaid.*?```", "", text, flags=re.S)


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```[\w+-]*\n.*?```", "", text, flags=re.S)


def section(text: str, heading: str) -> str:
    """Return body under ## heading until next ## (or #)."""
    pat = rf"(?m)^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
    m = re.search(pat, text, re.S)
    return m.group(1).strip() if m else ""


def section_any(text: str, headings: list[str]) -> str:
    for h in headings:
        body = section(text, h)
        if body:
            return body
    # try ### variants at top level of takeaways
    for h in headings:
        pat = rf"(?m)^### {re.escape(h)}\s*\n(.*?)(?=^## |^### |\Z)"
        m = re.search(pat, text, re.S)
        if m:
            return m.group(1).strip()
    return ""


def first_heading_title(text: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else "Lecture"


def shorten_bullets(body: str, limit: int = 12) -> list[str]:
    bullets: list[str] = []
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("- ") or s.startswith("* "):
            item = s[2:].strip()
            # drop command-heavy lines
            if item.startswith("`") and len(item) > 40:
                continue
            if re.match(r"^(npm|pip|python|import |from |cd |mkdir )", item):
                continue
            bullets.append(f"- {item}")
        if len(bullets) >= limit:
            break
    return bullets


def extract_table(body: str) -> str:
    """Keep markdown tables; drop surrounding prose."""
    lines = body.splitlines()
    tables: list[str] = []
    i = 0
    while i < len(lines):
        if "|" in lines[i] and i + 1 < len(lines) and re.search(r"\|?\s*-{3,}", lines[i + 1]):
            chunk = [lines[i], lines[i + 1]]
            i += 2
            while i < len(lines) and "|" in lines[i]:
                chunk.append(lines[i])
                i += 1
            tables.append("\n".join(chunk))
            continue
        i += 1
    return "\n\n".join(tables)


def condense_lecture(path: Path, course: str) -> str:
    raw = path.read_text(encoding="utf-8")
    raw = strip_mermaid(raw)
    raw = strip_code_blocks(raw)
    title = first_heading_title(raw)

    objectives = section_any(
        raw,
        ["Learning objectives", "Learning Objectives", "Objectives"],
    )
    key_terms = section_any(raw, ["Key terms", "Key Terms", "Glossary"])
    distinctions = section_any(
        raw,
        [
            "Distinctions the instructor insists on",
            "Distinctions",
            "Important distinctions",
        ],
    )
    exam = section_any(
        raw,
        [
            "Exam-oriented recap",
            "Exam oriented recap",
            "Key takeaways",
            "Lecture takeaways",
            "Takeaways",
            "Exam Bullets",
            "Exam lines",
        ],
    )
    formulas = section_any(raw, ["Formulas / frameworks (if any)", "Formulas / frameworks", "Formulas"])

    # For GenAI / courses without Key terms: pull short definitional bullets from
    # "What this lecture" is too long — use objectives + takeaways only.
    parts = [f"## {title}", ""]

    if objectives:
        bullets = shorten_bullets(objectives, limit=8)
        if bullets:
            parts.append("### Learning focus")
            parts.extend(bullets)
            parts.append("")

    table = extract_table(key_terms) if key_terms else ""
    if table:
        parts.append("### Key terms")
        parts.append(table)
        parts.append("")
    elif key_terms:
        bullets = shorten_bullets(key_terms, limit=15)
        if bullets:
            parts.append("### Key terms")
            parts.extend(bullets)
            parts.append("")

    if formulas:
        # keep short formula blocks / lists only
        fbullets = shorten_bullets(formulas, limit=8)
        ftable = extract_table(formulas)
        if ftable or fbullets:
            parts.append("### Frameworks / formulas")
            if ftable:
                parts.append(ftable)
            parts.extend(fbullets)
            parts.append("")

    if distinctions:
        db = shorten_bullets(distinctions, limit=8)
        if db:
            parts.append("### Distinctions")
            parts.extend(db)
            parts.append("")

    if exam:
        eb = shorten_bullets(exam, limit=12)
        # also allow numbered lists
        if not eb:
            for line in exam.splitlines():
                s = line.strip()
                if re.match(r"^\d+\.", s):
                    eb.append(f"- {re.sub(r'^\\d+\\.\\s*', '', s)}")
                if len(eb) >= 12:
                    break
        if eb:
            parts.append("### Exam lines")
            parts.extend(eb)
            parts.append("")

    # Extra concept tables from anywhere in the lecture (esp. GenAI comparisons)
    if course == "genai":
        all_tables = extract_table(raw)
        if all_tables and "### Key terms" not in "\n".join(parts):
            # keep at most two tables to avoid lab dumps
            tables = all_tables.split("\n\n")[:2]
            if tables:
                parts.append("### Concept tables")
                parts.extend(tables)
                parts.append("")

    # Fallback: if almost empty, take first ~8 bullets from whole file
    rendered = "\n".join(parts).strip()
    if rendered.count("\n") < 4:
        bullets = shorten_bullets(raw, limit=10)
        parts = [f"## {title}", "", "### What to remember"] + bullets + [""]
        rendered = "\n".join(parts).strip()

    return rendered + "\n"


COURSES = {
    "csp": {
        "name": "Cyber Security and Privacy",
        "course_line": "NPTEL 106106248 · Prof. Saji K. Mathew",
        "lectures_dir": ROOT / "courses/01-cyber-security-and-privacy/notes-2/lectures",
        "out_dir": ROOT / "courses/01-cyber-security-and-privacy/notes-3",
        "glob": "T*.md",
        "volumes": [
            ("vol-01.md", "Volume 01 — Introduction & Foundations", ["T01", "T48", "T03", "T04", "T05", "T06", "T07"]),
            ("vol-02.md", "Volume 02 — GRC & Contingency Planning", [f"T{i:02d}" for i in range(8, 15)]),
            ("vol-03.md", "Volume 03 — Policy & Risk Management", [f"T{i:02d}" for i in range(15, 22)]),
            ("vol-04.md", "Volume 04 — Industry, Tech & Privacy Foundations", [f"T{i:02d}" for i in range(22, 30)]),
            ("vol-05.md", "Volume 05 — Regulation, Economics, Strategy, Capstone", [f"T{i:02d}" for i in range(30, 47)]),
        ],
    },
    "genai": {
        "name": "Generative AI & LLMs",
        "course_line": "NPTEL · Generative AI / LLMs",
        "lectures_dir": ROOT / "courses/03-generative-ai-llms/notes-2",
        "out_dir": ROOT / "courses/03-generative-ai-llms/notes-3",
        "glob": "L*.md",
        "volumes": [
            ("vol-01.md", "Volume 01 — Intro, CNN, Colab labs (L00–L09)", [f"L{i:02d}" for i in range(0, 10)]),
            ("vol-02.md", "Volume 02 — Autoencoders (L10–L20)", [f"L{i:02d}" for i in range(10, 21)]),
            ("vol-03.md", "Volume 03 — VAE family (L21–L30)", [f"L{i:02d}" for i in range(21, 31)]),
            ("vol-04.md", "Volume 04 — GANs (L31–L43)", [f"L{i:02d}" for i in range(31, 44)]),
            ("vol-05.md", "Volume 05 — Diffusion (L44–L53)", [f"L{i:02d}" for i in range(44, 54)]),
            ("vol-06.md", "Volume 06 — NLP, Transformers, LLMs (L54–L63)", [f"L{i:02d}" for i in range(54, 64)]),
        ],
    },
    "infosec": {
        "name": "Information Security (CEC)",
        "course_line": "SWAYAM / CEC Information Security",
        "lectures_dir": ROOT / "courses/05-information-security-cec/notes-2/lectures",
        "out_dir": ROOT / "courses/05-information-security-cec/notes-3",
        "glob": "M*.md",
        "volumes": [
            ("vol-01.md", "Volume 01 — M00–M11", [f"M{i:02d}" for i in range(0, 12)]),
            ("vol-02.md", "Volume 02 — M12–M23", [f"M{i:02d}" for i in range(12, 24)]),
            ("vol-03.md", "Volume 03 — M24–M35", [f"M{i:02d}" for i in range(24, 36)]),
            ("vol-04.md", "Volume 04 — M36–M47", [f"M{i:02d}" for i in range(36, 48)]),
        ],
    },
}


def index_lectures(lectures_dir: Path, glob_pat: str) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for path in sorted(lectures_dir.glob(glob_pat)):
        m = re.match(r"([TMLtml]\d{2})", path.name)
        if not m:
            continue
        key = m.group(1).upper()
        # Prefer first match; GenAI uses L00 etc.
        if key.startswith("L"):
            key = f"L{int(key[1:]):02d}"
        elif key.startswith("T"):
            key = f"T{int(key[1:]):02d}"
        elif key.startswith("M"):
            key = f"M{int(key[1:]):02d}"
        out[key] = path
    return out


def build_course(key: str) -> None:
    cfg = COURSES[key]
    lectures = index_lectures(cfg["lectures_dir"], cfg["glob"])
    out_dir: Path = cfg["out_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "pdf").mkdir(exist_ok=True)

    for filename, title, ids in cfg["volumes"]:
        chunks = [
            f"# {title}",
            "",
            f"> {cfg['name']} · {cfg['course_line']}",
            "> **notes-3** — concept exam notes (definitions & what things do). Breadth over lab depth.",
            "",
            "---",
            "",
        ]
        missing = []
        for lid in ids:
            # de-dupe vol-05 CSP T38 listed twice in original map
            path = lectures.get(lid)
            if not path:
                # try alternate zero forms
                path = lectures.get(lid.upper())
            if not path:
                missing.append(lid)
                continue
            chunks.append(condense_lecture(path, key))
            chunks.append("\n---\n")
        text = "\n".join(chunks).rstrip() + "\n"
        path = out_dir / filename
        path.write_text(text, encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)} ({len(text.split())} words); missing={missing}")

    readme = out_dir / "README.md"
    if not readme.exists():
        readme.write_text(
            f"""# notes-3 — concept exam notes ({cfg['name']})

Condensed from **notes-2** for concept-style exams: what topics *are* and what they *do*.

Long transcript narrative, lab click-paths, code dumps, and filler detail are removed. Coverage of lecture topics is kept.

Rebuild: `python3 scripts/condense_notes3_from_notes2.py {key}` then `./scripts/build-notes3-pdfs.sh {key if key != 'csp' else 'csp'}`.
""",
            encoding="utf-8",
        )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("course", choices=["csp", "genai", "infosec", "all"])
    args = ap.parse_args()
    keys = list(COURSES) if args.course == "all" else [args.course]
    for k in keys:
        build_course(k)


if __name__ == "__main__":
    main()
