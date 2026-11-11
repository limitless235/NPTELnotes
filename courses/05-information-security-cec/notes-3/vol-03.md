# Volume 03 — M24–M35

> Information Security (CEC) · SWAYAM / CEC Information Security
> **notes-3** — concept exam notes (definitions & what things do). Breadth over lab depth.

---

## M24: Ethernet Security

### Learning focus
- Trace Ethernet from ALOHAnet and Xerox CSMA/CD through the DIX 1.0 spec to IEEE 802.3, and name the frame as the on-wire unit.
- State why Ethernet was designed without security, and list the five attack classes the lecture uses (access, confidentiality, integrity, DoS, system security).
- Contrast router-based segmentation, access control (including IEEE 802.1Q / 802.1X), higher-layer crypto, and monitoring.
- Describe IEEE 802.1AE MACsec: SecTAG and ICV placement, SA/SAK/PN/SCI, Protect/Validate, and replay protection.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Frame | Ethernet’s on-wire data unit; only one node should send one at a time |
| CSMA/CD | Carrier sense, multiple access, collision detection — Ethernet’s classic shared-medium rule |
| IEEE 802.3 | LAN/MAN standard grown from DIX Ethernet 1.0 (1980) and standardized in 1983 |
| VLAN hopping | Injecting VLAN-tagged frames (or abusing VLAN management) to reach VLANs the port should not join |
| STP TCN flood | DoS by flooding Spanning Tree topology-change notifications or other STP control |
| IEEE 802.1Q / QinQ / PVLAN | VLAN tagging, double tagging, and private-VLAN isolation (hosts only talk via a promiscuous router port) |
| IEEE 802.1X / EAP | Port authentication of a host to a switch that checks an authentication server |
| DHCP snooping | Bind MAC–IP–port from DHCP so ARP spoofing can be blocked, limited to what that switch can see |
| MACsec (IEEE 802.1AE) | Hop-by-hop encryption/integrity of Ethernet MSDUs using SecTAG, SAK, PN, SCI, and ICV |
| SecTAG / ICV / SAK / PN | MACsec tag, integrity check, association key, and packet number used for Protect, Validate, and replay checks |

### Exam lines
- Ethernet won wired LANs by simplicity, not by security; design never treated security as a first-class goal.
- Almost every attack starts with **segment access** (physical jack, rogue AP/switch, VLAN tricks, stolen switch, or a remotely owned host).
- Confidentiality, integrity (ARP/DHCP poisoning, MITM, session hijack), and STP/resource DoS are the concrete Ethernet threats taught here.
- Classic mitigation was “treat the LAN as dirty” (building + firewall) plus **IPsec/TLS**; that is costly and incomplete.
- Routers cut broadcast-domain attacks; 802.1Q/PVLAN/ACLs/802.1X limit who is on the wire; DHCP snooping hardens ARP; firewalls/IDS are secondary.
- **IEEE 802.1AE MACsec** is the Ethernet-layer protocol the lecture spends its last section on: encrypt and integrity-protect frames between authorized devices, with replay protection via PN.


---

## M25: Gigabit Ethernet

### Learning focus
- Explain why Gigabit Ethernet (1 Gbps / 1000 Mbps) was specified as a 10× Fast Ethernet successor that keeps the IEEE 802.3 frame and MAC modes.
- Map the Gigabit stack: GMII, PCS (8B/10B), PMA, PMD/MDI, and auto-negotiation of 10/100/1000 Mbps and half/full duplex.
- List the IEEE 802.3z / 802.3ab / 802.3ah (and related) physical types with media, wavelengths, and distances the lecture gives.
- Recite the basic Gigabit MAC frame fields, CSMA/CD vs full duplex, packet bursting, and **carrier extension**.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Gigabit Ethernet | 1000 Mbps / 1 Gbps IEEE 802.3 family, 10× Fast Ethernet |
| 1000BASE-X | IEEE 802.3z fiber/short-copper group (SX, LX, CX; ZX as vendor term) |
| 1000BASE-T | IEEE 802.3ab Gigabit on Cat 5/5e/6 UTP |
| GMII | Gigabit Media Independent Interface between MAC and PHY |
| 8B/10B | PCS coding: 8 data bits as 10-bit code groups (Fibre Channel style), 125 MHz toward PMA |
| Packet bursting | Half-duplex CSMA/CD enhancement: burst small packets to fill the pipe |
| IEEE 802.3x | Full-duplex operation and flow control used by Gigabit when not sharing the wire |
| Carrier extension | Extra symbols in the collision window so min/max 802.3 sizes still work at 1 Gbps distances; FCS ignores the extension |
| Length/Type | ≤1500 → LLC length; >1500 → optional Ethernet type |

