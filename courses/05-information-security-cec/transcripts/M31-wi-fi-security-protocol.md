# Wi-Fi Security Protocol

**Module 31**  
Duration: 25:36  
Video: https://www.youtube.com/watch?v=Ml3_13Hn9-I

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Prof Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:03]** [Music]

**[0:24]** [Music]

**[0:31]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:40]** University of Science and Technology Hisar harana today in this lecture we

**[0:46]** will study about Wi-Fi technology first of all please see the

**[0:53]** contents which I shall cover after covering brief introduction about Wi-Fi

**[1:00]** technology I shall take up its layered protocol architecture which will be

**[1:06]** followed by Wi-Fi standards in last I shall cover WiFi frame

**[1:14]** format a wireless local area network W Lan is a data Communication System

**[1:22]** implemented as an extension or as an alternative to a wired LAN WiFi is a

**[1:31]** technology of Wireless local area network based on the i e

**[1:38]** 82.1 series of Wireless standards issued by the Institute of electrical and

**[1:45]** electronic Engineers i e an international Professional Organization

**[1:53]** for electrical and electronic Engineers the i e does not test equipment for

**[2:01]** 2 minutes, 1 second compliance with their standards the nonprofit Wi-Fi Alliance was formed in

**[2:09]** 1999 to establish and enforce standards for interoperability and backward

**[2:18]** compatibility and to promote Wireless local area Network Technology the Wi-Fi Alliance enforces

**[2:27]** the use of the Wi-Fi brand to Technologies based on the i e

**[2:35]** 802.11 standard manufacturers with membership in the Wi-Fi Alliance whose

**[2:43]** products are manufactured as per I E 802.11 standard gain the right to mark

**[2:52]** their products with the Wii logo specifically the certification

**[2:59]** process requires compliance to the i e 802.11 radio standards the

**[3:08]** WPA and WPA2 security standards and the

**[3:14]** EAP authentication standards any manufacturer who manufactures product as

**[3:22]** per the standard can put a Wi-Fi logo on their product

**[3:30]** there are several Technologies to choose from while selecting a wireless LAN

**[3:37]** solution each with advantages and limitations most Wireless lens use

**[3:45]** spread Spectrum a whiteband radio frequency technique in which the signal

**[3:51]** is spread out over the available bandwidth there are two types of spread

**[3:58]** Spectrum first is frequency hoping and second direct sequence frequency hoping spread

**[4:07]** Spectrum FHS uses a narrow band carrier that

**[4:14]** changes frequency in a pattern known only to the transmitter and receiver on

**[4:21]** the other hand direct sequence spread Spectrum DS generates a red redundant bit pattern

**[4:31]** for each bit to be transmitted and requires more bandwidth for

**[4:40]** implementation this bit pattern called a chip or chipping code is used by the

**[4:47]** receiver to recover the original signal even if one or more bits in the

**[4:55]** chip are damaged during transmission statistical technique embedded in the radio can recover the

**[5:03]** original data without the need for retransmission now let us move on to the

**[5:12]** layered protocol architecture of i e 802.11 the i e

**[5:21]** 802.11 standard only covers the physical layer and medium excess layer of OSI

**[5:30]** reference model as shown in figure the physical layer is subdivided into

**[5:37]** physical layer convergence protocol plcp and the physical medium dependent

**[5:47]** sublayer PMD the plcp sublayer provides a carrier

**[5:55]** sense signal called Clear Channel assessment CCA and provides a common physical

**[6:04]** service access point sap independent of the transmission

**[6:11]** technology the second sublayer PMD handles modulations and encoding or

**[6:20]** decoding of signals the Mac management support medium Access Control

**[6:28]** Association and re Association of a station to an access point and roaming

**[6:35]** between different access points it also controls authentication mechanism

**[6:42]** encryption synchronization of a station with regard to an access point and power

**[6:50]** management to save battery power further

**[6:56]** 802.11 uses frequency hoping spread Spectrum

**[7:03]** fhws direct sequence spread Spectrum DS orthogonal frequency Division

**[7:12]** multiplexing ofdm and high rate direct sequence

**[7:19]** spread Spectrum HR DS modulation techniques at physical layer frequency

**[7:28]** hoping spread Spectrum FHS uses 79 channels of 1 mahz each and

**[7:37]** a pseudo random number generator is used to produce the sequence of frequencies

**[7:44]** hoped two this method provides a fair way to allocate Spectrum in the

**[7:52]** unregulated ism band direct sequence spread Spectrum d technique support

**[8:01]** 8 minutes, 1 second communication speed of 1 or 2 Mbps it basically uses a technique

**[8:09]** similar to code division multiple access CDMA next modulation technique used in

