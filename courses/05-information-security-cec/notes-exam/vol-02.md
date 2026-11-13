# Volume 02 — IPv4/IPv6, UDP, IPsec, Email, WWW, Media & Ethernet (M12–M23)

> Information Security (CEC) · Exam-readable notes
> Full concept coverage rewritten for understanding and answer writing (not the ultra-short notes-3).

---

## M12: IPV4 & IPV6

### In one line
IPv4 (RFC 791) is the connectionless 32-bit Internet packet protocol; IPv6 (128-bit) simplifies the header, adds QoS/security hooks, and uses extension headers where IPv4 used options and flags.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| IPv4 (RFC 791) | Fourth version of IP; connectionless packet-switched protocol with 32-bit addresses; still carries most Internet traffic; specified September 1981, replacing RFC 760 (1980). |
| IHL | Internet Header Length in 32-bit words; minimum 5 (20-byte header, no options), maximum 15 (header ≤ 60 bytes, options ≤ 40 bytes). |
| DSCP / ECN | Differentiated Services Code Point (6 bits) marks real-time class (e.g. VoIP); Explicit Congestion Notification (2 bits) signals congestion end-to-end without dropping packets. |
| DF / MF | Don’t Fragment (routers must not fragment); More Fragments (set on all fragments except the last). |
| Classful addressing | Historic A–E split of the IPv4 space by leading bits; no longer used for allocation, but still appears in literature. |
| CIDR (RFC 1519) | Classless Inter-Domain Routing: allocate remaining IPs in variable-sized blocks, aligned on block size, without regard to classes. |
| NAT | Network Address Translation: one (or few) public IP(s) for Internet traffic; internal hosts keep unique private addresses rewritten at the border. |
| RFC 1918 | Private ranges that must not appear on the public Internet: 10/8, 172.16/12, 192.168/16. |
| Flow label | IPv6 20-bit field: source and destination set up a pseudo-connection with particular flow-control / QoS properties. |
| Hop limit | IPv6 TTL-as-actually-used: 8-bit count decremented each hop (IPv4 TTL was “seconds” in theory but never used that way). |
| `::` | Compression of one or more consecutive groups of 16-bit zeros in an IPv6 address. |

### Concepts explained

**IPv4 introduction.** IPv4 is a core Internet protocol: connectionless, packet-switched, 32-bit addresses. A datagram has a header plus a data (text) part. The header has a **20-byte fixed part** plus a **variable options** part (minimum five 32-bit rows).

**IPv4 header fields (all taught).**

| Field | Size | What it does |
|-------|------|--------------|
| Version | 4 bits | IPv4 = 4. Also named: IPv5 (experimental real-time stream, never widely used), IPv6. |
| IHL | 4 bits | Number of 32-bit rows (5–15). |
| DSCP | 6 bits | Diffserv / real-time class. Originally Type of Service: 3-bit precedence + D/T/R flags. |
| ECN | 2 bits | Congestion notification without drops. |
| Total length | 16 bits | Header + data; max 65,535 bytes. |
| Identification | — | Shared ID for all fragments of one datagram so the destination can reassemble. |
| Flags | 3 bits | One unused; **DF**; **MF**. |
| Fragment offset | 13 bits | Where this fragment sits; non-last fragments multiple of 8 bytes; ≤ 8192 fragments → max ~65,536 bytes. |
| TTL | 8 bits | Limits lifetime; supposed to be seconds, max 255. |
| Protocol | 8 bits | Protocol in the data portion. |
| Header checksum | 16 bits | **Header only** (guards bad memory words in a router). |
| Source / destination | 32 bits each | May change in transit via NAT. |
| Options | variable | Escape hatch: security, strict/loose source routing, record route, timestamp. |

**Data is not checksummed.** Protocol values taught: 1 ICMP, 2 IGMP, 6 TCP, 17 UDP, 41 IPv6 encapsulation, 89 OSPF, 132 SCTP.

**IPv4 addressing.** Written dotted decimal (four bytes 0–255). Example: binary `10101100 00010000 11111110 00000001` → **`172.16.254.1`**. Range `0.0.0.0`–`255.255.255.255`.

**Classful leading bits and ranges:**

| Class | Starts with | Net / host bits | Range |
|-------|-------------|-----------------|-------|
| A | `0` | 8 / 24 | `1.0.0.0`–`127.255.255.255` |
| B | `10` | 16 / 16 | `128.0.0.0`–`191.255.255.255` |
| C | `110` | 24 / 8 | `192.0.0.0`–`223.255.255.255` |
| D | `1110` | — | Multicasting |
| E | `1111` | — | Reserved for future use |

**Network address** = first IP of network/subnet. Example host `192.168.64.100/24`: mask `255.255.255.0`; network = host AND mask → `192.168.64.0`. Classful default masks: A `/8` (`255.0.0.0`), B `/16`, C `/24`.

**CIDR (RFC 1519).** Sites get aligned variable blocks. Worked pool from `194.24.0.0`:

| Site | Need | Assignment | Mask |
|------|------|------------|------|
| Cambridge | 2048 | `194.24.0.0`–`194.24.7.255` | `255.255.248.0` |
| Oxford | 4096 | Cannot start at `194.24.8.0` (not on a 4096 boundary); gets `194.24.16.0`–`194.24.31.255` | `255.255.240.0` |
| Edinburgh | 1024 | `194.24.8.0`–`194.24.11.255` | `255.255.252.0` |

**NAT + RFC 1918.** Company gets one public IP; inside, every host has a unique private IP. On exit to the ISP, the NAT box rewrites. Private ranges must not appear on the Internet:

| Block | Range | Hosts taught |
|-------|-------|--------------|
| Class A style | `10.0.0.0`–`10.255.255.255` | 16,777,216 |
| Class B style | `172.16.0.0`–`172.31.255.255` | 1,048,576 |
| Class C style | `192.168.0.0`–`192.168.255.255` | 65,536 |

Example: internal `10.0.0.1` → global `198.60.42.12`. NAT is often combined with a firewall.

**IPv6.** Built for address exhaustion; intended to replace IPv4. **128-bit** addresses as eight groups of four hex digits with colons. Main features: longer addresses; simpler header (**seven fields** vs **13**); better options; security advance; more QoS attention. Fixed header = **first 40 bytes**.

| Field | Size | Role |
|-------|------|------|
| Version | 4 bits | Always 6 |
| Traffic class | 8 bits | Real-time delivery requirements |
| Flow label | 20 bits | Pseudo-connection / flow-control properties |
| Payload length | 16 bits | Bytes **after** the 40-byte header (header not counted) |
| Next header | 8 bits | Extension header or transport protocol |
| Hop limit | 8 bits | Decremented each hop |
| Source / dest | 16 bytes each | |

Example: `8000:0000:0000:0000:0123:4567:89AB:CDEF`. Compression: drop leading zeros in a group; replace one or more zero groups with `::` → `8000::123:4567:89AB:CDEF`.

**Six extension headers:** hop-by-hop (for routers); destination options; routing (loose list); fragmentation; authentication (sender identity); encapsulating security payload (encrypted contents).

**IPv4 fields that disappear in IPv6:** IHL (fixed length); protocol (next header); all fragmentation fields (different approach); checksum (performance); TTL renamed hop limit.

#### Numbers / formulas
- IPv4 binary → dotted: `10101100 00010000 11111110 00000001` = `172.16.254.1`
- IHL 5–15 → header 20–60 bytes; options ≤ 40 bytes; total length max 65,535
- Fragment offset: multiples of 8 bytes; ≤ 8192 fragments
- CIDR university blocks as table above; NAT private host counts as table above
- IPv6 header fixed 40 bytes; payload length excludes those 40

### How to answer
- State IPv4 as connectionless, 32-bit, RFC 791; header 20 + ≤40 options; name DSCP/ECN, DF/MF/offset, TTL, protocol, header-only checksum.
- Contrast classful A–E (historical) with CIDR’s aligned variable blocks; give Cambridge/Oxford/Edinburgh if asked for an example.
- Explain NAT + RFC 1918: internal 10.x rewritten at the border; private addresses must not appear on the public Internet; often paired with a firewall.
- Describe IPv6: 128-bit, 40-byte fixed header, seven fields, compression with dropped zeros and `::`, six extension headers (including AH and ESP).
- List what IPv6 drops (IHL, protocol, fragmentation fields, checksum) and why (fixed header, next header, different fragmentation, performance); TTL → hop limit.

---

## M13: UDP — User Datagram Protocol

### In one line
UDP is a thin, connectionless, unreliable transport that adds process-to-process delivery (ports) and an optional checksum on top of IP, with almost no control overhead.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| User datagram | UDP packet: fixed 8-byte header plus application data. |
| Ephemeral port | Client port chosen by UDP/OS (0–65,535); servers usually use well-known ports. |
| Socket | IP address + port number — the process-to-process endpoint. |
| Pseudo-header | IP-derived fields (including protocol 17) included in the UDP checksum so a corrupted IP header cannot deliver a good UDP datagram to the wrong host/protocol. |
| Silent drop | On checksum failure UDP discards the datagram with no NAK to the sender. |
| Protocol 17 | IP protocol number identifying UDP. |
| Multiplexing | Many processes → one UDP entity at the sender. |
| Demultiplexing | One UDP → many processes at the receiver, by port number. |
| Control-block table | Implementation table of open ports: state (free/in use), process ID, port number, queue number. |
| ICMP on unknown port | Input module response when a datagram arrives for a port with no table entry. |

### Concepts explained

**Place in the stack.** UDP sits between applications and IP. IP delivers host-to-host; UDP extends that to **process-to-process** via ports so many processes can share the network. Duties at transport vs what UDP does: ports for process delivery; control is minimal (no flow control, no ACK); error control = silent drop on error. Connectionless and unreliable — almost nothing beyond process addressing. Appropriate for a small message when the process does not care about reliability.

