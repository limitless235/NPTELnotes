# 10 Gigabit Ethernet

**Module 26**  
Duration: 35:29  
Video: https://www.youtube.com/watch?v=yu-UWXqj5wE

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:12]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:20]** University of Science and Technology Hisar harana I welcome you all to the video lecture series of cyber and

**[0:30]** information security in this lecture we will study about 10g ethernet which is

**[0:36]** basically used for data transmission on wired Lan at speed of 10

**[0:44]** gbps first of all please see the contents which I shall cover after covering brief introduction about 10

**[0:53]** gbit ethernet I shall take up layered protocol architecture of 10 GB ethernet

**[1:00]** which will be followed by physical and Mac layer of 10 GB ethernet in last I

**[1:09]** shall take up 10 GB ethernet standards so now let us start as the

**[1:17]** demand for highspeed Network grow the need for a faster ethernet technology is

**[1:24]** apparent in March 1999 a working group was formed as higher speed study group

**[1:33]** hssg to develop a standard for 10 gab ethernet 10 gab ethernet being

**[1:42]** standardized as i e 823a is a telecommunication technology

**[1:50]** that offers data speeds up to 10 billion bits per second 10 gabit ethernet called

**[2:00]** as 10 G or 10 GBE or 10 gig e is a group

**[2:08]** of computer networking Technologies for transmitting ethernet frames at a rate

**[2:14]** of 10 gab bits per second it was first defined by the i e

**[2:22]** 802.3 AE 2002 standard unlike previous ethernet

**[2:29]** standard standards 10 GB ethernet defines only full duplex Point topoint

**[2:36]** links which are generally connected by Network switches in gigabit Ethernet

**[2:44]** shared medium csma by CD operation has not been carried over from the previous

**[2:52]** generation ethernet standards half duplex operation and hubs

**[2:59]** do do not exist in 10 GBE like previous versions of ethernet

**[3:06]** 10 GBE can use either copper or Fiber cabling however because of its bandwidth

**[3:15]** requirement higher grade copper cables are required like Category 6 6A or

**[3:24]** category 7 cables for links up to 100 m different I E

**[3:32]** 802.3 standard for 10g ethernet are as shown in

**[3:40]** table i e 802.3 AE reified in 2002 supports 10

**[3:49]** gbits per second over fiber for landan and when i e

**[3:58]** 802.3 a K defined in 2004 supports 10

**[4:05]** gbit per second over twin XL cable i e

**[4:13]** 802.3 2005 is a revision of Base standard

**[4:19]** incorporating the prior amendments and era i e

**[4:27]** 802.3 n defined in 2006 supports 10

**[4:33]** gbits per second over copper twisted pair cable i e

**[4:42]** 802.3 a defined in 2007 is back plane ethernet which

**[4:50]** supports 1 and 10 gbits per second over

**[4:56]** printed circuit boards i e

**[5:02]** 802.3 AQ defined in 2006 supports 10

**[5:09]** gbits per second over multimode fiber with enhanced

**[5:17]** Equalization i e 802.3 2008 is a revision of Base

**[5:25]** standard i e 82.3 AV defined in 2009 is 10 gbit per second

**[5:36]** ethernet physical for Eon i e 82.3

**[5:43]** 2012 is latest version of Base standard now let us see layered protocol

**[5:53]** architecture of 10 GB ethernet the ethernet protocol basically

**[5:59]** implements the bottom two layers of the open system interconnect OSI model that

**[6:08]** is the data link and physical sublayers figure depicts the typical

**[6:15]** ethernet protocol stack and the relationship to the OSI model physical

**[6:22]** layer of OSI is mapped onto PMD PMA PCS and

**[6:31]** reconcilation Su layer RS Network layer of OSI is mapped onto

**[6:39]** map and LLC layer basic mediums

**[6:44]** supported by 10g ethernet R 10g base R

**[6:50]** for Len fiber 10g Bas W for Van fiber