### Exam lines
- Gigabit exists because Fast Ethernet desktops overflowed 100 Mbps backbones; it keeps **802.3 frames** so shops need not move backbones to **ATM** or **FDDI**.
- Architecture is **MAC → GMII → PCS (8B/10B, auto-neg) → PMA (125 MHz serialize) → PMD**.
- Fiber PHYs (SX/LX/LX10/BX10/EX/ZX) and copper (CX then T) are chosen by **reach and cabling already in the wall**.
- **Full duplex** is the shipping default (up to **2 Gbps** both ways, no CSMA/CD); half duplex still exists with **CSMA/CD + burst + carrier extension**.
- Frame layout is classic Ethernet (preamble through 32-bit CRC); **carrier extension is the Gigabit-specific MAC trick** taught at the end.


---

## M26: 10 Gigabit Ethernet

### Learning focus
- State that 10 Gigabit Ethernet (10 GbE / 10G / 10 GigE) sends Ethernet frames at **10 Gbps**, first in **IEEE 802.3ae-2002**, and that it is **full duplex only** (no hubs, no CSMA/CD).
- Walk the 10G stack: RS, PCS, PMA, PMD, XGMII, MDI, and the **WAN Interface Sublayer (WIS)** for SONET-friendly WAN PHYs.
- Contrast **serial 10 Gbps** vs **parallel n-lane** (including WDM) implementations.
- Recite the unchanged Ethernet MAC frame, why the minimum is **64 octets** without carrier extension, and the LAN-fiber / WAN-fiber / copper / backplane / EPON PHYs with rates, wavelengths, and reaches.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| 10 GbE / 10G / 10 GigE | Ethernet frames at 10 Gbps; full duplex only |
| IEEE 802.3ae-2002 | First 10G Ethernet standard (LAN/WAN fiber) |
| 10GBASE-R / W / X | LAN fiber, WAN fiber, and copper coding families |
| XGMII | 10 Gigabit Media Independent Interface (MAC–PHY) |
| WIS | WAN Interface Sublayer: simplified SONET framing between serial PCS and PMA |
| 64B/66B | Serial LAN PCS coding; LAN PHY line rate about 10.3 / 10.3125 Gbps |
| HSSG | Higher Speed Study Group (March 1999) that started 10G work |
| 10GBASE-T | IEEE 802.3an twisted-pair 10G (Cat 6 55 m; 6A/7 100 m) |
| 10GBASE-PR | IEEE 802.3av 10G EPON PHY with PR10/PR20/PR30 power budgets |

### Exam lines
- 10 GbE is still Ethernet frames, but **only full-duplex switched point-to-point** — CSMA/CD and hubs are gone because half duplex at 10 Gbps is not a market.
- Stack is classic 802.3 PHY split (**PCS/PMA/PMD**) plus **XGMII** and, for WAN, **WIS/SONET**.
- Implementers choose **one 10G serial pipe** (simple) or **n slower lanes / WDM** (cheaper silicon, more jitter and optics).
- MAC frame is the familiar 64-octet-minimum Ethernet frame; **no carrier extension**.
- PHY letter soup is organized as **LAN-R, WAN-W, copper/backplane, and EPON-PR**, with **10.3125 Gbps** as the repeated serial line rate on optical LAN PHYs.


---

## M27: ISDN