**User-datagram format (always 8-byte header).**

| Field | Size | Meaning |
|-------|------|---------|
| Source port | 16 bits | Client: usually ephemeral; server: usually well-known. |
| Destination port | 16 bits | Server: well-known; client: ephemeral (server copies ephemeral from request). |
| Length | 16 bits | Header + data (theory 0–65,535; limited by IP total length). Not strictly necessary (IP length − IP header = UDP length), but destination UDP computes data length from its own header after IP has dropped the IP header. Formula: **UDP length = IP length − IP header length**. |
| Checksum | 16 bits | Errors over entire user datagram (header + data). |

**Well-known UDP ports taught:** 7 Echo, 9 Discard, 11 Users, 13 Daytime, 17 Quote, 19 Chargen, 53 DNS, 67/68 BOOTP, 69 TFTP, 111 RPC, 123 NTP, 161/162 SNMP(+trap).

**Services.**
- **Connectionless:** each datagram independent; not numbered; no setup/teardown; may take different paths; each request must fit in one datagram (bound taught: < 65,507 bytes). No byte-stream chopping.
- **No flow control / no window** — receiver may overflow; process must provide flow control if needed.
- **Error control:** only checksum; silent discard; no knowledge of loss/duplication.
- **Checksum covers three sections:** pseudo-header + UDP header + data. Pseudo-header comes from encapsulating IP (some fields zeroed). Protocol field ensures UDP vs TCP (same port number can exist for both). If protocol changes in transit, checksum fails → drop.
- **No congestion control** — assumes small packets; may not hold for real-time audio/video.

**Encapsulation / decapsulation.** Process → UDP (message + socket pair + length) → IP (protocol = 17) → data-link → physical (electrical/optical). Reverse: physical → link check drop H/T → IP check drop header → UDP checksum drop header → process gets data **plus sender socket** (so it can reply).

**Queuing.** Queues associated with ports. Client requests a port from OS; some implementations have in+out queues, others only incoming. One port (and eventually one in/out queue) even if talking to many peers. Queues live while the process runs. Outgoing overflow → OS may ask client to wait.

**Multiplexing / demultiplexing.** One UDP, many processes: sender many-to-one by ports; receiver one-to-many by port after error check.

**Vs bare connectionless protocol.** Only difference is UDP’s **optional checksum**; still no feedback to the sender. UDP = that simple protocol + optional checksum.

**Features as advantages.** Short request/response in one datagram each: connectionless needs **two** packets vs connection-oriented **≥ nine** → less delay. Lack of error control avoids uneven delay from retransmission and avoids TCP-style resends that worsen congestion.

**UDP package (five components):** (1) control-block table; (2) input queues (one per process; no output queues in this sketch); (3) control-block module (bind PID+port; queue number starts at zero); (4) input module (enqueue or ICMP if no port); (5) output module (create and send).

#### Numbers / formulas
- Hex dump `CB84 000D 001C 001C`: source **52100**, dest **13** (daytime), total length **28**, data **20** bytes → client→server.
- Header always **8** bytes; IP protocol **17**; practical message bound **< 65,507** bytes.

### How to answer
- Define UDP as thin connectionless unreliable transport: ports for process-to-process, silent drop, minimal overhead vs TCP.
- Draw/parse the 8-byte header; work the hex example CB84/000D/001C/001C if given.
- State: no connection, numbering, flow window, or congestion control; checksum with pseudo-header is the only error tool.
- Trace encapsulation (protocol 17) and decapsulation down to “data + sender socket.”
- Argue why “weaknesses” help short exchanges and congested networks; sketch the five-component package (table, queues, three modules; ICMP on unknown port).

---

## M14: IPSec Security Protocol

### In one line
IPsec is a network-layer framework (not one protocol) that authenticates and encrypts IP packets via SAs, AH and/or ESP, transport or tunnel mode, and IKE for key/SA setup — especially useful for VPNs without changing every host.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| IPsec | Suite that authenticates and encrypts each IP packet of a session at the network layer; host–host, gateway–gateway, or gateway–host; useful for VPNs and dial-up without changing user PCs. |
| RFC 2401 | Architecture: security associations, AH, ESP, transport/tunnel modes, IKE. |
| SA | Security association: bundle of algorithms and parameters needed by AH and/or ESP. |
| Transport mode | Crypto endpoints = communication endpoints; usually only payload protected; IP header intact so routing works. |
| Tunnel mode | Entire original IP packet wrapped in a new outer IP header; at least one crypto endpoint is a gateway; used to build VPNs. |
| AH | Authentication Header: connectionless integrity + data-origin authentication; optional anti-replay; **no confidentiality**. |
| ESP | Encapsulating Security Payload: encryption (privacy) plus optional authentication. |
| SPI | 32-bit Security Parameter Index which, with destination IP, selects the receiver’s SA. |
| ICV | Integrity Check Value from a keyed hash; destination recomputes with the shared key. |
| IKE (RFC 2409) | Internet Key Exchange: mutual authentication and SA/key establishment; main vs aggressive mode; PSK / public-key encrypt / public-key signature. |

### Concepts explained

**Why network-layer security.** Earlier approaches put security in the application. IPsec secures IP itself so dial-up and VPN access to private networks can be arranged without reconfiguring every PC. Protections: confidentiality (encrypt), integrity (checksum/hash), authentication (signatures/certificates), anti-replay, session + key management.

**Architecture (RFC 2401).** SAs feed AH and ESP; those run in transport or tunnel; IKE manages keys/SAs.

**Modes compared.**

| Mode | Protected | Header / routing | Where used |
|------|-----------|------------------|------------|
| Transport | Usually payload only | IP header neither modified nor encrypted | Between communication endpoints (hosts A and B); crypto = comm endpoints |
| Tunnel | Whole original IP packet | Encapsulated under new outer IP header | When ≥1 crypto endpoint is not a packet endpoint (e.g. A↔RA↔RB↔B); outer addresses can be RA/RB; VPNs for net–net, host–net, host–host |

**AH.** Authenticates all or part of a datagram by adding a header from datagram values; works in both modes. Layout: transport — AH after TCP+data; tunnel — AH after original IP+data. Uses hashing + shared SA key → ICV. Destination recomputes to detect modification.

| AH field | Size | Meaning |
|----------|------|---------|
| Next header | 1 byte | Protocol after AH (header chaining) |
| Payload length | 1 byte | Length of AH itself in **2-octet units minus 2** |
| Reserved | 16 bits | Zero |
| SPI | 32 bits | With dest IP → SA |
| Sequence number | 32 bits | +1 per packet; anti-replay; never reused if detection on — renegotiate SA before wrap |
| ICV | Multiple of 32 bits | May pad to 8-octet (IPv6) or 4-octet (IPv4) boundary |

AH alone is not enough for privacy — that is ESP.

**ESP.** Privacy by encrypting; also origin authenticity, integrity, optional auth. Three components (not one header):

| Component | Contents | Placement |
|-----------|----------|-----------|
| ESP header | SPI, sequence number | Before encrypted data |
| ESP trailer | Padding, pad length, next header | After encrypted data |
| ESP auth data | ICV (optional) | After encryption — cannot sit in header/trailer |

Why split: (1) block ciphers need padding **after** data → trailer; (2) auth authenticates the **encrypted** datagram after encryption.

| Field | Size | Role |
|-------|------|------|
| SPI / seq | 32 bits each | SA select; anti-replay (counter per SA) |
| Payload | variable | Encrypted content |
| Padding | 0–255 octets | Cipher block + field alignment |
| Pad length / next header | 8 bits each | Trailer |

Transport: ESP around TCP+data. Tunnel: whole inner IP protected; outer header unprotected.

**IKE (RFC 2409).** Shared-secret support so outsiders can intercept but not read/tamper. Mutual auth; establish/maintain SAs; key exchange for network-layer security. Five negotiation variations with **aggressive** and **main** modes. Three auth methods: pre-shared key, public-key encryption, public-key signature. Full crypto detail treated as out of scope.

#### Numbers / formulas
- AH payload length example: value **4** = \(3+3-2\): three 32-bit rows + three 32-bit ICV rows → **24 octets**.
- SPI and sequence number: **32 bits** each; ICV multiple of 32 bits.

### How to answer
- Define IPsec as a suite (not one protocol) securing IP for host/gateway pairs and VPNs without changing every PC.
- Name RFC 2401 pieces: SA, AH, ESP, transport/tunnel, IKE.
- Contrast transport (payload; routing headers visible) vs tunnel (whole packet; VPN outer headers).
- AH = integrity + origin auth + optional anti-replay (SPI, seq, ICV); no privacy. ESP = encryption + optional auth; header/trailer/auth split and why.
- IKE (RFC 2409): mutual auth, SA setup, main/aggressive, three auth methods.

---

## M15: Network Topologies

### In one line
A network links nodes for distributed processing; physical/logical topologies (mesh, star, bus, ring, tree) and connection types (point-to-point vs multipoint) are chosen against five criteria: performance, consistency, reliability, recovery, and security.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Node | Computer, printer, or any device that can send and receive data. |
| Distributed processing | Split a task across multiple machines instead of one large machine doing everything. |
| Transit vs response time | Message travel time between devices vs elapsed time from inquiry to answer. |
| Throughput | Successful messages per unit time (file size ÷ time), in Mbps/kbps/bps. |
| Four delay components | Processing (header at routers), queuing, transmission (push bits onto link), propagation (signal travel). |
| Point-to-point / multipoint | Dedicated link for two devices vs one link shared by >2 (spatially simultaneous or time-shared turns). |
| Physical vs logical topology | Cable/device layout vs how data actually flows (can differ). |
| Full mesh | Every node to every other: \(n(n-1)/2\) duplex links; used for backbones. |
| Passive / active / intelligent hub | Signal splitter (flood all) vs regenerator/retransmitter vs path-selecting device (router/bridge/switch) with optional diagnostics. |
| Terminator / barrel connector | Bus end-stop to prevent reflections; connector to extend the bus. |
| Token | Permission to send on a ring; only the holder may transmit. |
| Tree / expanded star | Several star networks joined by a bus backbone (stem + branches). |

