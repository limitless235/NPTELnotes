# WiMAX Technology and its Security

**Module 35**  
Duration: 29:59  
Video: https://www.youtube.com/watch?v=K8I_4d-oGhA

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Prof Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering of Guru

**[0:08]** jambeshwar University of Science and Technology Hisar harana I welcome you all to the lecture series of cyber and

**[0:17]** information security in this lecture we will study about Bluetooth networks and security

**[0:25]** protocols which is basically used for data transmission on wireless personal

**[0:32]** area network first of all see the contents which I shall cover after covering brief introduction about

**[0:41]** Bluetooth technology I shall take up Bluetooth layered protocol architecture which will be followed by frame format

**[0:49]** of Bluetooth then I shall discuss versions of Bluetooth and i e standards

**[0:57]** for w pen technology in last I shall take up security architecture of Bluetooth technology so

**[1:07]** now let us start Bluetooth is a wireless technology standard for exchanging data over short

**[1:15]** distances using short wavelength UHF radio waves it operates in the ism band

**[1:23]** from 2.4 to 2.4856 and and mobile devices and

**[1:32]** building personal area networks in 1994 Ericson company became interested

**[1:39]** in connecting its mobile devices to other devices without cables together with four other

**[1:47]** companies IBM Intel Nokia and Toshiba it formed a special interest

**[1:56]** group they developed a wireless standard for interconnecting computing and communication devices and accessories

**[2:06]** using short range low power inexpensive Wireless radios this technology got named

**[2:15]** Bluetooth after the 10th Century King Herald Bluetooth who United disant

**[2:21]** Danish tribes into a single Kingdom the idea of this name was proposed in

**[2:28]** 1997 by by Jim card who developed a system that allowed mobile phones to

**[2:35]** communicate with computers Bluetooth special interest group SI defined standards for

**[2:44]** manufacturing Bluetooth devices in July 1999 the Bluetooth SI issued a 1,500

**[2:53]** page specification of version 1.0 shortly thereafter the i e standards

**[3:01]** 3 minutes, 1 second group for wireless personal area network 802.15 adopted the Bluetooth document as

**[3:10]** a basis and started working on it Bluetooth specification SI is for a

**[3:18]** complete system that is from the physical layer to the application layer but i e

**[3:27]** 802.15 defines only only the physical and data link layers the basic unit of a Bluetooth

**[3:36]** system is a ponet as shown in figure which consist of a master node and up to

**[3:44]** seven active slave nodes within a distance of 10 m multiple piconets can exist in the

**[3:54]** same large room and can even be connected via a bridge node as shown in

**[4:02]** figure an interconnected collection of piconets is called a scatternet all communication is between

**[4:11]** the master and the slave direct slave to slave communication is not

**[4:20]** possible after brief background let us see layered protocol architecture of Bluetooth the Bluetooth standard has

**[4:29]** many many protocols grouped Loosely into layers the basic Bluetooth protocol

**[4:36]** architecture is shown in figure the bottom layer is the physical radio layer which corresponds fairly

**[4:45]** well to the physical layer in the OSI and 802 models it deals with radio

**[4:53]** transmission and modulation using ISM band from 2.4 4 to

**[5:01]** 5 minutes, 1 second 2485 GHz frequency the baseband layer is somewhat

**[5:08]** analogous to the max subl layer but also includes elements of the physical layer

**[5:15]** it deals with how the master controls time slots and how these slots are grouped into

**[5:24]** frames the radio layer moves the bits from Master to slave or vice

**[5:30]** versa this layer turns the raw bit stream into frames and defines some key

**[5:38]** formats in the simplest form the master in each ponet defines a series of 6 25

**[5:46]** microc time slots with the Master's transmission starting in the even slot and the slave transmission starting in

**[5:55]** the odd slots this is traditional time division multiplexing with a master getting half

**[6:03]** the slots and slaves sharing the other half each frame is transmitted over a

**[6:12]** logical Channel called a link between the master and the slave two kind of

**[6:19]** Link exist the first is the ACL that is asynchronous connectionless link which

**[6:26]** is used for packet switch data available at irregular intervals the other is the SEO that is

**[6:35]** synchronous connection oriented link for realtime data such as Telephone

**[6:42]** Connections this type of channel is allocated a fixed slot in each Direction due to the time critical

**[6:51]** nature of SEO links frames sent over them are never retransmitted instead forward error diretion can be

