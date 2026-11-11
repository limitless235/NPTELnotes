# final pdf — combined notes-3 by subject

One printable PDF per course, concatenating every notes-3 volume **in order** with no content removed.

| File | Source volumes |
|------|----------------|
| `01-cyber-security-and-privacy-notes-3.pdf` | `courses/01-…/notes-3/pdf/vol-01…05` |
| `02-ethical-hacking-notes-3.pdf` | `courses/02-…/notes-3/pdf/vol-01…06` |
| `03-generative-ai-llms-notes-3.pdf` | `courses/03-…/notes-3/pdf/vol-01…06` (full course) |
| `03-generative-ai-llms-exam-kept-weeks.pdf` | **Exam map only** — weeks 1,2,3,5,7,9,10,11 (drops 4,6,8,12) |
| `04-cyber-security-tools-ignou-notes-3.pdf` | `courses/04-…/notes-3/pdf/vol-01…04` |
| `05-information-security-cec-notes-3.pdf` | `courses/05-…/notes-3/pdf/vol-01…04` |
| `05-information-security-cec-numericals.pdf` | **Worked numericals** restored (TCP window, CIDR, hex dump, etc.) |

## Info Sec numericals

Concept notes-3 dropped step-by-step calculations. Rebuild the companion pack:

```bash
pandoc courses/05-information-security-cec/notes-3/numericals.md \
  -o "final pdf/05-information-security-cec-numericals.pdf" \
  --pdf-engine=xelatex -V mainfont="DejaVu Serif" --toc
```

Markdown source: `courses/05-information-security-cec/notes-3/numericals.md`

## GenAI exam PDF

Rebuild the filtered exam pack (does not modify notes-3 volumes):

```bash
python3 scripts/build_genai_exam_final_pdf.py
```

Markdown source: `courses/03-generative-ai-llms/notes-3/exam-syllabus-kept-weeks.md`

## Full combined rebuild

```bash
python3 scripts/combine_notes3_final_pdfs.py
```
