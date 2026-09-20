# Ethernet and Fast Ethernet

**Module 23**  
Duration: 29:01  
Video: https://www.youtube.com/watch?v=AN-s1J2GrPk

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Prof Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:03]** [Music]

**[0:10]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:18]** University of Science and Technology Hisar harana I welcome you all to the

**[0:25]** video lecture series of cyber security and information secur in this lecture we will study about

**[0:33]** ethernet and fast ethernet which is basically used for data transmission on

**[0:40]** wired Lan at a speed of 10 and 100 Mbps respectively first of all please see the

**[0:49]** contents which I shall cover after covering brief introduction about ethernet I shall take up protocol

**[0:58]** architecture and frame format of ethernet which will be followed by Mac operations in the

**[1:07]** ethernet then I shall take up fast ethernet and protocol architecture of fast

**[1:14]** ethernet so now let us start ethernet is a family of computer networking

**[1:21]** Technologies for local area network and metropolitan area network it was

**[1:28]** developed as an experimental coxl cable network in 1970s by jerox

**[1:37]** Corporation initially it operated with a data rate of just 3 Mbps using a carrier

**[1:44]** sense multiple assess with Collision detection protocol for Lan it was

**[1:51]** commercially introduced in 1980 and standardized in 1983 as i e 8

**[2:01]** 2 minutes, 1 second 2.3 it has since been refined to support higher bit rates and longer link

**[2:09]** distances over time ethernet has largely replaced competing wired land

**[2:16]** Technologies such as token ring token bus fddi and

**[2:23]** arknet ethernet land topology is currently the most common Network architecture

**[2:30]** ethernet topologies are generally bus or bus star topologies the I 802.3 standard

**[2:40]** defines ethernet protocols for OSI media access control sublayer and physical

**[2:48]** layer Network characteristics the name ethernet refers to the cable ether four types of

**[2:57]** cablingserver ethernet as shown in table and figure

**[3:04]** table shows four types of cable standards however figure part A shows 10

**[3:12]** base five connections Part B shows 10 base 2 connections and part C shows 10

**[3:20]** base T connections historically 10 base 5 cabling popularly called thick ethernet

**[3:29]** came first connections to it are generally made using vampire tabs as shown in part

**[3:37]** A of figure in which a pin is very carefully forced halfway into the coxial

**[3:45]** caes core in Ethernet standard the first number is the speed in

**[3:53]** Mbps then comes the word base to indicate base band transmission

**[4:01]** 4 minutes, 1 second accordingly the notation 10 base 5 means that it operates at 10 Mbps using

**[4:10]** baseband signals and can support segments of up to 500

**[4:17]** M the second cable type 10 base 2 was made up of thin coxal cable using BNC

**[4:26]** connectors to form P Junctions rather than using vampire tabs as shown

**[4:34]** in Part B of figure thin ethernet is much cheaper and

**[4:41]** easier to install but it can run for only 185 m per segment Each of which can

**[4:50]** handle only 30 machines problem with 10 base 5 and 10

**[4:57]** Bas 2 is that whole network runs on single Cable in case cable gets fault at

**[5:06]** some place whole network goes down the problems associated with

**[5:14]** finding cable brakes drove systems toward a different kind of wiring

**[5:20]** pattern in which all stations have a cable running to a central Hub this

**[5:28]** scheme is called 10 Bas T in this scheme each computer is connected to HUB

**[5:36]** through separate twisted pair cable as shown in part C of figure it supports

**[5:44]** 100 m distance with 1024 nodes and is cheapest system a

**[5:52]** fourth cabling option for ethernet is 10 Bas F which uses fiber Optics this

**[6:01]** 6 minutes, 1 second alternative is expensive due to the cost of the connectors and Terminators but it has excellent noise

**[6:11]** immunity and is the method of choice when running between buildings or widely

**[6:18]** separated hubs runs of up to 2,000 M are allowed

**[6:25]** it also offers good security since wire tapping a fiber is much more difficult

**[6:33]** than wire tapping a copper wire it supports 1024 nodes and is best

**[6:41]** suitable for connecting two buildings now let us see ethernet

