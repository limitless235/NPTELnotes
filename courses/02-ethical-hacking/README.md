# Ethical Hacking — NPTEL Notes

| Field | Value |
|-------|-------|
| **Course ID** | noc26_cs157 / NPT_4125 / 106105217 |
| **Instructor** | Prof. Indranil Sengupta, IIT Kharagpur |
| **Lectures** | 62 |
| **Prerequisites** | Basic programming and networking |

## About

Concise, tool-focused study notes for the NPTEL *Ethical Hacking* course. Each lecture covers key concepts, offensive techniques, defensive countermeasures, and exam-ready bullets.

## Transcript-grounded notes (`notes-2/`)

Six printable PDF volumes built from YouTube/Digimat lecture captions (62 lectures). Markdown sources stay local; only PDFs are versioned.

| Volume | Lectures | PDF |
|--------|----------|-----|
| 01 | L01–L10 | [notes-2/pdf/vol-01.pdf](notes-2/pdf/vol-01.pdf) |
| 02 | L11–L20 | [notes-2/pdf/vol-02.pdf](notes-2/pdf/vol-02.pdf) |
| 03 | L21–L30 | [notes-2/pdf/vol-03.pdf](notes-2/pdf/vol-03.pdf) |
| 04 | L31–L40 | [notes-2/pdf/vol-04.pdf](notes-2/pdf/vol-04.pdf) |
| 05 | L41–L50 | [notes-2/pdf/vol-05.pdf](notes-2/pdf/vol-05.pdf) |
| 06 | L51–L62 | [notes-2/pdf/vol-06.pdf](notes-2/pdf/vol-06.pdf) |
| **Midsem** | **Weeks 1–5 (full syllabus)** | [notes-2/pdf/midsem-week1-5.pdf](notes-2/pdf/midsem-week1-5.pdf) |

Rebuild: `python3 scripts/scrape_ethical_hacking_transcripts.py` → `python3 scripts/generate_ethical_hacking_notes2.py` → `./scripts/build-notes2-pdfs.sh ethical-hacking`

## Structure

```
02-ethical-hacking/
├── README.md              ← this file
├── lecture-index.md       ← all 62 lecture titles with links
├── references.md          ← textbooks and tool documentation
├── notes-2/pdf/           ← transcript-grounded PDF volumes (6)
└── notes/
    ├── vol-01.md            ← Lectures 1–10  (Networking foundations)
    ├── vol-01.index.md
    ├── vol-02.md            ← Lectures 11–20 (Routing, recon, Nessus)
    ├── vol-02.index.md
    ├── vol-03.md            ← Lectures 21–30 (Metasploit, MITM, crypto)
    ├── vol-03.index.md
    ├── vol-04.md            ← Lectures 31–40 (Hash, PKI, network attacks)
    ├── vol-04.index.md
    ├── vol-05.md            ← Lectures 41–50 (Passwords, malware, hardware)
    ├── vol-05.index.md
    ├── vol-06.md            ← Lectures 51–62 (Web vulns, Nmap, Wireshark)
    └── vol-06.index.md
```

## Volume Map

| Volume | Lectures | Topics |
|--------|----------|--------|
| [vol-01](notes/vol-01.md) | 1–10 | Ethical hacking intro, OSI/TCP-IP, IP addressing, TCP/UDP, subnetting |
| [vol-02](notes/vol-02.md) | 11–20 | Routing protocols, IPv6, live demos, Nessus |
| [vol-03](notes/vol-03.md) | 21–30 | Metasploit, social engineering, MITM/ARP, cryptography |
| [vol-04](notes/vol-04.md) | 31–40 | Hash functions, digital signatures, steganography, network attacks |
| [vol-05](notes/vol-05.md) | 41–50 | Password cracking, phishing, Wi-Fi, DoS, hardware security |
| [vol-06](notes/vol-06.md) | 51–62 | Web app scanning, SQLi, XSS, Nmap deep-dive, Wireshark |

## How to Use

1. Start with [lecture-index.md](lecture-index.md) to locate a lecture.
2. Read the corresponding volume; each lecture has **Concepts → Tools → Attack Steps → Defenses → Exam Bullets**.
3. Mermaid diagrams appear in volumes covering TCP/IP (vol-01), ARP spoofing (vol-03), and SQL injection (vol-06).
4. Cross-reference [references.md](references.md) for textbook depth.

## Legal Notice

These notes document security techniques for **authorized** penetration testing and academic study only. Unauthorized access to computer systems is illegal under the IT Act 2000 (India) and equivalent laws worldwide.
