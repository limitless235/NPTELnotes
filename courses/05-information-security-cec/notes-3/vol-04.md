# Volume 04 — M36–M47

> Information Security (CEC) · SWAYAM / CEC Information Security
> **notes-3** — concept exam notes (definitions & what things do). Breadth over lab depth.

---

## M36: Introduction to Mobile IP and Addressing

### Learning focus
- Explain why classic IP prefixes break when a host moves, and why DHCP-only renumbering is not enough.
- Define home address vs care-of address and the roles of home agent, foreign agent, and collocated care-of address.
- Describe agent discovery (advertisement vs solicitation) and the agent-advertisement extension fields.
- Walk registration request/reply and the four-path data-transfer process (proxy ARP + tunneling).
- Distinguish double crossing (2X) from triangle (dog-leg) routing and the binding-cache fix plus its stale-cache problem.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Home address | Permanent address tying the host to its home network |
| Care-of address | Temporary address on the foreign network |
| Collocated care-of address | Care-of address when the mobile host is its own foreign agent (often via DHCP) |
| Home agent | Application-layer agent, usually a home-network router, that intercepts and tunnels |
| Foreign agent | Application-layer agent on the visited network that delivers tunneled packets |
| Agent advertisement | ICMP router advertisement plus type-16 extension (care-of list on FA) |
| Agent solicitation | ICMP request for an agent when advertisements are missing |
| Proxy ARP | How the home agent impersonates the mobile host on the home LAN |
| Tunneling | Home agent encapsulates the original IP packet to the foreign agent |
| Double crossing (2X) | Remote and mobile on the same net; reply path still detours via home |
| Triangle / dog-leg routing | Remote → home agent → mobile instead of a direct path |
| Binding / warning | Cache CoA at the correspondent; invalidate it after a move |

### Exam lines
- IP prefixes assume a **fixed** attachment point; DHCP renumbering breaks configs, DNS, and **in-flight connections**.
- Mobile IP keeps a **permanent home address** plus a **changing care-of address**, with HA/FA (or a collocated CoA) hiding the move.
- Discovery (ICMP advertisement type **16** / solicitation) then registration (type **1**, lifetime zeros = deregister) then four-path transfer with **proxy ARP** and **IP-in-IP**.
- Transparency is complete for the correspondent — and that is why **2X** and **triangle routing** waste path length.
- Binding caches can shortcut the triangle until the host moves; then the home agent must **warn**.


---

## M37: Cloud Computing Architecture

### Learning focus
- Define cloud computing versus local storage and versus a “simple remote machine.”
- Recite the essential characteristics without which, the lecture says, a service is not a cloud.
- Contrast private, public, community, and hybrid deployment, including cloud bursting.
- Distinguish SaaS, PaaS, and IaaS (SPI) with the examples given (CRM, App Engine, Azure, AWS).
- Draw the four-layer architecture and state which layers fall under SLAs.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Cloud | Metaphor for Internet-based, elastic, metered remote compute — not a simple remote PC |
| On-demand self-service | Customer provisions without a human intermediary |
| Broad network access | Browser, desktop app, or mobile (e.g. iPhone apps) from anywhere |
| Resource pooling | Multi-tenant dynamic assignment; location opaque except region/country |
| Rapid elasticity | Expand and release pools as demand changes |
| Measured service | Metering and audited pay-per-use reports |
| Private / public / community / hybrid | Four deployment models |
| Cloud bursting | Hybrid spike handling by drawing public-cloud capacity |
| SaaS / PaaS / IaaS (SPI) | App / platform / infrastructure service models |
| Thin vs thick client | Dependent low-power vs adequate local processing |
| SLA | Contract whose QoS penalties apply to management and hardware layers, not the user’s Internet path |
| OpenStack | Example stack for private-cloud create/deploy/manage |