### Learning focus
- Define ISDN as ITU/CCITT digital circuit- and packet-switched service over ordinary telephone-grade copper (and other media).
- Contrast BRI (2B+D = 144 kbps) with PRI (23B+D / 30B+D) and name B vs D channel rates.
- List bearer, teleservice, and supplementary services, plus TE1/TE2/TA/NT1/NT2 and R–V reference points.
- State ISDN vs ADSL differences, advantages/disadvantages, and the lecture’s security conclusion (logical attacks and HTTPS matter more than the physical medium).

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| ISDN | ITU/CCITT integrated digital voice/data network on phone copper (and other media) |
| B channel | Bearer channel, typically 64 kbps (sometimes 56), carries user voice/data |
| D channel | Delta/data channel for signaling and control (16 kbps BRI, 64 kbps PRI) |
| BRI / 2B+D | Basic Rate Interface, 144 kbps, individual users |
| PRI / 23B+D / 30B+D | Primary Rate, T1-like 1.536 Mbps or E1-like 1.984 Mbps |
| B-ISDN | Broadband ISDN on fiber, 155–622 Mbps and beyond |
| Bearer / teleservice / supplementary | OSI 1–3 network functions; OSI 4–7 user services; add-ons such as Centrex and CLIP |
| TE1, TE2, TA, NT1, NT2 | Native ISDN terminal, legacy terminal, adapter, customer NT, optional PBX |
| Out-of-band signaling | Setup packets on D, not ring voltage on the user channel |
| HTTPS | Example of the logical protection the lecture says to use on any medium |

### Exam lines
- ISDN digitized the local loop: **B channels for payload, D for signaling**, BRI for homes, PRI for sites that need T1/E1-scale bundles.
- Digital operation **could** have made security easier, but ISDN was **rolled out with little security design**.
- Operational wins: shared pair, ~2 s setup, out-of-band signaling, device sharing; costs and special telco service are the downsides.
- Versus ADSL: ISDN can carry voice; ADSL is data-only and often **survives local power loss**.
- Security punchline: **don’t fetishize the medium**. Pick a **reputable ISP/modem**, assume **logical IP attacks**, and protect sensitive use with **HTTPS** (and similar).


---

## M28: Stream Control Transmission Protocol (SCTP)

### Learning focus
- Place SCTP as a **reliable, message-oriented** transport between UDP and TCP, aimed at telephony signaling over IP.
- Explain **multistreaming** (association vs TCP’s one stream) and **multihoming** (multiple IP addresses, failover not load-share in current implementations).
- Number data with **TSN**, **SI**, and **SSN**; contrast SCTP **packets/chunks** with TCP **segments**.
- Sketch the **12-byte general header**, chunk layout, and the **four-way handshake** (INIT, INIT ACK, COOKIE ECHO, COOKIE ACK).

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| SCTP | Reliable, message-oriented transport combining UDP’s boundaries with TCP’s reliability, plus streams and multihoming |
| Association | SCTP’s name for a connection (multihoming-aware) |
| TSN | 32-bit transmission sequence number on **data chunks** |
| SI / SSN | Stream identifier and per-stream sequence number on data chunks |
| Chunk | Control or data block; several per packet; control before data |
| Verification tag | Per-direction association identifier (needed because of multihoming) |
| CRC-32 | 32-bit packet checksum in the 12-byte general header |
| INIT / INIT ACK / COOKIE ECHO / COOKIE ACK | Four-way handshake chunks |
| rwnd | Advertised receive window (in INIT/INIT ACK so data can ride packets 3–4) |

### Exam lines
- SCTP exists because **SS7-style signaling and IP telephony** need **message boundaries and reliability together**, which neither UDP nor TCP fully gives.
- An **association** can carry **many streams** (head-of-line blocking on one stream does not freeze the others) and **many IPs** (failover; **not** load-sharing in “current” implementations).
- Numbering is **chunk-based**: **TSN** globally, **SI+SSN** per stream; **control never consumes TSN**.
- The on-wire unit is a **packet**: 12-byte header (ports, verification tag, CRC-32) plus padded chunks.
- Setup is **four-way** with a **cookie**, and **user data may already appear** in the third and fourth packets.


---

## M29: ATM Network Security Protocol