**[7:00]** used to provide High reliability next layer link manager handles the establishment of logical

**[7:09]** channels between devices including power management authentication and quality of

**[7:19]** service The Logical link control adaptation protocol often called l2cap Shields the upper layers from the

**[7:28]** details of of transmission the l2cap layer has three major functions first it accepts packets

**[7:38]** of up to 64 KB from the upper layers and breaks them into frames for

**[7:45]** transmission at the far end the frames are reassembled into packets

**[7:52]** again second it handles the multiplexing and demultiplexing of multiple pack

**[8:00]** sources third l2cap handles the quality of service requirements as the name suggest the

**[8:09]** audio and control protocols deal with the audio and control respectively the applications can get at

**[8:19]** them directly without having to go through the l2cap protocol the next layer contains a

**[8:28]** mix of different protocols the RFC radio frequency communication is the protocol

**[8:35]** that emulates the standard serial Port found on PCs for connecting the keyboard

**[8:43]** mouse and modem among other devices the telepon protocol is a realtime protocol

**[8:51]** used for the three speech oriented protocols it also manages call setup and

**[9:00]** termination finally the service Discovery protocol is used to locate services within the

**[9:08]** network the top layer is where the applications and profiles are located

**[9:16]** they make use of the protocols in lower layers to get their work done so this was layered protocol architecture of

**[9:25]** Bluetooth now let us see frame format of Bluetooth the frame format of Bluetooth

**[9:32]** is shown in figure it begins with an SS code that usually identifies the master

**[9:41]** so that slaves within radio range of two masters can tell which traffic is for

**[9:48]** them next comes a 54 bit header containing typical Max sublayer

**[9:56]** Fields then comes the data field of up to 2744 bits for a five slot

**[10:04]** transmission for a single time slot the format is same except that the data field is 240

**[10:14]** bits let us take a quick look at details of the header the address field

**[10:21]** identifies which of the eight active devices the frame is intended for the

**[10:28]** type field identifies the frame type whether it is ACL SE Pole or null type

**[10:39]** it also tells the type of error correction used in the data field and

**[10:46]** how many slots long the frame is the flow bit is for flow control

**[10:53]** which is asserted by a slave when its buffer is full and cannot re receive any more

**[11:01]** 11 minutes, 1 second data the acknowledgement bit is used to piggy back an AK onto a

**[11:09]** frame the sequence bit is used to number the frames to detect retransmissions the protocol is stop and

**[11:18]** wait so one bit is enough then comes the 8bit header checkm

**[11:25]** the entire 8bit header is repeated three times to form the 54 bit header shown in

**[11:35]** figure on the receiving side a simple circuit examines all three copies of

**[11:42]** each bit if all three are same the bit is accepted if not the majority opinion

**[11:50]** wins Bluetooth SI has defined versions for Bluetooth and i e has defined stand

**[11:59]** standards for wireless pan let us first see versions defined by Si the versions

**[12:07]** were formalized by the Bluetooth special interest group SI the SI was formally announced on 20th

**[12:16]** May 1998 today it has a membership of over 20,000 companies

**[12:24]** worldwide it was initially established by Ericson IBM Intel Toshiba and Nokia

**[12:33]** and later it was joined by many other companies all versions of the Bluetooth

**[12:41]** standard support downward compatibility let us see each version one by

**[12:48]** one Bluetooth v1.0 and v1.0b these are basic most Bluetooth

**[12:57]** which had many problems at manufacturers had difficulty making their products

**[13:05]** interoperable Bluetooth v1.1 it was ratified as I E standard

**[13:13]** 802.15 one22 many errors found in the version 1.0b

**[13:21]** specifications were fixed in this version it added possibility of known encrypted channels at along with

**[13:30]** received signal strength indicator Bluetooth v1.2 this version supports faster

**[13:39]** connection and Discovery protocols it supports adaptive frequency hoping

**[13:45]** spread Spectrum which improves resistance to radio frequency interference by avoiding the use of

**[13:53]** crowded frequencies in the hoping sequence it supports higher transmission

**[14:00]** speeds in practice up to 721 kilobits per second than in

**[14:09]** v1.1 it was ratified as I E standard 802.1

**[14:16]** 15.1 2005 Bluetooth v2.0 plus

**[14:24]** EDR this version of the Bluetooth core specification was released in

**[14:30]** 2004 the main difference is the introduction of an enhanced data rate

**[14:36]** EDR for faster data transfer the nominal rate of EDR is about 3 megabits per

