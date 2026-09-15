# Information Security

**Course code:** `cec26_cs13`  
**Platform:** CEC / SWAYAM  
**Institution:** Consortium for Educational Communication (CEC)  
**Instructor:** Dr. Maninder Singh, Thapar Institute of Engineering & Technology

## Overview

This course provides a comprehensive introduction to **information security** and **cryptography** for undergraduate students. It covers security fundamentals, threat analysis, classical and modern cryptographic algorithms, public-key infrastructure, and security auditing mechanisms. The material is organized as **36 lectures** (3 per week × 12 weeks), following the official Class Central / SWAYAM week plan.

## Learning outcomes

By the end of this course, you should be able to:

1. Explain the CIA triad and core security principles.
2. Identify and classify security threats at the program, system, and network levels.
3. Implement classical ciphers and analyze their weaknesses.
4. Describe the operation of DES, AES, RSA, Diffie-Hellman, and ECC.
5. Apply hash functions, digital signatures, and message authentication codes.
6. Explain public key infrastructure (PKI) and certificate management.
7. Design auditing and monitoring strategies for system security.

## Prerequisites

- Basic computer science (data structures, operating systems concepts)
- Elementary number theory and modular arithmetic (covered in course)
- No prior cryptography experience required

## Repository structure

```
05-information-security-cec/
├── README.md              # This file
├── references.md          # Textbooks and standards
├── lecture-index.md       # All 36 lectures
└── notes/
    ├── vol-01.md          # L01–L09: Security fundamentals, threats
    ├── vol-01.index.md
    ├── vol-02.md          # L10–L18: System threats, classical crypto
    ├── vol-02.index.md
    ├── vol-03.md          # L19–L27: DES/AES, RSA, DH, ECC
    ├── vol-03.index.md
    ├── vol-04.md          # L28–L36: Hash, signatures, PKI, auditing
    └── vol-04.index.md
```

## Volume guide

| Volume | Lectures | Topics |
|--------|----------|--------|
| [Vol. 01](notes/vol-01.md) | L01–L09 | Security fundamentals, authentication, threats |
| [Vol. 02](notes/vol-02.md) | L10–L18 | System threats, classical cryptography |
| [Vol. 03](notes/vol-03.md) | L19–L27 | Symmetric/asymmetric crypto, DES, AES, RSA, DH, ECC |
| [Vol. 04](notes/vol-04.md) | L28–L36 | Hash functions, signatures, PKI, auditing |

## Building PDFs

From the repository root:

```bash
./scripts/build-pdf.sh courses/05-information-security-cec vol-01.md
./scripts/build-all-pdfs.sh
```

## Official resources

- [Class Central course listing](https://www.classcentral.com/course/swayam-information-security-91683)
- [SWAYAM platform](https://swayam.gov.in/)

## Disclaimer

These notes are **supplementary study material** inspired by the official CEC/SWAYAM course. They are not affiliated with or endorsed by CEC, SWAYAM, or Dr. Maninder Singh.
