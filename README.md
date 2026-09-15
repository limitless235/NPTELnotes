# NPTELnotes

Structured study notes for five NPTEL / SWAYAM cybersecurity and AI courses. Each course has its own folder with lecture-by-lecture markdown notes, companion index files, reference links, and PDF volumes grouped evenly across the full lecture count.

## Courses

| # | Course | Lectures | PDF volumes | Folder |
|---|--------|----------|-------------|--------|
| 1 | [Cyber Security and Privacy](courses/01-cyber-security-and-privacy/) | 40 | 4 × 10 | `courses/01-cyber-security-and-privacy/` |
| 2 | [Ethical Hacking](courses/02-ethical-hacking/) | 62 | 5 × 10 + 1 × 12 | `courses/02-ethical-hacking/` |
| 3 | [Fundamentals of Generative AI and Large Language Models](courses/03-generative-ai-llms/) | 36 | 4 × 9 | `courses/03-generative-ai-llms/` |
| 4 | [Cyber Security, Tools, Techniques and Counter Measures](courses/04-cyber-security-tools-ignou/) | 36 | 4 × 9 | `courses/04-cyber-security-tools-ignou/` |
| 5 | [Information Security](courses/05-information-security-cec/) | 36 | 4 × 9 | `courses/05-information-security-cec/` |

### Official course links

1. **Cyber Security and Privacy** — https://nptel.ac.in/courses/106106248
2. **Ethical Hacking** (NPT_4125) — https://onlinecourses.nptel.ac.in/e-learning/preview/noc26_cs157
3. **Fundamentals of Generative AI and LLMs** (NPT_4121) — https://onlinecourses.nptel.ac.in/e-learning/preview/noc26_cs95
4. **Cyber Security, Tools, Techniques and Counter Measures** — https://onlinecourses.swayam2.ac.in/e-learning/preview/nou26_ge86
5. **Information Security** — https://onlinecourses.swayam2.ac.in/e-learning/preview/cec26_cs13

## Repository layout

```
courses/
  01-cyber-security-and-privacy/
    README.md              # Course overview
    lecture-index.md       # All lectures with video links
    references.md          # Curated references
    notes/                 # Volume markdown + .index.md companions
    pdf/                   # Generated PDF volumes
  02-ethical-hacking/
  03-generative-ai-llms/
  04-cyber-security-tools-ignou/
  05-information-security-cec/
scripts/
  build-pdf.sh             # Build one volume PDF
  build-all-pdfs.sh        # Build all course PDFs
```

Each volume markdown file (`notes/vol-*.md`) has a companion index (`notes/vol-*.index.md`) listing lectures, topics, and links to the consolidated PDF.

## Building PDFs

**Requirements:** [Pandoc](https://pandoc.org/) and a LaTeX engine (XeLaTeX recommended).

```bash
# Install dependencies (Debian/Ubuntu)
sudo apt-get install -y pandoc texlive-xetex

# Build all PDFs
./scripts/build-all-pdfs.sh

# Build a single volume
./scripts/build-pdf.sh courses/03-generative-ai-llms vol-01.md
```

PDFs are written to each course's `pdf/` directory.

## Note depth

| Course | Style |
|--------|-------|
| Cyber Security and Privacy | Comprehensive — governance, risk, privacy regulation |
| Ethical Hacking | Concise, tool- and technique-focused |
| Generative AI & LLMs | Comprehensive — math, architectures, LLM pipelines |
| Cyber Security Tools (IGNOU) | Concise, hands-on tool walkthroughs |
| Information Security (CEC) | Comprehensive — cryptography, protocols, assurance |

## Video sources

Notes reference publicly available NPTEL, SWAYAM, and YouTube lecture videos. No course registration is required to access the linked materials.

## License

Notes are for personal study. Course content and video rights belong to NPTEL, SWAYAM, and respective institutions.
