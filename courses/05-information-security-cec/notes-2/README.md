# Transcript-grounded notes — Information Security

Study notes for the **EMRC Patiala YouTube series** (intro + 47 modules). Every lecture file is written from that lecture's transcript: definitions, named protocols, architectures, and conclusions the instructor actually taught. ASR errors are corrected to standard networking/security terms.

These notes are **not** the 36-lecture SWAYAM cryptography week plan in [`../notes/`](../notes/). That set stays as Volume 01–04 under `notes/`.

**Playlist:** https://www.youtube.com/playlist?list=PLcWnLUJA-zgdEW1tOYLs7xsZ0lP8gx-6b  
**Coordinator:** Dr. Maninder Singh, Thapar Institute of Engineering & Technology

## Layout

```
notes-2/
├── README.md              # This file
├── lectures/              # One markdown file per video (source of truth)
├── vol-01.md … vol-04.md  # Concatenated volumes (PDF source)
├── vol-01.index.md …
└── pdf/                   # Printable volume PDFs
```

## Volume map

| Volume | Modules | Topics | Notes | PDF |
|--------|---------|--------|-------|-----|
| 01 | M00–M11 | Ethics, network models, TCP/IP, MAC, addressing, TCP connections | [vol-01.md](vol-01.md) | [PDF](pdf/vol-01.pdf) |
| 02 | M12–M23 | IPv4/IPv6, UDP, IPsec, topologies, cursor PoC, email, WWW, media, Ethernet | [vol-02.md](vol-02.md) | [PDF](pdf/vol-02.pdf) |
| 03 | M24–M35 | Ethernet security, GbE/10GbE, ISDN, SCTP, ATM, wireless, Wi-Fi, Bluetooth, VPN, WiMAX | [vol-03.md](vol-03.md) | [PDF](pdf/vol-03.pdf) |
| 04 | M36–M47 | Mobile IP, cloud, GSM, MANET, 3G/4G/5G, VoIP, DDoS | [vol-04.md](vol-04.md) | [PDF](pdf/vol-04.pdf) |

Indexes: [vol-01.index.md](vol-01.index.md) · [vol-02.index.md](vol-02.index.md) · [vol-03.index.md](vol-03.index.md) · [vol-04.index.md](vol-04.index.md)

Per-lecture sources: [lectures/](lectures/).

## Building PDFs

From the repository root (Pandoc, XeLaTeX, mermaid-cli):

```bash
cd scripts && npm install && cd ..
python3 scripts/assemble_infosec_notes2.py
./scripts/build-notes2-pdfs.sh
```

Output is `notes-2/pdf/vol-0*.pdf`. Mermaid blocks are rendered to PNG during the PDF build.

## Caption caveat

**M35** is titled *WiMAX Technology and its Security* in the playlist, but the YouTube captions for that video are a near-duplicate of **M33 Bluetooth**. The notes follow the captions (Bluetooth) and flag the mismatch. They do not invent WiMAX material.

## Disclaimer

Supplementary study material grounded in public lecture transcripts. Course content and video rights remain with CEC, SWAYAM, EMRC Patiala, and the instructors.
