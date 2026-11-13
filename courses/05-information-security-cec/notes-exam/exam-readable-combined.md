# Information Security (CEC) — Exam-readable notes

> Full concept coverage rewritten for understanding and answer writing.
> Clearer than transcript notes-2; denser than ultra-short notes-3.
>
> Companion calculations: `final pdf/05-information-security-cec-numericals.pdf`

## How to use in exams

1. Read **In one line** to orient.
2. Memorize **Definitions** tables — these are write-ready.
3. Use **Concepts explained** for 5–10 mark explanations.
4. Expand **How to answer** bullets into paragraphs on the sheet.

---

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

\newpage

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

\newpage

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

\newpage

# Volume 04 — Mobile IP, Cloud, Cellular, MANET, VoIP & DDoS (M36–M47)

> Information Security (CEC) · Exam-readable notes
> Full concept coverage rewritten for understanding and answer writing (not the ultra-short notes-3).

---

## M36: Introduction to Mobile IP and Addressing

### In one line
Mobile IP keeps a permanent home address plus a changing care-of address so a host can move networks without breaking IP routing or active connections.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Home address | Permanent IP address that ties the mobile host to its home network; never changes as the host moves. |
| Care-of address (CoA) | Temporary address associated with the foreign (visited) network; changes each time the host moves. |
| Collocated care-of address | Care-of address when the mobile host acts as its own foreign agent (often obtained via DHCP), so no FA need be present. |
| Home agent (HA) | Application-layer agent, usually a home-network router, that intercepts packets for the mobile host and tunnels them to the foreign side. |
| Foreign agent (FA) | Application-layer agent on the visited network that unwraps the tunnel and delivers packets to the mobile host. |
| Agent advertisement | ICMP router advertisement with a type-16 agent extension listing care-of addresses (used by an FA). |
| Agent solicitation | ICMP request sent by the mobile host when it has moved but has not received advertisements. |
| Proxy ARP | Technique by which the home agent answers ARP for the mobile host’s home address, pretending to be that host on the home LAN. |
| Tunneling (IP-in-IP) | Encapsulation of the original IP packet inside a new IP packet from HA to FA. |
| Double crossing (2X) | Inefficiency when remote and mobile hosts are on the same network: the return path still detours via the home agent across the Internet twice. |
| Triangle / dog-leg routing | Moderate inefficiency: remote → home agent → mobile instead of a direct path to the CoA. |
| Binding / warning | Correspondent caches CoA to shortcut the triangle; HA must warn when the host moves again so the cache is not stale. |

### Concepts explained

**Why classic IP fails for mobility.** An IP address has a prefix (network) and a suffix (host). Routers deliver using the prefix, so the address is valid only while the host is attached to that network. Example taught: `10.3.4.24/8` belongs to network `10.0.0.0/8`. A host cannot “carry” that address to another network.

**Why DHCP-only renumbering is not enough.** Changing address on each move would require rewriting configuration files, often a reboot, updating DNS so every other host learns the new address, and—critically—would break in-flight connections because client and server IP addresses and ports must stay constant for the session.

**Two-address solution.** Mobile IP therefore gives each mobile host a permanent **home address** and a temporary **care-of address**. Transparency to the rest of the Internet requires a **home agent** and usually a **foreign agent**. Agents look like routers in diagrams but their agent functions run at the application layer (they are both routers and hosts). The mobile host may itself be the FA using a **collocated CoA** obtained e.g. via DHCP—advantage: it can visit any network even if no FA is installed.

**Three phases of mobile communication**

1. **Agent discovery** — find HA before leaving home; find FA (and CoA) after moving.
2. **Registration** — register with FA and HA; renew; cancel when returning home.
3. **Data transfer** — remote host is involved; four paths.

**Agent advertisement fields (type 16 extension):** Type (16), Length (of extension only), Sequence number (detect loss), Lifetime (seconds; all ones = infinite), Code (flags), Care-of address list (FA only; MH picks one for the registration request).

**Registration request (type 1):** Flag bits, Lifetime (all zeros = deregistration; all ones = infinite), Home address, Home-agent address, Care-of address, 64-bit Identification (echoed in reply), Extensions (authentication). Path: MH → FA → HA (FA’s IP becomes source of the relayed packet, so HA learns FA). Reply: HA → FA → MH (confirm or deny).

**Four-path data transfer**

| Path | What happens |
|------|----------------|
| 1 Remote → HA | Remote uses its own source and MH’s **home address** as destination. HA intercepts via **proxy ARP**. |
| 2 HA → FA | HA **tunnels**: outer IP HA→FA encapsulating the original packet. |
| 3 FA → MH | FA unwraps; looks up CoA in its registry (inner dest is still home address); delivers to CoA. |
| 4 MH → Remote | MH sends normally with **home address as source**; remote never sees mobility. |

**Inefficiencies and the binding fix.** 2X is severe because hosts often talk to local peers. Triangle routing is moderate. Fix: HA can send an **update binding** so the correspondent caches CoA and sends later packets directly. When MH moves again the cache is stale; HA must send a **warning**.

### How to answer
- State that IP prefixes assume fixed attachment; DHCP alone breaks config, DNS, and live connections.
- Define home address vs care-of address; name HA, FA, and collocated CoA.
- Describe discovery (advertisement type 16 / solicitation) then registration (type 1; lifetime 0 = deregister).
- Walk the four paths: proxy ARP, IP-in-IP tunnel, FA unwrap + CoA lookup, return with home source.
- Explain transparency to the correspondent and why that causes 2X and triangle routing.
- Mention binding cache as a shortcut and the stale-cache / warning problem.

---

## M37: Cloud Computing Architecture

### In one line
Cloud computing is Internet-based hiring of pooled, elastic, metered resources (not a simple remote PC), offered under four deployment models and three SPI service models over a four-layer architecture.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Cloud computing | Storing and accessing data/programs over the Internet from remote, scalable, elastic infrastructure—metaphorically “the cloud”—paying only for what is consumed. |
| On-demand self-service | Customer provisions resources without a human intermediary. |
| Broad network access | Resources reachable from anywhere via browser, desktop app, or mobile (e.g. iPhone apps). |
| Resource pooling | Multi-tenant dynamic assignment of storage, CPU, memory, bandwidth; exact location opaque except region/country. |
| Rapid elasticity | Expand and release resource pools as demand changes. |
| Measured service | Metering, monitoring, and audited pay-per-use reports for provider and consumer. |
| Private / public / community / hybrid | Four deployment models differing by who owns, shares, and controls the cloud. |
| Cloud bursting | Hybrid pattern: private capacity plus public-cloud spillover during demand spikes. |
| SaaS / PaaS / IaaS (SPI) | Software / Platform / Infrastructure as a Service. |
| Thin vs thick client | Thin: low processing, fully dependent; thick: adequate independent local processing. |
| SLA | Service-level agreement; QoS penalties apply to cloud management and hardware layers, **not** the user’s Internet path. |
| OpenStack | Example stack for creating, deploying, and managing a **private** cloud. |

### Concepts explained

**Cloud vs local vs “simple remote machine.”** Local hard-drive use is local storage/computing. Cloud requires Internet access to remote resources that are scalable and elastic—significantly different from just using another PC elsewhere. IT resources (servers, storage, network, applications, processes) can be dynamically provisioned for grids or non-grid three-tier / Web 2.0 apps. Especially attractive to individuals and SMEs wanting capacity without new capital, training, or licenses.

**Essential characteristics (all required).** The lecture stresses: if **any** is missing, it is **not** cloud computing.

| Characteristic | What it means in practice |
|----------------|---------------------------|
| On-demand self-service | Self-provision by demand with no human gatekeeper |
| Broad network access | Heterogeneous access: browser, desktop app, mobile (iPhone-app backends cited) |
| Resource pooling | Multi-tenant; dynamic assign/reassign of storage, processing, memory, bandwidth; location opaque except country/region; capacity often appears unlimited |
| Rapid elasticity | Take what is needed and free pools when demand falls |
| Measured service | Meter how much disk, which services, how many hours; audited reports; pay only for use |

**Deployment models**

| Model | What it is / why choose it |
|-------|----------------------------|
| **Private** | Behind firewall, corporate IT control, authorized users only; physical hosts may be internal or external but from a distinct pool; good for dynamic mission-critical uptime/security; still prone to disaster and insider theft; “what counts as private” is hard to define because service mixes vary. |
| **Public** | Open network usage; little distinguished location control; structure may differ little from private except security level; load management, SaaS-style apps, many users; lower CapEx/OpEx; free or pay-per-user; economies of scale; example free public cloud: **Google**. |
| **Community** | Shared by orgs with similar privacy/performance/security concerns and business objectives (e.g. banks and trading firms); managed internally or by a third party; hosted internally or externally; cost shared → savings. |
| **Hybrid** | Two or more clouds bound together but remaining individual entities; crosses isolation so it cannot be labeled simply public/private/community. |

**Hybrid examples taught:** non-critical development/test on third-party public, sensitive work internal; e-commerce on private for security/scalability plus brochure site on cheaper public; demand spikes → **cloud bursting** from public; big-data retained on private with analytical queries on public; hosting gains scalability/flexibility/security if one overlooks API incompatibility, connectivity issues, and CapEx. Selecting the right hosting type after analyzing demand matters.

**SPI service models**

| Model | Consumer gets | Examples taught | Control note |
|-------|---------------|-----------------|--------------|
| **SaaS** | Provider apps on cloud infra; possible limited user-specific config; thin-client (browser) or program interface | CRM, BI/analytics, online accounting | Does **not** manage/control underlying infra |
| **PaaS** | Deploy consumer-created/acquired apps with provider languages, libraries, tools; packaged ready-to-run framework; provider manages scalability/maintenance | Google App Engine, Microsoft Azure | Control deployed apps (+ possibly hosting-env config); vendors manage everything underneath |
| **IaaS** | Provision processing, storage, networks on pay-per-use; deploy OS and applications; provider owns housing/cooling/operation | Amazon Web Services (AWS) | More customer management; **already have a software package to install → choose IaaS not PaaS** |

**Four-layer architecture** (hierarchical; completely Internet-dependent):

