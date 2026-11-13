# Volume 01 — Foundations, Models, TCP/IP & Addressing (M00–M11)

> Information Security (CEC) · Exam-readable notes
> Full concept coverage rewritten for understanding and answer writing (not the ultra-short notes-3).

---

## M00: Introductory Video — Information Security

### In one line
A short course overview: why information security matters for individuals and enterprises, and what themes (DNS trust, HTTPS, client-side attacks, secure coding) the two-credit offering will cover.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Security loophole | An organizational gap that lets an attacker break in and then exploit a vulnerability. |
| Authoritative DNS reply | A name-server answer that should be trusted when judging whether a website is genuine — not visual appearance alone. |
| HTTPS digital signature | A cryptographic check that the web server is the claimed site when the connection uses HTTPS. |
| DNS poisoning | Tampering with name resolution so users are directed to a fake host instead of the real one. |
| Client-side attack | A compromise that succeeds because the user (browser) willingly approaches a malicious site. |
| Secure coding | Writing software so that vulnerabilities are not shipped; framed as the course’s ultimate goal. |

### Concepts explained
Information security is no longer a specialist niche. Organizational loopholes give criminals a breakthrough they can exploit against a single person or an enterprise. The course promises a big-picture tour of a secure web surface: recognizing fake websites via authoritative DNS replies, verifying HTTPS digital signatures, and a hands-on DNS-poisoning demonstration so students see how name resolution can be subverted.

The coordinator’s central claim: the main root cause of most information-security threats is poor programming. Copy-paste (“Ctrl+C / Ctrl+V”) coding across generations of software is called out as a habit to discourage. Secure coding is therefore the end-goal.

Client-side attacks get dedicated proof-of-concept attention because they are a critical attack vector. Securing one server is comparatively easy; if the client willingly visits a malicious site, the defender has almost no remaining control. Through PoCs, students should learn countermeasures and, more importantly, practice secure coding.

The offering is an eight-week, two-credit short-term course covering information and network security, operating-system and database security issues, DNS poisoning (including authoritative answers), and competencies against client-side attacks. Closing idea: information security keeps the hygiene of the connected world; the sooner it is understood, the better.

### How to answer
- State that security now spans both individuals and enterprises, not only specialists.
- Trust on the web is technical (authoritative DNS + HTTPS signatures), not visual “looks official.”
- Poor programming / copy-paste reuse is taught as the root cause of most threats.
- Client-side attacks are hard to stop once the user cooperates with the attacker.
- Name the course scope: network, OS, database, DNS, secure coding; eight weeks, two credits.

---

## M01: Information Security

### In one line
Social and ethical foundations of information security: ethics theories, CIA and system vs data security, hacking/crime distinctions, professional codes, and privacy / dataveillance / biometrics.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Ethics | Study of right/wrong and good/bad; analyzes behaviours, policies, laws, and social structures. |
| Consequentialism | Actions are wrong to the extent that they have bad consequences. |
| Deontology | People have moral duties that exist independently of good or bad consequences. |
| Computer ethics | 1980s field analyzing moral duties of computer professionals/users and ethical issues in IT public policy. |
| System security | Protecting hardware and software against malicious programs that sabotage system resources. |
| Information security | Protecting data that resides on disk or is transmitted between systems; defined via the CIA triad. |
| Confidentiality / Integrity / Availability | Conceal unauthorized disclosure; authorized entities change data only via authorized mechanisms; authorized entities can access when needed. |
| Safety-critical system | Real-time control system whose failure can threaten life (e.g. nuclear reactor, aircraft, medical treatment). |
| Hacking | Use of computer skills to gain unauthorized access; may be defined as malicious or (by self-identified hackers) non-malicious. |
| Cracking | Malicious and disruptive break-ins (hacker self-description contrasted with “hacking”). |
| Hacker ethic | Convictions that information should be free, computer access unlimited, and cyberspace cannot harm the real world. |
| Cyber trespass | Unauthorized access to computer systems or password-protected websites. |
| Cyber vandalism | Programs that disrupt network operations or corrupt data. |
| Cyber terrorism | Politically motivated hacking intended to cause grave harm — loss of life and/or severe economic loss. |
| Hacktivism | Political disruption of a site/server without intent to cause serious damage. |
| Information warfare | Using information and attacks on information systems as tools of war. |
| ISSA | Information Systems Security Association; code requires law plus “highest ethical principles” without specifying them. |
| Right to be let alone | Warren and Brandeis’s definition of privacy. |
| Informed consent | Inform people how personal data will be stored/used/exchanged and obtain consent. |
| Dataveillance | Large-scale computerized collection/processing of personal data to monitor actions and communications. |
| Biometrics | Identity verification from physiological or behavioral characteristics. |

### Concepts explained
**Ethics vs law.** Ethics distinguishes right from wrong and good from bad. Consequentialism judges actions by consequences; deontology holds duties independent of consequences. Ethical principles often inform legislation, but legislation cannot substitute for morality — individuals and corporations must weigh both legality and morality.

**Computer ethics** emerged in the 1980s. Sample questions: reading employees’ email, copying copyrighted software, online content without censorship. Analysis clarifies dilemmas, facts and values, balances rights/interests, and evaluates policies.

**Computer security** protects against unauthorized disclosure, manipulation, or deletion of information and against denial of service. Split: **system security** (hardware/software) vs **information/data security** (stored and transmitted data). Information security is customarily defined around **CIA**.

**Moral stakes of breaches.** Economic harm (hardware/software damage; data often worth more than hardware); personal/cultural/social value of data; psychological harm; injury/death in safety-critical systems (nuclear, aircraft/ATC, missiles, medical treatment) or indirectly (bridge design, medical diagnosis). Confidentiality breaches can violate property/IP rights, privacy rights, firm reputation, and trust in e-banking/e-commerce. Availability compromises can violate freedom of information and free speech (DoS, website hijacking).

**When security itself harms.** Over-protective measures can block legitimate access; discriminatory measures can wrongly exclude or privilege classes of users.

**Hacking and computer crime.** Hacking generally means unauthorized access. Self-identified hackers distinguish non-malicious hacking from cracking and justify activity via the hacker ethic. The lecture rejects “information should be free” as colliding with IP, privacy, and integrity. Major security-compromising crime types: cyber trespass and cyber vandalism.

**Cyber terrorism vs hacktivism vs information warfare.** Cyber terrorism = political motive + grave harm (life and/or severe economic loss); concern intensified after 9/11. Hacktivism disrupts without serious-damage intent (email bombs, low-grade viruses, temporary homepage hijackings). Information warfare extends ordinary war: propaganda, jamming/hijacking communications, hacking vital infrastructure (pipelines, power grids, rail).

**Professional responsibility.** Security professionals must assure correctness, reliability, availability, safety, and security — with life-or-death stakes in safety-critical systems. Codes (e.g. ISSA) are thin: they invoke “highest ethical principles” without specifying application. Codes are not enough; professionals need ethics training to recognize dilemmas and balance principles.

**Privacy.** Warren/Brandeis: right to be let alone; also control of access to private affairs. Valuable for protection from threats, autonomy, other rights, and democracy — but not absolute (balanced with public order/national security; lesser expectation at work/public). Informed consent is a key Western principle.

**IT and privacy.** Surveillance is systematic observation to exert influence (state and corporate). Computerization from the 1960s scaled surveillance; **dataveillance** monitors actions/communications via IT, CCTV, biometrics, data mining. 9/11 expanded state surveillance; corporations extend consumer surveillance. Privacy-in-public disputes cover video/IR/satellite/GPS/RFID/checkpoints/mobile tracking/audio/metadata. Biometrics raises anonymity loss, behavioural insight used against persons, and bodily-privacy concerns.

