# Computer Network Reference Models

**Module 04**  
Duration: 31:46  
Video: https://www.youtube.com/watch?v=i7nPyb1c-d4

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr. Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:16]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:23]** University of Science and Technology Hisar harana in this lecture we will

**[0:30]** study about TCP IP reference model first of all please see the contents which I

**[0:37]** shall cover after covering brief introduction about TCP IP reference model I shall take up its layered

**[0:47]** protocol architecture which will be followed by detailed

**[0:53]** explanation about protocols in tcpip reference model

**[1:01]** 1 minute, 1 second the Internet Protocol suit commonly known as TCP IP reference model is the

**[1:08]** computer networking model and set of communication protocols used on the

**[1:15]** internet it is commonly known as TCP IP because its most important protocols the

**[1:24]** transmission control protocol TCP and the Internet Protocol protocol IP were

**[1:32]** the first networking protocols defined in this standard the TCP IP reference model is

**[1:42]** the network model used in the current Internet architecture it has its origin back in

**[1:51]** the late 1960s with the grandfather of the internet the

**[1:58]** arpanet this was was a research Network sponsored by the Department of Defense

**[2:05]** in the United States and due to this reason it was also called DOD

**[2:14]** model the major design goals of tcpip reference model

**[2:20]** were ability to connect multiple networks together

**[2:26]** seamlessly ability for connections to remain intact as long as the source and

**[2:34]** destination machines are functioning to be built on flexible

**[2:43]** architecture the TCP IP model and related protocol models are maintained

**[2:51]** by the internet engineering task force ietf the tcpip internet Pro protocol

**[3:00]** suit resulted from research and development conducted by defense

**[3:07]** Advanced research project agency DARPA in the late

**[3:13]** 1960s after initiating the pioneering arpanet in

**[3:19]** 1969 DARPA started work on a number of other data transmission technologies in

**[3:28]** 1972 Robert E KH joined the DARPA information

**[3:34]** processing technology office where he worked on both satellite packet networks

**[3:42]** and groundbased radio packet networks and recognized the value of being able

**[3:51]** to communicate across both in the spring of

**[3:58]** 1973 vnon serve the developer of the existing arpanet Network control program

**[4:06]** NCP protocol joined KH to work on open architecture interconnection models with

**[4:15]** the goal of Designing the next protocol generation for the arpanet by the summer of

**[4:23]** 1973 KH and surf had worked out a fundamental reformulation in which the differences between Network

**[4:33]** protocols were hidden by using a common inter Network protocol and instead of

**[4:41]** the network being responsible for reliability as in the aranet the host

**[4:49]** became responsible the initial four computers connected to the network in the basic

**[4:57]** arpanet increased to several hundred in just a short time by linking

**[5:05]** universities research institutes and military installations with each other

**[5:13]** over Leed telephone lines as technologically different

**[5:20]** networks such as satellite Network and wireless networks were connected to the

**[5:26]** internet the originally implement ented protocols were soon overburdened by the data traffic

**[5:36]** translation required from one network to the other now let us see TCP IP reference

**[5:46]** model the actual TCP IP reference model consist of four layers that is layer 2

**[5:55]** to 5 as shown in figure these together together with the addition of the

**[6:01]** 6 minutes, 1 second physical layer that is layer one makes up the five layer hybrid TCP IP

**[6:09]** reference model lower most layer in TCP IP reference model is link layer which

**[6:17]** is also known as host to network layer above link layer is internet layer

**[6:25]** followed by transport layer topmost layer is application layer in

**[6:34]** tcpip reference model the link layer or host to network layer of the TCP IP

**[6:42]** reference model corresponds to the first two layers of the iso OSI reference

**[6:50]** model that is physical layer and data link layer its main task focuses on on

**[6:59]** the secure transmission of data packets of pulled bit sequences it is followed by the internet

**[7:09]** layer which corresponds to the network layer of the isoi reference

**[7:17]** model its main responsibility is to enable the data communication of Two end

**[7:24]** systems at a given location in the hetrogeneous communication ation Network

**[7:31]** the transport layer above it corresponds to the layer of the same name in the iso

**[7:39]** OSI reference model it enables two user programs on different computers in the

