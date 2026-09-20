# MANET - I

**Module 40**  
Duration: 24:21  
Video: https://www.youtube.com/watch?v=7CR1_FBxJ6o

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Sunil Kumar, Department of Electrical and Computer Engineering, Punjab Agriculture University, Ludhiana

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:02]** [Music]

**[0:17]** Hello friends I welcome you all to the video lecture series of cyber security and information security in this lecture

**[0:26]** we will study about mobile ad hoc network first of all please see the contents which I shall

**[0:33]** cover after covering brief introduction about Manet I shall take up characteristics of Manet which will be

**[0:41]** followed by challenges of Manet networks in last I shall take up applications of

**[0:47]** mobile ad hoc network so now let us start like traditional wir networks

**[0:55]** wireless networks are formed by routers and hosts in a wireless network Network the routers are responsible for

**[1:02]** forwarding data packets in the network and hosts may be sources or syns of data flows the fundamental difference between

**[1:11]** wired and wireless networks is the way that the network components communicate a wi Network relies on

**[1:19]** physical cables to transfer data in a wireless network the communication between different network components can

**[1:26]** be either wired or Wireless since wireless communication does not have the constraint of physical

**[1:33]** cables it allows a certain freedom for hosts and routers in a wireless network to

**[1:40]** move this is one of the advantages of a wireless network according to the mobility of

**[1:47]** hosts and routers there are three different types of wireless networks fixed wireless

**[1:54]** network fixed hosts and routers use wireless channels to communicate at with each other and hence form a fixed

**[2:03]** wireless network an example is a wireless network formed by fixed network devices using directed

**[2:11]** antenas according to the figure two computers are communicating VI antenna signals through this they can send or

**[2:19]** receive the data wireless network with fixed exess points mobile hosts use wireless

**[2:28]** channels to communicate with fixed access points which may act as routers for those mobile hosts and to form a

**[2:36]** mobile network with fixed access points an example is the number of mobile laptop users in a building that

**[2:44]** access fixed access points according to the figure two or more laptops are sending or receiving

**[2:53]** the data via access points mobile ad hoc network a Manet is formed by mobile

**[3:01]** 3 minutes, 1 second hosts some of these mobile hosts are willing to forward packets for Neighbors examples include vehicle to vehicle and

**[3:10]** ship to ship networks that communicate with each other by relying on peer-to-peer routings according to figure All Ships

**[3:19]** create a network without any centralized Administration mechanism they can easily establish the link with any node within

**[3:28]** the network it is an infrastructur less IP based network of mobile and wireless machine

**[3:35]** nodes connected with radio the nodes of a Manet do not have centralized Administration mechanism it is known for

**[3:44]** its route aable Network properties which each node act as a router to forward the traffic to other specific node in the

**[3:54]** network according to figure mobiles and laptops creates a network without any centralized Administration in the

**[4:02]** simplest scenarios nodes may be able to communicate directly with each other for example when they are within Wireless

**[4:10]** transmission range of each other however ad hoc networks must also support communication between nodes that are

**[4:17]** only indirectly connected by a series of Wireless hopes through other nodes according to figure to establish

**[4:25]** communication between nodes A and C the network must enless the aid of node B to

**[4:32]** relay packets between them these circles indicate the nominal range of each nodes radio

**[4:39]** transceiver nodes A and C are not in direct transmission range of each other

**[4:46]** since a circle does not cover C characteristics of mobile ad hoc

**[4:54]** networks as compared to other wired or infrastructure waste wireless networks menet has the following characteristics

**[5:02]** autonomous terminal distributed operation multi hope routing lightweight

**[5:09]** terminals Dynamic topology self organization multi hoping resource

**[5:18]** conversation limited capacity and scalability autonomous terminal in

**[5:26]** manate each mobile terminal is an autonomous node which may function as a host or a router in other words beside

**[5:35]** the basic processing ability as a host the mobile nodes can also perform switching functions as a router so

**[5:42]** usually endpoints and switches are indistinguishable in Manet distributed operation since there is no background

