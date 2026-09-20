# IPSec Security Protocol

**Module 14**  
Duration: 26:49  
Video: https://www.youtube.com/watch?v=wVX5KLPh_o8

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Prof Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:19]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:28]** University of Science and technology Hisar harana today in this lecture we will

**[0:35]** study about IP SEC security protocol first of all please see the contents

**[0:42]** which I shall cover after covering brief introduction about IPC Internet Security

**[0:50]** protocols I shall take up its architecture which will be followed by

**[0:56]** IPC protocols ah that is authentication header and ESP that is

**[1:05]** encapsulating security payload in last I shall cover ik that is internet key

**[1:14]** exchange protocol for Key Management IP SEC Internet Protocol

**[1:23]** security is a framework for a set of protocols for security at the network

**[1:30]** or packet processing layer of network communication earlier security

**[1:38]** approaches have inserted security at the application layer of the communication

**[1:45]** model IPC is set to be especially useful for implementing virtual private networks

**[1:54]** and for remote user access through dialup connection to PR private networks

**[2:01]** 2 minutes, 1 second a big advantage of IPC is that security Arrangements can be handled without

**[2:09]** requiring changes to individual user computers IPC is a protocol suit for

**[2:19]** securing Internet Protocol IP communication by authenticating and encrypting each IP

**[2:29]** packet of a communication session IPC can be used in protecting

**[2:37]** data flows between a pair of hosts means host to host between a pair of security

**[2:46]** gateways means Network to network or between a pair of security Gateway and a

**[2:54]** host means Network to host IP SEC is is not a single protocol

**[3:01]** 3 minutes, 1 second but rather a set of services and protocols that provide a complete

**[3:09]** Security solution for an IP network these services and protocols combine to

**[3:17]** provide various types of protection some of the kinds of protection services

**[3:25]** offered by IPC include the following it offers

**[3:32]** confidentiality by encrypting data it provides Integrity by calculating checkm

**[3:40]** or hash value of the data and authentication by using signatures and

**[3:50]** certificates it provides protection against certain types of security

**[3:56]** attacks such as replay attack it also manages sessions along with key

**[4:06]** management now after covering basic introduction of Ip sec let us move to

**[4:13]** its architecture RFC

**[4:16]** [Music]

**[4:18]** 241 defines the basic architecture of Ip

**[4:23]** SEC it covers Concepts in which security Association

**[4:30]** sa a provide the bundle of algorithms and data that provide the parameters

**[4:39]** necessary for operations of two IP protocols ah authentication header and

**[4:49]** ESP encapsulating security payload there are two modes in which

**[4:57]** these protocols work transport mode and tunnel mode in the

**[5:04]** end there is Key Management protocol like internet key exchange that is ik

**[5:14]** ke now let us first move on to modes of protocol in IP secc IPC can be

**[5:23]** implemented in a host to host transport mode as well as in a Network tunneling

**[5:32]** mode in transport mode only the payload of the IP packet is usually encrypted

**[5:40]** and authenticated the routing is intact because the IP header is neither

**[5:48]** modified nor encrypted in tunnel mode the entire IP

**[5:55]** packet is encrypted or authenticated it is then encapsulated into a new IP

**[6:04]** packet with a new IP header other way to explain difference

**[6:11]** between transport mode and tunnel mode is that transport mode can only be used

**[6:19]** between end points of a communication or we can say transport mode is used when

**[6:28]** the cryptographic end points are also the communication end points of the

**[6:36]** secured IP packets figure shows transport mode in

**[6:43]** which communication and cryptographic end points are A and B tunnel mode can

**[6:53]** be used between arbitrary peers when at least one cryptography traic Endo is not

**[7:01]** 7 minutes, 1 second a communication Endo of the secured IP

**[7:07]** packets sa a indicates here security associations lower part of figure shows

**[7:17]** tunnel mode in which communication takes place between either end point a and

**[7:25]** router R A or router r a a to router

**[7:31]** RB or router RB to endpoint B

**[7:39]** accordingly packet structure is shown in which source is router R A and

**[7:46]** destination is router RB tunnel mode is used to create virtual

**[7:54]** packet networks for Network to network communications host to network communications and host

**[8:04]** to host Communications IPC provides two choices of security service authentication

**[8:13]** header ah which essentially allows authentication of the sender of data and

**[8:21]** encapsulating security payload ESP which supports both authentication

**[8:28]** of the sender and encryption of data as well the specific information associated

**[8:37]** with each of these Services is inserted into the packet in a header that follows

