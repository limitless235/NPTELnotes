# L05: APT Lifecycle & Cyber Kill Chain

## Purpose

Understand how advanced persistent threats progress through stages — maps offensive tools to defensive detection points.

## Cyber Kill Chain (7 stages)

1. **Reconnaissance** — OSINT, Nmap
2. **Weaponization** — malware + exploit paired
3. **Delivery** — phishing email, drive-by
4. **Exploitation** — trigger vulnerability
5. **Installation** — persistence, backdoor
6. **Command & Control** — beacon to C2 server
7. **Actions on Objectives** — data theft, destruction

## MITRE ATT&CK mapping

Use [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) to map techniques (T1595 Recon, T1190 Exploit Public-Facing App) to tools covered in this course.

## Lab exercise

Given a phishing scenario, identify which Kill Chain stages are complete and which Snort/iptables rules would detect each stage.

## Countermeasures

- **Defense in depth** — block multiple stages.
- Email filtering + user awareness (break delivery).
- EDR for installation/C2 detection.
- Network segmentation to limit lateral movement.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