### Concepts explained

**What a network is.** Set of nodes connected by communication links. Most networks use distributed processing (PCs/workstations handle subsets of a task).

**Five criteria.**
1. **Performance** — error-free transfer rate via transit/response time; depends on users, medium, hardware, software. Metrics: throughput (bandwidth, SNR, hardware limits) and delay (four components). More throughput and less delay often **contradict** via congestion.
2. **Consistency** — predictable response and data accuracy (e.g. print in ~3 s vs >30 s signals a problem). Lost data destroys confidence.
3. **Reliability** — failure frequency, recovery time, protection from catastrophe (fire, earthquake).
4. **Recovery** — return to prescribed operation with little/no lost data; based on backup files.
5. **Security** — called most important for improving performance. Threats: viruses, unauthorized access. Practices: don’t open unknown attachments; antivirus; firewalls; backups to removable media; turn off and unplug when unused.

**Connection types.** Physical structure = connection type + topology. Point-to-point: entire capacity reserved (wire, microwave, satellite; IR remote↔TV; modem pair; terminal↔FEP; workstation↔printer). Multipoint (multi-drop): share spatially or by turns.

**Physical vs logical.** Physical topology is placement of cables, devices, and interconnections — driven by access devices/media, fault-tolerance goals, and cabling cost. Logical topology is how data flows regardless of that layout; two nets can differ in distance, rate, or signal type yet share a logical shape. Four basic topologies plus tree as hybrid: mesh, star, bus, ring, tree.

**Mesh.** A node sends its own signals and relays others. True/full mesh: every node to every other with a **dedicated** point-to-point link (that link carries traffic only between those two). For \(n\) nodes: \(n(n-1)\) physical links if counted one-way, or \(n(n-1)/2\) duplex-mode links; each device needs \(n-1\) I/O ports. **Full mesh is used only for backbone networks** — very expensive redundancy; not mostly used in ordinary computer nets, but **common in wireless** (flooding or routing). Partial mesh: some systems fully meshed; the rest connect to only one or two devices (workstations indirectly linked) — less costly, less redundancy. Pros: data from different devices simultaneously; withstands high traffic; alternate path if a component fails; expansion/modification without disrupting other nodes. Cons: redundant connections; overall cost much higher; setup, maintenance, and administration difficult.

**Star.** Unlike bus (nodes on a central cable), every workstation has a point-to-point link to a central hub/router/switch, so every computer is **indirectly** connected to every other via the hub. All data passes through the center; the hub is a junction that manages/controls the network and may act as repeater/booster; it can also talk to hubs of other networks. UTP Ethernet cable is the taught workstation link.

| Hub type | Behavior |
|----------|----------|
| Passive | Simple signal splitter; keeps electrical characteristics; **routes all traffic to all nodes** → heavy load; every computer reads each address and discards non-matching frames |
| Active | Same plus electronics that **regenerate and retransmit**; can extend network size |
| Intelligent | Path selection and some management; traffic only to the receiver’s branch; can route around cable problems if redundant paths exist; **routers, bridges, switches** are examples; may include diagnostics |

Pros vs bus: better performance; a sent signal reaches the destination after no more than three or four devices and two or three links; easy add/remove; centralized monitoring; one node/link failure does not take down the rest; easy to detect and troubleshoot. Cons: too much dependency on the center — hub failure kills the whole network; hub/router/switch raises cost; how many nodes can be added depends on central capacity.

**Bus (linear).** Simplest topology. All nodes (computers and servers) connect to a single backbone cable with interface connectors. Signal is **broadcast** to all workstations; only the intended recipient whose MAC or IP matches accepts; others discard. A **terminator** at each end prevents bouncing; a **barrel connector** can extend the bus. Pros: easy to set up and extend; least cable; costs very little; mostly used in small networks/LANs. Cons: limit on central-cable length and node count; main-cable failure breaks the whole network; proper termination required; hard to detect/troubleshoot a fault at an individual station; maintenance cost can rise; efficiency falls as device count rises; unsuitable for heavy traffic; **security is very low** because all computers receive the sent signal.

**Ring.** Nodes form a closed loop; each workstation connects to two neighbors; data travels in **one direction**. Send/receive uses a **token** sent with data. Next node checks whether the signal is for it: if yes, receives and puts an empty token back; otherwise passes token plus data onward. **Only the node holding the token may send**; others wait for an empty token. Found in offices, schools, and small buildings. Pros: organized; fewer collisions; traffic in one direction at very high speed; under increasing load better than bus; no network server required to control connectivity; additional components do not affect performance; equal access to resources. Cons: each packet must pass all computers between source and destination → slower than star; if one workstation or port goes down, the entire network is affected; highly dependent on the wire; MAUs and network cards are expensive compared with Ethernet cards and hubs.

**Tree (expanded star).** Integrates star and bus: several star networks connected using a bus. Main cable is the tree stem; stars are branches. Also called expanded star; Ethernet commonly used; each segment has dedicated point-to-point wiring to a central hub. Pros: used where star or bus alone cannot scale; expansion easy; network divided into manageable segments; error detection/correction easy; if one segment is damaged, other segments are not affected. Cons: relies heavily on the main bus cable — if it breaks, the whole network is crippled; more nodes/segments make maintenance difficult; scalability depends on the type of cable used.

### How to answer
- Define network + distributed processing; list five criteria with one concrete detail each (throughput vs delay trade-off; backups; antivirus/firewall/unplug).
- Distinguish point-to-point vs multipoint (spatial/time-share) and physical vs logical topology.
- For each topology give structure + 2–3 pros/cons; write full-mesh formula \(n(n-1)/2\).
- Contrast hub types (passive/active/intelligent) and bus terminator/barrel roles.
- Match topology to need: backbone → mesh; easy growth → star; cheap small LAN → bus; ordered access → ring; scale segments → tree.

---

## M16: Animated Cursor Vulnerability — Proof of Concept I

### In one line
A 2007 Windows animated-cursor (`.ANI`) buffer overflow in `user32.dll` shows how a client-side web visit can achieve remote code execution past a perimeter firewall — still relevant on unpatched XP/2000/Vista.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| CVE | Common Vulnerabilities and Exposures — public catalog of named software flaws. |
| Animated cursor / `.ANI` | Variable-size Windows pointer animation loaded through `user32.dll`. |
| RIFF | File header format identifying an animated cursor (`52 49 46 46`); must stay intact or the loader rejects the file. |
| Network firewall | Perimeter filter for *inbound* traffic; does not stop an insider who browses out to a hostile page. |
| Client-side attack | Compromise that starts because the insider visits a hostile site the organization already allows (HTTP/HTTPS outbound). |
| Remote code execution (RCE) | Running code on another person’s machine without proper authorization — attacker’s “ultimate goal” to steal data or act as the victim. |
| EIP | Instruction pointer; if overflow overwrites it with attacker-controlled data, the next instruction address is untrusted. |
| Patch | The taught avoidance: update the OS so the cursor loader no longer overflows. |

### Concepts explained

**CVE context.** The previous lecture introduced CVE (Common Vulnerabilities and Exposures). This module applies that idea to a real Windows flaw: the animated cursor vulnerability — still taught because legacy, unpatched systems remain in the wild.

**What an animated cursor is.** Windows ships many mouse pointers. Examples taught:

| Cursor | Character in this lecture |
|--------|---------------------------|
| I-beam (“I”) | Text caret in Notepad; small, not an animation |
| Hourglass | Animated sand falling from one bulb to the other |
| Horse-riding pointer | Larger animated cursor |

Animated pointers **differ in file size**. Loading them was implemented in **`user32.dll`**.

**Public flaw description.** A public write-up states the issue can be triggered from a **malicious web page** and can result in **remote code execution**:

- **Malicious web page** — a site the *user* chooses to visit that hosts hostile content.
- **Remote code execution** — running code on another person’s machine **without proper authorization**. The lecture treats RCE as an attacker’s “ultimate goal”: steal information or otherwise act as the victim.

**Client-side vs perimeter firewall.** Organizational security is often implemented at the **periphery**. A network firewall filters traffic *entering* the organization. That model fails when someone **inside** browses a hostile site. Most organizations **allow outbound HTTP and HTTPS**. If the destination page hosts a malicious cursor, the visitor can be compromised. That pattern is a **client-side attack**: the client approaches the attacker.

**Why a 2007 bug is still taught.** The vulnerability was discovered in **2007**. Legacy systems still run old, unpatched operating systems. Affected families named: **Windows XP**, **Windows 2000**, and **Windows Vista**.

The demonstration is framed as an **isolated lab** (hypervisor host, a Linux web role, a Windows XP browser role) so students can see that a page which merely **assigns a CSS cursor** can make Internet Explorer **load a `.ANI` file**. The file format is **RIFF** (`52 49 46 46`). A **buffer overflow** in the loader can overwrite the **instruction pointer (EIP)** — the diagnostic that attacker-controlled data became the next-instruction address.

**Defender constraints taught.** Two constraints matter for defenders as well as for understanding the bug class:

1. The file must remain a **recognized cursor** (the **RIFF** header must stay intact or the loader rejects it).
2. Control of EIP is the classic **buffer-overflow** observation: if the next-instruction address is attacker-controlled, **arbitrary / remote code execution** becomes possible.

**Closing assignment.** Study **client-side attacks** and **buffer overflow**. The avoidance taught here is **patching** the OS so the cursor loader no longer overflows.

### How to answer
- Define CVE; place the animated-cursor bug as a named Windows loader flaw (2007).
- Explain client-side attack vs inbound firewall: user goes out on allowed HTTP/HTTPS.
- State mechanism at concept level: variable-size `.ANI` via `user32.dll`; malformed file → buffer overflow → EIP overwrite → RCE.
- Note trigger: CSS cursor URL to crafted RIFF `.ANI`; affected XP/2000/Vista if unpatched.
- Close with **patch** and study of client-side attacks + buffer overflow.

---

## M17: Animated Cursor Vulnerability — Proof of Concept II

### In one line
After EIP is attacker-controlled, execution can be steered via already-mapped DLL code and victim-initiated (reverse) outbound sessions that firewalls already allow — so least privilege, patch/hotfix, and caution with links are the taught defenses.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Mapped DLL | Code already loaded in the process (`user32`, `shell32`, `kernel32`, `ntdll`, …) that overflow control can aim at so the CPU enters attacker-chosen behavior. |
| Bind vs reverse shell | Bind: victim listens, outsider connects *in* (often blocked inbound). Reverse: victim connects *out* carrying a shell — same class of outbound traffic orgs allow for the web. |
| Shellcode | Instructions that, if run, give a command interpreter on the remote machine. |
| Least privilege | Do not browse as Administrator; the attacker inherits the logged-in user’s token. |
| cve.mitre.org | Public CVE catalog across Windows, Linux, Mac, custom OS — look up flaws and apply patch/hotfix. |
| Malware / ransomware / CryptoWall | Harmful software; CryptoWall encrypts victim files and demands payment — ransomware; malvertising delivers malware via ads. |

### Concepts explained

**Continuation of PoC I.** Lecture I stopped after showing that a malformed `.ANI` can overwrite **EIP**. This session extends the same **Internet Explorer + crafted cursor** demonstration on **Windows XP** to show how buffer overflow plus a malicious web page can yield **remote access** — and then how to **think about stopping it**.

**Reusing mapped library code (concept, not recipe).** Memory holds the browser process **and many DLLs** (`user32.dll`, `shell32.dll`, `kernel32.dll`, `ntdll`, …). The lecture’s *idea* (not a recipe) is that once EIP is attacker-controlled, it can be pointed at an instruction **already present** in a loaded module so the CPU **enters the overflowed buffer**. Registers are inspected in a debugger because there is **no fixed map** of where a variable-size cursor lives; a large animation may sit on a **heap** reached by a **pointer-to-pointer**. **Byte order** (little-endian / host vs network) is mentioned because multi-byte addresses in a file are stored reversed from how humans write them.

**Shell models and the firewall you already allow.** **Shellcode** is defined as instructions that, if they run, give a **command interpreter** on the remote machine. Two delivery *ideas* are distinguished as firewall-relevant models:

| Model | Idea as taught | Why it matters to a defender |
|-------|----------------|------------------------------|
| Bind | Victim listens; outsider connects *in* | Needs an inbound path the perimeter often blocks |
| Reverse | Victim connects **out** to the other party, carrying the shell | Uses a connection the victim **initiates** — the same class of outbound HTTP/HTTPS organizations already allow |

The demonstration’s lesson is that a **user-initiated outbound** session can carry a remote shell, and that **killing the browser does not necessarily drop** that session. **`netstat`** on the victim would show an **ESTABLISHED** outbound TCP connection after the URL was opened.

**Privilege of the logged-in user.** If the captured shell is **Administrator**, it is because the user **surfed as Administrator**. Explicit security rule: browse the Internet with **minimal privilege**. If a cursor (or any other) bug runs, the attacker inherits **the logged-in user’s rights**. Administrative browsing turns one client-side bug into **full machine control**.

**Email and the firewall you cannot use.** A second attack vector is **social**: a lottery / prize email whose **link** is a page like the lab’s. The user **clicks on purpose**. **No firewall in the world** can treat that as hostile in the same way as unsolicited inbound packets: it is **legitimate outbound HTTP/HTTPS**.

**Where to look up flaws; what unpatched bugs cost.** **cve.mitre.org** lists vulnerabilities for Windows, Linux, Mac, and custom OS. If a flaw is not patched / no hotfix is applied, outcomes named here are: remote code execution (as demonstrated); data theft; compromise of **critical infrastructure** if the OS sits on a **SCADA**-class system. The advisory language cited: this **CVE-2007** animated-cursor issue exposes **Windows XP, Windows 2000, and Windows Vista**.

**Software, hardware, firmware — and malware.** Beyond the old triad software / hardware / firmware, the lecture adds **malware**: software that **damages** the system. Related coinages: **malvertising** (malware delivered via advertisement). A then-current example: **CryptoWall** — encrypt the victim’s data and demand money to unlock it: **ransomware**. Later course topics promised (not taught in this hour): ransomware, CryptoWall, viruses, worms, Trojans.

### How to answer
- After EIP is untrusted, control can use **already-mapped DLL code**; defender answer remains **patch the loader**.
- Contrast bind vs reverse; reverse matches allowed outbound web paths; session may survive browser kill.
- State least privilege: attacker inherits logged-in rights.
- Link lottery-style email to the same client-side pattern.
- Cite cve.mitre.org + patch/hotfix; name malware/ransomware/CryptoWall as the next threat category.

---

## M18: Electronic Mail

### In one line
Modern email is store-and-forward messaging: user agents format with RFC 5322/MIME, MTAs move mail with SMTP (MAIL/RCPT/DATA + MX), and clients read with POP3, IMAP, or MAPI.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Store-and-forward | Servers accept, forward, deliver, and store; sender and recipient need not be online together. |
| User agent (MUA/UA) | Local program to compose and read mail (CLI, menu, or GUI). |
| MTA / MSA / MDA | Message Transfer / Submission / Delivery agents along the SMTP path. |
| MIME (RFC 2045–2049) | Multipurpose Internet Mail Extensions: typed content, transfer encodings, multipart body tree (from RFC 1341). |
| RFC 5322 | Current Internet message format (lineage: RFC 822 → 2822 (2001) → 5322 (2008)). |
| SMTP / ESMTP | Transfer protocol: RFC 821 (1982) then RFC 5321 (2008) extended SMTP; connection-oriented text commands over TCP. |
| MX record | DNS mail exchanger naming the host for the domain after `@`. |
| LMTP | Local Mail Transfer Protocol — SMTP derivative for the MDA hop. |
| POP3 | Port 110; typically download-and-delete; Authorization → Transaction → Update (RFC 1939). |
| IMAP4 | Port 143; server-resident mail as truth; folders and partial fetch (RFC 3501). |
| MAPI | Proprietary Microsoft protocol for Outlook ↔ Exchange only. |

### Concepts explained

**Email as a system.** Digital messages sent/received over the Internet (or other networks) from one sender to one or more recipients. Early systems required author and recipient online at the same time. Today’s systems use **store-and-forward**: servers accept, forward, deliver, and store; neither users nor their computers need to be online together.

**Five basic functions.**

| Function | Role |
|----------|------|
| Composition | Creating messages and replies; any text editor can write the body; the system helps with addressing and header fields |
| Transfer | Moving the message from originator to recipient |
| Reporting | Telling the originator what happened: delivered, rejected, or lost |
| Displaying | Presenting incoming mail so people can read it |
| Disposition | What the recipient does next: discard unread, discard after reading, save, and similar |

**Two subsystems.**

| Subsystem | What it is | Protocols named here |
|-----------|------------|----------------------|
| User agent (UA) | Local program to compose and read (CLI, menu, or GUI) | Formatting: RFC 822 and MIME (first proposed in RFC 1341). Reading: POP3, IMAP, MAPI |
| Message transfer agent (MTA) | Background daemons that move mail through the network | SMTP |

**Message format lineage.** Internet mail format is **RFC 5322**, with multimedia in **RFC 2045–2049** (MIME). Lineage: **RFC 822** (nearly 20 years) → **RFC 2822** (2001) → **RFC 5322** (2008). A message has header and body separated by a **blank line**. Body is unstructured text, sometimes ending in a signature block. Each header field is logically one line of ASCII: field name, colon, value. RFC 822 did not cleanly separate envelope fields from header fields.

**Transport-related headers.**

| Field | Meaning |
|-------|---------|
| To | DNS address of primary recipient(s); multiple allowed |
| Cc | Secondary recipients; for delivery, primary and secondary are not distinguished |
| Bcc | Like Cc, but this line is deleted from copies sent to primary and secondary |
| From | Who wrote the message |
| Sender | Who sent it — need not be the same person as From |
| Received | Added by each MTA; agent identity, date/time, extra data for routing debugging |
| Return-Path | Added by the final MTA; how to get back to the sender |

**UA/human headers:** Date, Reply-To, Message-ID, In-Reply-To, References, Keywords, Subject.

**Why MIME exists.** Early mail was English ASCII text. RFC 822 specified headers and left body content to users — not enough for audio, image, text, video attachments. Fix: RFC 1341, updated as RFC 2045–2049 (MIME).

**Five MIME header fields:** MIME-Version (this is MIME, which version); Content-Description (ASCII what is in the message); Content-ID; Content-Transfer-Encoding (how the body is wrapped for networks that object to characters beyond letters/digits/punctuation); Content-Type (`type/subtype`, e.g. `video/mpeg`). Types listed: text, image, audio, video, application, message, multipart.

