# L16: SQL Injection Fundamentals & Manual Testing

## Purpose

SQL injection (SQLi) inserts malicious SQL via unsanitized input — manual testing confirms exploitability before automation.

## Manual testing steps

1. Identify input points: `?id=1`, login forms, search boxes.
2. Test with payloads:
   - `' OR '1'='1`
   - `1' ORDER BY 5--`
   - `1 UNION SELECT null,username,password FROM users--`
3. Observe errors, behavior changes, timing delays.
4. Classify: in-band, blind (boolean/time), out-of-band.

## DVWA lab

```
# Low security: http://target/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit
# Escalate through DVWA security levels
```

## Countermeasures

- **Parameterized queries / prepared statements** (primary fix).
- ORM with bound parameters.
- Least-privilege DB accounts (no FILE/SHUTDOWN).
- WAF as secondary layer; not a substitute for secure coding.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
