#!/usr/bin/env python3
"""Generate transcript-grounded notes-2 lecture files for Ethical Hacking."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "courses" / "02-ethical-hacking"
TRANSCRIPTS = COURSE / "transcripts" / "markdown"
OUT = COURSE / "notes-2" / "lectures"
META_PATH = COURSE / "transcripts" / "playlist-metadata.json"
INSTRUCTOR = "Prof. Indranil Sengupta, IIT Kharagpur"
COURSE_ID = "NPTEL 106105217 / noc26_cs157"

WEEK_MAP = {
    range(1, 6): "Week 1 — Intro, networking fundamentals, TCP/IP",
    range(6, 11): "Week 2 — IP addressing, routing, TCP/UDP, subnets",
    range(11, 15): "Week 3 — Routing protocols, IPv6",
    range(15, 19): "Week 4 — Lab setup, OSINT, recon tools, Nmap",
    range(19, 26): "Week 5 — Nessus, system hacking, malware, ARP/MITM",
    range(26, 31): "Week 6 — Cryptography foundations",
    range(31, 41): "Week 7 — Hash, PKI, steganography, network attacks",
    range(41, 51): "Week 8 — Passwords, phishing, Wi-Fi, DoS, hardware security",
    range(51, 63): "Week 9–10 — Web vulns, Nmap deep-dive, Wireshark, summary",
}

TOOL_PATTERNS = re.compile(
    r"\b(nmap|nessus|metasploit|msfconsole|msfvenom|wireshark|sqlmap|john the ripper|"
    r"hashcat|aircrack-ng|ettercap|arpspoof|bettercap|setoolkit|burp suite|openssl|"
    r"whois|dig|dnsenum|theharvester|netcraft|kali linux|virtualbox|vmware)\b",
    re.I,
)
CMD_PATTERN = re.compile(
    r"`([^`]+)`|(?:^|\s)((?:nmap|msfconsole|openssl|dig|whois|dnsenum|sqlmap|hashcat|"
    r"aircrack-ng|arpspoof|ettercap)\s[^\n.]{3,80})",
    re.I,
)
DEF_PATTERN = re.compile(
    r"([A-Z][^.!?]{0,80}?)\s+(?:is called|is known as|is defined as|means|refers to)\s+([^.!?]+[.!?])",
    re.I,
)


def slugify(title: str) -> str:
    s = title.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:80]


def week_for(lec: int) -> str:
    for rng, label in WEEK_MAP.items():
        if lec in rng:
            return label
    return "Ethical Hacking"


def load_transcript_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if "## Transcript" in text:
        text = text.split("## Transcript", 1)[1]
    text = re.sub(r"\*\*\[[^\]]+\]\*\*\s*", "", text)
    text = re.sub(r"\[(?:music|applause|laughter)\]", "", text, flags=re.I)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fix_asr(text: str) -> str:
    fixes = {
        "TCP IP": "TCP/IP",
        "tcp ip": "TCP/IP",
        "IP address": "IP address",
        "metas polar": "Metasploit",
        "metasploit": "Metasploit",
        "nessus": "Nessus",
        "n map": "Nmap",
        "nmap": "Nmap",
        "wire shark": "Wireshark",
        "man in the middle": "man-in-the-middle",
        "ARP spoofing": "ARP spoofing",
        "SQL injection": "SQL injection",
        "cross site scripting": "cross-site scripting",
        "denial of service": "denial-of-service",
        "Kali Linux": "Kali Linux",
        "hash function": "hash function",
        "public key": "public key",
        "private key": "private key",
    }
    for old, new in fixes.items():
        text = re.sub(re.escape(old), new, text, flags=re.I)
    return text


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if len(p.strip()) > 20]


def pick_objectives(sents: list[str], n: int = 5) -> list[str]:
    keys = (
        "we will",
        "in this lecture",
        "objective",
        "learn",
        "understand",
        "discuss",
        "cover",
        "explain",
        "demonstrate",
        "look at",
    )
    picked: list[str] = []
    for s in sents[:40]:
        low = s.lower()
        if any(k in low for k in keys) and len(s) < 220:
            picked.append(s.rstrip("."))
        if len(picked) >= n:
            break
    if len(picked) < 3:
        for s in sents[1:8]:
            if 40 < len(s) < 200:
                picked.append(s.rstrip("."))
            if len(picked) >= n:
                break
    return picked[:n]


def sectionize(sents: list[str]) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    current_title = "Core concepts from the lecture"
    bucket: list[str] = []
    title_triggers = (
        "now let us",
        "next we",
        "next let",
        "so now",
        "in this part",
        "moving on",
        "another important",
        "first let",
        "second",
        "third",
    )
    for s in sents:
        low = s.lower()
        if any(low.startswith(t) for t in title_triggers) and len(bucket) >= 3:
            sections.append((current_title, bucket))
            current_title = s[:70].rstrip(".") + ("…" if len(s) > 70 else "")
            bucket = [s]
        else:
            bucket.append(s)
        if len(bucket) >= 8:
            sections.append((current_title, bucket))
            current_title = "Continued"
            bucket = []
    if bucket:
        sections.append((current_title, bucket))
    return sections[:12]


def extract_tools(text: str) -> list[str]:
    found = sorted({m.group(0).strip() for m in TOOL_PATTERNS.finditer(text)}, key=str.lower)
    return found


def extract_commands(text: str) -> list[str]:
    cmds: list[str] = []
    for m in CMD_PATTERN.finditer(text):
        cmd = (m.group(1) or m.group(2) or "").strip()
        if cmd and cmd not in cmds:
            cmds.append(cmd)
    return cmds[:15]


def extract_terms(sents: list[str]) -> list[tuple[str, str]]:
    terms: list[tuple[str, str]] = []
    for s in sents:
        m = DEF_PATTERN.search(s)
        if m:
            term = m.group(1).strip()
            meaning = m.group(2).strip()
            if 3 < len(term) < 60:
                terms.append((term, meaning))
        if len(terms) >= 12:
            break
    return terms


def exam_bullets(sents: list[str]) -> list[str]:
    keys = (
        "important",
        "remember",
        "note that",
        "must",
        "always",
        "never",
        "difference between",
        "advantage",
        "disadvantage",
        "security",
        "attack",
        "defense",
        "vulnerability",
    )
    bullets: list[str] = []
    for s in sents:
        low = s.lower()
        if any(k in low for k in keys) and 30 < len(s) < 240:
            bullets.append(s.rstrip("."))
        if len(bullets) >= 8:
            break
    if len(bullets) < 4:
        bullets.extend(s.rstrip(".") for s in sents[-6:] if 30 < len(s) < 200)
    return bullets[:8]


def needs_mermaid(title: str, text: str) -> bool:
    keys = ("tcp", "osi", "arp", "mitm", "sql injection", "routing", "subnet", "handshake", "metasploit")
    blob = (title + " " + text).lower()
    return any(k in blob for k in keys)


def mermaid_for(title: str, text: str) -> str:
    low = (title + " " + text).lower()
    if "sql injection" in low or "authentication bypass" in low:
        return """```mermaid
sequenceDiagram
    participant U as User/Browser
    participant W as Web app
    participant D as Database
    U->>W: Malformed login input
    W->>D: Unsanitized query
    D-->>W: Auth bypass / data leak
    W-->>U: Unauthorized access
```"""
    if "arp" in low or "mitm" in low or "man-in-the-middle" in low:
        return """```mermaid
flowchart LR
    V[Victim] --> R[Router]
    A[Attacker poisons ARP cache]
    A --> V
    A --> R
    V --> A
    A --> R
```"""
    if "tcp" in low or "handshake" in low:
        return """```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    C->>S: SYN
    S->>C: SYN-ACK
    C->>S: ACK
    Note over C,S: Connection established
```"""
    if "routing" in low or "subnet" in low:
        return """```mermaid
flowchart TB
    P[Packet with destination IP]
    P --> M{Longest prefix match}
    M --> R1[Route 1]
    M --> R2[Route 2]
    M --> D[Local delivery / forward]
```"""
    return """```mermaid
flowchart LR
    R[Reconnaissance] --> S[Scanning]
    S --> E[Exploitation]
    E --> P[Post-exploitation]
    P --> Rep[Reporting]
```"""


def render_lecture(meta: dict, transcript_path: Path) -> str:
    lec = meta["lecture"]
    title = meta["title"]
    vid = meta["id"]
    slug = slugify(title)
    tstem = f"{lec:02d}-{slug}"
    text = fix_asr(load_transcript_text(transcript_path))
    sents = sentences(text)
    objectives = pick_objectives(sents)
    sections = sectionize(sents)
    tools = extract_tools(text)
    commands = extract_commands(text)
    terms = extract_terms(sents)
    bullets = exam_bullets(sents)

    lines = [
        f"# L{lec:02d}: {title}",
        "",
        f"**Transcript:** [{tstem}.md](../../transcripts/markdown/{tstem}.md)  ",
        f"**Video:** https://www.youtube.com/watch?v={vid}  ",
        f"**Week / theme:** {week_for(lec)}  ",
        f"**Instructor:** {INSTRUCTOR}",
        "",
        "## Learning objectives",
        "",
    ]
    for obj in objectives:
        lines.append(f"- {obj}.")
    lines.extend(["", "## What this lecture teaches", ""])

    for sec_title, sec_sents in sections:
        lines.append(f"### {sec_title}")
        lines.append("")
        for s in sec_sents:
            lines.append(s)
            lines.append("")
        if len(lines) > 500:
            break

    if needs_mermaid(title, text):
        lines.extend(["", mermaid_for(title, text), ""])

    if tools:
        lines.extend(["", "## Tools mentioned", ""])
        for t in tools:
            lines.append(f"- **{t}**")
        lines.append("")

    if commands:
        lines.extend(["", "## Commands / syntax from the lecture", ""])
        for c in commands:
            lines.append(f"- `{c}`")
        lines.append("")

    if terms:
        lines.extend(
            [
                "",
                "## Key terms",
                "",
                "| Term | Meaning in this lecture |",
                "|------|-------------------------|",
            ]
        )
        for term, meaning in terms:
            lines.append(f"| {term} | {meaning} |")
        lines.append("")

    lines.extend(["", "## Exam-oriented recap", ""])
    for b in bullets:
        lines.append(f"- {b}.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    playlist = json.loads(META_PATH.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    missing: list[int] = []
    for meta in playlist:
        lec = meta["lecture"]
        slug = slugify(meta["title"])
        tpath = TRANSCRIPTS / f"{lec:02d}-{slug}.md"
        if not tpath.exists():
            # fallback: any file starting with lecture number
            matches = list(TRANSCRIPTS.glob(f"{lec:02d}-*.md"))
            if not matches:
                missing.append(lec)
                continue
            tpath = matches[0]
        out_path = OUT / f"L{lec:02d}-{slug}.md"
        out_path.write_text(render_lecture(meta, tpath), encoding="utf-8")
        print("wrote", out_path.name)
    if missing:
        raise SystemExit(f"Missing transcripts for lectures: {missing}")
    print("done", len(playlist), "lectures")


if __name__ == "__main__":
    main()
