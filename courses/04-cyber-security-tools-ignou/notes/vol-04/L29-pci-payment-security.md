# L29: Payment Security, PCI-DSS & Web Hardening

## Purpose

PCI-DSS mandates controls for organizations handling cardholder data.

## PCI-DSS key requirements

1. Install and maintain firewall.
2. No default passwords.
3. Protect stored cardholder data.
4. Encrypt transmission.
5. Use and update antivirus.
6. Develop secure systems.
7. Restrict data access.
8. Unique IDs for each person.
9. Restrict physical access.
10. Track and monitor network access.
11. Regularly test security.
12. Maintain information security policy.

## ZAP for e-commerce

```bash
# Scan checkout flow
zap-cli quick-scan --self-contained http://shop.lab/checkout
# Check for: mixed content, missing headers, injection in payment fields
```

## Countermeasures

- Tokenize card data (use payment gateway — never store PAN).
- SAQ (Self-Assessment Questionnaire) compliance.
- Quarterly ASV scans (OpenVAS qualified).
- Segregate CDE (Cardholder Data Environment).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
