# Volume 06 Index — Lectures 51–62

**Theme:** Web application vulnerabilities, SQL injection, XSS, file upload, Nmap mastery, Wireshark, course summary

| Lec | Title | Key Tools | Top Exam Topic |
|-----|-------|-----------|----------------|
| 51 | Web App Vuln Scanning | Burp Suite, OWASP ZAP, gobuster | OWASP Top 10, active vs passive scan |
| 52 | SQLi Auth Bypass | Burp Repeater | `' OR '1'='1`, prepared statements |
| 53 | SQLi Error Based | UNION SELECT, extractvalue | Column count, information_schema |
| 54 | SQLi from Web App | DVWA, Burp Intruder | Filter bypass, blind SQLi, SLEEP() |
| 55 | SQLMAP | sqlmap | --dbs, --dump, --os-shell, tamper |
| 56 | Cross Site Scripting | BeEF, Burp | Reflected/stored/DOM XSS, CSP |
| 57 | File Upload Vuln | weevely, msfvenom | Web shell, whitelist validation |
| 58 | NMAP Relook I | nmap -PR, -Pn, -sL | ARP scan, host discovery methods |
| 59 | NMAP Relook II | nmap -sS -p- | Scan types, timing templates |
| 60 | NMAP Relook III | nmap -A, NSE vuln | -sV, -O, -oA, NSE scripts |
| 61 | Wireshark | tshark, tcpdump | Capture vs display filters, TLS |
| 62 | Course Summary | — | Pentest phases, defense-in-depth |

## Diagrams in This Volume

- [SQL Injection Auth Bypass Flow (Mermaid)](vol-06.md#sql-injection-authentication-bypass-flow) — Lecture 52

## Cross-References

- Networking foundations → [vol-01](vol-01.md)
- Nessus scanning → [vol-02 L19–20](vol-02.md)
- Metasploit exploitation → [vol-03](vol-03.md)
- Password cracking → [vol-05 L41](vol-05.md)
