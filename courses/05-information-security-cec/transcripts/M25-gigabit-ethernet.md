# Gigabit Ethernet

**Module 25**  
Duration: 32:22  
Video: https://www.youtube.com/watch?v=4rAKMS0KbJU

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:12]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:21]** University of Science and Technology Hisar harana I welcome you all to the video lecture series of cyber and

**[0:30]** information security in this lecture we will study about gigabit Ethernet which

**[0:37]** is basically used for data transmission on wired Lan at speed of 1,000 Mbps or 1

**[0:47]** gbps first of all please see the contents which I shall cover in this lecture after covering brief

**[0:55]** introduction about gigabit Ethernet I shall take up layer protocol architecture of gigabit Ethernet which

**[1:04]** will be followed by gigabit Ethernet physical specifications in last I shall take up

**[1:12]** frame format of gigabit Ethernet so now let us start one of the basic laws of network

**[1:21]** design is that we always underestimate the demand for increased

**[1:28]** capacity only a few years ago the idea of an Ethernet running at gigabit speeds

**[1:36]** would have seemed to be a little excessive but today's data intensive

**[1:43]** applications and increasing number of network users and new methods of

**[1:49]** information delivery are driving an ever increasing demand for more bandwidth

**[1:57]** when 100 Mbps Network working Technologies like fddi were first

**[2:04]** introduced most horizontal networks used 10 Mbps ethernet these new protocols

**[2:13]** were used primarily on backbones now that fast ethernet has

**[2:19]** taken over the horizontal Network Market a 100 Mbps backbone is in many cases

**[2:28]** insufficient to support the connections between switches that have to

**[2:34]** accommodate multiple fast ethernet networks gigabit Ethernet was developed

**[2:43]** to be the next generation of ethernet Network running at 1 gbps or 1000 Mbps

**[2:51]** speed that is 10 times the speed of fast ethernet now let us see i e standards

**[3:00]** for gigabit Ethernet the initial standard for

**[3:06]** gigabit Ethernet was produced by i e in June 1998 as i e

**[3:15]** 802.3 Zed and it required optical fiber for

**[3:22]** communication 802.3 Z is commonly referred to as thousand base X where X

**[3:30]** refers to either CX SX LX or non standard

**[3:38]** ZX i e 802.3ab ratified in 1999 defines gigabit Ethernet

**[3:47]** transmission over unshielded twisted pair UTP Cat 5 5e or six cable known as

**[3:57]** thousand base t with the rectification of 802.3 ab gigabit Ethernet became a

**[4:05]** desktop technology as organizations could use their existing copper cabling

**[4:13]** infrastructure i e 802.3 ah ratified in 2004 added two more

**[4:22]** gigabit Ethernet fiber standards thousand base LX 10 and 1,000 base

**[4:32]** bx10 this was part of a larger group of protocols known as ethernet in the first

**[4:40]** mile although it is still a relatively new technology gigabit Ethernet has

**[4:46]** virtually assured a place in the market like Fast ethernet it uses the same

**[4:54]** frame format frame size and media control method as used in standard 10

**[5:02]** MVPs ethernet fast ethernet has overtaken fddi because it prevented

**[5:09]** Network administrators from having to use a different protocol on the backbone

**[5:16]** in the same way gigabit Ethernet prevents administrators from having to

**[5:23]** use a different protocol like ATM for their backbones like all other ethernet Technologies the

**[5:32]** gigabit Ethernet standard is an extension of the base I

**[5:39]** 802.3 standard the specific design objectives for the gigabit Ethernet

**[5:46]** specification given to the task force includes the following should offer 10 times the

**[5:55]** bandwidth of fast ethernet must use the i e 802.3 ethernet frame

**[6:04]** format should employ the same half duplex and full duplex Mac operation

**[6:11]** schemes as its predecessor should be backward compatible with 10 Mbps and 100 Mbps

**[6:21]** ethernet Technologies should support all existing Network protocols used with the e

**[6:29]** ethernet family some of the more important features of gigabit Ethernet are

**[6:38]** outlined here supports the existing frame size and frame format of I 802.3

**[6:47]** ethernet which means it easily integrates with existing

**[6:53]** networks allows an easy upgrade path to High Performance networking while taking

**[7:01]** 7 minutes, 1 second advantage of existing Technologies and product knowledge supports full duplex mode for

**[7:10]** switch to switch and switch to end station connections most gigabit Ethernet

**[7:18]** products being shipped are full duplex in this mode there are no shared medium

**[7:26]** contention problems support s half duplex mode on shared network connections in this mode

**[7:35]** gigabit Ethernet use the same fundamental CSM by CD medium access

**[7:42]** method and traditional ethernet to resolve contention for the shared

