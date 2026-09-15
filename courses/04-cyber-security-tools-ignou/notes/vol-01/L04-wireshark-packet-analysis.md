# L04: Packet Analysis with Wireshark

## Purpose

Capture and decode network frames to troubleshoot issues and detect malicious traffic.

## Usage steps

1. Select the correct interface (e.g., `eth0`).
2. Apply capture filter: `tcp port 80`.
3. Start capture during a test (browse target web app).
4. Stop capture; apply display filter: `http.request.method == "GET"`.
5. Follow TCP stream to reconstruct sessions.
6. Export objects or save PCAP for evidence.

## Key display filters

| Filter | Use |
|--------|-----|
| `ip.addr == 10.0.0.5` | Host traffic |
| `tcp.flags.syn == 1` | SYN packets |
| `dns` | DNS queries |
| `tls.handshake.type == 1` | TLS ClientHello |

## Countermeasures

- Encrypt traffic (TLS 1.2+) to limit passive disclosure.
- Monitor for DNS tunneling and unusual protocols.
- Store PCAPs securely with access controls.
- Use encrypted management channels (SSH, not Telnet).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