### How to answer
- Contrast consequentialism vs deontology; stress ethics ≠ law.
- Distinguish system security vs information security and state CIA.
- Link breaches to rights/harms (economic, cultural, psychological, life/death; FOI and free speech when availability fails).
- Note that over-strong or discriminatory security can itself violate rights.
- Reject hacker-ethic “information should be free”; define trespass vs vandalism.
- Cyber terrorism = political + grave harm; contrast hacktivism and information warfare.
- Codes (ISSA) insufficient — need ethics training.
- Privacy = let alone / control access; dataveillance and biometrics squeeze anonymity; consent and context matter.

---

## M02: Network Security

### In one line
Why e-business networks need security: CIA goals, threat vs attack, passive/active attacks, cryptography (symmetric, asymmetric, hashing), and boundary devices plus security policy.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Confidentiality | Protect stored and transmitted information from unauthorized disclosure. |
| Integrity | Authorized entities change data only through authorized mechanisms; faults (e.g. power surge) can also violate it. |
| Availability | Authorized entities can access information when needed. |
| Threat | Possible danger that might exploit a vulnerability — a potential security violation. |
| Attack | Deliberate assault by an intelligent threat that tries to evade services and violate policy. |
| Passive attack | Eavesdropping/monitoring transmissions to obtain information. |
| Traffic analysis | Inferring communication nature from patterns (who, how often, how long) even when contents are encrypted. |
| Snooping | Unauthorized access to or interception of data; stopped by making data meaningless via encryption. |
| Replay | Capture a data unit and retransmit it later to produce an unauthorized effect. |
| Modification of messages | Alter, delay, or reorder legitimate messages for an unauthorized effect. |
| Denial of service (DoS) | Prevent or inhibit normal use/management of communication facilities (target one host or overload a network). |
| Symmetric-key cryptography | Same shared secret key for encryption and decryption (traditional cipher). |
| Asymmetric-key cryptography | Related public/private key pair; computationally infeasible to derive decryption key from encryption key alone. |
| RSA | Example asymmetric algorithm where either related key may encrypt and the other decrypt. |
| Hash / compression function | Arbitrary-length message → fixed-length digest via iterated fixed-size steps (n-bit in, m-bit out, n > m). |
| MD5 | Rivest message digest: 512-bit blocks → 128-bit digest (128 bits too small to resist attack). |
| SHA / NIST | Secure Hash Algorithm family standardized by NIST. |
| ACL | Access control list on a border router used for static layer-3 filtering. |
| Ingress / egress filtering | Permit only properly destined traffic to enter / leave the network. |
| Smurf attack | Spoofed ICMP echo requests to broadcast addresses so many hosts flood responses at a victim. |
| Stateful firewall | Tracks connections in a state table; blocks traffic not in established/permitted connections; most common type. |
| Proxy firewall | Intermediary so internal and external hosts never talk directly; full-packet protocol compliance; most advanced, least common. |
| IDS | Intrusion detection system: detect and alert (signatures/anomaly); does not auto-block. |
| IPS | Intrusion prevention system: detect and automatically block/prevent. |
| Defense in depth | Layered technical controls plus policy and awareness. |

### Concepts explained
E-business (e-commerce, supply-chain, remote access) needs scalable mission-critical networks carrying voice, video, and data. More applications and users mean more vulnerability; network security protects transactions via cryptography and security devices.

**CIA.** Confidentiality covers storage and transit. Integrity requires authorized changes via authorized mechanisms (bank balance example; accidental corruption still counts). Availability: information must be usable when needed (a bank that cannot serve accounts fails availability).

**Threat vs attack.** Threat = potential danger exploiting a vulnerability. Attack = deliberate intelligent assault violating policy.

**Passive attacks:** (1) release of message contents; (2) traffic analysis despite encryption. **Active-style effects:** replay; modification (e.g. change “John Smith” to “Fred Brown” in an access grant); DoS (targeted or network-wide overload).

**CIA-linked attacks.** Confidentiality threatened by snooping and traffic analysis; integrity by modification and replay; availability by DoS. Encryption makes snooped data meaningless.

**Cryptography** (Greek: secret writing) today has three mechanisms: symmetric-key, asymmetric-key, hashing. Symmetric: plaintext → algorithm + shared key → ciphertext; reverse with same key. Asymmetric: plaintext, algorithm, public/private pair, ciphertext, decryption algorithm; RSA may use either key to encrypt. Hashing: iterated compression; MD2/MD4/MD5 by Rivest; MD5 = 512-bit blocks → 128-bit digest (too small); SHA family from NIST.

**Boundary devices.** Border router = last router before untrusted Internet; static L3 ACL filtering; first/last line of defense; ingress/egress filtering; often block ICMP (DoS/recon), source-routed packets, out-of-band SYN. Smurf/DDoS example (9 Feb 2000, Yahoo/CNN): spoofed ICMP echoes to broadcasts; ingress/egress would have blocked spoofed traffic.

**Firewalls** are choke-points with allow/deny rules; pick up where the border router leaves off. Types: static (router-style packet filter), stateful (state table; most common), proxy (intermediary; protocol-compliant; most advanced/least common).

**IDS** = security alarm: signatures and statistical/anomaly analysis; alert via email/paging/logging (e.s. unauthorized DNS zone transfer, Unicode web attacks, buffer overflows, virus propagation). **IPS** auto-detects and blocks — combines firewall + IDS behaviour without waiting for an admin.

**Policy.** Technical controls alone are not enough. Good security policy hallmarks: authority (who responsible), scope (who affected), expiration (when ends), specificity (what required), clarity (understandable). Defense in depth needs comprehensive, realistic policy plus awareness.

### Numbers / formulas
- MD5: 512-bit blocks → 128-bit digest (too small).
- Smurf DDoS dated example: 9 February 2000 (Yahoo, CNN).

### How to answer
- Define CIA with storage/transit, authorized change (incl. accidents), and usable access examples.
- Threat = potential; attack = deliberate intelligent assault.
- Passive = contents + traffic analysis; active effects = replay, modification, DoS; map each to CIA; snooping ↔ encryption.
- Cryptography = three mechanisms; contrast same-key vs public/private; MD5 vs SHA.
- Place border router ACLs → firewalls (static/stateful/proxy) → IDS alerts / IPS blocks; mention Smurf + ingress/egress.
- List policy hallmarks; say defense in depth includes humans/policy, not only rule bases.

---

## M03: Computer Network Reference Models

### In one line
What a computer network is, coverage types (PAN–WAN), the seven-layer OSI model with chained vs end-to-end layers, and the four-layer TCP/IP model contrasted with OSI.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Computer network | Collection of autonomous computers interconnected by a single technology so they can exchange information. |
| Distributed system | Independent computers that appear to users as one coherent system, often via middleware (e.g. WWW looks like documents). |
| Middleware | Software above the OS that implements the distributed-system illusion. |
| PAN | Personal Area Network — IT devices within about 10 m; Bluetooth uses short-range radio ≈ 10 m. |
| LAN | Local Area Network — privately owned, single building/campus up to a few km; bounded worst-case delay. |
| MAN | Metropolitan Area Network — can cover a city (cable TV; WiMAX wireless MAN; head-end distribution). |
| WAN | Wide Area Network — large geography; customer hosts plus telco/ISP communication subnet (lines + switching elements). |
| Subnet | WAN transmission lines + switching elements/routers that carry messages host-to-host. |
| OSI | Open Systems Interconnection — ISO seven-layer model for systems open for interconnection. |
| Chained layers | Physical, data link, network — hop-by-hop; present on intermediate devices. |
| End-to-end layers | Transport through application — protocols only on end computers. |
| PDU names | Bit → frame → packet → TPDU → SPDU → PPDU → APDU. |
| MAC | Medium Access Control sublayer: shared-channel access on broadcast networks. |
| ARPANET | DoD-sponsored 1960s research network; grandfather of the Internet. |
| TCP vs UDP | Reliable connection-oriented vs unreliable connectionless transport. |