**[8:17]** physical layer is orthogonal frequency division multiplexing o fdm which

**[8:25]** delivers 54 Mbps and above speed in The

**[8:30]** Wider 5 GHz ISM band next technique is

**[8:36]** hrd s that is high rate Theta sequence spread Spectrum which offers speed of 11

**[8:47]** and 22 Mbps in 2.4 GHz

**[8:54]** bandwidth in Mac layer i e 802.11 uses two modes of operations the first

**[9:03]** called distributed coordination function DCF and second Point coordination

**[9:10]** function PCF DCF does not use any kind of central control it uses a protocol

**[9:19]** called carrier sense multiple SS with collision avoidance CSM by CA in this

**[9:28]** method both physical Channel sensing and virtual Channel sensing is done in

**[9:37]** physical Channel sensing when a station wants to transmit it senses the channel

**[9:43]** if it is Idle it just starts transmitting it does not sense the channel while transmitting but transmits

**[9:53]** full frame which may get destroyed at the receiver due to

**[10:00]** interference if a collision occurs the colliding station waits for a random

**[10:06]** amount of time using the ethernet binary exponential backof algorithm and then

**[10:14]** try again later in Virtual Channel sensing scheme medium access with collision avoidance

**[10:23]** maaca is used in point coordination scheme PCF base station is used to

**[10:31]** control all activity in its cell now let us see different Wireless lens standard

**[10:39]** for i e 802.11 i e 802.11 is a set of medium access control

**[10:49]** and physical layer specification for implementing Wireless local area network

**[10:57]** in 2.5 4 and 5 GHz frequency

**[11:04]** band they are created and maintained by the i e l standard committee i e

**[11:15]** 802.11 the base version of the standard was released in

**[11:21]** 1997 and had many subsequent amendments the standard and amendments

**[11:29]** provide the basis for wireless network products using the wifi brand there are

**[11:37]** several Wireless lens standards each suited for a particular environment as shown in

**[11:46]** figure first standard of I E 802.11 Series is

**[11:53]** 802.11 itself which was released in 1997

**[12:00]** it offers 1 to 2 MVPs speed with an indoor range of 20 M and an outdoor

**[12:08]** range of 100 m it uses

**[12:13]** fhws and DS as spread Spectrum technique

**[12:20]** it operates on 2.4 GHz ISM band next standard is 82.

**[12:29]** 11a which was released in 1999 it offers 54 and8 MVPs speed with

**[12:39]** an indoor range of 35 M and outdoor range of 120 M it uses ofdm as

**[12:48]** modulation technique it operates on 5 GHz ISM band

**[12:56]** since the 2.4 GHz band is heavily used so using the relatively unused 5 GHz

**[13:04]** band gives 802.11a significant advantage in theory

**[13:13]** 802.11a signals are absorbed more readily by walls and other solid objects

**[13:22]** in their path due to their smaller wavelength and as a result they cannot p

**[13:29]** penetrate now moving on to i e 802.11b this standard was released in

**[13:39]** 1999 it offers 11 and 22 MVPs speed with

**[13:45]** an indoor range of 35 M and outdoor range of 120 M it uses HR

**[13:55]** DS as spread Spectrum technique it it operates on

**[14:01]** 14 minutes, 1 second 2.4 GHz ISM band next is i e

**[14:08]** 802.11 g standard this standard was released in 2003 it offers 54 Mbps speed

**[14:18]** with an indoor range of 38 M and outdoor range of 140 M it uses ofdm and DM as

**[14:30]** spread Spectrum technique it operates on 2.4 GHz ISM band i e

**[14:40]** 802.11n released in 2009 is an amendment that improves upon the previous

**[14:48]** 802.11 standards by adding multiple input multiple output mimo antenas

**[14:57]** 802.11 and offer speed of 54 Mbps to 600 Mbps using ofdm

**[15:07]** spread Spectrum technique it operates on both the 2.4 GHz and the Lesser used 5

**[15:16]** GHz band support for 5 GHz band is optional this standard offers indoor

**[15:25]** range of 70 M and outdoor range of 2 250 m i e

**[15:32]** 802.11 AC released in 2013 is built on

**[15:40]** 802.11n it offers speed in the range of 1300 Mbps and operates on 5 GHz ISM

**[15:52]** band other i e 802.11 standards i e 802.11

**[15:59]** D addresses the spread of technology to countries not addressed by i e i e

**[16:10]** 802.11e focuses on the quality of service associated with wireless

**[16:16]** transmission of multimedia applications i e

**[16:23]** 802.11 f addresses roaming between APS and interoperability between different

**[16:32]** vendor groups i e 802.11h focuses on frequency selection

**[16:41]** and power concerns on the 5 gahz band in European