### Exam lines
- Cloud is Internet access to pooled, elastic, metered resources — **hire and pay for consumption**, not a new local box.
- **All** listed essential characteristics are required, or it is **not** cloud computing.
- Choose deployment by control and community: private for mission-critical (still disaster/insider-prone), public for scale/cost (Google example), community for shared concerns (banks/traders), hybrid for bursting and mixed sensitivity.
- **SPI:** SaaS uses apps; PaaS deploys onto a vendor-managed stack (App Engine, Azure); IaaS rents raw resources (AWS). Bring-your-own package → **IaaS not PaaS**.
- Four layers from client device to data center; **network is outside SLAs**, **management and hardware are inside**, with hardware affecting penalties most.


---

## M38: Security in Cloud Computing

### Learning focus
- Define cloud computing security as procedures, processes, and standards spanning physical and logical issues in SaaS/PaaS/IaaS and public/private/hybrid delivery.
- List data-security and virtual-data-center challenges (multi-tenancy, EU privacy, disk wipe standards, loss of visibility, provider insiders, hypervisor I/O).
- Enumerate cloud **network** challenges from guaranteed bandwidth through location-dependent VLANs.
- Explain how security responsibility shifts as capabilities (and risks) are inherited up the SPI stack.
- Detail SaaS, PaaS, and IaaS (especially private-cloud) security issues named in the lecture.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Cloud computing security | Procedures, processes, and standards for assurance in cloud environments |
| Trust path | Dependency among parties in Internet applications such as e-commerce |
| New insider | Provider staff who can see/control customer data without being company employees |
| Sticky services | Provider lock-in that makes leaving (e.g. incompatible storage APIs) hard |
| Hypervisor | Translation layer whose I/O and security model must not be assumed safe |
| Broadcast-domain abstraction | Missing cloud-network feature that forces application rewrites |
| XML encryption / WS-Security / SSL / TLS | In-transit protections listed for SaaS |
| Amazon S3 | Example where **data at rest are unencrypted by default** |
| CIA | Confidentiality, integrity, availability — QoS on virtual networks hits **availability** |
| Active Directory | Example traditional authentication repository that private cloud outgrows |

### Exam lines
- Cloud security is **physical and logical**, across **SPI** and **public/private/hybrid**, and must answer **where data live and who can see them**.
- Putting data off-premises raises **multi-tenancy, EU privacy, wipe standards, lost SIEM feeds, and provider insiders**.
- Virtual data centers hide load-time failures: hypervisor I/O, **app-unaware** VMs, huge disk images, and **portable images flooding storage networks**.
- Cloud networks struggle with **SLA bandwidth**, **appliance insertion**, **per-switch policy**, **protocol zoo**, **no broadcast domain**, **cloud IPs**, and **VLAN/port location binding**.
- **Risks inherit up the stack**; the lower the provider’s security cutoff, the more the customer must implement. SaaS adds browser/transit/locality/sticky/backup issues (encrypt S3 yourself); PaaS adds object isolation and privacy; IaaS/private cloud still has **hypervisor, awkward internal multi-tenancy, IAM, and virtual-network CIA**.
- Security is required at **every interface** among virtualized hardware, infrastructure, platforms, and business apps.


---

## M39: GSM Architecture

### Learning focus
- Place GSM as the dominant 2G digital cellular standard (CEPT GSM → ETSI → 3GPP) and list GSM900 / DCS1800 / PCS1900 bands.
- Partition the network into RSS, NSS, and OSS and name the A, Abis, Um, and O interfaces.
- Identify MS hardware vs SIM identifiers (IMEI, IMSI, PIN/PUK, Ki, Kc, TMSI, LAI).
- Explain MSC, HLR, VLR, EIR, AuC, GMSC, and SMS gateways, including HLR/VLR hierarchy.
- Classify GSM teleservices, bearer services (9.6 kbps, HSCSD, GPRS), and supplementary services (CLIP/CLIR, AoC, CUG, …).

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| GSM | 2G digital cellular; ~70% share; 800+ million users in 190+ countries |
| RSS / NSS / OSS | Radio, switching, and operation subsystems |
| Um / Abis / A / O | MS–BTS radio; BTS–BSC; BSS–MSC (PCM-30); management (SS7/X.25) |
| IMEI / IMSI | Equipment identity (in hardware) vs subscriber identity (on SIM) |
| PIN / PUK / Ki / Kc | Unlock SIM; unblock after 3 PIN fails; auth key; cipher key |
| TMSI / LAI | Temporary subscriber ID and location-area ID stored while camped |
| HLR / VLR | Permanent user DB vs per-MSC visitor copy (cuts long-distance signaling) |
| AuC / EIR | Auth/cipher secrets; IMEI white/black/grey lists (blacklists not shared across operators) |
| GMSC / SMS-GMSC / SMS-IWMSC | Incoming voice routing; SMS toward MS; SMS from MS |
| Teleservice / bearer / supplementary | Speech/SMS/fax; 9.6 kbps data path (HSCSD, GPRS); extras like CLIP and CUG |
| MSISDN / MSRN | Directory number vs routing number obtained from HLR |