### Concepts explained
**Network vs distributed system.** A network interconnects autonomous computers via copper, fiber, microwave, IR, or satellite. A distributed system makes independent computers look like one system (WWW via middleware).

**Coverage taxonomy.**
- **PAN (~10 m):** keyboard/mouse/printer links; Bluetooth.
- **LAN:** share resources; **bus** — at most one master transmits; IEEE 802.3 Ethernet = bus broadcast, decentralized, 10 Mbps–10 Gbps; **ring** — capture token then transmit; IEEE 802.5 Token Ring at 4 and 16 Mbps; FDDI also ring.
- **MAN:** city coverage; cable TV; WiMAX; head-end feeds TV/Internet to homes.
- **WAN:** hosts run user programs; subnet = lines (copper/fiber/radio) + switching elements connecting ≥3 lines; typically each host on a LAN with a router; lines+routers = subnet.

**Two architectures.** OSI protocols rarely used now but the model remains valid; TCP/IP protocols are widely used.

**OSI design principles (five):** create a layer where a different abstraction is needed; each layer a well-defined function; choose functions for international standards; minimize information across interfaces; enough layers that distinct functions are not forced together.

**Seven layers (top→bottom):** application, presentation, session, transport, network, data link, physical. Transmitter: user data down to physical onto the medium; receiver: physical up to application.

**Chained vs end-to-end.** Lower three = chained (hop neighbors, also on intermediate devices). Upper four = end-to-end (only on end hosts).

**Layer functions.**
- **Physical:** raw bits; voltage, timing, modulation; mechanical/electrical/bit-timing/medium.
- **Data link:** frames; ACK if reliable; flow control so fast sender does not drown slow receiver; MAC for shared channels.
- **Network:** subnet operation; routing; congestion control; addressing; QoS.
- **Transport:** accept data, split if needed, ensure correct arrival; service type to session/users; true end-to-end.
- **Session:** establish sessions; dialog control; token management (no simultaneous critical ops); synchronization.
- **Presentation:** syntax/semantics; encoding/decoding.
- **Application:** user interface; HTTP (WWW), file transfer, email, network news.

**TCP/IP.** Origin ARPANET / DoD. Goals: connect multiple networks seamlessly; keep connections intact while endpoints function; flexible architecture. Named for TCP and IP.

| TCP/IP layer | Correspondence |
|--------------|----------------|
| Host-to-network | OSI data link + physical |
| Internet | OSI network |
| Transport | OSI session + transport |
| Application | OSI application + presentation |

Early protocols: IP (routing, addressing, congestion); TCP (reliable, connection-oriented) and UDP (unreliable, connectionless) for end-to-end connectivity and flow control; applications Telnet, FTP, SMTP, later DNS, NNTP, HTTP.

**OSI vs TCP/IP.** Both: independent protocol stacks; roughly similar layer roles; end-to-end transport service; layers above transport application-oriented. Differences: 7 vs 4 layers; OSI clearly separates service/interface/protocol (TCP/IP originally did not); OSI network = both connection modes, transport only connection-oriented; TCP/IP network only connectionless, transport both (user choice of TCP or UDP).

### Numbers / formulas
- PAN ≈ 10 m; Ethernet 10 Mbps–10 Gbps; Token Ring 4 and 16 Mbps.
- PDU path: bit → frame → packet → TPDU → SPDU → PPDU → APDU.

### How to answer
- Define network vs distributed system (middleware / WWW).
- Classify PAN/LAN/MAN/WAN with technologies (Bluetooth, Ethernet/Token Ring/FDDI, cable/WiMAX, hosts+subnet).
- State five OSI principles; list seven layers and PDU names; chained (3) vs end-to-end (4).
- One function bullet per OSI layer (bits; frames/ACK/flow/MAC; routing/congestion/addressing/QoS; end-to-end TPDUs; session dialog/tokens/sync; syntax; user protocols).
- TCP/IP: ARPANET goals, four layers, TCP vs UDP, key apps.
- Contrast OSI vs TCP/IP on layer count, service/protocol clarity, connection modes.

---

## M04: Computer Network Reference Models — TCP/IP Layers Continuation

### In one line
Deep dive into the Internet protocol suite: history (DARPA, Kahn, Cerf, NCP), four/five-layer mapping, and named protocols at link, internet, transport, and application layers.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Internet protocol suite / TCP/IP | Model and communication protocols of the Internet; named for TCP and IP as first defined protocols. |
| DoD model | Alternate name because ARPANET was DoD-sponsored. |
| IETF | Internet Engineering Task Force — maintains TCP/IP and related models. |
| DARPA | Defense Advanced Research Projects Agency whose late-1960s R&D produced the suite. |
| NCP | ARPANET Network Control Program; Cerf was its developer. |
| Five-layer hybrid | Four TCP/IP layers plus an explicit physical layer 1. |
| MAC / LLC | Shared-medium access (fairness, collision discovery/avoidance) vs flow control, link management, error handling, packet sizing. |
| ATM | Asynchronous Transfer Mode — connection-oriented; fixed-size cells; mixes real-time audio/video with regular data. |
| ARP (RFC 826) | Maps IP address → MAC address on a local network (IPv4). |
| NDP | Neighbor Discovery Protocol — similar exploration for IPv6. |
| LLTD | Microsoft proprietary Link Layer Topology Discovery for topology/QoS exploration. |
| PPP | Point-to-Point Protocol — ISP dial-up over a telephone line between two nodes. |
| IP | Unreliable, packet-oriented end-to-end transmission; fragmentation/defragmentation; IPv4 and IPv6. |
| ICMP | Internet Control Message Protocol — errors and diagnostics (echo) sitting on IP. |
| IPsec / IKE | Authenticate/encrypt IP datagrams; Internet Key Exchange for keys. |
| IGMP | Administers IP multicast groups. |
| OSPF | Open Shortest Path First — link-state routing inside one AS; called most widely used Internet routing protocol here. |
| Socket | IP address + port = unique connection endpoint. |
| RFC 793 / RFC 768 | TCP / UDP standards. |
| DCCP / RSVP / SCTP | Congestion-aware datagrams; resource reservation; scalable reliable stream transport. |
| TLS / SSL | Encrypt TCP segments; negotiate parameters, keys, auth, encryption, signatures (TLS succeeds SSL). |

### Concepts explained
**History.** ARPANET 1969; DARPA then other data technologies from 1972. Robert Kahn (satellite and radio packet nets) and Vinton Cerf (NCP) in spring 1973 designed open interconnection. Summer 1973 reformulation: hide network differences behind a common internetwork protocol; move reliability from the network to the **host**. Growth from four computers to hundreds overloaded translation between dissimilar nets.

**Four layers (bottom→top):** link/host-to-network → internet → transport → application. With physical as layer 1 → five-layer hybrid. OSI was planned theoretically first; TCP/IP was derived from practice and now dominates; ISO OSI protocols are unused.

| TCP/IP layer | OSI map | Responsibility |
|--------------|---------|----------------|
| Link / host-to-network | Physical + data link | Secure bit/packet transmission between adjacent systems |
| Internet | Network | End systems across heterogeneous networks |
| Transport | Transport | Reliable connection-oriented exchange between user programs |
| Application | Session + presentation + application | Interface for applications |

**Chained vs end-to-end in TCP/IP.** Link + internet = chained; transport + application = end-to-end (process-to-process).

**Link layer.** Local network without intervening routers. MAC: fair access, collision discovery/avoidance. LLC: flow control, link management, recognize/correct errors, size-limited packets. Protocols: IEEE 802.3 Ethernet, 802.5 Token Ring, 802.11 WLAN; ATM cells; ARP (IPv4 IP→MAC); NDP (IPv6); Microsoft LLTD; PPP dial-up.