**[6:49]** layered protocol architecture in Ethernet both the data link and the

**[6:55]** physical layers are involved in the creation and transmission of frames the

**[7:03]** physical layer is related to the type of Lan cabling and how the bits are

**[7:09]** transmitted and received on the cable the data link layer is divided into Su

**[7:16]** layers which are logical link control LLC and media access control Mac the LLC

**[7:26]** sublayer is responsible for identifying and passing data to the network layer

**[7:33]** protocol and Max sub layer is responsible for medium access control

**[7:39]** for shared data the MAC sublayer address is the physical Hardware address of the

**[7:46]** source and destination computer this sublayer controls which

**[7:53]** computer devices send and receive the data and allows ni is to communicate

**[8:00]** with the physical layer the frame format of i e

**[8:08]** 802.3 is as shown in figure the Preamble of the frame which is of 7 bytes

**[8:16]** indicates the start of a new frame and establishes synchronization conditions between

**[8:25]** devices the last bite of Preamble known as start of frame delimiter soff always has

**[8:33]** a 10101010 bit pattern this bite indicates

**[8:42]** the start of a frame the destination address of 6 bytes is the hardware Mac

**[8:49]** address of the receiving device and the source address of 6 bytes specifies the

**[8:57]** hardware Mac address of of the sending device the length field of 2 bytes

**[9:05]** indicates the length of frame the data field is for the actual data being

**[9:12]** transmitted from device to device and length of data field is 46 to 1500

**[9:21]** bytes in case length of data is less than 46 bytes padding is done to make it

**[9:28]** 46 byte the cyclic redundancy check CRC of four bytes checks that the frame is

**[9:38]** received free from error after frame format let us see how

**[9:45]** medium access control works in Ethernet protocols in which stations

**[9:53]** listen for a carrier and act accordingly are called carrier sense protocol s

**[10:00]** ethernet uses CSM by CD as medium assess control protocol for channel

**[10:08]** sensing when a station has data to send it first listens to the channel to see

**[10:15]** if anyone else is transmitting at that moment if the channel is busy the

**[10:23]** station Waits until it becomes idle when the station detects an idle Channel it

**[10:31]** transmits a frame if a collision occurs the station Waits a random amount of

**[10:37]** time and starts all over again the process of csma by CD is shown

**[10:46]** in flowchart in this flowchart when a station is ready to send data it senses

**[10:53]** the channel if channel is busy it makes a new attempt to set s the channel if

**[11:01]** 11 minutes, 1 second channel is free it transmits data and senses the channel for Collision in case collisions are

**[11:10]** detected it transmits a jam signal to indicate that Collision has occurred and

**[11:17]** it wait as per back of strategy if no collisions are detected

**[11:26]** transmission completes CSM by CD uses the conceptual model

**[11:34]** shown in figure CSM by CD can be in one of three states contention transmission

**[11:44]** or idle at the point marked t0 a station has finished transmitting its

**[11:53]** frame any other station having a frame to send may now attempt to do so if two

**[12:01]** 12 minutes, 1 second or more stations decide to transmit simultaneously there will be a

**[12:08]** collision collisions can be detected by looking at the power or pulse width of

**[12:15]** the received signal and comparing it to the transmitted signal after a station

**[12:23]** detects a collision it aborts its transmission weits a r period of time

**[12:30]** and then tries again assuming that no other station has started transmitting

**[12:38]** in the meantime therefore our model for csma by CD will consist of alternating

**[12:47]** contention and transmission periods with ideal periods occurring when all

**[12:54]** stations are quiet now let us see what happens if Collision occurs after

**[13:03]** the first Collision each station Waits either zero or one slot times before

**[13:10]** trying again if two stations Collide and each one picks the same random number they

**[13:19]** will collide again after the second Collision each one picks either 0o 1 2

**[13:28]** or three at random and waits that number of slot

**[13:35]** times if a third Collision occurs then again the number of slots to wait is

**[13:42]** chosen at random from the interval 0 to

**[13:47]** 2 ^ 3 - 1 that is 7 in journal after I

**[13:54]** collisions a random number between zero and 2 to the^ IUS 1 is chosen and that

