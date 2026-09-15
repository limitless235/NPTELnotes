# L06: Threat Modeling & Attack Surface Mapping

## Purpose

Systematically identify threats before attackers do; prioritize which tools to deploy for testing.

## STRIDE model

| Threat | Example | Tool to test |
|--------|---------|-------------|
| Spoofing | Fake login page | Phishing sim |
| Tampering | SQL injection | sqlmap |
| Repudiation | Log deletion | auditd |
| Info disclosure | Verbose errors | Nikto |
| DoS | SYN flood | hping3 (lab) |
| Elevation | SUID exploit | manual |

## Attack surface mapping steps

1. Draw data-flow diagram (DFD).
2. List entry points: web forms, APIs, Wi-Fi, USB.
3. Assign trust boundaries.
4. Apply STRIDE per component.
5. Rank risks; schedule scans (OpenVAS, ZAP).

## Countermeasures

- Reduce attack surface: disable unused services.
- Apply least privilege.
- Re-model after every architecture change.
- Integrate threat modeling into SDLC.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
