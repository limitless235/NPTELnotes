# L20: Session Management, CSRF & Authentication Flaws

## Purpose

Weak session handling and missing CSRF tokens enable account takeover and unauthorized actions.

## Testing steps

1. Check cookie flags: `Secure`, `HttpOnly`, `SameSite`.
2. Test session fixation: login without accepting new session ID.
3. CSRF: create HTML form posting to state-changing endpoint.
4. Test password reset flow for token predictability.

## ZAP CSRF check

Active scan → look for 'Absence of Anti-CSRF Tokens' alerts.

## Countermeasures

- Generate cryptographically random session IDs.
- Rotate session ID on login.
- Implement CSRF tokens on all state-changing requests.
- Enforce MFA for sensitive operations.
- Set `SameSite=Strict` or `Lax` on cookies.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
