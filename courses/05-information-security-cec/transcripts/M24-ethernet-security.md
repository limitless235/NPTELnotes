# Ethernet Security

**Module 24**  
Duration: 34:12  
Video: https://www.youtube.com/watch?v=uaDXhq0k5sc

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Prof Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:15]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:23]** University of Science and Technology Hisar harana I welcome you all to the

**[0:30]** video lecture series of cyber security information security in this lecture we will study

**[0:38]** about ethernet security which is basically used to secure wired local

**[0:45]** area network and metropolitan area network first of all please see the

**[0:52]** contents which I shall cover after covering brief introduction about ethernet security I shall take up

**[1:01]** 1 minute, 1 second ethernet threats which will be followed by ethernet Security Solutions in last I shall take up Max

**[1:11]** SEC protocol for ethernet security so now let us

**[1:18]** start ethernet has its roots in the 1970s in a radio experiment called Aloha

**[1:26]** net developed under the direction of Norman Abramson at the University of

**[1:34]** Hawaii at about same time gerox Corporation created a landan with a data

**[1:41]** rate of 3 Mbps using a carrier sense multiple assess with Collision detection

**[1:49]** protocol csma by CD in 1980 the 10 Mbps ethernet version

**[1:58]** 1.0 spe specification was jointly released by digital Equipment

**[2:05]** Corporation Intel Corporation and Grox Corporation this was picked up by i e

**[2:15]** and became the i e 802.3 standard in

**[2:21]** 1983 a chunk of data transmitted by ethernet over the wire is called a frame

**[2:30]** on an Ethernet Network only a single node should be transmitting a frame at

**[2:37]** any time if multiple systems are transmitting simultaneously a collision will

**[2:45]** occur which can cause both signals to fail and require the systems to transmit

**[2:53]** their frames again these properties are summarized under ethernet

**[3:00]** designation as a carrier sense multiple assess with Collision detection CSM by

**[3:08]** CD protocol figure shows a wired network using ethernet ethernet supports both

**[3:18]** optical fiber and copper cabling yellow color infigure shows optical fiber and blue color shows

**[3:28]** twisted pair care CES in figure we can see Server form and pces connected to

**[3:36]** fast ethernet 100 Mbps network using switches the ethernet standards comprise

**[3:46]** several wiring and signaling variants of the OSI physical layer in use with

**[3:53]** ethernet the original 10 base 5 ethernet uses coxl cable as a shared medium while

**[4:03]** the newer ethernet variant use twisted pair and fiber optic links in

**[4:11]** conjunction with hubs or switches over the course of its history

**[4:18]** ethernet data transfer rates have been increased from the original 10 megabits

**[4:25]** per second to the latest 100 gbits per second with 400 gabs per second expected

**[4:35]** by early 2017 10 MVPs speed known as ethernet 100

**[4:42]** Mbps known as fast ethernet 1,000 Mbps known as gigabit Ethernet 10,000 Mbps

**[4:52]** speed as 10g ethernet and 100,000 Mbps as 100g

**[5:00]** ethernet 400 GB speed is also expected in

**[5:08]** 2017 ethernet is the only survivor of the wired Lan War it is hard to find an

**[5:16]** IP packet that has not passed over an Ethernet segment one important reason

**[5:23]** for this is ethernet's Simplicity and ease of configuration

**[5:30]** however ethernet has always been known to be an insecure technology recent successful malware

**[5:39]** attacks and the move toward cloud computing in data center demand that

**[5:46]** attention should be paid to the security aspect of ethernet now we shall move on to known

**[5:56]** ethernet related security threats the key historical reason for the security

**[6:04]** vulnerabilities of ethernet is that security has never been a major consideration in its

**[6:12]** design the basis for attack is gaining assess to the Target ethernet

**[6:19]** segment the attackers may be an Insider with full assess right or may have found

**[6:27]** an ethernet connection in a public public space before we describe the most

**[6:35]** prominent methods for attacking ethernet segment let us see how an attacker May utilize the network

**[6:43]** assess techniques used by attackers are learning about the private Network

**[6:51]** topology and the network traffic for use in attack gaining control over switch is

**[7:00]** routers or servers in the landan eaves

**[7:06]** dropping manipulating information disrupting the availability of the

**[7:15]** network the most prominent methods for attacking ethernet segments

**[7:22]** are network and system assess traffic confidentiality traffic

**[7:31]** Integrity denial of service system

**[7:37]** Security First of all let us see network and system assess type of

**[7:45]** attacks assess to the network is a prerequisite for attacks and a necessity

**[7:52]** for all types of attackers assess can be achieved by connecting equipment to the network or

**[8:01]** 8 minutes, 1 second by gaining control of existing resources various methods adopted for

