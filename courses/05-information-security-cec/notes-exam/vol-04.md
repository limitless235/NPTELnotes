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
