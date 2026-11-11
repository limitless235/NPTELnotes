# Volume 01 — Essentials, APT/Kill Chain, Firewalls (L01–L09)

> Cyber Security Tools · IGNOU/BAOU nou26_ge86 · Prof. Dr. Nilesh K. Modi  
> **notes-3** — concept exam notes (what things are / what they do). Condensed from course `pdf/` volumes. No lab command dumps.

Tool landscape, CIA/risk, Nmap/Netcat/Wireshark roles, Kill Chain, STRIDE, firewall concepts.

---

## L1: Course Introduction & Cyber Security Tool Landscape

### What it is / what it does
- Security tools are software utilities used to **detect**, **prevent**, **analyze**, or **respond to** cyber threats. This course maps tools to the BAOU PGDCS-103 blocks and hands-on lab workflows.
- **Tool categories:**

| Category | Examples | Role |
|----------|----------|------|
| Reconnaissance | Nmap, theHarvester | Discover assets |
| Scanning | Nikto, OpenVAS | Find vulnerabilities |
| Exploitation | sqlmap, Hydra | Demonstrate impact (lab only) |
| Defense | iptables, Snort, Windows Firewall | Block/detect attacks |
| Analysis | Wireshark, strings | Inspect traffic/files |

### Defenses (one-liners)
- Maintain asset inventory so unknown scanning is detectable.
- Segment lab networks from production LANs.
- Enforce **authorization** before any security testing.
- Log and monitor VM host activity.

### Exam lines
- Security tools are software utilities used to **detect**, **prevent**, **analyze**, or **respond to** cyber threats. This course maps…
- **Tool categories:**

---

## L2: CIA Triad, Risk Assessment & Security Policies

### What it is / what it does
- Establish the security foundation before tool usage. Aligns with PGDCS-101 Block 1 and Nina Godbole's risk-management chapters.
- **Confidentiality** — encryption, access control
- **Integrity** — hashing, change detection
- **Availability** — redundancy, backups, DDoS mitigation
- **Policy** — what must be done (e.g., 'All passwords ≥ 12 characters').
- **Procedure** — how to do it (e.g., Active Directory GPO steps).

### Defenses (one-liners)
- Publish acceptable-use and password policies.
- Conduct annual risk assessments.
- Map controls to frameworks (ISO 27001, NIST).

### Exam lines
- Establish the security foundation before tool usage. Aligns with PGDCS-101 Block 1 and Nina Godbole's risk-management chapters.
- **Confidentiality** — encryption, access control
- **Integrity** — hashing, change detection
- **Availability** — redundancy, backups, DDoS mitigation
- **Policy** — what must be done (e.g., 'All passwords ≥ 12 characters').

---

## L3: Network Discovery with Nmap & Netcat

### What it is / what it does
- **Nmap:** Network mapper for host discovery, port scanning, service/version detection, and OS fingerprinting.
- **Netcat:** Swiss-army TCP/UDP tool for connectivity testing, banner grabbing, and simple file transfer.

### Defenses (one-liners)
- Deploy IDS/IPS to detect SYN scans (nmap -sS).
- Close unused ports; firewall by default-deny.
- Use port knocking or jump hosts for admin access.
- Rate-limit connection attempts (fail2ban).

### Exam lines
- **Nmap:** Network mapper for host discovery, port scanning, service/version detection, and OS fingerprinting.
- **Netcat:** Swiss-army TCP/UDP tool for connectivity testing, banner grabbing, and simple file transfer.

---

## L4: Packet Analysis with Wireshark

### What it is / what it does
- Capture and decode network frames to troubleshoot issues and detect malicious traffic.
- **Key display filters:**

| Filter | Use |
|--------|-----|
| ip.addr == 10.0.0.5 | Host traffic |
| tcp.flags.syn == 1 | SYN packets |
| dns | DNS queries |
| tls.handshake.type == 1 | TLS ClientHello |

### Defenses (one-liners)
- Encrypt traffic (TLS 1.2+) to limit passive disclosure.
- Monitor for DNS tunneling and unusual protocols.
- Store PCAPs securely with access controls.
- Use encrypted management channels (SSH, not Telnet).

### Exam lines
- Capture and decode network frames to troubleshoot issues and detect malicious traffic.
- **Key display filters:**

