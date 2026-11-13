# Volume 03 — Ethernet Security, High-Speed LAN, ISDN, SCTP, ATM, Wireless & VPN (M24–M35)

> Information Security (CEC) · Exam-readable notes
> Full concept coverage rewritten for understanding and answer writing (not the ultra-short notes-3).

---

## M24: Ethernet Security

### In one line
How Ethernet grew into the default wired LAN, why it was designed without security, what attacks hit a shared segment, and how segmentation, access control, and IEEE 802.1AE MACsec protect frames.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Frame | Ethernet’s on-wire data unit; only one station should transmit a frame at a time, or a collision occurs. |
| CSMA/CD | Carrier Sense Multiple Access with Collision Detection — sense the medium, allow multiple stations, detect collisions and retransmit. |
| IEEE 802.3 | LAN/MAN standard based on the 1980 DIX Ethernet 1.0 spec; standardized by IEEE in 1983. |
| VLAN hopping | Attacking by injecting VLAN-tagged frames or abusing VLAN management so a host reaches VLANs its port should not join. |
| STP TCN flood | DoS that floods Spanning Tree topology-change notifications (or other STP control) to disrupt the switching fabric. |
| IEEE 802.1Q / QinQ / PVLAN | VLAN tagging; double tagging; private VLANs that isolate hosts so they talk only via a promiscuous port (usually a router). |
| IEEE 802.1X / EAP | Port-based authentication: host authenticates to a switch that checks an authentication server, using Extensible Authentication Protocol methods. |
| DHCP snooping | Switch feature that binds MAC–IP–port from DHCP messages and can block ARP spoofing, limited to DHCP paths that switch can see. |
| MACsec (IEEE 802.1AE) | Hop-by-hop encryption and integrity for Ethernet MSDUs using SecTAG, SAK, PN, SCI, and ICV. |
| SecTAG / ICV / SAK / PN | MACsec security tag; integrity check value; Security Association Key; Packet Number used for Protect, Validate, and replay protection. |

### Concepts explained

**History and rates.** Ethernet roots: 1970s **ALOHAnet** (Norman Abramson, Hawaii) and Xerox’s ~**3 Mbps CSMA/CD** LAN. In **1980**, DEC/Intel/Xerox issued **10 Mbps Ethernet Version 1.0 (DIX)**; IEEE adopted it as **802.3 (1983)**. Media: copper (twisted pair, originally coax 10BASE5) and fiber; hubs/switches connect stations. Rate ladder taught: Ethernet **10**, Fast **100**, Gigabit **1000**, 10 Gigabit **10 000**, 100 Gigabit **100 000** Mbps; **400 Gbps** expected by early 2017 in the lecture’s timeline. Ethernet won the wired LAN war by **simplicity**, yet was always known as **insecure**.

**Why attacks are easy.** Security was **never a first-class design goal**. Almost every attack starts with **access to the target Ethernet segment** (insider rights or a public jack). Once on the wire, an attacker can learn topology/traffic, control switches/routers/servers, eavesdrop, manipulate data, or disrupt availability.

**Five attack classes**

1. **Network and system access** (prerequisite for the rest)
2. **Traffic confidentiality**
3. **Traffic integrity**
4. **Denial of service**
5. **System security** (named class; worked examples sit under the first four)

**Access methods:** unused switch port / wall socket; unplug a PC and plug in; insert a switch between PC and jack; rogue user switches or APs; VLAN management listen-and-join; VLAN tagging/hopping; remote takeover of a host (e.g. social-engineered remote admin that dials out); switch control via default/no passwords or physical password reset (reroute, drop links, claim STP root, DoS links).

**Confidentiality:** capture payload, passwords, and topology for later attacks.

**Integrity techniques**

| Technique | What it does |
|-----------|--------------|
| ARP poisoning | ARP reply: victim IP + attacker MAC → frames delivered to attacker |
| DHCP poisoning | Answer broadcast DHCP first; assign gateway/DNS/IP and steer traffic |
| MITM | Steer traffic through attacker; modify if no integrity check |
| Session hijacking | Higher-layer sessions stay trusted after setup; recreate session from eavesdropped state |

**DoS:** exhaust switch control/management plane; **STP** self-configuring tree — pretend to be a switch; flood **TCNs** / STP control to halt the fabric.

**Traditional mitigation:** treat the LAN as untrusted (building + firewall + trusted staff) and push crypto to **IPsec/TLS** — costly and incomplete.

**Solution groups**

| Approach | What it does / why it matters |
|----------|-------------------------------|
| Router segmentation | Replace central switch with IP router → separate broadcast domains; ARP/STP/VLAN/MAC-table attacks cannot cross. Cost: IP config; mobility harder than pure Ethernet. |
| Physical + VLAN access | Locked cabinets/walls; **802.1Q** security domains; **QinQ / PVLAN** isolate hosts behind one promiscuous router port. |
| ACLs | Vendor switch ACLs on MAC / EtherType (not native Ethernet). |
| 802.1X | Authenticate at session start; bind MAC to port via EAP + auth server. |
| MACsec | Encrypt/integrity-protect frames between authorized hosts and switches. |
| DHCP snooping | Harden ARP; limited visibility if DHCP path bypasses the switch. |
| Monitoring | Ethernet firewall/DPI; IDS/IPS rarely useful for Ethernet-network protection; good admin practice matters. |

**IEEE 802.1AE MACsec.** Keeps DA/SA unchanged; inserts **SecTAG** before user data and **ICV** after. Facilitates correct connectivity, DoS isolation, localizing attack sources, shared public LAN infrastructure for suspicious customers, org-to-org LAN transit, and incremental deployment.

SecTAG carries **TCI, AN, PN, SCI**. Transmit: assign frame to **SA** via **AN** → lookup **SAK** and next **PN** → Protect → ICV + secure data. Receive: map AN/SCI → SA/SAK → Validate over DA, SA, SecTAG, data, ICV → **replay check** (PN ≥ lowest acceptable PN) → update lowest PN on success.

### How to answer
- Ethernet won by simplicity, not security; design never treated security as a primary goal.
- Almost every Ethernet attack starts with **segment access** (jack, rogue AP/switch, VLAN tricks, stolen switch, remotely owned host).
- Name concrete threats: eavesdropping; ARP/DHCP poisoning, MITM, session hijack; STP/resource DoS.
- Classic answer was “dirty LAN + firewall + IPsec/TLS”; incomplete and expensive.
- Routers cut broadcast-domain attacks; 802.1Q/PVLAN/ACLs/802.1X limit who is on the wire; DHCP snooping hardens ARP.
- **MACsec (802.1AE)** encrypts and integrity-protects frames hop-by-hop with SecTAG/ICV and PN-based replay protection.

---

## M25: Gigabit Ethernet

### In one line
Gigabit Ethernet delivers 1 Gbps while keeping IEEE 802.3 frames and MAC modes, with a GMII/PCS/PMA/PMD stack, fiber and copper PHYs, and carrier extension for half-duplex reach.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Gigabit Ethernet | 1000 Mbps / 1 Gbps IEEE 802.3 family — ten times Fast Ethernet. |
| 1000BASE-X | IEEE 802.3z fiber/short-copper group (SX, LX, CX; ZX as vendor term). |
| 1000BASE-T | IEEE 802.3ab Gigabit over Cat 5/5e/6 UTP. |
| GMII | Gigabit Media Independent Interface between MAC and PHY (extends Fast Ethernet MII). |
| 8B/10B | PCS coding: 8 data bits mapped to 10-bit code groups (Fibre Channel style), fed to PMA at 125 MHz. |
| Packet bursting | Half-duplex CSMA/CD enhancement: burst small packets to fill the 1 Gbps pipe. |
| IEEE 802.3x | Full-duplex operation and flow control used when Gigabit is not sharing the wire. |
| Carrier extension | Extra symbols counted in the collision window so classic min/max frame sizes still work at 1 Gbps distances; FCS ignores the extension. |
| Length/Type | Field ≤1500 → LLC length in Data; >1500 → optional Ethernet type ID. |

### Concepts explained

**Why 1 Gbps.** Capacity demand is always underestimated. After Fast Ethernet took the desktop/horizontal market, **100 Mbps backbones** could not aggregate many Fast Ethernet segments. Gigabit was the next generation at **1 Gbps**, keeping the **same frame format, size, and media-access method** as 10/100 Ethernet so shops need not move backbones to **ATM** or **FDDI**.

**Standards**

| Standard | Year | What it defined |
|----------|------|-----------------|
| IEEE 802.3z | June 1998 | Initial Gigabit; optical fiber required; **1000BASE-X** (CX, SX, LX; vendor ZX) |
| IEEE 802.3ab | 1999 | **1000BASE-T** on Cat 5/5e/6 — desktop Gigabit on existing copper |
| IEEE 802.3ah | 2004 | EFM PHYs **1000BASE-LX10**, **1000BASE-BX10** |

**Design objectives:** 10× Fast Ethernet bandwidth; same 802.3 frame; same half/full-duplex MAC schemes; backward compatible with 10/100; support existing Ethernet-family protocols.

**Features:** same frame → easy integration; full duplex for switch–switch and switch–station (most shipping products — no shared contention); half duplex still uses CSMA/CD + **packet bursting**; fiber or Cat 5/6; cheaper than routing for LAN/MAN/WAN stitching of identical frames (no fragmentation/reassembly/address translation).

**Stack:** MAC (10/100/1000, half or full) → **GMII** (8-bit TX/RX, carrier present, collision absent; reuses MII management) → **PCS** (8B/10B, CS/CD for half duplex, **auto-negotiation** of speed and duplex) → **PMA** (serialize 10-bit groups at **125 MHz**) → **PMD + MDI** (connectors and medium-specific signaling).

**Physical types (reach/cabling decide the choice)**

| PHY | Medium / λ | Reach (as taught) |
|-----|------------|-------------------|
| 1000BASE-SX | MMF, 850 nm | ~220 m on 62.5/125 μm; ≥500 m on modern 50/125 μm |
| 1000BASE-LX | Laser ~1300/1310 nm (1270–1355) | 5 km on 10 μm SMF; vendors often 10–20 km; >300 m may need launch-conditioning patch |
| 1000BASE-CX | Balanced STP copper | Max **25 m**; blade niches; T succeeded it for general wiring |
| 1000BASE-T | UTP Cat 5/5e/6 | Desktop copper Gigabit (do not confuse with TIA’s different **1000BASE-TX**) |
| 1000BASE-KX | 802.3ap backplane | 1–4 lanes, megabit to 10 Gbps class backplane links |
| 1000BASE-LX10 | Pair of 1310 nm SMF | Up to **10 km** |
| 1000BASE-BX10 | Single SMF strand | 10 km; downstream **1490 nm**, upstream **1310 nm** (ends not interchangeable) |
| 1000BASE-EX (industry) | Pair SMF, 1310 nm | Up to **40 km** |
| 1000BASE-ZX (vendor) | 1550 nm SMF | ≥**70 km** (some EZX to 120 km) |

