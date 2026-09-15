# L22: IDS Tuning, IPS Mode & Log Analysis

## Purpose

Operationalize IDS — reduce false positives, enable inline blocking, correlate alerts.

## Snort IPS (inline) mode

```bash
# Requires inline network tap or bridge
sudo snort -Q --daq afpacket -c /etc/snort/snort.conf -i eth0:eth1
```

## Suricata alternative

```bash
sudo apt install suricata
sudo suricatasc -c ruleset-reload-rules
sudo tail -f /var/log/suricata/fast.log
```

## Tuning steps

1. Baseline normal traffic for 48 hours.
2. Suppress noisy rules (e.g., ICMP ping).
3. Create custom rules for critical assets.
4. Integrate with SIEM (Splunk, ELK, Wazuh).
5. Define escalation playbooks per alert category.

## Countermeasures

- Defense: encrypted C2 is hard to signature-detect — use behavioral analytics.
- Regular purple-team exercises to validate detection coverage.
- Document every suppressed rule with justification.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
