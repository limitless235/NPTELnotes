# Volume 01 — M00–M11

> Information Security (CEC) · SWAYAM / CEC Information Security
> **notes-3** — concept exam notes (definitions & what things do). Breadth over lab depth.

---

## M00: Introductory Video — Information Security

### Learning focus
- State why information security now spans individuals and enterprises.
- List the course's promised themes: web trust, DNS, HTTPS, client-side attacks, and secure coding.
- Explain the coordinator's claim that poor programming is the root cause of most information-security threats.
- Recall that this is a short, two-credit course on information and network security.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Security loophole | Organizational gap that lets an attacker break in and exploit a vulnerability |
| Authoritative DNS reply | Name-server answer that should be trusted when judging whether a site is genuine |
| HTTPS digital signature | Cryptographic check that the web server is the claimed site |
| DNS poisoning | Tampering with name resolution so users reach a fake host |
| Client-side attack | Compromise that succeeds because the user (browser) approaches a malicious site |
| Secure coding | The course's stated end-goal: stop shipping the vulnerabilities that attacks exploit |

### Exam lines
- Security is ambient: individual and enterprise alike.
- Trust on the web is technical (DNS + HTTPS), not visual.
- Poor programming, especially copy-paste reuse, is framed as the root cause of threats.
- Client-side attacks are hard to stop once the user cooperates with the attacker.
- The two-credit course aims at network, OS, database, DNS, and secure-coding competence.


---

## M01: Information Security

### Learning focus
- Define ethics and contrast consequentialism with deontology as approaches to right and wrong.
- Distinguish system security from information (data) security and state the CIA triad.
- Relate computer-security breaches and overly protective measures to rights, harms, and interests.
- Contrast hacking vs cracking, cyber trespass vs cyber vandalism, and cyber terrorism vs hacktivism vs information warfare.
- Explain why codes of ethics are not enough for information-security professionals.
- State why privacy matters, how IT enables dataveillance, and what concerns arise from public-space tracking and biometrics.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Ethics | Study of right/wrong and good/bad; analyzes behaviours, policies, laws, and social structures |
| Consequentialism | Wrongness of actions judged by bad consequences |
| Deontology | Moral duties exist independently of consequences |
| Computer ethics | 1980s field on professional/user duties and IT public-policy ethics |
| System security | Protecting hardware/software against malicious sabotage |
| Information security | Protecting stored and transmitted data (CIA) |
| Safety-critical system | Real-time control system whose failure can threaten life |
| Hacking / cracking | Unauthorized access; crackers = malicious/disruptive break-ins (hacker self-description) |
| Hacker ethic | Information should be free; unlimited computer access; cyberspace cannot harm the real world |
| Cyber trespass | Unauthorized access to systems or password-protected sites |
| Cyber vandalism | Programs that disrupt networks or corrupt data |
| Cyber terrorism | Politically motivated hacking intended to cause grave harm (death and/or severe economic loss) |
| Hacktivism | Political site disruption without intent to cause serious damage |
| Information warfare | Using information and attacks on information systems as tools of war |
| ISSA | Information Systems Security Association; code requires law plus “highest ethical principles” without specifying them |
| Right to be let alone | Warren and Brandeis's definition of privacy |
| Informed consent | Tell people how personal data will be stored/used/exchanged and obtain consent |
| Dataveillance | Large-scale computerized collection/processing of personal data to monitor actions and communications |
| Biometrics | Identity verification from physiological or behavioral characteristics |

### Exam lines
- Ethics is not the same as law: legality does not replace morality for individuals or corporations.
- Computer security has a moral structure: CIA plus system vs data, tied to rights, harms, and interests — including economic, cultural, psychological, and life-and-death stakes in safety-critical systems.
- Over-strong or discriminatory security can itself violate access, fairness, and freedom rights (including FOI and free speech when availability is blocked).
- The hacker ethic's “information should be free” claim collides with intellectual property, privacy, and data integrity.
- Cyber terrorism is marked by **political motive plus grave harm**; hacktivism and ordinary cyber crime are not the same thing; information warfare extends ordinary war onto information systems.
- Professional codes (e.g. ISSA) are too thin: security practitioners need ethics **training**, not only a code.
- Privacy is the right to be let alone / control access to private affairs; it is valuable for autonomy and democracy but not absolute.
- IT scaled surveillance into **dataveillance**; 9/11 and consumer tracking intensified the privacy–surveillance tension; public-space tracking and biometrics further squeeze anonymity.