**[5:50]** Network for the central control of the network operations the control and management of the network is distributed

**[5:58]** among the terminals the nodes involved in a Manet should collaborate Among Us themselves and each node acts as a relay

**[6:07]** as needed to implement functions like security and routing multi hope routing

**[6:14]** in multihop routing ad hoc routing algorithms can be single hope or multi hope they are based on different link

**[6:23]** layer attributes and routing protocols single hope Manet is simpler than multi hope in terms of structure and

**[6:32]** implementation while transferring data packets from a source to its destination out of the direct Wireless transmission

**[6:40]** range the packets should be forwarded by intermediate nodes lightweight terminals

**[6:47]** in most of the cases the Manet nodes are mobile devices with less CPU processing capability small memory size and low

**[6:56]** power storage such devices need optimized algorithms and mechanisms that implement the Computing and communicating

**[7:05]** functions Dynamic topology all nodes of Manet are free to move causing Network

**[7:12]** topology change rapidly at unpredictable times links between nodes are expected to break much more frequently than with

**[7:21]** wired and infrastructure based wireless networks self organization due to the lack of infrastructure or Central

**[7:29]** Administration nodes should be able to form themselves into a network multi hoping in a Manet nodes

**[7:39]** use a wireless channel to transmit data and due to the limited number of nodes neighbors intermediate nodes are used to

**[7:47]** relay the packets resource conservation in manner the nodes are limited in both energy Supply and processing

**[7:56]** power power conservation becomes a very important factor to be considered when designing a network therefore optimizing

**[8:05]** all operations May minimize the energy consumption limited security mobile ad hoc networks are more prone to security

**[8:13]** threats than wi networks or infrastructure based wireless networks because of their unique

**[8:21]** characteristics each mobile node in an ad hoc network and function as a router or packet forwarded for other nodes

**[8:30]** both legitimate users and malicious attackers can access the wireless Channel and there is no well place where

**[8:38]** exess control mechanisms can be deployed scalability in some applications mobile

**[8:45]** ad hoc networks May grow up to several thousand nodes mobile ad hoc networks suffer from scalability problems in

**[8:53]** Channel capacity because Channel capacities are very limited and maximum use of Channel capacity can be reached

**[9:01]** 9 minutes, 1 second faster due to the multi- hoping nature of mobile ad hoc networks their scalability is related to the routing

**[9:08]** protocols they employ low bandwidth these networks have lower capacity and shorter transmission range

**[9:16]** than fixed infrastructure networks the throughput of wireless communication is lesser than wir communication because of

**[9:25]** the effect of multiple excess fading noise and and interference conditions

**[9:31]** challenges of mobile ad hoc networks in last few years mobile ad hoc networking has been a popular field of

**[9:40]** communication almost every aspect of the network has been explored in one way or other at different level of problem the

**[9:49]** topics that need to be resolved are as follows scalability routing quality of service

**[9:58]** client server model model shift security energy conservation node cooperation

**[10:07]** interoperation scalability most of The Visionaries depicting applications which are anticipated to benefit from the adhoc

**[10:16]** technology take scalability as granted imagine for example the vision of

**[10:22]** universal Computing where networks can be of any size however it is unclear how

**[10:30]** such large networks can actually grow adhoc networks suffer by Nature from the

**[10:36]** scalability problems in capacity routing routing in Wireless ad hoc networks is non-trivial due to the highly Dynamic

**[10:46]** environment an ad hoc network is a collection of Wireless Mobile nodes dynamically forming a temporary Network

**[10:53]** without the use of any pre-existing Network infrastructure or centralized Administration

**[11:00]** in a typical ad hoc network mobile nodes come together for a period of time to exchange information while exchanging

**[11:08]** information the nodes may continue to move and so the network must be prepared to adapt continually to establish Roots

**[11:16]** among themselves without any outside support quality of service the

**[11:23]** heterogenity of existing internet applications has challenged Network designers who have built the network to

**[11:31]** provide best effort service only Voice live video and file transfer are just a

**[11:38]** few applications having vast and diverse requirements quality of service that is