### Learning focus
- Define ATM as **asynchronous time-division multiplexing** of **fixed 53-byte cells** (5-byte header + 48-byte payload) on a **SONET/ISDN-style** backbone, with a VC set up **before** data.
- Decode **UNI vs NNI** headers (GFC, VPI, VCI, PT/EFCI/AUU, CLP, HEC) and name ABR/CBR/UBR/VBR.
- List ATM Forum–style security goals (confidentiality, AAL integrity, signaling signatures, availability functions) and ATM-specific threats (**VC stealing**, traffic analysis).
- Recite QoS/traffic parameters (PCR, SCR, CLR, CTD, CDV, BT/MBS, MCR), CAC, and the lecture’s ATM **disadvantages**.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| ATM cell | 5-byte header + 48-byte payload, hardware-switched |
| UNI / NNI | User–network vs network–network cell formats (GFC vs extra VPI bits) |
| VPI / VCI | Virtual path and channel IDs used for forwarding (and for VC-stealing attacks) |
| HEC | 8-bit header CRC; framing plus single-bit correct / multi-bit drop |
| AAL / AAL5 | Adaptation layer; AAL5 uses the AUU PT bit for packet boundaries |
| ABR / CBR / UBR / VBR | ATM bit-rate service classes |
| VC stealing | Compromised switches swap VPI/VCI to ride another user’s QoS |
| CAC | Connection admission control at setup for guaranteed QoS |
| Cell tax | 10% header overhead vs ~1% on Ethernet |
| NBMA | Non-broadcast multiple access — ATM has no native broadcast |

### Exam lines
- ATM’s security and performance story starts from **fixed cells and pre-established VCs** on a **SONET-class** fabric — good for **voice/video latency**, awkward for **surges** and **broadcast**.
- Header fields (**VPI/VCI, PT, CLP, HEC**) are both the switching mechanism and the **attack surface** (clear-text parties, CLP drops, false RELEASE).
- Forum-style security is **confidentiality, AAL checksums/sequence numbers, signed signaling, and a full management lifecycle** (log, alarm, audit, recover).
- Unique ATM threats taught here: **VC stealing** between colluding switches and **traffic/covert-channel analysis** despite encryption.
- QoS is a **traffic contract** (PCR/SCR/CLR/CTD/CDV/BT/MCR) plus **CAC**; unspecified QoS exists so the network is not wasted.
- The closer is practical: ATM **lost the LAN** to cheaper, simpler, more interoperable Ethernet despite remaining in some **telco backbones**.


---

## M30: Wireless Networks

### Learning focus
- Define a wireless network as radio (OSI physical layer) used to avoid cabling, and classify **WPAN, WLAN, WMAN, WWAN**.
- Describe Bluetooth **IEEE 802.15**: piconet/scatternet, 2.4 GHz ISM FHSS/GFSK, baseband/LMP/L2CAP, and the 72/54-bit frame.
- Explain IEEE 802.11 BSS/ESS, station mobility, **DCF (CSMA/CA)** vs **PCF**, why CSMA/CD fails, 802.11 MAC frame/types, and **hidden vs exposed station** (RTS/CTS).
- Outline WiMAX (IEEE 802.16), WWAN microwave/cellular (cells, BSC/MSC), and satellite networks as taught.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| WPAN / WLAN / WMAN / WWAN | Personal, local, metro, and wide-area wireless scopes |
| Piconet / scatternet | Bluetooth 1-master small net vs overlapping piconets |
| Parked state | Bluetooth secondary synced but not in the active seven |
| GFSK / FHSS 1600 hop/s | Bluetooth 2.4 GHz ISM modulation and hopping |
| BSS / ESS / AP | 802.11 building block, extended set, optional access point |
| DCF / PCF | CSMA/CA distributed access vs AP polling (PIFS < DIFS) |
| Hidden / exposed station | Collision because sender cannot hear a peer vs false deferral |
| RTS/CTS | Handshake that advertises duration so hidden nodes defer |
| WiMAX / IEEE 802.16 | Broadband WMAN |
| MSC | Mobile Switching Center in cellular |

### Exam lines
- Wireless is classified by **reach**: PAN (Bluetooth 802.15), LAN (Wi-Fi 802.11), MAN (WiMAX 802.16), WAN (microwave, cellular, satellite).
- Bluetooth is a **master-driven hopped piconet** (79×1 MHz, 1600 hop/s, GFSK) with a noisy-radio frame that **votes on a triple header** instead of retransmitting at baseband.
- 802.11 infrastructure is **BSS+AP**; ad hoc is BSS without AP. MAC is **CSMA/CA**, not CD, because of cost, **hidden nodes**, and fading.
- **RTS/CTS** mitigates hidden stations; the **exposed-station** problem is left as a capacity waste the handshake does not fully solve.
- Cellular **low-power cells + MSC** and satellites **cell-ize the planet** so coverage does not require cabling every site.


