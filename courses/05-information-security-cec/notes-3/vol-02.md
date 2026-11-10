# Volume 02 — M12–M23

> Information Security (CEC) · SWAYAM / CEC Information Security
> **notes-3** — concept exam notes (definitions & what things do). Breadth over lab depth.

---

## M12: IPV4 & IPV6

### Learning focus
- Place IPv4 as RFC 791’s connectionless 32-bit packet protocol and parse every IPv4 header field taught.
- Contrast classful IPv4 ranges and default masks with CIDR (RFC 1519) using the Cambridge / Oxford / Edinburgh example.
- Explain NAT and the RFC 1918 private ranges.
- List IPv6’s 128-bit notation, header fields, address compression, and six extension headers.
- State which IPv4 header fields disappear in IPv6 and why.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| RFC 791 / RFC 760 | IPv4 spec (1981) replacing the 1980 definition |
| IHL | Header length in 32-bit words; 5–15 |
| DSCP / ECN | Diffserv class; congestion signal without drops |
| DF / MF | Don’t fragment; more fragments |
| Classful addressing | Historic A–E split; no longer used |
| CIDR (RFC 1519) | Variable blocks, class-free, aligned on block size |
| NAT | One public IP; rewrite internals at the border |
| RFC 1918 | Private ranges 10/8, 172.16/12, 192.168/16 |
| Flow label | IPv6 pseudo-connection / QoS-related marking |
| Hop limit | IPv6 TTL-as-actually-used |
| `::` | Compression of one or more zero 16-bit groups |

### Exam lines
- IPv4 is connectionless, 32-bit, RFC 791; the header is 20 bytes plus up to 40 bytes of options, with DSCP/ECN, fragmentation (DF/MF/offset), TTL, protocol, and header-only checksum.
- Classful A–E is historical; CIDR hands out aligned variable blocks (Cambridge 2048, Oxford 4096 on a 4096 boundary, Edinburgh 1024).
- NAT plus RFC 1918 private space, often with a firewall, keeps internal 10.x addresses off the public Internet.
- IPv6 is 128-bit, 40-byte fixed header, seven fields, better options/security/QoS; addresses compress with dropped leading zeros and `::`.
- IPv6 drops IHL, protocol, fragmentation fields, and checksum; TTL is renamed hop limit; six extension headers (including AH and ESP) carry what IPv4 stuffed into options and flags.


---

## M13: UDP — User Datagram Protocol

### Learning focus
- Place UDP between applications and IP as a connectionless, unreliable, low-overhead process-to-process protocol.
- Parse the 8-byte user-datagram header and the hexadecimal dump example (ports, length, data).
- List UDP services: well-known ports, no connection, no flow/window, checksum with pseudo-header, no congestion control.
- Trace encapsulation/decapsulation, queuing, and multiplexing/demultiplexing.
- Describe the five-component UDP “package” (control-block table, input queues, control-block / input / output modules).

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| User datagram | UDP packet; 8-byte header plus data |
| Ephemeral port | Client port chosen by UDP/OS (vs well-known server ports) |
| Socket | IP address + port |
| Pseudo-header | IP-derived fields (including protocol 17) included in the UDP checksum |
| Silent drop | Checksum failure with no NAK to the sender |
| Protocol 17 | IP protocol number for UDP |
| Multiplexing | Many processes → one UDP at the sender |
| Demultiplexing | One UDP → many processes at the receiver |
| Control-block table | Open-port state, PID, port, queue number |
| ICMP on unknown port | Input module’s response when no table entry matches |

### Exam lines
- UDP is a thin, connectionless, unreliable transport: ports for process-to-process delivery, almost no control, silent drop on error.
- Header is always 8 bytes (src, dest, length, checksum); example `CB84/000D/001C/001C` is client port 52100 to daytime (13) with 20 data bytes.
- No connections, numbering, flow window, or congestion control; checksum (with pseudo-header) is the only error tool and is optional versus a bare datagram protocol.
- Encapsulation sets IP protocol 17; decapsulation peels physical → link → IP → UDP and passes the sender socket up for a reply.
- Features that look like weaknesses (no setup, no retry) are taught as advantages for short exchanges and for not feeding congestion.
- The sketched package: control-block table, per-process input queues, modules for bind, receive (ICMP if no port), and send.


