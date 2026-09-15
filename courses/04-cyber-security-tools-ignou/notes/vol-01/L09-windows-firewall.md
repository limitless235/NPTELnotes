# L09: Windows Firewall & Host-Based Perimeter Defense

## Purpose

Windows Defender Firewall provides host-level inbound/outbound filtering on Windows workstations and servers.

## PowerShell usage steps

```powershell
# Check status
Get-NetFirewallProfile | Select Name, Enabled

# Block inbound by default (Domain profile)
Set-NetFirewallProfile -Profile Domain -DefaultInboundAction Block

# Allow RDP from lab subnet only
New-NetFirewallRule -DisplayName "Lab RDP" `
  -Direction Inbound -Protocol TCP -LocalPort 3389 `
  -RemoteAddress 192.168.56.0/24 -Action Allow

# Block outbound SMB to internet
New-NetFirewallRule -DisplayName "Block SMB Out" `
  -Direction Outbound -Protocol TCP -RemotePort 445 `
  -RemoteAddress Internet -Action Block

# List rules
Get-NetFirewallRule | Where-Object {$_.Enabled -eq 'True'}
```

## GUI steps

1. `wf.msc` → Windows Defender Firewall with Advanced Security.
2. Inbound Rules → New Rule → Port/Program/Custom.
3. Assign profile (Domain, Private, Public).
4. Enable logging: Properties → Customize → Log dropped packets.

## Countermeasures

- Enforce GPO-managed firewall rules in AD environments.
- Combine with Defender ATP/EDR.
- Disable unnecessary services (SMBv1, Telnet).
- Audit rule changes via Windows Event Log (4946, 4947).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