---

## M31: Wi-Fi Security Protocol

### Learning focus
- Distinguish **IEEE 802.11** (PHY/MAC specs) from the **Wi-Fi Alliance** brand, interoperability testing, and required **WPA/WPA2** plus **EAP**.
- Describe **FHSS vs DSSS** (chips), the 802.11 split into **PLCP/PMD**, MAC management, and **DCF (CSMA/CA)** vs **PCF**.
- Tabulate 802.11 / a / b / g / n / ac (and d, e, f, h, i, j, ad, af) with bands, modulation, rates, and ranges the lecture gives.
- Decode the 802.11 **MAC frame** and **Frame Control** bits, including the **WEP** body-encryption flag.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Wi-Fi Alliance | 1999 nonprofit that certifies 802.11 interoperability; requires WPA/WPA2 and EAP |
| FHSS / DSSS / OFDM / HR-DSSS | 802.11 PHY families (hops, chips, 54 Mbps+ OFDM, 11/22 Mbps HR-DSSS) |
| PLCP / PMD | PHY convergence (CCA) vs medium-dependent modulation |
| CSMA/CA | DCF access: sense idle, send full frame, binary exponential backoff on collision; virtual sensing via MACA |
| MIMO | Multiple antennas added in 802.11n (54–600 Mbps) |
| IEEE 802.11i | Security/authentication amendment: RADIUS, Kerberos, 802.1X |
| WEP | Wired Equivalent Privacy; Frame Control W bit means the body is WEP-encrypted |
| 802.11ad / WiGig | 60 GHz PHY, peak 7 Gbps |
| 802.11af / White-Fi | TV white-space WLAN, 54–790 MHz cognitive radio |

### Exam lines
- **IEEE writes 802.11; the Wi-Fi Alliance owns the logo** and, for certification, insists on **WPA/WPA2 and EAP** — that is this lecture’s primary “security protocol” statement.
- 802.11 is **PHY + MAC only**: PLCP/PMD below, DCF/PCF above, with MAC management for **associate, roam, authenticate, encrypt, sleep**.
- Rate/range progression taught: **1–2 Mbps (1997) → a/b (1999) → g (2003) → n MIMO (2009) → ac ~1.3 Gbps (2013)**, plus **ad (60 GHz)** and **af (TV white space)**.
- **802.11i** is the amendment that names **RADIUS, Kerberos, and 802.1X**.
- The MAC header’s four addresses and Duration field support **distribution-system forwarding and channel reservation**; the **W bit** flags **WEP** on the body.


---

## M32: Wi-Fi Security Protocol

### Learning focus
- State why IEEE 802.11 needed a confidentiality protocol and why WEP failed that role.
- Describe WEP’s two authentication methods and the RC4/CRC/IV encryption pipeline.
- List the design flaws, IV weakness, and the mitigations that still left WEP crackable in minutes.
- Explain WPA as draft IEEE 802.11i (TKIP + Michael) and WPA2 as the full 2004 standard (AES).
- Compare WPA and WPA2 on 802.1X/EAP, PSK, mix-mode, cryptography, and processing cost.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| WEP | Wired Equivalent Privacy — original 802.11 confidentiality algorithm (1997) |
| WPA | Wi-Fi Protected Access — 2003 interim / draft 802.11i using TKIP |
| WPA2 | Full IEEE 802.11i-2004 using AES |
| IEEE 802.11i | WLAN security standard implemented in two steps as WPA then WPA2 |
| Open System Authentication | Join path that does not actually authenticate; encryption keys applied later |
| Shared Key Authentication | Four-step WEP challenge–response using the same key later used to encrypt |
| RC4 | Stream cipher WEP uses with a 256-entry 8-bit lookup table |
| IV | Initialization vector concatenated with the WEP key; sent in the clear — the IV weakness |
| CRC | WEP integrity check on plaintext; too weak to stop alteration |
| TKIP | Temporal Key Integrity Protocol — per-packet 128-bit keys in WPA |
| Michael | WPA message integrity check; stronger than CRC, still flawed on short packets |
| AES | WPA2 block cipher: 128-bit blocks; 128/192/256-bit keys; 9/11/13 rounds as taught |
| 802.1X / EAP | Framework both WPA and WPA2 use for mutual authentication and dynamic keys |
| PSK | Pre-shared key mode for home / small office |
| Mix-mode | WPA2 ability to host WPA and WPA2 stations on one network |