---

## M14: IPSec Security Protocol

### Learning focus
- Define IPsec as a network-layer framework (not a single protocol) for authenticating and encrypting IP packets.
- Name architecture pieces from RFC 2401: security associations, AH, ESP, transport vs tunnel mode, and IKE.
- Contrast transport mode (payload protected; IP header intact) with tunnel mode (whole packet wrapped; used for VPNs).
- Parse AH and ESP headers/trailers, ICV, SPI, and sequence numbers for anti-replay.
- State IKE’s role (RFC 2409): mutual authentication, SA setup, aggressive/main modes, and three authentication methods.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| IPsec | Network-layer suite: authenticate and encrypt each IP packet; useful for VPNs and dial-up without host software changes |
| RFC 2401 | IPsec architecture (SA, AH, ESP, modes, IKE) |
| SA | Security association: algorithms and parameters for AH/ESP |
| Transport mode | Crypto endpoints = communication endpoints; payload protected, IP header intact |
| Tunnel mode | Whole packet wrapped in a new IP header; VPNs; at least one crypto endpoint is a gateway |
| AH | Integrity and origin authentication; optional anti-replay; no privacy |
| ESP | Encryption (privacy) plus optional authentication |
| SPI | 32-bit index which, with dest IP, selects the SA |
| ICV | Integrity check value from a keyed hash |
| IKE (RFC 2409) | Mutual auth and SA/key setup; main vs aggressive; PSK / public-key encrypt / public-key signature |

### Exam lines
- IPsec secures IP itself (not the application), for host–host, gateway–gateway, or gateway–host, including VPNs, without reconfiguring every PC.
- Architecture is SAs plus AH and/or ESP in transport or tunnel mode, with IKE for keys.
- Transport keeps routing headers visible; tunnel hides the original packet behind gateway addresses and builds VPNs.
- AH authenticates (hash + SA key + ICV, SPI, anti-replay sequence); it does not give confidentiality — that is ESP.
- ESP splits header (SPI, seq), encrypted payload, trailer (pad, pad length, next header), and optional ICV after encryption for block ciphers and post-encrypt authentication.
- IKE (RFC 2409) negotiates SAs with main or aggressive mode and three auth methods; the lecture treats full crypto detail as out of scope.


---

## M15: Network Topologies

### Learning focus
- Define a network (nodes, links, distributed processing) and the five criteria: performance, consistency, reliability, recovery, security.
- Distinguish point-to-point from multipoint (spatially vs time-shared) connections.
- Separate physical topology from logical topology.
- Identify mesh (full and partial), star (passive/active/intelligent hub), bus, ring (token), and tree (expanded star), with the advantages and disadvantages taught for each.
- Use those trade-offs to match a topology to a network plan.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Node | Computer, printer, or other send/receive device |
| Distributed processing | Split a task across multiple machines |
| Transit vs response time | Message travel time vs inquiry-to-answer delay |
| Throughput | Successful messages per unit time (file size / time) |
| Four delay components | Processing, queuing, transmission, propagation |
| Point-to-point / multipoint | Dedicated pair vs shared link (spatial or time-shared) |
| Physical vs logical topology | Cable/device layout vs how data actually flows |
| Full mesh | \(n(n-1)/2\) duplex links; backbone use |
| Passive / active / intelligent hub | Splitter vs regenerator vs path-selecting (router/bridge/switch) |
| Terminator / barrel connector | Stop bus reflections; extend the bus |
| Token | Permission to send on a ring |
| Tree / expanded star | Stars joined by a bus backbone |

### Exam lines
- Networks are linked nodes doing distributed work; they are judged on performance (throughput vs delay), consistent response, reliability, recovery from backups, and security (antivirus, firewalls, backups, unplug when idle).
- Links are point-to-point (dedicated, including IR remote or satellite) or multipoint (spatial or turn-taking share).
- Physical layout can differ from logical data flow; the taught shapes are mesh, star, bus, ring, and tree.
- Full mesh is \(n(n-1)/2\) duplex links and is for backbones; partial mesh cuts cost; wireless often meshes with flooding or routing.
- Star is easy to grow and troubleshoot but dies with the hub; bus is cheap for small LANs but broadcasts to everyone and dies with the backbone; ring is ordered and collision-light via tokens but one break stops the ring; tree scales star+bus until the stem cable fails.