**[8:45]** the IP packet header now let us take each one by one authentication header ah

**[8:55]** is a member of the IPC protocol suit ah guarantees connectionless integrity and

**[9:04]** data origin authentication of Ip packets further it can optionally protect

**[9:11]** against replay attacks by using the sliding window technique and discarding

**[9:19]** old packets ah is one of the two core security protocols in IP

**[9:27]** SEC it provides authentication of either all or part of the contents of a

**[9:34]** datagram through the addition of a header that is calculated based on the

**[9:41]** values in the datag gr authentication header ah protocol work in both

**[9:49]** transport and tunneling mode figure shows packet format

**[9:56]** alteration with ah for Trans Port mode in this ah header is added after payload

**[10:05]** that consist of TCP header and data next is figure which shows packet

**[10:13]** format alteration with ah for tunnel mode in this ah header is added after

**[10:22]** original Ip header and data here data

**[10:28]** also contains TCP or UDP header ah uses a simple algorithm which

**[10:38]** uses special hashing algorithm and a specific key known only to the source

**[10:46]** and the destination security Association sa between two devices specifies these

**[10:56]** particulars so that the source and destination know how to perform the

**[11:03]** computation but nobody else can on the source device ah performs the

**[11:13]** computation and puts result Integrity check value or

**[11:20]** icv into a special header with other fields for transmission the destination device does

**[11:29]** the same calculation using the key that the two devices

**[11:36]** share this enables the device to see immediately if any of the fields in the

**[11:43]** original datagram were modified or not now let us move over to the format of

**[11:53]** authentication header please C figure which shows different fields of of authentication

**[12:01]** 12 minutes, 1 second header let us discuss each field one by one first field is next header it is of

**[12:10]** one byte which contains the protocol number of the next header after the

**[12:18]** a it is used to link headers together next field is payload length this field

**[12:27]** is of 1 byte and it measures the length of the authentication header itself

**[12:34]** including the payload the length of this authentication header is measured in two

**[12:43]** octet units minus 2 for example an ah

**[12:49]** value of 4 equal 3 + 3 - 2 here first

**[12:56]** three indicates first three rows of 32 bit each and next three indicates three

**[13:05]** rows for 32bit icv field and thus an ah

**[13:12]** value of 4 means 24 octets Third Field is reserve which is

**[13:20]** of 16 bits and is not used till now so it is set to zero next field is

**[13:29]** security parameter index SPI which is of 32 bits and it is

**[13:37]** arbitrary value which is used together with the destination IP address to

**[13:45]** identify the security Association of the receiving

**[13:51]** party security parameter index SPI is followed by sequence number field

**[13:58]** which which is of 32 bits the field is incremented by one for

**[14:05]** every packet sent to prevent replay attacks when replay detection is enabled

**[14:14]** sequence numbers are never reused because a new security Association must

**[14:21]** be renegotiated before an attempt to increment the sequence number Beyond its

**[14:30]** maximum value last field is integrity check value

**[14:38]** icv which is multiple of 32 bits this field may contain padding to align the

**[14:47]** field to an 8 octet boundary for IPv6 or

**[14:53]** a four octet boundary for ipv4

**[14:59]** the IPC authentication header ah provides Integrity authentication

**[15:06]** services to IP SEC capable devices so that they can verify that messages are

**[15:15]** received intact from other devices for many applications however

**[15:23]** this is only one piece of the puzzle we want to not only protect

**[15:29]** against intermediate devices changing the datagram but also to protect against

**[15:37]** them examining their contents as well for this level of private communication

**[15:46]** ah is not enough we need to use the ESP protocol because ah just provides

**[15:56]** authentication but not privacy privacy is provided by

**[16:04]** es now let us see next protocol in IPC that is

**[16:11]** encapsulating security payload that is es encapsulating security payload ESP is

**[16:21]** a member of the IPC protocol suit IPC provides origin

**[16:29]** authenticity Integrity confidentiality and protection of

**[16:36]** packets ESP operates directly on top of Ip the main job of ESP is to provide the

**[16:46]** Privacy we seek for IP datagram by encrypting them an encryption algorithm

**[16:55]** combines the data in the datagram with a key to transform it into an encrypted

**[17:03]** form ESP can also be implemented in both transport and tunneling

**[17:12]** mode figure shows packet format alteration with ESP for transport mode

**[17:21]** in this ESP header is added after payload that consist of TCP header and

**[17:28]** and data ESP trailer and ESP authentication fields are added before

**[17:36]** TCP header and data however in tunneling mode where the