**[8:08]** gaining unauthorized assess to network and system are unauthorized

**[8:16]** joins connect to an Ethernet segment by gaining assess to an unconnected port on

**[8:24]** a switch it can be done by gaining physical assess to the switch or gaining

**[8:32]** assess to a wall socket or removing the cable from a computer and plugging it

**[8:40]** into another computer or plugging in a switch between the existing computer and

**[8:47]** the socket unauthorized expansion of the

**[8:54]** network the architecture of the ethernet allows users to access spend the network

**[9:01]** 9 minutes, 1 second by installing their own switches or wireless access points which in turn

**[9:08]** allows other people join the network vland

**[9:15]** join if a switch listens for vand management protocol on host port a host

**[9:22]** can act as a switch and join all vlans on some switches

**[9:29]** the ports can be configured to not transmit VLAN management protocols but

**[9:36]** they will still listen for these protocols an attacker can probe the

**[9:42]** switch for hidden features like this vand tagging and

**[9:50]** hoping an attacker can create ethernet frames that have a ven tag and thus

**[9:57]** inject frames to V lanss to which they are not supposed to have access remote access to the

**[10:06]** landan assess to an Ethernet segment can be achieved by gaining higher layer

**[10:13]** access to a host on the segment for example by using social engineering and

**[10:20]** to get a user at the Target Network to open a remote system administration

**[10:28]** service which then connects to a host on the internet and enables the attackers to assess the

**[10:36]** ethernet layer switch control as previously mentioned switches

**[10:44]** are shipped with default or no passwords and the password can usually be

**[10:51]** physically reset if an attacker gains control of a switch traffic can be

**[10:58]** rerouted by switching links down claiming the STP route by Rising the

**[11:05]** priority of the switch or dose selected links second type of attack methods are

**[11:14]** traffic confidentiality traffic on the network can be useful in itself and also serve

**[11:23]** the attackers in search of Targets in such type of attack

**[11:30]** an attacker not only gains information being transmitted but also gets authentication information like

**[11:39]** passwords and network topology information that can be used for further

**[11:46]** purposes third type of attacks are of traffic Integrity type it is done by modifying traffic on

**[11:56]** the network for example an attacker can imitate A bank's web server to a user

**[12:05]** and imitate the user to the bank server and gain temporary control of the

**[12:12]** users's bank account different ways to modify traffic on the network are ARP

**[12:21]** and DHCP poisoning host capture traffic intended

**[12:28]** for another host post just by sending an ARP message to the sender with the

**[12:35]** intended receiver's IP address and the attacker's MAC address in a similar way a host can

**[12:44]** detect broadcast DHCP server request and raise the server to reply them first

**[12:53]** upon success the attackers can assign a Gateway and DNS server to the Target

**[13:00]** host along with its IP address and control the host traffic at

**[13:07]** will man in the middle if an attacker can direct traffic to pass through his node and that

**[13:17]** traffic is not protected by an Integrity verification mechanism the attacker can

**[13:24]** easily modify the traffic such attackers are called man in the middle

**[13:31]** attack session hijacking ethernet is a stateless protocol but many higher level protocols

**[13:41]** create a session once a session is set up it is often assumed to be trusted and no

**[13:50]** further traffic verification is made if an attacker can Eaves drop on or

**[13:59]** otherwise gain enough information about an session the attacker can recreate the

**[14:06]** session and act like one end point next type of ethernet attacks are

**[14:13]** denial of service attack the attacker's motivation for dose attacks is not to gain access to

**[14:23]** data but to prevent its use the attacks can cause total loss of service or

**[14:31]** degradation of service a dose attack can be performed in various

**[14:37]** ways resource exhaust attack resource exhaust attack can Target the control

**[14:46]** and management planes of a switch by sending frames that require additional

**[14:52]** processing and handling protocol based dose

**[14:59]** the STP that makes a tree out of a mesh network is designed to be

**[15:06]** self-configuring an attacker that controls a node on the network can send

**[15:12]** STP messages and pretend to be a switch the whole switching Network can be

**[15:20]** brought to halt by flooding it with STP tcns or other STP control messages

**[15:30]** is next we shall see solutions to Common ethernet attacks the security of ethernet has

**[15:38]** been improved by standard organizations equipment vendors and the

**[15:45]** research Community traditionally ethernet lack of security has been

**[15:52]** solved by defining any ethernet segment as unsecure and require iring it to be

**[15:59]** placed inside a protected domain like placing it behind a firewall in a secure

**[16:07]** building with trusted staff higher layer cryptographic

**[16:12]** Solutions like IPC and TLs are used to solve the remaining

**[16:20]** issues cryptography carries its own cost and thus cannot be considered a

