# NPTELnotes

A curated study-notes repository for **five NPTEL / SWAYAM courses** in cybersecurity, ethical hacking, and generative AI. Every lecture in each course is covered with structured markdown notes, companion index files, reference links, and printable PDF volumes.

## What this project is

NPTELnotes is a self-contained reference library — not a video mirror or course platform. It organizes publicly available lecture material into:

- **Lecture-by-lecture notes** with key concepts, definitions, diagrams, and takeaways
- **Volume PDFs** grouped so lectures divide evenly across the full course (e.g. 36 lectures → 4 PDFs × 9 lectures)
- **Index files** beside each PDF volume for quick navigation
- **Reference lists** with standards, tools, papers, and official documentation

All video links point to public NPTEL, SWAYAM, or YouTube sources. No registration is required.

## At a glance

| | |
|---|---|
| **Courses** | 5 |
| **Total lectures** | 210 |
| **PDF volumes** | 22 |
| **Formats** | Markdown (source) + PDF (export) |

## Courses

| # | Course | Lectures | PDF split | Folder |
|---|--------|----------|-----------|--------|
| 1 | [Cyber Security and Privacy](courses/01-cyber-security-and-privacy/) | 40 | 4 × 10 | `courses/01-cyber-security-and-privacy/` |
| 2 | [Ethical Hacking](courses/02-ethical-hacking/) | 62 | 5 × 10 + 1 × 12 | `courses/02-ethical-hacking/` |
| 3 | [Generative AI & LLMs](courses/03-generative-ai-llms/) | 36 | 4 × 9 | `courses/03-generative-ai-llms/` |
| 4 | [Cyber Security Tools (IGNOU)](courses/04-cyber-security-tools-ignou/) | 36 | 4 × 9 | `courses/04-cyber-security-tools-ignou/` |
| 5 | [Information Security (CEC)](courses/05-information-security-cec/) | 36 | 4 × 9 | `courses/05-information-security-cec/` |

### Official course links

| Course | URL |
|--------|-----|
| Cyber Security and Privacy | https://nptel.ac.in/courses/106106248 |
| Ethical Hacking (NPT_4125) | https://onlinecourses.nptel.ac.in/e-learning/preview/noc26_cs157 |
| Generative AI & LLMs (NPT_4121) | https://onlinecourses.nptel.ac.in/e-learning/preview/noc26_cs95 |
| Cyber Security Tools | https://onlinecourses.swayam2.ac.in/e-learning/preview/nou26_ge86 |
| Information Security | https://onlinecourses.swayam2.ac.in/e-learning/preview/cec26_cs13 |

## Project structure

```
NPTELnotes/
├── README.md                          # This file — project overview
├── courses/                           # One folder per course (numbered 01–05)
│   ├── 01-cyber-security-and-privacy/
│   │   ├── README.md                  # Course overview, volume map, study tips
│   │   ├── lecture-index.md           # All lectures with titles + video links
│   │   ├── references.md              # Curated external references
│   │   ├── diagrams/                  # Standalone diagram source files (optional)
│   │   ├── notes/
│   │   │   ├── vol-01-lectures-01-10.md          # Consolidated volume notes (PDF source)
│   │   │   ├── vol-01-lectures-01-10.index.md    # Companion index for that PDF
│   │   │   ├── vol-02-lectures-11-20.md
│   │   │   ├── vol-02-lectures-11-20.index.md
│   │   │   └── ...
│   │   └── pdf/
│   │       ├── vol-01-lectures-01-10.pdf         # Generated printable PDF
│   │       └── ...
│   │
│   ├── 02-ethical-hacking/            # 62 lectures · 6 PDF volumes
│   │   ├── README.md
│   │   ├── lecture-index.md
│   │   ├── references.md
│   │   ├── notes/
│   │   │   ├── vol-01.md … vol-06.md
│   │   │   └── vol-01.index.md … vol-06.index.md
│   │   └── pdf/
│   │       └── vol-01.pdf … vol-06.pdf
│   │
│   ├── 03-generative-ai-llms/         # 36 lecture notes + 64 video transcript PDFs
│   ├── 04-cyber-security-tools-ignou/ # 36 lectures · 4 PDF volumes
│   │   └── notes/
│   │       ├── vol-01.md … vol-04.md          # Consolidated volumes
│   │       ├── vol-01/ … vol-04/              # Per-lecture source files
│   │       │   ├── L01-….md
│   │       │   └── .index.md
│   │       └── vol-01.index.md … vol-04.index.md
│   │
│   └── 05-information-security-cec/   # 36 lectures · 4 PDF volumes
│
└── scripts/
    ├── build-pdf.sh                   # Build one volume: mermaid preprocess + pandoc + XeLaTeX
    ├── build-all-pdfs.sh              # Rebuild all 22 PDF volumes
    ├── preprocess-mermaid.py          # Render ```mermaid blocks to PNG for PDF export
    ├── convert-math-for-github.py     # Convert LaTeX math delimiters for GitHub preview
    ├── generate-cst-lectures.py       # Helper used to scaffold IGNOU lecture files
    ├── scrape-genai-transcripts.py    # Fetch YouTube captions + build per-video PDFs
    ├── assemble-notes2-volumes.py     # Concatenate notes-2 lectures into print volumes
    └── build-notes2-pdfs.sh           # Build transcript-grounded GenAI notes PDFs