### Exam lines
- GSM is Europe’s answer to fragmented analog 1G: **one digital 2G** under ETSI then **3GPP**, built to **roam** with **ISDN-like voice**, later band-extended as GSM900 / DCS1800 / PCS1900.
- Users only see **MS + BTS antennas**; the real machine is **RSS (Um/Abis) + NSS (A, HLR/VLR/MSC) + OSS (O, TMN)**.
- Identity splits: **IMEI** (stolen phone) vs **IMSI/SIM** (stolen credentials); **VLR copies HLR** so the home database is not hit on every local event.
- Incoming calls go **GMSC → HLR (MSRN) → visited MSC**; SMS has analogous **GMSC/IWMSC** pair.
- Services stack as **teleservices (13 kbps speech, SMS, fax)**, **bearers (9.6 kbps, then HSCSD/GPRS)**, and a long list of **supplementary** controls (CLIP/CLIR, barring, CUGs, AoC).
- EIR blacklists **do not sync between operators**, so a stolen handset may still work on another network.


---

## M40: MANET - I

### Learning focus
- Contrast wired networks with wireless networks and name the three wireless types the lecture uses: fixed wireless, wireless with fixed access points, and MANET.
- Define a mobile ad hoc network as an infrastructure-less, IP-based radio network in which nodes act as both hosts and routers.
- List MANET characteristics (autonomous terminals, distributed operation, multi-hop routing, dynamic topology, limited resources and security, scalability, low bandwidth).
- State the open challenges the instructor listed: scalability, routing, QoS, the client–server model shift, security, energy conservation, node cooperation, and interoperation.
- Recall the application families taught: military, home/office/education, VANET, wireless sensor networks, wireless mesh networks, disaster relief, and personal area networks.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| MANET | Infrastructure-less, IP-based radio network of mobile nodes that route for one another |
| Access point | Fixed infrastructure node that mobile hosts associate with in the non-ad-hoc wireless type |
| Multi-hop | Relaying through intermediate nodes when source and destination are not in direct range |
| Dynamic topology | Unpredictable, rapid link change because nodes move freely |
| QoS | Guaranteed performance for a flow: delay, jitter, bandwidth, packet-loss probability |
| VANET | Vehicular ad hoc network; V2V between vehicles, V2I via roadside units |
| WSN | Sensor-node network treated as a low-mobility special case of MANET, with sink nodes |
| Wireless mesh | Many 802.11a/b/g mesh routers sharing an Internet connection by dynamic hop-by-hop routing |
| PAN | Person-centred short-range network, including Bluetooth wire-replacement |

### Exam lines
- Wireless freedom of movement yields three classes; MANET is the infrastructure-less extreme.
- Every MANET node is potentially a host **and** a router; A–C communication may require B.
- Design is dominated by dynamics, scarce energy/CPU/bandwidth, and the absence of a place to hang access control.
- Routing, QoS, naming/addressing without servers, security without a CA, and merging dissimilar networks are still open.
- The same idea covers battlefields, classrooms, vehicles, sensors, city-scale meshes, disasters, and PANs.


---

## M41: MANET – Routing Protocols

