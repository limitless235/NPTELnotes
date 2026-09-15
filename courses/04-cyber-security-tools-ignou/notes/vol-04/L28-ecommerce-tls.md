# L28: E-Commerce Security & TLS/SSL Configuration

## Purpose

E-commerce depends on transport encryption and secure certificate management — PGDCS-103 Block 2, Unit 3.

## OpenSSL — usage steps

```bash
# Check certificate
echo | openssl s_client -connect shop.example.com:443 2>/dev/null | openssl x509 -noout -dates -subject

# Test TLS configuration
testssl.sh https://shop.example.com

# Generate self-signed (lab)
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

## TLS best practices

- TLS 1.2 minimum; prefer TLS 1.3.
- Strong cipher suites (AEAD: AES-GCM, ChaCha20).
- HSTS header: `Strict-Transport-Security: max-age=31536000`.
- Certificate transparency monitoring.

## Countermeasures

- Auto-renew certs (Let's Encrypt, cert-manager).
- Disable SSLv3, TLS 1.0/1.1.
- Implement OCSP stapling.
- Monitor for cert expiry (30-day alerts).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