**[11:45]** Q aware Solutions are being developed to meet the emerging requirements of these

**[11:51]** applications qos has to be guaranteed by the network to provide certain performance for a given flow or or a

**[11:59]** collection of flows in terms of Qs parameters such as delay Jitter

**[12:06]** bandwidth packet loss probability and so on despite the current research efforts

**[12:12]** in Qs areas Qs in ad hoc networks is still an unexplored area client server

**[12:20]** model in the internet a network client is typically configur to use a server as its partner for Network transactions the

**[12:29]** these servers can be found automatically or by a static configuration in and hoc networks however the network structure

**[12:37]** cannot be defined by collecting IP addresses into subnets there may not be servers but the demand for basic

**[12:45]** Services still exists address allocation name resolution authentication and the

**[12:52]** service location itself are just examples of basic Services which are needed but their location in the network

**[12:59]** is unknown and dynamically changes over time due to the infrastructure less nature of these networks and node

**[13:08]** Mobility a different addressing approach may be required in addition it is still not clear who will be responsible for

**[13:16]** managing various Network Services therefore while there have been vast research initiatives in this area the

**[13:24]** issue for shifting from the traditional client server model remains to be appropriately addressed security a vital

**[13:34]** issue that has to be addressed is the security in ad hoc networks applications like military and confidential meetings

**[13:42]** require High degree of security against enemies and active passive attackers ad hoc networks are

**[13:50]** particularly prone to malicious behavior lack of any centralized Network management or certification Authority

**[13:58]** makes these dynamically changing Wireless structures security is often considered

**[14:04]** to be the major Rod Block in commercial application interoperation when two autonomous ad

**[14:12]** hoc networks move into same area the interference with each other becomes unavoidable and the networks would

**[14:21]** recognize the situation and be merged however the issue of joining two networks is not trivial the networks may

**[14:28]** be used using different synchronization or even different Mac or routing protocols security also becomes a major

**[14:36]** concern can the networks adapt to the situation for example a military unit moving into an area covered by a sensor

**[14:45]** Network could be such a situation moving unit would probably be using different routing protocol with location

**[14:53]** information support while the sensor Network might be using a simple static router protocol so now we move on to the

**[15:02]** applications of ad hoc networks mobile ad hoc networks are best suitable for situations where an

**[15:09]** infrastructure is not available or to deploy one is not cost effective the following are some of the important

**[15:18]** applications military applications mobile ad hoc networks satisfies several military needs such as Battlefield

**[15:26]** survivability in such environment setting up of an infrastructure for communication between shoulders in

**[15:33]** Battlefield could be impossible the wireless devices carried by shoulders can form a mobile ad hoc network to

**[15:41]** support communication among them according to the figure shoulders tanks helicopter and other vehicles carry the

**[15:50]** mobile devices for message passing process home office and educational applications ad hoc networks also have

**[15:59]** applications in Home and Office environments the simplest and most direct application of ad hoc networks in

**[16:07]** both homes and offices is the networking of laptops pdas and other WLAN enabl

**[16:15]** devices in the absence of Wireless based station another home application that falls within the personal area network

**[16:23]** that is pan class as wire replacement through Wireless links and as in Bluetooth all periphery devices can

**[16:32]** connect to computer through wireless Bluetooth links eliminating the need for wide connections ad hoc networks can also

**[16:41]** enable streaming of video and audio among Wireless nodes even in the absence of any base station for example students

**[16:50]** in a classroom can use their laptops to obtain the latest class material from a professor's laptop as the class progresses

**[16:59]** universities and campus settings virtual classrooms ad hoc Communications during meetings or lectures are some of the

**[17:07]** educational applications of ad hoc networks a vehicular ad hoc network ret vehicular ad hoc networks are

**[17:16]** responsible for the communication between moving vehicles in a certain environment a vehicle can communicate

**[17:23]** with another vehicle directly which is called vehicle to vehicle that is v2v communic ation or a vehicle can

**[17:31]** communicate to an infrastructure such as roadside unit RSU known as vehicle to infrastructure