**[7:47]** communication Network to exchange reliable and connection oriented

**[7:54]** data the application layer of the TCP IP reference model Model includes the three

**[8:02]** upper layers of the iso OSI reference model and serves as an interface for the

**[8:10]** actual application programs that wish to communicate with each other over the

**[8:20]** network unlike the iso OSI reference model it was not conceived and planned

**[8:27]** theoretically but was derived from the protocols that had been put into practice on the

**[8:36]** internet the isoi protocols on the other hand were planned

**[8:43]** theoretically and adopted before protocols could be invented that

**[8:50]** implemented the different functions for the layers of the isoi reference model

**[8:59]** today isoi Protocols are no longer used and the tcpip reference model protocols

**[9:07]** which had been developed from practical application dominate the

**[9:15]** internet layered Communication in TCP IP reference model is as shown in figure

**[9:24]** here lower two layers link and internet are chained layers and upper two layers

**[9:33]** transport and application are end to endend layers where process to process

**[9:41]** communication takes place now we will see the task and the

**[9:49]** protocols of the individual layers of the TCP IP reference model first is link

**[9:57]** layer or Network to host layer the link layer is the lowest layer of the TCP I

**[10:06]** reference model the link layer defines the networking methods within the scope of

**[10:16]** the local network link on which host communicate without intervening

**[10:24]** routers the primary task of the link layer is the secure your transmission of

**[10:31]** individual data packets between two adjacent end

**[10:38]** systems this layer of the TCP IP reference model is normally subdivided into two further layers medium access

**[10:47]** control that is mac sublayer and logical link control that is LLC sublayer Mac

**[10:56]** sublayer regulates assess to the shared channels by defining a mechanism of

**[11:03]** allowing fair and efficient assess to all participants this includes methods

**[11:10]** for the discovery of collisions or their avoidance as many participants wish to

**[11:18]** transmit data at the same time LLC sublayer forms the data link layer of

**[11:25]** the landan it provides flow control and Link management data transmission errors must

**[11:34]** be recognized and if possible corrected the data is also subdivided

**[11:42]** into size limited data packets as per requirement in this layer important

**[11:50]** Protocols of the link layer of the TCP IP reference model most important Protocols of the

**[11:59]** the link layer of the TCP IP reference model are based on the i e 802 Lan

**[12:08]** standard these are Technologies such as ethernet i e

**[12:15]** 82.3 token ring i e 82.5 as well as different Wireless W

**[12:23]** land Technologies I 802.11 and many any more the most

**[12:31]** important Protocols of the link layer of the tcpip protocol family are ATM a

**[12:40]** synchronous transfer mode ATM which stands for a synchronous transfer mode

**[12:48]** which is a connection oriented packet switching Network protocol that breaks

**[12:55]** down and forward the data to be transported in a cells of a fixed

**[13:03]** size behind this design principle was the idea of providing time critical

**[13:10]** realtime data such as video or audio information together with regular data

**[13:19]** over a standardized protocol ARP address resolution protocol Within

**[13:29]** the help of the ARP protocol described in RFC 826 the MAC address of a host can be

**[13:39]** determined from the IP address in the Internet Protocol of the layer above it

**[13:48]** this is important if a data packet from the Internet is to be delivered to a

**[13:54]** local network whose Mac address must be determined from the stored IP address of

**[14:03]** the receiver for forwarding in the landan

**[14:10]** NDP neighbor Discovery protocol the functions of the NDP Protocols are very

**[14:17]** similar to the ARP protocol and serve to explore and discover further host in the

**[14:27]** local network in contrast to ARP NDP was developed for the next generation of the

**[14:36]** Internet Protocol IPv6 while ARP Works under the current

**[14:43]** version ipv4 lltd link layer topology Discovery the

**[14:53]** proprietary lltd protocol was developed by the Microsoft company for exploration

**[15:02]** of the present Network topology and verification of the guaranteed quality

**[15:10]** of service in a network PPP Point too

**[15:18]** protocol PPP is a simple protocol that serves the connection between two

**[15:26]** Network nodes PP p is used by the majority of Internet providers to offer

**[15:34]** their customers a dialup connection over a standard telephone line in the