**[6:56]** and 10 G base x for copper the architecture of ethernet subdivides the

**[7:04]** physical layer into three sub layers the physical medium dependent PMD sublayer

**[7:13]** the physical medium attachment PMA and a physical coding sublayer

**[7:21]** PCS PMD physical medium dependent the PMD sublayer is responsible for

**[7:30]** signaling transmission the typical PMD functionality includes amplifier

**[7:37]** modulation and wave shaping different PMD devices May support different

**[7:45]** media PCS physical coding sublayer the PCS sublayer consist of coding and a

**[7:55]** serializer or multiplexing functions the structure of this layer is defining

**[8:02]** feature that differentiates the Lan and Van physical for the van physical the

**[8:10]** PCS operates in a serialized fashion for the L physical it operates in two

**[8:19]** different modes first is parallel mode in which there is a multiplexer that

**[8:26]** multiplexes the data onto four 2.5 gbps

**[8:32]** lines second is serial L that acts as a serializer that serializes and

**[8:42]** deserializes the data to and from a single channel the serial Lan physical

**[8:50]** uses a 64bit by 66 bit coding scheme for

**[8:57]** the serial when physical and additional sublayer the van interface sublayer

**[9:06]** W is required between the serial PCS and the serial

**[9:14]** PMA the Wiis sublayer ensures operability with Sonet by including a

**[9:22]** simplified Sonet frame in w p ma physical medium attachment the

**[9:33]** PMA sublayer is responsible for serialization of code groups into bit

**[9:40]** stream suitable for serial bit oriented physical devices and vice versa it

**[9:49]** supports multiple encoding schemes in support of the different pmds that use

**[9:56]** an encoding that is specific to the medium it supports

**[10:03]** reconcilation sublayer the reconcilation sublayer acts as a command translator it

**[10:11]** Maps the terminology and commands used in the Mac layer into electrical formats

**[10:19]** appropriate for the physical layer entities medium access control Mac the

**[10:27]** medium access control sub layer provides a logical connection between the Mac

**[10:34]** clients of itself and its peer station its main responsibility is to initialize

**[10:43]** control and manage the connection with the peer station

**[10:50]** xgm I 10 gigabit media independent

**[10:57]** interface it provides a standard interface between the Mac layer and the

**[11:03]** physical layer it isolates the Mac layer and the physical layer enabling the Mac

**[11:11]** layer to be used with various implementations of the physical layer

**[11:19]** MDI medium dependent interface it defines different connector types for

**[11:26]** different physical media and BD devices first let us see physical layer

**[11:34]** architecture of 10g ethernet one of the first things that anyone familiar with

**[11:41]** ethernet would notice about 10 gabit variant is that there are two options

**[11:49]** for implementing the physical layer first is serial solution and second is

**[11:55]** parallel solution the serial solution uses is one highspeed

**[12:02]** 10gbps PCS PMA PMD circuit block and the

**[12:08]** parallel solution uses multiple PCS PMA PMD slow speed links Each of which

**[12:17]** operates at lower speed in the serial implementation there is one physical

**[12:24]** Channel operating at 10 GBS per second as shown in figure the operation is

**[12:33]** straightforward for transmission the reconcilation module passes the signals

**[12:40]** corresponding to the make data word by word to the PCS module the PCS module

**[12:48]** then encodes the signals with a predefined coding technique and passes

**[12:55]** the encoded signal to the PMA module modle the PMA module then serializes the

**[13:04]** encoded signals and passes the stream to the PMD module the PMD module transmits

**[13:13]** the signal stream over the fiber at 10 gbits per second on receiving side the

**[13:22]** process is reverse the main advantage of the serial architecture is that the

**[13:30]** transmitting receiving operation is straightforward it does not require a

**[13:37]** complicated multiplexing or demultiplexing that is needed in the parallel

**[13:44]** implementation in parallel implementation there are multiple physical channels say n subchannels that

**[13:52]** may be implemented by using parallel cables or wdm