**MIME body as a hierarchy.** Parts in a tree. Top is the root body part. Parts that contain other parts are descendants. Containers = multipart body parts; leaves with no further parts = content body parts (plain text, attachment, HTML page, …).

**SMTP.** Internet standard for email transmission: first RFC 821 (1982); updated 2008 as extended SMTP (ESMTP) in RFC 5321. Connection-oriented and text-based: sender issues commands and supplies data over a reliable, ordered TCP stream.

**Mail processing model.** MUA submits to MSA with SMTP on TCP **587** (many providers still allow **25**) → MSA hands off to MTA (often two instances of the same software with different launch options) → boundary MTA finds target via DNS **MX** for the domain right of `@` → MTA connects to that MX as SMTP client → MX hands message to MDA for local delivery into the mailbox format → MDA may store locally or forward with SMTP or **LMTP** → end-user clients retrieve with IMAP, POP3, or MAPI.

**SMTP session and transaction.** Session: client commands and server responses; opens, parameters exchanged, may contain zero or more transactions. A transaction is three command/reply sequences: **MAIL** (return address / bounce / envelope sender); **RCPT** (one recipient; may be issued multiple times — also envelope data); **DATA** (header + body separated by an empty line).

**POP3 (Post Office Protocol version 3).** Basic procedure: retrieve all inbound messages to the client, delete them on the server, disconnect — user pulls mail from the ISP’s MTA. Simple and robust when mail is always read from one PC. Specs: RFC 1939 (from RFC 1081); extension RFC 2449; authentication RFC 1734. Opens TCP to MTA on port **110**. Three states in order: **Authorization** (login) → **Transaction** (collect and mark for deletion: LIST, RETR, DELE) → **Update** (marked messages actually deleted on QUIT). Observable with Telnet to `mail.isp.com` port 110 (ASCII banner, then username/password).

**IMAP (Internet Message Access Protocol).** POP3 fails when the user needs mail from other computers — that gap produced IMAP. Defined in RFC 2060; current IMAP4 in RFC 3501. Connection-oriented. Standard procedure: **leave messages on the server**; client copies allowed, but in an inversion of POP3 the **server copies are the real ones**. Security benefit: you do not lose mail if the client disk fails. Server listens on port **143**. Further facilities: read messages or **parts** of messages (important with large audio/video attachments); create, destroy, and manipulate **multiple mailboxes** on the server (e.g. one mailbox per correspondent).

**MAPI.** Proprietary Microsoft protocol used by Outlook to talk to Microsoft Exchange. Offers somewhat more functionality than IMAP, but only for Outlook ↔ Exchange.

### How to answer
- Define store-and-forward + five functions; split UA (format) vs MTA (SMTP transfer).
- Cite RFC 5322 lineage and MIME’s five headers + multipart tree purpose.
- Trace submission 587/25 → MX → MAIL/RCPT/DATA.
- Contrast POP3 (download-delete, 110, three states) vs IMAP (server truth, 143, folders/partial) vs MAPI (Outlook/Exchange only).

---

## M19: Email Security Protocols

### In one line
Unprotected email is a postcard on untrusted relays; PGP/OpenPGP and S/MIME secure it with hybrid crypto and signatures, while PEM (single-root X.509 + DES) never deployed.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Postcard model | Email contents visible to every relay handler — unlike a sealed letter whose envelope can show tampering. |
| PGP | Pretty Good Privacy (Phil Zimmermann, 1991): hybrid IDEA+RSA, MD5 signatures, ZIP, free multi-OS email privacy package. |
| Session key | One-time symmetric key for bulk encryption; RSA wraps it under the recipient’s public key. |
| Alien-strength RSA | 2048-bit RSA; lecture recommendation for all PGP use (RSA only wraps tiny blobs). |
| OpenPGP | IETF standard RFC 4880 (from RFC 1991 / 2440); Camellia RFC 5581; ECC RFC 6637; both parties must participate. |
| PEM | Privacy-Enhanced Mail RFC 1421–1424; DES; rigid single-root X.509; CRLs; proposed but never widely deployed. |
| Web of trust | PGP’s decentralized PKI answer to PEM’s single central root. |
| IPRA / PCA | Internet Policy Registration Authority / Policy Certification Authority in PEM’s certificate hierarchy. |
| MOSS | MIME Object Security Services — post-PEM MIME security effort leading toward S/MIME. |
| S/MIME | Secure MIME (RFC 2632–2643): authentication, integrity, secrecy, non-repudiation inside MIME with multiple trust anchors. |
| Non-repudiation | S/MIME service (with auth, integrity, secrecy) so a sender cannot later deny the message. |

### Concepts explained

**Why privacy is hard.** Since about 1993, “email” is the common name for exchanging digital messages over the Internet or other networks. Email privacy covers unauthorized access and inspection while the message is **in transit** and while it is **stored** on a server or user computer. Mail crosses potentially untrusted intermediate servers. There is no inherent way to tell if an unauthorized party read it. Unlike a sealed letter (where the envelope might show tampering), email is like a **postcard**: contents are visible to everyone who handles it. Cryptography can make unauthorized access difficult if not impossible, but messages often cross national borders with different rules, so privacy is legally as well as technically complicated. That problem drove PGP, PEM, and S/MIME.

**PGP — Pretty Good Privacy.** A public-key encryption program originally written by Phil Zimmermann in 1991. It became a de facto standard for encrypting Internet email: a complete package for privacy, authentication, digital signatures, and compression, easy to use, with source code free on the Internet, on Unix, Linux, Windows, and Mac.

**PGP confidentiality.** The message is encrypted with a symmetric algorithm under a one-time session key. The session key travels with the message, itself encrypted under the receiver’s public key. Only the receiver’s private key unwraps the session key.

**Authentication/integrity.** Integrity: detect post-finish change. Authentication: claimed sender. Encrypted content → wrong key fails decrypt. Digital signature: hash plaintext, sign hash with sender’s private key (RSA or DSA).

**Alice → Bob flow taught.**
1. MD5 of P; encrypt hash with Alice’s RSA private → signed hash.
2. Concatenate with P → ZIP compress → P1.Z.
3. IDEA encrypt with session key; RSA-encrypt IDEA key with Bob’s public; Base64.
4. Bob: reverse Base64; RSA-decrypt IDEA key with his private; IDEA decrypt; decompress; verify MD5 with Alice’s public.
5. RSA used **only twice** (128-bit MD5 + 128-bit IDEA key) — efficiency.

**RSA key-length labels:** Casual 384 (easy break); Commercial 512 (three-letter org); Military 1024 (not breakable on Earth); Alien 2048 (not on other planets either) — use Alien always.

**Classic PGP message parts:** Key (identifier + IDEA key); Signature (header, timestamp, sender key id, algorithms, encrypted MD5); Message (header, default filename, creation timestamp, content).

**OpenPGP.** Most widely used email-encryption standard in the lecture. IETF OpenPGP WG; standards track. History: July 1997 proposal; RFC 1991 → 2440 → **4880** (2007); Camellia **5581**; ECC **6637**. Secures delivery and at-rest files (mobile/cloud); both parties must run it; verifies who created/sent.

**PEM.** Official IETF 1993 proposal (PSRG/IRTF roots). Steps: canonicalize whitespace → hash MD2/MD5 → concatenate → encrypt with **DES** (56-bit flagged as suspect) → optional Base64; one-time key via RSA or 3DES-EDE. Key management: X.509 from CA under **single root**; CRL revocation advantage. **Never deployed** because: who runs the root (politics); RSA Security wanted to charge per certificate (US patents; free outside US culture); rejection of central authority → Zimmermann’s web of trust; then MIME needs → MOSS/S/MIME. PEM idea: hierarchical auth via IPRA/PCA certifying senders’ public keys.

**S/MIME.** MIME itself has **no security**; S/MIME adds signatures/encryption via new MIME headers. Services: authentication, integrity, secrecy, non-repudiation; flexible algorithms. Lesson from PEM: **multiple trust anchors** (valid if chains to some anchor the user trusts), not one rigid root.

**Comparison.** PEM collapsed. Currently used: **S/MIME v3** and **OpenPGP** (similar services, incompatible formats — like GIF vs JPEG).

| Topic | S/MIME v3 | OpenPGP |
|-------|-----------|---------|
| Packaging | Binary CMS MIME | Contrasted MIME/ASCII-oriented forms |
| Certificates | Binary X.509v3 | Classic PGP certificates |
| Key agreement / signatures | Diffie–Hellman with DSS or RSA | ElGamal with DSS |
| Hash | SHA-1 | SHA-1 |

### How to answer
- Postcard vs sealed letter; transit + at-rest + jurisdiction.
- PGP hybrid flow (IDEA + RSA on tiny blobs + ZIP + MD5); push 2048-bit RSA; name OpenPGP RFCs.
- PEM: DES + single X.509 root + why it died (root politics, patent fees, MIME).
- S/MIME: MIME-native services + multiple trust anchors vs PEM’s one root.
- S/MIME v3 vs OpenPGP: same user services, incompatible certificates/encodings.

---

## M20: WWW Security

