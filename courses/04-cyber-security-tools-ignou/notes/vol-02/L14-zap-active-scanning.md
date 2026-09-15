# L14: ZAP Active Scanning & Proxy Interception

## Purpose

Actively probe web apps for injection flaws, XSS, and misconfigurations.

## Active scan steps

1. Spider the target (Automated Scan → Spider).
2. Run **Active Scan** on discovered URLs.
3. Intercept requests: Break tab → modify parameters.
4. Replay with Fuzzer: right-click → Attack → Fuzz.
5. Review risk levels (High/Medium/Low/Info).

## Manual interception

```
# Example: modify POST parameter via ZAP proxy
# Original: id=1
# Modified: id=1' OR '1'='1
# Observe server response for SQL errors
```

## Countermeasures

- Input validation and parameterized queries.
- WAF with virtual patching.
- Disable verbose error messages in production.
- Scope active scans to authorized URLs only.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