**[14:04]** number of slots is skipped however after 10 collisions have

**[14:10]** been reached the randomization interval is Frozen at maximum of

**[14:16]** 1023 slots after 16 collisions the controller throws in the towel and

**[14:24]** reports failure back to the computer further recovery is up to the higher

**[14:32]** layers this algorithm is called binary exponential back off now let us see the

**[14:41]** reason for having padding bits in Ethernet frame reason for having a minimum length

**[14:49]** frame is to prevent a station from completing the transmission of a short

**[14:56]** frame before the first bit has even reached the far end of the cable where

**[15:03]** it may collide with another frame this problem is Illustrated in

**[15:09]** figure in figure a at Time Zero station a at one end of the network sends off a

**[15:18]** frame let T be the propagation time for this Frame to reach the other end B in

**[15:27]** figure B just before the frame gets to the other end that is at time T minus E

**[15:35]** the most distant station B starts transmitting as shown in figure C when B

**[15:43]** detects that it is receiving more power than it is putting out it knows that a

**[15:50]** collision has occurred so it aborts its transmission

**[15:56]** and generates a 40 8bit noise burst to warn all other stations in other words

**[16:06]** it jams The Ether to make sure the sender does not miss the collision at about time

**[16:16]** 2T the sender sees the noise burst and about its transmission as shown in

**[16:23]** figure D it then Waits a random time before trying

**[16:29]** again if a station tries to transmit a very short frame and collision occurs

**[16:36]** the sender will then incorrectly conclude that the frame was successfully

**[16:44]** sent to prevent this situation from occurring all frames must take more than

**[16:50]** 2T time to send data frame so that the transmission is still taking place when

**[16:58]** and the noise burst gets back to the sender that is the reason why padding

**[17:06]** bits are added so that transmission is not complete in 2T time frames with

**[17:14]** fewer than 64 bytes are padded out to 64 bytes with a pad

**[17:22]** field so this was about ethernet now let us move on to fast ethernet fast

**[17:30]** ethernet is traditional csma by CD at 100 Mbps over twisted pair cable the

**[17:40]** idea of fost ethernet was first proposed in 1992 during the early development of

**[17:49]** fast ethernet two different groups worked out standard proposals and both

**[17:55]** were finally approved but under different itle committees one standard

**[18:03]** passed a full review in June 1995 and was formally assigned the name

**[18:12]** 802.3 U and the other became 100 VG any

**[18:18]** Lan which is now governed by I 802.2

**[18:24]** committee the letter uses the demand priority media exess method instead of

**[18:31]** CSM by CD method 100 VG any Lan has not caught on

**[18:40]** while fast ethernet enjoyed great success in Enterprise Lan

**[18:48]** environment due to slow speed of ethernet fast ethernet came into existence which is simple speed up

**[18:56]** version of ethernet with same rules and regulations the 802.3 committee decided

**[19:06]** to go with a speed up ethernet for three primary reasons one the need to be

**[19:14]** backward compatible with existing ethernet Lens two the fear that a new protocol

**[19:23]** might have unforeseen problems three the desire to get the job done before the

**[19:32]** technology changed in fast ethernet instead of creating a completely new

**[19:39]** protocol the itle decided to keep all the old packet formats

**[19:46]** interfaces and procedural rules and simply reduce the bit time

**[19:53]** from 100 nond to 10 nanc this effectively increased the

**[20:00]** bandwidth to 100 Mbps the protocol was officially known as

**[20:08]** 802.3 U but was more commonly called Fast ethernet the change in bit time

**[20:17]** presented a number of challenges to the designers of fast ethernet the reduction

**[20:24]** in bit time increases the number of bits sent within a set time period however these

**[20:33]** bits still take the same amount of time to travel across a length of wire that

**[20:40]** is the propagation delay is the same over a given length this means that more

**[20:48]** bits will be sent during the propagation delay time used as the Collision

**[20:56]** window either minim minimum frame size need to be increased or the propagation delay need to be reduced by reducing

**[21:06]** cable length changing the minimum frame size would have caused problems with a

**[21:14]** backward compatibility of this standard so the maximum Network size was reduced