### In one line
The Web’s two-way, highly visible client–server model needs security at IP (IPsec), above TCP (SSL/TLS/HTTPS), in the application (SET, PGP, S/MIME), and at the border (packet-filter vs proxy firewalls), plus user awareness.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Passive vs active Web attack | Passive: eavesdrop / read restricted data. Active: impersonate, alter messages in transit, alter site content. |
| IPsec transport / tunnel | Transport: protect transport-layer payload into IP. Tunnel: wrap entire original IP packet under a new outer header. |
| AH vs ESP | AH: source authentication + integrity. ESP: those plus confidentiality (header + trailer; auth data at end). |
| SSL / TLS | Security just above TCP: Record, Handshake, Change Cipher Spec, Alert; goals auth, confidentiality, integrity. |
| HTTPS | HTTP carried inside SSL/TLS (`https://` instead of `http://`). |
| SET | Secure Electronic Transaction: Mastercard/Visa card-payment security specs (not a payment system); DES + RSA + SHA-1; merchant never sees PAN. |
| Packet filter | Forward/block by IP, ports, protocol (TCP/UDP); static (router table) or stateful (appliance). |
| Application gateway | Proxy that is server to client and client to server; inspects application content (e.g. URLs on port 80). |

### Concepts explained

**Why the Web is a hard target.** The WWW is framed as one of the biggest inventions and the world’s largest information resource — anywhere, anytime, any format — and a breeding ground for e-business. Technically it is a **client–server application on Internet/TCP/IP**: pages stored on servers, retrieved by browsers. Online banking and transactions need special attention. Challenges not always appreciated in ordinary computer/network security:

- The Internet is **two-way**, unlike traditional publishing, teletext, voice response, or fax-back.
- Sites are vulnerable to attacks on web servers over the Internet.
- The Web is a **highly visible** outlet for corporate/product information and a platform for business transactions — reputation and money at stake.
- Servers are easy to use/configure, but **underlying software is extraordinarily complex** and can hide flaws; “properly” installed new/upgraded systems have still been attackable.
- A subverted server can be a **launching pad** into the rest of a corporation — data and systems not part of the Web itself but connected on the local site.
- Casual, untrained users often do not know the risks and lack countermeasure tools.

**Threat taxonomy.** Passive: eavesdropping on browser–server traffic; gaining restricted site information. Active: impersonating another user; altering messages in transit; altering information on a website. Main threats briefed as integrity, confidentiality, authentication, and denial of service:

| Threat | Main examples taught | Consequences | Countermeasures taught |
|--------|----------------------|--------------|------------------------|
| Integrity | Modification of user data; Trojan-horse browser; modification of memory; modification of message traffic in transit | Loss of information; compromised machine; exposure to all other threats | Cryptographic checksums / SSL |
| Confidentiality | Eavesdropping; theft from server or client; leakage of network configuration and of who talks to whom | Loss of information; loss of privacy | Encryption and web proxies |
| Authentication | Impersonating legal users; data forgery | Misrepresentation; users believe false information is valid | Cryptographic techniques |
| Denial of service | Killing user threads; flooding with bogus requests; filling disk or memory; isolating a machine via DNS attacks | Disruptive; users cannot get work done | **Very difficult to prevent** |

**Where to put Web security.** Approaches are similar in service but differ in scope and location in the TCP/IP stack: network (IPsec), transport (SSL/TLS), application (SET; PGP/S/MIME for mail), and firewalls.

**Network layer — IPsec.** Collection of IETF protocols securing packets at the network layer. Advantages: transparent to end users and applications (general-purpose); filtering so only selected traffic pays the IPsec processing cost. Creates authenticated and confidential packets for IP.

| Mode | What is protected | Header handling | Typical use |
|------|-------------------|-----------------|-------------|
| Transport | Payload from transport into IP — not the whole original IP header | IPsec header/trailer wrap that payload; IP header added later | Host-to-host |
| Tunnel | Entire original IP packet (including its header) | Apply IPsec, then add a new IP header (different from the original) | Router–router, host–router, or router–host — imaginary tunnel |

Relative placement: transport sits between transport and network; tunnel flow is network → IPsec → network again. **AH:** authenticate source and ensure integrity of IP payload (hash + symmetric key → message digest). **ESP:** AH does not provide confidentiality; ESP adds source authentication, integrity, and confidentiality; header and trailer added; ESP authentication data sit at the end of the packet (easier calculation).

**Transport layer — SSL/TLS.** Security just above TCP. Two implementation choices: (1) SSL as part of the underlying protocol suite — transparent to applications; (2) SSL embedded in specific packages — e.g. Netscape and Microsoft Internet Explorer browsers, and most servers. Goals: server and client authentication, data confidentiality, data integrity. HTTP encapsulating data in SSL records uses **`https://`** (HTTP Secure) — e.g. credit-card numbers for online shoppers.

SSL is four protocols in two layers:

| Protocol | Role |
|----------|------|
| Record | Carrier: messages from the other three protocols and application data; Record messages are payload to TCP |
| Handshake | Security parameters for Record: cipher suite, keys; authenticates server to client and client to server if required |
| Change Cipher Spec | Signals that cryptographic secrets are ready |
| Alert | Reports abnormal conditions |

**Application layer — SET (and named mail crypto).** Application-specific security embedded in particular apps. For the Web, the important example is **SET** on top of HTTP (some implementations use TCP directly). Email at this layer: PGP and S/MIME (fully specified in M19).

SET is an open encryption and security specification to protect credit-card transactions on the Internet. SET 1 came from a Mastercard and Visa call for standards in February 1996; companies involved included IBM, Microsoft, Netscape, RSA; first wave of SET-compliant products around 1998. **SET is not itself a payment system** — it is protocols and formats that let users employ the existing credit-card infrastructure on an open network securely. Three services: secure communication channel among all parties; trust via X.509v3 digital certificates; privacy — information only to parties when and where necessary.

| Feature | Mechanism taught |
|---------|------------------|
| Confidentiality | Cardholder account and payment data protected in transit. **Merchant does not learn the credit-card number** — only the issuing bank does. Conventional encryption with DES |
| Integrity | Order information, personal data, payment instructions unchanged. RSA digital signatures with SHA-1 hashes; some messages also HMAC-SHA-1 |
| Cardholder account authentication | Merchant verifies the holder is a legal user of a valid account. X.509v3 with RSA signatures |
| Merchant authentication | Cardholder verifies the merchant has a relationship with a financial institution that allows it to accept cards. X.509v3 with RSA signatures |

Unlike IPsec and SSL/TLS, SET provides **only one choice per cryptographic algorithm** — appropriate because SET is one application with one requirement set.

**Firewalls.** Previous measures cannot stop a sender from emitting harmful messages. To control access, use a firewall: usually a router or dedicated machine between the internal network and the rest of the Internet that forwards some packets and filters others (by host or service). Classification: packet-filter vs proxy-based.

**Packet-filter firewalls.** Forward or block using network- and transport-layer headers: source/destination IP, source/destination ports, protocol (TCP or UDP). Often a router with a filtering table. Lecture examples: block incoming from entire network `131.34.0.0`; block incoming to internal Telnet (port 23); block incoming to internal host `194.78.20.8` (internal use only); block outgoing to HTTP port 80 (organization does not want employees to browse). Split: **static** (can be routers) vs **stateful** (standalone firewall devices).

**Proxy firewalls / application gateways.** Packet filters cannot see application content. Example policy: only Internet users who already have a business relationship may see the company web page. Everything arrives at port 80, so the filter cannot distinguish — the check must use **URLs** at the application layer. Solution: a proxy computer (application gateway) between internal and external hosts — server to the client and client to the server. Flow: client message received by gateway server process → gateway opens the packet at the application layer and tests whether the request is legal → if legal, acts as client toward the real server → if not, message dropped and error sent to the external user.

**Close.** As dependence on the WWW grows and crucial information moves over it, need for security increases. Controls exist at network, transport, and application layers and as firewalls, but the user must still be diligent. **User awareness** protects against many threats.

### How to answer
- Why Web ≠ traditional publishing: two-way, visibility, complexity, pivot from hacked server, untrained users.
- Passive/active + four threat rows with one countermeasure each; call out DoS as hard.
- Place IPsec / SSL-TLS-HTTPS / SET-PGP-S/MIME / firewalls in the stack.
- SET: not a payment network; hides PAN from merchant; pins algorithms.
- Packet filter vs proxy: who-on-port-80 needs application gateway; end with user diligence.

---

## M21: Mobile Code Security

### In one line
Mobile code (applets to agents) buys flexibility and bandwidth but creates two-way risk — hosts can be protected with sandboxing, signing, PCC, and fine-grained access control, while protecting code from a malicious host remains research and needs cryptography.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Mobile code | Programs that execute on one or several hosts other than their origin (simple applets through intelligent agents). |
| Sandbox | Restricted execution environment (e.g. JDK 1.0 applets); confines code and enforces fixed policy — often too limited to be useful alone. |
| Authenticode / digital shrink-wrap | Producer digitally signs; consumer verifies origin before run (Microsoft Authenticode); combinable with sandbox (Sun Java 1.2). |
| PCC / VCGen | Proof-carrying code (Necula & Lee, CMU): producer supplies a proof of safety; consumer’s VCGen emits safety predicate; proof checker validates — then install without further runtime checks. |
| Code signing (JDK 1.1 / ActiveX) | Valid signature → full trust / all Java features; unsigned → JDK 1.0-style sandbox; coarse all-or-nothing ACL left to the end user. |
| JAAS | Java Authentication and Authorization Service: ties the **identity of the user running the code** into access control (JDK 1.2+ finer policies). |
| Forward integrity / PRAC | Hash-chaining so collected agent data stays integral up to the first malicious host; PRAC = small partial-result authentication code over all offers. |
| Sliding encryption | Compact encryption for tiny data collected on many hops without excessive RSA padding / storage growth. |
| Holographic proof + PIR | Probabilistically check a computation proof by examining few bits (polylog time); PIR hides which bits the verifier queries from the proving host. |
| Function hiding | Encrypt function \(f\) into \(E(f)\); run \(E(f)(x)\) on untrusted host; decrypt output to get \(f(x)\) — confidentiality without extra hardware. |

### Concepts explained

