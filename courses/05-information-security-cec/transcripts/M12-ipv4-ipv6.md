# IPV4 & IPV6

**Module 12**  
Duration: 32:07  
Video: https://www.youtube.com/watch?v=HXbCUPDXLG8

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Prof Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:04]** [Music]

**[0:11]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:18]** University of Science and Technology Hisar harana I welcome you all to the

**[0:24]** lecture series of cyber and information security in this lecture we will study

**[0:31]** about ipv4 and IPv6 protocols used at Network layer level first of all please

**[0:41]** see the contents which I shall cover after covering brief introduction about Internet Protocol version 4 I

**[0:49]** shall take up header of ipv4 which will be followed by addressing in

**[0:56]** ipv4 in last I shall take up internet protocol version 6 that is ipv 6 so now

**[1:05]** let us start Internet Protocol version 4 that is ipv4 is the fourth version in the

**[1:14]** development of the Internet Protocol it is one of the core Protocols of Internet

**[1:22]** it still Roots most internet traffic today despite the ongoing development of

**[1:29]** the successor protocol IPv6 ipv4 is described in ietf

**[1:38]** publication RFC 791 in September 1981 replacing an earlier definition RFC

**[1:48]** 760 in January 1980 ipv4 is a connectionless protocol

**[1:56]** for use on packet switch networks with 30 2bit address now first of all let us

**[2:04]** see header of ipv 4 and ipv4 datagram consist of a header part and a text part

**[2:13]** the header has a 20 by fixed part and a variable length optional part the header

**[2:20]** format is shown in figure there are minimum five rows of 32

**[2:27]** bit each additional rows are optional now we shall see fields of ipv4

**[2:34]** header one by one version the version field are first four

**[2:42]** bits in first row of Ip header for IP V4 this has a value of four other versions

**[2:51]** are ipv5 which was an experimental realtime stream protocol that was never widely

**[3:00]** used and IPv6 which is expected to be deployed in near

**[3:08]** future internet header length IHL this field of 4 bits is the internet

**[3:16]** header length IHL which indicates number of 32bit rows in the header the minimum

**[3:25]** value is five which applies when no options are present the maximum value of

**[3:33]** this 4bit field is 15 which limits the header to 60 bytes and thus the option

**[3:40]** field to 40 bytes differentiated Services code point

**[3:49]** dscp this field of six bits is now defined for differentiated

**[3:55]** Services new technologies are emerging that require realtime data streaming and therefore

**[4:03]** make use of the dscp field an example is voice over IP which

**[4:10]** is used for interactive data voice exchange originally this six-bit field

**[4:17]** was defined as type of service which contained a 3-bit precedence field and

**[4:24]** three flags delay d throughput t and reliability

**[4:32]** R explicit congestion notification ecn this field of two bits is now

**[4:40]** defined which allows end to end notification of network congestion without dropping

**[4:48]** packets earlier these two bits were not defined total length the total length of

**[4:57]** 16 bits includes length of both header and data the maximum length is

**[5:06]** 65,535 bytes identification this field is an identification field and is primarily

**[5:15]** used for uniquely identifying the group of fragments of a single IP

**[5:22]** datagram the identification field is needed to allow the destination host to

**[5:28]** determine which datagram a newly arrived fragment belongs to all the fragments of a datagram

**[5:38]** contain the same identification value flag there are three bits in this

**[5:45]** field out of which one is unused bit and two are one bit Fields DF and MF DF

**[5:55]** stands for don't fragment and MF for more fragment DF is an order to the routers not to

**[6:03]** fragment the datagram because the destination is incapable of putting the

**[6:09]** pieces back together again MF stands for more fragments all fragments except the last

**[6:19]** one have this bit set it is needed to know when all

**[6:25]** fragments of a datagram have arrived fragment offset this field of 13bit

**[6:34]** tells where in the current datagram this fragment belongs all fragments except

**[6:41]** the last one in a datagram must be a multiple of8 bytes the elementary

**[6:48]** fragment unit since 13 bits are provided there is a maximum of

**[6:55]** 8192 fragments per datagram giving a maximum datagram length of

**[7:04]** 65,536 bytes one more than the total length field time to live this field of 8 Bits

**[7:15]** is a counter used to limit packet lifetime it is supposed to count time in

