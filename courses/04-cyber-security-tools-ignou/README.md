# Cyber Security Tools — IGNOU / BAOU

**Course code:** `nou26_ge86`  
**Instructor:** Prof. Dr. Nilesh K. Modi  
**Institution:** IGNOU / Dr. Babasaheb Ambedkar Open University (BAOU)  
**Duration:** 12 weeks · 36 lectures (3 per week)  
**Format:** Tool-focused practical notes aligned with PGDCS-101 and PGDCS-103

## Overview

This course develops hands-on competence with industry-standard offensive and defensive security tools. Each lecture covers **purpose**, **step-by-step usage** (lab-safe), and **countermeasures** defenders apply in production environments.

All practical work must be performed only on **authorized lab systems** you own or have explicit written permission to test.

## Repository layout

| Path | Description |
|------|-------------|
| [`lecture-index.md`](lecture-index.md) | Full list of 36 lecture titles with week mapping |
| [`references.md`](references.md) | Textbooks, SLMs, and external resources |
| [`notes/`](notes/) | Per-lecture markdown + consolidated `vol-XX.md` (PDF source) |
| [`pdf/`](pdf/) | Printable volume PDFs (4 × 9 lectures) |
| [`notes-3/`](notes-3/) | Concept exam packs condensed from `pdf/` volumes |

Each notes volume includes a `.index.md` quick-reference and a consolidated `vol-XX.md` for PDF export.

## Concept exam notes (`notes-3/`)

Shorter concept packs for mid-sem style questions (what tools/topics *are* / what they *do*). Lab command dumps removed; full lecture topic coverage kept. Condensed from the course `pdf/` volumes (no notes-2 for this course). See [`notes-3/`](notes-3/).

| Volume | Lectures | PDF |
|--------|----------|-----|
| 01–04 | L01–L36 | [notes-3/pdf/](notes-3/pdf/) |

Rebuild: `python3 scripts/condense_notes3_ignou.py` → `./scripts/build-notes3-pdfs.sh ignou`

## 12-week schedule

| Week | Theme | Lectures | Primary tools |
|------|-------|----------|---------------|
| 1 | Introduction & security fundamentals | L1–L3 | Kali VM, Nmap, Netcat |
| 2 | Reconnaissance & network scanning | L4–L6 | Wireshark, Nmap, Kill Chain mapping |
| 3 | Firewalls & perimeter defense | L7–L9 | iptables, Windows Firewall, UFW |
| 4 | Wireless security | L10–L12 | Airodump-ng, Aircrack-ng, Nikto |
| 5 | Web scanning & proxy inspection | L13–L15 | OWASP ZAP, Nikto, Gobuster |
| 6 | Web application attacks | L16–L18 | sqlmap, ZAP, manual testing |
| 7 | Advanced web exploitation | L19–L21 | sqlmap, ZAP, Snort |
| 8 | IDS/IPS & vulnerability management | L22–L24 | Snort, Suricata, OpenVAS |
| 9 | Assurance & malware analysis | L25–L27 | policy frameworks, ClamAV, strings |
| 10 | E-commerce & payment security | L28–L30 | OpenSSL, testssl.sh, ZAP |
| 11 | Social engineering & credential attacks | L31–L33 | SET, John the Ripper, Hydra |
| 12 | Cyber law, synthesis & assessment | L34–L36 | legal frameworks, tool-chain review |

Week themes follow the 12-week cybersecurity progression used on [Class Central](https://www.classcentral.com/) listings (footprinting → scanning → enumeration → system attacks → web/mobile → wireless → IDS/firewalls → assessment).

## Video lectures

Recorded sessions are published on the **BAOU YouTube channel**: [scsbaou5615](https://www.youtube.com/@scsbaou5615)

Search the channel for **Cyber Security Tools** or course code **nou26_ge86**.

## Lab prerequisites

- Virtual machine host (VirtualBox / VMware / Hyper-V)
- Kali Linux or Parrot OS VM (attacker) + Ubuntu/Windows VM (target)
- Isolated lab network — **never** scan or attack production systems
- Minimum 8 GB RAM, 40 GB disk per VM

## Building PDFs

From the repository root:

```bash
./scripts/build-pdf.sh courses/04-cyber-security-tools-ignou vol-01.md
./scripts/build-all-pdfs.sh   # builds all vol-*.md files
```

Output appears in `courses/04-cyber-security-tools-ignou/pdf/`.

## Related BAOU / IGNOU courses

| Code | Title |
|------|-------|
| PGDCS-101 | Principles of Cyber Security |
| PGDCS-103 | Cyber Security Techniques |
| PGDCS-204 | Cyber Attacks and Counter Measures: User Perspective |

## License & ethics

Notes are for academic use under IGNOU/BAOU programmes. Unauthorized access to computer systems is illegal under the **IT Act, 2000** (India) and equivalent laws worldwide.