**[16:48]** countries i e 802.11i focuses on enhancing W lens

**[16:56]** security and Authentication for

**[17:00]** 802.11 that include radius karos and i e

**[17:07]** 802.1 x i e 802.11 j focuses on the Japanese

**[17:16]** equivalent of 802.11 h i e

**[17:22]** 802.11 a d is an amendment that defines a new physical layer for

**[17:30]** 802.11 Network to operate in the 60 GHz Spectrum products implementing the

**[17:40]** 802.11 ad standard are being brought to Market under the Y gig brand

**[17:49]** name the certification program is now being developed by the wifi Alliance

**[17:56]** instead of Y gig Alliance the peak transmission rate of

**[18:03]** 802.11 ad is 7 GBS per second i e

**[18:11]** 802.11 AF also referred to as whitei or super WiFi is an amendment

**[18:21]** approved in February 2014 that allows W Lan operation in TV

**[18:28]** white space Spectrum in the VHF and UHF

**[18:33]** bands between 54 and 790

**[18:40]** mahz it uses cognitive radio technology to transmit on unused TV channels

**[18:49]** Wireless lens use electromagnetic waves to communicate information from one

**[18:56]** point to another without relying on a wired connection radio waves are often

**[19:04]** referred to as radio carriers because they simply perform the function of

**[19:10]** delivering energy to a remote receiver the data being transmitted are

**[19:18]** superimposed on the radio carrier so that they can be extracted accurately at

**[19:25]** the receiving end this process is generally referred to as carrier

**[19:33]** modulation i e 802.11b and

**[19:39]** 802.11g standard utilizes the 2.4 GHz Spectrum however

**[19:47]** 802.11a used the more heavily regulated 5 GHz band i e

**[19:56]** 802.11n utilizes both 2.4 GHz and 5 GHz

**[20:03]** band these bands are commonly referred to as 2.4 GHz and 5 GHz band in most of

**[20:14]** the literature each spectrum is subdivided into Channels with a center frequency

**[20:22]** and bandwidth analog to the way radio and TV broadcast bands are

**[20:30]** subdivided the 2.4 GHz band is divided into 14 channels spaced 5 mahz apart

**[20:39]** beginning with Channel 1 which is centered on

**[20:45]** 2412 GHz the L channels have additional restrictions or are unavailable for use

**[20:54]** in some regulatory domains figure shows exact frequencies

**[21:00]** of 14 different channels used in 2.4 GHz ISM

**[21:09]** band now we will move on to the frame format of I E

**[21:15]** 802.11 standard frame format of this Wireless lens standard is as shown in

**[21:23]** figure there are nine fields in frame format of this standard starting from

**[21:31]** frame control to checkum frame control field has 11

**[21:37]** subfields now let us see each field one by one frame control field which is of

**[21:45]** two bytes is used for control purpose details of subfield of frame

**[21:51]** control field will be discussed after discussing main fields

**[21:59]** second field is duration which tells how long the frame and its acknowledgement

**[22:06]** will occupy the channel the frame header contains four

**[22:13]** addresses the source and the destination are obviously needed and the other two

**[22:19]** are used for the source and destination base stations for intercell traffic

**[22:30]** the sequence field allows fragments to be numbered of the 16 bits available 12

**[22:38]** identify the frame and four identify the fragment the data field contains the

**[22:46]** payload up to 2312 bytes followed by the usual check sum of 4

**[22:54]** bytes now let us see details of frame control field which has 11

**[23:02]** subfields the first of these is protocol version which allows two versions of the

**[23:09]** protocols to operate at the same time in the same cell then comes the type field which

**[23:17]** indicates data control or management type of frame and next field indicates

**[23:26]** subtype the two DS and from DS bits indicates that the frame is going to or

**[23:35]** coming from the inter cell distribution system for example ethernet

**[23:42]** system the MF bit means that more fragments will follow the retry bit marks a retr

**[23:52]** transmission of a frame sent earlier the power management

**[23:59]** pwr bit is used by the base station to put the receiver into sleep state or

**[24:08]** take it out of sleep State the more bit indicates that the

**[24:15]** sender has additional frames for the receiver the wbit specifies that the

**[24:24]** frame body has been encrypted using the web wired equivalent privacy algorithm

**[24:33]** and finally the obit tells the receiver that a sequence of frame with this bit

**[24:41]** on must be processed strictly in order so dear friends today in this

**[24:50]** lecture we have covered introductory concepts of Wi-Fi technology followed by

**[24:56]** its layered protocol architecture and i e

**[25:03]** 802.11 standards in last we have seen frame format of i e

**[25:11]** 802.11 technology so this was all about WiFi technology thank you

**[25:21]** [Music]