**[14:45]** second although the Practical data transfer rate is 2.1 megabits per second

**[14:52]** EDR uses a combination of gfsk and phase shift King

**[15:00]** modulation Bluetooth 2.1 plus EDR Bluetooth core specification version 2.1

**[15:08]** plus EDR was adopted by the Bluetooth SI on 26th July

**[15:15]** 2017 the headline feature of v2.1 is secure simple pairing

**[15:23]** SSP this improves the pairing experience for Bluetooth devices while increasing

**[15:30]** the use and strength of security Bluetooth v3.0 plus

**[15:39]** HS this version was adopted by the Bluetooth SI on 21st April

**[15:47]** 2009 Bluetooth v3.0 plus HS that is highspeed provides theoretical data

**[15:55]** transfer speed of up to 24 megab bits per second though not over the Bluetooth

**[16:03]** Link itself instead the Bluetooth Link is used for negotiation and

**[16:10]** establishment and the high data rate Traffic is carried over a 802.11

**[16:18]** link Bluetooth v4.0 the Bluetooth SI completed the

**[16:25]** Bluetooth core specification version 4.0 called bluetooth smart and has been

**[16:32]** adopted on 30th June 2010 it includes classic Bluetooth

**[16:39]** Bluetooth highspeed and Bluetooth low energy Le protocols Bluetooth LE previously known

**[16:47]** as vibri is a subset of Bluetooth v4.0 with an entirely new protocol stack

**[16:56]** for Rapid buildup of simple links Bluetooth

**[17:02]** v4.1 the Bluetooth SI announced formal adoption of the Bluetooth v4.1

**[17:09]** specification on 4th December 2013 this specification is an

**[17:16]** incremental software update to Bluetooth specification v4.0 and not a hardware

**[17:25]** update features include increased coex resistance support for LTE bulk data

**[17:32]** transfer exchange rates and Aid developer Innovation by allowing devices

**[17:38]** to support multiple roles simultaneously Bluetooth

**[17:46]** v4.2 Bluetooth v4.2 was released on December 2

**[17:52]** 2014 it introduces some key features such as data length extension that

**[17:59]** require a hardware update but some older Bluetooth Hardware may receive some

**[18:06]** Bluetooth v4.2 features such as privacy updates via firmware update

**[18:13]** also now after Bluetooth version let us see i e standards for wireless personal

**[18:21]** area network i e 802.15 is a working group of The

**[18:28]** Institute of electrical and electronic Engineers i e which specifies Wireless

**[18:35]** personal area network standards now we will take up each standard one by one as shown in

**[18:44]** figure i e 802.1 15.1 W pan

**[18:51]** Bluetooth this standard is based on Bluetooth technology it defines physical

**[18:58]** layer phy and media access control Mac specification for wireless connectivity

**[19:06]** with fixed portable and moving devices within or entering personal operating

**[19:15]** space standards were issued in 2002 and

**[19:21]** 2005 I 82.1 15.2 coexistence

**[19:28]** this standard addresses the coexistence of Wireless personal area networks wpen

**[19:36]** with other wireless devices operating in unlicensed frequency bands such as

**[19:43]** Wireless local area networks W Lan the i e

**[19:50]** 802.15 point2 203 standard was published

**[19:55]** in 2003 and task group 2 went into

**[20:01]** 20 minutes, 1 second hibernation i e 802.1 15.3 High rate W

**[20:08]** pen i e 802.15 3 2003 is a Mac and phy standard

**[20:17]** for high rate of 11 to 55 Mbps in Wireless personal area

**[20:25]** networks this standard has three standards i e p 802.1 15.3 a 802.1

**[20:36]** 15.3 B 2006 and 802.1 15.3 C

**[20:45]** 2009 next is i e

**[20:49]** 802.15.4 low rate W pen i e 802.15.4

**[20:59]** 2003 low rate W pen deals with a low data rate but very long battery life and

**[21:06]** very low complexity the standard defines both the physical and data link layers of the OSI

**[21:16]** model this standard has two versions first is wpan low rate alternative phy 4

**[21:23]** a formally called i e 82.5 15.4 a

**[21:32]** 2007 second is revision and enhancement 4B formally called as i e

**[21:42]** 802.15.4 20006 i e 802.1 15.5 Mesh

**[21:51]** networking it provides the architectural framework enabling Wan devices to promote

**[21:59]** interoperable stable and scalable Wireless Mesh networking this standard is composed of