---

## M02: Network Security

### Learning focus
- State why e-business networks need network security and list the CIA goals.
- Distinguish a **threat** from an **attack**, and **passive** from **active** attacks.
- Relate snooping, traffic analysis, replay, modification, and denial of service to confidentiality, integrity, and availability.
- Describe cryptography's three mechanisms: symmetric-key, asymmetric-key, and hashing (including MD5 and SHA).
- Place border routers, firewalls (static / stateful / proxy), IDS, and IPS in a network-boundary defense.
- List hallmarks of a good security policy and the non-technical side of defense in depth.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Confidentiality | Protect stored and transmitted information from unauthorized disclosure |
| Integrity | Authorized entities change data only through authorized mechanisms (faults can also violate it) |
| Availability | Authorized entities can access information when needed |
| Threat | Possible danger that might exploit a vulnerability |
| Attack | Deliberate assault that tries to evade services and violate policy |
| Passive attack | Eavesdropping / monitoring to obtain transmitted information |
| Traffic analysis | Inferring communication nature from patterns despite encryption |
| Snooping | Unauthorized access to or interception of data |
| Replay | Capture a data unit and retransmit it for an unauthorized effect |
| Symmetric-key crypto | Same shared secret key for encrypt and decrypt |
| Asymmetric-key crypto | Related public/private pair; decryption key infeasible to derive from encryption key |
| RSA | Example algorithm where either related key may encrypt and the other decrypt |
| Compression function | Fixed-size hash step: n bits in, m bits out, n > m |
| MD5 | Rivest message digest: 512-bit blocks → 128-bit digest (too small) |
| SHA / NIST | Secure Hash Algorithm family standardized by NIST |
| ACL | Access control list on a border router (static L3 filter) |
| Ingress / egress filtering | Only properly destined traffic enters / leaves |
| Smurf attack | Spoofed ICMP echo to broadcast addresses; responses flood the victim |
| Stateful firewall | Tracks connections in a state table; most common type |
| Proxy firewall | Intermediary; full-packet protocol compliance; most advanced, least common |
| IDS | Detect and alert (signatures / anomaly); does not auto-block |
| IPS | Detect and automatically prevent/block |
| Defense in depth | Layered technical controls plus policy and awareness |

### Exam lines
- E-business needs scalable voice/video/data networks; more applications and users mean more threats, so network security is central.
- CIA is the goal set: conceal in storage and transit; authorize changes (including against accidental corruption); keep authorized access working (a bank that cannot serve accounts fails availability).
- A threat is potential danger; an attack is a deliberate intelligent assault. Passive attacks steal or infer information; replay, modification, and DoS produce unauthorized effects; snooping is stopped by making data meaningless via encryption.
- Cryptography today is three mechanisms: shared-key ciphers, public/private-key (RSA-style) algorithms, and iterated hashes (MD2/4/5; SHA from NIST). MD5's 128-bit digest is too small.
- Boundary defense: border router ACLs (ICMP, source routing, SYN, Smurf-style spoofing via ingress/egress), then firewalls (static vs stateful vs proxy), then IDS alerts and IPS auto-blocks.
- Defense in depth also needs a clear, scoped, dated, specific, understandable policy with named authority — not only tuned rule bases.


---

## M03: Computer Network Reference Models