1. **User/client (lowest)** — thin (fully dependent, very low processing), thick (adequate independent processing), mobile/handheld initiating connections; cloud apps often feel like web apps but internal properties differ.
2. **Network** — Internet for public cloud (location abstract/worldwide); LAN possible for private; users need minimum bandwidth; **outside SLA/QoS** (Internet path not counted).
3. **Cloud management** — cloud OS between data center and user; scheduling, provisioning, optimization, server/storage/workload consolidation, internal governance; delays/discrepancies can violate SLA → **penalty**; **under SLA** for private and public (AWS, Azure public; **OpenStack** private create/deploy/manage).
4. **Hardware / data center** — **most important layer governing SLAs**; access should be as quick as SLA allows or penalty applies; needs high-speed DC links and efficient algorithms; a cloud may have many DCs; several clouds can share a DC. Loose isolation between layers 3 and 4 is possible depending on deployment.

### How to answer
- Define cloud as Internet hire-and-pay elastic resources, not a local box or dumb remote PC.
- List all five essential characteristics and say all are mandatory.
- Contrast private / public / community / hybrid with at least one hybrid example (bursting).
- Distinguish SaaS, PaaS, IaaS with taught examples; state bring-your-own package → IaaS.
- Draw/describe four layers and state: network outside SLA; management and hardware inside; hardware governs penalties most.

---

## M38: Security in Cloud Computing

### In one line
Cloud security is the set of procedures, processes, and standards spanning physical and logical issues across SPI and public/private/hybrid delivery, with risks inherited up the stack and distinct data, virtualization, network, and service-model challenges.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Cloud computing security | Procedures, processes, and standards that provide information-security assurance in cloud environments. |
| Trust path | Chain of dependency among parties in Internet applications such as e-commerce. |
| New insider | Provider staff who can see or control customer data without being company employees. |
| Sticky services | Provider lock-in (e.g. incompatible storage APIs) that makes migration hard. |
| Hypervisor | Virtualization translation layer; its I/O path and security model must not be assumed safe. |
| Broadcast-domain abstraction | Cloud-network feature often missing; forces application rewrite for IP/failover assumptions. |
| XML encryption / WS-Security / SSL / TLS | In-transit protections listed for SaaS web/services traffic. |
| Amazon S3 (as taught) | Example where **data at rest are unencrypted by default**—user must encrypt data and backups separately. |
| CIA | Confidentiality, integrity, availability; virtual-network QoS issues hit **availability**. |
| Active Directory | Traditional authentication repository that private cloud must grow beyond for tenants and fabric admin. |

### Concepts explained

**Scope.** Cloud security covers physical and logical issues for SaaS/PaaS/IaaS and public/private/hybrid delivery. End users care how and when data are stored and who has access. Putting business data with an outside provider makes regulatory compliance riskier; clients must **verify** provider practices after loss of direct oversight.

**Research context taught:** reliable distributed apps needing trust paths; next-gen data centers that are scalable, efficient, agile, reliable, and secure for millions of developers and billions of users; virtualization allocating compute/network/storage under SLA for availability, performance, and security (likened to telecom-scale networks).

**Data-security challenges** (data sit in the provider’s infrastructure, not the org’s territory):
- Service models with **multiple tenants sharing** the same infrastructure.
- **Data mobility** vs legal rules such as the **European Union data privacy directive**.
- **Lack of standards** on how providers securely recycle disk space and erase existing data.
- **Loss of visibility** into key security/operational intelligence that no longer feeds enterprise IT SIEM and risk management.
- A **new type of insider** who does not work for your company but may control and see your data.

**Virtual data-center / virtualization issues.** Data live in a virtual data center of unknown location whose backbone is VMs; problems often **do not appear in staging** and show up only when VMs take the same load as physical machines. Two cornerstones: network and storage.
- **Lack of performance/availability:** many I/O tasks tuned for hardware move into software via the **hypervisor** translation layer (software view ↔ physical CPU).
- **Lack of application awareness:** hypervisor/kernel-based virtualization virtualizes only the **OS**; even apps do not realize they sit on virtual hardware.
- **Overflowing storage:** P2V helps dynamism but hard drives become extremely large flat-file virtual disk images → unmanageable file storage.
- **Congested storage network:** OS-image portability makes it trivial to move VMs host-to-host or array-to-array, flooding the storage network—the same reason disk files overrun physical storage.

**Cloud network challenges (backbone of the cloud):**
- **Application performance:** tenants need specified / **guaranteed bandwidth** between server instances so tiered apps meet SLAs like on-premises; insufficient bandwidth → significant latency.
- **Flexible appliance deployment:** DPI, IDS, firewalls, plus load balancing, caching, application acceleration must still be usable.
- **Policy-enforcement complexity:** traffic isolation and end-user access control impact configuration of **each** router and switch.
- **Changing requirements / protocol zoo:** OSPF, LAG, VRRP, L2 spanning-tree flavors, vendor-specific protocols make building/operating/interconnecting at scale hard.
- **Application rewriting:** missing **broadcast-domain abstraction**; **cloud-assigned IPs** for virtual servers; IP/failover assumptions break.
- **Location dependency:** server IP tied to VLAN/subnet on **physical switch ports** → VMs cannot migrate smoothly; utilization/flexibility fall; IP pools fragment.

**Inherited risk on SPI.** Providers offer varied services with challenges: secured network, locality of resources, accessing secure data, privacy, backup policy. **IaaS is the basis of all cloud services**; PaaS builds upon IaaS; SaaS upon PaaS. **Capabilities are inherited—so are information-security issues and risks.** Trade-offs exist among integrated features, complexity vs extensibility, and security. If the provider secures only the lower part, **consumers become more responsible** for the rest. SaaS is emerging as the dominant enterprise delivery model; PaaS abstracts everything up to OS/middleware and offers a complete SDLC view.

**SaaS security issues.** On-premises, sensitive data stay inside the enterprise boundary under physical/logical/personnel controls. SaaS is web-accessed → **browser security** matters; officers consider web-services security, **XML encryption**, **SSL**, strong encryption, fine-grained authorization.

| Issue | Teaching |
|-------|----------|
| Network security | Encrypt sensitive data in flight with **SSL/TLS** |
| Resource locality | Users often do not know exact location; country compliance/privacy make locality critical |
| Cloud standards | Needed for interoperability/stability/security; incompatible storage APIs → **sticky services** / hard migration |
| Data access | Org policies (who may see what) must still hold inside a cloud hosting many orgs |
| Data breaches | Many users’ data lie together → high-value target; one breach hits all |
| Backup | Regular encrypted backups for disaster recovery; on **Amazon S3, data at rest are not encrypted by default**—encrypt data and backups yourself |

**PaaS security issues:** challenges mainly from spread of user objects over cloud hosts; stringently allow object access and defend against malicious/corrupt providers; network access and service measurement need secure communications and access control; well-known practices: **object-scale authorization** and **undeniable traceability**; privacy-aware solutions in public shared clouds; enterprises need fault-tolerant continuity.

**IaaS / private-cloud security issues that remain** (private cloud solves many problems but is “not that good at solving security”):
- **Hypervisor security** — do not take the model for granted; evaluate security models and hypervisor development.
- **Multi-tenancy** — even same-company tenants may dislike sharing infra.
- **Identity/access** — beyond a small set of repos such as **Active Directory**: authz for cloud infra, tenants, and delegated fabric administration.
- **Network security** — many components talk only over virtual channels; need powerful ACLs and QoS (CIA **availability**).

**Combined picture:** combining three clouds (public/private/hybrid) with three delivery models gives a complete environment interlinked by connectivity devices and information-security components. Virtualized physical resources, infrastructure, middleware platforms, and business applications are provided as services. **Providers and consumers must establish security at all levels of interfaces.**

### How to answer
- Define cloud security as procedures/processes/standards across SPI and deployment models.
- List data challenges: multi-tenancy, EU privacy, wipe standards, lost visibility, provider insider.
- Name virtualization cornerstones (hypervisor I/O, app-unaware VMs, huge images, storage-network flood).
- Enumerate network challenges including missing broadcast domain and VLAN/port binding.
- Explain risk inheritance IaaS→PaaS→SaaS and give SaaS/PaaS/IaaS issue examples (encrypt S3 yourself; hypervisor/IAM).

---

## M39: GSM Architecture

### In one line
GSM is the dominant 2G digital cellular standard (CEPT → ETSI → 3GPP) built from RSS, NSS, and OSS with distinct identities, databases, interfaces, and teleservice / bearer / supplementary services.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| GSM | Global System for Mobile Communications — 2G digital cellular; ~70% market share; 800+ million users in 190+ countries. |
| RSS / NSS / OSS | Radio Subsystem, Network and Switching Subsystem, Operation Subsystem. |
| Um / Abis / A / O | MS–BTS radio (TDMA/FDMA); BTS–BSC; BSS–MSC (PCM-30, up to 30×64 kbps); management via SS7/X.25. |
| IMEI / IMSI | Equipment identity burned into hardware at manufacture vs subscriber identity stored on the SIM. |
| PIN / PUK / Ki / Kc | Unlock SIM; unblock after three wrong PINs; authentication key on SIM/AuC; cipher key while camped. |
| TMSI / LAI | Temporary Mobile Subscriber Identity and Location Area Identification stored while logged on. |
| HLR / VLR | Home Location Register (permanent user DB) vs Visitor Location Register (per-MSC copy that cuts long-distance signaling). |
| AuC / EIR | Authentication Center (Ki, algorithms); Equipment Identity Register (IMEI white/black/grey lists). |
| GMSC / SMS-GMSC / SMS-IWMSC | Gateway for mobile-terminating voice; SMS toward MS; SMS originated by MS to SMS Center. |
| Teleservice / bearer / supplementary | Speech/SMS/fax etc.; data path (9.6 kbps, HSCSD, GPRS); extras such as CLIP, CLIR, AoC, CUG. |
| MSISDN / MSRN | Directory number vs Mobile Station Roaming Number obtained from HLR for routing. |

### Concepts explained

**History and bands.** Digital cellular networks are wireless extensions of PSTN/ISDN allowing seamless national/worldwide roaming with the same phone; mainly voice today with growing data. GSM is the most popular digital system (~70% share; 800+ million users; 190+ countries). Early 1980s Europe had many coexisting analog systems on slightly different carriers. To avoid that for fully digital 2G, **Groupe Spécial Mobile (1982)** was founded; soon renamed **Global System for Mobile Communications** under **ETSI**. With UMTS, development transferred to **3GPP** (new standard numbers). Primary goal: roam throughout Europe with voice compatible with ISDN/other PSTN. Typical **2G**: replaces 1G analog but does not offer 3G (e.g. UMTS) worldwide high data rates.

