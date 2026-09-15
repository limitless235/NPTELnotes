# L12: Web Server Scanning with Nikto

## Purpose

Open-source web server scanner that identifies outdated software, dangerous files, and misconfigurations.

## Usage steps

```bash
# Basic scan
nikto -h http://192.168.56.101

# Scan specific port + SSL
nikto -h 192.168.56.101 -p 443 -ssl

# Save report
nikto -h http://target -o report.html -Format html

# Tune scan (evade IDS)
nikto -h http://target -Tuning 123456789
```

## Common findings

- Default files (`/admin`, `/phpinfo.php`)
- Outdated Apache/IIS versions
- HTTP methods enabled (PUT, TRACE)
- Missing security headers

## Countermeasures

- Remove default pages and sample apps.
- Keep web server patched.
- Disable dangerous HTTP methods.
- Add security headers (CSP, X-Frame-Options).
- Rate-limit scanner traffic at WAF.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