**[7:50]** media a packet burst in feature was added to csma by CD that allows servers

**[7:58]** switches and other devices to send burst of small packets in order to fully

**[8:06]** utilize available bandwidth uses fiber optic cable or Cat

**[8:13]** 5 or cat 6 cable one of the main benefits of gigabit standard is that it offers a

**[8:22]** lowcost solution to solve the demands for bandwidth not only the cost of

**[8:29]** installation is low but the cost of network maintenance and management is

**[8:36]** minimum as well management and maintenance for gigabit Ethernet may be

**[8:44]** done by local network administrators in addition to the cost reduction benefit gigabit Ethernet may

**[8:53]** allow faster switching since gigabit Ethernet uses

**[9:00]** the same frame format it allows seamless integration of Lan man and

**[9:09]** when there is no need for packet fragmentation reassembling or address translation

**[9:18]** eliminating the need for routers that are much slower than switches now let us see layer protocol

**[9:27]** architecture of gigabit ethernet gigabit Ethernet supports 10

**[9:34]** 100 and 1,000 Mbps data rates it provides separate 8 bit wide receive and

**[9:43]** transmit data paths so it can support both full duplex as well as half duplex

**[9:51]** operation the GMI provides two media status signals one indicates presence of

**[9:59]** the carrier and the other indicates absence of collision the various layers of the

**[10:06]** gigabit Ethernet protocol architecture are shown in figure the gmii is the interface between

**[10:16]** the Mac layer and the physical layer it allows any physical layer to be used

**[10:23]** with the Mac layer it is an extension of the Mii media independent dependent

**[10:30]** interface used in Fast ethernet it uses the same management interface as

**[10:39]** Mii with the gmii it is possible to connect various media types such as shielded and

**[10:48]** unshielded twisted pair and single mode and multimode optical fiber while using

**[10:57]** the same Mac controller the GMI sits above three main

**[11:04]** Su layers the PCS the pmma and the PMD

**[11:10]** let us see each layer one by one PCS this layer of the GMI provides a

**[11:19]** uniform interface for all possible physical media it uses an 8B by 10B

**[11:28]** coding scheme just like fiber channel in this type of coding 10bit code groups

**[11:37]** represent group of eight bits the PCS sublayer also generates the carrier

**[11:44]** sense and collision detection indications for half duplex operation it

**[11:52]** manages the auto negotiation process by which a NIC communicates with the

**[11:59]** network to determine the network speed that is 10 100 or th000 Mbps and mode of

**[12:08]** operation as half duplex or full duplex PMA this sublayer provides a

**[12:17]** medium independent means for the PCS to support various serial bit oriented

**[12:25]** physical media this layer takes the 10bit code

**[12:31]** groups sent at 125 mahz by the PCS and

**[12:37]** converts them into serial format before Transmission in the reverse Direction it

**[12:46]** deserializes bits received from transmitter back into code groups for delivery to the

**[12:54]** PCS PMD this sublayer Maps the physical medium to the

**[13:02]** PCS this layer defines the physical layer signaling used for various media

**[13:09]** the medium dependent interface MDI a component of the PMD is the actual physical layer

**[13:18]** interface this layer defines the actual physical attachment such as connectors

**[13:25]** for different media types it defines different type of physical standards like

**[13:33]** 802.3 Z 802.3ab and 802.3

**[13:41]** a now after layer protocol architecture let us see physical specifications of gigabit

**[13:48]** Ethernet the physical layer of gigabit Ethernet describes the physical properties of the communication media as

**[13:57]** well as the electrical properties and interpretation of the exchanged

**[14:05]** signals following three types of media specified in the i e

**[14:11]** 802.3 z standard collectively known as thousand base X standard are as shown in

**[14:21]** table th base SX it is a fiber optic gigabit Ethernet standard it operates

**[14:30]** over multimode fiber using a 850 nanom near infrared light wavelength the

**[14:40]** specification allows for a maximum distance between end points of 220 M over

**[14:48]** 62.5 or 125 microm fiber with good quality

**[14:56]** Terminators thousand base SX will usually work over significantly longer

**[15:03]** distances modern 50 or 125 micrometer fiber can reliably extend the signal to

**[15:12]** 500 M or more this standard is highly popular for intra building links in

**[15:21]** large Office Buildings collocation facilities and carrier neutral internet

**[15:31]** exchanges thousand base LX it is a fiber optic gigabit Ethernet standard using a

**[15:39]** long wavelength laser its wavelength is 1270 to 135

**[15:47]** nanometer typically gigabit Ethernet lasers will be specified as having a

**[15:54]** 1300 or 1310 nanom wavelength thousand

