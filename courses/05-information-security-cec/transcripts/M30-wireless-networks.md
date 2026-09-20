# Wireless Networks

**Module 30**  
Duration: 29:13  
Video: https://www.youtube.com/watch?v=MdLxztyDzck

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Navdeep Singh, Department of Computer Engineering, Punjabi University, Patiala

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:15]** my dear students hello I welcome you all in our series of lectures on cyber security today we are going to study

**[0:24]** about how to identify basic topologies and their variations we'll also learn about how to determine appropriate topology for a

**[0:33]** given Network plan so let us begin with it so the first thing is what is a wireless

**[0:41]** network a wireless network is any type of computer network that uses wireless data connections for connecting network

**[0:50]** nodes Wireless networking is a method by which homes telecommunication networks and Enterprise installations avoid the

**[0:59]** costly process of introducing cables into a building or as a connection between various equipment

**[1:06]** locations Wireless telecommunication networks are generally implemented and administered using radio

**[1:14]** communication this implementation takes place at the physical layer of the Osa model Network

**[1:21]** structure now what are the various types of wireless networks wireless networks are

**[1:28]** categorized into number one Wireless pan number two wireless LAN number three

**[1:35]** Wireless man and number four Wireless van let us study them one by

**[1:42]** one number one Wireless pan pans stands for personal area networks Wireless pans interconnect

**[1:51]** devices within a relatively small area that is generally within a person's Reach For example both Bluetooth radio

**[2:00]** and invisible infrared light provides a while span for interconnecting a headset to a

**[2:07]** laptop now what is a Bluetooth Bluetooth is a wireless technology used to transfer data between different electronic

**[2:16]** devices the distance of data transmission is small in comparison to other modes of wireless

**[2:24]** communication this technology eradicates the use of cords cables adapters and permits the electronic devices to

**[2:31]** communicate wirelessly among each other a Bluetooth Lan is an ad hoc network which means that the network is

**[2:40]** formed spontaneously the devices sometimes called gadgets find each other and make a network called EP

**[2:48]** piconet a Bluetooth lan can even be connected to the internet if one of the gadgets has this

**[2:56]** capability Bluetooth was originally started as a project by the company it is named for Herald blaten the king of

**[3:03]** Denmark who United Denmark and Norway blaten translates to Bluetooth in English Today Bluetooth technology is

**[3:13]** the implementation of a protocol defined by the Ia 802.15 standard the Bluetooth protocols let the

**[3:22]** devices find and connect to each other an act called pairing and scarely transfers data

**[3:30]** Bluetooth defines two types of networks piconet and scatternet a Bluetooth Network called a

**[3:37]** piconet is a small net a piconet can have up to eight stations one of which is called the primary the rest are

**[3:44]** called the secondaries all the scandy stations synchronize their clocks and hopping sequence with the

**[3:53]** primary note that a piconet can have only one primary station the communication between the primary and

**[4:00]** the secondary can be one to one or one to many the figure shows a piconet although a ponet can have a

**[4:09]** maximum of seven scaries and additional eight scaries can be in the park State a secondary in a park state is

**[4:17]** synchronized with the primary but cannot take part in communication until it is moved from the park

**[4:25]** State because only eight stations can be active in a ponet active activating a station from the parkk state means that

**[4:32]** an active station must go to the park state next is

**[4:39]** scatternet piconets can be combined to form what is called a scatter net a scand station in one ponet can be the

**[4:47]** primary in another ponet this station can receive messages from the primary in the first ponet as a

**[4:55]** secondary and acting as a primary deliver them to the secondaries in the second ponet a station can be a member of two

**[5:04]** piconets now coming back to the Bluetooth let us discuss Bluetooth in detail Bluetooth uses a 2.4 GHz ISM band

**[5:12]** divided into 79 channels of 1 MHz each Bluetooth uses the frequency hopping spread Spectrum method in the

**[5:21]** physical layer to avoid interference from other devices or other networks Bluetooth hop, 1600 times per