### Learning focus
- Define what a routing protocol does in a MANET and why metrics and information exchange matter under changing conditions.
- Distinguish **reactive (on-demand)**, **proactive (table-driven)**, and **hybrid** routing, including the bandwidth and latency trade-offs the lecture stated.
- Explain **AODV** (RFC 3561): RREQ / RREP / RERR, expanding-ring TTL, sequence numbers, precursor lists, and the three RERR circumstances.
- Explain **OLSR** as a proactive protocol that uses **multipoint relays (MPRs)**, Hello-based neighbour sensing, MPR flooding, topology-control (TC) messages, and Dijkstra shortest paths.
- Explain **TORA** as a hybrid protocol that builds a **DAG** of **heights** using QUERY, UPDATE, and CLEAR, with route creation, five maintenance cases, and route deletion.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| Reactive / on-demand | Build a route only when needed; higher search latency |
| Proactive / table-driven | Continuously maintain routes to all nodes via periodic control traffic |
| Hybrid | Proactive backbone plus reactive flooding for extra demand |
| AODV | Ad hoc On-Demand Distance Vector (RFC 3561); RREQ, RREP, RERR |
| Expanding ring | Increase RREQ TTL on retransmission if no reply |
| Precursor list | Neighbours that likely use this node as next hop; used to send RERR |
| OLSR | Optimized Link State Routing; proactive, MPR-optimized link state |
| MPR | Multipoint relay: selected one-hop neighbour that forwards floods to two-hop neighbours |
| TC message | Topology-control advertisement from nodes with a non-empty MPR selector set |
| TORA | Temporally-Ordered Routing Algorithm; DAG of ordered heights, loop-free multiple paths |
| QUERY / UPDATE / CLEAR | TORA control packets for create, maintain, and delete routes |

### Exam lines
- MANET routing is the algorithm-as-protocol that tracks a moving graph with chosen metrics.
- Reactive protocols save bandwidth but pay **initial delay**; proactive protocols start sessions quickly but **waste bandwidth** and recover slowly from failures; hybrid needs **foreknowledge** of size and demand.
- AODV finds a path when RREQ hits the destination or a node with a valid cache, replies along reverse routes, and uses RERR plus precursor lists when links die.
- OLSR shrinks classical link state by letting only MPRs rebroadcast and by advertising only MPR-selector links; Dijkstra then yields hop-shortest routes.
- TORA orients a DAG with heights so traffic is loop-free; QUERY/UPDATE build routes, five cases repair them, and CLEAR erases a partition.


---

## M42: 3G Network and Security

### Learning focus
- Place 3G in the ITU **IMT-2000** story (spectrum, pre-commercial and commercial launches, India’s MTNL/BSNL path, and the GPRS → EDGE transition).
- State what 3G is: third-generation mobile telecommunications meeting **IMT-2000**, with at least **200 kbps** and later 3.5G / 3.75G broadband rates.
- List 3G capabilities, applications, and services (mobile Internet, HTML vs plain-text email, SMS/MMS/IM plus presence).
- Sketch 3G architecture: **RAN** (Node B, RNC) and **core** (packet domain SGSN/GGSN, circuit domain MSC, CGF) over **ATM** **Iu/Iub/Iur** with AAL2 voice and AAL5 data.
- Recall 3G security: CIA, KASUMI vs A5/1, IMSI/TMSI and false-base-station issues, and the **ETSI TS 121 133** threat classes.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| IMT-2000 | ITU name for 3G technical specifications |
| EDGE / EGPRS | Enhanced GPRS step before 3G; new 3G frequencies still need new infrastructure |
| RAN / Node B / RNC | Radio access network; Node B ≈ 2G BTS; RNC ≈ BSC (RRM, handover) |
| SGSN / GGSN / MSC / CGF | Packet core (as in GPRS), circuit MSC for voice, charging gateway |
| Iu / Iub / Iur | ATM RAN interfaces; Iu split CS (AAL2 voice) and PS (AAL5 data) |
| KASUMI | 3G block cipher replacing A5/1; still taught as having serious weaknesses |
| IMSI / TMSI | Subscriber identity; IMSI sent in clear when assigning TMSI |
| False BS | Rogue base station that camps the user away from legitimate paging |
| ETSI TS 121 133 | Specification used to classify 3G confidentiality, integrity, DoS, repudiation, and service-access threats |

