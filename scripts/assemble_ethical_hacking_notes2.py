#!/usr/bin/env python3
"""Concatenate Ethical Hacking notes-2 lecture files into six volume markdown files."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "courses" / "02-ethical-hacking" / "notes-2"
LECTURES = NOTES / "lectures"

VOLUMES = [
    {
        "file": "vol-01.md",
        "title": "Volume 01 — Networking Foundations (L01–L10)",
        "blurb": "Introduction to ethical hacking, OSI/TCP-IP, IP addressing, TCP/UDP, subnetting.",
        "range": range(1, 11),
    },
    {
        "file": "vol-02.md",
        "title": "Volume 02 — Routing, Recon & Nessus (L11–L20)",
        "blurb": "Routing protocols, IPv6, live OSINT/Nmap demos, Nessus vulnerability scanning.",
        "range": range(11, 21),
    },
    {
        "file": "vol-03.md",
        "title": "Volume 03 — Metasploit, MITM & Crypto I (L21–L30)",
        "blurb": "Metasploit exploitation, social engineering, ARP/MITM, cryptography foundations.",
        "range": range(21, 31),
    },
    {
        "file": "vol-04.md",
        "title": "Volume 04 — Hash, PKI & Network Attacks (L31–L40)",
        "blurb": "Hash functions, digital signatures, steganography, biometrics, DNS/email security.",
        "range": range(31, 41),
    },
    {
        "file": "vol-05.md",
        "title": "Volume 05 — System Attacks & Hardware Security (L41–L50)",
        "blurb": "Password cracking, phishing, malware, Wi-Fi, DoS, side channels, PUF, hardware trojans.",
        "range": range(41, 51),
    },
    {
        "file": "vol-06.md",
        "title": "Volume 06 — Web Vulns, Nmap & Wireshark (L51–L62)",
        "blurb": "Web app scanning, SQLi, XSS, file upload, Nmap deep-dive, Wireshark, course summary.",
        "range": range(51, 63),
    },
]


def lecture_files() -> dict[int, Path]:
    out: dict[int, Path] = {}
    for path in sorted(LECTURES.glob("L*.md")):
        num = int(path.name[1:3])
        out[num] = path
    return out


def main() -> None:
    files = lecture_files()
    missing = [n for vol in VOLUMES for n in vol["range"] if n not in files]
    if missing:
        raise SystemExit(f"Missing lecture files: {missing}")

    for vol in VOLUMES:
        parts = [
            f"# {vol['title']}",
            "",
            "**Course:** NPTEL Ethical Hacking (106105217) · **Instructor:** Prof. Indranil Sengupta, IIT Kharagpur",
            "",
            f"**Series:** notes-2 (transcript-grounded) — {vol['blurb']}",
            "",
            "Study notes derived from YouTube/Digimat lecture captions. For authorized lab use and exam preparation only.",
            "",
            "---",
            "",
        ]
        for n in vol["range"]:
            parts.append(files[n].read_text(encoding="utf-8").strip())
            parts.append("\n---\n")
        (NOTES / vol["file"]).write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
        print("wrote", vol["file"])


if __name__ == "__main__":
    main()