**[16:27]** universal Sol solution now let us see few existing Security

**[16:36]** Solutions first of all let us see router based security methods in this Solution

**[16:44]** One Central ethernet switch is replaced with an IP router the IP router

**[16:51]** partitions ethernet Network into several segments each new segment is a separate

**[17:00]** broadcast domain ARP STP VLAN and Mac address

**[17:07]** table based attacks are no longer possible between the segments inside the segment the same

**[17:16]** attacks remain feasible unless each switch is replaced with a multi-port

**[17:23]** router replacing a switch with a router will incur some cost

**[17:29]** an IP router requires configuration such as address allocation and default route

**[17:39]** configuration occasionally this can be automated as is the case for residential

**[17:45]** Broadband where the topology is clear to the assess router the router also

**[17:53]** prohibits easy Mobility a host may move in the ethernet Network nwor and keep its IP and Mac

**[18:01]** 18 minutes, 1 second addresses as it is the MAC address tables in switches are updated

**[18:09]** automatically compared to an ethernet switch an IP router provides a considerable amount of protection

**[18:18]** against other users connected to the same router second method is assess control

**[18:26]** method an attacker needs assess before being able to perform any attack

**[18:34]** untrusted entities can be kept out by limiting assess to the network or requiring

**[18:42]** authentication few methods of protection using assess control mechanism

**[18:49]** are physical protection of the network network equipment can be located in

**[18:56]** locked cabinets and rs and wiring installed inside walls to prevent unauthorized

**[19:04]** assess segmentation and V Lans inside ethernet the i e

**[19:12]** 802.1q virtual L mechanism provides a way to limit broadcast and other traffic

**[19:20]** to specific segments vlans are logically separate within the same physical installation

**[19:28]** and Define security domains inside one network individual

**[19:34]** vlans each host on the ethernet can also be placed into its own VLAN using i e

**[19:44]** 82.1 a q inq double tagging or vendor

**[19:50]** provided private vand switch configuration the PV Lan technique uses

**[19:58]** switch configuration to isolate host and only let their traffic pass to one

**[20:04]** promiscous port typically connected to a router and to the

**[20:10]** internet each host sees only itself and the host connected to the promiscous

**[20:18]** port and only a few VLAN IDs are needed at the trunks to indicate PV Lan traffic

**[20:27]** assess control list assess control list security feature is not part of the ethernet

**[20:37]** specification switch vendors have added various types of capabilities by

**[20:46]** themselves the ethernet frame does not have many features for a simple ethernet

**[20:52]** frame ACL the usable attribute are the senders or

**[20:59]** receiver's Mac address or The Ether type field assess can be limited based on Mac

**[21:07]** addresses but several service specific ACLS are commonly

**[21:14]** implemented authentication based assess control I E

**[21:21]** 802.1x port authentication supports several types of authentication credentials

**[21:29]** such as a username and password pair or a certificate and corresponding private

**[21:37]** key in i e 802.1x the client communicates with the

**[21:44]** authentication switch and the switch verifies the authentication from the

**[21:51]** database in authentication server as shown in figure 802 .1x uses extensible

**[22:02]** Authentication Protocol EAP that has broad support for different

**[22:08]** types of authentication methods and structures 802.1x authenticates a host at the

**[22:18]** beginning of a session attaching the MAC address to a specific port in the

**[22:26]** switch so this these were assess control based Security Solutions which limit the

**[22:34]** availability of targets to attackers now we shall see secure

**[22:40]** protocols for ethernet security the targets can also be made harder to reach

**[22:47]** by adding security features to protocols and such security Protocols are

**[22:54]** implemented by following methods encryption and integrity

**[23:02]** verification cryptography can solve integrity and confidentiality requirements i e

**[23:11]** 82.1 AE Max SEC forms encrypted connections between host and switches

**[23:21]** protecting confidentiality and integrity of the content in the frame

**[23:29]** deployment requires software installation and configuring authentication for each participating

**[23:39]** Network entity maxc provides protection against

**[23:45]** Intruders to the network preventing reading and modification of data

**[23:52]** frames we will see details of Max protocol later in this lecture

**[24:00]** securing address resolution protocol ARP creates a major

**[24:07]** vulnerability in the ethernet architecture information gained by DHCP snooping can be used to prevent ARP

**[24:17]** spoofing attacks by attaching Mac addresses to their corresponding IP

**[24:23]** addresses and ports based on information gained from DHCP messages DHCP snooping

**[24:34]** suffers from a potential lack of scope as a single switch cannot see the

**[24:40]** allocations made to host whose path to the DHCP server does not pass through this

**[24:49]** switch last type of security methods are security monitoring based solution

**[24:58]** in previous sections security techniques that are mostly proactive and once set

