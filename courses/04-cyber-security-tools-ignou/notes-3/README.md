# notes-3 — concept exam notes (Cyber Security Tools · IGNOU)

Condensed from the course **`pdf/`** volume set (markdown source: `notes/vol-*.md`). This course has no notes-2 series.

**Focus:** what each tool/topic *is* and what it *does* — definitions, comparison tables, frameworks, one-line defenses, exam lines.  
**Dropped:** command recipes, install/UI click-paths, lab IP walkthroughs, and payload dumps.

## Volumes

| Volume | Lectures | Markdown | PDF |
|--------|----------|----------|-----|
| 01 Essentials, APT/Kill Chain, Firewalls | L01–L09 | [vol-01.md](vol-01.md) | [pdf/vol-01.pdf](pdf/vol-01.pdf) |
| 02 Wireless, Web Scanning, App Inspection | L10–L18 | [vol-02.md](vol-02.md) | [pdf/vol-02.pdf](pdf/vol-02.pdf) |
| 03 Web Attacks, IDS, Assurance, Malware | L19–L27 | [vol-03.md](vol-03.md) | [pdf/vol-03.pdf](pdf/vol-03.pdf) |
| 04 E-Commerce, Social Engineering, Cyber Law | L28–L36 | [vol-04.md](vol-04.md) | [pdf/vol-04.pdf](pdf/vol-04.pdf) |

## Rebuild

```bash
python3 scripts/condense_notes3_ignou.py
./scripts/build-notes3-pdfs.sh ignou
```

Study notes for IGNOU/BAOU Cyber Security Tools (nou26_ge86). Offensive techniques are for authorized labs and exams only.