**[15:43]** internet second layer in TCP IP model is internet layer the internet layer has the

**[15:52]** responsibility of sending packets across potentially multiple

**[16:00]** networks it requires sending data from The Source Network to the destination

**[16:08]** Network the Internet Protocol performs three basic

**[16:14]** functions host addressing and identification which is accomplished

**[16:21]** with a hierarchial IP addressing system packet routing which is the basic

**[16:29]** task of sending packets of data from source to destination by forwarding them

**[16:36]** to the next Network router closer to the Final

**[16:43]** Destination congestion control which is used for control of traffic

**[16:50]** congestion now let us see two basic protocols at internet layer the center

**[16:58]** Cal protocol of the internet layer is the Internet Protocol

**[17:05]** IP IP offers an unreliable data packet oriented endtoend

**[17:13]** information transmission it is responsible for fragmentation and

**[17:21]** defragmentation into IP data grams IP exist today in two versions

**[17:30]** ipv4 and ipv 6 in addition the protocol

**[17:37]** icmp internet control message protocol is implemented in the internet layer it

**[17:47]** is responsible for the notification of specific errors occurring during IP

**[17:55]** transmission as well as for further diagnos G nostic task such as sending

**[18:02]** Eco request to test the availability of a computer and the necessary

**[18:09]** transmission time icmp is a protocol that sits

**[18:15]** directly on the IP two different variations of the icmp protocol exist

**[18:23]** one for ipv4 and another for ipv 6 beside IP and

**[18:31]** icmp there are two more protocols that work on the internet layer of TCP IP

**[18:39]** protocol stack for example IP SEC Internet Protocol security it is

**[18:47]** comprised of a protocol suit to ensure the secure execution of Ip data traffic

**[18:57]** within a data stream IP datagrams can be authenticated and

**[19:04]** encrypted additionally included in IPC are protocols for the handling

**[19:12]** establishment and exchange of secure cryptography Keys called internet key

**[19:19]** exchange protocol Ike igmp internet group management protocol

**[19:28]** protol the igmp protocol carries out the administration of Ip multicast group of

**[19:37]** end systems within a tcpip network special multicast rotors

**[19:45]** administer address list of end systems that can be addressed commonly via one

**[19:53]** multicast address OSF open shortest path

**[20:00]** first the OSF protocol a link state routing protocol transmits IP datagrams

**[20:10]** within a single routing domain or autonomous system OSF is the most widely

**[20:18]** used routing protocol on the internet third layer in TCP IP model is

**[20:27]** transport layer the transport layer establishes a basic

**[20:33]** data channel that an application uses in its task specific data

**[20:41]** exchange the layer establishes process to process connectivity by providing

**[20:48]** endtoend services that are independent of the structure of user data and the logistics

**[20:57]** of exchanging in information for any particular specific

**[21:04]** purpose the protocol of the transport layer establishes a direct virtual

**[21:11]** endtoend communication connection to allow multiple application

**[21:18]** programs on the same computer every application program is assigned a port

**[21:25]** number to provide unique identification on the transport layer

**[21:33]** every unit of data sent must contain the port number of the sender and the

**[21:40]** receiver in order to be transmitted correctly together with the IP address

**[21:48]** the port number defines what is commonly known as Network socket a unique

**[21:55]** connection end point in the network work endtoend message transmission or

**[22:02]** connecting applications at the transport layer can be categorized as either

**[22:09]** connection oriented which is implemented in TCP or connectionless implemented in

**[22:18]** UDP the transport control protocol TCP is a core element of the Internet

**[22:25]** Protocol architecture and the most most popular protocol of the transport layer

**[22:32]** in the TCP IP reference model standardized as RFC

**[22:40]** 793 it carries out a reliable connection oriented bidirectional data exchange

**[22:48]** between two end systems TCP enables the establishment of virtual networks next

**[22:57]** the user data protocol UDP is the second most prominent protocol of the transport

**[23:05]** layer standardized as RFC 768 it transmits independent data units

**[23:13]** known as datagram between application programs that reside on different

**[23:20]** computers in networks the transmission is unreliable possibly combined

**[23:29]** with data loss proliferation of datagrams and changes in sequence the

