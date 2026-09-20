# notes-2 writing style

These notes are **transcript-grounded**. Every concept, case, formula, distinction, and example that the lecture actually teaches must appear. Do not write generic cybersecurity encyclopedia text. Do not skip Q&A teaching (definitions, formulas, blockchain, vishing, data owners, residual-risk corrections). Skip only platform logistics (assignment deadlines, certificate rules, how to download videos).

## File format

Write one markdown file per lecture at:

`courses/01-cyber-security-and-privacy/notes-2/lectures/TXX-slug.md`

Use this skeleton:

```markdown
# Lecture TXX: Title

**Playlist index:** XX  
**Transcript:** [filename](../../transcripts/markdown/filename.md)  
**Video:** https://www.youtube.com/watch?v=ID  
**Week / theme:** ...

## Learning objectives
- ...

## What this lecture actually teaches

### ...
(full coverage of every teaching beat, in original wording)

```mermaid
...
```

## Cases and examples from the lecture
- ...

## Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| ... | ... |

## Formulas / frameworks (if any)
...

## Distinctions the instructor insists on
- X is not Y because ...

## Exam-oriented recap
- ...
```

## Diagrams

Include mermaid wherever a framework, process, triad, formula relationship, policy hierarchy, or attack path is taught. Prefer `graph TB`, `flowchart LR`, or `sequenceDiagram`. Keep node labels short.

## Voice

Study notes, not a transcript dump. Short paragraphs, headings, tables. Quote a phrase only when the instructor’s wording is the definition.