### Exam lines
- Air is shared with hackers; 802.11’s first answer was WEP, designed to be **hard** to break and **optional**, not military-grade.
- WEP’s shared-key handshake reuses one key for auth and encryption and is **MITM-prone**; RC4 with a **clear IV** and **CRC** leaked keystream.
- Firmware-friendly **WPA/TKIP/Michael** was only a bridge to **802.11i**; Michael still allowed short-packet reinjection.
- **WPA2/AES** is the full 2004 standard: stronger crypto, authentication, key management, replay protection, and integrity — at higher CPU cost.
- Prefer WPA2; WPA is described as hackable, WPA2 as theoretically not. Both still share 802.1X/EAP, PSK, and 802.11a/b/g coverage.


---

## M33: Bluetooth Networks and Security Protocols

### Learning focus
- Place Bluetooth as a short-range UHF ISM WPAN technology and recount SIG / IEEE 802.15 origins.
- Draw a piconet and scatternet and state the master/slave communication rule.
- Walk the Bluetooth protocol stack, ACL vs SCO links, L2CAP roles, and the 54-bit header frame.
- Recite SIG versions from 1.0 through 4.2 and the IEEE 802.15.x WPAN family.
- Name Bluetooth’s three native security services and the four BR/EDR/HS security modes, including NIST’s warning on mode 1.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| WPAN | Wireless personal area network; Bluetooth’s setting |
| SIG | Bluetooth Special Interest Group (1998; 1,500-page v1.0 in 1999) |
| Piconet | Master + up to 7 active slaves within ~10 m |
| Scatternet | Piconets joined by a bridge node |
| ACL / SCO | Async connectionless data vs synchronous connection-oriented real-time (no retransmission, FEC) |
| L2CAP | Segmentation, multiplexing, QoS |
| RFCOMM | Serial-port emulation |
| Access code | Identifies the master so overlapping piconets can be distinguished |
| EDR | Enhanced Data Rate (v2.x): ~3 Mbps nominal, 2.1 Mbps practical, GFSK+PSK |
| HS | High Speed (v3.0): 24 Mbps over 802.11 after Bluetooth setup |
| LE / Wibree | Bluetooth Low Energy new stack inside v4.0 “Bluetooth Smart” |
| SSP | Secure Simple Pairing (v2.1); ECDH link keys in security mode 4 |
| 802.15.1–.10 | IEEE WPAN family: Bluetooth, coexistence, high/low rate, mesh, BAN, VLC, PAC, KMP, L2 routing |
| Security modes 1–4 | Non-secure; service-level; link-level mandatory crypto; SSP service-level |

### Exam lines
- Bluetooth is a complete SIG stack on cheap short-range ISM radios; IEEE 802.15 only standardizes PHY/MAC.
- A piconet is strictly **star-shaped**: no slave-to-slave path except through the master (or a scatternet bridge).
- Baseband TDD (625 µs), ACL vs SCO, and L2CAP fragmentation/mux/QoS are the operational core; audio/control can bypass L2CAP.
- Versions add hopping hygiene, EDR, SSP, 802.11 offload, LE, LTE coexistence, and longer PDUs — always backward compatible.
- Native security is **device** auth, confidentiality, and service authorization only. **Never use mode 1** (NIST). Mode 4 modernizes **key agreement** (ECDH) without changing the old auth/encryption algorithms.


---

## M34: Virtual Private Network

