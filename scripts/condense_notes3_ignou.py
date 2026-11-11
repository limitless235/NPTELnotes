#!/usr/bin/env python3
"""Build concept-focused notes-3 volumes for Cyber Security Tools (IGNOU).

Source of truth is the course volume set under pdf/ (built from notes/vol-*.md).
There is no notes-2 folder for this course — condense from those volume notes.

Keeps: purpose, definitions, comparison tables, frameworks, countermeasures.
Drops: command recipes, install/UI click-paths, lab IP walkthroughs, payloads.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "courses" / "04-cyber-security-tools-ignou" / "notes"
OUT = ROOT / "courses" / "04-cyber-security-tools-ignou" / "notes-3"

VOLUMES = [
    {
        "file": "vol-01.md",
        "title": "Volume 01 — Essentials, APT/Kill Chain, Firewalls (L01–L09)",
        "blurb": "Tool landscape, CIA/risk, Nmap/Netcat/Wireshark roles, Kill Chain, STRIDE, firewall concepts.",
    },
    {
        "file": "vol-02.md",
        "title": "Volume 02 — Wireless, Web Scanning, App Inspection (L10–L18)",
        "blurb": "Wi-Fi assessment ideas, Nikto/ZAP/Gobuster roles, SQLi/XSS concepts — no lab command dumps.",
    },
    {
        "file": "vol-03.md",
        "title": "Volume 03 — Web Attacks, IDS, Assurance, Malware (L19–L27)",
        "blurb": "Server-side flaws, session/CSRF, Snort/IDS, OpenVAS, CVSS, frameworks, malware analysis roles.",
    },
    {
        "file": "vol-04.md",
        "title": "Volume 04 — E-Commerce, Social Engineering, Cyber Law (L28–L36)",
        "blurb": "TLS/PCI, phishing/OSINT, password attacks conceptually, IT Act/DPDP, CERT-In, course synthesis.",
    },
]

# Sections that are lab/procedure dumps — drop entirely
DROP_SECTION_RE = re.compile(
    r"(?i)^(usage steps|lab setup steps|lab exercise|installation|"
    r".*usage steps|.*— usage steps|powershell usage steps|gui steps|"
    r"passive scan steps|active scan steps|manual interception|"
    r"manual testing steps|manual testing payloads|dvwa lab|"
    r"sandbox steps|audit steps|scoring steps|attack surface mapping steps|"
    r"risk assessment steps|cli \(openvas-cli\)|hash extraction \(awareness\)|"
    r"fail2ban defense|gophish \(alternative\)|hashcat alternative|"
    r"zap testing|zap csrf check|zap detection|zap for e-commerce|"
    r"beef \(awareness\)|command injection testing|lfi/rfi testing|"
    r"capstone scenario|assessment prep)$"
)

# Prefer keeping short purpose-like headings as concept material
PURPOSE_RE = re.compile(
    r"(?i)^(purpose|overview|.*— purpose|nmap — purpose|netcat — purpose|"
    r"iptables — purpose)$"
)


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```[\w+-]*\n.*?```", "", text, flags=re.S)


def strip_inline_cmds(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        inner = m.group(1).strip()
        # Drop long shell/flag lines; keep short tokens and header names
        if (" " in inner or inner.startswith("-")) and len(inner) > 24:
            return inner.split()[0]
        return inner

    return re.sub(r"`([^`]+)`", repl, text)


def clean_bullet(line: str) -> str | None:
    s = line.strip()
    if s.startswith(("- ", "* ")):
        body = s[2:].strip()
    elif re.match(r"^\d+\.\s+", s):
        body = re.sub(r"^\d+\.\s+", "", s).strip()
    else:
        return None
    body = strip_inline_cmds(body)
    if not body or len(body) < 3:
        return None
    # Drop command-recipe bullets
    if re.match(
        r"^(sudo |nmap |nc |nikto |sqlmap |hydra |john |gobuster |dirb |"
        r"ffuf |airmon|airodump|aireplay|aircrack|hashcat |zap-|"
        r"openssl |theHarvester |clamscan |omp |echo \|)",
        body,
        re.I,
    ):
        return None
    if body.startswith("/") or body.startswith("?") or body.startswith(";"):
        return None
    if "192.168." in body or "127.0.0.1" in body:
        # Keep conceptual lines that merely mention lab IPs in passing? Prefer drop.
        if re.search(r"\b(http://|https://|ssh://|ftp://)", body):
            return None
    return f"- {body}"


def extract_table(body: str) -> str:
    lines = body.splitlines()
    tables: list[str] = []
    i = 0
    while i < len(lines):
        if "|" in lines[i] and i + 1 < len(lines) and re.search(r"\|?\s*-{3,}", lines[i + 1]):
            chunk = [strip_inline_cmds(lines[i]), lines[i + 1]]
            i += 2
            while i < len(lines) and "|" in lines[i]:
                chunk.append(strip_inline_cmds(lines[i]))
                i += 1
            tables.append("\n".join(chunk))
            continue
        i += 1
    return "\n\n".join(tables)


def section_chunks(lecture: str) -> list[tuple[str, str]]:
    """Split lecture body into (heading, body) pairs under ## headings."""
    parts = re.split(r"(?m)^## ", lecture)
    chunks: list[tuple[str, str]] = []
    for part in parts[1:]:
        lines = part.splitlines()
        if not lines:
            continue
        heading = lines[0].strip()
        body = "\n".join(lines[1:]).strip()
        # Stop at lab reminder / trailing ---
        body = re.split(r"(?m)^\*Lab reminder:", body)[0].strip()
        body = body.rstrip("-").strip()
        chunks.append((heading, body))
    return chunks