### Learning focus
- Define a computer network and distinguish it from a distributed system (middleware / World Wide Web example).
- Classify networks by coverage: PAN, LAN, MAN, WAN, with named technologies and topologies.
- State the seven OSI-layer design principles and the PDU names from bit through APDU.
- Contrast **chained** layers (physical–network) with **end-to-end** layers (transport–application).
- List the function of each OSI layer (including MAC as a data-link sublayer).
- Describe the four-layer TCP/IP model, its ARPANET / DoD origins and design goals, key protocols, and how it differs from OSI.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Computer network | Autonomous computers interconnected by a single technology, able to exchange information |
| Distributed system | Independent computers appearing as one coherent system (often via middleware) |
| Middleware | Software above the OS that implements the distributed-system illusion |
| PAN / Bluetooth | ~10 m personal interconnection; short-range radio |
| IEEE 802.3 Ethernet | Bus-based broadcast LAN, decentralized control, 10 Mbps–10 Gbps |
| IEEE 802.5 Token Ring | Ring LAN at 4 and 16 Mbps; transmit after capturing a token |
| FDDI | Another ring-network example |
| WiMAX | Wireless MAN technology |
| Head-end | Central MAN point that feeds TV and Internet to homes |
| Subnet | WAN communication lines + switching elements/routers, typically telco/ISP owned |
| OSI | Open Systems Interconnection; ISO seven-layer model |
| Chained layers | Physical, data link, network — hop-by-hop, present on intermediate devices |
| End-to-end layers | Transport through application — only on end computers |
| TPDU / SPDU / PPDU / APDU | PDUs at transport, session, presentation, application |
| MAC | Medium Access Control sublayer: shared-channel access on broadcast networks |
| ARPANET | DoD-sponsored 1960s research network; grandfather of the Internet |
| TCP vs UDP | Reliable connection-oriented vs unreliable connectionless transport |

### Exam lines
- A network interconnects autonomous computers; a distributed system (WWW via middleware) makes them look like one machine.
- Coverage taxonomy: PAN (~10 m, Bluetooth), LAN (Ethernet bus / Token Ring / FDDI), MAN (cable TV, WiMAX, head-end), WAN (customer hosts plus telco/ISP subnet of lines and routers).
- OSI's seven layers follow explicit design principles; PDUs run bit → frame → packet → TPDU → SPDU → PPDU → APDU; lower three layers are chained, upper four are end-to-end.
- Each OSI layer has a distinct job: bits and media; frames, ACK, flow control, MAC; routing, congestion, addressing, QoS; end-to-end TPDUs and service type; sessions (dialog, tokens, sync); syntax/semantics; user protocols (HTTP, mail, news, file transfer).
- TCP/IP is the living Internet model: four layers, ARPANET/DoD goals (internetworking, surviving as long as endpoints live, flexibility), IP plus TCP/UDP plus Telnet/FTP/SMTP/DNS/NNTP/HTTP.
- Shared idea of a protocol stack and transport-to-applications split; OSI has more layers and a cleaner service/interface/protocol split; TCP/IP puts connectionless IP below and lets the user choose TCP or UDP above.


---

## M04: Computer Network Reference Models — TCP/IP Layers Continuation

### Learning focus
- Trace TCP/IP from ARPANET / DARPA (Kahn and Cerf, NCP) to the IETF-maintained Internet protocol suite.
- Map the four TCP/IP layers (and the five-layer hybrid that adds physical) onto OSI, including chained vs end-to-end layers.
- List link-layer tasks (MAC, LLC) and named link protocols: IEEE 802 family, ATM, ARP, NDP, LLTD, PPP.
- State IP's three functions and the internet-layer protocols IP, ICMP, IPsec/IKE, IGMP, and OSPF.
- Contrast TCP and UDP (RFCs, reliability, sockets/ports) and name DCCP, RSVP, TLS/SSL, and SCTP.
- Identify application-layer protocols with their RFCs: Telnet, FTP, SMTP, HTTP, RPC, DNS, SNMP, RTP.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Internet protocol suite / TCP/IP | Model and protocols of the Internet; named for TCP and IP |
| DoD model | Alternate name because ARPANET was DoD-sponsored |
| IETF | Body that maintains TCP/IP and related models |
| DARPA | Agency whose late-1960s R&D produced the suite |
| NCP | ARPANET Network Control Program; Cerf was its developer |
| Five-layer hybrid | Four TCP/IP layers plus an explicit physical layer 1 |
| MAC / LLC | Shared-medium access vs flow control, link management, error handling, packet sizing |
| ATM | Fixed-size cells; mix real-time audio/video with regular data |
| ARP / NDP | IP→MAC mapping for IPv4 vs IPv6 neighbor discovery |
| LLTD | Microsoft proprietary topology / QoS discovery |
| PPP | ISP dial-up over a telephone line between two nodes |
| IP | Unreliable datagram forwarding; fragmentation; IPv4 and IPv6 |
| ICMP | Errors and diagnostics (echo) sitting on IP |
| IPsec / IKE | Authenticate/encrypt IP datagrams; key exchange |
| IGMP | IP multicast group administration |
| OSPF | Link-state IGP inside one AS; called the most widely used Internet routing protocol here |
| Socket | IP address + port = unique connection endpoint |
| RFC 793 / RFC 768 | TCP / UDP standards |
| DCCP / RSVP / SCTP | Congestion-aware datagrams; resource reservation; scalable stream TCP-like transport |
| TLS / SSL | Encrypt TCP segments; keys, auth, encryption, signatures |