| Name | Band as taught |
|------|----------------|
| GSM900 | Europe initially: **890–915 MHz uplink**, **935–960 MHz downlink** |
| DCS 1800 | GSM at 1800 MHz |
| PCS 1900 | Mainly US at 1900 MHz |

**Three subsystems.** Hierarchical architecture. User mainly sees MS and some BTS antennas (RSS); NSS and OSS are internal. RSS↔NSS via **A** (typically circuit-switched **PCM-30**, up to **30 × 64 kbps**); RSS↔OSS via **O** (**SS7** based on **X.25**, management data).

**Radio subsystem (RSS):** all radio-specific entities—MS plus **base station subsystem (BSS)**. A GSM network has many BSS, each controlled by a **BSC**. BSS maintains radio connections, voice coding/decoding, and rate adaptation. A BSS contains several **BTS**.
- **BTS:** antennas, signal processing, amplifiers; one cell or several with sectorized antennas; **Um** to MS, **Abis** to BSC. Um carries TDMA/FDMA etc.; cell size ~**100 m to 35 km**.
- **BSC:** reserves radio frequencies; handover BTS↔BTS within BSS; pages MS; multiplexes radio channels onto fixed network at A.
- **MS:** hardware + SIM. Hardware holds **IMEI** (set at manufacture, cannot change; checked at registration for stolen gear). SIM holds card type, serial, subscribed services, **PIN**, **PUK**, **Ki**, **IMSI**. Wrong PIN three times locks SIM → need PUK. While logged on: dynamic **Kc**, **TMSI**, **LAI**. Transmit power up to **2 W** GSM900; **1 W** enough for GSM1800 (smaller cells). Extras: Bluetooth, cameras, PDAs, car integration, container tracking.

**NSS (heart of GSM):** connects wireless network with public networks; handovers between different BSS; worldwide localization; charging, accounting, roaming across countries.
- **MSC:** like PSTN/ISDN switch plus mobility; backbone among MSCs and BSCs via A; manages several BSCs in a region (registration, authentication, call location, inter-MSC HO, routing); interfaces PSTN, other MSCs, PDN (e.g. X.25); signaling for setup/release/HO.
- **HLR:** most important DB. Static: **MSISDN**, subscribed services (call forwarding, roaming restrictions, GPRS), **IMSI**. Dynamic: current LA, **MSRN**, current VLR and MSC. Updated when MS leaves LA; at switch-on registers so network knows BTS; even idle phones re-register periodically for localization. Each user’s data exist **once** in a single HLR (may be distributed across subcenters); highly specialized real-time DB for millions; supports charging/accounting.
- **VLR:** associated with each MSC; dynamic DB of users in that LA (IMSI, MSISDN, HLR address). On entry, VLR **copies** relevant HLR data—**hierarchy avoids frequent HLR updates and long-distance signaling**. Commonly integral to MSC for faster access.
- **EIR / AuC:** decide whether equipment may enter (IMEI); protected DB of secret key also in SIM for authentication and radio ciphering.
- **GMSC:** point to which a mobile-terminating call is initially routed without knowing MS location; obtains **MSRN from HLR** based on MSISDN; routes to visited MSC. “MSC” in the name is misleading—gateway op need not link to an MSC.
- **SMSG:** **SMS-GMSC** (messages to mobile) and **SMS-IWMSC** (messages originated by mobile; fixed access to SMS Center).

**OSS:** operation and maintenance; own entities; accesses others via SS7; connected to NSS and BSC; monitors overall network and BSS traffic load. As BTS count scales, some maintenance moves to BTS to cut cost of ownership.
- **OMC:** traffic monitoring, status reports, subscriber and security management, accounting/billing; uses **TMN** concept (ITU).
- **AuC (OSS view):** separate because radio interface and MSs are vulnerable; authentication algorithms and encryption keys; generates values for user authentication in HLR; may sit in special protected HLR part.
- **EIR (OSS view):** all registered IMEIs; **blacklist** stolen/locked; **whitelist** valid; **grey list** malfunctioning. **Blacklists of different providers are not usually synchronized**, so illegal use on another operator’s network is possible.

**Services (three basic types)**
- **Teleservices:** telephony (full-rate speech **13 kbps**; emergency via three digits to nearest provider); videotex/teletex/fax/alternate speech+fax; **SMS** (also news, sports, financial, language, location-based data).
- **Bearer services:** building block toward mobile Internet; currently **9.6 kbps**; newer **HSCSD** and **GPRS**.
- **Supplementary services:**

| Service | Meaning |
|---------|---------|
| Conferencing | Multi-party (≥3); normal telephony only |
| Call waiting / hold / forwarding / barring | Notify/answer/ignore; park/resume; divert; restrict outgoing (e.g. ISD) or undesired incoming |
| CLIP / CLIR | Show / hide caller’s number |
| COLP / COLR | Show / hide connected number (useful when forwarded; COLR normally overrides presentation) |
| Malicious call identification | Identify obscene/annoying calls in the network |
| AoC | Advice of Charge; data calls time-based |
| CUG | Closed User Group—members call only each other |

**Incoming-call path (exam story):** PSTN → GMSC → HLR (request MSRN) → visited MSC → VLR/BSS paging with TMSI/LAI → MS answers; cipher with Kc.

### How to answer
- Place GSM as digital 2G replacing fragmented analog 1G; name ETSI/3GPP and three bands.
- Partition RSS / NSS / OSS and name Um, Abis, A, O with roles.
- Contrast IMEI (equipment) vs IMSI/SIM (subscriber); PIN/PUK/Ki/Kc/TMSI/LAI.
- Explain MSC, HLR/VLR hierarchy, GMSC+MSRN, AuC, EIR (unsynced blacklists).
- Classify teleservices, bearers (9.6 / HSCSD / GPRS), and key supplementary services.

---

## M40: MANET - I

### In one line
A MANET is an infrastructure-less, IP-based radio network of mobile nodes that act as both hosts and routers, with dynamic topology, scarce resources, open security/routing challenges, and applications from battlefields to VANETs and meshes.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| MANET | Mobile Ad hoc Network — infrastructure-less, IP-based radio network of mobile nodes that route for one another without centralized administration. |
| Fixed wireless network | Fixed hosts/routers communicate over wireless channels (e.g. directed antennas). |
| Wireless with fixed APs | Mobile hosts associate with fixed access points that may act as routers (e.g. campus WLAN). |
| Multi-hop | Relaying through intermediate nodes when source and destination are outside each other’s radio range. |
| Dynamic topology | Links break unpredictably and often because nodes move freely. |
| QoS | Guaranteed performance for a flow: delay, jitter, bandwidth, packet-loss probability. |
| VANET | Vehicular ad hoc network; **V2V** vehicle-to-vehicle, **V2I** via roadside units. |
| WSN | Wireless sensor network — low-mobility special case of MANET with sinks and sensing nodes. |
| Wireless mesh (WMN) | Many 802.11a/b/g mesh routers sharing connectivity by dynamic hop-by-hop routing. |
| PAN | Personal area network for devices around one person; Bluetooth wire-replacement example. |

### Concepts explained

**Wired vs wireless.** Both are formed by routers (forward packets) and hosts (sources or sinks). Wired networks rely on cables; wireless may mix wired and wireless links. Freedom from cables gives hosts and routers mobility—an advantage of wireless networking.

**Three wireless types (by mobility of hosts/routers)**

| Type | How formed | Example |
|------|------------|---------|
| Fixed wireless | Fixed hosts/routers use wireless channels | Directed antennas between two computers |
| Wireless with fixed APs | Mobile hosts talk to fixed access points (may act as routers) | Laptops in a building |
| **MANET** | Mobile hosts, some of which forward for neighbours | Vehicle-to-vehicle; ship-to-ship peer routing with **no centralized administration** |

**What a MANET is.** Infrastructure-less, **IP-based** radio network of mobile wireless machines. Nodes have no central admin. It is **routable**: **each node acts as a router** and forwards toward a destination. Mobiles and laptops can form one among themselves. Simplest case: direct communication in range. Must also support **indirect** paths through hops. Taught figure: nodes **A** and **C** are not in each other’s radio circles, so **B** must relay; circles = nominal transceiver range.

**Characteristics (expanded)**
- **Autonomous terminal:** each node may be host or router; endpoints and switches usually indistinguishable.
- **Distributed operation:** no background network for central control; nodes collaborate as relays for security and routing.
- **Multi-hop routing:** single-hop MANETs are simpler; outside direct range, intermediates forward.
- **Lightweight terminals:** less CPU, small memory, low power storage → optimized algorithms.
- **Dynamic topology:** free movement → rapid unpredictable change; links break far more often than wired/infra wireless.
- **Self-organization** and **multi-hopping** without infrastructure.
- **Resource conservation:** energy and processing limits dominate design.
- **Limited capacity / limited security:** more prone to threats; both legitimate users and attackers access the wireless channel; **no well-placed location for access-control mechanisms**.
- **Scalability:** apps may grow to thousands of nodes; channel capacity limited and hit faster under multi-hopping; related to routing protocols used.
- **Low bandwidth:** shorter range than fixed infra; throughput reduced by multipath fading, noise, interference.

**Open challenges listed:** scalability, routing, QoS, client–server model shift, security, energy conservation, node cooperation, interoperation.
- **Scalability:** unclear how “universal computing” scale can actually grow; capacity scalability problems are inherent.
- **Routing:** nodes dynamically form a temporary network without pre-existing infra; must continually adapt and establish routes without outside support while still moving.
- **QoS:** heterogeneous apps (voice, live video, file transfer) need guarantees on delay, jitter, bandwidth, packet-loss probability; still described as an **unexplored area**.
- **Client–server shift:** structure cannot be defined by collecting IPs into subnets; may be no servers, yet demand remains for address allocation, name resolution, authentication, service location whose location is unknown and changes; unclear who manages services.
- **Security:** military and confidential meetings need protection against active/passive attackers; lack of central management or a **certification authority** is a major roadblock to commercial use.
- **Interoperation:** two autonomous ad hoc nets in the same area must recognize and merge despite different synchronization, MAC, or routing (example: military unit with location-based routing meeting a sensor net with simple static routing). Energy conservation and node cooperation remain on the list.