**[13:59]** multiplexing for transmission the distributor multiplexes the data accepted from the Mac layer into n

**[14:09]** streams in the round robin motion each stream is given to each PCS

**[14:17]** module each PCS module encodes the received stream and passes it to each

**[14:25]** PMA module for serialization after

**[14:31]** serialization each PMD module transmits each serialized data stream at the rate

**[14:38]** of 10 divided by n gbits per second on

**[14:45]** receiver side reverse process is done the process is shown in

**[14:53]** figure the main advantage of the parallel implementation is that the

**[14:59]** operating rate in the PCS PMA module is reduced which enables cheaper devices

**[15:08]** like cimos or bipolar to be used the disadvantages are the need of

**[15:16]** distributor or collector module that may be sensitive to timing Jitters and the

**[15:24]** usage of multiple sets of logic circuits and Laser equipment now let us see Mac layer of

**[15:33]** 10g ethernet the Mac layer of 10 GB ethernet is very similar to the Mac layer of

**[15:43]** previous ethernet Technologies it uses the same ethernet address and frame formats but it does

**[15:52]** not support the half duplex mode it supports data rates of less than

**[15:59]** 10 gbps using a pacing mechanism for rate adaptation and flow control it

**[16:09]** supports full duplex mode only in previous ethernet standards there were

**[16:16]** two modes of operation half duplex and full duplex the half duplex mode has

**[16:23]** been defined since the original version of ethernet in this mode data is

**[16:31]** transmitted using the popular CSM by CD protocol on a shared medium its

**[16:39]** Simplicity contributed to the early success of the ethernet standard this

**[16:46]** mode of operation is so famous that many wrongly associate the csma by CD

**[16:53]** protocol with standard ethernet operation efficiency and distance limitation are the main

**[17:03]** disadvantages of the half duplex mode in this mode the link distance is limited

**[17:10]** by the minimum Mac frame size this restriction reduces the efficiency

**[17:18]** drastically for high rate transmission at the transmission rate of

**[17:25]** 10 gbps the half duplex mode is not an attractive option and no Market would

**[17:33]** realistically exist for the half duplex operation at this rate of transmission

**[17:40]** as most of the Links at 10 gbps are point to point over Optical

**[17:48]** fibers in this case the full duplex operation would be the preferred option

**[17:55]** so the standard for 10 GB ethernet specifies only the full duplex operation

**[18:04]** in full duplex operation there is no contention the Mac layer entity can

**[18:10]** transmit whenever it wants provided that its Speer is ready to

**[18:18]** receive Mac frame format the key purpose of developing 10 GB ethernet standard is

**[18:26]** to use the same Mac frame format as specified in the preceding ethernet

**[18:34]** standards this will allow a seamless integration of the 10 GB ethernet with

**[18:40]** the existing ethernet networks since the full duplex operation is used the link

**[18:48]** distance does not affect the Mac frame size the minimum Mac frame size will be

**[18:56]** made equal to 6 four octets as specified in the previous ethernet

**[19:04]** standards the macrame format is depicted in figure carrier extension is not required

**[19:14]** here the 10g ethernet frame format consist of the following Fields Preamble

**[19:23]** PR it consist of seven bytes the Preamble is an alter alternating pattern

**[19:30]** of ones and zeros that tells receiving stations that a frame is coming and that

**[19:37]** provides a means to synchronize the frame reception portion of receiving

**[19:44]** physical layers with the incoming bit stream start of frame delimiter s

**[19:53]** oof it consist of one byte the sof is an alternating pattern of ones and Zer

**[20:03]** ending with two consecutive one bits indicating that the next bit is the

**[20:10]** leftmost bit in the leftmost bite of the destination address destination address

**[20:19]** da consist of six bytes the da field identifies which station should receive

**[20:27]** the frame the leftmost bit in the da field indicates whether the address is

**[20:34]** an individual address indicated by a zero or a group address indicated by a

**[20:42]** one the second bit from the left indicates whether the da is globally

