# ATM Network Security Protocol

**Module 29**  
Duration: 25:45  
Video: https://www.youtube.com/watch?v=JdRurgWuHvQ

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Lal Chand, Department of Computer Engineering, Punjabi University, Patiala

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:01]** 1 second [Music]

**[0:17]** Hello friends I welcome you all to the video lecture series of cyber security and information security in this lecture

**[0:25]** we will study about ATM network security protocol so what is an ATM asynchronous transfer

**[0:34]** mode ATM is a switching technique used by telecommunication networks that uses asynchronous time division multiplexing

**[0:42]** to encode data into small fixed sized cells this is different from Ethernet or Internet which use variable packet sizes

**[0:51]** for data or frames ATM is the core protocol used over the synchronous Optical Network Sonet backbone of the

**[1:00]** ISDN asynchronous transfer mode was designed with sales in mind this is because voice data is converted to

**[1:07]** packets and is forced to share a network with burst data passing through the same medium so no matter how small the voice

**[1:15]** packets are they always encounter full size data packets and could experience maximum queing

**[1:23]** delays this is why all data packets should be of the same size the fixed Sal structure of of ATM means it can be

**[1:31]** easily switched by Hardware without the delays introduced by rooted frames and software switching this is why some

**[1:38]** people believe that ATM is the key to the internet bandwidth problem ATM creates fixed Roots between two points

**[1:47]** before data transfer begins which differs from tcpip where data is divided into packets Each of which takes a

**[1:54]** different route to get to its destination this makes it easier to build data usage however an ATM network

**[2:03]** is less adaptable to a sudden Network traffic search the ATM provides data link layer services that run on the OSI

**[2:11]** layer one physical links it functions much like small packet switched and circuit switch networks which makes it

**[2:19]** idal for real time low latency data such as viip and video as well as for high

**[2:26]** throughput data traffic like file transfers a virtual circuit or connection must be established before

**[2:33]** the two end points can actually exchange data ATM Services generally have four different bit rate choices available bit

**[2:42]** rate provides a guaranteed minimum capacity but data can be bursted to higher capacities when Network traffic

**[2:49]** is minimal constant bit rate specifies a fixed bit rate so that data is sent in a

**[2:56]** steady stream this is analogous to a leased line unspecified bit rate doesn't guarantee

**[3:03]** any throughput level and is used for applications such as file transfers that can tolerate delays variable bit rate

**[3:12]** vbr provides a specified throughput but data is not sent evenly this makes it a even popular choice for voice and video

**[3:21]** conferencing the structure of an ATM cell an ATM cell consists of a 5 byte

**[3:27]** header and a 48 by payload ATM defines two different cell formats as shown in

**[3:34]** the figure uni user network interface and nni that is network network

**[3:41]** interface most ATM links use uni cell format GFC that is generic flow control

**[3:50]** four bits and default is 40 bits VPI that is virtual path identifier

**[3:58]** 8 Bits uni or 12 Bits n ni I VCI virtual

**[4:03]** Channel identifier 16 bits PT P type that is three bits PT bit three Network

**[4:13]** management cell if zero user data cell and the following apply PT bit 2

**[4:21]** explicit forward conen indication efci 1 is equal to network congestion

**[4:28]** experienced PT bit 1 On's bit ATM user to user AA bit used by aal5 to indicate

**[4:38]** packet boundaries CLP that is cell loss priority 1

**[4:46]** bit HC that is header error control which is

**[4:51]** 8bit CRC polinomial is equal to x ^ 8 + x ^ 2 + 1

**[5:00]** ATM uses the PT field to designate various special kinds of sales for operations Administration and management

**[5:08]** that is om purposes and to delineate packet boundaries in some ATM adaptation layers A

**[5:16]** A if the most significant bit of the PT field is zero this is a user data cell and the other two bits are used to

**[5:25]** indicate Network congestion and as a general purpose header bit available for ATM adaptation

**[5:31]** layers if the MSB bit of the PT bit is one this is a management cell and the other two bits indicate the type that is

**[5:40]** Network management segment Network management end to end resource management and reserved for future

**[5:48]** use several ATM link protocols use the HC field to drive a CRC based framing

**[5:55]** algorithm which allows locating the ATM cells with no overhead beyond what is otherwise needed for header protection

