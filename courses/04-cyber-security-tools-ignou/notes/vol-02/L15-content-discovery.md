# L15: Directory & Content Discovery

## Purpose

Find hidden directories, backup files, and admin panels not linked in the application.

## Gobuster — usage steps

```bash
# Directory brute-force
gobuster dir -u http://192.168.56.101 -w /usr/share/wordlists/dirb/common.txt -x php,txt,bak

# DNS subdomain enumeration
gobuster dns -d example.com -w subdomains.txt

# ffuf (fast alternative)
ffuf -u http://target/FUZZ -w common.txt -fc 404
```

## dirb usage

```bash
dirb http://192.168.56.101 /usr/share/dirb/wordlists/common.txt
```

## Countermeasures

- Remove backup files from web roots.
- Return consistent 404 pages (no size differences).
- Require authentication for admin paths.
- Monitor for enumeration patterns (many 404s from one IP).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