**Hardware upgrade path:** Gigabit NICs; aggregating switches; Gigabit switches; Gigabit repeaters.

**Duplex and MAC.** Half duplex: send **or** receive; CSMA/CD + bursting. Full duplex: both ways → up to **2 Gbps** aggregate, longer reach, **no CSMA/CD**, uses **802.3x** flow control — preferred for backbones and servers.

**Basic frame fields:** Preamble 7 B; SOF/SFD 1 B; DA 6 B (I/G and G/L bits); SA 6 B (always individual); Length/Type 2 B; Data ≤1500 B (pad to 46 if short); FCS 4 B CRC-32 over DA…Data.

**Carrier extension:** keeps IEEE 802.3 min/max sizes interoperable at Gigabit distances. Extension symbols are **in the collision window** (whole extended frame collides or drops) but **FCS covers only the original frame**; receiver strips extension before FCS check.

### How to answer
- Gigabit exists because Fast Ethernet desktops overflowed 100 Mbps backbones; same **802.3 frames** avoid ATM/FDDI backbone swaps.
- Architecture: **MAC → GMII → PCS (8B/10B, auto-neg) → PMA (125 MHz) → PMD**.
- Choose PHY by **reach and existing cabling** (SX/LX/LX10/BX10/EX/ZX vs CX then T).
- Shipping default is **full duplex** (up to 2 Gbps both ways, no CSMA/CD); half duplex needs CSMA/CD + burst + **carrier extension**.
- Frame is classic Ethernet; **carrier extension** is the Gigabit-specific MAC trick for distance/interoperability.

---

## M26: 10 Gigabit Ethernet

### In one line
10 Gigabit Ethernet sends Ethernet frames at 10 Gbps on full-duplex point-to-point links only, with an RS/PCS/PMA/PMD stack, optional WIS for SONET WAN, and a family of LAN/WAN/copper/backplane/EPON PHYs.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| 10 GbE / 10G / 10 GigE | Technologies that transmit Ethernet frames at 10 Gbps; **full duplex only**. |
| IEEE 802.3ae-2002 | First 10G Ethernet standard for LAN/WAN fiber. |
| 10GBASE-R / W / X | Coding families: LAN fiber, WAN fiber, copper. |
| XGMII | 10 Gigabit Media Independent Interface between MAC and PHY. |
| WIS | WAN Interface Sublayer — simplified SONET framing between serial PCS and PMA. |
| 64B/66B | Serial LAN PCS coding; LAN PHY line rate about **10.3 / 10.3125 Gbps**. |
| HSSG | Higher Speed Study Group (March 1999) that started 10G work. |
| 10GBASE-T | IEEE 802.3an twisted-pair 10G (Cat 6 **55 m**; Cat 6A/7 **100 m**). |
| 10GBASE-PR | IEEE 802.3av 10G EPON PHY with PR10/PR20/PR30 power budgets. |

### Concepts explained

**What 10G is.** As high-speed demand grew, a faster Ethernet was needed. The **Higher Speed Study Group (HSSG)** formed in **March 1999**. 10 Gigabit Ethernet (also **10G**, **10GbE**, **10 GigE**) is a group of technologies that transmit Ethernet frames at **10 billion bits/s**, first defined by **IEEE 802.3ae-2002**. It is presented as a telecommunication technology as well as a LAN technology.

Unlike earlier Ethernet, **10 GbE defines only full-duplex point-to-point links**, generally via network switches. **Shared-medium CSMA/CD was not carried forward. Half duplex and hubs do not exist** in 10GbE. It can use copper or fiber, but bandwidth forces higher-grade copper: **Category 6, 6A, or 7** for links up to **100 m**.

**Why drop half duplex.** Original Ethernet’s half duplex used CSMA/CD on a shared medium; many people wrongly treat CSMA/CD as “standard Ethernet.” Half duplex’s problems are **efficiency** and **distance**: link distance is limited by minimum MAC frame size, which hurts high-rate efficiency. At **10 Gbps**, half duplex is not attractive; no realistic market exists because most 10 Gbps links are **point-to-point optical**. Full duplex has **no contention**: the MAC may send whenever the peer is ready. So the 10G standard specifies **full duplex only**.

**IEEE documents taught**

| Document | Year | Scope |
|----------|------|-------|
| 802.3ae | 2002 | 10 Gbps fiber LAN and WAN |
| 802.3ak | 2004 | 10 Gbps twinax |
| 802.3-2005 | 2005 | Base-standard revision |
| 802.3an | 2006 | Twisted-pair copper |
| 802.3ap | 2007 | Backplane Ethernet (1 and 10 Gbps) |
| 802.3aq | 2006 | MMF with enhanced equalization |
| 802.3-2008 | 2008 | Another base revision |
| 802.3av | 2009 | 10G EPON PHY |
| 802.3-2012 | 2012 | Lecture’s “latest” base standard |

**Layered architecture.** Ethernet implements OSI **data link** and **physical**. Mapping: OSI physical → **PMD, PMA, PCS, Reconciliation Sublayer (RS)**; toward the network → **MAC + LLC**. **RS** is a command translator: maps MAC terminology/commands into electrical formats for PHY entities. **MAC** initializes, controls, and manages the peer connection. **XGMII** is the standard MAC↔PHY interface that isolates the MAC so it can run over various PHYs. **MDI** = connector types per medium/PMD.

Basic media families: **10GBASE-R** (LAN fiber), **10GBASE-W** (WAN fiber), **10GBASE-X** (copper coding family).

| Sublayer | Role |
|----------|------|
| PMD | Amplify, modulate, wave-shape on the wire/fiber; different PMDs for different media |
| PCS | Coding plus serializer/multiplexing; structure distinguishes LAN vs WAN |
| PMA | Serializes code groups into a bit stream (and reverse); supports multiple encodings |
| WIS | WAN only: simplified SONET framing between serial PCS and serial PMA |

**LAN PCS modes.** WAN PHY: PCS operates serialized. LAN PHY: (1) **parallel** — multiplexer puts data on **four 2.5 Gbps** lines; (2) **serial** — single channel with **64B/66B** coding. Serial LAN PHY **line rate ~10.3 Gbps** (commonly **10.3125 Gbps**).

**Serial vs parallel PHY implementations.** **Serial:** one high-speed 10 Gbps PCS–PMA–PMD block; one physical channel. TX: RS → PCS encode → PMA serialize → PMD at 10 Gbps. Advantage: straightforward; no complicated mux/demux. **Parallel:** **n subchannels** (parallel cables or **WDM**). A distributor multiplexes MAC data round-robin into n streams, each at **(10/n) Gbps**. Advantage: cheaper CMOS/bipolar parts. Disadvantages: distributor/collector sensitive to **timing jitter**; multiple logic sets and lasers.

**MAC and frame.** Same addresses and frame formats as earlier Ethernet, but **no half duplex**. Can support rates less than 10 Gbps via a **pacing mechanism** for rate adaptation and flow control. Point of 10G was to **keep the same MAC frame** for seamless integration. With full duplex, **link distance does not affect MAC frame size**. **Minimum MAC frame size is 64 octets**; **carrier extension is not required.**

| Field | Size | Meaning |
|-------|------|---------|
| Preamble | 7 B | Alternating 1/0; announces frame; PHY sync |
| SFD | 1 B | Ends in two 1s; next bit is leftmost of DA |
| DA / SA | 6 B each | Same I/G and G/L rules as Gigabit |
| Length/Type | 2 B | ≤1500 → LLC length; optional type ID |
| Data | ≤1500 B | Pad to 46 if short |
| FCS | 4 B | CRC-32 over DA…Data |

**PHY families**

1. **LAN fiber (R):** SR, LRM, LR, ER, LX4, ZR  
2. **WAN fiber (W):** SW, LW, EW (same fiber types/distances as SR/LR/ER under 802.3ae)  
3. **Copper / backplane:** CX4, T, KX4, KR  
4. **EPON:** PR  

| LAN PHY | Medium / λ | Line rate | Reach | Std |
|---------|------------|-----------|-------|-----|
| 10GBASE-SR | Serial MMF 850 nm | 10.3125 Gbps | 300–400 m | 802.3ae |
| 10GBASE-LR | SMF 1310 nm, 64B/66B | 10.3125 Gbps | 10 km | 802.3ae |
| 10GBASE-ER | SMF 1550 nm | 10.3125 Gbps | 40 km (vendors to 80) | 802.3ae |
| 10GBASE-LX4 | WDM 1310 nm; 4 lasers × 3.125 Gbps | — | 300 m MMF / 10 km SMF | 802.3ae (being replaced by LRM) |
| 10GBASE-LRM | 1310 nm FDDI-grade 62.5 μm MMF | 10.3125 Gbps | 220 m (802.3aq) | 802.3aq |

Despite the name **LAN**, fiber can run **up to 80 km** in some cases. LAN PHY is the most common optical variety used directly between routers and switches.

**Copper/backplane.** **10GBASE-CX4** (802.3ak): four lanes each direction over InfiniBand 4X twinax (8-pair), **15 m** max, **lowest cost per port**, each lane ~**3.125 GHz**. **10GBASE-T** (802.3an, 2006): Cat 6 **55 m**; Cat 6A/7 **100 m**. **10GBASE-KX4** and **10GBASE-KR** (802.3ap): blade servers / modular routers; must work with **≤1 m copper PCB + two connectors**; new backplanes prefer **KR** (single lane) over KX4 (four lanes).

**10GBASE-PR (802.3av):** 10G Ethernet PHY for passive optical networks. Downstream **1577 nm** lasers at **10.3125 Gbps** point-to-multipoint; upstream **1270 nm**. Three power budgets: **10GBASE-PR10, PR20, PR30**.

### How to answer
- 10 GbE is still Ethernet frames, but **only full-duplex switched P2P** — CSMA/CD and hubs are gone because half duplex at 10 Gbps has no market.
- Stack: **RS + PCS/PMA/PMD + XGMII**; WAN adds **WIS/SONET**.
- Implementers choose **serial 10G** (simple) or **n lanes/WDM** (cheaper silicon, more jitter and optics).
- MAC frame is familiar **64-octet minimum**; **no carrier extension**.
- Organize PHYs as **LAN-R, WAN-W, copper/backplane, EPON-PR**; remember **10.3125 Gbps** serial LAN line rate.

---

## M27: ISDN