### Exam lines
- TCP/IP is a practice-first, IETF-maintained DoD/ARPANET descendant: Kahn and Cerf hid network differences behind a common internet protocol and moved reliability from the network to the **host** (replacing NCP).
- Four layers (or five if physical is drawn separately): link and internet are chained; transport and application are end-to-end process communication. OSI protocols were designed first and are unused; TCP/IP dominates.
- Link layer is local (no routers): IEEE 802 (Ethernet, Token Ring, 802.11), ATM cells, ARP (IPv4) vs NDP (IPv6), Microsoft LLTD, and ISP PPP dial-up.
- Internet layer: hierarchical addressing, hop-by-hop routing, congestion control — IP (unreliable, fragmenting, v4/v6), ICMP, IPsec+IKE, IGMP multicast, OSPF inside an AS.
- Transport: ports and sockets; TCP (RFC 793, reliable bidirectional) vs UDP (RFC 768, fast, lossy, unordered); also DCCP, RSVP, TLS/SSL, SCTP.
- Application is the OSI 5–7 interface: Telnet, FTP, SMTP, HTTP, RPC, DNS, SNMP, RTP, several explicitly tied to RFCs and to client–server over TCP.


---

## M05: Protocol Stack

### Learning focus
- Distinguish a protocol **suite** (definition) from a protocol **stack** (software implementation) and state why layered modules exist.
- Recite the five OSI layering principles (including ISO 7498) and describe encapsulation/decapsulation (headers, Layer-2 trailer, physical signals).
- List services of each of the seven OSI layers, with named mechanisms (baud rate, line codes, CSMA/CD, IP/ICMP/IGMP/IPsec, TCP vs UDP, session beans, etc.).
- Describe the four TCP/IP layers and early applications Telnet, FTP, SMTP, and DNS (including the Yahoo name-to-address example).
- State the lecture's listed merits and demerits of TCP/IP.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Protocol suite | Definition of the protocols |
| Protocol stack | Software implementation of the suite; hierarchy of layers |
| ISO 7498 | Identifier of the OSI model standard |
| D7…D1 | Data units at OSI layers 7 down to 1 |
| Baud / symbol rate | Symbol (or pulse) changes per second on the medium |
| Modem | Device that both modulates and demodulates |
| Line encoding | Unipolar, polar, bipolar, Manchester patterns of voltage/current/photons |
| Simplex / half / full duplex | One-way; either direction but not both at once; both at once |
| Frame | DLL PDU: link header + packet; trailer typically only here |
| ARQ | Retransmit specified frames when errors are detected |
| IEEE 802.2 LLC | Common LAN logical-link protocol |
| CSMA/CD vs token passing | Ethernet MAC vs Token Ring MAC |
| Slow start | Congestion avoidance that starts (or restarts after loss) at low rate |
| UDP-Lite | Lightweight UDP variant; still connectionless, no inherent congestion control |
| Session beans | Session-scoped objects deleted when the web session disconnects |
| Network virtual terminal | Emulated terminal so a remote host accepts a logon |
| www.yahoo.com → 204.71.177.71 | DNS example given in the lecture |

