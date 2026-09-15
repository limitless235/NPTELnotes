# References — Cyber Security Tools (nou26_ge86)

## Primary programme texts (BAOU PGDCS)

### PGDCS-101 — Principles of Cyber Security

- **Publisher:** Dr. Babasaheb Ambedkar Open University (BAOU)
- **Coverage:** CIA triad, risk management, cryptography basics, network security principles, security policies, legal and ethical foundations
- **Relevant units for this course:** Information security fundamentals; types of attacks; security controls; organizational security aspects
- **SLM access:** [BAOU PGDCS study materials](https://www.baou.edu.in/) → PGDCS programme → PGDCS-101

### PGDCS-103 — Cyber Security Techniques

- **Publisher:** BAOU (also adopted by MPBOU as PGDCS-02)
- **Block structure:**
  - **Block 1:** Information security basics, cyber crime modes, IDS, wireless security
  - **Block 2:** Assurance framework, desktop security, malware, e-commerce & web-app security, social engineering
  - **Block 3:** Risk management, computer forensics, cyber initiatives in India
  - **Block 4:** Network security threats, technologies, controls, physical security
- **SLM PDF:** [Cyber Security Techniques (PGDCS-103)](https://mpbou.edu.in/uploads/files/Cyber_Security_Techniques.pdf)
- **Direct mapping:** Volumes 1–4 of this course align with Blocks 1–4 tool labs

### PGDCS-204 — Cyber Attacks and Counter Measures: User Perspective

- User-facing threat awareness, phishing, safe browsing, mobile security
- Complements Vol. 04 (social engineering, cyber law)

---

## Nina Godbole — recommended textbooks

### 1. *Information Systems Security: Security Management, Metrics, Frameworks and Best Practices*

- **Author:** Nina Godbole
- **Edition:** 2nd ed., Wiley India, 2017
- **ISBN:** 978-8126564057
- **Use in this course:** Risk metrics, assurance frameworks (L25), policy vs procedure, audit preparation, SOX/SAS 70 context for asset management
- **Chapters of interest:** Risk analysis; network & database security controls; privacy; legal/compliance

### 2. *Cyber Security* (with Sunit Belapure)

- **Authors:** Nina Godbole, Sunit Belapure
- **Publisher:** Wiley India, 2011
- **ISBN:** 978-8126521791
- **Use in this course:** Cybercrime taxonomy, tools used in attacks (L5–L6), legal perspectives (L34–L36), organizational implications, forensics introduction
- **Chapters of interest:** Tools and methods in cybercrime; legal perspectives; computer forensics; careers in cybersecurity

---

## Tool documentation (official)

| Tool | Reference |
|------|-----------|
| Nmap | https://nmap.org/book/man.html |
| Wireshark | https://www.wireshark.org/docs/wsug_html_chunked/ |
| iptables | https://netfilter.org/documentation/ |
| OWASP ZAP | https://www.zaproxy.org/docs/ |
| sqlmap | https://github.com/sqlmapproject/sqlmap/wiki |
| Nikto | https://github.com/sullo/nikto |
| Snort | https://docs.snort.org/ |
| OpenVAS / GVM | https://greenbone.github.io/docs/ |
| John the Ripper | https://www.openwall.com/john/doc/ |
| Hydra | https://github.com/vanhauser-thc/thc-hydra |
| Aircrack-ng | https://www.aircrack-ng.org/documentation.html |

---

## Frameworks & standards

| Resource | URL | Lectures |
|----------|-----|----------|
| MITRE ATT&CK | https://attack.mitre.org/ | L5, L6 |
| Cyber Kill Chain (Lockheed Martin) | https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html | L5 |
| OWASP Top 10 | https://owasp.org/www-project-top-ten/ | L13–L20 |
| OWASP Testing Guide | https://owasp.org/www-project-web-security-testing-guide/ | L13–L19 |
| NIST SP 800-53 | https://csrc.nist.gov/publications/sp800 | L25 |
| PCI DSS | https://www.pcisecuritystandards.org/ | L28–L29 |
| CVSS v3.1 | https://www.first.org/cvss/ | L23–L24 |

---

## Indian cyber law

| Act / Rule | Relevance |
|------------|-----------|
| IT Act, 2000 (amended 2008) | Sections 43, 66, 67 — unauthorized access, hacking, obscenity |
| IT (Amendment) Act, 2008 | Section 66A repealed; 69A blocking; 79 intermediary liability |
| IT Rules, 2011 | Reasonable security practices; data protection |
| CERT-In directions (2022) | Incident reporting timelines for organizations |
| DPDP Act, 2023 | Personal data processing obligations |

Full text: [India Code — IT Act](https://www.indiacode.nic.in/)

---

## Video & open courseware

| Source | Link |
|--------|------|
| BAOU YouTube (scsbaou5615) | https://www.youtube.com/@scsbaou5615 |
| SWAYAM — Introduction to Cyber Security | https://swayam.gov.in/ |
| Class Central — cybersecurity course listings | https://www.classcentral.com/subject/cybersecurity |

---

## Supplementary reading

- Stallings, W. & Brown, L. — *Computer Security: Principles and Practice* (Pearson)
- Easttom, C. — *Computer Security Fundamentals* (Pearson)
- McClure, S. et al. — *Hacking Exposed* series (McGraw-Hill) — tool methodology reference
- RFC 2616 / HTTP — web attack context
- RFC 8446 — TLS 1.3

---

## Lab distributions

- **Kali Linux:** https://www.kali.org/
- **Metasploitable 2/3:** https://sourceforge.net/projects/metasploitable/
- **DVWA (Damn Vulnerable Web App):** https://github.com/digininja/DVWA
- **bWAPP:** http://www.itsecgames.com/
- **VulnHub:** https://www.vulnhub.com/ — practice VMs
