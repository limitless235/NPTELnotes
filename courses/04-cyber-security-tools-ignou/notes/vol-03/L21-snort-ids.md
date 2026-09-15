# L21: Intrusion Detection with Snort

## Purpose

Snort is an open-source network IDS/IPS that matches traffic against rule-based signatures.

## Installation (Ubuntu)

```bash
sudo apt install snort
# Or Snort 3 from source: docs.snort.org
```

## Usage steps

```bash
# Test configuration
sudo snort -T -c /etc/snort/snort.conf

# IDS mode (alert only)
sudo snort -A console -c /etc/snort/snort.conf -i eth0

# Custom rule example
alert tcp any any -> $HOME_NET 80 (msg:"SQL Injection Attempt"; \
  content:"UNION"; content:"SELECT"; sid:1000001;)

# Log to unified2
sudo snort -c /etc/snort/snort.conf -i eth0 -l /var/log/snort
```

## Countermeasures (attacker evasion awareness)

- Fragmentation, encoding, encryption bypass signature IDS.
- Defenders: combine Snort with anomaly detection, TLS inspection (where legal).
- Keep rules updated: `sudo snort-update` / PulledPork.
- Tune rules to reduce false positives.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