---

## M16: Animated Cursor Vulnerability — Proof of Concept I

### Learning focus
- Restate **CVE** (Common Vulnerabilities and Exposures) and why a **2007 Windows animated-cursor** flaw is still taught.
- Distinguish a **client-side attack** from traffic a **perimeter firewall** can filter.
- Define **remote code execution (RCE)** as unauthorized code running on someone else's machine.
- Explain at a concept level that Windows loads variable-size **`.ANI`** cursors via **`user32.dll`**, and that a malformed cursor can cause a **buffer overflow**.
- Name the lecture's defensive close: **patch** legacy systems; study **client-side attacks** and **buffer overflow**.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| CVE | Common Vulnerabilities and Exposures — catalog of named flaws |
| Animated cursor / `.ANI` | Variable-size Windows pointer animation, loaded through `user32.dll` |
| RIFF | File header that identifies an animated cursor |
| Network firewall | Perimeter filter for *inbound* traffic; does not stop a user who *goes out* to the web |
| Client-side attack | Compromise that starts because the insider visits a hostile page |
| Remote code execution | Running code on another machine without authorization |
| EIP | Instruction pointer; overflow target in the demonstration |
| Patch | The stated way to avoid the flaw on systems that still run the old loader |

### Exam lines
- Perimeter firewalls do not stop **client-side** browsing of a page that hosts a malicious cursor.
- The 2007 animated-cursor bug is a **buffer overflow in the Windows cursor loader** (`user32.dll`) that can yield **RCE** on **unpatched XP / 2000 / Vista**.
- A page need only **assign a CSS cursor URL** to a crafted **RIFF `.ANI`**.
- Overflow that **overwrites EIP** is the diagnostic that attacker-controlled data became the next-instruction address.
- **Patch** legacy systems; study client-side attacks and buffer overflow.


---

## M17: Animated Cursor Vulnerability — Proof of Concept II

### Learning focus
- Continue the animated-cursor demonstration conceptually: after EIP is attacker-controlled, execution can be redirected using instructions **already mapped** in system DLLs.
- Contrast **bind** vs **reverse** remote-shell *models* as firewall-relevant ideas (inbound listen vs victim-initiated outbound).
- Recite the **defensive lessons actually taught**: browse with **least privilege**, treat unexpected email links as client-side lures, **patch / hotfix** from **cve.mitre.org**, and see **malware / ransomware** as the next threat category.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Mapped DLL | Code already in the process (`user32` and others) that overflow control can be aimed at |
| Bind vs reverse shell | Inbound listen vs victim-initiated outbound — the latter matches allowed web traffic |
| Least privilege | Do not browse as Administrator; the attacker inherits the logged-in token |
| cve.mitre.org | Public CVE catalog; patch/hotfix against listed issues |
| Malware / ransomware / CryptoWall | Harmful software; CryptoWall encrypts files and extorts payment |
| Malvertising | Advertisement channel used to push malware |

### Exam lines
- After EIP is untrusted, execution can be steered using **code already in system DLLs**; the defender's answer is still **patch the loader**.
- **Reverse** connections piggyback on **user-initiated outbound** paths that firewalls already allow for the web.
- **Administrator browsing** makes a client-side bug a full compromise; **least privilege** is the taught countermeasure on the endpoint.
- **Lottery-style email links** are the same client-side pattern: the user **asks** to fetch the page.
- Track flaws on **cve.mitre.org** and **patch / hotfix**; unpatched loaders on XP/2000/Vista (CVE-2007 animated cursor) were the worked example.
- The course next frames **malware** (including **ransomware / CryptoWall**) as a fourth companion to software, hardware, and firmware.


---

## M18: Electronic Mail