**[7:22]** seconds allowing a maximum lifetime of 255 seconds protocol

**[7:30]** this field of 8 Bits Define the protocol used in the data portion of the IP

**[7:37]** datagram header check sum this field of 16bit verifies the header only such a

**[7:44]** check sum is useful for detecting errors generated by bad memory words inside a

**[7:52]** router Source address this field of 32bits is the IP V4 address

**[8:00]** of the sender of the packet this address may change in

**[8:05]** transit by a network address translation device destination address this field of

**[8:14]** 32bit is the ipv4 address of the receiver of the packet as with the

**[8:21]** source address this may change in the transit by a network address translation

**[8:28]** device next field is options field it was designed to provide an escape to allow subsequent versions of the

**[8:36]** protocol to include information not present in the original design to permit

**[8:45]** experimenters to try out new ideas and to avoid allocating header bits to

**[8:52]** information that is rarely needed originally five options were

**[8:58]** defined as listed in figure but since then some new ones have been

**[9:06]** added as shown in figure the security option tells how secret the datagram

**[9:14]** is the strict Source routing option gives the complete path from source to

**[9:20]** destination as a sequence of IP addresses the lose Source routing option

**[9:28]** gives a list of rou RS not to be missed on the way the record route option tells the

**[9:36]** router along the path to append their IP address to the option

**[9:42]** Fields finally the time stamp option is like the record route option except that

**[9:50]** in addition to recording its 32bit IP address each router also records a 32bit

**[9:58]** time stamp second part of Ip header is data portion the data portion of the packet is not

**[10:07]** included in the packet check sum its contents are interpreted based on the value of the protocol header

**[10:16]** field some of the common protocols for the data portion are listed in the table

**[10:23]** here protocol value one indicates icmp two indicates I igmp six indicates

**[10:32]** TCP 17 indicates UDP 41 indicates en

**[10:39]** NCAP 89 indicates OSF and 132 indicates

**[10:47]** sctp so this was ipv4 header now let us see ipv4 addressing

**[10:56]** schemes Network addresses in IP P V4 which are 32bit numbers are usually

**[11:03]** written in dotted decimal notation in this format 32bit IP address is divided

**[11:11]** into four parts of one byte each each of the four bytes is written in decimal

**[11:19]** notation from 0 to 255 for example the

**[11:27]** 32bit 1 0 1 0 1 1 0 0 0 0 0 1 0 0 0 0 1

**[11:39]** 1 1 1 1 1 1 0 0 0 0

**[11:47]** 001 address is written as 172 16.

**[11:57]** 2541 the low lowest IP in this addressing scheme is

**[12:06]** 0.0.0.0 and the highest IP is

**[12:12]** 255.255 do 255.255 for several decades IP addresses

**[12:21]** were divided into five categories as shown in figure this allocation is class full

**[12:31]** addressing it is no longer used but references to it in the literature are still common we will discuss the

**[12:40]** replacement of class full addressing shortly first let us see classful

**[12:48]** addressing in classful addressing there are five types of classes the class A

**[12:55]** starts with zero bit Class B starts with 1 Class C starts with 1 1 0 class D

**[13:04]** starts with 1 1 1 and Class E starts with 1 1 one

**[13:13]** 1 there are eight bits for Network address and 24 bits for host address in

**[13:20]** class A and total address ranges from 1.

**[13:27]** 0.0.0 to to 127

**[13:34]** 255.255 255 in class A There are 16 bits for Network

**[13:43]** addresses and 16 bits for host addresses in class B and address ranges from

**[13:53]** 128.0 do0 do0 to 191 .

**[14:00]** 255 255.255 in class

**[14:07]** B there are 24 bits for networks and eight bits for host address in class C

**[14:15]** and total address ranges from 1920.

**[14:22]** 0.02 223 255.255 255 in class

**[14:32]** C Class D addresses which starts with 1110 are used for

**[14:41]** multicasting Class E addresses which starts with one one one one are reserved

**[14:49]** for future use now let us see what is Network

**[14:55]** address and subnet mask net Network address is first IP address of any

**[15:02]** network or subnet here IP address is 1921 128.

**[15:11]** 64.

**[15:14]** 100/24 where sl24 indicates that there are 24 bits in network address and rest

**[15:23]** eight bits are for host so subnet mask contains 241s and

