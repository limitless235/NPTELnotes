# notes-3 — concept exam notes (Information Security CEC)

Condensed from **notes-2** (48 EMRC modules) for concept-style exams: key-term tables and lecture takeaways. Breadth over lab depth.

## Volumes

| Volume | Modules | PDF |
|--------|---------|-----|
| 01 | M00–M11 | [pdf/vol-01.pdf](pdf/vol-01.pdf) |
| 02 | M12–M23 | [pdf/vol-02.pdf](pdf/vol-02.pdf) |
| 03 | M24–M35 | [pdf/vol-03.pdf](pdf/vol-03.pdf) |
| 04 | M36–M47 | [pdf/vol-04.pdf](pdf/vol-04.pdf) |

## Rebuild

```bash
python3 scripts/condense_notes3_from_notes2.py infosec
./scripts/build-notes3-pdfs.sh infosec
```

## Worked numericals

Step-by-step calculations flattened out of notes-3 are restored in:

- [`numericals.md`](numericals.md)
- [`../../final pdf/05-information-security-cec-numericals.pdf`](../../final%20pdf/05-information-security-cec-numericals.pdf)

Covers M06 TCP window, M07 stop-and-wait \(U\), M09–M10 addressing/CIDR, M11 seq/ACK, M12 binary/CIDR blocks, M13 UDP hex dump, M14 AH length.
