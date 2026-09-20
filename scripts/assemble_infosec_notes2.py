#!/usr/bin/env python3
"""Concatenate notes-2 lecture files into four volume markdown files."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "courses" / "05-information-security-cec" / "notes-2"
LECTURES = NOTES / "lectures"

VOLUMES = [
    {
        "file": "vol-01.md",
        "title": "Volume 01 — Ethics, Network Models, and TCP/IP",
        "blurb": "Introductory video and modules M00–M11: information-security ethics, network security, OSI/TCP-IP models, protocol stack, TCP, data-link and MAC, IP addressing, and TCP connection management.",
        "range": range(0, 12),
    },
    {
        "file": "vol-02.md",
        "title": "Volume 02 — Addressing, Applications, and Ethernet",
        "blurb": "Modules M12–M23: IPv4/IPv6, UDP, IPsec, topologies, animated-cursor vulnerability, email and WWW security, mobile code, transmission media, and Ethernet.",
        "range": range(12, 24),
    },
    {
        "file": "vol-03.md",
        "title": "Volume 03 — High-Speed Links, Wireless, and VPN",
        "blurb": "Modules M24–M35: Ethernet security, Gigabit/10-Gigabit Ethernet, ISDN, SCTP, ATM, wireless LANs, Wi-Fi security, Bluetooth, VPN, and WiMAX.",
        "range": range(24, 36),
    },
    {
        "file": "vol-04.md",
        "title": "Volume 04 — Mobility, Cloud, Cellular, VoIP, and DDoS",
        "blurb": "Modules M36–M47: Mobile IP, cloud architecture and security, GSM, MANET, 3G/4G/5G, VoIP, and DDoS attacks and defenses.",
        "range": range(36, 48),
    },
]


def lecture_files() -> dict[int, Path]:
    out: dict[int, Path] = {}
    for path in sorted(LECTURES.glob("M*.md")):
        num = int(path.name[1:3])
        out[num] = path
    return out


def main() -> None:
    files = lecture_files()
    missing = [n for vol in VOLUMES for n in vol["range"] if n not in files]
    if missing:
        raise SystemExit(f"Missing lecture files for modules: {missing}")

    for vol in VOLUMES:
        parts = [
            f"# {vol['title']}",
            "",
            "**Course:** CEC / SWAYAM Information Security · **Coordinator:** Dr. Maninder Singh, Thapar Institute",
            "",
            vol["blurb"],
            "",
            "These notes are grounded in the official YouTube lecture transcripts. They are study material, not an official CEC publication.",
            "",
            "---",
            "",
        ]
        for n in vol["range"]:
            body = files[n].read_text(encoding="utf-8").strip() + "\n"
            parts.append(body)
            parts.append("\n---\n")
        (NOTES / vol["file"]).write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
        print("wrote", vol["file"])


if __name__ == "__main__":
    main()