### In one line
ISDN is the ITU/CCITT digital circuit- and packet-switched voice/data service over telephone copper, with BRI/PRI B and D channels, reference-point architecture, and a security punchline that logical protection beats the medium.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| ISDN | Integrated Services Digital Network — ITU/CCITT standards for digital circuit-switched (and packet) voice/data over ordinary telephone-grade copper and other media. |
| B channel | Bearer channel, typically **64 kbps** (sometimes 56), carries user voice/data. |
| D channel | Delta/data channel for signaling and control (**16 kbps** BRI, **64 kbps** PRI). |
| BRI / 2B+D | Basic Rate Interface: 2×64 + 16 = **144 kbps**, for individual users. |
| PRI / 23B+D / 30B+D | Primary Rate: North American–style **1.536 Mbps** (23B+D) or E1-style **1.984 Mbps** (30B+D). |
| B-ISDN | Broadband ISDN on fiber, **155–622 Mbps and beyond**. |
| Bearer / teleservice / supplementary | Network functions (OSI 1–3); end-user services (OSI 4–7); add-ons such as Centrex and calling-line ID. |
| TE1, TE2, TA, NT1, NT2 | Native ISDN terminal; legacy terminal; terminal adapter; customer network termination; optional PBX. |
| Out-of-band signaling | Call setup as digital packets on the D channel, not ring voltage on the user B channel. |
| HTTPS | Example of logical end-to-end protection the lecture says to use on any access medium. |

### Concepts explained

**From POTS to ISDN.** Analog **POTS** (Post Office Telephone Service name stuck) used copper to the CO with operator routing and line noise. From the **1960s**, digitization and switching advanced; **CCITT → ITU-T** pushed ISDN from **1984**. Early US implementations (Northern Telecom, AT&T) failed to interoperate; **National ISDN 1 (NI-1)** restored compatibility with proprietary gear. Digital nature **could** ease security, but ISDN was **rolled out with little security design**.

**Channels.** Voice/data ride **B** at 64 (or 56) kbps vs analog ~52 kbps cited. **D** carries setup/teardown and B-related signaling at 16 or 64 kbps. Future **B-ISDN**: voice+data+video on fiber at 155–622+ Mbps.

**BRI vs PRI**

| Interface | Structure | Total |
|-----------|-----------|-------|
| BRI | 2×64 B + 1×16 D | 144 kbps |
| PRI (N. America–style) | 23×64 B + 1×64 D | 1.536 Mbps (like channelized T1) |
| PRI (E1-style) | 30 B + D | 1.984 Mbps (E1 2.048 Mbps fabric) |

One D can control more than 23 B channels, so a **24B** circuit is possible if another PRI supplies control.

**Three service classes.** **Bearer** (OSI 1–3): e.g. 64 kbps 8 kHz-structured speech — network may transform speech without bit integrity. **Teleservices** (OSI 4–7): telephony, fax, teletex on B with D control. **Supplementary:** Centrex, call transfer, call waiting, calling line ID — also apply to packet data calls.

**How it uses the pair.** Analog offers one channel at a time; ISDN logically splits the same pair into multiple B/D channels (often one B voice, one B data on BRI).

**Components and reference points**

| Component | Role |
|-----------|------|
| TE1 | Native ISDN phone/PC/fax |
| TE2 | Legacy analog/modem gear |
| TA | Adapts TE2 (and e.g. Ethernet) to ISDN |
| NT1 | End of telco local loop / start of CPE |
| NT2 | Optional PBX (usually absent in homes) |
| LT / ET | Telco physical / logical exchange termination |

Reference points: **R** (TE2–TA); **S/T** coincide as S/T bus without NT2; **U, V** on telco side with LT/ET. ITU standards cover OSI **physical, data-link, network**.

**ISDN vs ADSL**

| | ISDN | ADSL |
|--|------|------|
| Service | Two voice channels **or** one ~128 kbps data channel | Data-only |
| Power | Needs local power — **dies if local power fails** | Copper often **stays up** without local power |

**Advantages:** multiple digital channels on one pair; BRI bonding (BONDING / Multilink PPP) to uncompressed **128 kbps**; PRI to ~**1920 kbps**; many devices share one line; call setup ~**2 s** vs 30–60 s analog; **out-of-band** D signaling does not steal B bandwidth.

**Disadvantages:** costlier than ordinary telephony; special Digital Services required.

**Security conclusion.** Physical tapping of slow dial-up POTS can be easier than tapping newer/encrypted media, but **most attacks are logical** (hack ISP or customer modem/PC over IP from afar). Physical spying still exists for targeted victims (TEMPEST, optical keyboard capture). Advice for DSL/T1/cable/ISDN: pick a **reputable ISP/modem**; assume logical IP attacks; never do sensitive work without **HTTPS** (or similar).

### How to answer
- ISDN digitizes the local loop: **B for payload, D for signaling**; BRI for homes, PRI for T1/E1-scale sites.
- Digital design **could** have helped security, but deployment largely ignored it.
- Wins: shared pair, ~2 s setup, out-of-band signaling, device sharing; costs and special telco service are downsides.
- Versus ADSL: ISDN can carry voice; ADSL is data-only and often survives local power loss.
- Security punchline: **don’t fetishize the medium** — reputable ISP/modem + logical protection (**HTTPS**).

---

## M28: Stream Control Transmission Protocol (SCTP)

### In one line
SCTP is a reliable, message-oriented transport between UDP and TCP, built for telephony signaling over IP, with multistreaming, multihoming, chunk packets, and a four-way cookie handshake.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| SCTP | Reliable, message-oriented transport combining UDP’s message boundaries with TCP’s reliability, plus streams and multihoming. |
| Association | SCTP’s name for a connection (aware of multiple IPs per end). |
| TSN | 32-bit Transmission Sequence Number on **data chunks** (randomly initialized). |
| SI / SSN | Stream Identifier and per-stream Stream Sequence Number on data chunks. |
| Chunk | Control or data block; several per packet; control chunks come before data. |
| Verification tag | Per-direction association identifier needed because of multihoming. |
| CRC-32 | 32-bit packet checksum in the 12-byte general header. |
| INIT / INIT ACK / COOKIE ECHO / COOKIE ACK | Four-way handshake chunks that establish an association. |
| rwnd | Advertised receive window (carried in INIT/INIT ACK so data can ride packets 3–4). |

### Concepts explained

**Why SCTP.** Stream Control Transmission Protocol is a **reliable, message-oriented transport-layer protocol**. In the Internet suite it sits between application and network like TCP and UDP. It was designed for apps that need more sophisticated service than TCP:

| Application | Role |
|-------------|------|
| IUA | ISDN over IP |
| M2UA, M3UA | Telephony signaling |
| H.248 | Media Gateway Control |
| H.323 | IP telephony |
| SIP | IP telephony |

SCTP provides the enhanced performance and reliability those apps need. It uses **well-known ports in the TCP port space** (IUA **9901**, M2UA **2904**, M3UA **2905**, H.248 **2949**, H.323 **1718/1719/1720**, SIP **5060**).

**UDP vs TCP vs SCTP.** UDP is **message-oriented**: boundaries conserved; messages independent — desirable for IP telephony — but **unreliable** (loss, duplication, reordering) with **no congestion or flow control**. TCP is **byte-oriented**: messages become a byte stream in segments; **no message boundaries**; **reliable** with congestion and flow control. **SCTP combines the best of both:** preserves message boundaries **and** detects lost/duplicate/out-of-order data, with congestion and flow control, plus features neither UDP nor TCP has.

| | UDP | TCP | SCTP |
|--|-----|-----|------|
| Orientation | Message | Byte stream | Message |
| Boundaries | Preserved | Lost | Preserved |
| Reliability | No | Yes | Yes |
| Congestion/flow control | No | Yes | Yes |
| Extra | — | One stream | Multistream + multihoming |

**Services offered**

- **Process-to-process communication** via ports as above.
- **Multiple streams:** a TCP connection is one stream; a loss anywhere blocks the rest — bad for real-time audio/video. SCTP allows **multistream service** in each connection (**association**). If one stream blocks, others still deliver (highway lanes: regular vs carpool).
- **Multihoming:** TCP uses one source IP and one destination IP even if a host is multihomed. An SCTP association lets each end define **multiple IP addresses**. If one path fails, another interface continues — fault tolerance for Internet telephony. Example: client on two LANs, server on two networks → four IP pairs, but **current implementations use only one pair for normal communication**; the alternative is **failover only**. **SCTP does not currently allow load sharing** across paths.
- **Full-duplex** like TCP (send and receive buffers at each end).
- **Connection-oriented:** establish association, exchange data both ways, terminate — but named **association** to emphasize multihoming.
- **Reliable service** with acknowledgements (like TCP).

**TSN, SI, SSN, packets vs segments.** TCP’s data unit is a **byte**. SCTP’s data unit is a **data chunk**, which may or may not be 1:1 with an application message because of **fragmentation**. Transfer is controlled by numbering chunks. **TSN** (32 bits, randomly initialized in 0…2³²−1) plays TCP’s sequence-number role; every data chunk must carry its TSN. **SI** (16-bit, from 0) places the chunk in the right stream. **SSN** orders chunks **inside that stream**.

An SCTP **packet** plays the role of a TCP segment. Differences:

| TCP segment | SCTP packet |
|-------------|-------------|
| Control in the header | Control is **control chunks** of several types |
| Data is one entity | Several **data chunks**, possibly different streams |
| Optional options field | **No options**; new features = new chunk types |
| Mandatory header 20 bytes | General header **12 bytes** |
| Sequence number in header | **TSN in each data-chunk header** |
| ACK and window in header | ACK and window in **control chunks** |
| Header length needed | Fixed 12-byte header, no HL |
| Urgent pointer | None |
| Checksum 16 bits | Checksum **32 bits (CRC-32)** |
| Connection ID = IP + ports | Multihoming ⇒ **verification tag** |
| Some control segments consume a sequence number | **Control chunks never use TSN, SI, or SSN** |

Control chunks come **before** data chunks in a packet. Acknowledgements of data are **chunk/TSN-oriented**; control chunks are acked by the right control type (INIT by INIT ACK) — no sequence/ACK number needed for that.

**Worked packing idea.** Process A sends 11 messages on three streams (4 + 3 + 4). If each message is one data chunk and the network allows only three data chunks per packet → four packets. Each data chunk needs **TSN** (cumulative, flow/error control), **SI**, and **SSN** (starting at 0 per stream).

**Packet format.** Mandatory **12-byte general header** + variable-length chunks:

| Field | Size | Role |
|-------|------|------|
| Source port | 16 bits | Sending process |
| Destination port | 16 bits | Receiving process |
| Verification tag | — | Matches packet to this association; stops old-association packets; **separate tag each direction**; repeated in every packet |
| Checksum | 32 bits | CRC-32 over the packet including header |