**[5:30]** second which means that each device changes its modulation frequency 1600 times per second to transform bits to a

**[5:38]** signal Bluetooth uses a sophisticated version of FSK called gfsk that is FSK

**[5:45]** with goian bandwidth filtering gfsk has a carrier frequency bit one is represented by

**[5:54]** frequency deviation above the carrier bit a is represented by a frequency deviation below the carrier the frequencies in megahertz are

**[6:03]** defined according to the formula FC is = 2402 + n for n is equal to 0 1 2 3 up to

**[6:11]** 78 for each channel for example the first channel uses carrier frequency 242 MHz and the

**[6:20]** second Channel uses carrier frequency 243 mahz the link control or Bas band layer

**[6:28]** is somewhat analogous to the Max sub layer but also includes elements of the physical layer it deals with how the master

**[6:37]** controls time slots and how these slots are grouped into frames the link manager handles the establishment of logical channels

**[6:45]** between devices including power management pairing and encryption and quality of service it lies below the host

**[6:54]** controller interface line this interface is a convenience for implementation typically the protocols

**[7:02]** below the line will be implemented on a Bluetooth chip and the protocols above the line will be implemented on the

**[7:09]** Bluetooth device that host the chip the link protocol above the line is

**[7:15]** L2 capab called logical link control adaption protocol it frames variable length

**[7:22]** messages and provides reliability if needed many protocols uses L2 cap such

**[7:29]** as the two utility protocols that are shown the service Discovery protocol is used to locate services within the

**[7:38]** network the radio frequency communication protocol emulates the standard serial Port found on the PCS for connecting the keyboard mouse and

**[7:46]** modem among other devices the top layer is where the applications are located the profiles

**[7:54]** are represented by vertical boxes because they each Define a slice of the protocol stack for a particular

**[8:01]** 8 minutes, 1 second purpose specific profiles such as the headset profile usually contain only those protocols needed by that

**[8:09]** application and no others for example profiles may include L2 cap if they have Packers to send but

**[8:17]** skip L2 cap if they have only a steady flow of audio samples now let us discuss about frame

**[8:25]** format of Bluetooth here in the figure we have various fields such as number one access

**[8:33]** code this 72 bit field normally contains synchronization bits and the identifier of the primary to distinguish the frame

**[8:41]** of one ponet from another number two header this 54 bit field is a repeated 8bit pattern it is further divided into

**[8:50]** six subfields the subfields are number one address the 3-bit address of field can

**[8:58]** Define up to 7 secondaries if the address is zero it is used for broadcast communication from the primary to all the

**[9:07]** secondaries number two type the 4bit type sub field defines the type of data coming from the upper

**[9:15]** layers number three F this onebit subfield is for flow control when set it indicates that the

**[9:23]** device is unable to receive more frames that is buffer is full number four

**[9:31]** a this one bit sub field is for acknowledgement Bluetooth uses stop and weight arq one bit is sufficient for

**[9:39]** acknowledgement number five s this 1 bit subfield holds a sequence

**[9:46]** number Bluetooth uses stop and wait arq 1 bit is sufficient for sequencing

**[9:53]** numbering number six HC the 8bit header error correction of field is a checkm to detect errors in

**[10:02]** each 18-bit header section the header has three identical 18-bit sections the receiver Compares these

**[10:10]** sections bit by bit if each of the corresponding bits is the same the bit is accepted if not the majority opinion

**[10:20]** rules this is a form of forward error correction this double error control is needed because the nature of the

**[10:27]** communication via eror is very noisy note that there is no retransmission in this sub

**[10:34]** layer then comes payload this sub field can be 0 to 2740

**[10:41]** bits long it contains data or control information coring from the upper layers now let us see various

**[10:50]** applications of Bluetooth number one Bluetooth biggest contribution is to provide a phone with a headset that

**[10:58]** works wirelessly this is possible by providing the collar with an earpiece and a small microphone attached to the caller

**[11:06]** shirt the mobile phone can be located in a bag or anywhere in the body the caller can do a number even