### Exam lines
- 3G is IMT-2000: ≥200 kbps (later several Mbit/s), new spectrum and infrastructure, not just a software bump from EDGE.
- The architecture splits RAN (Node B + RNC) from a dual CS/PS core, with ATM AAL2/AAL5 on Iu.
- User-facing 3G is mobile Internet, email (spam/virus fears), SMS/MMS/IM+presence, and location services — with sharp regional MMS uptake differences.
- Mutual authentication is an improvement over earlier generations, but IMSI exposure, false base stations, optional encryption, and KASUMI weaknesses remain.
- ETSI TS 121 133 organises 3G threats around CIA plus repudiation and unauthorized service access.


---

## M43: 4G LTE

### Learning focus
- Define **LTE (Long Term Evolution)** as the 3GPP 4G standard on the GSM → UMTS path, aimed at ~10× 3G speeds via new DSP and modulation, and an **IP-based** architecture with lower latency.
- Place LTE among competing 4G candidates (**UMB**, **IEEE 802.16 / WiMAX**, **802.16m / WiMAX Advanced**) and **LTE Advanced (Release 10)**.
- Separate marketing “4G” (**HSPA**) from **4G LTE**, and state OFDM, peak-rate, and VoLTE/RCS benefits as taught.
- List LTE technical objectives (throughput, latency, simplified **E-UTRAN**, mobility) and the two resources required: a capable **network** and a capable **device**.
- Recall the lecture’s LTE security framing: confidentiality and integrity, plus research goals for comparing LTE cryptographic algorithms.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| LTE | Long Term Evolution; 3GPP 4G on the GSM/UMTS path |
| LTE Advanced | 3GPP **Release 10**, the release taught as qualifying as 4G |
| E-UTRAN | Simplified LTE radio architecture: no RNC, no CS domain, no DCH |
| HSPA | High Speed Packet Access — “4G” branding without LTE; faster 3G GSM, slower than LTE |
| OFDM | Orthogonal frequency-division multiplexing; why 4G is faster |
| VoLTE | Voice over LTE: IP voice on the LTE data network |
| RCS | Rich Communication Services launched from the native dialer |
| WiMAX / 802.16m | Competing 4G path (WirelessMAN-Advanced / WiMAX 2) |
| UMB | Ultra Mobile Broadband, another competing 4G standard |

### Exam lines
- LTE is 3GPP’s IP redesign of the GSM/UMTS family: DSP/OFDM speed, simpler E-UTRAN, sub-5 ms user-plane latency in the ideal case.
- Marketing “4G” may be HSPA; **4G LTE** is taught as the pure 4G form, still needing both network and device — and the right spectrum.
- VoLTE is not only HD codecs (8 vs 13 kbps) but RCS, faster setup, better battery than Skype-class OTT, and a path to VoWiFi and cross-carrier handset interoperability.
- Security is framed as CIA plus a research programme over LTE cryptographic algorithms, not a finished protocol walkthrough in this lecture.


---

## M44: 5G

### Learning focus
- Define **5G** as fifth-generation mobile/wireless broadband as the lecture presented it, including the **IEEE 802.11ac** claim and the generation path from 1G through 4G LTE.
- State **NGMN Alliance** rate, connection-count, spectral-efficiency, coverage, signalling, and **~1 ms latency** requirements.
- Describe the taught **all-IP 5G architecture**: user terminal plus multiple simultaneous **radio access technologies (RATs)**, software-defined radios, and terminal-side choice via middleware.
- Contrast 5G with 4G on speed, capacity (~1000×), latency, millimetre-wave vs existing bands, MIMO, and small cells.
- List benefits, device/network requirements, applications (IPv6, global coverage), disadvantages, and the “nanocore / 6G” closing remarks — all as taught.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| 5G | Fifth-generation mobile/wireless; lecture also ties it to IEEE 802.11ac and a 5 GHz signal |
| NGMN Alliance | Source of 5G rate, massive-IoT connection, spectral, coverage, and ~1 ms latency requirements |
| RAT | Radio access technology; each appears as an IP link; multiple active interfaces at once |
| MIMO | Multiple-input multiple-output, to boost shorter-range higher-frequency 5G signals |
| Millimetre wave | Very high frequencies (taught as 3–300 GHz): fast, little broadcast coexistence, poor through walls — hence small cells |
| LTE vs WiMAX | Competing 4G; LTE became the consistent standard 5G builds on |
| IPv6 | Addressing for mobile IP tied to network and geography in the 5G application vision |
| Nanocore | Speculative future 5G enhancement combined with AI |