**Applications** (best where infrastructure is unavailable or not cost-effective)
- **Military:** battlefield survivability; devices on soldiers, tanks, helicopters, vehicles pass messages.
- **Home/office/education:** laptops/PDAs/WLAN devices without a base station; Bluetooth **PAN** wire replacement; stream video/audio (students pull class material from professor’s laptop); universities, virtual classrooms, meeting/lecture ad hoc links.
- **VANET:** V2V direct; V2I via roadside units (RSUs).
- **WSN:** special case of MANET with reduced/no mobility; tiny disposable low-power nodes; sensors monitor sound, temperature, humidity, vibration, pressure, motion, pollutants; nodes sense/process/communicate in a self-organizing battery network; one or more **sinks** reach the user (possibly via wired nets); topology may be a simple star; military then civilian (environment, disaster, smart home, production, healthcare).
- **Wireless mesh:** city-scale; dozens–hundreds of mesh nodes like wireless routers using **802.11a/b/g** on 2.4/5 GHz (802.11a up to **54 Mbps**); hop-by-hop dynamic choice of quickest/safest path; Internet cloud as backbone of mesh routers/APs/base stations.
- **Disaster relief:** keep networks operating when quakes/floods disable infrastructure.
- **PAN:** person-centred nodes (clothes, belt, handbags)—e.g. print upstairs from the couch; upload phone photo to desktop.

### How to answer
- Contrast three wireless types; define MANET as infrastructure-less host+router radio IP network.
- Explain A–B–C multi-hop story and list key characteristics (dynamic topology, energy, security, bandwidth).
- Name open challenges: routing, QoS, naming without servers, security without CA, interoperation.
- Give application families: military, campus, VANET, WSN, mesh, disaster, PAN with one concrete detail each.

---

## M41: MANET – Routing Protocols

### In one line
MANET routing protocols find paths under topology change using reactive (AODV), proactive (OLSR), or hybrid (TORA) strategies with distinct control messages and trade-offs.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| Routing protocol | Software/hardware implementation of a routing algorithm: finds paths, exchanges router info, adapts under changing conditions using chosen metrics. |
| Reactive / on-demand | Builds a route only when needed (route request flood); higher search latency; saves idle bandwidth. |
| Proactive / table-driven | Continuously maintains routes to all nodes via periodic control traffic; fast session start; not bandwidth-efficient; slow recovery after some failures. |
| Hybrid | Proactive pre-planned routes plus reactive flooding for extra demand; needs foreknowledge of traffic and node count. |
| AODV | Ad hoc On-Demand Distance Vector (RFC 3561); RREQ, RREP, RERR. |
| Expanding ring | Increase RREQ TTL on retransmission if no reply, limiting flood scope. |
| Precursor list | Neighbours likely to use this node as next hop; used to target RERR. |
| OLSR | Optimized Link State Routing — proactive protocol using multipoint relays. |
| MPR | Multipoint relay: selected symmetric one-hop neighbour that forwards floods to cover all two-hop neighbours. |
| TC message | Topology-control advertisement from nodes with a non-empty MPR selector set. |
| TORA | Temporally-Ordered Routing Algorithm — hybrid DAG of ordered heights; QUERY / UPDATE / CLEAR. |

### Concepts explained

**Comparison of types**

| Type | Example | Bandwidth | Latency to start | Notes |
|------|---------|-----------|------------------|-------|
| Reactive | AODV | Better when idle | Higher (search delay) | Topology info only on demand |
| Proactive | OLSR | Periodic overhead | Low | Too much maintenance data; slow link-failure recovery |
| Hybrid | TORA | Mixed | Mixed | Only when demand/size known beforehand |

**AODV (reactive, RFC 3561).** No route → flood limited **RREQ**. Route found when RREQ hits destination **or** intermediate node with valid entry. Passive when route dies → request again. Control messages:
- **RREQ:** source addr/seq, broadcast ID, dest addr/seq, hop count; expanding-ring TTL.
- **RREP:** unicast back (forwarders cached reverse path); source/dest, dest seq, hop count, lifetime.
- **RERR:** on active-route link break; uses precursor lists.

**Four-node example:** Node 1 wants 3; neighbours are 2 and 4; cannot reach 3 directly. RREQ to 2 and 4. Node with route or = dest sends RREP; else rebroadcast until lifespan. No reply → longer TTL + new ID. Sequence numbers stop duplicate rebroadcasts. In example **node 2 has route to 3 → RREP**; **node 4 rebroadcasts**. Better sequence number in RREP replaces table entry.

**Three RERR circumstances:** (1) must forward data but has no route (someone wrongly thinks path is here); (2) receives RERR that invalidates own routes → send RERR for newly unreachable dests; (3) cannot talk to neighbour → invalidate next-hop entries → RERR. Receivers remove routes containing bad nodes.

**OLSR (proactive).** Permanent routing tables; periodic topology exchange; dense deployments; Dijkstra hop-shortest paths. Differs from classical link state: (1) only MPRs of A forward A’s updates; (2) A’s update size shrinks to neighbours that selected A as MPR.
- **Neighbour sensing:** Hello (not forwarded) carries neighbour list/link status (symmetric/asymmetric); builds two-hop set; MPR selection; MPR selector list (forward only from selectors).
- **MPR flooding:** smallest subset of symmetric one-hop neighbours covering all two-hop neighbours; cuts duplicate Tx/Rx.
- **Topology diffusion:** TC messages from nodes with non-empty MPR selector set advertise links to selectors → topology table → routing table; recalculate on change.

**TORA (hybrid).** Addresses high mobility / congestion where classical shortest-path and link-state fail. Flat algorithm; **loop-free multiple routes** via **DAG of totally ordered heights** (unidirectional flow → no infinite loops). Operations: create / maintain / delete. Packets: **QUERY, UPDATE, CLEAR**.

**Route creation:** no directed link + unset flag → broadcast QUERY (dest ID), set flag. On QUERY: no downstream + unset → rebroadcast; no downstream + already set → discard; downstream with null height → set height, broadcast UPDATE; downstream with non-null height → timed UPDATE/QUERY rules as taught. On UPDATE with flag set: set height, unset flag, broadcast UPDATE.

**Five maintenance cases:** (1) generate new reference after losing last downstream; (2) propagate highest neighbour reference if no downstream; (3) reflect higher sub-level after link reversal with reflection bit; (4) partition detection when reference equals neighbours’ → set height null; (5) new reference when failure occurs between propagation and reflection.

**Route deletion:** CLEAR after partition (case 4); matching reference nulls neighbour heights and rebroadcasts until partitioned portion heights are null and invalid routes erased.

### How to answer
- Define routing protocol role and compare reactive / proactive / hybrid trade-offs.
- Explain AODV RREQ/RREP/RERR, expanding ring, sequence numbers, and the 1→3 via 2/4 story.
- List the three RERR circumstances and precursor lists.
- Describe OLSR MPRs, Hello sensing, TC messages, Dijkstra.
- Describe TORA DAG heights, QUERY/UPDATE/CLEAR, and summarize five maintenance cases + CLEAR deletion.

---

## M42: 3G Network and Security

### In one line
3G (IMT-2000) delivers ≥200 kbps mobile broadband via a RAN+dual-core architecture over ATM, with mutual authentication improvements but significant remaining threats classified in ETSI TS 121 133.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| IMT-2000 | ITU name for the 3G family of technical specifications (spectrum ~400 MHz–3 GHz allocated). |
| EDGE / EGPRS | Enhanced GPRS (“GPRS on steroids”) step before 3G; 3G still needs new frequencies and new infrastructure. |
| RAN / Node B / RNC | Radio Access Network; Node B ≈ 2G BTS; RNC ≈ BSC (radio resource management, handover). |
| SGSN / GGSN / MSC / CGF | Packet core (as in GPRS), circuit MSC for voice, Charging Gateway Function. |
| Iu / Iub / Iur | ATM RAN interfaces; Iu split CS (**AAL2** voice) and PS (**AAL5** IP-over-ATM data). |
| KASUMI | 3G block cipher replacing GSM’s A5/1; lecture notes serious weaknesses remain. |
| IMSI / TMSI | Permanent subscriber identity; temporary identity — IMSI is sent in clear when allocating TMSI. |
| False base station | Rogue BS that camps the user so they miss legitimate network paging. |
| ETSI TS 121 133 | Spec used to classify 3G threats: confidentiality, integrity, DoS, repudiation, unauthorized service access. |
| CIA | Confidentiality (no unauthorized disclosure), integrity (no unauthorized modification), availability (no unauthorized withholding). |

### Concepts explained

**History of 3G.** Result of ITU R&D from the early 1980s; specs developed over ~15 years and published as **IMT-2000**. Spectrum between **~400 MHz and 3 GHz** allocated for 3G.

| Event | Who / where |
|-------|-------------|
| First pre-commercial 3G | **NTT DoCoMo**, Japan, **1998** (branded **FOMA**) |
| First European pre-commercial UMTS | **Manx Telecom**, Isle of Man |
| First commercial “live” | **SK Telecom**, South Korea — **CDMA2000 1x EV-DO** |
| First commercial US 3G | **Monet Mobile Networks** — CDMA2000 1x EV-DO |
| Southern-hemisphere pre-commercial | **m.Net**, Adelaide, Feb 2002 — UMTS on **2100 MHz** |
| First 3G in Africa | **MTN**, 11 Dec 2008 |
| India | Government **MTNL** in Delhi then Mumbai; **BSNL** from **22 Feb 2009** Chennai then nationwide |

Before 3G: transition **GPRS → EDGE / EGPRS** (“GPRS on steroids”); MMS boomed and mobile Internet took off. 3G is a direct capability upgrade to EDGE but runs on a **wholly different set of frequencies**—**entirely new infrastructure** must be deployed.

**What 3G is.** Third generation of wireless mobile telecommunications: standards for devices, user services, and networks complying with **IMT-2000**. In user terms: faster Internet from a mobile—video calls while travelling; send images, videos, email as fast as from a desktop; online real-time connectivity and immediate location-specified on-demand information. Applications named: wireless voice telephony, mobile Internet, fixed wireless Internet, video calls, mobile TV. Framed as evolution of **GSM** standards. Supports ≥**200 kbps**; later **3.5G / 3.75G** provide several Mbit/s to smartphones and laptop modems. Beyond 3G the lecture previewed seamless mobility and **4G** broadband at home/office/on the move.