**Internet layer — IP’s three functions:** (1) hierarchical host addressing/identification; (2) packet routing hop-by-hop toward destination; (3) congestion control. Protocols: IP (unreliable datagrams, fragmentation, v4/v6); ICMP (errors, echo diagnostics; sits on IP); IPsec + IKE; IGMP multicast; OSPF link-state inside one AS.

**Transport.** Process-to-process channel independent of user-data structure; virtual end-to-end connection; **ports** identify applications; port + IP = socket. Connection-oriented = TCP (RFC 793: reliable, bidirectional, virtual connections). Connectionless = UDP (RFC 768: datagrams; loss, duplication, reordering possible; false datagrams discarded; less complex → higher throughput, less reliability). Also DCCP (message-oriented, overload notifications, congestion control, parameter negotiation); RSVP (reserve resources; not for data transport; similar role flavour to ICMP/IGMP); TLS/SSL (encrypt TCP segments); SCTP (scalable reliable stream alternative to TCP).

**Application (OSI 5–7 interface).**

| Protocol | RFC (as taught) | Role |
|----------|-----------------|------|
| Telnet | RFC 854 | Bidirectional remote CLI |
| FTP | RFC 959 | Client–server file transfer/manipulation |
| SMTP | RFC 821 | Electronic mail |
| HTTP | RFC 2616 | WWW over reliable TCP |
| RPC | RFC 1057 / 5531 | Call external subroutine in another address space |
| DNS | — | Readable names ↔ IP addresses |
| SNMP | RFC 3411 | Monitor/administer/control network systems |
| RTP | RFC 1889 | Real-time audio/video |

### How to answer
- Trace DARPA → ARPANET → Kahn/Cerf: common internet protocol + host responsibility for reliability (replacing NCP).
- Draw four (or five hybrid) layers; chained vs end-to-end; practice-first vs OSI theory-first.
- Link: MAC/LLC; name IEEE 802 family, ATM, ARP vs NDP, LLTD, PPP.
- Internet: IP’s three functions; IP/ICMP/IPsec+IKE/IGMP/OSPF.
- Transport: sockets/ports; TCP RFC 793 vs UDP RFC 768; also DCCP, RSVP, TLS/SSL, SCTP.
- Application table with RFCs: Telnet, FTP, SMTP, HTTP, RPC, DNS, SNMP, RTP.

---

## M05: Protocol Stack

### In one line
Suite vs stack, OSI layering principles and encapsulation, detailed services of each of seven OSI layers, and TCP/IP layers with merits/demerits.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Protocol suite | Definition/specification of the protocols. |
| Protocol stack | Software implementation of the suite; hierarchy of layers each supporting the one above. |
| ISO 7498 | Identifier of the OSI model standard. |
| Baud / symbol rate | Symbol (or pulse) changes per second on the medium. |
| Modem | Device that both modulates and demodulates. |
| Line encoding | Pattern of voltage/current/photons representing bits (unipolar, polar, bipolar, Manchester). |
| Simplex / half duplex / full duplex | One-way only; either direction but not both at once; both directions at once. |
| Frame | Data-link PDU: link-layer header followed by a packet; trailer typically only at layer 2. |
| ARQ | Automatic repeat request — retransmit specified frames when errors are detected. |
| IEEE 802.2 LLC | Common LAN logical-link protocol. |
| CSMA/CD vs token passing | Ethernet MAC vs Token Ring MAC. |
| Slow start | Congestion avoidance that keeps bandwidth low at the start of a transmission or after retransmission. |
| UDP-Lite | Lightweight UDP variant; still connectionless with no inherent congestion control. |
| Session beans | Session-scoped objects deleted when the web session disconnects. |
| Network virtual terminal | Emulated terminal so a remote host accepts a logon as if from a local terminal. |
| www.yahoo.com → 204.71.177.71 | DNS name-to-address example given in the lecture. |

### Concepts explained
**Suite vs stack.** Suite = definition; stack = software implementation. Layers modularize design: each module talks mainly to two neighbors; lowest deals with physical hardware; higher layers add features; apps use top layers. Practical split: media / transport / applications, with OS interfaces between media↔transport (e.g. TCP/IP ↔ Ethernet) and transport↔applications (e.g. browser ↔ TCP/IP).

**OSI.** Conceptual model for interoperability without regard to internal technology; seven abstraction layers; ISO 7498. **Five principles:** different abstraction → new layer; well-defined function; internationally standardizable; minimize interface traffic; enough layers without unwieldy architecture (also “small enough”).

**Encapsulation.** Data units D7…D1; descending from application, each layer may add a header; trailer commonly only at layer 2; physical layer turns bits into electromagnetic signals. At destination, unwrap upward removing corresponding headers/trailers.

**Physical (L1).** Carry bitstream: mechanical/electrical specs, connectors/cables (max length), signal level/impedance, radio (spectrum, allocation, strength, bandwidth), IR fiber/wireless. Baud/symbol rate; modulation (carrier varied by modulating signal); modem = modulate + demodulate; line codes; bit synchronization (same rate, clocks synced); line config point-to-point vs multipoint; topology; transmission mode simplex/half/full duplex.

**Data link (L2).** Adjacent nodes / same LAN segment; framing; physical addressing (remote nets use next-hop device address); flow control; error control via ARQ; LLC (establish/control logical links; IEEE 802.2; hides DLL details); MAC (CSMA/CD for Ethernet; token passing for Token Ring).

**Network (L3).** Packet forwarding/routing; QoS; logical addressing (IP); datagram encapsulation; fragmentation/reassembly; error/diagnostics. Protocols: ICMP, IGMP, IPsec, IPv4, IPv6.

**Transport.** Host-to-host; transport PDU carried intact by network nodes. Services: connection-oriented stream, reliability, flow control, multiplexing. Same-order delivery via segment numbering; reliability via checksum + ACK/NACK + ARQ; flow control against buffer overrun/underrun; congestion avoidance (slow start) because ARQ alone can keep a network congested; ports multiplex endpoints (session layer in OSI, transport in TCP/IP). **TCP:** connection-oriented until apps finish; segments packets; flow control; retransmit dropped/garbled; ACK all arrivals. **UDP:** best-effort datagrams; no delivery/duplication guarantees; low overhead; no end-to-end connection; no inherent congestion control — apps must not blast at line rate. UDP-Lite similar.

**Session.** Open/close/manage semi-permanent dialogue; often with RPC. Services: authentication, authorization, session restoration; checkpointing/recovery; combine/synchronize streams. Examples: session beans; web conferencing lip-sync; live TV seamless audio/video merge.

**Presentation.** Syntax/semantics translator; translation between encodings; encryption/decryption; compression (especially multimedia).

**Application.** User/software network access: mail forwarding/storage; network virtual terminal (remote logon); directory services; file transfer/access/management (FTAM).

**TCP/IP in this lecture.** Packet-switched connectionless internetwork. Host-to-network underspecified except host must send IP packets somehow. Internet: inject packets that travel independently; IP format; routing. Transport: peer conversations; full or half duplex; apps choose TCP or UDP over IP. Application originals: Telnet (remote apps over TCP), FTP (share files across architectures), SMTP (mail via relays), DNS (name ↔ number; Yahoo example).

**Merits of TCP/IP:** operates independently; scalable; client–server; supports many routing protocols; can connect two computers. **Demerits:** transport does not guarantee delivery; model not reusable in other applications; replacing protocols not easy; services/interfaces/protocols not clearly separated.

### How to answer
- Suite = definition; stack = implementation; media/transport/app OS interfaces.
- State ISO 7498 principles; describe encapsulation (headers + L2 trailer → EM signal → unwrap).
- Bullet key services per OSI layer with named mechanisms (baud, line codes, CSMA/CD, IP suite, TCP/UDP, session beans, translation/encrypt/compress, virtual terminal).
- TCP/IP four layers + Telnet/FTP/SMTP/DNS (Yahoo IP example).
- List the five merits and four demerits exactly as taught.