**[11:15]** without touching a button on the mobile phone this technology has the advantage of eliminating the radiation hitting the cerebral

**[11:23]** region number two PDA PC or laptop which has enabled Bluetooth can communicate

**[11:30]** with each other and update with its latest information this technology has helped in synchronizing the data

**[11:39]** easily number three it is difficult to send emails while traveling in a flight on Landing of the flight the Bluetooth

**[11:48]** enabled laptop can send the email only when it gets in touch with the user's phone number four wireless mouse and

**[11:57]** keyboards number number five one will be alerted on his or her mobile phone when your laptop receives the

**[12:04]** mail number six you can try to locate a printer via laptop you will get the print out of that document once that

**[12:12]** printer is located so Bluetooth has many applications possible because of the many features that the Bluetooth possess

**[12:21]** the key features of Bluetooth technology are number one less complication number two less power

**[12:28]** consumption number three available at cheaper rates and number four robustness now let us discuss next kind

**[12:36]** of wireless networks called Wireless lens Wireless lens are most important

**[12:43]** Access Network Technologies in the internet most popular is the it 802.11 Wireless landan known also as

**[12:52]** Wi-Fi there are several standards for wireless land technology the standard defines two

**[13:00]** kinds of services the basic service set BSS and the extended service set

**[13:06]** ESS now what is basic service set i e 802.11 defines the basic service set as

**[13:13]** the building block of a wireless lamp a basic service set is made of stationary or mobile wireless stations and an

**[13:21]** optional Central base station known as the access point figure shows two sets in this standard

**[13:29]** the BSS without an AP is a standalone Network and cannot send data to any other

**[13:35]** BSS it is called an ad hoc architecture in this architecture stations can form a network without the need of an AP they

**[13:45]** can locate one another and agree to be part of a BSS a BSS with an AP is sometimes

**[13:52]** referred to as an infrastructure Network when multiple BSS are connected the ations Within Reach of one another can

**[14:01]** 14 minutes, 1 second communicate without the use of an AP however communication between two stations in two different BSS usually

**[14:10]** occurs via two APS the idea is similar to Communication in a cellular network if we consider

**[14:17]** each BSS to BSL and each AP to be B station note that a Mobile station can

**[14:25]** belong to more than one BSS at the same time next is station types i e

**[14:34]** 802.11 defines three types of stations based on their mobility in a wireless lamp number one no

**[14:42]** transition number two BSS transition and number three ESS transition Mobility a station with no transition

**[14:51]** Mobility is either stationary or moving only inside a BSS a station with BSS transition

**[14:59]** Mobility can move from one PSS to another but the movement is confined inside one

**[15:06]** ESS a station with ESS transition Mobility can move from one es to another

**[15:12]** however I E 802.11 does not guarantee that communication is continuous during the move then comes Max upair I

**[15:22]** 802.11 defines two Max of layers the distributed coordination function DCF and point coordination function

**[15:30]** PCF one of the two protocols defined by it at the max sub layer is called the distributed coordination

**[15:38]** function distributed coordination function uses CSM CA as the exess

**[15:44]** method Wireless lens cannot Implement csms CD for three reasons number one for Collision detection a station must be

**[15:53]** able to send data and receive Collision signals at the same time this can mean mean costly stations

**[16:00]** and increased bandwidth requirements number two Collision may not be detected because of the Hidden

**[16:08]** station problems number three the distance between stations can be great signal

**[16:15]** fading could prevent a station at one end from hearing a collision at the other end the point coordination function is

**[16:23]** an optional access method that can be implemented in an infrastructure Network not in an ad hoc

**[16:31]** network it is implemented on top of the DCF and is used mostly for time sensitive

**[16:39]** transmission PCF has a centralized contention free polling access method the AP performs polling for

**[16:46]** stations that are capable of being pulled the stations are ped one after another sending any data they have to

**[16:54]** the AP to give priority to PCF over DCF another set of interframe spaces has been