**Capabilities:** high-speed data; symmetrical and asymmetrical data; improved voice quality; greater capacity; multiple simultaneous services; global roaming; improved security; service flexibility. **Applications listed:** wireless Internet; audio on demand; electronic postcards; video conferencing; secure mobile-commerce; traffic and travelling information; location-specified 3G services. **Services:** wide-bandwidth messaging/email/video/web browsing; location-specific info (stores, restaurants, gas, free parking); business users get direct access to company networks while travelling. Marketing task: identifying, designing, and pricing these services.

**User services detail**
- **Mobile Internet:** merge cellular and Internet so handhelds reach all Internet services. 2G mainly voice-centric with low data; 2.5G/3G raise speeds. In 3G, data speed **depends on how many users access the network at the same time**.
- **Email:** number-one preferred mobile service in Sweden 2001 (then banking, encyclopedia). Categories: web-style **HTML** email vs **plain-text**. Cheap/asynchronous, but **spam** and the **first mobile virus** (BBC News 2003 cited) may slow adoption.
- **Messaging:** SMS and MMS expected as most utilized; step from text to pictures/video. Europe had not widely adopted MMS (pricing/complexity) vs Asians averaging **20–30 MMS/month** vs **1–2** for a typical European. **IM** popular among youngsters: near-real-time text/HTML/pictures/songs/video plus a **presence** service showing who is available.

**3G architecture.** Consists of a **radio access network (RAN)** and a **core network**.
- **Core packet-switched domain:** **3G SGSN** and **GGSN** (same functionality as in GPRS).
- **Core circuit-switched domain:** **3G MSC** for voice calls.
- **Charging Gateway Function (CGF)** for services and access.
- RAN functionality is **independent** of the core; either core domain can access any appropriate RAN service (e.g. a speech radio access bearer from the packet domain).
- **RAN elements:** **Node B** (≈ 2G BTS); **Radio Network Controller (RNC)** replaces BSC—radio resource management, handover control, support for both CS and PS domains.
- Interconnection uses **Iu, Iub, Iur** based on **ATM** as layer-2 switching. Data from the terminal over IP uses ATM with QoS; voice is embedded into ATM from the edge (Node B) and transported over ATM out of the RNC. **Iu** split into CS and PS parts: voice on VCs using **AAL2**; IP over ATM for data using **AAL5**—switched independently to 3G SGSN (data) or 3G MSC (voice).

**Effect of 4G on 3G (India-focused).** Reliance Jio 4G called the largest investment in Indian history. Operators had invested significantly in 3G network and spectrum **2010–2015**; slow 3G uptake meant investment not yet recovered. Some operators consider shutting 3G to simplify architecture (happening where 3G had run ~15 years). Developing countries such as Indonesia and Thailand still focused on 3G even after launching 4G. India similar until 2015: five years after launch, **3G penetration <10%**. Key reason: smartphones and 3G data pricing both expensive—figures: **300 million** Internet users, **180 million** with smartphones, only **90 million** bought 3G plans.

**Network security (general, then 3G).** Policies and practices to prevent and monitor unauthorized access, misuse, modification, or denial of a computer network and network-accessible resources. Access authorized/controlled by a network administrator via ID/password (or other authenticators). Covers public and private networks. CIA:

| Element | Meaning |
|---------|---------|
| Confidentiality | Prevent unauthorized **disclosure** of information (including about resources) |
| Integrity | Prevent unauthorized **modification**; maintain status quo of resources/information/personnel |
| Availability | Prevent unauthorized **withholding** of resources from those who need them when they need them |

Contemporary exposures named: government surveillance of mobiles; flaws in authentication protocols making Wi-Fi easy to pierce; malware controlling VIP communications from a PC.

**3G-specific security.** Claims **greater security** with **mutual authentication between terminals and networks**. As 3G grows, the mobile plays a PC-like role—attackers can spy on movements, listen to calls, read messages, access private data; generation brings a vast number of vulnerabilities (“heaven for hackers”); few consumers aware; each operator may need to spend **5–10% of its gain** securing 3G; new solutions needed at service-provider and handset-manufacturer levels. Cryptography: **KASUMI block cipher** instead of older **A5/1 stream cipher**, but several serious weaknesses identified in KASUMI. Main problems listed: **IMSI sent in clear text** when allocating TMSI; IMSI transmission unprotected—**IMSI is not a security feature**; user can be enticed to camp on a **false base station**, then out of reach of serving-network paging; **hijacking outgoing/incoming calls** possible when encryption is disabled—intruder as man-in-the-middle drops the user once the call is set up.

**ETSI TS 121 133 threat classification**
- **Unauthorized access to sensitive data (confidentiality):** eavesdropping; masquerading; traffic analysis (time/rate/length/source/destination → location or business transaction); browsing; leakage (via processes with legitimate access); inference (observe system reaction to queries/radio messages).
- **Unauthorized manipulation (integrity):** messages deliberately modified, inserted, replayed, or deleted.
- **Disturbing/misusing services (DoS / reduced availability):** intervention (jamming traffic/signalling/control); resource exhaustion (overload); misuse of privileges; abuse of services to gain advantage or disrupt.
- **Repudiation** — user or network denies actions that took place.
- **Unauthorized access to services** — masquerading as users/network entities, or misuse of access rights.

### How to answer
- Define 3G as IMT-2000 ≥200 kbps needing new spectrum/infra after EDGE.
- Sketch RAN (Node B, RNC) + CS/PS core (MSC, SGSN/GGSN, CGF) over ATM AAL2/AAL5.
- List key services (mobile Internet, email types, SMS/MMS/IM+presence, location).
- State mutual auth improvement plus IMSI cleartext, false BS, optional encryption, KASUMI weaknesses.
- Outline ETSI TS 121 133 threat groups under CIA + repudiation + service access.

---

## M43: 4G LTE

### In one line
LTE is 3GPP’s IP-based Long Term Evolution of the GSM/UMTS path to ~10× 3G speeds via OFDM and a simplified E-UTRAN, distinct from marketing “4G” HSPA, with VoLTE/RCS benefits and a CIA-focused security research framing.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| LTE | Long Term Evolution — 3GPP 4G wireless standard on the GSM → UMTS evolutionary path. |
| LTE Advanced | 3GPP **Release 10**, taught as the release that qualifies as 4G. |
| E-UTRAN | Simplified LTE radio architecture: **no RNC**, **no CS domain**, **no DCH**. |
| HSPA | High Speed Packet Access — often branded “4G” without LTE; faster 3G GSM, slower than LTE. |
| OFDM | Orthogonal frequency-division multiplexing — packs more data on RF, reduces latency and interference. |
| VoLTE | Voice over LTE — IP voice (and related media) on the 4G LTE data network. |
| RCS | Rich Communication Services (video call, file transfer, translation, video VM, IM) from the native dialer. |
| WiMAX / 802.16m | Competing 4G path (WirelessMAN-Advanced / WiMAX 2). |
| UMB | Ultra Mobile Broadband — another competing 4G candidate. |

### Concepts explained

**Goals.** LTE applies to improving wireless broadband speeds under rising demand. Increase capacity/speed with new **DSP** techniques and modulations (~**10× 3G** for smartphones, tablets, notebooks, wireless hotspots). Further goal: redesign and simplify network architecture to an **IP-based** system with significantly reduced transfer latency versus 3G.

**Generation path taught**

| Step | Placement |
|------|-----------|
| 1973 | First call by engineer **Martin Cooper** (Motorola) |
| 1G | **AMPS** — Advanced Mobile Phone System |
| 2G | **GSM** and **CDMA** |
| 3G | **UMTS** and **EV-DO** |
| 4G | **LTE** (3GPP) and **IEEE 802.16m** (WirelessMAN-Advanced / WiMAX 2) |

Competing 4G candidates also include **UMB**. LTE progresses through releases; **Release 10 / LTE Advanced** is taught as qualifying as 4G. Era context: Verizon/AT&T launching 4G LTE; Sprint on WiMAX; Android LTE phones; iPhone 5 / iPad 3 expected LTE. Vertical example: **Intuit GoPayment**—street vendors attach a small card reader to a phone/tablet. With large-scale VoLTE and LTE Advanced ahead, the instructor asked what the next forty years might hold.

**Technical objectives:** user throughput (DL/UL); downlink and uplink capacity; latency—user-plane transition **<5 ms** in ideal conditions, control-plane **100 ms**, fast connection setup; simplified architecture—simpler **E-UTRAN**, **no RNC**, **no CS domain**, **no DCH**; mobility optimized for low speed but supporting **120 km/h**.

**4G vs LTE vs “4G without LTE.”** 4G technologies provide IP-based voice, data, and multimedia streaming at least megabits/s and up to **~1 Gbit/s**. **Is LTE the same as 4G? No.** There is 4G, and there is **4G LTE**—taught as the **purest form of 4G**. If a provider says “4G” **without mentioning LTE**, they are probably talking about **HSPA**: a faster version of 3G GSM, still faster than 3G but **not as fast as LTE**. Most 4G / “true 4G” nets have nearly identical upload and download speeds; LTE is described as the fastest wireless connection then available.

**Two resources required:** (1) a **network** that can support the speeds; (2) a **device** able to connect and download fast enough. A phone with 4G LTE inside does **not** guarantee those speeds—like buying a car that can do 200 mph but driving on a 55 mph freeway.

**Why faster; rates; compatibility.** **OFDM** squeezes more data onto the same RF and reduces latency/interference. 4G uses **different frequencies** than 3G → handset needs a supporting modem. Peak rates taught: potential **100 Mbit/s downstream** and **30 Mbit/s upstream**; reduced latency; scalable bandwidth capacity; backwards compatibility with existing **GSM and UMTS**. Also said to assure interoperability with **WCDMA, HSPA, CDMA, TD-SCDMA**. Advantages: low latency, high throughput, increased data-transfer speed, more cost-effectiveness, improvements over 3G. Devices: phones, laptops, cameras, camcorders. Disadvantages: customers must buy new equipment; then only accessible in certain cities; needs complex hardware.