### Exam lines
- A suite is the specification; a stack is the running layered software, often split into media / transport / applications with two OS interfaces (e.g. TCP/IP ↔ Ethernet, browser ↔ TCP/IP).
- OSI (ISO 7498) uses seven abstraction layers with explicit design rules; data grows headers (and a layer-2 trailer) going down, becomes an EM signal, and is unwrapped going up.
- Physical: bits, baud, connectors, radio/IR, modulation/modems, line codes, bit sync, point-to-point vs multipoint, topology, duplex modes.
- Data link: frames, hardware addresses, flow control, ARQ, LLC (802.2), MAC (CSMA/CD vs token passing).
- Network: logical IP addresses, routing, datagrams, fragmentation, ICMP/IGMP/IPsec/IPv4/IPv6.
- Transport PDUs traverse the network unmodified; TCP is a reliable connection; UDP/UDP-Lite are cheap and connectionless — applications must not blast at line rate. Ports multiplex (OSI would put that in session).
- Session (auth, authorization, restoration, checkpointing; session beans, lip-sync, live TV), presentation (translate, encrypt, compress), application (mail, virtual terminal, directories, FTAM).
- TCP/IP: underspecified host-to-network, connectionless IP, TCP or UDP (full or half duplex), Telnet/FTP/SMTP/DNS on top. Merits: independence, scale, client–server, many routing protocols, can connect two computers. Demerits: transport does not always guarantee delivery, poor reuse in other applications, hard protocol replacement, fuzzy service/interface/protocol split.


---

## M06: Transmission Control Protocol

### Learning focus
- Place TCP in the Cerf–Kahn 1974 internetworking paper and in RFC 793 / 1122 / 1323.
- Explain reliable stream delivery: segments, acknowledgements, timers, retransmission, and nesting TPDU ⊂ packet ⊂ frame.
- Define sockets, TSAPs/ports (including well-known ports below 1024 and IANA), and TCP's full-duplex, point-to-point, byte-stream service.
- Walk the 20-byte TCP header field by field (ports, seq/ack, data offset, flags, window, checksum, urgent pointer, options).
- Use socket primitives and the three-way handshake (plus simultaneous-open collision and FIN release / two-army timers).
- Apply variable-size sliding-window flow control, including a zero window and the one-byte probe that prevents deadlock.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Transmission control program (1974) | Cerf–Kahn component later split into TCP + IP |
| RFC 793 / 1122 / 1323 | TCP definition; clarifications and bug fixes; extensions |
| Segment | TCP unit of transmission; IP encapsulates it for delivery |
| TPDU | Transport protocol data unit nested in packets then frames |
| Socket / TSAP | IP + 16-bit port; port is TCP's transport service access point |
| Well-known ports | Numbers below 1024 reserved for standard services; IANA assigns |
| Byte stream | Message boundaries not preserved; writes may coalesce or split |
| 20-byte header | Fixed TCP header; options extra; max data 65495 with 20-byte IP |
| ACK number | Next byte expected, not last byte received |
| SYN/ACK/FIN/RST/PSH/URG | Connection setup, valid ACK, close, reset, push, urgent offset |
| Sliding window | Variable-size; WIN says how many bytes may be sent from ACK point |
| Pseudo-header | Included in the TCP checksum along with header and data |
| Three-way handshake | SYN; SYN+ACK; ACK (seq X / Y, ACK X+1 / Y+1) |
| Two-army problem | Connection-release uncertainty; solved with 2× MPL timers |
| Zero window | Sender stops except urgent data or a 1-byte window probe |

### Exam lines
- TCP grew out of the 1974 Cerf–Kahn transmission control program, then split from IP; it is specified in RFC 793 with later fixes (RFC 1122) and extensions (RFC 1323).
- It is a reliable, ordered **byte stream** with ACKs, retransmission timers, and segments carried inside IP packets inside frames — not a message stream, and not multicast/broadcast.
- Endpoints are sockets (IP + port/TSAP); well-known ports below 1024 (FTP 20, Telnet 23, SMTP 25/587, DNS 53, HTTP 80, POP/IMAP, ISAKMP 500, RTSP 554, etc.) are IANA-assigned.
- The 20-byte header numbers every byte, advertises a window, checksums a pseudo-header, and uses six flags for urgent data, valid ACKs, push, reset, setup (SYN), and teardown (FIN).
- Servers socket/bind/listen/accept; clients socket/connect; close is symmetric. Setup is a three-way handshake (RST if nobody listens); simultaneous open can collide. Teardown is two FINs (often four segments, sometimes three) plus timers against the two-army problem.
- Flow control is a variable window independent of data-link-style ACK coupling: a full 4K buffer can advertise WIN=0; urgent data and a one-byte probe still get through so a lost window update cannot deadlock.