**[15:31]** 80 with subnet mask as 255.255.255.0 Network address is

**[15:42]** obtained by performing and operation of IP address of host with subnet mask as

**[15:50]** shown in figure finally Network address obtained is 19218 .

**[16:03]** 64.0 classful addressing prescribed only three possible subnet mask for class A

**[16:10]** it is 255.0.0.0 or

**[16:19]** sl8 for class B it is 255.255.0.0 or/

**[16:30]** 16 and for Class C it is

**[16:38]** 255.255.255.0 or sl24 this was class full addressing now

**[16:46]** let us see class L inter domain routing cidr the basic idea behind cidr which is

**[16:56]** described in RFC 1519 is to allocate the remaining IP

**[17:02]** addresses in a variable sized blocks without regard to the

**[17:08]** classes if a site needs say 2,000 addresses it is given a block of 2048

**[17:16]** addresses on a 2048 byte boundary to make the forwarding algorithm easier to

**[17:24]** understand let us consider an example in which millions of addresses are available starting at 194.

**[17:36]** 24.

**[17:39]** 0.0 suppose that Cambridge University needs 2048 addresses and is assigned the

**[17:47]** addresses 194. 24.0 do0 through 194.

**[17:57]** 24.7 255 along with subnet mask

**[18:03]** 255.255 do2 48.0 next Oxford University asked for

**[18:12]** 4096 addresses since a block of 4096

**[18:17]** addresses must lie on a 4096 byte boundary they cannot be given addresses

**[18:25]** starting at 19424 4.8.0 instead they get

**[18:35]** 19424 16.0 through 194.

**[18:42]** 24.31 255 along with subnet mask 255.255 do2

**[18:53]** 40.0 now the University of Edinburg asked for 10 24 addresses and his

**[19:01]** 19 minutes, 1 second assigned addresses 194.

**[19:06]** 24.80 through 194.

**[19:11]** 24.11 255 along with subnet mask 255.255

**[19:22]** 2520 these assignments are summarized in figure after after cidr let us see net

**[19:31]** which is Network address translation the basic idea behind net is to assign each

**[19:38]** company a single IP address for internet traffic within the company every

**[19:46]** computer gets a unique IP address which is used for routing internal traffic

**[19:53]** however when a packet exit the company and goes to the ISP and address translation takes place to make this

**[20:03]** scheme possible three ranges of IP addresses have been declared as private

**[20:10]** companies may use them internally as they wish the Only Rule is that no

**[20:17]** packet containing these addresses may appear on the internet

**[20:24]** itself these private addresses are also not used for any websites the following are the three

**[20:33]** ranges reserved for private networks as defined in RFC

**[20:41]** 19918 for class A it is 10.0.0.0 to

**[20:49]** 10255 255.255 with 1 67 lakh 7

**[21:01]** 21 minutes, 1 second 7,216 host in each Network for class B it is

**[21:11]** 172.16.0.0 to 17231

**[21:20]** 255.255 with 1048576 host in each

**[21:27]** Network for Class C this range is

**[21:35]** 192.168.0.0 2 192.168.255.255

**[21:43]** with 65,536 host in each

**[21:50]** Network the operation of net is shown in figure within the company premises each

**[21:57]** machine has has a unique address of the form 10. x.y

**[22:04]** doz however when a packet leaves the company premises it passes through a net

**[22:10]** box that converts the internal IP Source address 10.0.0 do1 in the figure to the

**[22:20]** company's true IP global address 198

**[22:27]** 6042 about 12 in given example the netbox is often combined in

**[22:35]** a single device with a firewall which provides security by careful

**[22:43]** control so this was ipv4 now let us move on to ipv 6

**[22:50]** Internet Protocol version 6 IPv6 was developed by the internet

**[22:57]** engineering task force ietf to deal with the long anticipated

**[23:04]** problem of ipv4 address exhaustion IPv6 is intended to replace

**[23:14]** ipv4 IPv6 addresses are 128 bits which are represented as eight groups of four

**[23:22]** hexadecimal digits with the groups being separated by columns as shown in figure

**[23:30]** the main feature of IPv6 are discussed below first and foremost IPv6 has longer

**[23:38]** addresses than ipv4 which is 128 as compared to

**[23:45]** 32 the second major Improvement of IPv6 is the simplification of the header it