**VoLTE / HD voice / RCS / VoWiFi**
- VoLTE lets carriers use **IP-based 4G LTE data networks for voice**—WhatsApp-like call, video, conferencing.
- Most noticeable benefit: improved voice quality. Traditional voice ~**8 kbps** codec; Verizon described using **13 kbps** with more modern compression.
- **RCS** (standards-based, enabled by VoLTE): video calling, file transfer, real-time language translation, video voicemail, IM—many exist as OTT (**FaceTime, Skype, Google Translate**); VoLTE launches them from the **native dialer**.
- Faster call setup than older circuit-switched 2G.
- **Signals Research Group:** VoLTE much better battery life than OTT VoIP such as Skype; consistently higher call quality than CS voice and OTT; far lower network consumption than a Skype voice call.
- Integration with **Voice over Wi-Fi**: same call-setup path as VoLTE eases offering VoWiFi where licensed spectrum is weak/unavailable; improves indoor coverage.
- True device interoperability: once VoLTE works across carriers, the **CDMA/GSM divide** among major US operators need no longer matter if the device supports enough LTE bands—voice and data all on the same 4G LTE technology.

**Security of 4G LTE (as framed):** “LTE security” as defence versus Internet threats from multiple attack types. Essential Next-Gen points: **confidentiality** (right people get right data) and **integrity** (message from A to B did not change). More powerful security to be achieved by discovering main factors to compare LTE cryptographic algorithms; finding trends/weaknesses of each; evaluating which provides higher security; proposing an algorithm from the existing LTE set that may enhance security—not a finished protocol walkthrough in this lecture.

**Brief 5G forward look in this lecture:** fifth generation aimed beyond 2020; much faster than 4G (**20 GB per second** wording—fast enough to download HD movies in seconds); expected to drive IoT, smart cities, Digital India, and a 2020 vision associated with A.P.J. Abdul Kalam.

### How to answer
- Define LTE as 3GPP Long Term Evolution on GSM/UMTS path; name Release 10 LTE Advanced.
- State IP redesign, OFDM ~10× speed, E-UTRAN simplifications, latency targets.
- Separate marketing 4G (HSPA) from 4G LTE; require both network and device.
- Explain VoLTE benefits: HD codec, RCS, setup, battery vs OTT, VoWiFi, interoperability.
- Summarize security as CIA plus comparative crypto-algorithm research goals.

---

## M44: 5G

### In one line
5G is fifth-generation all-IP mobile broadband (as taught, also linked to IEEE 802.11ac) with multi-RAT terminals, NGMN ~1 ms latency targets, mmWave/small-cell capacity, and unfinished security/privacy work.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| 5G | Fifth-generation mobile/wireless systems; lecture also ties it to IEEE 802.11ac / ~5 GHz signal and builds on 4G LTE. |
| NGMN Alliance | Body defining 5G requirements for rates, massive connections, spectral/signalling efficiency, coverage, ~1 ms latency. |
| RAT | Radio Access Technology; each appears as an IP link; multiple interfaces active at once. |
| MIMO | Multiple-input multiple-output antennas used to boost shorter-range higher-frequency signals. |
| Millimetre wave | Very high bands taught as ~3–300 GHz: high rate, little AM/FM/TV coexistence, poor through walls → dense small cells. |
| IPv6 (5G vision) | Addressing for mobile IP tied to connected network and geography. |
| Nanocore | Speculative future enhancement combining with AI (robot control, brain-to-type ideas); 6G buzz noted. |

### Concepts explained

**Generations as told.** The **G** stands for Generation: **1G** early 1990s voice; **2G** text messages; **3G** calls, texts, Internet browsing; **4G** enhanced 3G—browse/text/call plus download/upload large video. After 4G, companies added **LTE**; with 4G connectivity LTE became the fastest and most consistent variety versus competing technologies like **WiMAX**. WiMAX and LTE achieved similar outcomes, but a single standard mattered; **LTE makes 4G faster**. 5G provides better speeds and coverage than 4G; lecture states it works with a **5 GHz signal** and offers up to **1 Gbit/s for tens of connections** or **tens of Mbit/s for tens of thousands**; builds on 4G LTE with speed that makes **Ultra HD and 3D** easy.

**NGMN Alliance requirements** a 5G standard should fulfil:
- Data rates of **tens of Mbit/s for tens of thousands of users**
- **100 Mbit/s** for metropolitan areas
- **1 Gbit/s simultaneously** to many workers on the same office floor
- Several hundreds of thousands of simultaneous connections for a **massive wireless sensor network**
- Spectral efficiency significantly enhanced vs 4G; coverage improved; signalling efficiency enhanced
- **1 millisecond latency** (or less—“virtually zero”); smart communication; latency reduced significantly vs LTE

**Design of 5G mobile network architecture.** Proposed model is an **all-IP** architecture for wireless and mobile-network interoperability. System = **user terminal** (crucial role) + a number of **independent, autonomous RATs**. Within each terminal, each RAT is seen as an **IP link** to the outside Internet. There must be a **different radio interface for each RAT**. Example: access to four RATs requires **four different access-specific interfaces, all active at the same time**, for the architecture to be functional.

**Concepts for 5G mobile networks:** terminals will have **software-defined radios** and modulation schemes plus **new error-control schemes downloadable from the Internet**; development focus is toward the user terminal; terminals access different wireless technologies at the same time and should **combine different flows**; **vertical handovers should be avoided** (not feasible with many technologies/operators/providers); **each network handles user mobility**; the **terminal makes the final choice** among access-network providers for a given service based on **open intelligent middleware** in the phone.

**Is 5G really faster?** Yes—“much faster.” 4G LTE tops about **1 Gbit/s** (about an hour for a short HD movie in perfect conditions); people rarely see the maximum because of buildings, microwaves, other Wi-Fi. 5G said to increase downloads up to **~10 Gbit/s** (full HD movie in seconds) and reduce latency significantly; path to thousands of connected devices in homes/offices. Average home 4G **25–40 Mbps** vs 5G likely **>500 Mbps**; many entities believe **1 Gbit/s mobile to 10 simultaneous connections**; Huawei expects at least **100×** the then-fastest 4G LTE. Capacity: current 4G may promise ~150 Mbit/s on the go but leave inclusive allowances under 5 GB; 5G expected **upwards of 1,000× the capacity of 4G** → greater data allowances. Latency example: 4G speed test **49 ms**; Huawei targeting **<1 ms** vs **>50 ms on 4G**—video starts when you hit play; also helps games, automated equipment, IoT, AR (Oculus Rift, Gear VR, HoloLens).

**How cellular radio works; spectrum.** Phones are two-way radios: voice → electrical signal → radio waves to nearest cell site → network of cells. New technologies take higher unused frequencies (move information faster) but **do not travel as far**. 4G occupied bands up to **~20 MHz**; 5G will likely use up to **~6 GHz**. **MIMO** will probably boost signals. UK 4G context: LTE on **800 MHz, 1800 MHz, 2.6 GHz** (1800 repurposed by EE/Three; other bands from 2012 auction). Huawei: combine **new RAT** with existing LTE, HSPA, GSM, Wi-Fi. Samsung/NYU discussed **millimetre-wave** (taught **3–300 GHz**): scarcely used by AM/FM/TV → greater speeds/more data; downside—do not pass through solids well, hard over long distances → **lots of smaller base stations**. All 5G standards expected to use small-cell approach for maximum capacity and minimal latency; coverage may bounce off solid surfaces. **No universal agreed standard** yet; launch may see a variety under the 5G banner (like LTE and WiMAX under 4G). Cadence taught: new telecom standard ~every 10 years (2G 1991, 3G 2001, 4G 2012, 5G expected **2020 or 2022**). Industry framing: more sustainable operator investment; SMS was underestimated, video calling overestimated; regulators can stimulate investment; some 3G/4G business cases may not fit 5G.

**Benefits:** businesses—capacity/speed for mobile working and video-conference from any location; consumers—e.g. download a film to a smartphone in under a second; capacity, latency, coverage gains as above.

**Requirements list taught:** better coverage area and high data rate at cell edge; low battery consumption / longer battery life; multiple data-transfer paths; around 1 Gbit/s easily possible; more security; good energy and spectral efficiency; worldwide coverage; about **90% reduction in network energy usage**.

**Applications:** network availability everywhere; world as a “real Wi-Fi zone”; **mobile IP address** via **IPv6** depending on connected network and geographical position; unified global standards; receive radio signals even at higher altitude.

**Disadvantages:** research still going on; speed claims seem difficult because of other devices and uneven technology worldwide; many old devices must be replaced (cost); developing infrastructure increases cost; **security and privacy issues yet to be solved**. Future span: **nanocore** with AI (control intelligent robot from mobile; mobile that types what the brain thinks); Google Hot Trends rated **6G** highly searched; closing “that’s all for 5G technology.”

### How to answer
- Define 5G and list NGMN rate/connection/latency (~1 ms) targets.
- Describe all-IP multi-RAT terminal-centric architecture (SDR, middleware choice, no vertical HO).
- Contrast with 4G on speed, ~1000× capacity, latency, mmWave vs lower bands, MIMO, small cells.
- Give benefits (IoT/AR/film download/data plans) and disadvantages (cost, unfinished security/privacy).
- Mention IPv6 addressing vision and that no universal standard existed at lecture time.

---

## M45: VoIP Protocols

### In one line
VoIP packetizes digital voice over IP instead of circuit TDM, using codecs plus H.323/SIP/MGCP signalling and RTP, trading TDM cost for QoS and security challenges such as SPIT and toll fraud.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| VoIP | Voice over Internet Protocol — analog audio digitized and sent as packets over IP instead of circuit-switched TDM. |
| H.323 | Comprehensive ITU-T umbrella for voice/video/data (H.225, H.235, H.245, H.450) with RTP/RTCP over UDP and TLS call setup. |
| SIP | Session Initiation Protocol (IETF RFC 3261) — text request/response signalling; depends on TLS/IPsec because proxies must see routing headers. |
| MGCP | Media Gateway Control Protocol (RFC 3435) — gateway control; IPsec AH/ESP between media gateway and media gateway controller. |
| G.711 / G.729 / G.723 | Example voice codecs on the send path. |
| Playout buffer | Receiver jitter buffer; queues packets then plays; late packets are discarded. |
| SPIT | Spam over Internet Telephony — real-time recorded/self-dialed voice spam; needs real-time defence. |
| Toll fraud | Unauthorized use of paid voice service for gain, often via signalling abuse or misconfiguration. |
| PSTN | Public Switched Telephone Network — still required for number translation and non-VoIP users. |

### Concepts explained

**What VoIP is.** Takes analog telephone audio, digitizes it, and transmits packets over the Internet. Methodology/technologies for voice and multimedia sessions over IP networks—**IP rather than traditional circuit transmission**. Defined in ITU-T H.32x recommendations and (as spoken) RFC 2543 for early SIP; SIP later given as **RFC 3261**.