Chunks share Type (8), Flags (8), Length (16); information padded to a multiple of 4 bytes; chunks end on a 32-bit boundary. Up to 256 chunk types possible.

**Four-way handshake** (client initiates toward a prepared server)

1. Client → server **INIT** (general-header verification tag **0**): initiate tag for server→client packets, initial TSN, advertises **rwnd** (normally in SACK, but needed here because data may ride packets 3–4). **No other chunks** with the first packet.
2. Server → client **INIT ACK** (tag = client initiate tag): server initiate tag, initial TSN server→client, server rwnd, and a **cookie** defining the server’s state at that moment.
3. Client → server **COOKIE ECHO** — echoes the cookie **unchanged**; **data chunks allowed**.
4. Server → client **COOKIE ACK**; **data chunks allowed** here too.

### How to answer
- SCTP exists because SS7-style signaling and IP telephony need **message boundaries and reliability together**.
- An **association** can carry **many streams** (avoids head-of-line blocking across streams) and **many IPs** (failover, not load-share in current implementations).
- Numbering is **chunk-based**: TSN globally, SI+SSN per stream; control never uses TSN.
- On-wire unit: **12-byte header** (ports, verification tag, CRC-32) + padded chunks (control before data).
- Setup is **four-way with a cookie**; user data may appear in packets 3 and 4.

---

## M29: ATM Network Security Protocol

### In one line
ATM switches fixed 53-byte cells on pre-established virtual circuits over SONET-class fabrics, with UNI/NNI headers, Forum-style security goals, ATM-specific threats (VC stealing, traffic analysis), and traffic-contract QoS.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| ATM cell | Fixed unit: **5-byte header + 48-byte payload**, hardware-switched. |
| UNI / NNI | User–Network vs Network–Network cell formats (GFC vs extra VPI bits). |
| VPI / VCI | Virtual Path and Virtual Channel identifiers used for forwarding (and for VC-stealing attacks). |
| HEC | 8-bit header CRC (polynomial x⁸+x²+1): framing, single-bit correct, multi-bit drop. |
| AAL / AAL5 | ATM Adaptation Layer that segments messages into cells; AAL5 uses the AUU PT bit for packet boundaries. |
| ABR / CBR / UBR / VBR | Available, Constant, Unspecified, and Variable bit-rate service classes. |
| VC stealing | Compromised switches swap VPI/VCI so one user rides another’s QoS path. |
| CAC | Connection Admission Control — accept a new VC only if resources can meet the QoS contract. |
| Cell tax | ~**10%** header overhead vs ~**1%** on Ethernet. |
| NBMA | Non-Broadcast Multiple Access — ATM has no native broadcast/multicast. |

### Concepts explained

**What ATM is.** Asynchronous Transfer Mode is a switching technique that uses **asynchronous time-division multiplexing** to encode data into **small fixed-size cells**. That differs from Ethernet or the Internet, which use variable-size packets/frames. ATM is called the **core protocol over the SONET backbone of ISDN**.

**Why cells.** Voice is packetized and must share a network with bursty data. However small the voice packets, they would otherwise meet full-size data packets and suffer **maximum queueing delay** — so all data units should be the same size. Fixed cells can be **switched in hardware** without the delays of routed frames and software switching. ATM **creates fixed routes between two points before transfer**, unlike TCP/IP where packets may take different routes. That makes usage accounting easier, but an ATM network is **less adaptable to a sudden traffic surge**. It provides data-link services on OSI layer-1 physical links and behaves like a mix of small packet switching and circuit switching — suited to real-time low-latency traffic (VoIP/video) and high-throughput file transfers. A **virtual circuit must exist before endpoints exchange data**.

**Bit-rate classes**

| Class | Meaning |
|-------|---------|
| ABR (Available) | Guaranteed minimum capacity; may burst higher when the network is idle |
| CBR (Constant) | Fixed rate, steady stream — analogous to a leased line |
| UBR (Unspecified) | No throughput guarantee; delay-tolerant apps such as file transfer |
| VBR (Variable) | Specified throughput but not sent evenly — popular for voice/video conferencing |

**Cell structure.** **5-byte header + 48-byte payload**. Two formats: **UNI** (most links) and **NNI**.

| Field | Size | Notes |
|-------|------|--------|
| GFC | 4 bits (UNI) | Default 0; local flow control / sub-multiplexing (like two ISDN phones on one BRI) |
| VPI | 8 UNI / 12 NNI | Path identifier |
| VCI | 16 bits | Channel identifier |
| PT | 3 bits | Special cell kinds |
| CLP | 1 bit | Which cells to drop first in congestion |
| HEC | 8 bits | CRC polynomial x⁸+x²+1 |

**PT field.** MSB=1 → network management cell (other bits: segment OAM, end-to-end OAM, resource management, reserved). MSB=0 → user data: bit 2 = **EFCI** (congestion experienced); bit 1 = **AUU** used by **AAL5** to mark packet boundaries. HEC drives CRC-based framing that finds cell boundaries with no extra overhead; corrects single-bit header errors; on multi-bit errors, current and subsequent cells are dropped until a good header appears. NNI reallocates GFC bits to VPI (12-bit VPI).

**Interfaces and layers.** Public/private UNI; private/public NNI; **DXI** between packet routers and ATM DSUs. **AAL** breaks application messages into cells. **ATM layer:** transmission, switching, reception, congestion control, buffer management, cell-header generation/removal, reset connection identifiers for the next hop, cell address translation, sequential delivery. Physical: e.g. SONET.

**ATM Forum security services**

- **Data confidentiality** — data available only to intended, authorized parties.
- **Data integrity and authentication** — AAL frames protected by appending a **cryptographic checksum**; reordering protection via a **sequence number in AAL frames before** that checksum.
- **Signaling protection** — digital signature in an **information element (IE)**, especially with **SME (security message exchange)**. SETUP and CONNECT protected by signing IE fields specified by SME; protection also offered for RELEASE, STATUS, RESTART and for SETUP/CONNECT if SME is not used (sign part of the IE).
- **Availability / security system functions:** verify identities; controlled access/authorization; protect confidentiality and integrity; strong accountability; activities logging; alarm reporting; audit; security recovery; **security management**. If the system cannot recover and stops providing security services, it is **no longer secure**.

**Threats.** Typical: eavesdropping, spoofing, service denial, **VC stealing**, **traffic analysis**. The last two are taught as ATM-specific.

- **Eavesdropping:** fiber does not make tapping magically impossible.
- **Spoofing:** impersonate a user; may need PDU tools / special access; public ATM subject to this via Internet interconnect.
- **Service denial:** connection-oriented VCs managed by signals. False **RELEASE** or **DROP PARTY** to any intermediate switch disconnects the VC; frequent abuse disables QoS and can block users entirely when combined with eavesdropping.
- **VC stealing:** two compromised switches A and B swap VPI/VCI so U1’s cells ride U2’s path and back. Intermediate switches forward on VCI/VPI and will not notice. In ATM with **guaranteed QoS**, U1 can steal a higher-quality channel they are not entitled to (worse in ATM internetworking across organizations).
- **Traffic analysis / covert channels:** volume, timing, and clear header parties remain even if payload is encrypted; covert channels may encode info in timing, volume, VCI, or session keys.

**Traffic management and QoS.** Users specify at setup:

| Parameter | Meaning |
|-----------|---------|
| PCR | Peak Cell Rate — max instantaneous rate (inverse of min inter-cell interval) |
| SCR | Sustained Cell Rate — average over a long interval |
| CLR | Cell Loss Ratio; CLP=1 dropped first; can specify separately for CLP=0 and CLP=1 |
| CTD | Cell Transfer Delay (propagation + queueing + service) |
| CDV | Cell Delay Variation — high variation ⇒ larger buffers for voice/video |
| BT / MBS | Burst Tolerance / Maximum Burst Size — leaky-bucket bucket size; max back-to-back cells at PCR while drained at SCR |
| MCR | Minimum Cell Rate desired by a user |

First six originally in **UNI version 3**. **Traffic contract** = connection traffic descriptor + conformance definition. **Not every VC needs specified QoS** — otherwise a large fraction of resources would be wasted. **Unspecified QoS** can be supported best-effort. **CAC** accepts a new connection only if resources suffice for acceptable QoS.

**Disadvantages (why Ethernet won LANs)**

| Drawback | Detail |
|----------|--------|
| Expense | Moderate ATM switch and NICs cost far more than LAN/Ethernet hardware |
| Setup latency | Distant VC setup/teardown can take longer than using the VC |
| Cell tax | ~**10%** header overhead vs ~**1%** on Ethernet |
| No efficient broadcast | NBMA — broadcast simulated by app copying to each computer |
| QoS complexity | Cumbersome; many implementations do not support the full standard |
| Homogeneity assumption | Designed as a single universal system; minimal interop provision |

Some phone companies still use ATM in **backbone networks**.

### How to answer
- ATM’s story starts from **fixed cells + pre-established VCs** on SONET-class fabric — good latency, awkward for surges/broadcast.
- Header fields (**VPI/VCI, PT, CLP, HEC**) are both the switching mechanism and the **attack surface**.
- Forum security: confidentiality, AAL checksums/seq, signed signaling, full management lifecycle.
- Unique threats: **VC stealing** and **traffic/covert-channel analysis**.
- QoS = traffic contract (PCR/SCR/CLR/CTD/CDV/BT/MCR) + **CAC**; unspecified QoS saves capacity.
- Practical closer: ATM **lost the LAN** to cheaper, simpler, more interoperable Ethernet.

---

## M30: Wireless Networks

### In one line
Wireless networks use radio at the OSI physical layer to avoid cabling, classified as WPAN/WLAN/WMAN/WWAN, with Bluetooth piconets, 802.11 CSMA/CA, WiMAX, cellular, and satellite as the taught examples.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| WPAN / WLAN / WMAN / WWAN | Personal, local, metro, and wide-area wireless scopes. |
| Piconet / scatternet | Bluetooth one-master small net (≤7 active slaves) vs overlapping piconets joined by a bridge. |
| Parked state | Bluetooth secondary synchronized with the master but not among the seven active communicators. |
| GFSK / FHSS 1600 hop/s | Bluetooth 2.4 GHz ISM modulation and hopping rate. |
| BSS / ESS / AP | 802.11 basic service set; extended set of BSSs; optional access point. |
| DCF / PCF | Distributed CSMA/CA access vs AP polling (PIFS < DIFS so AP wins). |
| Hidden / exposed station | Collision because sender cannot hear a peer vs false deferral that wastes capacity. |
| RTS/CTS | Handshake that advertises duration so hidden nodes defer. |
| WiMAX / IEEE 802.16 | Broadband wireless MAN technology. |
| MSC | Mobile Switching Center coordinating cellular base stations with the telephone network. |