**[16:00]** base LX is specified to work over a distance of up to 5 kilom over 10 microm

**[16:09]** single mode fiber in practice it will often operate correctly over a much

**[16:17]** greater distance many manufacturer will guarantee operations up to 10 or 20

**[16:25]** kilom provided that their equipment is used at both ends of the link for any

**[16:34]** link distance greater than 300 M the use of a special launch conditioning patch

**[16:42]** cord may be required this launches the laser at a precise offset from the center of the

**[16:51]** fiber which causes it to spread across the diameter of the fiber core

**[16:59]** base CX it is an initial standard for gigabit Ethernet connections with

**[17:06]** maximum distance of 25 M using balanced shielded twisted pair with a pinout

**[17:15]** different from, base T the short segment length is due to very high signal

**[17:23]** transmission rate although it is still used for specific appli ations for

**[17:30]** example ethernet connections between the blade servers and the switch modules but

**[17:37]** now thousand base T has succeeded it for Journal copper wiring

**[17:45]** use physical specifications under i e

**[17:51]** 802.3ab is, base t or TX as shown in table th000 Base

**[18:00]** TX the telecommunication industry Association TI created and promoted a version of

**[18:09]** thousand based T that was simpler to implement calling it th000 Base TX the

**[18:17]** simplified design would in theory have reduced the cost of the required

**[18:23]** Electronics by using only two pair in each Direction many thousand based T products are

**[18:32]** advertised as thousand based TX due to lack of knowledge that thousand Base DX

**[18:40]** is actually a different standard physical specifications under i e

**[18:47]** 802.3 AP also known as ethernet in the first mile is, base

**[18:56]** KX th000 base lx10 and th000 base bx10

**[19:03]** as shown in table th000 base KX it is part of the i e

**[19:11]** 802.3 AP standard for ethernet operation over electrical back planes this

**[19:20]** standard defines one to four lanes of black plane links one RX and one 1 TX

**[19:30]** differential pair per Lane at link bandwidth ranging

**[19:36]** from megabit to 10 gabit per

**[19:43]** second, base lx10 it was standardized 6 years after

**[19:49]** the initial gigabit fiber version as part of the ethernet in the first mile

**[19:57]** task group it is very similar to, base LX but

**[20:03]** achieves longer distances up to 10 km over a pair of 1310 nanometer wavelength

**[20:12]** single mode fiber due to higher quality Optics thousand base

**[20:21]** bx10 it is capable of up to 10 kilom over a single strand of single mode

**[20:29]** fiber with a different wavelength going in each Direction the terminals on each

**[20:36]** side of the fiber are not equal as the transmitting Downstream that is from the

**[20:43]** center of the network to the outside uses the 1490 nanometer wavelength and

**[20:51]** the one transmitting Upstream uses the 1310 nanometer w wav

**[20:59]** length few other known standard physical specifications are thousand base ex and

**[21:08]** thousand base ZX as shown in table thousand base ex is a nonn

**[21:16]** standard but industry accepted term to refer to gigabit Ethernet transmission

**[21:24]** it is very similar to th base lx10 but achieves longer distances up to 40 kilm

**[21:32]** over a pair of single mode fiber due to higher quality Optics then lx10 running

**[21:40]** on 1310 nanometer wavelength lasers thousand base ZX is a known

**[21:48]** standard but multivendor term to refer to gabit ethernet transmission

**[21:55]** using 1550 nanometer wavel length to achieve distances of at least 70 kilm

**[22:04]** over single mode fiber some vendors specify distances up

**[22:12]** to 120 kilom over single mode fiber sometimes called thousand base EZ

**[22:21]** X essentially four types of Hardware are needed to upgrade an existing ethernet

**[22:29]** or fast ethernet Network to gigabit Ethernet gigabit Ethernet network

**[22:36]** interface card Nic aggregating switches that connect a number of fast ethernet segments 2 gab

**[22:46]** ethernet gigabit Ethernet switches gigabit Ethernet

**[22:52]** repeaters now let us see CSM by CD and frame format of gigabit

**[23:02]** Ethernet the Mac layer of gigabit Ethernet uses the same csma by CD

**[23:08]** protocol as used in Ethernet the maximum length of a cable segment used to

**[23:15]** connect stations is limited by the CSM ycd protocol if two stations

**[23:23]** simultaneously detect an idle medium and start transmitting a collision

**[23:30]** occurs the i e 802.3 z Mac operation can

**[23:36]** be either half or full duplex mode a half duplex channel can receive and

**[23:44]** transmit but not at the same time with full duplex transmission it is possible

**[23:51]** to transmit and receive data at the same time in full duplex mode the gigabit

