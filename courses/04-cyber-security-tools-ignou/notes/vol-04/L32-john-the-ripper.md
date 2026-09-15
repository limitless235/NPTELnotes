# L32: Password Attacks with John the Ripper

## Purpose

John the Ripper (JtR) cracks password hashes offline — demonstrates why strong hashing matters.

## Usage steps

```bash
# Identify hash format
john --list=formats --format=crypt

# Crack /etc/shadow entries (lab)
unshadow /etc/passwd /etc/shadow > combined.txt
john combined.txt
john --wordlist=/usr/share/wordlists/rockyou.txt combined.txt

# Show cracked passwords
john --show combined.txt

# Specific format
john --format=md5crypt combined.txt
```

## Hash extraction (awareness)

```bash
# From Windows SAM (lab)
# mimikatz or samdump2 — authorized forensics only
```

## Countermeasures

- Store passwords with **bcrypt**, **scrypt**, or **Argon2** — never MD5/SHA1.
- Enforce password complexity + length (≥ 12 chars).
- Implement account lockout / rate limiting.
- Deploy MFA everywhere.
- Use password managers.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