**[23:53]** contains only Seven Fields as compared to 13 in IP PV

**[24:00]** 4 the third major Improvement was better support for options the fourth area in which IPv6

**[24:10]** represents a big Advance is in security finally more attention has been

**[24:17]** paid to quality of service the IPv6 header is shown in

**[24:26]** figure an IPv6 p has two parts a header and payload the fixed header occupies the

**[24:34]** first 40 bytes of the IPv6 packet the version field of 4 bits is

**[24:42]** always six for IPv6 as it was 4 in case of

**[24:49]** ipv4 the traffic class field of eight bits is used to distinguish between packets with different real time

**[24:58]** delivery requirements the flow label field of 20 bits is used to allow a source and

**[25:08]** destination to set up a pseudo connection with particular properties and requirements with regard to flow

**[25:17]** control the payload length of 16 bits field tells how many bytes follow the 40

**[25:25]** byte header the name was changed CH from ipv4 total length field because the

**[25:33]** meaning was also changed slightly the 40 header bytes are no longer counted as

**[25:40]** part of the length this next header field of 8 Bits

**[25:47]** tells the receiver how to interpret the data which follows the header this field tells which of the six

**[25:56]** extension header if any follow this one if this header is the last IP header

**[26:05]** the next header field tells which transport protocol handles to pass the packet

**[26:13]** to the Hope limit field of 8 Bits is used to keep packets from living

**[26:20]** forever it is in practice the same as the time to live field in ipv 4 namely

**[26:28]** if field that is decremented on each hope in theory in ipv4 it was time in

**[26:35]** seconds but no router used it that way so the name was changed to reflect the

**[26:42]** way it is actually used next Comes The Source address and destination address fields which are of

**[26:51]** 16 bytes each and contain source and destination address a new notation has

**[26:59]** been devised for writing 16 byte addresses they are written as eight

**[27:05]** groups of four hexadecimal digits with columns between the groups as shown in

**[27:13]** Figure 8 0000 0 colon

**[27:18]** 0000 0 colon 0 0000 0 colon

**[27:25]** 000000 0 colon 0123 colon

**[27:33]** 4567 colon 89 a b column CDE e

**[27:41]** f since many addresses will have many zeros inside them optimizations have been

**[27:50]** authorized first leading zeros within a group can be omitted say 0 1 2 3 can be

**[27:58]** written as 1 2 3 second one or more group of 160 bits

**[28:07]** can be replaced by a pair of columns thus the above addresses now

**[28:15]** become 8 00 colon colon 1 2 3 colon

**[28:24]** 4567 colon 89 a B colon CDE e f now let

**[28:34]** us see extension headers in IPv6 some of the missing ipv4 fields are

**[28:43]** occasionally still needed so ipv4 has introduced the concept of an optional

**[28:50]** extension header these headers can be supplied to provide extra

**[28:58]** information but encoded in an efficient way six kinds of extension headers are

**[29:05]** defined at present as listed in figure The Hope by hope header is used

**[29:13]** for Mis laneous information for routers destination options provides

**[29:20]** additional information for the destination a router field provides lose

**[29:28]** list of routers to visit fragmentation is for management of datagram

**[29:37]** fragments authentication deals with verification of the sender's

**[29:43]** identity encrypted security payload provides information about the encrypted

**[29:52]** contents now after options let us see comparison of fields in

**[29:58]** ipv4 and IPv6 header the IHL field is gone in IPv6

**[30:07]** because the IPv6 header has a fixed length header the protocol field was taken out

**[30:16]** in IPv6 because the next header field tells what follows the last IP

**[30:25]** header all the fields related to fragmentation were removed because IPv6

**[30:32]** takes a different approach to fragmentation for time to live in ipv4

**[30:41]** there is a hope limit in ipv six finally the checkum field is gone

**[30:48]** because calculating it greatly reduces performance so friends this was ipv4 and

**[30:58]** ipv 6 finally summarizing we learned about introduction to Internet Protocol

**[31:06]** which was followed by header of ipv4 and details of addressing in

**[31:13]** ipv4 in the end we discussed IPv6 header hope the concepts explained in

**[31:21]** this lecture were understandable and helpful hope to see you again in next

**[31:28]** lecture till then goodbye enjoy the day thank you

**[31:34]** [Music]