### Learning focus
- Define **email** as store-and-forward digital messaging and list its **five basic functions**.
- Split an email system into **user agents (UA)** and **message transfer agents (MTA)** and match them to **RFC 822 / MIME** versus **SMTP**.
- Describe **RFC 5322** headers (To, Cc, Bcc, From, Sender, Received, Return-Path, and UA fields) and **MIME** headers and body hierarchy.
- Trace **SMTP** submission, **MX** lookup, and the **MAIL / RCPT / DATA** transaction.
- Contrast **POP3**, **IMAP**, and **MAPI** as message-*reading* protocols.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Store-and-forward | Servers accept, forward, deliver, and store; parties need not be online together |
| User agent (MUA/UA) | Local compose/read program |
| MTA / MSA / MDA | Transfer, submission, and delivery agents in the SMTP path |
| MIME | RFC 2045–2049: types, encodings, multipart body tree |
| RFC 5322 | Current Internet message format (via RFC 822 → 2822 → 5322) |
| SMTP / ESMTP | RFC 821 then RFC 5321 (2008); MAIL, RCPT, DATA on TCP |
| MX record | DNS mail exchanger for the domain after `@` |
| LMTP | Local Mail Transfer Protocol — SMTP derivative for MDA hop |
| POP3 | Port 110; download-and-delete; AUTH / Transaction / Update |
| IMAP4 | Port 143; server-resident mail; multiple mailboxes |
| MAPI | Microsoft Outlook–Exchange proprietary protocol |

### Exam lines
- Modern email is **store-and-forward** with five functions: compose, transfer, report, display, dispose.
- **UAs** format with **RFC 822/5322 + MIME**; **MTAs** move mail with **SMTP**.
- MIME added **typed, hierarchical bodies** so mail is more than ASCII English.
- SMTP submission is **587** (still often **25**); routing uses **DNS MX**; a transaction is **MAIL, RCPT, DATA**.
- **POP3** pulls and typically **deletes** on the server; **IMAP** keeps the **server copy as truth** and supports folders and partial fetch; **MAPI** is Outlook/Exchange only.


---

## M19: Email Security Protocols

### Learning focus
- Explain why ordinary email is compared to a **postcard**, not a sealed letter, including **transit and at-rest** inspection and **cross-border** legal complexity.
- Describe **PGP** (and **OpenPGP**) as hybrid encryption plus signatures, compression, and the taught **RSA key-length** choices.
- Outline **PEM** (RFC 1421–1424): canonicalization, hash, DES, one-time keys, **X.509** hierarchy — and **why it was never deployed**.
- State **S/MIME** services and its **multiple trust anchors** versus PEM's single root.
- Compare **S/MIME v3** and **OpenPGP** as the two systems the lecture treats as currently used.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Postcard model | Email visible to every relay; unlike a sealed envelope |
| PGP | Zimmermann 1991; IDEA + RSA + MD5 + ZIP + signatures; free, multi-OS |
| Session key | One-time symmetric key; RSA wraps it for the recipient |
| Alien-strength RSA | 2048-bit; recommended for all PGP use here |
| OpenPGP | IETF RFC 4880 (from RFC 1991 / 2440); Camellia RFC 5581; ECC RFC 6637 |
| PEM | RFC 1421–1424; DES; X.509 single-root CA; CRLs; unused |
| Web of trust | PGP's PKI answer to PEM's central root |
| IPRA / PCA | Policy authorities in the PEM certificate story |
| MOSS | MIME Object Security Services — post-PEM MIME security effort |
| S/MIME | RFC 2632–2643; MIME + crypto; multiple trust anchors |
| Non-repudiation | S/MIME service listed with authentication, integrity, secrecy |

### Exam lines
- Unprotected email is a **postcard** on untrusted servers; cryptography is necessary but **jurisdiction** makes privacy messy.
- **PGP** hybridizes **IDEA** (bulk) and **RSA** (tiny hash and session-key blobs), with **ZIP**, **MD5** signatures, and a strong push to **2048-bit** RSA.
- **OpenPGP** (RFC 4880) is the interoperable IETF form; both parties must run it; it also protects **stored** files.
- **PEM** matched PGP's goals with a **single X.509 root** and **DES**, and **died** on root politics, patent fees, and MIME.
- **S/MIME** keeps PEM-like services but allows **many trust anchors** and lives **inside MIME**.
- **S/MIME v3** and **OpenPGP** both secure mail; **certificates and encodings differ**, so they do not interoperate.


---

## M20: WWW Security