**[6:04]** the 8bit CRC is used to correct single bit header errors and detect multi-bit header errors when multi-bit header

**[6:12]** errors are detected the current and subsequent sales are dropped until a cell with no header errors is

**[6:19]** found a un cell reserves the GFC field for a local flow controls sub

**[6:26]** multiplexing system between users this was intended to allow several terminals to share a single network connection in

**[6:34]** the same way that two integrated Services digital Network ISDN phones can share a single basic rate ISDN

**[6:42]** connection all four GFC bits must be Zero by default the nni cell format replicates

**[6:51]** the uni format almost exactly except that the 4bit GFC field is

**[6:57]** reallocated to the V field extending the VPI to 12 bits thus the single nni ATM

**[7:06]** interconnection is capable of addressing almost 2 to the power 16 VPS of up to almost 2 to the power 16 VCS each in

**[7:16]** practice some of the VP and VC numbers are reserved ATM network interfaces following are the ATM network interfaces

**[7:25]** and are shown in the figure user to network interface public network interface private network

**[7:33]** interface second Network to node interface which includes private nni public

**[7:40]** nni data exchange interface dxi between packet routers and ATM digital service

**[7:48]** units DSU the ATM adaption layer how to break

**[7:54]** application messages to sales the ATM layer transmission switching

**[8:01]** 8 minutes, 1 second reception congestion control buffer management cell header generation removal at source or

**[8:09]** destination reset connection identifiers for the next hope at switch sell address translation

**[8:17]** sequential delivery the ATM Forum specifications data confidentiality the

**[8:24]** function of confidentiality is to protect precious business data from unauthorized persons confidentiality

**[8:32]** part of network security makes sure that the data is available only to the intendent and authorized

**[8:39]** persons data integrity and authentication this goal means maintaining and assuring the accuracy

**[8:47]** and consistency of data the function of Integrity is to make sure that the data is reliable and is not changed by

**[8:55]** unauthorized persons AAL frames are protected Ed by appending a cryptographic check sum to a

**[9:03]** frames possibility is given to provide reordering protection by introducing a sequence number into AAL frames before

**[9:12]** calculating the cryptographic check sum signaling protection any signaling messages may be authenticated and

**[9:20]** integrity protected by introducing a digital signature into an siie especially if anme protocol is

**[9:28]** employed protection is offered for setup and connects messages by calculating the signature over the siie fields specified

**[9:37]** by the smme protocol it is still offered for any other signaling messages release

**[9:44]** status restart and for setup and connect messages if the smme protocol is not used by introducing a signature

**[9:53]** calculated over part of the siie availability this goal means maintaining and assuring

**[10:02]** the accuracy and consistency of data the function of Integrity is to make sure that the data is reliable and is not

**[10:09]** changed by unauthorized persons so ATM security system should provide the following functions verification of

**[10:18]** identities security system should be able to establish and verify the claimed identity of any actor in an ATM

**[10:25]** network controlled access and authorization the actors should not be able to gain access to information or resources if

**[10:34]** they are not authorized to protection of confidentiality stored and communicated

**[10:41]** data should be confidential protection of data Integrity the security system should guarantee the Integrity of the

**[10:49]** stored and communicated data strong accountability an entity cannot deny the responsibility of its performed actions

**[10:57]** as well as their effects activities logging the security system should support the capability to

**[11:05]** retrieve information about security activities in the network elements with the possibility of tracing this

**[11:11]** information to individuals or entities alarm reporting the security system should be able to generate alarm

**[11:20]** notification about certain adjustable and selective security related events audit when violations of security happen

**[11:29]** the system should be able to analyze the logged data relevant to security security recovery the security system

**[11:36]** should be able to recover from successful or attempted breaches of security Security

**[11:43]** Management the security system should be able to manage the security services derived from the above requirements they

**[11:51]** are necessary to support the maintenance of Security Services if the security system cannot be recovered from attacks

**[11:58]** and not providing Security Services anymore then the system won't be secure after these attacks on the other hand

**[12:05]** Security Services and information about security have to be managed securely they are foundations of the security

**[12:13]** system threads to ATM as other networks ATM networks will suffer a lot of threats typical ones are

**[12:23]** eavesdropping spoofing service denial VC stealing and traffic analysis

**[12:30]** Etc notice that VC stealing and traffic analysis happen only in ATM networks