**Why VoIP despite IP weaknesses.** IP delivers digitized-voice packets but was **not designed for realtime** voice/video. IP is **connectionless**: no virtual connection before transmission; **no guarantees** of reliability, flow control, error detection, or correction; packets may be out-of-sequence or lost. Voice needs a guaranteed connection and reasonable delay. VoIP still succeeds partly due to the **high cost of circuit-switched TDM**; packet switching makes the network transparent to upper voice layers; existing IP nets allow **voice–data integration**. Vendors developed higher-layer protocols for guaranteed connection/transmission. VoIP follows a layered model comparable to OSI—manageable and flexible; changes in one layer have minimal impact on others.

**Signalling protocols.** The two most generally used are **ITU-T H.323** and **IETF SIP** (discover, maintain, terminate calls). Additionally **MGCP** signals/manages between VoIP gateways and traditional **PSTN** gateways.

| Protocol | Role / security as taught |
|----------|---------------------------|
| **H.323** | Comprehensive for voice/video/data. **H.225** call setup/teardown; **H.245** media methods and parameter (capability) negotiation; **H.450** supplementary services (e.g. hold); **H.235** protection framework (authentication, integrity, privacy, some non-repudiation) designed to work with H.245/H.225. Call setup secured through **TLS**; then encryption/media-channel negotiation. Transport **RTP/RTCP over UDP**; encryption within RTP by third-party hardware or at network layer. Auth: **symmetric** via **Diffie–Hellman** (no prior contact) **or** subscription-based prior shared secret—password+symmetric, password+hashing, or certificate+signatures (per H.235). |
| **SIP** | Text-based application-layer RFC 3261 request–response. Auth/authorization via lower-layer scheme or per-request challenge–response. **Lightweight**; own security capabilities **very limited**. Requests/responses **cannot be fully end-to-end encrypted** because request/routing fields must be **visible to proxies**. Voice often clear text over UDP. S/MIME can encrypt some content, but certain header fields cannot → depends on **TLS or IPsec for the entire message**. |
| **MGCP** | RFC 3435; expects secure IP as in IPsec architecture (RFC 2401) using **AH (RFC 2402)** or **ESP (RFC 2406)** between the **media gateway** (circuit↔packet conversion) and **media gateway controller** (service logic): connectionless integrity, origin authentication, optional anti-replay. |

**Processing path.** Sender: analog → digital, compress/format with codec (**G.711, G.729, G.723**, etc.) → equal-sized packets → attach **RTP, UDP, IP**, plus link-layer header → send. Receiver: depacketize/decode; **playout buffer** smooths jitter (introduces delay); packets later than playout deadline are **discarded**. Signalling (SIP/H.323) sets up new IP calls and closes media streams.

**QoS** = degree of user satisfaction.

| Factor | Meaning |
|--------|---------|
| Delay | Time from speaking until hearing; categories: **source**, **receiver**, **network** |
| Jitter | Variation in transmission delay; harms voice quality |
| Packet loss | Lost, corrupted, or late (discarded at playout or on buffer overflow); retransmit adds more delay |
| Echo | Caller hears reflection of own voice; **electrical** in PSTN; **acoustic** is the VoIP difficulty |
| Throughput | Max bits received out of bits sent in an interval |

**Threat classes (classification only—not recipes)**
- **DoS:** flood that reduces available IPs/DHCP/router functions or blocks a server; VoIP DoS overloads call-processing with so many simultaneous requests that authorized users are denied; can hit any network component.
- **Network sniffing:** observe traffic patterns on a shared medium.
- **Eavesdropping:** collect signalling/media to prepare attacks or gain intelligence; vendor call-manager issues cited (listen/forward calls, unauthorized access).
- **Spoofing / caller-ID spoofing:** masquerade as licensed user; display looks authentic → VoIP phishing for sensitive info.
- **Toll fraud:** unauthorized access for financial gain—among most critical for providers; manipulated signalling or misconfigured charging; open dial-plan/test/remote-access lines; resell after compromise; large-org theft may go unnoticed while bills accumulate.
- **SPIT:** lower cost attracts spammers vs PSTN; recorded self-dialed calls; **more severe than email spam** (assaultive; needs real-time defence); fake ID to harvest account numbers, SSN, security answers.

**Defences taught:** DoS—monitor/filter suspicious users, authenticate before forwarding, prefer **stateless proxies** (less memory-exhaustion risk; can filter spam sources), size servers as first line; eavesdropping—authorized wiring-closet access, port-based MAC security, scan unauthorized modes, encrypt VoIP; spoofing—effective authentication + encryption; toll fraud—powerful firewalls and protected ports; SPIT—blacklist source IPs, vendor tools flagging suspicious callers, receivers must not disclose important info to unknowns.

**Deployment options:** USB adapters for standard analog phones; softphones (PC + headset/sound card; often free with provider); dedicated VoIP phones/base stations (possibly WLAN); dedicated routers on ADSL/cable that still route for a PC and work independent of PC software; wireless compatibility on mobiles if WLAN installed (needs firewall/encryption). Wireless VoIP issues (mainly corporate): scalability; QoS poorer than wired; higher setup/maintenance cost (many APs); higher security threat.

**Limitations:** QoS (IP designed for ordered error-free data—prioritize voice); interoperability with PSTN signalling via H.323/SIP/MGCP; security on Internet backbone (interception, DoS, fraud)—tunnelling such as **L2TP** and **SSL** encryption cited but **encryption not widely available for VoIP**; integration with PSTN so they appear as one network (VoIP number has IP address translated to telephone number); **scalability** is the main obstacle as users grow.

### How to answer
- Define VoIP vs TDM and explain why IP alone is a poor realtime transport.
- Compare H.323, SIP, and MGCP including security dependencies (TLS/IPsec, H.235 variants).
- Trace codec → RTP/UDP/IP → playout buffer path.
- List QoS factors (delay, jitter, loss, echo types, throughput).
- Name threat classes (DoS, sniff, eavesdrop, spoof, toll fraud, SPIT) and matching defences—not attack recipes.

---

## M46: Introduction to DDoS

### In one line
DoS/DDoS attacks target availability by flooding or exploiting weaknesses; DDoS amplifies impact via many bots, exploiting Internet design flaws and classifying into physical, volumetric, and application-layer types.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| DoS | Denial of Service — explicit attempt to prevent legitimate users from using a service (hits **availability** in CIA). |
| DDoS | Distributed DoS — attack traffic from **many sources**, amplifying power and complicating defence. |
| Bot / botnet | Compromised machines (masters/handlers/zombies) used as a distributed attack network. |
| IP spoofing | Forged source addresses that hide origin and defeat simple identity-by-IP defences. |
| SYN flooding | Volumetric class abusing TCP three-way handshake so servers hold many **half-open** connections until timeout. |
| Volumetric attack | Layers 2–4 congestion / bandwidth exhaustion with high packet volume. |
| Application-layer DDoS | Layers 5–7: low network volume but high application/request load (e.g. HTTP GET/POST floods). |
| Ping of Death | Named vulnerability class: oversized ICMP mishandled by some OSes (buffer overflow → crash); patchable. |
| CIA | Confidentiality, integrity, availability — DDoS primarily targets availability. |

### Concepts explained

**Why availability mattered late.** Internet usage grew; lives depend on it for information, business, commerce, communication, education, entertainment, research. Original goal was **unobstructed flow and scalability without keeping security in mind**—now precarious. Simple architectural design eased usage but fascinated attackers. Threats can hit the **CIA** model; **availability** is primarily targeted by DoS: an **explicit attempt to prevent legitimate users from using a service**.

DoS has overtaken other concerns as arguably the most severe attack form of the last decade. Example: a reputed shopping site suddenly unavailable under a flood of packets. Traditionally the security community focused on unauthorized disclosure/modification and theft of services; DoS was largely ignored as unlikely because “characters would not gain anything.” That is **not the case today**: DoS can put merchants out of business, cause major visible disruption, be used from grudge or paid attack, or be used by terrorists against critical infrastructure. A DoS may flood a network, disrupt connections between two machines, or disrupt service to a specific system/person so legitimate traffic never reaches the server/site; it can target OSes or network services.

**Two high-level DoS forms (classification, not a playbook):**
1. **Vulnerability / crafted-packet DoS** — crash a system by exploiting software vulnerabilities (named class: **Ping of Death**—oversized ICMP that some OSes mishandled via buffer overflow → crash/freeze/reboot). Instructor: this form can be **prevented by patching**.
2. **Flooding DoS** — massive volumes of useless traffic occupy resources that would have served legitimate traffic. **Cannot be easily prevented**; targets can be attacked simply because they are connected to the **public Internet**.

**DoS vs DDoS.** When attack traffic comes from **multiple sources**, it is **DDoS**—amplifies power and makes defence much more complicated. Both are huge threats; DDoS is more complex because: it can use a very large number of machines—**any target, however well provisioned, can be taken offline**; gathering an “army” is simple via automated tools that need little sophistication; acting against e.g. 1,000 hosts is hard; some DDoS uses **seemingly legitimate traffic** with **no distinguishing feature**, so response without also disturbing legitimate activity is extremely hard.

**Botnet architecture.** OSes and protocols were developed without security engineering, leaving insecure unpatched machines. Attackers implant programs; depending on sophistication, compromised machines are **masters, handlers, or zombies** (collectively **bots**); the attack network is a **botnet**. Control instructions go to masters → zombies; zombies send packets that converge at the victim/network to exhaust **communication or computational** resources. Incidents common against clients, businesses, ISPs, and companies such as **Yahoo, Twitter, Facebook, eBay, Google**. Attack sizes taught: **<10 Gbps** before 2005; about **100 Gbps** in 2010; up to **400 Gbps** in 2014. Vast majority of attacks are **not reported**.

**Motives**

| Motive | As taught |
|--------|-----------|
| Recognition | Early proofs of concept/pranks; taking a popular site offline brings underground recognition |
| Ideological activism | Political disagreement with org, media, corporation, or government |
| Financial gain | May demand **ransom** to prevent further attacks; described as most experienced |
| Vandalism | Destroy resources; “don’t believe in anything”; reports of increase |
| Revenge / competitive spirit | Business revenge; possibly dishonoured employees |

**Consequences** (depend on kind of attack, organisation, target; long-duration attacks more rigorous—mitigate quickly after detection): huge revenue losses; reputation damage; loss of shareholder confidence; customer dissatisfaction; loss of important data due to system crashes; extra operational cost → social, financial, and legal effects.

