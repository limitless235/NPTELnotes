# Ethical Hacking — NPTEL Notes

| Field | Value |
|-------|-------|
| **Course ID** | noc26_cs157 / NPT_4125 / 106105217 |
| **Instructor** | Prof. Indranil Sengupta, IIT Kharagpur |
| **Lectures** | 62 |
| **Prerequisites** | Basic programming and networking |

## About

Concise, tool-focused study notes for the NPTEL *Ethical Hacking* course. Each lecture covers key concepts, offensive techniques, defensive countermeasures, and exam-ready bullets.

## Structure

```
02-ethical-hacking/
├── README.md              ← this file
├── lecture-index.md       ← all 62 lecture titles with links
├── references.md          ← textbooks and tool documentation
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
