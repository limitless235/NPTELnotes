# L23: Vulnerability Scanning with OpenVAS/GVM

## Purpose

OpenVAS (Greenbone Vulnerability Manager) performs authenticated and unauthenticated network vulnerability scans.

## Usage steps

1. Install GVM: `sudo apt install gvm` → `sudo gvm-setup`.
2. Access web UI: `https://127.0.0.1:9392`.
3. Create target (IP/host list).
4. Create task with scan config (Full and fast / Full and deep).
5. Launch scan; review results by severity.
6. Export PDF/CSV report for remediation tracking.

## CLI (openvas-cli)

```bash
omp -u admin -w password --xml='<get_reports/>'
```

## Countermeasures

- Patch or mitigate every Critical/High finding.
- Schedule monthly scans; continuous with Greenbone Enterprise.
- Use credentialed scans for accurate patch status.
- Validate fixes with re-scan.

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