**[12:38]** eavesdropping eavesdropping refers to the threat that the attacker connects or taps into the transmission media and

**[12:45]** gain unauthorized access to data it is one of the most common attacks to the network since most ATM networks are

**[12:52]** connected with fiber optic cables some people might get the wrong impression that it is not so easy to tap a ATM

**[13:00]** network spoofing spoofing attack means that an attacker tries to impersonate another

**[13:08]** user to the third part therefore can get access to resources belonging to the victim to take advantage or just destroy

**[13:16]** them poofing might need special tools to manipulate the protocol data unit sometimes it might require the attacker

**[13:23]** has special access permission C must be super user in Unix environment however since a network will be

**[13:30]** connected to many interested networks via the Internet it's impossible to prevent a hacker from getting this exess

**[13:38]** permission or even trace the people with this particular exess permission ATM is being implemented in public domain

**[13:45]** therefore it is subjected to this kind of attack also service denial ATM is a

**[13:52]** connection oriented technique a connection which is called virtual circuit VC in ATM is managed by a set of

**[14:01]** 14 minutes, 1 second signals VC is established by setup signals and can be disconnected by release or drop party signals if an

**[14:11]** attacker sends release or drw party signal to any intermediate switch on the way of a VC then the VC will be

**[14:19]** disconnected by sending these signals frequently the attacker can greatly disturb the communication between one

**[14:26]** user to another therefore will disable the quality of service in ATM combining this technique with other tricks like

**[14:34]** eavesdropping the attacker can even completely block one user from another stealing of VCS if two switches

**[14:44]** in an ATM network compromise the attacker can even steal a VC from another user say vc1 and vc2 are two

**[14:53]** virtual channels which will go through switch a and switch B wec one is owned

**[14:59]** by user U1 and vc2 is owned by user U2 if a and b have compromised then a can

**[15:06]** switch VC one's cell going from A to B through vc2 and B will switch back those

**[15:13]** cells to vc1 since switches will forward cells based on the VCI that is virtual Channel identifier or VPI that is

**[15:22]** virtual path identifier in the cell header A and B can just alter these fields back and fourth switches between

**[15:31]** A and B won't notice these changes and will switch the assumed vc2s sale just

**[15:37]** like the authentic vc2s sales in public packet switching Network U1 won't gain

**[15:44]** too much by District however in an ATM network if quality of service is guaranteed then user one can gain a lot

**[15:53]** of stealing a higher quality Channel which user one is not entitled to use ACC to the exess control policy user one

**[16:03]** can gain even more if every user has to pay for the communication in both cases user two will be hurt someone may argue

**[16:12]** that the possibility that the switches will compromises pretty low that will true if the ATM network is owned by one

**[16:20]** organization when we consider ATM inter networking in which Kells will travel through different ATM networks it will

**[16:28]** will be very easy for two switches to compromise traffic analysis traffic analysis refers to a threat that the

**[16:36]** hacker can get information by collecting and analyzing the information like the volume timing and communication parties

**[16:44]** of a VC volume and timing can reveal a lot of information to the hacker even though the data is encrypted because

**[16:52]** encryption won't affect the volume and timing of information and also the source and this destination parties can be obtained from

**[17:00]** the cell header normally is in clear text and some knowledge about the routing table another related thre is called

**[17:10]** convert channels in this technique the attacker can encode the information in the timing and volume of data VCI or

**[17:19]** even session key to release information to another people without being monitored normally these two attack

**[17:27]** won't happen however when ATM is used in an environment requiring stringent security it might

**[17:35]** happen traffic Management in order for ATM networks to deliver guaranteed quality of service on demand while

**[17:43]** maximizing the utilization of available network resources effective traffic management mechanisms are needed almost

**[17:51]** every aspect of ATM network operation from signaling requests and routing to network resource allocation and policing

**[17:59]** contains some traffic management mechanisms some of parameters are as follows quality of service attributes

**[18:09]** while setting up a connection on ATM networks users can specify the following parameters related to the desired

**[18:15]** quality of service Peak cell rate PCR the maximum instantaneous rate at which

**[18:23]** the user will transmit for bursty traffic the inter cell interval and the cell rate varies considerably the PCR is

**[18:32]** the inverse of the minimum inter cell interval sustained cell rate

**[18:39]** ISC this is the average rate as measured along a long time interval cell loss ratio CLR the