**[25:05]** do not require active participation from external systems or human

**[25:13]** interaction were described active Technologies enhance the protection of the network by

**[25:21]** implementing security monitoring based Solutions which are as explained

**[25:29]** below ethernet firewall and deep packet inspection firewalls are used to limit

**[25:37]** traffic between Network segments and can be considered more complex cases of

**[25:44]** assess control list including stateful features current firewall products can

**[25:53]** operate on all Network layers intrusion detection and prevention

**[26:01]** 26 minutes, 1 second systems intrusion detection system IDs and intrusion prevention system IPS use

**[26:10]** DPI to identify Network attacks usually from a signature library of known

**[26:18]** attacks such systems are rarely useful for ethernet Network

**[26:25]** protection planning configuration and Administration good Network

**[26:32]** Administration and practices can considerably influence the aspect of an

**[26:38]** Ethernet Network several of the Technical Solutions mentioned previously

**[26:45]** require configuration and constant adjustment at the network topology

**[26:53]** changes so these were techniques to secure ethernet Network now let us move

**[27:01]** 27 minutes, 1 second on to last part of this lecture that is maxc

**[27:07]** protocol Max SEC that is Max security defined by i e

**[27:14]** h2.1 AE standard allows authorized systems that attach to and interconnect

**[27:23]** lens in a network they maintain confidentiality of transmitted data and

**[27:30]** to take measures against frames transmitted or Modified by unauthorized

**[27:38]** devices maxc protocol facilitates following maintenance of correct network

**[27:46]** connectivity and services isolation of denial of service

**[27:53]** attacks localization of any source of network communication to the land of

**[28:01]** 28 minutes, 1 second origin construction of public networks offering service to unrelated or

**[28:08]** possibly mutually suspicious customers using shared land

**[28:15]** infrastructures secure communication between organizations using a landan for

**[28:23]** transmission incremental and non disruptive deployment protecting the most

**[28:31]** vulnerable Network components maxc operates in data part of

**[28:38]** ethernet frame as shown in figure destination address and Source

**[28:44]** address are same in mpdu or data part of

**[28:50]** ethernet frame SEC tag is inserted before data and I see V is inserted

**[29:00]** after data Max SEC comprises modification and additions to the max

**[29:08]** service data unit msdu conveyed by each frame transmitted

**[29:16]** by a user of the protocol the Mac security tag SE tag

**[29:24]** conveys parameters that identify the protocol and identify the key to be used to

**[29:32]** validate the received frame and provide replay protection these parameters are TAG

**[29:41]** control information TCI Association number a packet number

**[29:47]** PN and secure Channel identifier SCI the secure data field conveys the US

**[29:58]** user data encrypted if confidentiality is provided the icv ensures the Integrity

**[30:07]** of the Mac destination address Mac Source address SE tag and user

**[30:17]** data figure illustrates the transmission and reception of a frame by

**[30:24]** maxc on transmission side the frame name is first assigned to an security

**[30:31]** Association sa identified locally by its Association number the a is used to

**[30:40]** identify the security Association key s AK and the next packet number PN for

**[30:49]** that sa a the a sci and the PN encoded in the SE

**[30:58]** tag are given to protect unone transmitter

**[31:04]** side protect unit on transmitter side transmits icv and user secure data to

**[31:14]** receiver on reip of mexc frame the a sci

**[31:21]** and PN are extracted from the SE tag at receiver side

**[31:29]** the A and seci are used to assign the frame to an sa and hence to identify the

**[31:38]** security Association key s a k the validation function on receive

**[31:46]** side of the current Cipher suit is presented with the sack

**[31:54]** pnci the destination and source address of the frame together with the octets of

**[32:02]** the SE tag secure data and icv if the Integrity of the frame has

**[32:10]** been preserved and user data can be successfully decoded from the secure

**[32:17]** data a valid indication and the octets of the user data are returned if the receive frame

**[32:27]** is Val replay protection is applied by checking that the received PN is not less than

**[32:36]** the lowest acceptable PN for the sa if the check succeeds the parameter

**[32:43]** of the frame unchanged from those transmitted are presented to the max SEC

**[32:50]** receiver and lowest acceptable PN is updated and hence transmission is

**[32:58]** successfully accepted so friends this was about

**[33:04]** ethernet security finally summarizing we learned about introduction to ethernet

**[33:11]** security which was followed by ethernet security threats and then ethernet

**[33:18]** Security Solutions in the end we discussed working of very famous Max sex

**[33:27]** security protocol hope the contents explained in this lecture were understandable and

**[33:36]** helpful hope to see you again in next lecture till then goodbye enjoy the day

**[33:43]** thank you

**[33:46]** [Music]

**[33:58]** n

**[34:06]** [Music]
