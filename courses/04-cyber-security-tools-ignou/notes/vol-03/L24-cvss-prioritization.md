# L24: CVSS Scoring & Vulnerability Prioritization

## Purpose

Common Vulnerability Scoring System (CVSS) provides standardized severity ratings for triage.

## CVSS v3.1 metrics

- **Base:** Attack Vector, Complexity, Privileges, User Interaction, Scope, Impact (C/I/A)
- **Temporal:** Exploit maturity, remediation level
- **Environmental:** asset-specific modifiers

## Scoring steps

1. Obtain CVE and NVD entry.
2. Calculate base score (use NVD calculator).
3. Apply environmental score for your asset criticality.
4. Prioritize: Critical (9.0–10.0) → immediate; Low (0.1–3.9) → scheduled.

## Calculator

https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator

## Countermeasures

- Don't chase volume — prioritize by exploitability + asset value.
- Track mean time to remediate (MTTR) by severity.
- Integrate CVSS with ticketing (Jira, ServiceNow).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