**Paradigm.** Producer vs consumer (running host). Advantages vs traditional distributed computing: design flexibility beyond OOP; bandwidth optimization. Cost: Internet-style intrusion risk.

**Two threat directions.** (1) Classical: malicious applet/ActiveX attacks the remote host. (2) Less classical: remote environment subverts the mobile code and its data.

**Host-protection requirements when mobility applies:** authenticate origin (separate identities); verify integrity (code exposed on network); access control + semantic verification (another party generated the code).

**Code-protection threats from host:** spoofing owner; theft/secrecy violation; integrity violation of code semantics — protect data segments and semantics.

**Host defenses.**
1. **Sandboxing** — confine via type checking / language / protection domains; fixed policy; JDK 1.0 applets; drawback: seldom useful.
2. **Digital shrink-wrap / Authenticode** — cannot decide malice from bits alone, but can verify claimed source; combine with sandbox.
3. **PCC** — five steps: producer annotates (certifying compiler) → consumer VCGen (simple safety + emit predicates → safety predicate) → proof producer proves → proof checker (axioms/rules, same predicate) → trusted install, no further runtime checks. Consumer need not trust the proof producer.
4. **Code signing** — ActiveX then JDK 1.1: signature ≠ unrestricted trust; users deciding from signatures is questionable; all-or-nothing access risks entire security even without admin rights.
5. **Access control** — finer application-specific policies; signer identity via PKI; JDK 1.2; JAAS adds user identity; best of sandbox+signing for useful software; cost = dynamic runtime enforcement.
6. **Program checking** — static/dynamic structure or behavior vs policy; PCC as static checking where checking a proof is cheaper than proving; automating proof generation still hard (often by hand).

**Protecting code from malicious host (harder — host has total control).** Classify data vs code; integrity vs confidentiality.

**Data protection for agents** (e.g. comparison shopping / auctions): know if collected data changed; if itinerary followed; if host cannot exploit previous bids. Integrity: sign each result (size grows linearly) or **hash chaining / PRAC** for forward integrity; signatures if non-repudiation needed. Confidentiality: encrypt each hop; **sliding encryption** when data are tiny.

**Integrity of computation.** Fault tolerance: replica hosts + vote, or slightly altered replica agents to spot malice. Cryptographic proof/hint: computation trace → **holographic proof** (few bits); validity requires query bits unknown to prover → **PIR**; hidden-query results + answer smaller than original proof.

**Privacy of computation.** Tamper-proof hardware (smart card) as secure kernel; **function hiding** for matrix-representable functions / Boolean circuits — standalone confidentiality.

**Close.** Good host protection achievable (finer ACLs, semantic analysis). Protecting code from malicious host = **open research**. Non-cryptographic methods generally **not enough** for the code.

### How to answer
- Define mobile code; name flexibility/bandwidth benefits and two threat directions.
- List four host requirements; walk sandbox → shrink-wrap → PCC → signing caveats → JAAS-style ACL → program checking.
- For agents: hash chains/PRAC, sliding encryption, replicas/voting, holographic proofs+PIR, smart cards, function hiding.
- Verdict sentence: host protection in reach; code vs malicious host research; crypto required.

---

## M22: Transmission Media

### In one line
Transmission media (physical-layer communication channels) are guided (UTP/STP, coax, fiber) or unguided (radio, microwave, infrared), with rate and reach set by bandwidth, impairment, interference, and number of receivers.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Communication channel | Synonym for transmission media: pathway carrying electrical or electromagnetic signals from sender to receiver. |
| UTP / STP | Unshielded twisted pair (RJ-45; cheapest, here fastest copper) vs foil/braid-shielded pair (better noise immunity; must be grounded; costly; rare in Ethernet). |
| Subscriber loop | Twisted pair from residential phone to the telephone end office. |
| Baseband / broadband coax | Baseband: one high-speed digital signal (mostly LANs, ~50 Ω). Broadband: many analog FDM signals on CATV plant. |
| BNC / T / terminator | Coax connectors: end to device; T-branch to a computer; terminator stops reflection. |
| Critical angle | Substance property governing refraction vs bending along interface vs total internal reflection in fiber. |
| Step-index / graded-index / single-mode | Multimode constant-density core (abrupt bend, distortion); graded index (density falls to edge, less distortion); single-mode focused near-horizontal beams. |
| Uplink / downlink | Ground→satellite / satellite→ground. |
| Omnidirectional vs unidirectional | Radio antennas need not align (multicast-friendly) vs microwave narrowly focused alignment (unicast). |
| IrDA | Infrared Data Association device standards: originally 75 kbps to 8 m; later 4 Mbps. |

### Concepts explained

**Physical layer.** Transmission media is the pathway that carries information from sender to receiver — also called a communication channel. Data travel as electrical signals (current) or electromagnetic signals (pulses at various frequencies) through copper, optical fiber, atmosphere, water, or vacuum. Media differ in bandwidth, delay, cost, and ease of installation/maintenance. The lecture locates media at the physical layer. Guided capacity depends critically on distance and on point-to-point vs multipoint. Three common guided media: twisted pair, coaxial cable, optical fiber.

**Design factors for data-transmission systems.** Key concern is data rate and distance — greater of both is better. Factors that set those limits:

| Factor | Teaching |
|--------|----------|
| Bandwidth | All else equal, greater signal bandwidth → higher data rate |
| Transmission impairment | Attenuation limits distance on guided media. Twisted pair generally suffers more than coax, which suffers more than optical fiber |
| Interference | Competing signals in overlapping bands can distort or wipe out a signal. Especially serious for unguided media; also a guided-media problem. Shielding of guided media minimizes it |
| Number of receivers | Guided media may be point-to-point or a shared link with multiple attachments. Each attachment adds attenuation and distortion, limiting distance and rate |

**Twisted pair.** Two copper conductors, each with plastic insulation. One wire carries the signal; the other is a ground reference. The receiver uses the difference between them. If the two wires were parallel, noise and crosstalk would not hit both equally, leaving a difference at the receiver. **Twisting** balances this: in one twist wire A is nearer the noise, in the next wire B is — so both are equally affected and the difference cancels unwanted signals. Twists per unit length affect quality. Types: UTP and STP.

**UTP** is the most common communications twisted pair. Once thought slower than other copper; the lecture says that is no longer true — UTP is the **fastest copper-based medium** here. Speed/throughput **10 to 1000 Mbps**; average cost per node very low; media and connector size very small; common connector **RJ-45**.

**STP** wraps each pair in metallic foil; four pairs then in an overall braid or foil. Typically **150 Ω**, specified for some Ethernet installs. Combines shielding, cancellation, and twisting. Reduces noise inside the cable and from outside. Often uses a dedicated STP data connector; can also use the same RJ connectors as UTP. Prevents interference better than UTP but is more expensive and harder to install. The shield **must be grounded at both ends**; improper grounding makes the shield an antenna. Because of cost and termination difficulty, STP is **rarely used in Ethernet**; it is primarily used in Europe. Speed/throughput **10 to 100 Mbps**; average cost moderately high; media/connector size medium to large.

**Applications of twisted pair:** many Ethernet networks; telephone systems; the workhorse medium inside buildings. Residential phones connect to the local exchange (end office) by twisted pair — **subscriber loops**. Advantages: easy to install, flexible, cheap, high speed capacity. Disadvantages: lower bandwidth than coax; less protection from interference.

**Coaxial cable.** Named because it has two conductors parallel to each other. Build-up: center copper conductor (solid or stranded); PVC insulation/sheath; outer conductor of metal foil (shield against noise and the return conductor); outer conductor in an insulating sheet; outermost plastic cover. Common standards: **50 Ω RG-8 or RG-11** (thick Ethernet); **50 Ω RG-58** (thin Ethernet); **75 Ω RG-59** (cable television); **93 Ω RG-62** (ARCNET). Connectors: **BNC** to attach cable end to a device; **BNC T** in Ethernet to branch to a computer; **BNC terminator** at the cable end to prevent reflection. Performance: attenuation is much higher than twisted pair — coax has much higher bandwidth, but the signal weakens rapidly and needs frequent repeaters. Applications: analog telephone (one coax network could carry **10,000 voice** signals); digital telephone (up to **600 Mbps**) — in phones, coax is largely replaced by fiber; cable TV; early Ethernet LANs.

| | Baseband | Broadband |
|---|----------|-----------|
| Typical cable | 50 Ω, digital, mostly LANs | Analog on standard CATV cabling |
| Signals | One signal at a time, very high speed | Several simultaneous signals on different frequencies |
| Reach | Needs amplification about every 1000 ft | Larger area than baseband |

Advantages listed: high bandwidth; long-distance telephone; digital at 10 Mbps; higher noise immunity; transmission without distortion; longer distance at higher speed than twisted pair because of better shielding. Disadvantages: single cable failure can take down the entire network; harder and more expensive to install than twisted pair; imperfect shield can cause a ground loop.

**Optical fiber.** Glass or plastic; signals as light. Light goes straight in a uniform substance; at a density change it bends. Relative to the **critical angle** (a property of the substance): incidence less than critical → ray refracts toward the surface; equal to critical → light bends along the interface; greater than critical → **total internal reflection**; ray turns back into the denser substance. Fibers guide light by reflection. Bandwidth taught: **more than 2 Gbps**.

| Mode | Structure | Behavior |
|------|-----------|----------|
| Multimode step-index | Core density constant center to edge | Beam goes straight until core/cladding; abrupt density drop bends the beam — “step” = suddenness, which distorts the signal |
| Multimode graded-index | Index of refraction highest at center, decreasing to the edge | Reduces distortion versus step-index |
| Single-mode | Step-index fiber plus a highly focused source | Beams limited to a small range of angles near the horizontal |