### Exam lines
- 5G is taught as all-IP, multi-RAT, terminal-centric: the phone keeps several radios up and chooses a provider; networks handle mobility; vertical handovers are to be avoided.
- NGMN targets tens of thousands of users, massive sensor connections, better spectral/signalling efficiency, and about **1 ms** latency.
- Speed/capacity claims in the lecture range from 500+ Mbps typical, 1–10 Gbit/s peaks, ~1000× 4G capacity, and Huawei’s “100× fastest LTE” / sub-1 ms latency — with the caveat that **no universal standard existed yet**.
- Higher bands (up to 6 GHz and mmWave) buy rate but lose range, so MIMO and dense small cells (including bounce-off-surfaces coverage) are part of the story.
- Benefits (IoT, AR, film-in-a-second, bigger data plans) sit beside unsolved security/privacy, device replacement cost, and unfinished research.


---

## M45: VoIP Protocols

### Learning focus
- Define **VoIP** as packetized digital voice/multimedia over IP instead of circuit-switched TDM, and explain why IP alone is a poor realtime transport.
- Place VoIP against the **OSI** layered model and name the three signalling/control protocols taught: **ITU-T H.323**, **IETF SIP**, and **MGCP**.
- Trace sender-to-receiver processing: codecs **G.711, G.729, G.723**, RTP/UDP/IP headers, playout buffer, and SIP/H.323 for call setup/teardown.
- List **QoS** factors: delay (source, receiver, network), jitter, packet loss, echo, and throughput.
- Recall VoIP **threat classes** (DoS, sniffing, eavesdropping, spoofing, toll fraud, SPIT) and the **defences and deployment options** the instructor listed — not attack recipes.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| VoIP | Packet voice/multimedia over IP instead of circuit TDM |
| H.323 | ITU-T umbrella (H.225, H.235, H.245, H.450) with RTP/RTCP over UDP and TLS setup |
| SIP | IETF RFC 3261 text request/response signalling; needs TLS/IPsec because proxies must see headers |
| MGCP | RFC 3435 gateway control; IPsec AH/ESP between media gateway and MGC |
| G.711 / G.729 / G.723 | Example voice codecs on the send path |
| Playout buffer | Receiver jitter buffer; late packets discarded |
| SPIT | Spam over Internet Telephony — real-time voice spam |
| Toll fraud | Unauthorized use of paid voice service, often via signalling or configuration abuse |
| PSTN | Public Switched Telephone Network; still required for number translation and non-VoIP users |

### Exam lines
- VoIP wins on TDM cost and voice–data integration, but IP is connectionless and offers no realtime guarantees — hence codecs, RTP, jitter buffers, and signalling (H.323, SIP, MGCP).
- H.323 is a full ITU stack with H.235 authentication variants and Diffie–Hellman; SIP is lightweight and **cannot hide routing headers from proxies**, so TLS/IPsec carry the security burden; MGCP assumes IPsec to the PSTN gateway.
- QoS is delay, jitter, loss, echo (electrical vs acoustic), and throughput — not a single number.
- Threats taught are DoS, sniffing, eavesdropping, caller-ID spoofing/phishing, toll fraud, and SPIT; responses are authentication, encryption, filtering/blacklists, firewalls, physical/port security, and user caution — not protocol exploits.
- Deployment spans USB adapters, softphones, dedicated phones/routers, and wireless LAN, with scalability, PSTN interworking, and incomplete encryption as the practical limits.


---

## M46: Introduction to DDoS

