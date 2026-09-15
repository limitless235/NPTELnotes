# L01: Course Introduction & Cyber Security Tool Landscape

## Overview

Security tools are software utilities used to **detect**, **prevent**, **analyze**, or **respond to** cyber threats. This course maps tools to the BAOU PGDCS-103 blocks and hands-on lab workflows.

## Tool categories

| Category | Examples | Role |
|----------|----------|------|
| Reconnaissance | Nmap, theHarvester | Discover assets |
| Scanning | Nikto, OpenVAS | Find vulnerabilities |
| Exploitation | sqlmap, Hydra | Demonstrate impact (lab only) |
| Defense | iptables, Snort, Windows Firewall | Block/detect attacks |
| Analysis | Wireshark, strings | Inspect traffic/files |

## Lab setup steps

1. Install VirtualBox or VMware.
2. Download **Kali Linux** ISO from kali.org.
3. Create two VMs on a **host-only network**: Kali (attacker) + Ubuntu/Metasploitable (target).
4. Snapshot VMs before each lab.
5. Verify connectivity: `ping <target-ip>` from Kali.

## Countermeasures

- Maintain asset inventory so unknown scanning is detectable.
- Segment lab networks from production LANs.
- Enforce **authorization** before any security testing.
- Log and monitor VM host activity.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
