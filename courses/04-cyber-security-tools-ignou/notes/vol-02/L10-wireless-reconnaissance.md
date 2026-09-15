# L10: Wireless Reconnaissance & Monitoring

## Purpose

Discover Wi-Fi networks, clients, and security configurations using passive and active wireless monitoring.

## Tools

- **iwconfig / iw** — interface configuration
- **Airodump-ng** — capture 802.11 frames
- **Kismet** — wireless IDS

## Usage steps

```bash
# Enable monitor mode
sudo airmon-ng check kill
sudo airmon-ng start wlan0

# Scan all channels
sudo airodump-ng wlan0mon

# Target specific BSSID + channel
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture wlan0mon
```

## Countermeasures

- Use **WPA3** or WPA2-Enterprise (802.1X).
- Hide SSID is not security — rely on strong PSK/passphrase.
- Deploy WIDS (wireless IDS).
- Disable legacy protocols (WEP, WPA-TKIP).

---

*Lab reminder: test only on authorized systems. Unauthorized access violates the IT Act, 2000.*