**[17:02]** defined Pips and sifts the sifs is the same as that in DCF but the Pips is

**[17:09]** shorter than the DFS this means that if at the same time a station wants to use only DCF and an

**[17:17]** AP wants to use PCF the AP has priority next is frame

**[17:25]** format the Mac clear frame consists of 9 ft number one frame control

**[17:32]** FC the FC field is two bytes long and defines the type of frame and some control

**[17:39]** information in all frame types except one this field defines the duration of the transmission that is used to set the

**[17:47]** value of NY in one control frame this field defines the ID of the

**[17:54]** frame number two address there are four address fields each six bytes long the meaning of each

**[18:01]** 18 minutes, 1 second address field depends on the value of the two DS and from DS subfields number three sequence control

**[18:10]** this field defines the sequence number of the frame to be used in flow control number four frame

**[18:18]** body this field which can be between 0 and 2312 bides contains information based on the type and the subtype

**[18:27]** defined in the FC field number five FCS the FCS field is 4 bytes long and contains a crc32 error

**[18:36]** detection sequence then comes frame types a wireless land defined by i e 802.11 has three categories of frames

**[18:45]** management frames control frames and data frames let us discuss them one by one number one management

**[18:54]** frames management frames are used for the initial communication between the stations and access

**[19:01]** 19 minutes, 1 second points number two control frames control frames are used for accessing the channel and acknowledging

**[19:10]** frames number three data frames data frames are used for carrying data and control

**[19:19]** information next is hidden and exposed station problems let us discuss hidden node problem

**[19:27]** first as show shown in the figure station B has a transmission range shown by the left oval every station in this

**[19:35]** range can hear any signal transmitted by station B station C has a transmission range

**[19:43]** shown by the right oval every station located in the range can hear any signal transmitted by

**[19:50]** C station C is outside the transmission range of B likewise station B is outside

**[19:57]** the transmission range of C station a however is in the area covered

**[20:03]** by both B and C it can hear any signal transmitted by B or C assume that station B is sending data

**[20:12]** to station a in the middle of this transmission station C also has data to send to station

**[20:19]** a however station C is out of B's range and Transmissions from B cannot reach C

**[20:26]** therefore C thinks the is free station C sends its data to a which results in equal at a because this station is

**[20:36]** receiving data from both B and C in this case we say that station B and C are hidden from each other with

**[20:44]** respect to a hidden stations can reduce the capacity of the network because of the possibility of the

**[20:53]** Collision the solution to the hidden station problem is the use of the handshake frames figure shows that the RTS message

**[21:02]** breaches a but not C however because both B and C are within the range of a the CTS message

**[21:11]** which contains the duration of data transmission from B to a reaches C station C knows that some hidden

**[21:19]** station is using the channel and refrains from transmitting until their duration is over now let us discuss expose station

**[21:27]** problem now consider a situation that is inverse of the previous one the exposed station

**[21:34]** problem in this problem a station refrains from using a channel when it is in fact available in the figure station a is

**[21:44]** transmitting to station B station C has some data to send to station D which can be sent without

**[21:51]** interfering with the transmission from A to B however station C is exposed to transmission from a

**[21:59]** it hears what a is sending and thus refrains from sending in other words C is too conservative and was the capacity of the

**[22:08]** channel the handshaking messages RTS and CTS cannot help in this

**[22:14]** case station C hears the RTS from a but does not hear the CTS from B station C after hearing the RTS from a

**[22:24]** can wait for time so that the CTS from B reaches a it then sends an RTS to D to show that

**[22:31]** it needs to communicate with d both stations b and a may hear this RTS but station a is in the sending

**[22:40]** State not the receiving State station B however responds with a CTS the problem is here if station a has

**[22:49]** started sending its data station C cannot hear the CTS from station D because of the Collision it cannot sends

**[22:57]** its data to D it remains exposed until a finishes sending its data next is Wireless

**[23:06]** man Wireless metropolitan area network is a type of wireless network that connects several Wireless