### Learning focus
- Distinguish **DoS** from **DDoS** and place both as attacks on **availability** in the CIA triad.
- Explain why Internet growth and a security-light original design made flooding and related availability attacks severe.
- State attacker **motives** and organisational **consequences** as listed in the lecture.
- Name the **protocol/architecture weaknesses** the instructor blamed (stateless forwarding, lack of authentication / IP spoofing, predictable TCP handshake, mimicry of legitimate users).
- Classify DDoS **as taught**: physical (layer 1), volumetric (layers 2–4), and application-layer (layers 5–7) — class names only, not operational recipes.

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| DoS | Denial of service: prevent legitimate users from using a service (availability) |
| DDoS | DoS whose traffic comes from **many sources**, amplifying impact and complicating defence |
| Bot / botnet | Compromised machines (masters, handlers, zombies) used as a distributed attack network |
| IP spoofing | Forged source addresses; hides origin and defeats simple identity-by-IP defences |
| SYN flooding | Volumetric class that leaves TCP connections **half-open** until timeout |
| Volumetric attack | Layers 2–4 congestion/bandwidth exhaustion |
| Application-layer DDoS | Layers 5–7: low network volume, high application/request load |
| Ping of Death | Named vulnerability class: oversized ICMP mishandled by some OSes; patchable |
| CIA | Confidentiality, integrity, availability — DDoS targets availability |

### Exam lines
- Availability was historically under-weighted; flooding proved it can bankrupt, embarrass, or politically coerce a victim.
- DDoS is harder than DoS because of **scale**, **legitimate-looking traffic**, and **spoofed identity**.
- The Internet’s **stateless forwarding**, **weak authentication**, **predictable TCP handshake**, and **easy mimicry of users** are the taught root causes — not a single bug.
- Classification is **physical vs volumetric vs application-layer**; named floods (MAC, ICMP, SYN, UDP, HTTP GET/POST) are **types**, not procedures.
- Patching stops some vulnerability DoS; **public-Internet flooding has no easy preventative**, and commercial tools have not closed the problem.


---

## M47: Defence to DDoS Attacks

### Learning focus
- Explain why **DDoS flooding** is hard to defend: easy launch, traffic similarity, IP spoofing, huge volume, many zombies, and Internet **hub-and-spoke** chokepoints.
- Separate **technical** vs **social** defence challenges (distributed response, missing incident data, no benchmarks, large-scale testing; deployment economics).
- List **goals of an ideal defence**: effectiveness, completeness, minimum collateral damage, low false positives, low cost.
- Name the four **defence modules**: prevention, detection, source identification, and reaction — as strategies, not attack methods.
- Recall the instructor’s **hardening tips** (filters, patches, unused services, quotas, baselines, physical security, integrity tools, redundancy, backups, passwords).

### Key terms
| Term | Meaning in this lecture |
|------|-------------------------|
| IP spoofing (defence view) | Makes new legitimate clients indistinguishable from attack initiators |
| Collateral damage | Legitimate traffic dropped or delayed by a defence |
| False positive | Defence treats a non-attack (e.g. flash crowd) as DDoS |
| Flash event | Sudden legitimate load that must be distinguished from DoS |
| SYN cookies | Example partial preventive for SYN floods; not complete by itself |
| Anomaly-based detection | Preferred DDoS detector; signatures change too often |
| Source identification | Finding origins even when addresses are forged |
| PlanetLab / Emulab | Named research testbeds; small-scale tests are not credible |
| Tripwire | Example integrity tool for detecting configuration-file changes |

### Exam lines
- Flooding looks like a “perfect crime”: cheap volume, spoofed identity, too many bots to punish, and hubs that can congest the whole Internet.
- A box next to the victim cannot keep up; real defence must be **distributed**, but **economics and reputation-secrecy** block the data, benchmarks, and deployment that research needs.
- Ideal properties are **actually stopping attacks**, covering **many attack styles**, **not punishing legitimate users** (including flash crowds), **few false alarms**, and **cost in line with benefit**.
- The operational pipeline is **prevent (especially anti-spoof near sources) → anomaly-detect → identify sources → react without collateral damage**.
- Everyday hygiene — filters, SYN-flood patches, turning off spare services, quotas, baselines, physical security, Tripwire, redundancy, backups, strong admin passwords — **reduces exposure**; it is **not** a complete DDoS solution, which the instructor says the market has not yet delivered.


---