def prose_to_bullets(body: str, limit: int = 8, max_len: int = 220) -> list[str]:
    """Turn short prose paragraphs into bullets; keep existing bullets/tables handled elsewhere."""
    out: list[str] = []
    for para in re.split(r"\n\s*\n", body):
        para = para.strip()
        if not para or "|" in para.splitlines()[0]:
            continue
        if para.startswith("-") or re.match(r"^\d+\.", para):
            for line in para.splitlines():
                b = clean_bullet(line)
                if b:
                    out.append(b)
            continue
        para = strip_inline_cmds(re.sub(r"\s+", " ", para))
        # Drop bare URLs / long syllabus cross-refs as standalone bullets
        if para.startswith("http"):
            continue
        if 20 <= len(para) <= max_len:
            out.append(f"- {para}")
        elif len(para) > max_len:
            # Keep first clause as a shorter concept line
            clause = re.split(r"[.—]", para)[0].strip()
            if 20 <= len(clause) <= max_len:
                out.append(f"- {clause}.")
        if len(out) >= limit:
            break
    return out[:limit]


def exam_line(text: str) -> str | None:
    """Compress a bullet into a short exam-style line."""
    s = text[2:].strip() if text.startswith("- ") else text.strip()
    s = re.sub(r"\s+", " ", s)
    if "table below" in s.lower() or "comparison/reference" in s.lower():
        return None
    # Prefer the clause before syllabus cross-refs
    s = re.split(
        r"\s[—-]\s(?:maps|Aligns|foundation for|PGDCS|Nina|capstone for)",
        s,
    )[0].strip()
    if len(s) > 140:
        s = s[:137].rsplit(" ", 1)[0] + "…"
    if len(s) < 12:
        return None
    return f"- {s}"


def condense_lecture(block: str) -> str | None:
    block = strip_code_blocks(block)
    hm = re.match(r"# (L\d+:.+)\n", block)
    if not hm:
        return None
    title = hm.group(1).strip()
    title = re.sub(r"^L0(\d):", r"L\1:", title)

    what: list[str] = []
    defenses: list[str] = []
    tables: list[str] = []
    exam_seeds: list[str] = []

    for heading, body in section_chunks(block):
        h = heading.strip()
        if DROP_SECTION_RE.match(h):
            continue
        if re.search(r"(?i)countermeasure", h):
            for line in body.splitlines():
                b = clean_bullet(line)
                if b and len(b) < 180:
                    defenses.append(b)
            defenses = defenses[:5]
            continue

        table = extract_table(body)
        if table:
            tables.append(table)

        if PURPOSE_RE.match(h):
            bullets = prose_to_bullets(body, limit=4)
            # Prefix tool-purpose headings so Nmap/Netcat stay distinct
            if "—" in h or " - " in h:
                tool = re.split(r"\s[—-]\s", h)[0].strip()
                prefixed = []
                for b in bullets:
                    item = b[2:]
                    if not item.lower().startswith(tool.lower()):
                        prefixed.append(f"- **{tool}:** {item}")
                    else:
                        prefixed.append(b)
                bullets = prefixed
            what.extend(bullets)
            exam_seeds.extend(bullets)
            continue

        # Keep fuller lists for high-value frameworks (PCI 12 reqs, Kill Chain stages)
        lim = 14 if re.search(r"(?i)pci|kill chain|framework|it act", h) else 8
        bullets = prose_to_bullets(body, limit=lim)
        if bullets:
            first = bullets[0][2:]
            if not first.startswith("**"):
                bullets[0] = f"- **{h}** — {first}"
            what.extend(bullets)
            exam_seeds.extend(bullets[:3])
        elif table:
            what.append(f"- **{h}:**")

    def uniq(items: list[str]) -> list[str]:
        seen: set[str] = set()
        out: list[str] = []
        for x in items:
            key = re.sub(r"\W+", "", x.lower())
            if key in seen:
                continue
            seen.add(key)
            out.append(x)
        return out

    what = uniq(what)[:14]
    defenses = uniq(defenses)[:5]
    exam: list[str] = []
    for seed in exam_seeds + what:
        line = exam_line(seed)
        if line:
            exam.append(line)
    exam = uniq(exam)[:5]

    parts = [f"## {title}", ""]
    if what or tables:
        parts.append("### What it is / what it does")
        parts.extend(what)
        for t in tables:
            parts.append("")
            parts.append(t)
        parts.append("")
    if defenses:
        parts.append("### Defenses (one-liners)")
        parts.extend(defenses)
        parts.append("")
    if exam:
        parts.append("### Exam lines")
        parts.extend(exam)
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def split_lectures(text: str) -> list[str]:
    parts = re.split(r"(?m)^(?=# L\d+:)", text)
    return [p.strip() for p in parts if p.strip().startswith("# L")]


def build_volume(meta: dict) -> str:
    src = (SRC / meta["file"]).read_text(encoding="utf-8")
    lectures = split_lectures(src)
    body: list[str] = []
    for lec in lectures:
        rendered = condense_lecture(lec)
        if rendered:
            body.append(rendered)
            body.append("---\n")
    header = f"""# {meta['title']}

> Cyber Security Tools · IGNOU/BAOU nou26_ge86 · Prof. Dr. Nilesh K. Modi  
> **notes-3** — concept exam notes (what things are / what they do). Condensed from course `pdf/` volumes. No lab command dumps.

{meta['blurb']}

---

"""
    return header + "\n".join(body).rstrip() + "\n"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "pdf").mkdir(exist_ok=True)
    for meta in VOLUMES:
        text = build_volume(meta)
        path = OUT / meta["file"]
        path.write_text(text, encoding="utf-8")
        words = len(text.split())
        print(f"Wrote {path.relative_to(ROOT)} ({words} words, {text.count(chr(10))+1} lines)")


if __name__ == "__main__":
    main()
