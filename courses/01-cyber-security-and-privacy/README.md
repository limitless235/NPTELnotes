# Cyber Security and Privacy

**NPTEL Course ID:** 106106248  
**Course URL:** https://nptel.ac.in/courses/106106248  
**Instructor:** Prof. Saji K. Mathew, Department of Management Studies, IIT Madras  
**Duration:** 12 weeks · **40 lectures**  
**Level:** Undergraduate / Postgraduate (management and technology audiences)

## Overview

This course introduces cybersecurity and information privacy from an **organizational and managerial** perspective. It covers governance, risk, and compliance (GRC); contingency planning; security policy; risk management; industry attack patterns; security technologies; and the regulatory and economic dimensions of privacy—including GDPR and India's DPDP Act.

The course is designed for students who need a **wholesome understanding** of cyber risk in business contexts, not only technical implementation.

## Course structure

| Volume | Lectures | Topics |
|--------|----------|--------|
| [Vol. 01](notes/vol-01-lectures-01-10.md) | 1–10 | Introduction, foundations, CIA triad, GRC, contingency planning (start) |
| Vol. 02 | 11–20 | Contingency planning, cybersecurity policy, risk management, industry perspective |
| Vol. 03 | 21–30 | Industry perspective, security technologies, privacy foundations, privacy regulation |
| Vol. 04 | 31–40 | GDPR, Indian privacy (DPDP, Aadhaar), privacy economics, strategy and safety |

## Study materials in this folder

| File | Description |
|------|-------------|
| [lecture-index.md](lecture-index.md) | All 40 lectures with titles and YouTube links |
| [references.md](references.md) | Curated references for GRC, privacy, GDPR, DPDP |
| [notes/vol-01-lectures-01-10.md](notes/vol-01-lectures-01-10.md) | Detailed notes, Lectures 1–10 |
| [notes/vol-02-lectures-11-20.md](notes/vol-02-lectures-11-20.md) | Detailed notes, Lectures 11–20 |
| [diagrams/cia-triad.md](diagrams/cia-triad.md) | Mermaid CIA triad diagram |
| [transcripts/](transcripts/) | Per-video cleaned YouTube transcripts (markdown + PDF) |

## Weekly syllabus (NPTEL)

| Week | Topics |
|------|--------|
| 1 | Introduction; confidentiality, integrity, availability |
| 2 | Foundations; CIA triangle; case studies (e.g., Target data breach) |
| 3 | Security management; GRC framework; security standards |
| 4 | Contingency planning; control strategies; cryptography (guest) |
| 5 | Cybersecurity policy (ESSP, ISSP, SYSSP) |
| 6 | Risk management: identification, assessment, control |
| 7 | Industry perspective: defense technologies, attacks, exploits |
| 8 | Cybersecurity technologies: access control, encryption, standards |
| 9 | Foundations of privacy: measurement, theories |
| 10 | Privacy regulation: anonymity, breach notification |
| 11 | European privacy (GDPR); Indian privacy (DPDP, Aadhaar) |
| 12 | Privacy economics, strategy, and safety trade-offs |

## Prerequisites

A core course in Management Information Systems is desirable but not mandatory.

## Industry relevance

IT services, AI/blockchain startups, Industry 4.0, autonomous systems, and any organization handling personal or operational data.

## Building PDFs

From the repository root:

```bash
./scripts/build-pdf.sh courses/01-cyber-security-and-privacy vol-01-lectures-01-10.md
./scripts/build-pdf.sh courses/01-cyber-security-and-privacy vol-02-lectures-11-20.md
```

## Playlist

Full NPTEL playlist: https://www.youtube.com/playlist?list=PLyqSpQzTE6M-jkJEzbS5oHJUp2GWPsq6e