**[22:08]** two parts low rate W pan meshless and high rate Wan mesh

**[22:17]** networks the low rate mesh is built on i e 802.15.4

**[22:25]** 2006 Mac while the high rate mesh utilizes i e 802.1

**[22:33]** 15.3 3B ma next is I 802.1

**[22:40]** 15.6 body area networks in December 2011 the i e

**[22:49]** 802.15.4 task group approved a draft of a standard for body area network ban

**[22:59]** Technologies focus is on devices in or around the human body to serve a variety

**[23:06]** of applications including medical consumer electronics and personal

**[23:14]** entertainment other standards are i e 82.1 15.7 that is visible light

**[23:23]** communication i e p 802.15 8 that is peer aware

**[23:32]** Communications I P 82.1 15.9 that is Key Management protocol and

**[23:40]** last is i e p802 15.10 that is layer 2 routing after

**[23:50]** versions and standards we now move on to security architecture of Bluetooth

**[23:59]** three basic security services are specified in the Bluetooth standard

**[24:06]** authentication it is for verifying the identity of communicating devices based on their Bluetooth device

**[24:14]** address Bluetooth does not provide native user authentication second is

**[24:22]** confidentiality it is for preventing information compromise caused by e dropping by ensuring that only

**[24:31]** authorized devices can access and view transmitting data third is

**[24:38]** authorization it is for allowing the control of resources by ensuring that a device is authorized to use a service

**[24:48]** before permitting it to do so Bluetooth does not address other

**[24:54]** security services such as audit integrity and non repudiation if such services are needed

**[25:03]** they should be provided through additional means the family of Bluetooth BR that is

**[25:11]** basic rate EDR that is enhanced data rate HS that is highspeed

**[25:18]** specifications defines four security modes each Bluetooth device must operate

**[25:26]** in one of these modes modes let us see these modes one by one security mode one

**[25:35]** in this mode devices are considered non-secure security functionality like

**[25:42]** authentication and encryption is never initiated leaving the device and

**[25:49]** connections susceptible to attackers in effect Bluetooth devices in this mode

**[25:56]** are indiscriminate and do not employ any mechanisms to prevent other bluetooth enabled devices

**[26:05]** from establishing connections however if a Remote device initiates security such as a pairing

**[26:14]** authentication or encryption request a security mode one device will

**[26:22]** participate all v2.0 and earlier devices can support

**[26:28]** security mode 1 and v2.1 and later devices can use security mode one for

**[26:37]** backward compatibility with other devices but n recommends never use

**[26:46]** security mode one for Bluetooth devices second is security mode

**[26:54]** two in this mode security procedures May be initiated after link establishment

**[27:01]** 27 minutes, 1 second but before logical Channel establishment for this security mode a local security

**[27:09]** manager as specified in the Bluetooth architecture controls access to specific

**[27:16]** de Services the centralized security manager maintains policies for Access

**[27:23]** Control and interfaces with other protocols and device

**[27:30]** users security mode three this mode is the link level enforced security mode in which a

**[27:39]** Bluetooth device initiates security procedures before the physical link is fully

**[27:46]** established Bluetooth devices operating in security mode 3 mandate authentication and encryption for all

**[27:55]** connections to and from the device all v2.0 and earlier devices can support

**[28:04]** security mode 3 but v2.1 and later devices can only support it for backward

**[28:12]** compatibility purposes last is security mode 4 similar to security mode 2 security

**[28:22]** mode 4 introduced in Bluetooth v2.1 plus EDR is a service level and fr

**[28:30]** security mode in which security procedures are initiated after physical

**[28:37]** and logical link setup security mode 4 uses secure simple pairing SSP in which

**[28:48]** elliptic curve Dey Helman key agreement replaces Legacy key agreement for link

**[28:56]** key generation however the device authentication and encryption algorithm are identical to

**[29:05]** the algorithm in Bluetooth v2.0 plus EDR and earlier

**[29:12]** versions so friends this was Bluetooth networks and security protocols finally

**[29:21]** summarizing we learned about Bluetooth lead protocol architecture which was followed by frame format of Bluetooth

**[29:30]** then we discussed versions and i e standards for Bluetooth technology in

**[29:38]** last we covered security architecture of Bluetooth technology hope the concepts explained

**[29:47]** in this lecture were understandable and helpful hope to see you in next lecture

**[29:54]** till then goodbye enjoy the day thank you thank you