### Learning focus
- Explain why the **WWW** as a **client–server TCP/IP** application creates security problems that traditional publishing did not.
- Group Web threats as **passive vs active** and as **integrity, confidentiality, authentication, and DoS**, with the lecture's consequences and countermeasures.
- Place Web security in the stack: **IPsec** (network), **SSL/TLS** (transport), **SET / PGP / S/MIME** (application), plus **firewalls**.
- Distinguish IPsec **transport vs tunnel** mode and **AH vs ESP**.
- Outline **SSL/TLS**'s four protocols and **SET**'s card-payment properties.
- Classify **packet-filter** (static/stateful) and **proxy / application-gateway** firewalls, including the lecture's filter-table examples.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Passive vs active Web attack | Eavesdrop / read restricted data vs impersonate, alter transit, deface |
| IPsec transport / tunnel | Protect transport payload vs wrap the entire original IP packet |
| AH vs ESP | Integrity + source auth vs those plus confidentiality |
| SSL / TLS | Security just above TCP; Record, Handshake, Change Cipher Spec, Alert |
| HTTPS | HTTP carried in SSL/TLS |
| SET | Mastercard/Visa card-payment security; DES + RSA + SHA-1; merchant never sees PAN |
| Packet filter | IP/port/protocol table; static router or stateful appliance |
| Application gateway | Proxy that inspects URLs/content, e.g. HTTP |

### Exam lines
- The Web is a **two-way, highly visible, complex** client–server system; a hacked server can **pivot** into the rest of the site.
- Threats are **integrity, confidentiality, authentication, and DoS**; DoS is called out as **hard to stop**.
- Put crypto at **IP (IPsec)**, **above TCP (SSL/TLS / HTTPS)**, or **in the app (SET, PGP, S/MIME)**.
- SET is **not a payment network**; it **hides the card number from the merchant** and **pins algorithms**.
- Firewalls **filter or proxy**; application policy that depends on **who** is on port 80 needs a **proxy**, not just a packet table.
- Technical controls still require **user awareness**.


---

## M21: Mobile Code Security

### Learning focus
- Define the **mobile-code** paradigm (applets through agents), its flexibility/bandwidth benefits, and its **two threat directions** (code vs host, host vs code).
- List host-protection requirements: **authenticate origin, verify integrity, access control, semantic checks**.
- Explain host defenses taught: **sandboxing, digital shrink-wrap / Authenticode, proof-carrying code (PCC), code signing, access control / JAAS, program checking**.
- Outline **data and code protection** for agents: signatures, **hash chaining / forward integrity**, **sliding encryption**, replication, **holographic proofs + PIR**, tamper-proof hardware, **function hiding**.
- Repeat the close: host protection is **achievable**; protecting code from a **malicious host** is still **research**; **non-cryptographic** methods are generally **not enough** for the code.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Mobile code | Code that runs on hosts other than its origin (applets to agents) |
| Sandbox | Restricted environment; JDK 1.0 applets; often too limited to be useful |
| Authenticode / digital shrink-wrap | Producer signs; consumer verifies origin before run |
| PCC / VCGen | Proof-carrying code; consumer generates safety predicate, checks producer's proof |
| Code signing (JDK 1.1 / ActiveX) | Valid signature → full trust; else sandbox; coarse access control |
| JAAS | Ties **user identity** into Java access control (JDK 1.2+ model) |
| Forward integrity / PRAC | Hash-chain / small authenticator over agent-collected offers |
| Sliding encryption | Compact encryption for small data on many hops |
| Holographic proof + PIR | Probabilistic, tiny checks of a computation proof without revealing query bits |
| Function hiding | Run an encrypted function on a malicious host; decrypt the result |

### Exam lines
- Mobile code buys **flexibility and bandwidth** and opens **two-way** risk: **hostile applets/ActiveX** and **hostile hosts**.
- Hosts must **authenticate origin, check integrity, constrain rights, and check semantics**.
- Practical host tools: **sandbox, signing/Authenticode, PCC, JAAS-style policies**; signing alone is a **poor user decision** and an **all-or-nothing** ACL.
- Agents need **crypto** (hash chains, sliding encryption, holographic proofs, function hiding, smart cards); **replicas/voting** help integrity of results.
- Host protection is **in production reach**; **code vs malicious host** is **still research**; **crypto is required**.


---

## M22: Transmission Media