### Concepts explained

**Definition and aims.** A wireless network is any computer network that uses wireless data connections between nodes. Homes, telecom networks, and enterprises use it to **avoid the cost of cabling**. Wireless telecom is generally **radio**, implemented at the **OSI physical layer**. Lecture aims: identify basic topologies and variations, and choose an appropriate topology for a network plan. Four categories: **WPAN, WLAN, WMAN, WWAN**.

**WPAN — Bluetooth (IEEE 802.15).** Transfers data over a short distance and removes cords/cables/adapters. A Bluetooth LAN is an **ad hoc** network formed spontaneously: gadgets find each other and form a **piconet**; it can reach the Internet if one gadget has that capability. Named for **Harald Bluetooth** (Harald Blåtand), who united Denmark and Norway. Protocols support **pairing** and secure transfer.

**Piconet:** up to eight stations — **one primary (master)** and secondaries (slaves). All secondaries synchronize clocks and hopping with the primary. Communication is one-to-one or one-to-many. Maximum **seven active** secondaries; additional secondaries can be **parked** (synchronized but not communicating). Activating a parked station means an active station must park. **Scatternet:** a secondary in one piconet can be primary in another (bridge/forward); a station can be a member of two piconets.

**Radio:** **2.4 GHz ISM**, **79 channels of 1 MHz**, **FHSS** hopping **1600 times/s**, **GFSK** (bit 1 = deviation above carrier, bit 0 = below). Carrier frequencies Fc = **2402 + n MHz** for n = 0…78.

**Stack:** link control/baseband (master controls time slots → frames; MAC-like with PHY elements); **Link Manager / LMP** (logical channels, power, pairing, encryption, QoS) below **HCI** (chip vs host split); **L2CAP** (variable-length messages, reliability if needed); **SDP** (find services); **RFCOMM** (serial-port emulation); applications/profiles (headset may skip L2CAP for steady audio samples).

**Bluetooth frame:** **72-bit access code** (sync + primary identifier); **54-bit header** = three identical **18-bit** sections compared bit-by-bit with **majority vote** (FEC — radio is very noisy; **no retransmission in this sublayer**); payload **0–2740 bits**. Header subfields: Address 3 (0 = broadcast), Type 4, Flow (buffer full), ACK (stop-and-wait), Seq (1 bit), HEC 8. Features emphasized: less complication, less power, cheaper, robustness. Applications: headset, PDA/PC sync, email via phone, mouse/keyboard, printer discovery.

**WLAN — IEEE 802.11 (Wi-Fi).** Most important access-network technology. **BSS** = building block: stations + optional **AP**. Without AP = standalone **ad hoc** (cannot send to another BSS). With AP = **infrastructure**. Multiple BSSs: stations in range can talk without AP, but inter-BSS communication usually goes via two APs (like cellular). A mobile station can belong to more than one BSS. **ESS** = interconnection of BSSs.

| Mobility type | Movement |
|---------------|----------|
| No-transition | Stationary or only inside one BSS |
| BSS-transition | One BSS to another inside one ESS |
| ESS-transition | One ESS to another; **802.11 does not guarantee continuous communication** |

**MAC: DCF and PCF.** **DCF** uses **CSMA/CA**. WLANs cannot implement CSMA/CD because: (1) detecting collisions would require sending and receiving at once → costly stations and more bandwidth; (2) collisions may be missed due to the **hidden-station problem**; (3) **distance and fading** can hide a far-end collision. **PCF** is optional, infrastructure only, on top of DCF, mostly for time-sensitive traffic: AP polls stations. Extra IFS: **SIFS** (same as DCF) and **PIFS < DIFS**, so if a DCF station and an AP both want the medium, the **AP wins**.

**802.11 MAC frame (nine field groups):** Frame Control 2 B; Duration/ID (sets **NAV**, or frame ID in one control type); Address ×4 (6 B each; meaning depends on To DS / From DS); sequence control; frame body 0–2312; FCS CRC-32. Categories: **management**, **control**, **data**.

**Hidden station problem.** B and C cannot hear each other; both send to A → collision at A. Reduces capacity. **Solution: RTS/CTS.** RTS from B reaches A not C; CTS from A (with duration of B→A data) reaches both B and C; C refrains until duration ends.

**Exposed station problem (inverse).** A transmits to B; C has data for D that would not interfere, but C hears A and refrains — too conservative, wasting capacity. **RTS/CTS does not fully fix this** (C may hear RTS but not CTS; collisions with ongoing data can keep C exposed).

**WMAN — WiMAX (IEEE 802.16).** Connects several WLANs; enables broadband wireless packet rates with mobility without cable or a Wi-Fi hotspot. Needs telecom-scale infrastructure like GSM/CDMA: base stations, sectorized antennas, control centers. Media claims of **over 30 miles** from one base station hold only in ideal conditions. Practically, satisfactory broadband is about **4–5 miles**; with line of sight up to **10 miles**. Coverage/QoS depend on terrain and population.

**WWAN.** Covers neighboring towns/cities for branch offices or public Internet. Links between access points are usually **point-to-point microwave** with parabolic dishes on **2.4 GHz**, plus base-station gateways, APs, wireless bridging relays, or **mesh** relays. **Cellular:** locate/track caller, assign channel, hand off between base stations; cells with antennas and solar/AC base stations controlled by an **MSC** (connects calls, records info, bills). Cell size shrinks in dense areas; transmit power kept low to limit adjacent-cell interference. **Satellite networks:** artificial regenerating satellites preferred over the Moon (delay/distance); divide the planet into cells; reach undeveloped regions without huge ground infrastructure. Security management is deferred to later lectures.

### How to answer
- Classify wireless by **reach**: PAN (Bluetooth 802.15), LAN (802.11), MAN (WiMAX 802.16), WAN (microwave/cellular/satellite).
- Bluetooth: master-driven hopped piconet (79×1 MHz, 1600 hop/s, GFSK) with **triple-header majority vote** instead of baseband retransmission.
- 802.11 infrastructure = **BSS+AP**; ad hoc = BSS without AP; MAC is **CSMA/CA**, not CD.
- **RTS/CTS** mitigates hidden stations; exposed-station waste remains.
- Cellular **low-power cells + MSC** and satellites extend coverage without cabling every site.

---

## M31: Wi-Fi Security Protocol

### In one line
IEEE 802.11 defines WLAN PHY/MAC; the Wi-Fi Alliance brands and certifies interoperability with mandatory WPA/WPA2 and EAP, while this lecture maps the 802.11 stack, amendments, rates, and MAC Frame Control (including the WEP bit).

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Wi-Fi Alliance | 1999 nonprofit that certifies 802.11 interoperability and restricts the Wi-Fi brand; certification requires WPA/WPA2 and EAP. |
| FHSS / DSSS / OFDM / HR-DSSS | 802.11 PHY families: frequency hops; chipping codes; 54 Mbps+ OFDM; 11/22 Mbps high-rate DSSS. |
| PLCP / PMD | Physical Layer Convergence Protocol (CCA / common SAP) vs Physical Medium Dependent modulation. |
| CSMA/CA | DCF access: sense idle, send full frame, binary exponential backoff on collision; virtual sensing via MACA. |
| MIMO | Multiple antennas added in 802.11n (54–600 Mbps). |
| IEEE 802.11i | Security/authentication amendment naming RADIUS, Kerberos, and 802.1X. |
| WEP | Wired Equivalent Privacy; Frame Control **W** bit means the body is WEP-encrypted. |
| 802.11ad / WiGig | 60 GHz PHY; peak rate **7 Gbps**. |
| 802.11af / White-Fi | TV white-space WLAN in **54–790 MHz** using cognitive radio. |

### Concepts explained

**WLAN vs Wi-Fi vs IEEE vs Alliance.** Despite the playlist title “Wi-Fi Security Protocol,” this lecture introduces Wi-Fi technology: architecture, IEEE 802.11 standards, and frame format. Security appears as Alliance certification (**WPA/WPA2, EAP**), **802.11i**, and the **WEP bit** in Frame Control.

A **WLAN** is a data communication system used as an extension or alternative to a wired LAN. **Wi-Fi** is WLAN technology based on the **IEEE 802.11** series. **IEEE does not test equipment for compliance.** The nonprofit **Wi-Fi Alliance** formed in **1999** to establish and enforce interoperability and backward compatibility and to promote WLAN technology. It restricts the Wi-Fi brand to 802.11-based technologies. Certification requires compliance with: **IEEE 802.11 radio** standards; **WPA and WPA2** security standards; **EAP** authentication standards.

**Spread spectrum on WLANs.** Most WLANs use spread spectrum — a wideband RF technique that spreads the signal over available bandwidth. **FHSS:** a narrowband carrier that changes frequency in a pattern known only to transmitter and receiver. **DSSS:** generates a redundant bit pattern (**chip / chipping code**) for each bit, needing more bandwidth; the receiver can recover even if some chip bits are damaged, using statistical techniques **without retransmission**.

**Layered protocol architecture.** IEEE 802.11 covers only the **physical layer** and **medium-access layer**.

- **PLCP** — Clear Channel Assessment (CCA) and a common PHY SAP independent of transmission technology.
- **PMD** — modulation and encoding/decoding.
- **MAC management** — medium access, association/reassociation to an AP, roaming, authentication, encryption, synchronization, power management.

| PHY technique | Facts taught |
|---------------|--------------|
| FHSS | 79 channels of 1 MHz; PRNG hop sequence; fair allocation of unregulated ISM |
| DSSS | 1 or 2 Mbps; technique similar to CDMA |
| OFDM | 54 Mbps and above in the wider 5 GHz ISM band |
| HR-DSSS | 11 and 22 Mbps in 2.4 GHz |

**DCF:** no central control; **CSMA/CA** with physical and virtual sensing. Physical: sense idle → transmit full frame (does **not** sense while sending); on collision, binary exponential backoff. Virtual: **MACA**. **PCF:** a base station controls all activity in its cell.

**IEEE 802.11 standards (MAC + PHY in 2.4 and 5 GHz).** Base version **1997**, then many amendments; basis for Wi-Fi brand products.

| Standard | Year | Rate | Indoor/outdoor | Modulation | Band |
|----------|------|------|----------------|------------|------|
| 802.11 legacy | 1997 | 1–2 Mbps | 20 / 100 m | FHSS & DSSS | 2.4 GHz |
| 802.11a | 1999 | 54 Mbps | 35 / 120 m | OFDM | 5 GHz (less crowded but poorer wall penetration) |
| 802.11b | 1999 | 11 & 22 Mbps | 35 / 120 m | HR-DSSS | 2.4 GHz |
| 802.11g | 2003 | 54 Mbps | 38 / 140 m | OFDM & DSSS | 2.4 GHz |
| 802.11n | 2009 | 54–600 Mbps | 70 / 250 m | OFDM + **MIMO** | 2.4 & optional 5 GHz |
| 802.11ac | 2013 | ~1300 Mbps | — | built on n | 5 GHz |

