# L13: OWASP ZAP — Installation & Passive Scanning

## Purpose

OWASP Zed Attack Proxy (ZAP) is a free web app security scanner and intercepting proxy.

## Installation

```bash
# Kali: pre-installed; verify with
zaproxy --version
# Or download from zaproxy.org
```

## Passive scan steps

1. Launch ZAP → create new session.
2. Set target URL: `http://192.168.56.101/dvwa`.
3. Configure browser proxy: `127.0.0.1:8080`.
4. Browse the application manually.
5. Review **Alerts** tab for passive findings (missing headers, cookie flags).
6. Export report: Report → Generate HTML.

## Countermeasures

- Fix all passive findings before active testing.
- Set `HttpOnly` and `Secure` on session cookies.
- Implement Content-Security-Policy.
- Run ZAP in CI/CD pipeline (baseline scan).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