**[17:39]** v2i according to figure vanet scenario is creating VI v2v communication and v2i

**[17:46]** communication between the vehicles on the road wireless sensor networks wireless sensor networks can be considered as

**[17:55]** special case of mobile ad hoc networks Manet with reduced or no Mobility initially wsn was mainly

**[18:05]** motivated by military applications on the civilian application domain of wireless sensor networks such as

**[18:13]** environmental and spaces monitoring disaster management smart home production and Healthcare

**[18:21]** Etc these wsn May consist of heterogeneous and mobile sensor nodes the Network topology

**[18:29]** may be as simple as start topology the scale and density of a network varies depending on the

**[18:37]** application according to the figure application of wireless sensor networks include disaster management Network

**[18:45]** management home networks Healthcare informatics and Military applications sensor networks have

**[18:53]** emerged as a promising tool for monitoring the physical world utilizing self organization networks of battery

**[19:02]** powered Wireless sensors that can sense process and communicate a sensor network is a

**[19:09]** network of many tiny disposable lower part devices called nodes which are specially distributed in order to

**[19:17]** perform an application oriented Global task these nodes form a network by

**[19:25]** communicating with each other either directly or through other nodes one or more nodes among them will

**[19:33]** serve as sync that are capable of communicating with the user either directly or through the existing wild

**[19:41]** networks the primary component of the network is the sensor essential for monitoring real world physical

**[19:49]** conditions such as sound temperature humidity vibration pressure motion

**[19:55]** pollutant Etc at different locations wireless mesh networks wireless mesh

**[20:02]** networks can easily effectively and wirelessly connect entire cities using

**[20:09]** inexpensive existing technology traditional networks rely on a small number of wired access points or

**[20:16]** wireless hotspots to connect users in a wireless mesh Network the network connection is spread out among dozens or

**[20:25]** even hundreds of wireless mesh nodes that talk talk to each other to share the network connection across a large

**[20:33]** area mesh nodes are small radio transmitters that function in the same way as wireless router nodes use the

**[20:42]** common Wi-Fi standards known as 802.11 a B and G to communicate

**[20:50]** wirelessly with users and with each other it works on 2.4 GHz and 5 GHz

**[20:58]** frequency bands depending on the physical layer used for example if i e

**[21:05]** 802.11a is used the speed can be up to 54 MVPs nodes are programmed with

**[21:13]** software that tells them how to interact with a large Network information travels across the network from point A to point

**[21:21]** B by hoping wirelessly from one mesh node to the next the nodes automatically

**[21:28]** choose the quickest and safest path using a process known as Dynamic routing according to the figure there is

**[21:36]** an internet Cloud which is the backbone of mesh routers mesh routers are connected with

**[21:43]** access points base stations and other network devices all network devices provide the

**[21:50]** internet access functionality to all connected users in the network disaster relief operations

**[21:59]** every year natural disasters like earthquake flood destroy people's lives around the world as the importance of

**[22:08]** the internet grows the loss of network connectivity during such disasters will be more noticable effect of The

**[22:16]** Misfortune so it is important to find ways to enable the operations of networks even when infrastructure

**[22:24]** elements are disabled as a result of disasters personal area networks a personal area

**[22:32]** network that is pan is a computer network used for data transmission among devices such as computers telephones and

**[22:41]** personal digital assistants the idea of a personal area network is to create a network that

**[22:48]** consists of nodes which are associated with a single person these nodes may be placed in a

**[22:55]** person's clothes belt or carried in handle bags this type of network provides great flexibility for example

**[23:04]** it allows you to send a document to the printer in the office upstairs while you are sitting in the couch with your

**[23:11]** laptop using pan you can upload the photo from your cell phone to your desktop computer so friends this was all

**[23:21]** about Manet hope the concepts explained in this lecture were understandable and helpful in the next next lecture of

**[23:29]** Manet I will cover the routing protocols used in mobile ad hoc network hope to see you in the next

**[23:36]** lecture till then goodbye thank you

**[23:41]** [Music]
