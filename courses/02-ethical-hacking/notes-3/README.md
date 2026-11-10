# notes-3 — concept exam notes (Ethical Hacking)

Condensed from the transcript-heavy **notes-2** PDFs / concept **notes/** for mid-sem style exams.

**Focus:** what each topic *is* and what it *does* — definitions, comparisons, one-line defenses, exam lines.  
**Dropped:** long command recipes, lab click-paths, plugin install stats, and other detail that does not help “explain the concept” questions.

## Volumes

| Volume | Lectures | Markdown | PDF |
|--------|----------|----------|-----|
| 01 Networking Foundations | L01–L10 | [vol-01.md](vol-01.md) | [pdf/vol-01.pdf](pdf/vol-01.pdf) |
| 02 Routing, Recon & Nessus | L11–L20 | [vol-02.md](vol-02.md) | [pdf/vol-02.pdf](pdf/vol-02.pdf) |
| 03 Metasploit, MITM & Crypto | L21–L30 | [vol-03.md](vol-03.md) | [pdf/vol-03.pdf](pdf/vol-03.pdf) |
| 04 Hash, PKI & Network Attacks | L31–L40 | [vol-04.md](vol-04.md) | [pdf/vol-04.pdf](pdf/vol-04.pdf) |
| 05 System & Hardware Security | L41–L50 | [vol-05.md](vol-05.md) | [pdf/vol-05.pdf](pdf/vol-05.pdf) |
| 06 Web, Nmap & Wireshark | L51–L62 | [vol-06.md](vol-06.md) | [pdf/vol-06.pdf](pdf/vol-06.pdf) |

## Rebuild

```bash
python3 scripts/condense_notes3_ethical_hacking.py
./scripts/build-notes3-pdfs.sh ethical-hacking
```

Study notes for NPTEL Ethical Hacking. Offensive techniques are for authorized labs and exams only.