**[23:13]** lens ymax is a type of wiress man and is described by the i e 802.16

**[23:21]** standard ymax is basically a technology that enables viess transmission of data packets at broadband data rate

**[23:30]** it empowers computer or mobile terminals with enhanced mobility and ability to access high-speed internet without the

**[23:38]** need of connecting the terminal to any cable network or Wi-Fi hotspot implementation of VX requires a

**[23:47]** similar scale of basic telecommunication infrastructure as built in case of a voice communication Network like GSM and

**[23:57]** CDMA BAS base stations sectorized antenas control centers and other critical constituents generally a part

**[24:05]** of such infrastructure wmax network has often been claimed in media to be capable of

**[24:12]** providing Broadband speeds to a coverage of over 30 Mi with a single base station but that's possible only in ideal

**[24:20]** conditions practically a single base station can provide a satisfactory Broadband access within a range of 4 to 5 month

**[24:29]** miles with line of sight conditions the coverage can go up to 10 miles rest of the coverage and quality

**[24:36]** of service details are solely dependent upon the Terren and population conditions then comes wiress when

**[24:45]** Wireless wide area networks are wireless networks that typically cover large areas such as between neighboring towns

**[24:52]** and cities these networks can be used to connect Branch officers of business or as a public internet access

**[25:01]** 25 minutes, 1 second system the wireless connections between access points are usually pointto Point microwave links using parabolic tissues

**[25:08]** on the 2.4 GHz band rather than only directional antennas used with smaller

**[25:15]** networks a typical system contains base station gateways access points and wireless bridging

**[25:23]** relays other configurations are mesh systems where each access point access as a

**[25:29]** relay Wireless technology is also used in cellular telephony and satellite networks cellular telepone is designed

**[25:38]** to provide Communications between two moving units called mobile stations or between one mobile unit and one stationary unit often called a land

**[25:48]** unit a service provider must be able to locate and track a caller assign a channel to the call and transfer the

**[25:55]** channel from base station to the base station as the caller moves out of range to make this tracking possible

**[26:03]** each cellular service area is divided into small regions called cells each cell contains an antenna and

**[26:11]** is controlled by a solar or AC powered Network station called the base station each base station is controlled

**[26:19]** by a switching office called a mobile switching Center msse the msse coordinates communication between all the base stations and the

**[26:27]** telephone phone central office it is a computerized center that is responsible for connecting calls

**[26:34]** recording call information and billing cell size is not fixed and can be increased or decreased depending on

**[26:42]** the population of the area high density areas require more geographically smaller cells to meet

**[26:49]** traffic demands that do low density areas once determined cell size is optimized to prevent the interference of

**[26:58]** adjacent cell signals the transmission power of each cell is kept low to prevent its signal

**[27:05]** from interfering with those of other cells last but not the least is satellite

**[27:12]** Network a satellite network is a combination of nodes some of which are satellites that provide communication from one point on the earth to

**[27:22]** another a node in the network can be a satellite an earth station or an end user terminal or

**[27:29]** telephone although a natural satellite such as the moon can be used as a laying node in the network the use of artificial satellites

**[27:38]** is preferred because we can install electronic equipment on the satellite to regenerate the signal that has lost its

**[27:45]** energy during travel another restriction on using natural satellites is their distance from the earth which creates a long

**[27:54]** delay in communication satellite networks are like cellular networks in that they divide the planet into

**[28:03]** cells satellites can provide transmission capability to and from any location on Earth no matter how

**[28:11]** remote this Advantage makes high quality communication available to undeveloped parts of the world without requiring a

**[28:18]** huge investment in groundbased infrastructure so with this our today's lecture is over today we discussed about

**[28:26]** the various basic topologies and their variations we also discussed about Wireless standards and their various features apart from their

**[28:35]** advantages so I hope you understood today's lecture in the next lecture we'll discuss about Security

**[28:42]** Management till then goodbye thank you

**[28:46]** [Music]

**[28:58]** n

**[29:00]** [Music]