**[20:48]** administered indicated by a zero or locally administered indicated by a one

**[20:57]** the remaining 4 six bits are a uniquely assigned value that identifies a single

**[21:05]** station a defined group of station or all stations on the

**[21:13]** network Source address sa it consist of six bytes the sa field identifies the

**[21:24]** sending station the sa is always an individual address and the leftmost bit

**[21:32]** in the essay field is always zero length type consist of two bytes this field

**[21:41]** indicates either the number of Mac client databased bytes that are contained in the data field of the frame

**[21:49]** or the frame type ID if the frame is assembled using an optional format if

**[21:58]** the length type field value is less than or equal to 1500 the number of LLC bytes in the data

**[22:08]** field is equal to the length type field value

**[22:15]** data it is a sequence of n bytes of any value where n is less than or equal to

**[22:24]** 1,500 if the length of the data field is less than 46 the data field must be

**[22:30]** extended by adding a filler sufficient to bring the data field length to 46

**[22:38]** bytes frame check sequence FCS consist of 4 bytes this sequence

**[22:48]** contains a 32bit cyclic redundancy check CRC value

**[22:55]** which is created by the sending Mac and is recalculated by the receiving magc to

**[23:02]** check for damaged frames the FCS is

**[23:07]** generated over the da sa length type and data

**[23:14]** fields so this was frame format of 10g ethernet now let us see standards of 10g

**[23:25]** ethernet the 10 GB ethernet standard includes a number of different physical

**[23:32]** layer standards they are broadly divided into three categories first category is Lan fiber

**[23:42]** which supports 10g Bas Sr 10 G Bas LR M

**[23:49]** 10 G Bas LR 10 G base E 10 G base

**[23:56]** lx4 and 10 G G base ZR type of physical standard second category is V fiber

**[24:06]** which supports 10 G Bas s SW 10 G Bas LW

**[24:12]** and 10 G Bas ew type of physical standard third category is len copper

**[24:21]** which supports 10g base CX4 10g base p

**[24:28]** 10g base kx4 and 10g base KX type of

**[24:36]** standard first of all let us see Lan using fiber the most common Optical variety is

**[24:45]** referred to as Lan physical used for connecting directly between routers and

**[24:53]** switches it is basically indicated by alphabet R in ethernet standard although

**[25:01]** 25 minutes, 1 second called Lan this can be used with fiber cable up to 80 kilomet Lan physical uses a line rate of

**[25:12]** 10.3 gbits per second and a 66 bit encoding different standards used for

**[25:20]** fiber Lan are as shown in table 10g Bas Sr R it is short reach

**[25:31]** standard defined in 2002 and designed to support short distances over deployed

**[25:40]** serial multimode fiber cabling with 850nm wavelength it delivers serialized

**[25:49]** data at a line rate of 10.3125

**[25:54]** gbits per second its range is 300 to 400

**[26:01]** 26 minutes, 1 second m it falls under i e 802.3 AE

**[26:08]** standard 10g Bas LR it is a long range Optical technology defined in 2002

**[26:18]** delivering serialized 10 GB ethernet over 1310 NM single mode fiber using

**[26:29]** 64bit by 66 bit physical coding sublayer PCS it delivers serialized data at a

**[26:38]** line rate of 10.3125 gabs per second its range is 10 kilm it

**[26:48]** falls under i e 802.3 AE

**[26:54]** standard 10g base ER it is is an extended range fiber defined in 2002

**[27:04]** which supports distances up to 40 kilom over single mode fiber with 1550 NM

**[27:14]** wavelength and speed of 10.3125 gbits per second recently several

**[27:24]** manufacturers have introduced 80 kilm range ER plugable

**[27:31]** interfaces it falls under i e 802.3 AE standard 10g base

**[27:41]** lx4 it was defined in 2002 using wavelength division multiplexing to

**[27:48]** support ranges of 300 M over deployed multimode cabling and 10 km over single