**Other amendments:** **d** (countries not in base rules); **e** (QoS for wireless multimedia); **f** (roaming between APs / vendor interop); **h** (5 GHz Europe frequency selection and power); **i** (WLAN security/authentication including **RADIUS, Kerberos, 802.1X**); **j** (Japanese equivalent of h); **ad / WiGig** (60 GHz PHY, peak **7 Gbps**); **af / White-Fi / Super Wi-Fi** (Feb 2014; TV white space VHF/UHF **54–790 MHz**, cognitive radio).

**Bands and channels.** 802.11b/g → 2.4 GHz; 802.11a → more regulated 5 GHz; 802.11n → both. Each spectrum is subdivided into channels with center frequency and bandwidth. The **2.4 GHz band has 14 channels spaced 5 MHz apart**; channel 1 centered on **2412 MHz**; some channels restricted or unavailable by regulatory domain.

**MAC frame format.** Nine fields from Frame Control through checksum. **Frame Control is 2 bytes with 11 subfields.**

| Field | Role |
|-------|------|
| Frame Control | Control (11 subfields) |
| Duration | How long this frame and its ACK occupy the channel |
| Four addresses | Source/destination plus source/destination base stations for intercell traffic |
| Sequence | 12 bits identify the frame; 4 bits identify the fragment |
| Data | Up to 2312 bytes |
| FCS | 4-byte CRC |

Frame Control subfields: Protocol version; Type (data/control/management); Subtype; To DS / From DS; More Fragments; Retry; Power management (sleep/wake); More data; **W (WEP — body encrypted)**; Order (strict in-order processing).

### How to answer
- **IEEE writes 802.11; Wi-Fi Alliance owns the logo** and requires **WPA/WPA2 + EAP** for certification.
- 802.11 is **PHY + MAC only**: PLCP/PMD below; DCF/PCF above; MAC management for associate/roam/auth/encrypt/sleep.
- Rate path: **1–2 (1997) → a/b (1999) → g (2003) → n MIMO (2009) → ac ~1.3 Gbps (2013)**; plus ad (60 GHz) and af (TV white space).
- **802.11i** is the amendment that names RADIUS, Kerberos, and 802.1X.
- Four addresses + Duration support DS forwarding and reservation; **W bit** flags WEP on the body.

---

## M32: Wi-Fi Security Protocol

### In one line
WEP was 802.11’s original optional confidentiality algorithm and failed; WPA (draft 802.11i with TKIP/Michael) bridged to WPA2 (full 802.11i with AES), which is the preferred Wi-Fi security standard.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| WEP | Wired Equivalent Privacy — original 802.11 confidentiality algorithm (1997). |
| WPA | Wi-Fi Protected Access — 2003 interim / draft IEEE 802.11i using TKIP. |
| WPA2 | Full IEEE 802.11i-2004 using AES. |
| IEEE 802.11i | WLAN security standard rolled out in two Alliance steps: WPA then WPA2. |
| Open System Authentication | Join path that does not actually authenticate; WEP keys may be applied later to data. |
| Shared Key Authentication | Four-step WEP challenge–response using the same shared key later used to encrypt. |
| RC4 | Stream cipher WEP uses with a 256-entry 8-bit S-box lookup. |
| IV | Initialization vector concatenated with the WEP key and sent in the clear — the IV weakness. |
| CRC | Weak WEP integrity check computed on plaintext. |
| TKIP | Temporal Key Integrity Protocol — per-packet 128-bit keys in WPA. |
| Michael | WPA message integrity check; stronger than CRC, still flawed on short packets. |
| AES | WPA2 block cipher: 128-bit blocks; 128/192/256-bit keys with 9/11/13 rounds as taught. |
| 802.1X / EAP | Framework both WPA and WPA2 use for mutual authentication and dynamic keys. |
| PSK | Pre-shared key mode for home / small office. |
| Mix-mode | WPA2 ability to host WPA and WPA2 stations on one WLAN. |

### Concepts explained

**Why confidentiality on Wi-Fi.** Wireless networking is popular for home and business use. Radio is available to authorized users **and** to unauthorized users (hackers). IEEE **802.11** therefore offered **Wired Equivalent Privacy (WEP)** — instructions/rules so wireless data can travel over the air with some security. This lecture covers three protocols then compares the last two: **WEP** (1997 original; soon replaced), **WPA** (interim fix), **WPA2** (full IEEE 802.11i 2004; AES). WEP can be **cracked in a few minutes** with automated tools; WPA/WPA2 were designed to address those issues.

**WEP as originally specified (1997).** Intention: data confidentiality **comparable to a traditional wired network** — hence the name. Design objectives:

| Objective | Meaning |
|-----------|---------|
| Reasonably strong | Security rests on difficulty of brute-forcing the secret key; depends on **key length** and **how often keys change** |
| Self-synchronizing | Resynchronize **per message** — critical for best-effort data-link encryption |
| Efficient | Implementable in hardware or software |
| Exportable | Maximize chances of U.S. government export approval |
| Optional | Implementation and use in 802.11 should be optional |

Those objectives show WEP was **not military-grade**. Intention: make break-in **hard, not impossible**.

**WEP authentication** (when a device first joins)

| Method | What happens |
|--------|----------------|
| Open System Authentication | Client need not provide credentials; any client can authenticate then attempt to associate; **in fact no authentication occurs**; afterward WEP keys **can** encrypt data if the client has the correct keys |
| Shared Key Authentication | Four-step challenge–response: (1) device sends authentication request; (2) AP sends **128-bit random challenge in cleartext**; (3) device signs challenge with shared secret and returns response; (4) AP decrypts with same key and verifies → success or fail |

**After Shared Key authentication, no new secret key is exchanged.** The **same shared key** is used for both authentication and encryption. There is therefore no way to tell whether a later message comes from the trusted device or an **imposter** — **prone to man-in-the-middle attack**.

**WEP encryption (RC4 + CRC + IV).** Uses **RC4** stream cipher (taught as 8-bit RC4 with a **256-entry** 8-bit S-box lookup). Pipeline: (1) CRC on plaintext concatenated to plaintext; (2) secret key concatenated with **IV** fed into RC4; (3) RC4 emits keystream; (4) XOR with (plaintext‖CRC) → ciphertext; (5) **same IV prepended in cleartext**; (6) IV + ciphertext + headers go over the air. Attack implications: part of the secret is used with different exposed values; analyzing early keystream bytes recovers the secret with relatively little work — the **IV weakness**.

**Collapse of confidence.** Early belief in impenetrable resistance failed as cryptanalysts found design flaws (little peer review). For most users — especially home users — WEP was the only choice for a time: **something is better than nothing** against unauthorized use and bandwidth theft. Suggested patches: bigger IV; hash of IV instead of clear IV; replace CRC with hash-based integrity; change secret key regularly/dynamically; better key management handshakes; new authentication with **EAP**. Even with those, WEP still **cracked in minutes**.

**From WEP to WPA to WPA2.** 2003: Alliance announced WEP superseded by **WPA**. 2004: full **IEEE 802.11i** ratified as **WPA2**; IEEE declared WEP obsolete. Alliance implemented 802.11i in two steps. **WPA** was intermediate pending full 802.11i — addable by **firmware upgrades** on WEP-era NICs that **could not support WPA2**, delaying hardware purchases (some old APs still needed replacement). WPA ≈ **draft IEEE 802.11i (2003)**; WPA2 ≈ **IEEE 802.11i-2004**.

**WPA: TKIP and Michael**

| | WEP | WPA (TKIP) |
|--|-----|------------|
| Key | 40- or 104-bit key, manually entered, does not change | **Per-packet** dynamically generated **128-bit** key |
| Integrity | CRC | Message integrity check — algorithm **Michael** |

Per-packet keys stop the attacks that compromised WEP. MIC stops altering and resending packets. CRC did not give a strong enough integrity guarantee; stronger MACs needed too much computation for old cards. **Michael is much stronger than CRC**, but researchers still found a flaw: retrieving **keystream from short packets** for reinjection and spoofing.

**WPA2: AES and full 802.11i.** Solves WPA problems and fully implements 802.11i. Features taught: stronger cryptography, stronger authentication, control, key management, replay-attack protection, and data integrity. Encryption is **AES**, not TKIP: fixed block size **128 bits**; key sizes **128 → 9 rounds**, **192 → 11**, **256 → 13**; substitution cipher (substitute, rearrange, special multiplication each round). Brute-force time for AES-128 cited around **2,200 years**.

**WPA versus WPA2 — similarities:** both use **802.1X / EAP** for central mutual authentication and dynamic key management; both offer **PSK** for home/small office; both designed to secure **802.11a/b/g** as taught. **Differences:** WPA2 **mix-mode** hosts WPA and WPA2 stations on one WLAN (WPA supports only one); most significant — **AES instead of TKIP**; **WPA2 theoretically not hackable, WPA is**; **WPA2 requires more processing power**.

### How to answer
- Air is shared with hackers; WEP aimed to be **hard** and **optional**, not military-grade.
- Shared-key WEP reuses one key for auth and encryption (MITM); RC4 + **clear IV** + CRC leaked keystream.
- Firmware-friendly **WPA/TKIP/Michael** was only a bridge; Michael still allowed short-packet reinjection.
- **WPA2/AES** is full 2004 802.11i: stronger crypto, auth, key management, replay protection, integrity — higher CPU cost.
- Prefer **WPA2**; WPA is described as hackable. Both still share 802.1X/EAP, PSK, and a/b/g coverage.

---

## M33: Bluetooth Networks and Security Protocols

### In one line
Bluetooth is a short-range UHF ISM WPAN technology with SIG/IEEE origins, master–slave piconets, a full protocol stack, version history through 4.2, and four BR/EDR/HS security modes (never use mode 1).

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| WPAN | Wireless personal area network — Bluetooth’s operating setting. |
| SIG | Bluetooth Special Interest Group (1998; ~1500-page v1.0 in July 1999). |
| Piconet | Master + up to **seven active** slaves within about **10 m**. |
| Scatternet | Piconets joined by a bridge node. |
| ACL / SCO | Asynchronous Connection-Less data vs Synchronous Connection-Oriented real-time (no retransmission; FEC). |
| L2CAP | Logical Link Control and Adaptation Protocol — segmentation, multiplexing, QoS. |
| RFCOMM | Serial-port emulation over Bluetooth. |
| Access code | Identifies the master so overlapping piconets can be distinguished. |
| EDR | Enhanced Data Rate (v2.x): ~3 Mbps nominal, ~2.1 Mbps practical; GFSK+PSK. |
| HS | High Speed (v3.0): up to 24 Mbps over **802.11** after Bluetooth setup/negotiation. |
| LE / Wibree | Bluetooth Low Energy — new stack inside v4.0 “Bluetooth Smart”. |
| SSP | Secure Simple Pairing (v2.1); ECDH link-key agreement in security mode 4. |
| 802.15.1–.10 | IEEE WPAN family: Bluetooth, coexistence, high/low rate, mesh, BAN, VLC, PAC, KMP, L2 routing. |
| Security modes 1–4 | Non-secure; service-level; link-level mandatory crypto; SSP service-level. |