**[23:36]** datagrams recognized as false are discarded by UDP and do not even reach

**[23:44]** the receiver in comparison to TCP UDP is clearly less complex which is reflected

**[23:53]** in its increased data throughput but UD DP suffers a dramatic

**[24:00]** loss of reliability and security other important Protocols of

**[24:08]** the transport layer are dccp that is datagram congestion control protocol

**[24:16]** which is a message oriented protocol of the transport layer in addition to

**[24:23]** reliably establishing and terminating connections it also distributes overload

**[24:32]** notifications it provides overload or congestion control and can be used for

**[24:39]** the negotiation of transmission parameters RSVP that is resource reservation

**[24:49]** protocol which is used for the request and reservation of network resources

**[24:57]** using IP to transmit data streams it is

**[25:03]** not intended for the actual data transport and bears a similarity to the

**[25:11]** mcmp and igmp protocols at the internet layer RSVP can be implemented by end

**[25:21]** systems as well as routers without having to reserve and maintain specified

**[25:29]** service qualities TLS that is transport layer

**[25:36]** security is predecessor of the secure socket layer protocol

**[25:43]** SSL TLS supplies cryptographic protocols for secure data transport in Internet

**[25:53]** individual TCP segments are encrypted by T LS and

**[26:01]** 26 minutes, 1 second SSL TLS provides protocols for the negotiation of transmission parameters

**[26:09]** for the exchange of cryptographic keys and authentication as well as for encryption

**[26:18]** and digital signature SCP that is stream control

**[26:25]** transmission protocol is a proposal for a highly scalable and performance

**[26:32]** version of the original TCP protocol which is reliable connection oriented

**[26:40]** and is specialized in transmitting large amounts of data next we move on to last

**[26:50]** layer of TCP IP model that is application layer the functions on the

**[26:56]** application layer in the TCP IP reference model can be mapped onto layer

**[27:03]** 5 to 7 in the iso OSI reference model

**[27:10]** the application layer primarily functions as an interface for the actual

**[27:17]** application programs wishing to communicate over the network a few of the many important

**[27:26]** Protocols of the application layer located in the tcpip protocol family are

**[27:34]** tnet that is tet type Network which is defined as RFC

**[27:41]** 854 which allows the setup of an interactive bidirectional communication

**[27:48]** connection to a remote computer through a command line

**[27:55]** interface FTP that is file transfer protocol defined by RFC

**[28:03]** 959 facilitates the transmission and manipulation of data between two

**[28:11]** computers connected over a tcpip network FTP functions according to

**[28:18]** the client server Paradigm a client initiates the connection and request a service the

**[28:27]** server takes the connection request and answers the service

**[28:34]** request SMTP that is simple mail transfer protocol defined by RFC

**[28:42]** 821 is a simple structured protocol for the transmission of electronic mail on

**[28:49]** the internet HTTP that is hyper text

**[28:55]** transport protocol defined by RFC 2616 is used for data transmission in

**[29:04]** the world wide web just as many other Protocols of the application layer it

**[29:12]** works according to the client server Paradigm and is based on the reliable transport protocol

**[29:21]** TCP RPC that is remote procedure call defined by RFC

**[29:29]** 1057 and RFC 5531 is used for interprocess

**[29:36]** communication that allows a computer program to call an external sub rotine

**[29:43]** located in another addressing area DNS that is domain name system

**[29:52]** establishes a name and directory service that delivers the assignment of readable

**[30:00]** and system names to IP addresses for all participating systems on the

**[30:08]** internet SNMP that is simple mail Network management protocol defined in

**[30:17]** 341 RFC helps Network Management Systems monitor administer and control

**[30:27]** individual ual systems connected to the network RTP that is realtime transport

**[30:36]** protocol defined by rfc1 189 is used for transmission of real time audio and

**[30:46]** video data over internet so friends this was about TCP

**[30:53]** IP reference model in this lecture we first discussed about introductory

**[31:00]** concepts of TCP IP reference model which was followed by layered protocol

**[31:08]** architecture of tcpip reference model in the end we discussed different protocols

**[31:17]** at different layers of this model thank you

**[31:28]** a

**[31:35]** [Music]