**[18:48]** percentage of cells that are lost in the network because of error or congestion and are not delivered to the destination

**[18:55]** recall that each ATM cell has a cell loss priority the CLP bit in the header

**[19:02]** during periods of congestion the network will first discard cells with CLP is equal to 1 since the loss of cells with

**[19:11]** CLP is equal to zero is more harmful to the operation of the application CLR can be specified separately for cells with

**[19:20]** CLP is equal to 1 and for those with CLP is equal to zero cell transfer delay ctd

**[19:29]** the delay experienced by a Cale between Network entry and exit points is called the sale transfer delay it includes

**[19:38]** propagation delays queing delays at various intermediate switches and service times at queing

**[19:45]** Point cell delay variation CDV this is mayor of variance of

**[19:52]** ctd high variation implies larger buffering for delay sensitive traffic such as Vo and video burst tolerance

**[20:02]** BT this determines the maximum burst size that can be sent at the peak rate this is the bucket size parameter for

**[20:10]** leaky bucket algorithm that is used to control the traffic entering the network the algorithm consist of putting all

**[20:18]** arriving cells in a buffer bucket which is drained at the sustained cell rate is

**[20:25]** CR the maximum number of backto back cells that can be sent at the peak sell rate is called maximum burst size

**[20:34]** MBS minimum sell rate MCR this is the minimum rate desired by a user the first six of the above

**[20:43]** traffic parameters were originally specified in un version 3 traffic contract to provide a

**[20:52]** guaranteed qos a traffic contract is established during connection setup which contains a connection traffic

**[21:00]** descriptor and a confirmance definition however it is not necessary for every ATM virtual connection to have

**[21:08]** a specified qos the reason for this is that if only specified qos connections are supported

**[21:16]** by ATM then a large percentage of the network resources will be wasted this can happen when one or more connections

**[21:24]** are not utilizing the full capacity of their qos cont contracts unspecified qos contracts can

**[21:32]** be supported by an ATM network on a best effort basis such best effort services are sufficient for supporting most of

**[21:41]** the existing data applications congestion control techniques congestion control lies at

**[21:49]** the heart of the general problem of traffic management for ATM networks in general congestion arises when the

**[21:56]** incoming traffic to a specified link is more than the outgoing link capacity the primary function of congestion control

**[22:04]** is to ensure good throughput and delay performance while maintaining a fair allocation of network resources to the

**[22:11]** user one method to avoid Network congestion is to accept a new ATM connection during connection setup phase

**[22:20]** only when sufficient network resources are available to provide the acceptable qos this is called connection and

**[22:28]** Mission Control CAC which is needed for connections where the qos must be

**[22:35]** guaranteed disadvantages ATM has not been widely accepted although some phone companies

**[22:43]** still use it in their backboard networks the expense complexity and lack of interoperability with other technologies

**[22:52]** have prevented ATM from becoming more prevalent expense ATM technology provides a comprehensive list of

**[23:00]** services even a moderate ATM switch costs much more than inexpensive land Hardware in addition the network

**[23:08]** interface card needed to connect a computer to an ATM network is significantly more expensive than a

**[23:15]** corresponding ethernet Nic connection setup latency ATM's connection oriented

**[23:23]** Paradigm introduces significant delay for distant communication the time required to set up and tear down the ATM

**[23:30]** VC for distant communication is significantly larger than the time required to use it sell tax ATM sell

**[23:39]** headers impose a 10% tax on all data transfer in case of ethernet sell taxes 1% lack of efficient

**[23:48]** broadcast connection oriented networks like ATM are sometimes called non-broadcast multiple

**[23:56]** exess NB M networks because the hardware does not support broadcast or multicast

**[24:05]** on an ATM network broadcast to a set of computers is simulated by arranging for an application program to pass a copy of

**[24:14]** data to each computer in the set as a result broadcast is inefficient complexity of

**[24:23]** qos the complexity of this specification makes implementation cumbers some and difficult many implementations do not

**[24:32]** support the full standard Assumption of homogenity ATM is designed to be a

**[24:38]** single Universal networking system there is minimal provision for interoperating

**[24:45]** with other Technologies so friends this was all about ATM network security protocols hope the concepts explained in

**[24:53]** this lecture were understandable and helpful hope to see you in the next lecture till then goodbye thank you

**[25:01]** 25 minutes, 1 second [Music]