Connectors: **SC** (subscriber channel/connector) — cable TV; push-pull locking. **ST** (straight tip) — cable to network devices; bayonet lock; called more reliable than SC. **MT-RJ** — same size as RJ-45. Applications: backbone networks (wide bandwidth is cost-effective); hybrid fiber-coax cable-TV (fiber backbone, coax to the premises); LANs such as 100BASE-FX and 1000BASE-X. Advantages: high-quality, very high speed; immune to EMI so noise/distortion is very low; analog and digital. Disadvantages: expensive; difficult to install; expensive/difficult maintenance; do not allow complete routing of light signals.

**Unguided (wireless) media.** Carry electromagnetic waves without a physical conductor. Signals are broadcast in free space to anyone with a receiver. Propagation methods: **ground**, **sky**, and **line-of-sight**. The radio/microwave part of the spectrum is divided into **eight bands** (very low frequency through extremely high frequency), regulated by government authorities. **Antenna:** electrical conductor(s) that radiate or collect electromagnetic energy. **Satellite:** downlink = satellite → ground station(s); uplink = ground → satellite. Companies sell uplink, downlink, or both to TV stations, corporations, and carriers. Wireless transmission grouped into radio, microwave, and infrared. **Two frequencies** are used so they do not interfere and full duplex is possible; also, transmit power scales with frequency, so higher frequency means heavier equipment.

**Radio waves (3 kHz to 1 GHz).** Omnidirectional: sending and receiving antennas need not be aligned; any receiver antenna can pick up the waves. Disadvantage: interference from another antenna on the same frequency/band. Sky-mode radio can travel long distances — good for AM long-distance broadcasting. Low and medium frequencies penetrate walls: an AM radio works indoors (advantage) but you cannot isolate a communication to inside vs outside (disadvantage). The radio band is relatively narrow (just under 1 GHz) versus microwave. Applications (multicast, one sender many receivers): AM and FM radio, television, maritime radio, cordless phones, paging.

**Microwaves (about 1–300 GHz).** Unidirectional / narrowly focused: antennas must be aligned. Advantage: one aligned pair need not interfere with another. Characteristics: (1) line of sight — towers must see each other; far-apart towers must be tall; Earth’s curvature and obstacles block short towers; repeaters for long distance; (2) very high frequency microwaves cannot penetrate walls — a problem if receivers are indoors; (3) band is wide (~299 GHz) → wider subbands and high data rate; (4) some portions require permission from authorities. Applications (unicast): cellular phones, satellite networks, wireless LANs.

**Infrared (300 GHz to 400 THz).** Short range. Cannot penetrate walls — prevents interference between a system in one room and the next (TV remotes do not bother the neighbors) but is useless for long range. Cannot use outdoors because sunlight contains infrared that interferes. Applications: band ~400 THz has excellent potential for very high-rate digital transmission. **IrDA** standards for keyboards, mice, PCs, printers. Some PCs have an IrDA port for a wireless keyboard. Original standard: **75 kbps** up to **8 m**; later **4 Mbps**.

### How to answer
- Define media at physical layer; list four design factors.
- Compare UTP vs STP (speed, cost, grounding, Ethernet rarity of STP).
- Coax: structure, RG types, baseband/broadband, pros/cons vs pair and fiber replacement in telephony.
- Fiber: critical angle / TIR; three modes; connectors; EMI immunity; >2 Gbps.
- Wireless: radio omni multicast vs microwave LOS unicast vs infrared in-room IrDA; uplink/downlink.

---

## M23: Ethernet and Fast Ethernet

### In one line
Ethernet (IEEE 802.3) is the dominant wired LAN MAC using CSMA/CD; Fast Ethernet (802.3u) keeps the same frames and rules but cuts bit time from 100 ns to 10 ns and shortens cable length for 100 Mbps.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| IEEE 802.3 / 802.3u | Ethernet standardized 1983; Fast Ethernet approved June 1995 (succeeded in enterprise LANs). |
| 10BASE5 / 2 / T / F | 10 Mbps baseband: thick coax 500 m (vampire taps); thin coax 185 m / 30 nodes (BNC T); twisted-pair hub 100 m / 1024 nodes; fiber 2000 m / 1024 nodes. |
| Vampire tap | 10BASE5 connector: pin forced halfway into the coax core. |
| LLC / MAC | Logical Link Control: identify/pass data to network-layer protocol. MAC: shared-media access, hardware addresses, NIC↔physical. |
| CSMA/CD | Carrier Sense Multiple Access with Collision Detection: listen, send when idle, detect collision, jam, backoff. |
| Binary exponential backoff | After *i*th collision wait uniform in \(0 \ldots 2^i-1\) slots; freeze max 1023 after 10; give up after 16 and report failure to higher layers. |
| Slot time / 2T | Collision window ≈ round-trip; minimum frame **64 bytes** so sender is still transmitting when jam returns. |
| 100VG-AnyLAN | IEEE 802.12 demand-priority alternative to Fast Ethernet; did not catch on. |
| MII / PCS / PMA / PMD | Fast Ethernet MAC–PHY stack: media-independent interface; coding + autonegotiation; serialize/deserialize; medium-dependent signaling. |

### Concepts explained

**History.** Xerox experimental coax 1970s at **3 Mbps** with CSMA/CD; commercial **1980**; IEEE **802.3** in **1983**. Refined for higher rates/longer links; largely replaced Token Ring, Token Bus, FDDI, ARCNET. Most common LAN; topologies generally bus or bus-star. Name from cable “ether.” Naming: speed + BASE (baseband) + medium/length hint.

**Four 10 Mbps families.**

| Type | Medium | Reach / nodes | Notes |
|------|--------|---------------|-------|
| 10BASE5 | Thick coax, vampire taps | 500 m | Historically first |
| 10BASE2 | Thin coax, BNC T | 185 m, 30/segment | Cheaper/easier |
| 10BASE-T | TP to hub | 100 m, 1024 | Answer to single coax fault killing whole net |
| 10BASE-F | Fiber | 2000 m, 1024 | Noise immunity; harder to tap (security); buildings/distant hubs |

**Frame format (IEEE 802.3).**

| Field | Size | Role |
|-------|------|------|
| Preamble | 7 bytes | Sync / start of new frame |
| SFD | Last lead-in byte | Start-of-frame (repeating 10 pattern) |
| Dest / src MAC | 6 + 6 bytes | Addresses |
| Length | 2 bytes | Frame length |
| Data | 46–1500 bytes | Pad if shorter than 46 |
| CRC | 4 bytes | Error check |

**CSMA/CD operation.** Ready → sense; if busy, keep sensing; if free, transmit and watch; on collision send **jam** (48-bit noise burst) and backoff; else complete. States: contention, transmission, idle. Collision detected by comparing received power/pulse width with transmitted signal.

**Binary exponential backoff:** 1st → 0–1; 2nd → 0–3; *i*th → \(0 \ldots 2^i-1\); after 10 freeze at 1023; after 16 fail to higher layers. Same random pick → collide again.

**Why 64-byte minimum.** Propagation A→B = **T**. A starts at 0; B may start at \(T-\varepsilon\); B jams; A hears jam at ~**2T**. If frame finishes before jam returns, A wrongly thinks success. All frames must take **> 2T** to send → pad under 64 bytes to 64.

**Fast Ethernet.** Proposed 1992; **802.3u** June 1995 succeeded; **100VG-AnyLAN** (802.12 demand priority) did not. Reasons to keep sped-up Ethernet: backward compatibility; fear of new-protocol unknowns; finish before technology changed. Kept formats/interfaces/procedures; only bit time **100 ns → 10 ns**. More bits in same propagation delay → enlarge min frame **or** shorten cable; enlarging broke compatibility → **max cable ~100 m**. Frame format unchanged.

**PHY types.**

| PHY | Medium | Notes |
|-----|--------|-------|
| 100BASE-T4 | Cat 3 four-pair | 100 m, RJ-45 |
| 100BASE-TX | Cat 5 UTP or Type 1 STP | Full duplex 100 Mbps each way |
| 100BASE-FX | Two 62.5/125 µm multimode | Full duplex; station–hub to 2000 m; SC/MIC/ST |
| 100BASE-SX | Two multimode, short-λ | Cheaper than FX long-λ; to 550 m |
| 100BASE-BX | One single-mode + λ mux | 1310/1550 nm; 10/20/40 km |
| 100BASE-LX10 | Two single-mode | Nominal 10 km, 1310 nm |

**Layered PHY.** MII between MAC and any PHY (carrier present, collision absent) → Reconciliation maps to MAC primitives → **PCS** (uniform interface, carrier sense, collision detect, **autonegotiation** 10/100 and half/full) → **PMA** (serialize/deserialize code groups) → **PMD** (per-medium signaling).

#### Numbers / formulas
- Bit times: Ethernet **100 ns**; Fast Ethernet **10 ns**
- Min frame **64 bytes**; jam **48 bits**; backoff cap **1023** after 10; fail after **16**
- 10BASE reaches: 500 / 185 / 100 / 2000 m; Fast copper typical **100 m**

### How to answer
- Place Ethernet historically (Xerox 3 Mbps → 1980 commercial → 802.3 1983) and name four 10 Mbps cabling families with reach.
- Split LLC vs MAC; list 802.3 frame fields including 46–1500 data and CRC.
- Walk CSMA/CD + jam + binary exponential backoff + why pad to 64 bytes (2T collision window).
- Fast Ethernet = same rules, 10 ns bits, shortened cable for compatibility; 802.3u won over 100VG-AnyLAN.
- List copper/fiber PHYs and MII–PCS–PMA–PMD roles (autonegotiation in PCS).

---