---

## M07: Data Link Layer

### Learning focus
- Place the data link layer (DLL / Layer 2) above the physical layer and split it into LLC and MAC.
- List DLL functions: framing, hardware addressing, error control, flow control, and multi-access (CSMA/CD).
- Describe four framing methods: byte count, flag bytes with byte stuffing, flag bits with bit stuffing (01111110), and physical-layer coding violations (Manchester / IEEE 802).
- Contrast stop-and-wait with sliding-window flow control, including utilization U = 1/(1+2a).
- Explain ARQ error control: stop-and-wait ARQ, Go-Back-N ARQ, and selective-repeat ARQ.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| DLL / Layer 2 | OSI layer above physical; hides hardware; frames for upper layers |
| Collision domain | Shared-link setting that makes DLL work harder |
| LLC | Point-to-point sublayer: protocols, flow control, error control |
| MAC | Who uses the broadcast medium; CSMA/CD for shared access |
| NIC | Network interface card / adapter (e.g. Ethernet) implementing DLL in hardware |
| Segmentation / encapsulation | Split network-layer stream; add header and frame flags |
| Byte stuffing | Insert ESC before accidental flag bytes in the data |
| Bit stuffing | After five 1s in data, insert 0; flag is 01111110 |
| Manchester / coding violation | 1→10, 0→01; illegal physical codes delimit IEEE 802 frames |
| Stop-and-wait | One data frame, then wait for ACK; U = 1/(1+2a) |
| a | Propagation time / transmission time |
| Sliding window | Numbered frames; window up to 2^K−1; used by TCP (kernel buffer) |
| ARQ | Automatic repeat request after error detection |
| Stop-and-wait ARQ | ACK/NAK plus timer; duplicates discarded; small buffers, poor on long delay |
| Go-Back-N | Continuous send; on NAK/timeout resend that frame and all later ones; max window 2^K−1 |
| RR | Receive Ready piggyback (e.g. RR1) |
| Selective repeat | Retransmit only lost/NAK frames; receiver resequences from storage |