**[17:43]** entire original Ip packet is encapsulated with a new packet header

**[17:51]** added ESP protection is afforded to the whole inner IP packet while the outer

**[18:00]** header remains unprotected as in transport mode ESP

**[18:06]** trailers and ESP authentication are added before

**[18:13]** data now let us move over to the format of encapsulating security payload ESP

**[18:22]** please see the figure which shows different fields of

**[18:27]** ESP let us discuss each field One By One ESP has several fields that are same

**[18:37]** as those used in ah but it packages its field in a very different way instead of

**[18:47]** having just a header it divides its Fields into three

**[18:54]** components first is ESP header this contains two Fields SPI and sequence

**[19:03]** number and they come before the encrypted data its placement depend on

**[19:11]** whether ESP is used in transport mode or tunnel mode as explained earlier in my

**[19:20]** lecture next is ESP trailer this section is placed after the encrypted data it

**[19:28]** contains padding that is used to align the encrypted data through a padding and

**[19:36]** Pad length field interestingly it also contains the next header field for

**[19:45]** ESP ESP authentication data this field contains an

**[19:52]** icv that is computed in such a manner that is similar to

**[19:59]** how the ah protocol works the field is used when esp's optional authentication

**[20:06]** feature is employed now let us see each of these

**[20:12]** field one by one first field is security parameter index which is of 32 bits it

**[20:22]** stores an arbitrary value used together with a destination I I address to

**[20:30]** identify the security Association of the receiving party next field is sequence number

**[20:39]** which is also of 32 bits it is monotonically increasing sequence number

**[20:47]** which increments by one for every packet sent to protect against replay

**[20:55]** attacks there is a separate counter kept for every security

**[21:02]** Association Next we move on to payload data field which is variable after

**[21:09]** payload data it is padding which is of 0 to 255 octets it is used as padding for

**[21:19]** encryption to extend the payload data to a size that fits the encryption Cipher

**[21:26]** block size and to align the next field next field is pad length field which is

**[21:35]** of 8 Bits And it specifies size of padding in

**[21:41]** octets moving on to next header field which is of 8 Bits And contains next

**[21:48]** Header information now there are two reasons why these fields are broken into pieces

**[21:57]** like this the first is that some encryption algorithms require the data to be

**[22:05]** encrypted to have a certain block size and so padding must appear after the

**[22:12]** data and not before it that's why padding appears in the ESP trailer field

**[22:21]** the second is that the ESP authentication data appears separately

**[22:27]** because it is used to authenticate the rest of the encrypted datagram after

**[22:35]** encryption this means that it cannot appear in the ESP header or ESP trailer

**[22:43]** next we shall discuss Key Management protocol in IP SEC which is internet key

**[22:51]** exchange I ke like many secure networking protocol sets it is based on the concept of a

**[23:01]** 23 minutes, 1 second shared secret two devices that want to send information securely and code and

**[23:09]** decode it using a piece of information that only the devices know anyone who

**[23:18]** isn't on the secret is able to intercept the information but is prevented either

**[23:27]** from reading it or from tempering the primary support protocol used for this

**[23:34]** purpose in IPC is known as Internet key exchange that is ik

**[23:44]** ke ik is defined in RFC 249 and it is more complicated of the

**[23:53]** IPC protocols to comprehend in fact it is simply impossible to truly understand more than

**[24:03]** a real simplification of its operation without significant background in

**[24:11]** cryptography the purpose of ik e is to allow devices to exchange

**[24:18]** information that is required for secure communication as the title suggest this

**[24:27]** includes cryptographic keys that are used for encoding authentication information and

**[24:36]** Performing payload encryption ik works by allowing IPC capable devices to

**[24:45]** exchange SAS main feature of ik are as shown in

**[24:54]** figure ik is an IPC component used for performing Mutual authentication and

**[25:03]** establishing and maintaining security associations it is typically used for

**[25:10]** establishing ipx sessions it has a key exchange mechanism for security at

**[25:18]** Network layer it has five variations of an ik negotiation with two

**[25:27]** modes aggressive and Main it also has three authentication

**[25:35]** methods pre-shared public key encryption and public key

**[25:43]** signature so dear friends today in this lecture we have covered introductory

**[25:49]** concepts of IPC protocol followed by its architecture then we covered IP Che

**[25:58]** protocols ah that is authentication header and ESP that is

**[26:05]** encapsulating security payload in the last ik that is internet key exchange

**[26:13]** protocol for Key Management was covered thank you

**[26:31]** [Music]

**[26:42]** [Music]