---

## M06: Transmission Control Protocol

### In one line
TCP as reliable ordered byte-stream transport: history, sockets/ports, 20-byte header fields, three-way handshake and release, and variable sliding-window flow control (including zero-window probe).

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Transmission control program (1974) | Cerf–Kahn component later split into TCP (connection-oriented) + IP (internet layer). |
| RFC 793 / 1122 / 1323 | TCP definition; clarifications/bug fixes; extensions. |
| Segment | TCP unit of transmission; IP encapsulates it for delivery. |
| TPDU | Transport protocol data unit nested in packets then frames. |
| Socket / TSAP | IP address + 16-bit port; port is TCP’s transport service access point. |
| Well-known ports | Numbers below 1024 reserved for standard services; IANA assigns. |
| Byte stream | Message boundaries not preserved; application writes may coalesce or split. |
| ACK number | Next byte expected — not the last byte correctly received. |
| Sliding window | Variable-size; WIN says how many bytes may be sent starting at the acknowledged byte. |
| Pseudo-header | Included in the TCP checksum along with header and data. |
| Three-way handshake | SYN; SYN+ACK; ACK (seq X/Y, ACK X+1/Y+1). |
| Two-army problem | Connection-release uncertainty; solved with timers of about two maximum packet lifetimes. |
| Zero window | Sender stops except urgent data or a 1-byte window probe that prevents deadlock. |

### Concepts explained
**Foundation.** May 1974 IEEE paper by Cerf and Kahn: packet-switching internetworking; transmission control program later modularized into TCP + IP → Internet protocol suite.

**Reliable stream delivery.** Guarantees bytes identical and in order. Receiver ACKs; sender records each packet and runs a timer; retransmits on timeout if lost/corrupted. IP delivers; TCP tracks segments, reassembles, orders, and checks errors. Nesting: TPDU ⊂ packet ⊂ frame.

**Sockets and ports.** Service via sockets (IP + 16-bit port/TSAP). Multiple connections may share a socket; connections identified by both-end socket IDs (no VC numbers). Ports < 1024 = well-known (IANA).

### Numbers / formulas
| Port | Service |
|------|---------|
| 20 | FTP data |
| 23 | Telnet |
| 25 / 587 | SMTP / message submission |
| 53 | DNS |
| 69 | TFTP |
| 80 | HTTP |
| 109 / 110 / 995 | POP2 / POP3 |
| 143 / 220 | IMAP |
| 119 | NNTP |
| 500 | ISAKMP |
| 530 | RPC |
| 554 | RTSP |
| 107 | Remote Telnet |
| 115 | Simple File Transfer |
| 698 | OLSR (UDP) |
| 953 | DNS RNDC |

- Fixed header **20 bytes**; max data with 20-byte IP: **65535 − 20 − 20 = 65495**; data-less segments legal (ACKs/control).
- Port + IP = **48-bit** unique endpoint; seq/ack fields **32 bits** (every byte numbered).

**Service properties.** Full duplex (both directions at once); point-to-point (exactly two endpoints; no multicast/broadcast). Byte stream, not message stream — four 512-byte writes may arrive as four 512s, two 1024s, one 2048, etc.

**Header fields.** Source/destination ports; sequence and acknowledgement (next expected); data offset in 32-bit words (variable options); unused 6 bits; six flags:

| Flag | Meaning |
|------|---------|
| URG | Urgent pointer in use (byte offset from current seq to urgent data) |
| ACK | Acknowledgement number valid (else ignored) |
| PSH | Deliver to application on arrival; do not wait for full buffer |
| RST | Reset confused connection (e.g. host crash) |
| SYN | Establish: request SYN=1 ACK=0; reply SYN=1 ACK=1 |
| FIN | Release; sender has no more data |

Window size for variable sliding-window flow control; checksum over header + data + pseudo-header; urgent pointer; options.

**Socket primitives.** Server: socket → bind → listen (queue space) → accept (block). Client: socket → connect (block; bind optional). Then send/receive. Close is symmetric: both sides close → released.

**Three-way handshake.** Server passive (listen/accept); client connect sends SYN ACK=0. If no listener → RST. If accepted: Host2 gets SYN seq=X → returns SYN seq=Y ACK=X+1 → Host1 data seq=X+1 ACK=Y+1. Simultaneous open between same sockets can collide.

**Release.** Either side FIN; after ACK that direction shut for new data; other direction may continue; both shut → released. Normally four segments (FIN+ACK each way); first ACK and second FIN can share a segment → three. Timers (~2× max packet lifetime) avoid two-army problem if FIN response never arrives.

**Window example (4096-byte buffer).** Send 2048 seq=0 → ACK=2048 WIN=2048 → send 2048 seq=2048 → ACK=4096 WIN=0 (stop). Exceptions at WIN=0: urgent data; one-byte probe so receiver re-announces window (prevents deadlock if window update lost). After app reads 2K → ACK=4096 WIN=2048; continue.

### How to answer
- Cerf–Kahn 1974 → TCP+IP; RFC 793/1122/1323; reliable ordered byte stream with ACK+timer+retransmit.
- Socket = IP+port; well-known ports <1024; list key ports; full duplex, point-to-point, not message stream.
- Walk 20-byte header: ports, seq/ack (next expected), offset, six flags, window, checksum+pseudo-header.
- Server socket/bind/listen/accept vs client connect; three-way handshake numbers; RST if no listen.
- Teardown FIN both ways (3 or 4 segments) + two-army timers.
- Sliding window independent of DLL-style ACK coupling; worked 4K example; WIN=0 exceptions (urgent + 1-byte probe).

---

## M07: Data Link Layer

### In one line
OSI Layer 2: LLC/MAC split, framing methods, stop-and-wait vs sliding-window flow control (U = 1/(1+2a)), and ARQ variants (stop-and-wait, Go-Back-N, selective repeat).

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| DLL / Layer 2 | OSI layer above physical; hides hardware particulars; presents a channel to upper layers. |
| Collision domain | Shared-link setting where several hosts compete; makes DLL work harder. |
| LLC | Logical Link Control — for point-to-point links: protocols, flow control, error control. |
| MAC | Media Access Control — decides which user uses the broadcast medium at a given time. |
| NIC | Network interface card/adapter (e.g. Ethernet) implementing DLL in hardware. |
| Segmentation / encapsulation | Split network-layer stream into blocks; add header and frame flags. |
| Byte stuffing | Insert ESC before accidental flag bytes in the data. |
| Bit stuffing | After five consecutive 1s in data, insert a 0; flag pattern is 01111110. |
| Manchester / coding violation | 1→10, 0→01; illegal physical codes delimit IEEE 802 frames. |
| Stop-and-wait | Send one data frame, wait for ACK; inefficient if propagation >> transmission. |
| a | Propagation time / transmission time. |
| Sliding window | Numbered frames; window up to 2^K−1; used by TCP (kernel buffer). |
| ARQ | Automatic repeat request after error detection. |
| Stop-and-wait ARQ | ACK/NAK + timer; duplicates discarded by sequence; small buffers, poor on long delay. |
| Go-Back-N | Continuous send; on NAK/timeout resend that frame and all successive; max window 2^K−1. |
| Selective repeat | Retransmit only lost/NAK frames; receiver stores and resequences. |
| RR | Receive Ready piggyback ACK (e.g. RR1). |

### Concepts explained
DLL works between hosts connected directly (broadcast or point-to-point). On broadcast, systems share a link; multi-host collision domains are hardest. DLL converts streams to bit signals outbound and rebuilds frames inbound. Implemented in hardware/software, CPU or NIC.

**Functions:** framing (packets → frames); unique manufacturing-time hardware addressing; error detection/recovery; flow control for speed mismatches; multi-access (e.g. CSMA/CD).