### Concepts explained

**Origins and naming.** Bluetooth exchanges data over short distances using short-wavelength UHF radio in the **ISM band 2.4–2.485 GHz**, for mobile devices and **PANs / WPANs**. In **1994**, Ericsson wanted cable-free mobile connections; with **IBM, Intel, Nokia, and Toshiba** it formed a **Special Interest Group (SIG)** for a short-range, low-power, inexpensive radio standard. Named after 10th-century king **Harald Bluetooth** (proposed **1997** by **Jim Kardach**). SIG defines manufacturing standards; **July 1999** issued a **~1,500-page v1.0**. IEEE WPAN working group **802.15** adopted that document as a basis. **Bluetooth SIG specification = complete system (PHY through application)**; **IEEE 802.15 = only physical and data-link layers**.

**Piconet and scatternet.** Basic unit: **master** + up to **seven active slaves** within about **10 m**. Multiple piconets in one room can connect via a **bridge** node into a **scatternet**. **All communication is master–slave.** Direct **slave-to-slave communication is not possible**.

**Layered protocol architecture**

| Layer / protocol | Role |
|------------------|------|
| Radio (physical) | Transmission/modulation in ISM 2.4–2.485 GHz |
| Baseband | MAC-like; master controls **625 µs** slots and frames; turns bit stream into frames |
| Link Manager | Logical channels: power management, authentication, QoS |
| L2CAP | Shields upper layers from transmission details |
| Audio and control | May reach them **directly**, without L2CAP |
| RFCOMM | Emulates a PC serial port |
| Telephony protocol | Real-time speech protocols; call setup/termination |
| SDP | Locate services |
| Applications/profiles | Top layer |

**TDD slots.** Master defines **625 µs** slots; master TX in **even** slots, slave TX in **odd** — classical TDM (master gets half the slots). Two link types: **ACL** (Asynchronous Connection-Less) — packet-switched data at irregular intervals; **SCO** (Synchronous Connection-Oriented) — real-time (e.g. telephone), **fixed slot each direction**, frames **never retransmitted**, reliability via **FEC**.

**L2CAP’s three functions:** (1) accept packets up to **64 KB**, fragment to frames, reassemble; (2) multiplex/demultiplex multiple sources; (3) handle QoS.

**Frame format.** Begins with **access code** that usually identifies the master (distinguish overlapping masters). Then **54-bit header**, then data up to **2,744 bits** (five-slot) or **240 bits** (single slot). Header fields: Address (which of eight active devices); Type (ACL/SCO/POLL/NULL, error-correction type, slot count); Flow (buffer full); Acknowledgement; Sequence (stop-and-wait, one bit); 8-bit header checksum. Entire 8-bit header **repeated three times**; majority vote on disagreement.

**SIG versions (all downward compatible).** SIG announced **20 May 1998**; membership **over 20,000** companies. Founders: Ericsson, IBM, Intel, Toshiba, Nokia.

| Version | What was taught |
|---------|-----------------|
| v1.0 / 1.0b | Basic Bluetooth; many problems; interop struggles |
| v1.1 | IEEE 802.15.1-2002; fixed errors; non-encrypted channels; RSSI |
| v1.2 | Faster connection/discovery; **AFH** skips crowded hops; up to **721 kbps**; 802.15.1-2005 |
| v2.0 + EDR | ~**3 Mbps** nominal / **2.1 Mbps** practical; GFSK + PSK |
| v2.1 + EDR | **26 July 2007**; **Secure Simple Pairing (SSP)** |
| v3.0 + HS | **21 April 2009**; up to **24 Mbps** — Bluetooth negotiates; traffic rides **802.11** |
| v4.0 | **30 June 2010** “Bluetooth Smart”: Classic + HS + **LE** (formerly Wibree — entirely new stack) |
| v4.1 | **4 Dec 2013** software update: LTE coexistence, bulk rates, multiple roles |
| v4.2 | **2 Dec 2014**; data-length extension needs hardware; some privacy via firmware |

**IEEE 802.15 WPAN family:** **.1** Bluetooth PHY/MAC (2002/2005); **.2** coexistence with WLANs (2003, then hibernation); **.3** high-rate 11–55 Mbps (+ amendments); **.4** low-rate, long battery, low complexity; **.5** mesh (low-rate on 15.4 MAC; high-rate on 15.3b); **.6** Body Area Network (in/around body); **.7** visible light; **.8** peer-aware; **.9** key management; **.10** layer-2 routing.

**Security architecture — three native services:** Authentication (verify device by Bluetooth address — **no native user authentication**); Confidentiality (stop eavesdropping); Authorization (device must be authorized for a service). Does **not** address audit, integrity, or non-repudiation.

**Four BR/EDR/HS security modes** (each device operates in one):

| Mode | Behavior |
|------|----------|
| 1 Non-secure | Never initiates auth/encryption; indiscriminate; will participate if remote starts; v2.1+ only for backward compat; **NIST: never use** |
| 2 Service-level | After link establishment, before logical-channel establishment; local security manager holds access-control policies |
| 3 Link-level | Before physical link fully established; **auth and encryption mandatory**; v2.1+ only for backward compat |
| 4 SSP (v2.1+) | After physical and logical links; **SSP** with **ECDH** replacing legacy key agreement; device auth/encryption algorithms remain those of v2.0+EDR and earlier |

### How to answer
- Bluetooth = complete SIG stack on cheap short-range ISM radios; IEEE 802.15 only PHY/MAC.
- Piconet is **star-shaped**: slave-to-slave only via master or scatternet bridge.
- Operational core: baseband TDD 625 µs, ACL vs SCO, L2CAP fragment/mux/QoS; audio/control can skip L2CAP.
- Versions add AFH, EDR, SSP, 802.11 offload, LE, LTE coexistence, longer PDUs — always backward compatible.
- Native security is **device** auth, confidentiality, authorization. **Never use mode 1.** Mode 4 modernizes **key agreement (ECDH)** without changing old auth/encryption algorithms.

---

## M34: Virtual Private Network

### In one line
A VPN overlays tunnels and encryption on a public network to obtain private-network properties without leased-line cost, using Layer-2 (PPTP/L2F/L2TP), Layer-3 IPsec, or OpenVPN, preferably with firewalls.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Private network | Company hosts plus leased telephone lines — secure but expensive. |
| VPN | Virtual Private Network — overlay of tunnels + encryption on a public non-secure network. |
| NAS | Network Access Server at the ISP point of presence. |
| PAC / PNS | PPTP Access Concentrator / PPTP Network Server. |
| LAC / LNS | L2TP Access Concentrator / L2TP Network Server. |
| Home Gateway | L2F name for the VPN server. |
| PAP / CHAP | PPP authentication protocols used by Layer-2 VPNs. |
| LCP / NCP | PPP Link Control Protocol / Network Control Protocol (e.g. IPCP). |
| GRE | Generic Routing Encapsulation used by PPTP; many firewalls lack GRE support. |
| AH / ESP | IPsec Authentication Header (auth/integrity only) vs Encapsulating Security Payload (adds confidentiality). |
| OpenVPN | SSL/TLS VPN via OpenSSL; not interoperable with IPsec/L2TP/PPTP. |
| TAP | Virtual Ethernet device used for OpenVPN bridging. |

### Concepts explained

**Private network vs VPN.** Almost all companies have offices scattered over cities — sometimes countries. The old approach was to **lease telephone lines** between locations. A network of **company computers + leased telephone lines** is a **private network**: traffic does not leak from company locations, and intruders must **physically wiretap** the lines. The problem is **cost**. When public data networks and the **Internet** appeared, companies wanted private-network security on public pipes — producing the **VPN**: an **overlay** on public networks with most properties of private networks.

A VPN provides a **secure connection** between sender and receiver over a **public, non-secure** network. It is **virtual** in the same sense as virtual circuits and virtual memory — an illusion, not a physical private plant. Created by a **virtual point-to-point path** using dedicated connections, virtual tunnels, and traffic encryption. From the user’s view, extended resources are used the same way as resources inside the private network.

**Uses taught:** employees securely access the company intranet while traveling; geographically separated offices join into one cohesive network; individuals secure wireless transactions, circumvent geo-restrictions/censorship, and connect to proxy servers to protect personal identity and location.

**Three types of VPN** (all use the Internet as enterprise backbone, different groups):

| Type | Who it serves |
|------|----------------|
| Access VPN | Remote/mobile users, telecommuters, or a branch needing reliable access to the corporate network |
| Intranet VPN | Branch offices linked to corporate headquarters securely |
| Extranet VPN | Customers, suppliers, and partners accessing the corporate intranet securely |

**Architecture — four components:** (1) VPN client; (2) **Network Access Server (NAS)**; (3) tunnel-terminating device — VPN server; (4) VPN protocol. Typical Access VPN: client connects to NAS over **PSTN** and starts **PPP**; NAS (ISP-owned, usually in ISP **PoP**) authenticates, then directs the packet into the **IP tunnel** between NAS and VPN server (VPN server may sit in ISP PoP or at corporate site); VPN server recovers/unwraps and delivers to the corporate network.

**Two categories of tunneling protocols:** Layer 2 — **PPTP, L2F, L2TP**; Layer 3 — **IPsec**. When PPTP and L2F were both submitted to the **IETF**, features were combined into **L2TP**.

**How Layer-2 tunneling works.** Operate at the data-link layer; use security from **PPP**: authentication via **PAP** and **CHAP**; **no specific provision for data encryption** (user may encrypt before requesting VPN). Tunnel-creation process: (1) client dials NAS and starts PPP; (2) NAS performs **LCP** negotiation; (3) **PAP/CHAP** auth request/reply; (4) NAS attempts to open PPP/VPN toward VPN server; (5) VPN server authenticates NAS with PAP/CHAP; (6) client and VPN server use **NCP** to negotiate the network-layer protocol; (7) tunnel complete.

