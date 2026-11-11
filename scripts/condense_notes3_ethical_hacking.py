#!/usr/bin/env python3
"""Build concept-focused notes-3 volumes for Ethical Hacking from notes/ sources.

notes-3 keeps definitions, comparisons, and what things do — drops command
syntax, lab procedures, and tool laundry lists that exams do not ask for.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "courses" / "02-ethical-hacking" / "notes"
OUT = ROOT / "courses" / "02-ethical-hacking" / "notes-3"

VOLUMES = [
    {
        "file": "vol-01.md",
        "title": "Volume 01 — Networking Foundations (L01–L10)",
        "blurb": "Ethical hacking intro, OSI/TCP-IP, IP addressing, TCP/UDP, subnetting — concepts only.",
    },
    {
        "file": "vol-02.md",
        "title": "Volume 02 — Routing, Recon & Nessus (L11–L20)",
        "blurb": "Routing protocols, IPv6, OSINT/Nmap ideas, Nessus — what each is and does.",
    },
    {
        "file": "vol-03.md",
        "title": "Volume 03 — Metasploit, MITM & Crypto I (L21–L30)",
        "blurb": "Exploitation frameworks, social engineering, ARP/MITM, cryptography foundations.",
    },
    {
        "file": "vol-04.md",
        "title": "Volume 04 — Hash, PKI & Network Attacks (L31–L40)",
        "blurb": "Hash functions, signatures, steganography, biometrics, DNS/email security.",
    },
    {
        "file": "vol-05.md",
        "title": "Volume 05 — System Attacks & Hardware Security (L41–L50)",
        "blurb": "Passwords, phishing, malware, Wi-Fi, DoS, side channels, PUF, hardware trojans.",
    },
    {
        "file": "vol-06.md",
        "title": "Volume 06 — Web Vulns, Nmap & Wireshark (L51–L62)",
        "blurb": "Web scanning, SQLi, XSS, file upload, Nmap/Wireshark roles, course wrap-up.",
    },
]


def strip_inline_code_cmds(text: str) -> str:
    """Turn `nmap -sS` style into plain tool/idea names where helpful."""
    def repl(m: re.Match[str]) -> str:
        inner = m.group(1).strip()
        # Keep short identifiers; drop long command lines
        if " " in inner and len(inner) > 20:
            # Prefer the first token as the tool name
            return inner.split()[0]
        return inner

    return re.sub(r"`([^`]+)`", repl, text)


def clean_bullet(line: str) -> str | None:
    line = line.strip()
    if not line.startswith("-"):
        return None
    body = line[1:].strip()
    body = strip_inline_code_cmds(body)
    # Drop pure command-recipe bullets
    if re.match(r"^(nmap|msf|hydra|john|hashcat|arpspoof|sqlmap|dig|whois)\s", body, re.I):
        return None
    if body.startswith("echo ") or body.startswith("systemctl "):
        return None
    return f"- {body}"


def extract_section(block: str, name: str) -> list[str]:
    pattern = rf"### {re.escape(name)}\n(.*?)(?=\n### |\n---|\n## |\Z)"
    m = re.search(pattern, block, re.S)
    if not m:
        return []
    out: list[str] = []
    for line in m.group(1).splitlines():
        b = clean_bullet(line)
        if b:
            out.append(b)
    return out


def extract_lecture(block: str) -> str | None:
    hm = re.match(r"## (L\d+:.+)\n", block)
    if not hm:
        return None
    title = hm.group(1).strip()
    concepts = extract_section(block, "Concepts")
    # Some lectures use a named diagram section — skip mermaid bodies
    defenses = extract_section(block, "Defenses")
    exams = extract_section(block, "Exam Bullets")

    # Soft-merge a few defense ideas into "Also know" if short
    defenses = [d for d in defenses if len(d) < 160][:4]

    parts = [f"## {title}", ""]
    if concepts:
        parts.append("### What it is / what it does")
        parts.extend(concepts)
        parts.append("")
    if defenses:
        parts.append("### Defenses (one-liners)")
        parts.extend(defenses)
        parts.append("")
    if exams:
        parts.append("### Exam lines")
        parts.extend(exams)
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def split_lectures(text: str) -> list[str]:
    # Drop volume header through first --- after title blurb
    parts = re.split(r"\n(?=## L\d+:)", text)
    lectures = []
    for p in parts:
        if p.startswith("## L"):
            # trim trailing nav links
            p = re.split(r"\n\*Previous:|\n\*Next:", p)[0].strip()
            lectures.append(p)
    return lectures


def build_volume(meta: dict) -> str:
    src = (SRC / meta["file"]).read_text(encoding="utf-8")
    lectures = split_lectures(src)
    body = []
    for lec in lectures:
        rendered = extract_lecture(lec)
        if rendered:
            body.append(rendered)
            body.append("---\n")
    header = f"""# {meta['title']}

> Ethical Hacking · NPTEL 106105217 · Prof. Indranil Sengupta  
> **notes-3** — concept exam notes (what things are / what they do). No lab command dumps.

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
        print(f"Wrote {path.relative_to(ROOT)} ({words} words)")


if __name__ == "__main__":
    main()
