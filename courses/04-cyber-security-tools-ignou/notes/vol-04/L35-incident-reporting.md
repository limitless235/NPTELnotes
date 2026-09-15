# L35: Digital Evidence, Incident Reporting & CERT-In

## Purpose

Proper evidence handling and timely reporting are legal and operational requirements.

## Chain of custody

1. Identify and isolate affected systems.
2. Photograph/document state.
3. Hash all acquired images: `sha256sum image.dd`.
4. Log every person who handles evidence.
5. Store on write-once media or WORM storage.
6. Maintain custody transfer forms.

## CERT-In reporting (2022 directions)

- Report cyber incidents within **6 hours** for: data breaches, ransomware, DDoS on critical infra, etc.
- Log retention: 180 days minimum.
- NTP synchronization required.

## Countermeasures

- Pre-draft incident response plan (IRP).
- Tabletop exercises quarterly.
- Retainer with legal counsel.
- Preserve logs centrally (SIEM) before attacker deletion.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
