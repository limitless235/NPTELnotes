# L18: Cross-Site Scripting (XSS) & Client-Side Attacks

## Purpose

XSS injects malicious scripts into pages viewed by other users — stored, reflected, and DOM-based variants.

## Manual testing payloads

```html
<script>alert('XSS')</script>
<img src=x onerror=alert(1)>
"><svg onload=alert(1)>
```

## ZAP detection

1. Active scan flags XSS automatically.
2. Manual: submit payloads in every input field.
3. Check if payload appears unencoded in response.

## BeEF (awareness)

Browser Exploitation Framework hooks browsers post-XSS — demonstrates impact of session hijacking via client-side execution.

## Countermeasures

- **Output encoding** (HTML, JS, URL context-aware).
- Content-Security-Policy: `default-src 'self'`.
- HttpOnly cookies prevent JavaScript access.
- Sanitize HTML with allowlist libraries (DOMPurify).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