**Frame header fields:** address (sender/receiver), error-detecting checksum, control (protocol functions). Receiver must find start/end via frame flags with little bandwidth waste.

**Four framing methods:**
1. **Byte count** — header field states byte length.
2. **Flag bytes + byte stuffing** — same flag delimiter start/end; ESC before accidental flags in data.
3. **Flag bits + bit stuffing** — flag **01111110**; after five 1s in data insert 0; receiver deletes that 0.
4. **Physical coding violations** — Manchester (1=10, 0=01); illegal codes as delimiters (IEEE 802).

**Why flow control.** Fast Pentium drowning slow 80386; Ethernet hosts linked by 28.8 kbps modem — sender must not overburden receiver memory/CPU. Flow control tells the sender how much data it may transfer before waiting for an acknowledgement; the receiver must report before its limits (buffer memory or processing power) are reached.

**Stop-and-wait.** Request-reply; only one frame in transit; major drawback when propagation delay > transmission delay. Needs two-way (half or full duplex) so ACKs return; a small processing delay sits between last data bit and ACK generation. With transmission time = 1 and propagation = a: if a < 1 first bit arrives before send finishes; if a > 1 sender finishes before leading bits arrive. **Utilization U = 1/(1+2a)** — good on LANs (small a), poor on satellite. On fast LANs the idle gap is minor; WAN/multi-hop paths spend most time idle.

**Sliding window.** Stop-and-wait fails when one message is many frames and a > 1. Efficiency rises if multiple frames fly on a full-duplex line. K-bit sequence field → numbers 0…2^K−1; max sender (and initially stated receiver) window **2^K−1**; sender buffers equal to window size. ACK carries next expected number and can ACK multiple frames / announce readiness for the next n frames. TCP places a kernel buffer between app and network; as the app reads, space frees for more network data. Later description: receiver window size one if order required (out-of-order discarded and resent); window grows by one on correct receipt. Ideal steady state: data forward + window announcements reverse constantly in flight.

**Error control — three ARQ schemes.**
- **Stop-and-wait ARQ:** wait for ACK/NAK; timer on loss (retransmit old frame; receiver discards duplicates by sequence label); NAK on noise corruption before timeout; simple, minimum buffers, inefficient on long delay.
- **Go-Back-N:** continuous ARQ (send without waiting); NAK or timeout → resend that frame **and all successive**; also resends if ACK lost; piggybacked RR on full duplex; for K-bit seq, max window **2^K−1** so cumulative RR is unambiguous (e.g. 3-bit → window 7 — otherwise another RR1 after eight frames could mean cumulative OK or total damage); higher throughput, more complex.
- **Selective-repeat:** retransmit only lost/NAK/timed-out frames; most efficient; sender more complex (out-of-order sends); receiver needs storage and processing to reinsert frames in sequence.

### Numbers / formulas
- Flag bit pattern: **01111110**.
- **U = 1/(1+2a)** with **a = T_prop / T_trans**.
- Sequence field K bits → window max **2^K − 1**.
- Example speeds motivating flow control: 200 MHz Pentium vs 25 MHz 80386; 28.8 kbps modem between Ethernets.

### How to answer
- Place DLL above physical; LLC vs MAC; NIC implementation; list five functions.
- Describe four framing methods with stuffing rules and Manchester violations.
- Contrast stop-and-wait vs sliding window; write U = 1/(1+2a) and when it is poor.
- Explain ARQ trio: stop-and-wait (simple/inefficient), Go-Back-N (rewind + window 2^K−1), selective repeat (only lost frames + reorder).

---

## M08: Medium Access Control Protocols

### In one line
MAC sublayer for shared media: static FDM vs dynamic allocation, random access (ALOHA, CSMA, CSMA/CD) vs controlled access, with throughput formulas and Ethernet collision procedure.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| MAC sublayer | Bottom of the data-link layer; IEEE media access, error detection, station addressing; serves LLC, uses physical layer. |
| Multiple access | Many stations share one broadcast medium. |
| FDM | Frequency-division multiplexing — static split of bandwidth into fixed partitions. |
| Collision | Overlapping transmissions that garble the signal. |
| Carrier sensing | Electrical sense that the channel is busy or free. |
| ALOHA | Random-access protocol from University of Hawaii (early 1970s), originally packet radio. |
| Vulnerable period | Time window in which another packet can overlap and destroy a transmission. |
| G, S | Offered load per packet time; successful throughput per slot. |
| CSMA | Carrier Sense Multiple Access — sense before transmit. |
| Nonpersistent CSMA | If busy, wait random time without sensing, then retry sense cycle. |
| 1-persistent CSMA | Keep sensing until idle, then send with probability 1 (Ethernet CSMA/CD). |
| p-persistent CSMA | After idle, send with probability p (CSMA/CA / Wi-Fi). |
| CSMA/CD | CSMA plus collision detection, jam signal, and backoff (early Ethernet). |
| 10BASE5 / 10BASE2 / 10BROAD36 / 1BASE5 | Cabling options named by Mbps, baseband/broadband, segment length × 100 m. |

### Concepts explained
When many stations share one medium, simultaneous transmissions garble messages. MAC provides fair access and collision avoidance; also frame delimiting, address recognition, error checking. Tied to LAN topology.

**Static vs dynamic allocation.** Static FDM: n equal bands for n users — fine for few constant users; with varying traffic, unused bands waste spectrum or leave extra users without a channel; n queued users → average delay n× mean. Dynamic allocation (LANs/WANs) adapts to traffic. Assumptions: independent stations, constant work rate, single shared channel, start anytime or in slots, collisions detectable and retransmittable, carrier sensing optional.

**Protocol families (asynchronous TDM).**
| Family | Examples |
|--------|----------|
| Random / contention | ALOHA, CSMA, CSMA/CD; register insertion (obsolete) |
| Controlled / deterministic | Centralized polling; distributed token passing, slotted ring |

Wired multi-drop: host polls inbound. Radio: two bands. Satellite: uplink channels, downlink return.

**Pure ALOHA.** Send whenever ready; depend on ACK; timeout = max RTT = **2 × T_P**; random backoff T_B (same timeout for all would re-collide). Even first-bit vs last-bit overlap destroys both frames. Pure ALOHA does not listen before transmit. Vulnerable period = **two packet times**. Throughput S = average successful traffic per unit time (slot = one equal-size frame); max S is 1 but collisions waste channel. Poisson load G: probability of no collision in the vulnerable window gives **S = G e^{−2G}**; max at **G = 0.5**; ~**18%** utilization. Pros: no sync. Cons: inefficient.

**Slotted ALOHA.** Discrete slots = packet time; transmit only at slot starts; sync required; equal frames; collision detectable before slot ends. Vulnerable period halved to one packet time. **S = G e^{−G}**; max at **G = 1**; ~**36.8%** utilization (twice Pure ALOHA).

**CSMA.** Sense carrier; if busy wait until free (“listen before talk”). Vulnerable time = propagation T_P (e.g. A starts at T1; reaches far end D at T1+T_P). Variants: **nonpersistent** (if busy, random wait without sensing, then retry whole cycle — fewer collisions, better throughput); **1-persistent** (sense until idle, send with p=1 — Ethernet CSMA/CD); **p-persistent** (after idle send with p, else wait next slot — Wi-Fi CSMA/CA).

**CSMA/CD.** While transmitting, detect other signals; abort; jam until minimum packet time so all hear collision; increment retry counter; abort if max attempts; else random backoff based on collision count and re-enter main sense loop. Cutting transmission short saves time/bandwidth. Taught as more efficient than ALOHA, slotted ALOHA, and plain CSMA. Best on bus/multipoint with bursty asynchronous traffic; all stations share one path via transceiver; fully decentralized contention; supports baseband and broadband. Naming: leading number = Mbps; middle = BASE/BROAD; trailing = segment length × 100 m (10BASE5, 10BASE2, 10BROAD36, 1BASE5). Manchester at baseband; broadband uses PSK of the Manchester-encoded signal.