```

### File conventions

| File | Purpose |
|------|---------|
| `README.md` (course root) | Course description, instructor info, volume breakdown |
| `lecture-index.md` | Master list of every lecture with public video URLs |
| `references.md` | Standards, textbooks, tools, and further reading |
| `notes/vol-*.md` | Full notes for one PDF volume — this is the PDF source |
| `notes/vol-*.index.md` | Table of contents + lecture links for that volume |
| `pdf/vol-*.pdf` | Generated output — rebuild from markdown with the scripts |
| `diagrams/*.md` | Optional diagram definitions (mermaid / ASCII) |

## How to use

1. **Pick a course** from the table above and open its `README.md`.
2. **Find a lecture** in `lecture-index.md` and watch the linked video.
3. **Read the notes** in the matching volume under `notes/`, or open the PDF in `pdf/`.
4. **Use the index** (`vol-*.index.md`) to jump to a specific lecture within a volume.
5. **Follow references** in `references.md` for deeper reading.

## Note depth by course

| Course | Style | Focus |
|--------|-------|-------|
| Cyber Security and Privacy | Comprehensive | GRC, contingency planning, GDPR, DPDP |
| Ethical Hacking | Concise, tool-focused | Recon, exploitation, post-exploitation, reporting |
| Generative AI & LLMs | Comprehensive | VAEs, GANs, diffusion, transformers, RAG |
| Cyber Security Tools (IGNOU) | Concise, hands-on | Nmap, Wireshark, ZAP, Snort, malware analysis |
| Information Security (CEC) | Comprehensive | Cryptography, protocols, IAM, assurance |

## Building PDFs

Markdown is the source of truth. PDFs are generated with [Pandoc](https://pandoc.org/), XeLaTeX, and [mermaid-cli](https://github.com/mermaid-js/mermaid-cli) (diagram preprocessing).

```bash
# Install system dependencies (Debian/Ubuntu)
sudo apt-get install -y pandoc texlive-xetex

# Install mermaid-cli (one-time, for diagram rendering in PDFs)
cd scripts && npm install && cd ..

# Build all 22 PDF volumes
./scripts/build-all-pdfs.sh

# Build a single volume
./scripts/build-pdf.sh courses/03-generative-ai-llms vol-01.md
```

Output is written to each course's `pdf/` directory. Mermaid code blocks in markdown are rendered to PNG images during the PDF build (`scripts/preprocess-mermaid.py`). In GitHub markdown preview, mermaid blocks render natively.

## Contributing

Notes are organized for personal study. If you spot an error or want to add a reference, open an issue or PR on the relevant course folder.

## License

Notes are for personal study. Course content and video rights belong to NPTEL, SWAYAM, IGNOU, CEC, and their respective institutions.