**Vulnerabilities in basic protocols and architecture**
1. **Stateless nature of the Internet** — intermediate routers do not maintain state about forwarded packets → accountability/forensics difficult.
2. **Lack of authenticity** — users can claim others’ identities; common class **IP spoofing** (forged source addresses).
3. **Deterministic/predictable Internet protocols** — often needed for proper operation; TCP three-way handshake is predictable and can be abused as **SYN flooding**.
4. **Mimicking legitimate user behaviour** — leads to application-layer DoS hard to separate from real users.

**Classification of DDoS by OSI region** (may occur at every layer; figure grouped three classes)

| Class | Layers | What it is (types, not recipes) |
|-------|--------|----------------------------------|
| **Physical** | 1 | Concerned with physical security of nodes/hosts/switches/hubs/routers/servers/media. **Destruction of assets** (damage or cut LAN backbone)—prevent with physical security. **Jamming** (mainly WSN: noise so throughput falls; packets corrupted by interference). **Tampering** (erase programs/modify code; extract crypto keys from captured nodes)—keep packages tamper-proof. |
| **Volumetric** | 2–4 | Congestion by consuming bandwidth; traffic via distributed bots; most packets have **spoofed sources** (hinders traceback). **MAC flooding**—forged/cloned MACs exhaust switch memory / disturb ARP and router tables. **ICMP flooding**—spoofed query volume; replies consume bandwidth; fragmented ICMP overloads reassembly; related classes **Smurf**, **Ping of Death**. **TCP/SYN flooding**—incomplete handshakes leave half-open state until timeout; related fragmented-ACK examples. **UDP flooding**—connectionless volume; **echo** and **chargen** commonly abused; also DNS flood, UDP fragmentation, VoIP flood classes. |
| **Application** | 5–7 | **Low traffic at the network** but **large request load on the web server**. Named: **HTTP GET and POST** flooding; protocols exploited include HTTP, HTTPS, DNS, others. |

Closing: DoS/DDoS is devastating; many commercial solutions exist, but an **ideal solution is still elusive**.

### How to answer
- Place DoS/DDoS under CIA availability; contrast single-source vs many-source.
- Distinguish patchable vulnerability DoS from public-Internet flooding.
- List motives and organisational consequences briefly.
- Name four architectural weaknesses (stateless, spoofing, predictable TCP, mimicry).
- Classify physical / volumetric / application-layer with named flood **types** only—no procedures.

---

## M47: Defence to DDoS Attacks

### In one line
DDoS flooding is hard to stop because of easy tools, spoofed legitimate-looking volume, many zombies, and Internet hubs; ideal defence needs prevention, anomaly detection, source identification, and low-collateral reaction plus basic hardening.

### Definitions (write these)
| Term | Meaning (answer-ready) |
|------|------------------------|
| IP spoofing (defence view) | Makes new legitimate clients indistinguishable from attack initiators, defeating IP-based resource sharing. |
| Collateral damage | Legitimate traffic dropped or delayed by a defence while fighting an attack. |
| False positive | Defence treats a non-attack (e.g. flash crowd) as DDoS and triggers costly filtering. |
| Flash event | Sudden legitimate load that must be clearly distinguished from DoS. |
| SYN cookies | Example partial preventive for SYN floods; incomplete unless combined with other mechanisms. |
| Anomaly-based detection | Preferred DDoS detector; signature-based detection fails because signatures change constantly. |
| Source identification | Locating origins even when packet source addresses are forged. |
| PlanetLab / Emulab | Named research testbeds; small-scale tests alone are not credible for DDoS claims. |
| Tripwire | Example integrity tool for detecting changes to configuration and other files. |

### Concepts explained

**Why flooding is hard (the “perfect crime”).** Flooding DoS/DDoS is effective for attackers and extremely hard to defend:
- **Easy launch tools** automate agent recruitment even for novices (existence of tools is a defence challenge—the lecture does **not** teach their use).
- **Traffic resembles legitimate flows** and can vary contents/headers (unlike worms/intrusions needing crafted packets) → filtering is extremely hard.
- **IP spoofing** defeats per-IP resource sharing; ongoing sessions with known users might be told apart, but the victim **cannot distinguish new legitimate requests from attack ones**, so **no new users can be served**.
- **Huge volume** overwhelms the target and allows only simple per-packet processing.
- **Many zombies** overwhelm large nets, vary attacks via subsets/few packets each, and defeat many traceback ideas; knowing 10,000 identities barely helps; the agent pool grows with Internet hosts and novice users; wide security deployment is unlikely under distributed Internet management.
- **Hub-and-spoke topology:** congesting a few well-connected hubs can grind the Internet to a halt.

Result: high impact, spoofed identity, too many bots to punish, little automated tracing → low attacker risk.

**Challenges of DDoS defence** fall into **technical** and **social** categories. Technical issues involve current Internet protocols and threat characteristics. Social issues concern how a technical solution is introduced, accepted, and widely deployed. Main problem in both: large-scale DDoS is a **distributed threat** needing overlapping solutions across the Internet, because attacking machines may be anywhere. Attack streams can be controlled only if there is a point of defence between agents and victims.

Two deployment sketches: (1) one defence close to the victim monitoring all incoming traffic—deficient mainly because it must efficiently handle huge volume; (2) distributed defence dividing workload—must be widespread to cover any agent–victim pair. Because widespread deployment cannot be granted, the technical challenge is defences that still work if **sparsely deployed**; the social challenge is an **economic model that motivates large-scale deployment**.

**Technical challenges:** need for **distributed response** at many Internet points (very few DDoS types can be handled only by the victim; Internet is administered in a distributed manner so cooperative deployment cannot be enforced—discourages researchers); **lack of detailed attack information** (reporting believed to damage reputation; incidents often only to government under secrecy; useful data = type, time/duration, number of agents if known, attempted response and effectiveness, damage suffered—**not** to be confused with publicly available attack-tool info); **lack of defence-system benchmarks** (vendors make bold claims; no standardized testing → cherry-picked tests; researchers cannot compare performance); **difficulty of large-scale testing** (need realistic environment; lack of large testbeds, safe live distributed experiments, or simulators for thousands of nodes; small-scale claims not credible; named testbeds **PlanetLab** and **Emulab**).

**Social challenges (deployment patterns many defences demand):** complete deployment at each host/router/network; continuous/neighbour deployment at directly connected hosts/routers; large-scale widespread deployment (majority of Internet hosts); complete deployment at a carefully selected set of points (all must deploy); modification of widely deployed protocols such as **TCP/IP or HTTP**.

**Goals of a strong DDoS defence**
1. **Effectiveness** — actually defend: effective prevention that makes attacks impossible, or effective reaction so the DoS effect goes away; reactive response should be sufficiently quick and automated that the target does not suffer seriously.
2. **Completeness** — handle all possible attacks or at least a large number (a mechanism that handles TCP SYN flooding but not a ping flood is less valuable than one that handles both). Example: **TCP SYN cookies** help but are **not sufficient unless coupled with other mechanisms**. Completeness also required in detection and reaction—if detection misses a pattern, no response is invoked. Extremely hard because attackers develop new types to bypass existing defence. **Flash events** need clear-cut distinction from DoS.
3. **Minimum collateral damage** — core goal is not merely to stop attack packets but to ensure legitimate users continue normal activity. Legitimate traffic may share sources, share the victim’s network as destination, share some Internet path, or share application protocol/destination port—**none** of these should be disrupted. In practice, imperfect characterization drops some legitimate traffic = collateral damage; especially serious with flash events.
4. **Low false-positive rates** — preventive mechanisms should not hurt other traffic; reactive mechanisms should activate only when an attack is underway. Detecting an attack when none is happening is a false positive → collateral damage plus CPU/memory/delay cost on all packets.
5. **Low deployment and operational cost** — cost commensurate with benefits. Commercial solutions have purchase and system-administration cost; signature systems need ongoing updates; stateful inspection may delay each packet; throttling suspicious sources may slow legitimate interactions. Unless costs are extremely low or rare, balance against degree of protection.

**Four defence modules**
1. **Attack prevention** — stop attacks before they reach the target. For DDoS that uses spoofed traffic, highlighted approach: **filter spoofed packets close to or at the attack sources**—taught as one of the **most effective** approaches for that subclass.
2. **Attack detection** — detect DDoS when it occurs to direct further action, based on traffic-feature distribution. **Signature-based detection is not applied** for DDoS because signatures change constantly; **anomaly-based detection** is suitable.
3. **Attack source identification** — locate sources regardless of whether the source-address field contains erroneous information; crucial to minimize damage and deter potential attackers.
4. **Attack reaction** — eliminate or curtail attack effects; final step determining overall defence performance; challenge is to filter attack traffic **without disturbing legitimate traffic**.

**Practical tips to reduce exposure** (administrative/hardening—not a complete DDoS solution)
1. Implement **router filters**—lessen exposure and help prevent users on your network from launching certain DoS attacks.
2. Install **patches** (when available) against TCP SYN flooding—substantially reduces exposure but may not eliminate risk entirely.
3. **Disable unused/unneeded network services**.
4. Enable **quota systems** (e.g. disk quotas for accounts running network services); partition the file system to separate critical functions if OS supports volumes.
5. Observe system performance and establish **baselines** for ordinary disk/CPU/network activity.
6. Routinely examine **physical security**: servers, routers, unattended terminals, network access points, wiring closets, environmental systems (air and power).
7. Use **Tripwire or similar** to detect changes in configuration or other files.
8. Invest in **redundant and fault-tolerant** network configurations.
9. Establish and maintain regular **backup** schedules/policies, particularly for important configuration information.
10. Establish and maintain appropriate **password policies**, especially for highly privileged accounts (Unix **root** or Windows **administrator**).

Closing: DDoS remains devastating; defence is still elusive despite many academic and commercial solutions—the market has **not** delivered a complete cure.

### How to answer
- Explain why flooding is hard: tools, similarity, spoofing, volume, zombies, hubs (“perfect crime”).
- Separate technical challenges (distributed response, missing data/benchmarks/testbeds) from social deployment economics.
- List ideal goals: effectiveness, completeness, low collateral, low false positives, low cost.
- Name the four modules: prevent (anti-spoof near sources) → anomaly-detect → identify → react carefully.
- Give hardening tips and state they reduce exposure but are not a full DDoS cure.

---

\newpage