### Learning focus
- Define **transmission media** as the physical-layer path for **electrical or electromagnetic** signals and list design factors: **bandwidth, impairment, interference, number of receivers**.
- Compare **guided** media: **UTP, STP, coaxial (baseband/broadband), fiber** (step/graded multimode, single-mode), with connectors, applications, and trade-offs as taught.
- Describe **unguided** propagation (**ground, sky, line-of-sight**), **antennas**, and **satellite uplink/downlink**.
- Distinguish **radio, microwave, and infrared** bands, properties, and applications (including **IrDA**).

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Communication channel | Synonym for transmission media at the physical layer |
| UTP / STP | Unshielded vs foil/braid-shielded twisted pair; RJ-45 vs STP data connector |
| Subscriber loop | Twisted pair from home to telephone end office |
| Baseband / broadband coax | One high-speed digital signal vs many analog FDM signals on CATV plant |
| BNC / T / terminator | Coax connectors; terminator stops reflection |
| Critical angle | Governs refraction vs total internal reflection in fiber |
| Step-index / graded-index / single-mode | Fiber propagation families |
| Uplink / downlink | Ground→satellite / satellite→ground |
| Omnidirectional vs unidirectional | Radio vs microwave antenna behavior |
| IrDA | Infrared device-to-device standards (75 kbps then 4 Mbps) |

### Exam lines
- Rate and reach are set by **bandwidth, impairment, interference, and how many receivers share the guided medium**.
- **Twisting** cancels crosstalk; **UTP** is cheap and, here, the **fastest copper**; **STP** shields better but is **costly, must be grounded, rare in Ethernet**.
- **Coax** outperforms pair on bandwidth/noise but **attenuates fast**, can **fail the whole net**, and lost the telephone backbone to **fiber**.
- Fiber uses **reflection**, **>2 Gbps**, EMI immunity; modes are **multimode step, multimode graded, single-mode**.
- Wireless is **radio (omni, multicast), microwave (LOS unicast), infrared (in-room, IrDA)**; antennas and **licensed bands** matter.


---

## M23: Ethernet and Fast Ethernet

### Learning focus
- Place **Ethernet** historically (Xerox, commercial 1980, **IEEE 802.3** in 1983) and name the four **10 Mbps** cabling families.
- Map **LLC vs MAC**, list **IEEE 802.3 frame fields**, and walk **CSMA/CD** including **jam**, **binary exponential backoff**, and **why padding to 64 bytes** exists.
- Explain **Fast Ethernet (802.3u)** as the same rules with **bit time 100 ns → 10 ns**, and why **cable length** shrank instead of **minimum frame size**.
- List Fast Ethernet **PHY** types (T4, TX, FX, SX, BX, LX10) and the **MII / PCS / PMA / PMD** stack.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| IEEE 802.3 / 802.3u | Ethernet (1983); Fast Ethernet (June 1995) |
| 10BASE5 / 2 / T / F | Thick coax 500 m; thin 185 m; TP hub 100 m; fiber 2 km |
| Vampire tap | 10BASE5 pin into the coax core |
| LLC / MAC | Network-protocol handoff vs shared-media access and MAC addresses |
| CSMA/CD | Sense, send, detect collision, jam, backoff |
| Binary exponential backoff | Wait 0…2^i−1 slots; cap 1023 after 10; fail after 16 |
| Slot time / 2T | Collision window; min frame **64 bytes** so sender still transmitting when jam returns |
| 100VG-AnyLAN | 802.12 demand-priority alternative that did not succeed |
| MII / PCS / PMA / PMD | Fast Ethernet MAC–PHY stack; autonegotiation in PCS |

### Exam lines
- Ethernet grew from Xerox **3 Mbps** coax to **IEEE 802.3** and displaced Token Ring, FDDI, and ARCNET on wired LANs.
- Shared coax (**10BASE5/2**) dies on **one cable fault**; **10BASE-T** hubs and **10BASE-F** fiber (noise, distance, **harder tapping**) were the answers at 10 Mbps.
- MAC is **CSMA/CD** with **jam**, **binary exponential backoff**, and a **64-byte floor** so collisions are **heard in 2T**.
- Fast Ethernet is the **same frames and MAC** with **10 ns** bits and **~100 m** copper reach, standardized as **802.3u**; **100VG-AnyLAN** lost.
- Copper PHYs are **T4 (Cat 3)** and **TX (Cat 5, full duplex)**; fiber PHYs cover **short, long, bidirectional-single-fiber, and 10 km** plants, glued to MAC by **MII + PCS/PMA/PMD**.


---
