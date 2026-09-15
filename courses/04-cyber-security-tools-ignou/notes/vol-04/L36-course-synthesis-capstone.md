# L36: Course Synthesis — Tool Chain Integration & Assessment

## Purpose

Integrate all tools into an end-to-end assessment workflow — capstone for nou26_ge86.

## Capstone scenario

Assess a small e-commerce lab environment:
1. **Recon:** Nmap network scan.
2. **Enum:** Gobuster + Nikto on web server.
3. **Vuln scan:** OpenVAS full scan.
4. **Web test:** ZAP active scan + sqlmap on injection point.
5. **Wireless:** Document WPA configuration (if applicable).
6. **Defense:** Write Snort rule for attack traffic observed.
7. **Firewall:** iptables rules to block attacker IP.
8. **Credentials:** Demonstrate Hydra risk; recommend MFA.
9. **Report:** CVSS-rated findings + remediation + legal disclaimer.

## Report template

1. Executive summary
2. Scope and authorization
3. Methodology (tools + versions)
4. Findings table (ID, severity, CVSS, evidence, recommendation)
5. Conclusion and re-test plan

## Assessment prep

- Review all 36 lecture tool summaries.
- Watch BAOU YouTube channel: scsbaou5615.
- Complete PGDCS-103 Block review questions.
- Practice in isolated VMs only.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
