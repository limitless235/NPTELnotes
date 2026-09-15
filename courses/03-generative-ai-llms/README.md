# Fundamentals of Generative AI and LLMs

**Course code:** `noc26_cs95` / `NPT_4121`  
**Platform:** NPTEL / SWAYAM  
**Institution:** Indian Institute of Science (IISc), Bangalore  
**Instructors:** Prof. Sriram Ganapathy, Prof. Ashwini Kodipalli, Prof. Baishali Garai

## Overview

This course develops the **mathematical and algorithmic foundations** of modern generative artificial intelligence—from deep learning prerequisites through variational autoencoders, GANs, diffusion models, transformers, and large language models. The material is organized as **36 lectures** (3 per week × 12 weeks), aligned with the official NPTEL syllabus. Weeks 1–9 correspond to approximately **58 official NPTEL video lectures**; this repository consolidates that content into a structured lecture sequence with expanded derivations and diagrams.

## Learning outcomes

By the end of this course, you should be able to:

1. Explain generative modeling as learning and sampling from probability distributions.
2. Derive and optimize the ELBO for variational autoencoders.
3. Formulate GAN training as a minimax game and analyze failure modes.
4. Describe forward and reverse diffusion processes and DDPM training.
5. Implement self-attention and understand the transformer architecture.
6. Design retrieval-augmented generation (RAG) pipelines for grounded LLM applications.
7. Evaluate multimodal models and articulate ethical risks in generative AI deployment.

## Prerequisites

- Linear algebra (vectors, matrices, eigendecomposition)
- Probability and statistics (Bayes' rule, expectation, KL divergence)
- Multivariable calculus (gradients, chain rule)
- Basic deep learning (feedforward networks, backpropagation, CNNs)

## Repository structure

```
03-generative-ai-llms/
├── README.md              # This file
├── references.md          # Textbooks and papers
├── lecture-index.md       # All 36 lectures with NPTEL mapping
└── notes/
    ├── vol-01.md          # L01–L09: DL foundations, autoencoders, VAE
    ├── vol-01.index.md
    ├── vol-02.md          # L10–L18: Advanced VAEs, GANs
    ├── vol-02.index.md
    ├── vol-03.md          # L19–L27: Diffusion, NLP, transformers
    ├── vol-03.index.md
    ├── vol-04.md          # L28–L36: LLMs, RAG, multimodal, ethics
    └── vol-04.index.md
```

## Volume guide

| Volume | Lectures | Topics |
|--------|----------|--------|
| [Vol. 01](notes/vol-01.md) | L01–L09 | Deep learning foundations, autoencoders, VAE foundations |
| [Vol. 02](notes/vol-02.md) | L10–L18 | Advanced VAEs, GANs, advanced GAN variants |
| [Vol. 03](notes/vol-03.md) | L19–L27 | Diffusion models, sequence models, transformers |
| [Vol. 04](notes/vol-04.md) | L28–L36 | LLMs, RAG, multimodal AI, ethics |

## Building PDFs

From the repository root:

```bash
./scripts/build-pdf.sh courses/03-generative-ai-llms vol-01.md
./scripts/build-all-pdfs.sh   # builds all courses
```

Requires [Pandoc](https://pandoc.org/) and a LaTeX distribution with XeLaTeX.

## Official resources

- [NPTEL course page](https://nptel.ac.in/courses/106108002)
- [SWAYAM preview](https://onlinecourses.nptel.ac.in/e-learning/preview/noc26_cs95)

## Disclaimer

These notes are **supplementary study material** inspired by the official NPTEL course. They are not affiliated with or endorsed by NPTEL, IISc, or the course instructors.