### Numbers / formulas
- Pure ALOHA: **S = G e^{−2G}**, max ≈ **18%** at **G = 0.5**; vulnerable = 2 packet times; timeout **2 T_P**.
- Slotted ALOHA: **S = G e^{−G}**, max ≈ **36.8%** at **G = 1**.
- CSMA vulnerable time = **T_P**.

### How to answer
- MAC under LLC; functions; static FDM waste vs dynamic assumptions.
- Random (ALOHA/CSMA/CD) vs controlled (polling vs token/slotted ring).
- Pure vs slotted ALOHA: formulas, G optima, 18% vs 36.8%, vulnerable periods.
- CSMA three persistences and where used (Ethernet vs Wi-Fi).
- CSMA/CD jam → backoff steps; naming of 10BASE5 etc.; conclude it beats ALOHA/CSMA.

---

## M09: TCP/IP Model — IP Addressing I

### In one line
Vertical path of a payload down the practical TCP/IP stack, ports and segments, classful IPv4 addressing, and why CIDR/subnetting is needed to cut waste.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| All People Seem To Need Data Processing | Mnemonic for seven layers from application down. |
| Payload | Application data handed down the stack (e.g. `www.google.com`). |
| Protocol | Set of instructions/rules for a line of action (TCP or UDP at transport). |
| Segment | Transport PDU: payload plus source and destination ports. |
| Port | 16-bit application identifier; 2^16 = 65,536 possible values. |
| Well-known ports | Below 1024; not used as random source ports (source cannot be < 1024). |
| Dotted-decimal | IPv4 written as four octets 0–255 (form X.Y.Z.A). |
| Subnet mask | Marks which IP bits are network vs host. |
| Unicast | One machine talking to one other machine. |
| Network address | IP logically ANDed with the subnet mask (host bits become zero). |
| Broadcast address | All host bits set to 1. |
| Gateway | Router address used to reach another network (often taught as last host IP). |
| CIDR | Classless inter-domain routing — subnetting to reduce classful waste. |

### Concepts explained
To secure systems, first understand networks. Layers talk **vertically**, not horizontally. Practical model combines application + presentation + session into one application layer (browser as user interface). Path: **application → transport → network → data-link → physical**. Data-link/physical depend on Wi-Fi vs wired.

**Transport.** Protocol chooses TCP or UDP. Most real-time apps (WWW/HTTP, mail) use TCP — taught as default for real-time apps. Segment = payload + source port + destination port. Destination port fixed by application (HTTP → **80**); source = random **> 1024**.

| Application | Port(s) |
|-------------|---------|
| HTTP | 80 |
| FTP | 20 and 21 |
| SMTP | 25 |
| SSH | 22 |
| Telnet | 23 |

**IPv4.** 32-bit addresses → 2^32 unique; dotted decimal. Classes A/B/C for hosts; D multicast; E reserved unused. Network vs host bits depend on mask.

| Class | Default mask | Cue / split | Implication |
|-------|--------------|-------------|-------------|
| A | 255.0.0.0 | First octet 0–126; 8 net / 24 host | 2^8 nets, 2^24 hosts each — “bigger networks” |
| B | 255.255.0.0 | 16 / 16 | ~65,536 hosts per network |
| C | 255.255.255.0 | 24 / 8 | 256 addresses — smallest classful size |
| D | — | reserved | Multicasting |
| E | — | reserved | Not used |

Example: `10.10.10.10` → Class A.

**20-host Class C example.** Need 20 machines: Class A wastes huge space (2^24 hosts/net); Class C is the classful fit but still wastes 236 of 256 — “pretty huge waste.” Net `192.168.1.0`; hosts `.1`…`.20` share the same network. Unicast = one machine to one other (e.g. `.2` to one peer). To talk to all on-net machines you need the network identity. Network of `192.168.1.2` AND `255.255.255.0` = `192.168.1.0` (AND with zero octets clears them). Broadcast = host bits all 1 → last octet 255 → `192.168.1.255`. Each network that must talk to another needs three special addresses: network, broadcast, and gateway. Gateway = router to the other network; standard taught = last IP → `192.168.1.254`.

**Usable hosts:** **2^n − 2**. Class C n=8 → 254 hosts; one of those is the gateway → 253 live hosts on a full Class C; for only 20 needed, hundreds still wasted after that accounting.

**CIDR preview.** Classful A/B/C waste IPv4; CIDR (classless inter-domain routing) = subnetting to cut waste. Five host bits cover 20 hosts (binary weights 1+2+4+8+16 = 31 machines); only five of eight last-octet host bits used; three bits go to the network; waste ≈ 11 instead of hundreds. Exact new last-octet mask deferred to next lecture; supernetting also previewed — “play with host bits and network bits.”

**Recap chain:** application payload → vertical to transport → ports make a segment (dest fixed by app, e.g. 80) → network adds source/dest IPs → classful or classless numbering → classful wastes (20-host example) → CIDR next, plus MAC/data-link addresses.

### Numbers / formulas
- Ports: **2^16 = 65,536**; IPv4: **2^32** addresses.
- Usable hosts: **2^n − 2** (Class C: 254).
- Example net/broadcast/gateway: `192.168.1.0` / `.255` / `.254`.

### How to answer
- Vertical stack path; practical merge of top three layers; TCP default for HTTP/mail.
- Segment = payload + ports; dest fixed (80), source > 1024; list FTP/SMTP/SSH/Telnet ports.
- Classful A–E table with masks and bit splits; D multicast, E unused.
- Compute network (AND), broadcast (host bits 1), gateway; write 2^n−2.
- Explain classful waste for 20 hosts and CIDR idea (five host bits).

---

## M10: TCP/IP Model — IP Addressing II

### In one line
Finish CIDR worked examples (20 and 10 hosts), equate slash and mask notation, then map IP (logical) to MAC (physical) via ARP — including the gateway-MAC rule for off-net traffic.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| CIDR | Classless inter-domain routing; slash prefix equivalent to a subnet mask. |
| Incomplete octet | Mask octet that is not 0 or 255; block size = 256 − that value. |
| Block size | Number of addresses in the CIDR block (e.g. 32 for mask 224, 16 for 240). |
| `/28` | 28 network bits = mask `255.255.255.240`. |
| Frame | Data-link PDU with source and destination MAC. |
| Logical vs physical address | IP (logical, like a phone number) vs MAC (physical, like IMEI on a NIC). |
| OUI / OEM | First three MAC bytes (24 bits) — manufacturer. |
| ARP | Address Resolution Protocol — broadcast request / unicast reply mapping IP → MAC on the same network. |
| Gateway MAC | Destination MAC of an off-net frame (not the remote server’s MAC). |

### Concepts explained
Previous lecture left a 20-machine network on `192.168.1.0` needing CIDR with minimal waste. **Powers of two** for last octet must be memorized: 1, 2, 4, 8, 16, 32, 64, 128 — the eight bits of the last octet. Rule taught: bits weighted **1** are network; **0** are host (in the worked mask construction).

**Example 1 — 20 machines on `192.168.1.0`.** Five bits suffice for 20 hosts; five bits address hosts, three address the network in the last octet. Network-bit weights 128+64+32 = **224** → subnet mask **`255.255.255.224`**. That last 224 leaves five host bits. Always work on the **incomplete octet**: incomplete value 224; subtract from 256 → block size **256 − 224 = 32** (32 addresses per block). Network `.0`; last address in block = broadcast = **32 − 1 = 31** → `.31`; hosts `.1`…`.20`; addresses `.21`–`.30` are waste if only 20 machines are required.