**[21:22]** with typical maximum cable length of 100 m now let us see different media types

**[21:32]** supported by fast ethernet fast ethernet defines three basic physical layer

**[21:40]** specifications as shown in figure 100 base

**[21:46]** T4 this uses Category 3 four pair twisted pair

**[21:53]** cable it supports a distance of 100 m and RJ 45

**[22:00]** connectors 100 Bas TX this uses Category 5 twisted pair

**[22:07]** which are more expensive than Category 3 cables these are Cat 5 UTP or type 1 STP

**[22:18]** cable with RJ45 connectors this scheme allows full duplex

**[22:26]** communication stations can trans transmit at 100 Mbps and receive at 100

**[22:32]** MVPs at the same time 100 base FX this uses two strands

**[22:42]** of 62.5 or 125 multimode fiber one for each

**[22:49]** Direction so it to is full duplex with 100 Mbps in each Direction in addition

**[22:59]** the distance between a station and a hub

**[23:04]** can be up to 2,000 M it supports SC mic

**[23:11]** or STD connectors there are also few other physical standards in fast ethernet

**[23:20]** which will be explained now 100 base SX it is a version of fast ethernet over or

**[23:28]** optical fiber it uses two strands of multimode optical fiber for receive and

**[23:37]** transmit it is a lower cost alternative to using 100 base effects because it

**[23:46]** uses short wavelength Optics which are significantly less expensive than the

**[23:54]** long wavelength Optics used in 100 base FX 100 base SX can operate at distances

**[24:04]** up to 550 M 100 base BX it is a version of

**[24:13]** fast ethernet over a single strand of optical fiber single mode fiber is used

**[24:21]** along with a special multiplexer which splits the signal into transmit and re receive wavelengths the

**[24:30]** two wavelengths used for transmit and receive are 131 nanometer and 1 1550

**[24:40]** nanometer distances supported are 10 20 or 40

**[24:49]** kilom 100 base LX 10 it is a version of fast ethernet over two single mode optic

**[24:59]** fibers it has a nominal reach of 10 kilm and a nominal wavelength of

**[25:06]** 1310 nanometer now let us move on to layered protocol architecture of fast

**[25:14]** ethernet various layers of the fast ethernet protocol architecture are shown in

**[25:22]** figure the Mii is medium independent interface between the Mac layer and the physical

**[25:31]** layer it allows any physical layer to be used with the Mac layer the Mii provides

**[25:41]** two media status signals one indicates presence of the carrier and the other

**[25:48]** indicates absence of collision the reconcilation Su layer

**[25:54]** Maps these signals to physical signaling primitiv understood by the existing map

**[26:03]** the physical layer is divided into three sublayers physical coding sublayer PCS

**[26:11]** this sublayer provides a uniform interface to the reconcilation layer for

**[26:17]** all physical media carrier sense and collision detect indications are

**[26:24]** generated by this sublayer it also manages the autonegotiation

**[26:31]** process by which the network interface card communicates with the network to

**[26:38]** determine the network speed 10 or 100 MVPs and mode of operation whether it is

**[26:47]** half duplex or full duplex physical medium attachment PMA

**[26:54]** this sublayer provides a medium indep dependent means for the PCS to support

**[27:02]** various serial bit oriented physical media this layer serializes code groups

**[27:10]** for transmission and deserializes bits received from The

**[27:16]** Medium into code groups physical medium dependent PMD this Maps the physical

**[27:26]** medium to the PM it defines the physical layer signaling used for various

**[27:35]** media so this was about layered protocol architecture of fast

**[27:41]** ethernet frame format of fast ethernet is same as that of

**[27:48]** ethernet so friends this was ethernet and fast ethernet finally summarizing we

**[27:56]** learned about introduction to ethernet which was followed by layered protocol

**[28:03]** architecture and details of physical and Mac operations in Ethernet after

**[28:10]** ethernet we discussed fast ethernet hope the concepts explained in

**[28:18]** this lecture were understandable and helpful hope to see you again in the

**[28:25]** next lecture till then goodbye bye enjoy the day thank you

**[28:32]** [Music]