**[27:58]** mode fiber using wavelength of 1310 NM this is achieved through the use of

**[28:07]** four separate laser sources operating at 3.125 gabs per second on unique

**[28:18]** wavelengths it falls under i e 802.3 AE standard it is now getting

**[28:26]** replaced by 10g Bas lrm now 10g Bas

**[28:34]** lrm it is Long Reach multim mode standard defined in 2006 which support

**[28:42]** distances up to 22m on fddi grade

**[28:48]** 62.5 micromet multi mode cable with 1310 NM wavelength which was originally in

**[28:58]** installed in early 1990s for 100 Mbps networks and it

**[29:05]** offers speed of 10.3125 GBS per second it falls under i e

**[29:15]** 802.3 AQ standard next we shall see van using

**[29:23]** fiber 10g Bas s SW 10g base LW and 10g

**[29:30]** Bas ew are varieties that use the van physical the when physical variants

**[29:38]** correspond at the physical layer to 10g Bas Sr 10gbase LR and 10g Bas ER

**[29:47]** respectively and hence use the same type of fiber and support the same distances

**[29:55]** it falls under i e 802.3 AE standard now moving on to

**[30:04]** Copper Lan 10g base CX4 this standard was designed in 2002

**[30:13]** and is also known by its working group name i e

**[30:19]** 802.3 a k it transmits over four lanes in each Direction Over copper CA using

**[30:29]** infini band 4X twin XL 8 pair it is

**[30:35]** designed to work up to a distance of 15 M only this technology has the lowest

**[30:43]** cost per Port among all 10 GB interconnects at the expense of range

**[30:52]** each lane of the copper carries 3.125 GHz of signaling

**[31:00]** bandwidth 10g base T it is a newly released standard by the i e 802.3

**[31:09]** committee defined in 2006 to provide 10 gabit per second connections over

**[31:18]** conventional unshielded or shielded twisted pair cables of category 6 6A and

**[31:28]** 7 category 6 supports 55 M distance and

**[31:33]** Category 6 a and 7 supports 100 m

**[31:39]** distance this standard is defined as i e 802.3 a

**[31:47]** n 10g base kx4 and 10g Bas

**[31:53]** KR it is a back plane ethernet also known know by its task force name i e

**[32:02]** 802.3 a and is used in Back plane applications

**[32:08]** such as blade servers and modular router or switches with upgradable line cards

**[32:18]** 802.3 AP implementations are required to operate in an environment comprising up

**[32:25]** to 1 M of proper printed circuit board with two connectors the standard defines two Port

**[32:35]** types for 10 gabit per second that is 10g base kx4 and 10 gbas

**[32:46]** KR new back plane designs use 10g base KR which uses single back plane Lane

**[32:55]** rather than 10g Bas KX x 4 which operates over four back plane

**[33:03]** Lanes apart from all the standards explained till now there is one more standard called 10g base

**[33:12]** PR 10g Bas PR that is Pawn originally specified in i e

**[33:21]** 802.3 AV is a 10g ethernet physical for Passive Optical networks and

**[33:29]** uses 157 nanometer lasers in the downstream

**[33:35]** Direction and 1270 nanometer lasers in the Upstream Direction on Downstream

**[33:44]** side it delivers serialized data at a line rate of 10.3125

**[33:52]** gabs per second in a point to multi-point configuration

**[33:58]** 10g Bas PR has three power budgets specified as 10g Bas

**[34:05]** pr1 10 gbas pr20 and 10 gbas

**[34:12]** pr30 so friends this was 10 GB ethernet finally summarizing we learned about

**[34:21]** introduction to 10 GB ethernet which was followed by layer protocol r

**[34:28]** architecture and details of physical and Mac layer of 10g ethernet in the end we

**[34:38]** discussed different standards of 10 gbit ethernet hope the concepts explained in

**[34:47]** this lecture were understandable and helpful see you in the next lecture till

**[34:54]** then goodbye enjoy the day thank you you

**[35:00]** [Music]