**Example 2 — 10 machines on `192.168.1.0`.** Same network address; eight last-octet bits would cover 256 machines; **four bits** cover 10 hosts (four network + four host in last octet). Usable **2^4 − 2 = 14**. Last octet `11110000` → 128+64+32+16 = **240** → mask **`255.255.255.240`**. IPv4 has 32 bits: four host bits ⇒ **28 network bits** ⇒ slash form **`192.168.1.0/28`**. **CIDR notation (`/28`) and subnet-mask notation (`255.255.255.240`) are the same thing.** Incomplete octet 240 → block **256 − 240 = 16**. Network (first in block) `.0`; broadcast (last) `.15`; first host `.1`; last assigned of the 10 = `.10`; unused `.11`–`.14` (four wasted).

These addresses are used at the **network layer**, which forms a **packet**: source IP (client), destination IP (server), plus data from transport and application — **host-to-host** communication — then passes vertically down to data-link.

**Data-link frames.** Hardware-dependent (Wi-Fi ≠ wired format) but both carry source and destination MAC. IP = logical; MAC = physical 48-bit hex (e.g. `00:A0:C0:AB:CD:01`): first 24 bits OEM/OUI, last 24 bits card serial. Hierarchy when surfing: **name → IP → MAC**. Tools: `ipconfig /all` (IP, mask, MAC); `ping www.google.com` (lecture reply then `173.194.126.80`).

**Same-net vs off-net MAC (common exam trap).** Common mistake: assume frame destination MAC is always the server’s MAC. Same network (`192.168.1.1` ↔ `.3`): computer computes both network addresses; if they match, hosts already talk at the network layer but the frame still needs MACs. Source MAC from `ipconfig /all`; destination MAC learned by **ARP** — machine `.1` sends **ARP request (broadcast)**; `.3` returns **ARP reply (unicast)** with its 48-bit MAC; then `.1` forms the data frame. **Different network:** frame destination MAC is the **gateway/router MAC**, not the remote server’s MAC. (What a router is, and IP spoofing, are deferred to later lectures.)

**Layer address roles.**

| Layer | Address | Communication name |
|-------|---------|-------------------|
| Transport | Port (process) | Process-to-process |
| Network | IP (logical) | Host-to-host |
| Data-link | MAC (physical, 48-bit) | Node-to-node |

Classful addressing wastes IPs; CIDR takes only as many host bits as the machine count needs, then you compute network, broadcast, first host, last host. Frames need MACs from ARP. First 24 MAC bits = OEM; next 24 = card sequence. Application still starts from a string; the stack turns it into ports, IPs, and MACs.

### Numbers / formulas
- 20 hosts: mask **255.255.255.224**, block **32**, broadcast **.31**.
- 10 hosts: **/28** = **255.255.255.240**, block **16**, broadcast **.15**, usable **14**.
- MAC: **48 bits** = 24-bit OUI + 24-bit serial.
- Usable hosts: **2^n − 2**.

### How to answer
- Show 20-host mask 224, block 32, net/broadcast/.0/.31 and leftover waste.
- Show 10-host /28 = 240, block 16, table of network/broadcast/first/last/unused.
- Equate CIDR slash with subnet mask.
- Contrast logical IP vs physical MAC (OUI + serial); name → IP → MAC.
- ARP same-net; **off-net dest MAC = gateway** (state the student mistake).
- Process / host / node communication naming by layer.

---

## M11: TCP Connection Management and Flow Control

### In one line
How connection-oriented TCP runs over connectionless IP: three-way open (incl. SYN flooding), bidirectional data with PSH/URG, and three-way close vs four-way half-close.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Virtual path | TCP’s connection-oriented path over connectionless IP; all segments of a message follow one virtual pathway. |
| Passive open | Server tells TCP it is ready to accept; does not itself initiate. |
| Active open | Client request to connect to a particular server. |
| SYN | Control segment that synchronizes ISN; consumes one sequence number; no real data (taught as one imaginary byte). |
| SYN+ACK | Server’s reverse SYN plus ACK of client SYN; carries receive window (rwnd). |
| ISN | Random Initial Sequence Number chosen by each side. |
| TCB | Transmission control block — state/resources allocated per embryonic connection. |
| SYN flooding | DoS via many forged SYNs that exhaust server resources while waiting for the third handshake leg. |
| Cookie | Technique to postpone resource allocation until the client IP is shown valid. |
| Piggybacking | ACK carried together with data. |
| PSH | Push: send/deliver without waiting to fill buffers (interactive immediacy). |
| URG / urgent pointer | Mark a stream range for special treatment; not priority or out-of-order delivery. |
| FIN | Close in one direction; consumes one sequence number if it carries no data. |
| Half-close | Stop sending while still receiving (e.g. client finishes upload, server still returns sorted data). |

### Concepts explained
**TCP over IP.** TCP is connection-oriented (virtual path aids ACK and retransmission) yet uses connectionless IP. IP delivers individual segments unaware; TCP retransmits losses and holds out-of-order segments until gaps fill. Three phases: establishment → data transfer → termination. Full duplex: both sides may send simultaneously after mutual approval.

**Three-way handshake.**
1. **Client SYN:** only SYN set; random ISN; no ACK number; no window (window only with ACK); consumes **one** sequence number; cannot carry data in this account.
2. **Server SYN+ACK:** reverse-direction SYN with server ISN + ACK = client ISN+1; defines **rwnd**.
3. **Client ACK:** usually no data; **ACK consumes no sequence numbers**; seq often same as after SYN; defines server window. Some implementations may carry first data (then new seq = first data byte). Simultaneous open (both active) rare: both send SYN+ACK → one connection.

**SYN flooding (DoS).** Attackers flood SYNs with faked source IPs; server allocates TCB tables and timers, sends SYN+ACK to fakes (lost), waits for third leg; resources stay allocated; valid clients denied. Mitigations: limit connection requests per period; filter unwanted source addresses; postpone allocation until valid IP verified via **cookie**.

**Data transfer.** Bidirectional data + piggybacked ACKs. Example pattern: client 2000 bytes in two segments, server 2000 in one, client one more; first three carry data+ACK, last ACK-only. **PSH:** sending TCP must not wait to fill window; receiver delivers ASAP. Interactive apps need this; most current implementations may ignore application push requests. **URG:** urgent bytes at start of segment; urgent pointer marks end of urgent range; receiver informed (OS-dependent); action is application’s discretion. Urgent mode is **neither priority nor expedited service** — only marks a portion of the in-order stream; TCP never delivers out of order.

**Termination.** Either side may close; usually the client. Two options taught: three-way handshaking and four-way with half-close.
- **Three-way close (common):** after client process close, client TCP sends FIN (may carry last data chunk or be control-only; control-only FIN consumes one seq — “FIN consumes one sequence number if it does not carry data”) → server informs its process, then FIN+ACK (confirms client FIN and announces close the other way; may carry last server data; if not, consumes one seq) → client final ACK (cannot carry data; consumes no seq; ACK number = 1 + sequence in server’s FIN).
- **Four-way half-close:** one end stops sending while still receiving. Client half-closes with FIN → server accepts with ACK → server may still send remaining data → when done, server FIN → client ACK. After half-close, data server→client and ACKs client→server continue; client cannot send more data. Useful when server needs all input before processing (e.g. sorting: client sends all data, closes client→server, but server→client must stay open to return sorted results). ACK of client FIN consumes no sequence number; server numbering stays at next expected until server’s own FIN; last ACK still uses client sequence x because that direction consumed no further sequence numbers during the remaining transfer.

### How to answer
- TCP virtual connection over unaware IP; three phases; full duplex needs mutual init.
- Walk SYN / SYN+ACK / ACK with ISN, seq consumption rules, and rwnd.
- Define SYN flooding as DoS on TCB/timers; list limits, filters, cookies.
- Piggybacked ACKs; PSH for interactive push; URG marks in-order special bytes (not priority/out-of-order).
- Contrast three-way FIN close with four-way half-close and when half-close is needed.
