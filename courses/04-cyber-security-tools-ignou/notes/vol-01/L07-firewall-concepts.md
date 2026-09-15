# L07: Firewall Concepts — Stateful vs Stateless Filtering

## Purpose

Firewalls enforce access control at network boundaries — foundation for iptables (L8) and Windows Firewall (L9).

## Types

- **Packet-filtering** — examines headers (IP, port); stateless.
- **Stateful** — tracks connection state; allows return traffic automatically.
- **Application-layer (proxy)** — inspects HTTP/DNS content.
- **Next-gen (NGFW)** — IPS, app awareness, threat intel.

## Rule design principles

1. **Default deny** — block all, allow explicitly.
2. **Least privilege** — minimum ports/services.
3. **Document** every rule with owner and expiry.
4. Test rules in staging before production.

## Countermeasures

- Place firewalls at trust boundaries (DMZ, internal segments).
- Log denied packets; alert on spikes.
- Combine with IDS (Snort) for deep inspection.
- Review rules quarterly; remove orphans.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
