#!/usr/bin/env python3
"""Assemble notes-2 lecture files into volume markdown for PDF export."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEC = ROOT / "courses/01-cyber-security-and-privacy/notes-2/lectures"
OUT = ROOT / "courses/01-cyber-security-and-privacy/notes-2"

VOLUMES = [
    (
        "vol-01.md",
        "Volume 01 — Introduction and Foundations",
        "Course welcome, introduction parts 1–3, CIA and Target case",
        [
            "T01-course-welcome.md",
            "T48-introduction-part-01.md",
            "T03-introduction-part-02.md",
            "T04-introduction-part-03.md",
            "T05-foundations-part-01.md",
            "T06-foundations-part-02.md",
            "T07-foundations-part-03.md",
        ],
    ),
    (
        "vol-02.md",
        "Volume 02 — GRC and Contingency Planning",
        "Governance, risk and compliance; IR / DR / BCP; live Q&A",
        [
            "T08-grc-part-01.md",
            "T09-grc-part-02.md",
            "T10-grc-part-03.md",
            "T11-contingency-part-01.md",
            "T13-contingency-part-02.md",
            "T12-contingency-part-03.md",
            "T14-live-session-contingency.md",
        ],
    ),
    (
        "vol-03.md",
        "Volume 03 — Policy and Risk Management",
        "EISP / ISSP / SysSP; residual risk; TVA worksheet",
        [
            "T15-policy-part-01.md",
            "T16-policy-part-02.md",
            "T17-policy-part-03.md",
            "T18-live-session-policy.md",
            "T19-risk-part-01.md",
            "T20-risk-part-02.md",
            "T21-risk-part-03.md",
        ],
    ),
    (
        "vol-04.md",
        "Volume 04 — Industry, Technologies, and Privacy Foundations",
        "Industry attacks; crypto and access control; privacy theories",
        [
            "T22-industry-part-01.md",
            "T23-industry-part-02.md",
            "T24-live-session-risk-tech.md",
            "T25-technologies-part-01.md",
            "T26-technologies-part-02.md",
            "T27-privacy-foundations-part-01.md",
            "T28-privacy-foundations-part-02.md",
            "T29-privacy-foundations-part-03.md",
        ],
    ),
    (
        "vol-05.md",
        "Volume 05 — Regulation, Economics, Strategy, and Capstone",
        "GDPR, DPDP/Aadhaar, privacy economics, strategy/safety, live capstone",
        [
            "T30-privacy-regulation-part-01.md",
            "T31-privacy-regulation-part-02.md",
            "T32-privacy-regulation-part-03.md",
            "T38-gdpr-part-01.md",
            "T33-gdpr-part-02.md",
            "T34-gdpr-part-03.md",
            "T35-india-privacy-part-01.md",
            "T36-india-privacy-part-02.md",
            "T37-india-privacy-part-03.md",
            "T39-privacy-economics-part-01.md",
            "T40-privacy-economics-part-02.md",
            "T41-privacy-economics-part-03.md",
            "T42-strategy-safety-part-01.md",
            "T43-strategy-safety-part-02.md",
            "T44-strategy-safety-part-03.md",
            "T45-live-capstone-a.md",
            "T46-live-capstone-b.md",
        ],
    ),
]


def rewrite_links(text: str) -> str:
    return text.replace("../../transcripts/markdown/", "../transcripts/markdown/")


def main() -> None:
    for filename, title, blurb, parts in VOLUMES:
        chunks = [
            f"# Cyber Security and Privacy — {title}\n\n"
            f"**Course:** NPTEL 106106248 · **Instructor:** Prof. Saji K. Mathew, IIT Madras  \n"
            f"**Series:** notes-2 (transcript-grounded)  \n"
            f"**Scope:** {blurb}\n\n"
            "These notes follow the lecture videos and public captions. "
            "They are study material, not official NPTEL transcripts.\n\n---\n"
        ]
        for part in parts:
            body = (LEC / part).read_text(encoding="utf-8")
            chunks.append(rewrite_links(body).rstrip() + "\n\n---\n")
        out = OUT / filename
        out.write_text("\n".join(chunks), encoding="utf-8")
        print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