### Learning focus
- Contrast a leased-line private network with a VPN overlay on a public network.
- Name Access, Intranet, and Extranet VPNs and the four architectural components (client, NAS, VPN server, protocol).
- Reconstruct Layer-2 tunnel setup (PPP, LCP, PAP/CHAP, NCP) and the PPTP, L2F, and L2TP packet stories.
- Distinguish IPsec AH vs ESP and Layer-2 vs Layer-3 tunneling.
- State OpenVPN’s SSL/TLS properties and the lecture’s protocol preference; explain why firewalls and VPNs are used together.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Private network | Company hosts plus leased telephone lines |
| VPN | Overlay tunnels + encryption on a public non-secure network |
| NAS | Network Access Server at the ISP PoP |
| PAC / PNS | PPTP Access Concentrator / PPTP Network Server |
| LAC / LNS | L2TP Access Concentrator / L2TP Network Server |
| Home Gateway | L2F name for the VPN server |
| PAP / CHAP | PPP authentication used by Layer-2 VPNs |
| LCP / NCP | PPP link control / network control (IPCP etc.) |
| GRE | PPTP encapsulation; many firewalls lack it |
| AH / ESP | IPsec authentication-only vs encrypting payload |
| OpenVPN | SSL/TLS VPN via OpenSSL; not interoperable with IPsec/L2TP/PPTP |
| TAP | Virtual Ethernet device for OpenVPN bridging |

### Exam lines
- VPNs buy private-network **properties** without leased-line **cost**, via tunnels and encryption on the Internet.
- Layer 2 (PPTP/L2F/L2TP) is the dial-up/PPP world and can carry non-IP; IPsec is IP-only, router/firewall oriented, and has **no user authentication**.
- IETF folded PPTP+L2F into **L2TP**; encrypt L2TP with **IPsec** when possible.
- **Avoid PPTP.** Prefer **OpenVPN**; use **L2TP/IPsec** only for quick, non-critical, especially mobile, setups.
- A firewall pair without a tunnel still leaks on the Internet; **firewall + VPN** is stronger than either mechanism alone.


---

## M35: WiMAX Technology and its Security

### Learning focus
- Place Bluetooth as a short-range UHF ISM WPAN technology and recount SIG / IEEE 802.15 origins.
- Draw a piconet and scatternet and state the master/slave communication rule.
- Walk the Bluetooth protocol stack, ACL vs SCO links, L2CAP roles, and the 54-bit header frame.
- Recite SIG versions from 1.0 through 4.2 and the IEEE 802.15.x WPAN family.
- Name Bluetooth’s three native security services and the four BR/EDR/HS security modes, including the recommendation never to use mode 1.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| WPAN | Wireless personal area network; Bluetooth’s setting |
| SIG | Bluetooth Special Interest Group (1998; 1,500-page v1.0 in 1999) |
| Piconet | Master + up to 7 active slaves within ~10 m |
| Scatternet | Piconets joined by a bridge node |
| ACL / SCO | Async connectionless data vs synchronous connection-oriented real-time (no retransmission, FEC) |
| L2CAP | Segmentation, multiplexing, QoS |
| RFCOMM | Serial-port emulation |
| Access code | Identifies the master so overlapping piconets can be distinguished |
| EDR | Enhanced Data Rate (v2.x): ~3 Mbps nominal, 2.1 Mbps practical, GFSK+PSK |
| HS | High Speed (v3.0): 24 Mbps over 802.11 after Bluetooth setup |
| LE / Wibree | Bluetooth Low Energy new stack inside v4.0 “Bluetooth Smart” |
| SSP | Secure Simple Pairing (v2.1); ECDH link keys in security mode 4 |
| 802.15.1–.10 | IEEE WPAN family: Bluetooth, coexistence, high/low rate, mesh, BAN, VLC, PAC, KMP, L2 routing |
| Security modes 1–4 | Non-secure; service-level; link-level mandatory crypto; SSP service-level |

### Exam lines
- Captions for this playlist slot teach **Bluetooth**, not WiMAX: complete SIG stack on cheap short-range ISM radios; IEEE 802.15 only standardizes PHY/MAC.
- A piconet is strictly **star-shaped**: no slave-to-slave path except through the master (or a scatternet bridge).
- Baseband TDD (625 µs), ACL vs SCO, and L2CAP fragmentation/mux/QoS are the operational core; audio/control can bypass L2CAP.
- Versions add hopping hygiene, EDR, SSP, 802.11 offload, LE, LTE coexistence, and longer PDUs — always backward compatible.
- Native security is **device** auth, confidentiality, and service authorization only. **Never use mode 1**. Mode 4 modernizes **key agreement** (ECDH) without changing the old auth/encryption algorithms.


---