---

## L5: APT Lifecycle & Cyber Kill Chain

### What it is / what it does
- Understand how advanced persistent threats progress through stages — maps offensive tools to defensive detection points.
- **Reconnaissance** — OSINT, Nmap
- **Weaponization** — malware + exploit paired
- **Delivery** — phishing email, drive-by
- **Exploitation** — trigger vulnerability
- **Installation** — persistence, backdoor
- **Command & Control** — beacon to C2 server
- **Actions on Objectives** — data theft, destruction
- **MITRE ATT&CK mapping** — Use [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) to map techniques (T1595 Recon, T1190 Exploit Public-Facing App) to tools covered in this course.

### Defenses (one-liners)
- **Defense in depth** — block multiple stages.
- Email filtering + user awareness (break delivery).
- EDR for installation/C2 detection.
- Network segmentation to limit lateral movement.

### Exam lines
- Understand how advanced persistent threats progress through stages
- **Reconnaissance** — OSINT, Nmap
- **Weaponization** — malware + exploit paired
- **Delivery** — phishing email, drive-by
- **MITRE ATT&CK mapping** — Use [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) to map techniques (T1595 Recon,…

---

## L6: Threat Modeling & Attack Surface Mapping

### What it is / what it does
- Systematically identify threats before attackers do; prioritize which tools to deploy for testing.
- **STRIDE model:**

| Threat | Example | Tool to test |
|--------|---------|-------------|
| Spoofing | Fake login page | Phishing sim |
| Tampering | SQL injection | sqlmap |
| Repudiation | Log deletion | auditd |
| Info disclosure | Verbose errors | Nikto |
| DoS | SYN flood | hping3 (lab) |
| Elevation | SUID exploit | manual |

### Defenses (one-liners)
- Reduce attack surface: disable unused services.
- Apply least privilege.
- Re-model after every architecture change.
- Integrate threat modeling into SDLC.

### Exam lines
- Systematically identify threats before attackers do; prioritize which tools to deploy for testing.
- **STRIDE model:**

---

## L7: Firewall Concepts — Stateful vs Stateless Filtering

### What it is / what it does
- Firewalls enforce access control at network boundaries — foundation for iptables (L8) and Windows Firewall (L9).
- **Packet-filtering** — examines headers (IP, port); stateless.
- **Stateful** — tracks connection state; allows return traffic automatically.
- **Application-layer (proxy)** — inspects HTTP/DNS content.
- **Next-gen (NGFW)** — IPS, app awareness, threat intel.
- **Default deny** — block all, allow explicitly.
- **Least privilege** — minimum ports/services.
- **Document** every rule with owner and expiry.
- Test rules in staging before production.

### Defenses (one-liners)
- Place firewalls at trust boundaries (DMZ, internal segments).
- Log denied packets; alert on spikes.
- Combine with IDS (Snort) for deep inspection.
- Review rules quarterly; remove orphans.

### Exam lines
- Firewalls enforce access control at network boundaries
- **Packet-filtering** — examines headers (IP, port); stateless.
- **Stateful** — tracks connection state; allows return traffic automatically.
- **Application-layer (proxy)** — inspects HTTP/DNS content.
- **Default deny** — block all, allow explicitly.

---

## L8: Linux Packet Filtering with iptables & UFW

### What it is / what it does
- **iptables:** Linux kernel netfilter framework for packet filtering, NAT, and mangling.

### Defenses (one-liners)
- Automate rule deployment (Ansible, Puppet).
- Never expose management ports to the internet.
- Test with nmap after rule changes.
- Monitor /var/log/kern.log for DROP entries.

### Exam lines
- **iptables:** Linux kernel netfilter framework for packet filtering, NAT, and mangling.

---

## L9: Windows Firewall & Host-Based Perimeter Defense

### What it is / what it does
- Windows Defender Firewall provides host-level inbound/outbound filtering on Windows workstations and servers.

### Defenses (one-liners)
- Enforce GPO-managed firewall rules in AD environments.
- Combine with Defender ATP/EDR.
- Disable unnecessary services (SMBv1, Telnet).
- Audit rule changes via Windows Event Log (4946, 4947).

### Exam lines
- Windows Defender Firewall provides host-level inbound/outbound filtering on Windows workstations and servers.

---