**[24:00]** Ethernet Mac uses the i e 802.3x full duplex specification which

**[24:08]** includes the i e 802.3x flow control in half duplex mode

**[24:16]** the gigabit Ethernet Mac uses the long established CSM by CD assess method the

**[24:25]** use of full duplex Transmission in gabit ethernet increases the overall bandwidth

**[24:32]** from 1 to 2 gbps for point2 Point links it also increases the maximum

**[24:41]** transmission distances for the particular media CSM by CD is not used for media

**[24:50]** access in full duplex gigabit Ethernet because the use of full duplex operation

**[24:58]** eliminates collisions on The Wire full duplex operation is best

**[25:06]** suited to Backbone transmission and as assess to highspeed servers the protocol

**[25:14]** supports both half and full duplex mode of operation an enhancement that was

**[25:23]** introduced in the switched version of 100 Mbps ethernet in the half duplex

**[25:29]** mode of operation the protocol maintains the CSM by CD feature of the original

**[25:38]** protocol now coming on to gigabit Ethernet frame format the gigabit

**[25:45]** Ethernet defines a basic data frame format that is required for all Mac

**[25:53]** implementations plus several additional optional formats that are used to extend

**[26:00]** the protocol's basic capability the basic data frame format

**[26:06]** contains the Seven Fields as shown in figure Preamble PR it consists of seven

**[26:14]** bytes the Preamble is an alternating pattern of ones and zeros that tells

**[26:22]** receiving stations that a frame is coming and that provides a means to

**[26:29]** synchronize the frame reception portion of receiving physical layers with the incoming bit

**[26:37]** stream start of frame s soof it consist of one byte the soff is an alternating

**[26:46]** pattern of ones and zeros ending with two consecutive one bits indicating that

**[26:54]** the next bit is the leftmost bit in the leftmost most bite of the destination

**[27:02]** address destination address da consist of six bytes the da field identifies

**[27:10]** which station should receive the frame the leftmost bit in the da field indicates whether the address is an

**[27:19]** individual address which is indicated by a zero or a group address which is indicated by a one

**[27:28]** the second bit from the left indicates whether the da is globally administered

**[27:34]** which is indicated by a zero or locally administered which is indicated by a

**[27:42]** one the remaining 46 bits are a uniquely assigned value that identifies a single

**[27:51]** station a defined group of stations or all stations on the

**[27:58]** Network Source address sa consist of six bytes the sa field identifies the

**[28:07]** sending station the essay is always an individual address and the leftmost bit

**[28:14]** in the essay field is always zero length oblique type it consist of

**[28:21]** two bytes this field indicates either the number of Mac clients data bytes that are contained in the data field of

**[28:30]** the frame or the frame type ID if the frame is assembled using an optional

**[28:38]** format if the length oque type field value is less than or equal to 1500 the

**[28:45]** number of LLC bytes in the data field is equal to the length or type field value

**[28:53]** if the length type field value is greater than 1500 the frame is an

**[28:59]** optional type frame and the length type field value identifies the particular

**[29:06]** type of frame being sent or received data it is a sequence of n

**[29:15]** bytes of any value where n is less than or equal to 1,500 if the length of the data field is

**[29:24]** less than 46 the data field must be extended by adding a filler or a pad sufficient

**[29:32]** to bring the data feied length to 46 bytes frame check sequence FCS it

**[29:41]** consist of four bytes this sequence contains a 32bit cyclic redundancy check CRC value

**[29:51]** which is created by the sending Mac and is recalculated by the receiving MEC to

**[29:58]** check for damaged frames the FCS is generated over the da sa length type and

**[30:08]** data fields extension gigabit Ethernet should be

**[30:15]** interoperable with existing 802.3 networks carrier extension is a

**[30:22]** way of maintaining i e 802.3 minimum and maximum frame sizes

**[30:30]** with meaningful cable distances for Carrier extended frame the known data extension symbols are

**[30:39]** included in the Collision window that is the entire extended frame is considered

**[30:46]** for collision and dropped however the frame check sequence

**[30:53]** FCS is calculated only on the original frame the extension symbols are removed

**[31:01]** 31 minutes, 1 second before the FCS is checked by the receiver so friends this was gigabit

**[31:11]** Ethernet finally summarizing we learned about introduction to gigabit Ethernet which

**[31:19]** was followed by layered protocol architecture of gigabit Ethernet and

**[31:25]** then gigabit Ethernet physical specifications in the end we discussed

**[31:33]** frame structure of gigabit Ethernet hope the contents explained in

**[31:40]** this lecture were understandable and helpful hope to see you in the next

**[31:46]** lecture till then goodbye enjoy the day thank you

**[31:52]** [Music]

**[32:15]** [Music]
