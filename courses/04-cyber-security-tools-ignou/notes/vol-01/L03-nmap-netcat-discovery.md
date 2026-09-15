# L03: Network Discovery with Nmap & Netcat

## Nmap — purpose

Network mapper for host discovery, port scanning, service/version detection, and OS fingerprinting.

## Nmap — usage steps

```bash
# Host discovery (no port scan)
nmap -sn 192.168.56.0/24

# TCP SYN scan (requires root)
nmap -sS -p- 192.168.56.101

# Service + version detection
nmap -sV -O 192.168.56.101

# Safe script scan
nmap --script safe 192.168.56.101
```

## Netcat — purpose

Swiss-army TCP/UDP tool for connectivity testing, banner grabbing, and simple file transfer.

## Netcat — usage steps

```bash
# Listen on port 4444
nc -lvnp 4444

# Connect and grab banner
nc -v 192.168.56.101 80

# Port scan (basic)
nc -zv 192.168.56.101 20-80
```

## Countermeasures

- Deploy IDS/IPS to detect SYN scans (`nmap -sS`).
- Close unused ports; firewall by default-deny.
- Use port knocking or jump hosts for admin access.
- Rate-limit connection attempts (fail2ban).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