**PPTP (Point-to-Point Tunneling Protocol).** Developed by **Microsoft** with Ascend and 3Com as a PPP extension. Handles **only point-to-point** (not multipoint). NAS = **PAC**; VPN server = **PNS**. No packet-by-packet encryption of its own — relies on PPP’s native encryption. Packet story: PPP payload (data + original IP/TCP) + PPP header encapsulated in **GRE**, then an **IP header** on top of GRE.

**L2F (Layer 2 Forwarding).** Proprietary **Cisco**. Protocol-independent — can run over **X.25, Frame Relay, and ATM**. Supports private IP, IPX, and AppleTalk; uses **UDP** for Internet tunneling. Many connections inside one tunnel. VPN server = **Home Gateway**. Uses PPP for dial-up user authentication. Defines its **own encapsulation header** (not dependent on IP and GRE). Packet: SLIP/PPP payload in L2F packet with L2F header and optional L2F checksum trailer.

**L2TP (Layer 2 Tunneling Protocol).** Combines PPTP and L2F. Runs over **UDP, not GRE** — many firewalls do not support GRE, so L2TP is more firewall-friendly than PPTP. NAS = **LAC**; VPN server = **LNS**. Uses PAP/CHAP and also allows **RADIUS**. Permits **multiple tunnels** between the same endpoint pair, each with different **QoS**. Relies on **IPsec** for data encryption; if the remote end lacks IPsec, falls back to less secure PPP encryption. Expected to be the predominant Layer-2 protocol once standardized.

**Layer 3: IPsec.** Designed to add security to TCP/IP: packet-level authentication, integrity, and confidentiality via two headers:

| Header | Provides | Notes |
|--------|----------|--------|
| AH | Header integrity and authentication **without confidentiality** | Preferred when only authentication is required / encryption export-restricted; lower processing overhead than ESP |
| ESP | Integrity, authentication, **and confidentiality** of the payload | Packet-by-packet encryption + standards-based key management |

An IPsec VPN can use AH, ESP, or both.

**Layer 2 versus Layer 3**

| | Layer 2 (PPTP, L2F, L2TP) | Layer 3 (IPsec) |
|--|---------------------------|-----------------|
| Traffic | Can carry **non-IP** (IPX, AppleTalk) | **IP only** |
| Dial-up | Individual dial-up via **PPP user authentication** — seamless through ISPs | Security between routers/firewalls; **does not provide user authentication** |

**OpenVPN.** Open-source product using **OpenSSL** and **SSL v3 or TLS v1**. Supports neither Layer-2 nor Layer-3 tunneling in the IPsec/L2TP/PPTP sense; **not compatible** with those protocols. Highly configurable; runs best on **UDP** but can use any port including **TCP 443**. Ciphers taught: AES, Blowfish, 3DES, CAST-128, Camellia, and more. Capabilities: tunnel any IP subnet or virtual Ethernet adapter over a single UDP/TCP port; scalable load-balanced servers for thousands of dynamic clients; all OpenSSL encryption/authentication/certification; static-key or certificate-based public-key encryption; static PSK or TLS dynamic key exchange; adaptive compression and traffic shaping; tunnel dynamic public endpoints; tunnel through stateful firewalls and NAT; secure Ethernet bridges using virtual **TAP** devices; GUI on Windows/Mac. Compared with PPTP and L2TP/IPsec, generic OpenVPN can be fiddly unless a provider ships a customized client.

**Which protocol to choose (instructor ranking)**

| Protocol | Verdict |
|----------|---------|
| PPTP | **Very insecure — avoid**, despite easy setup |
| L2TP/IPsec | Much more secure; good for non-critical use and quick setup without extra software, especially mobile where OpenVPN support is patchy |
| OpenVPN | **Best all-round**: reliable, fast, most importantly secure |

**Wherever possible, always choose OpenVPN.**

**Firewalls and VPNs together.** They go hand in hand. VPNs open secure tunnels; firewalls sit at strategic locations and block certain traffic; many firewall products provide encrypted firewall-to-firewall tunnels. Firewalls control access and establish trust. Two sites each with a firewall still send data vulnerable on the Internet; a VPN supplies privacy when there is usually no trust between the two sides. **Firewall + VPN** establishes trust and privacy and is **more secure than either alone**. Many new firewall products support VPN functionality.

### How to answer
- VPNs buy private-network **properties** without leased-line **cost** via tunnels + encryption.
- Layer 2 (PPTP/L2F/L2TP) is the dial-up/PPP world and can carry non-IP; IPsec is IP-only, router/firewall oriented, **no user auth**.
- IETF folded PPTP+L2F into **L2TP**; encrypt L2TP with **IPsec** when possible.
- **Avoid PPTP.** Prefer **OpenVPN**; use L2TP/IPsec only for quick, non-critical, especially mobile, setups.
- Firewall pair without a tunnel still leaks on the Internet; **firewall + VPN** is stronger than either alone.

---

## M35: WiMAX Technology and its Security

### In one line
Playlist title says WiMAX, but the taught captions duplicate Module 33: Bluetooth WPAN architecture, versions, IEEE 802.15 family, and security modes 1–4 (do not invent WiMAX material).

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| WPAN | Wireless personal area network; Bluetooth’s setting (content actually taught in this slot). |
| SIG | Bluetooth Special Interest Group (1998; ~1500-page v1.0 in 1999). |
| Piconet | Master + up to 7 active slaves within ~10 m. |
| Scatternet | Piconets joined by a bridge node. |
| ACL / SCO | Async connectionless data vs synchronous connection-oriented real-time (no retransmission; FEC). |
| L2CAP | Segmentation, multiplexing, QoS. |
| RFCOMM | Serial-port emulation. |
| Access code | Identifies the master among overlapping piconets. |
| EDR | Enhanced Data Rate (~3 Mbps nominal / 2.1 Mbps practical; GFSK+PSK). |
| HS | High Speed (v3.0): 24 Mbps over 802.11 after Bluetooth setup. |
| LE / Wibree | Bluetooth Low Energy new stack inside v4.0 “Bluetooth Smart”. |
| SSP | Secure Simple Pairing (v2.1); ECDH link keys in security mode 4. |
| 802.15.1–.10 | IEEE WPAN family from Bluetooth through mesh, BAN, VLC, KMP, L2 routing. |
| Security modes 1–4 | Non-secure; service-level; link-level mandatory crypto; SSP service-level. |

### Concepts explained

**Source caveat for exams (critical).** Playlist metadata names this module **WiMAX Technology and its Security**. The auto-generated captions attached to the video are a near-duplicate of **Module 33**: they open with Bluetooth WPAN and **never mention WiMAX or IEEE 802.16**. Exam answers for this slot must follow **what was taught** (Bluetooth), not invented WiMAX material. Brief WiMAX facts appear earlier in **M30** (IEEE 802.16 WMAN, practical ~4–5 mile broadband reach).

**Origins (as taught in this slot).** Bluetooth is a wireless standard for exchanging data over short distances using short-wavelength UHF radio in **ISM 2.4–2.485 GHz**, for mobile devices and PANs/WPANs. Ericsson (1994) with IBM, Intel, Nokia, and Toshiba formed the **SIG**. Named after Harald Bluetooth (proposed 1997 by Jim Kardach). July 1999: ~1,500-page v1.0; IEEE **802.15** adopted it as a basis. **SIG = complete stack**; **IEEE 802.15 = PHY/MAC only**.

**Piconet and scatternet.** Master + up to seven active slaves within ~10 m; bridge node joins piconets into a scatternet. **All communication is master–slave**; no direct slave-to-slave path.

**Protocol stack and links.** Radio → Baseband (625 µs TDD; master even / slave odd slots) → Link Manager (power, authentication, QoS) → L2CAP (≤64 KB fragment/reassemble, mux, QoS) → RFCOMM / telephony / SDP / profiles. Audio and control may bypass L2CAP. **ACL** = irregular packet data; **SCO** = real-time fixed slots, never retransmit, FEC for reliability.

**Frame.** Access code (usually identifies master) + **54-bit header** (8-bit header ×3 with majority vote) + data (**240 bits**/1 slot or **2,744 bits**/5 slots). Header: Address, Type (ACL/SCO/POLL/NULL + FEC/slots), Flow, ACK, Sequence (stop-and-wait), 8-bit checksum.

**SIG versions (backward compatible):** 1.0/1.0b interop pain → 1.1 (802.15.1-2002, RSSI, non-encrypted channels) → 1.2 AFH (~721 kbps, 802.15.1-2005) → 2.0+EDR (~3/2.1 Mbps, GFSK+PSK) → 2.1+EDR **SSP** → 3.0+HS (24 Mbps via 802.11 offload) → 4.0 Bluetooth Smart (Classic+HS+LE/Wibree) → 4.1 LTE coexistence / multi-role → 4.2 data-length extension.

**IEEE 802.15 family:** .1 Bluetooth; .2 coexistence; .3 high-rate; .4 low-rate long battery; .5 mesh; .6 BAN; .7 VLC; .8 peer-aware; .9 key management; .10 layer-2 routing.

**Security architecture.** Three native services only: **device** authentication (Bluetooth address — **no native user authentication**), confidentiality, service authorization. Does **not** address audit, integrity, or non-repudiation.

| Mode | Behavior |
|------|----------|
| 1 Non-secure | Never initiates auth/encryption; will join if peer starts; **never use** (NIST) |
| 2 Service-level | After link, before logical channel; security manager + policies |
| 3 Link-level | Before physical link fully up; auth+encryption mandatory |
| 4 SSP (v2.1+) | After physical/logical links; **ECDH** for link keys; auth/encrypt algorithms still v2.0-era |

Modes 1 and 3 on v2.1+ only for backward compatibility.

### How to answer
- State the **caption caveat** first: this playlist slot’s taught captions are **Bluetooth**, not WiMAX/802.16 — do not invent WiMAX security for the exam.
- Bluetooth = complete **SIG** stack on cheap short-range ISM radios; **IEEE 802.15** standardizes only PHY/MAC.
- A piconet is strictly **star-shaped** (no slave-to-slave except via master or scatternet bridge); baseband **TDD 625 µs**; distinguish **ACL** vs **SCO**; list **L2CAP** fragment/mux/QoS roles.
- Version path: AFH, EDR, SSP, 802.11 HS offload, LE/Wibree, LTE coexistence, longer PDUs — always backward compatible.
- Native security is **device** authentication, confidentiality, and service authorization only (no native user auth, audit, integrity, or non-repudiation).
- **Never use security mode 1** (NIST). Mode 4 modernizes **key agreement with ECDH** without changing the old authentication/encryption algorithms.
- If a question truly asks for WiMAX from this course, point only to the brief **M30** WMAN facts (IEEE 802.16, practical ~4–5 mile broadband) — not to invented M35 WiMAX security.

---