### Exam lines
- Layer 2 sits on the physical bit pipe, hides the hardware, and is hardest on a shared collision domain; LLC (point-to-point protocols, flow, errors) and MAC (who speaks on the broadcast medium) split the work, often in an Ethernet NIC.
- Packets become frames with address, checksum, and control fields; four ways to mark frame edges are count, byte-stuffed flags, bit-stuffed 01111110, and Manchester coding violations (IEEE 802).
- Speed mismatches (Pentium vs 80386, Ethernet vs a 28.8 kbps modem) require flow control: stop-and-wait is simple but idle on long-delay paths (U = 1/(1+2a), bad for satellite); sliding windows of size at most 2^K−1 (and TCP's kernel buffer) keep multiple frames in flight and can cumulative-ACK.
- Errors are recovered by ARQ: stop-and-wait ARQ (ACK/NAK, timer, drop duplicates) is simplest and least efficient; Go-Back-N is continuous and rewinds to the bad frame (window capped at 2^K−1 so piggybacked RR cannot be ambiguous); selective repeat is most efficient and most complex because only lost frames are resent and the receiver must reorder.


---

## M08: Medium Access Control Protocols

### Learning focus
- Place the MAC sublayer in the OSI data-link layer and list its basic functions.
- Contrast static channel allocation (FDM) with dynamic allocation and state the LAN assumptions that dynamic methods need.
- Distinguish random-access (ALOHA, CSMA, CSMA/CD) from controlled-access (polling, token passing, slotted ring) methods.
- Compute Pure ALOHA and slotted ALOHA throughput and explain the vulnerable period in each.
- Describe nonpersistent, 1-persistent, and *p*-persistent CSMA, and the CSMA/CD collision procedure used on early Ethernet.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| MAC sublayer | Bottom of the data-link layer; IEEE media-access, error detection, station addressing; serves LLC, uses the physical layer |
| LLC | Logical Link Control; MAC’s user above |
| Multiple access | Many stations share one broadcast medium |
| FDM | Static split of bandwidth into fixed frequency partitions |
| Collision | Overlapping transmissions that garble the signal |
| Carrier sensing | Electrical sense that the channel is busy or free |
| ALOHA | Random-access protocol from the University of Hawaii (early 1970s) |
| Vulnerable period | Time window in which another packet can overlap and destroy a transmission |
| \(G\), \(S\) | Offered load per packet time; successful throughput per slot |
| CSMA | Sense-before-transmit multiple access |
| 1-persistent CSMA | Keep sensing a busy medium, then send with probability 1 (Ethernet CSMA/CD) |
| *p*-persistent CSMA | After idle, send with probability \(p\) (CSMA/CA, Wi-Fi) |
| CSMA/CD | CSMA plus collision detection, jam, and backoff (early Ethernet) |
| 10BASE5 / 10BASE2 / 10BROAD36 / 1BASE5 | CSMA/CD cabling options named by Mbps, baseband/broadband, and segment length × 100 m |

### Exam lines
- Shared-medium LANs need MAC so simultaneous sends do not garble frames; MAC sits under LLC and above the physical layer.
- Static FDM wastes spectrum or starves users when traffic is not small and constant; dynamic methods are what LANs and WANs actually use.
- Random access (ALOHA, CSMA, CSMA/CD) versus controlled access (polling vs token/slotted ring) is the main protocol split; register insertion is obsolete.
- Pure ALOHA needs no sync but tops out near 18% (\(S = Ge^{-2G}\) at \(G=0.5\)); slotted ALOHA halves the vulnerable period and reaches about 36.8% (\(S = Ge^{-G}\) at \(G=1\)).
- CSMA listens first; 1-persistent is Ethernet/CSMA/CD, *p*-persistent is Wi-Fi/CSMA/CA.
- CSMA/CD aborts into a jam and backoff, and is taught as more efficient than ALOHA and plain CSMA on a bus with bursty traffic.


---

## M09: TCP/IP Model-IP Addressing – I

### Learning focus
- Trace a payload vertically down the TCP/IP stack from application to physical layer.
- State what a protocol is and when TCP versus UDP is used at the transport layer.
- Bind well-known applications to port numbers and describe a TCP segment’s source and destination ports.
- Explain IPv4 dotted-decimal addressing, classful classes A–E, default masks, and network versus host bits.
- Compute network, broadcast, and gateway addresses, and state why CIDR/subnetting is introduced to cut classful waste.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| All People Seem To Need Data Processing | Mnemonic for the seven layers from application down |
| Payload | Application data handed down (e.g. `www.google.com`) |
| Protocol | Set of rules for a line of action (TCP or UDP at transport) |
| Segment | Transport PDU: payload plus source and destination ports |
| Port | 16-bit application identifier; 65,536 possible values |
| Well-known ports | Below 1024; not used as random source ports |
| Dotted-decimal | IPv4 written as four octets 0–255 |
| Subnet mask | Marks which IP bits are network vs host |
| Unicast | One machine talking to one other machine |
| Network address | IP AND mask; host bits zero |
| Broadcast address | All host bits one |
| Gateway | Router address used to reach another network |
| CIDR | Classless inter-domain routing; subnetting to reduce classful waste |

### Exam lines
- Layers talk only **down the stack**; the browser payload becomes a TCP segment (ports) then an IPv4 packet (addresses).
- TCP is taught as the default for HTTP and mail; UDP is the other transport choice.
- HTTP listens on **80**; sources pick a port **above 1024**; FTP 20/21, SMTP 25, SSH 22, Telnet 23.
- IPv4 is 32-bit dotted decimal; classful A/B/C (with D multicast, E reserved) waste space when a site needs only 20 hosts.
- Network = IP AND mask; broadcast = host bits all 1; a gateway (often last host address) is required to leave the network; usable hosts are \(2^n-2\).
- CIDR/subnetting uses only as many host bits as needed (five bits for 20–31 hosts); mask arithmetic and MAC addresses are the next lecture.


---

## M10: TCP/IP Model-IP Addressing – II

### Learning focus
- Finish the 20-host CIDR example: mask `255.255.255.224`, block size, network and broadcast.
- Repeat the method for 10 hosts (`/28`) and list network, broadcast, first/last host, and wasted addresses.
- Write the same prefix in subnet-mask form and in CIDR slash notation.
- Distinguish IPv4 **logical** addresses from 48-bit **MAC** **physical** addresses (OUI + serial).
- Use ARP (broadcast request, unicast reply) to fill a frame when two hosts are on the same network; note that off-net frames use the **gateway’s** MAC.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| CIDR | Classless inter-domain routing; slash prefix equivalent to a mask |
| Incomplete octet | The mask octet that is not 0 or 255; used to get block size as \(256 -\) that value |
| Block size | Number of addresses in the CIDR block (e.g. 32 for mask 224, 16 for 240) |
| `/28` | 28 network bits = mask `255.255.255.240` |
| Frame | Data-link PDU with source and destination MAC |
| Logical vs physical | IP vs MAC (phone number vs IMEI analogy) |
| OEM / OUI | First three MAC bytes: manufacturer |
| `ipconfig /all` | Shows IP, mask, and MAC |
| `ping` | Reveals the current IP of a name such as `www.google.com` |
| ARP | Broadcast request / unicast reply to map IP → MAC on the same network |
| Gateway MAC | Destination MAC of an off-net frame (not the remote server’s MAC) |

### Exam lines
- For 20 hosts, mask **`255.255.255.224`**, block **32**, network `.0`, broadcast `.31`; leftover `.21–.30` are waste.
- For 10 hosts, **`192.168.1.0/28`** = **`255.255.255.240`**, block **16**, broadcast `.15`, 14 usable, four leftover if only 10 are assigned.
- Network layer = host-to-host **packet**; data-link = hardware **frame** with 48-bit MACs (24-bit OEM + 24-bit serial).
- Names become IPs (`ping`); IPs become MACs (`ipconfig /all` plus ARP).
- Same-net destination MAC comes from ARP; **off-net destination MAC is the gateway**, not the server — the usual student error.
- Transport = process-to-process (ports), network = host-to-host (IP), data-link = node-to-node (MAC).


---

## M11: TCP Connection Management and Flow Control

### Learning focus
- Explain how TCP can be connection-oriented while using connectionless IP.
- Walk the three-way handshake (passive/active open, SYN, SYN+ACK, ACK) including sequence-number consumption.
- Describe SYN flooding as a denial-of-service attack and the mitigations taught (limits, filters, cookies).
- Account for bidirectional data transfer, piggybacked ACKs, PSH, and URG (including what urgent mode is not).
- Contrast three-way connection termination with four-way half-close.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Virtual path | TCP’s connection-oriented path over connectionless IP |
| Passive open | Server ready to accept; does not itself initiate |
| Active open | Client request to connect to a particular server |
| SYN | Control segment that syncs ISN; consumes one sequence number; no real data |
| SYN+ACK | Server’s reverse SYN plus ACK of client SYN; carries rwnd |
| ACK (handshake 3) | Usually no data; consumes no sequence number |
| ISN | Random initial sequence number |
| TCB | Transmission control block; state allocated per embryonic connection |
| SYN flooding | DoS via forged SYNs that exhaust server resources |
| Cookie | Postpone allocation until the client IP is shown valid |
| Piggybacking | ACK carried with data |
| PSH | Push: send/deliver without waiting to fill buffers |
| URG / urgent pointer | Mark a stream range for special treatment; not priority or out-of-order delivery |
| FIN | Close in one direction; consumes one sequence number if no data |
| Half-close | Stop sending but keep receiving (e.g. sort-then-reply) |

### Exam lines
- TCP is virtually connection-oriented on top of unaware, connectionless IP (retransmission and reordering are TCP’s job).
- Full-duplex use needs a three-way handshake: SYN (ISN, one seq), SYN+ACK (reverse ISN + rwnd), ACK (usually no seq consumption).
- SYN flooding is DoS by fake source IPs filling TCB/timer resources; limits, filters, and cookies are the taught defenses.
- Data is bidirectional with piggybacked ACKs; PSH is for interactive immediacy (often ignored); URG only marks special bytes in order.
- Close is three-way FIN / FIN+ACK / ACK, or four-way half-close so one side can finish sending while the other still replies.


---
