# Stream Control Transmission Protocol (SCTP)

**Module 28**  
Duration: 26:43  
Video: https://www.youtube.com/watch?v=a277VGgcYi0

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Sunil Kumar, Department of Electrical and Computer Engineering, Punjab Agriculture University, Ludhiana

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** Hello friends I welcome you all to the video lecture series of cyber security and information security in this lecture

**[0:09]** we will study about stream control transmission protocol that is sctp first of all please see the

**[0:17]** contents which I shall cover after covering brief introduction about sctp and sctp Services I shall

**[0:25]** take a features of sctp which will be followed by sctp packet format and last

**[0:33]** I shall take up sctp Association so now let us start stream control transmission

**[0:41]** protocol is a new reliable message oriented transport layer protocol figure shows the relationship of sctp to the

**[0:50]** other protocols TCP and UDP in the Internet Protocol suit sctp lies between the application

**[0:58]** layer and the n Network layer and serves as the intermediary between the application programs and the network

**[1:07]** operations sctp however is mostly designed for internet applications that have recently been

**[1:15]** introduced these new applications such as iua ISDN over IP

**[1:22]** m2ua and M3 UA that is telephony signaling h248 that is Media India Gateway control

**[1:31]** h.323 IP telepon N Sip IP telephony need a more sophisticated service that TCP

**[1:40]** can provide sctp provides this enhanced performance and reliability we briefly

**[1:48]** compare UDP TCP and sctp UDP is a message oriented protocol

**[1:57]** process delivers a message to UDP which is encapsulated in a user datagram and

**[2:04]** sent over the network UDP conserves the message boundaries each message is

**[2:10]** independent from any other message this is a desirable feature when we are dealing with the applications such as IP

**[2:18]** telepon and transmission of realtime data as we will see later in the text

**[2:25]** however UDP is unreliable the sender cannot know the destination of messages sent a message can be lost duplicated or

**[2:35]** received out of order UDP also lacks some other features such as congestion control and flow control needed for a

**[2:44]** friendly transport layer protocol TCP is a bite oriented protocol it is

**[2:52]** receives a message or messages from a process stores them as a stream of bites and sends them in segment

**[3:01]** 3 minutes, 1 second there is no preservation of the message boundaries however TCP is a reliable protocol the duplicate segments are

**[3:09]** detected the LW segments are recent and the bites are delivered to the end process in

**[3:15]** order TCP also has congestion control and flow control mechanisms sctp combines the best

**[3:25]** features of UDP and TCP sctp is a reliable message oriented protocol it preserves the message

**[3:34]** boundaries and at the same time detects lost data duplicate data and out of order data it also has congestion

**[3:43]** control and flow control mechanisms later we will see that sctp has other Innovative features

**[3:51]** unavailable in UDP and TCP sctp is a message oriented reliable

**[3:59]** protocol that combines the best features of UDP and TCP sctp

**[4:07]** Services let us explain the services offered by sctp to the application layer processes process to process

**[4:15]** communication sctp uses all whenn ports in the TCP space following table lists

**[4:23]** some extra port numbers used by sctp protocol iua uses port number

**[4:32]** 90 protocol M2 UA uses port number

**[4:38]** 2904 protocol M3 UA users port number 2905 protocol

**[4:47]** h248 uses port number 2949 protocol h.323 users port numbers

**[4:57]** 1718 1719 1 1720 and

**[5:03]** 11720 protocol sip users port number 5060 multiple

**[5:11]** streams each connection between a TCP client and a TCP server involves one single stream the problem with this

**[5:20]** approach is that a loss at any point in the Stream blocks the delivery of the rest of the

**[5:27]** data this can be acceptable when we are transferring text it is not when we are sending realtime data such as audio or

**[5:36]** video sctp allows multistream service in each connection which is called Association in sctp

**[5:46]** terminology if one of these streams is blocked the other streams can still deliver their data the idea is similar to multiple

**[5:55]** Lanes on a highway each lane can be used for a different type of of traffic for example one lane can be used for a

**[6:03]** regular traffic another for car pools if the traffic is blocked for regular Vehicles car pool Vehicles can still

**[6:11]** reach their destinations multi homing a TCP connection involves one source and one

**[6:20]** destination IP address this means that even if the sender or receiver is a multihomed host connected to more than

**[6:29]** one physical address with multiple IP addresses only one of these IP addresses per end can be utilized during the

**[6:37]** connection an sctp association on the other hand supports multihoming

**[6:44]** service the sending and receiving host can Define multiple IP addresses in each in for an association in this fault

**[6:54]** tolerant approach when one path fails another interface can be used for data delivery without

**[7:01]** 7 minutes, 1 second interruption this fault tolerant feature is very helpful when we are sending and receiving a realtime playl such as

**[7:10]** Internet telepon figure shows the idea of multihoming in the figure the client is

**[7:17]** connected to two local networks with two IP addresses the server is also connected to two networks with two IP

**[7:27]** addresses the client and the server can make an association using four different pairs of IP addresses however note that

**[7:36]** in the current implementations of sctp only one pair of IP addresses can be chosen for normal communication the

**[7:44]** alternative is used if the main choice fails in other words at present sctp

**[7:52]** does not allow load sharing between different parts satp Association allows multiple

**[7:59]** IP addresses for each end full duplex communication like TCP sctp offers full

**[8:08]** duplex service where data can flow in both directions at the same time each sctp then has a sending and receiving

**[8:17]** buffer and packets are sent in both directions connection oriented service

**[8:24]** like TCP sctp is a connection oriented protocol how however in sctp a connection is called an

**[8:33]** association when a process at site a wants to send and receive data from another process at site B the following

**[8:42]** occurs the two actps establish an association between each other data are exchanged in both

**[8:52]** directions the association is terminated reliable service if sctp like

**[9:00]** TCP is a reliable transport protocol it uses an acknowledgement mechanism to

**[9:07]** check the safe and sound arrival of data we will discuss this feature further in the section on error

**[9:15]** control sctp features let us discuss the general features of

**[9:22]** sctp transmission sequence number TSN the unit of data in TCP is a bite

**[9:31]** data transfer in TCP is controlled by numbering bytes using a sequence number on the other hand the unit of data in

**[9:40]** sctp is a data chunk which may or may not have a one to one relationship with

**[9:47]** the message coming from the process because of fragmentation data transfer in sctp is

**[9:55]** controlled by numbering the data chunks SC TP uses a transmission sequence

**[10:01]** 10 minutes, 1 second number TSN to number the data chunks in other words the TSN in sctp plays the

**[10:09]** analogous role as the sequence number in TCP tsn's are 32 bits long and randomly

**[10:18]** initialized between 0 and 232 -1 each data chunk must carry the

**[10:26]** corresponding TSN in its header in satp a data chunk is numbered using a

**[10:34]** transmission sequence number stream identifier si in TCP there is only one stream in

**[10:44]** each Connection in sctp there may be several streams in each Association each

**[10:51]** stream inp needs to be identified using a stream identifier SI each data chunk must get car the SI

**[11:00]** in its header so that when it arrives at the destination it can be properly placed in its stream the SI is a 16 bit

**[11:09]** number starting from zero to distinguish between different streams sctp users and

**[11:18]** Si stream sequence number SSN when a data chunk arrives at the

**[11:25]** destination satp it is delivered to the appr at stream and in the proper order

**[11:32]** this means that in addition to an SI sctp defines each data Chunk in each

**[11:39]** stream with a stream sequence number SSN to distinguish between different data chunks belonging to the same stream

**[11:48]** satp uses ssns packets in TCP a segment carries data

**[11:56]** and control information data data are carried as a collection of bytes control information is defined by six control

**[12:05]** Flags in the header the design of sctp is totally different data are carried as

**[12:12]** data chunks control information as control chunks several control chunks and data chunks can be packed together

**[12:20]** in a packet a packet in sctp plays the same role as a segment in

**[12:27]** TCP TCP has segments sctp has packets we will discuss the format of sctp packet

**[12:36]** in the next section for the moment let us briefly list the differences between an actp

**[12:43]** packet and a TCP segment the control information in TCP is part of the header the control

**[12:51]** information in SCP is included in the control chunks there are several types of control chunks each is used for

**[13:00]** different purpose the data in TCP segment treated as one entity an actp packet can carry

**[13:09]** several data chunks each can belong to different stream the options section which can be

**[13:17]** part of TCP segment does not exist in an sctp packet options in satp are handled

**[13:26]** by defining new chunk types the mandatory part of TCP header is 20

**[13:32]** bytes while the general header in sctp is only 12 bytes the sctp header is shorter due to the

**[13:41]** following an sctp sequence number TSN belongs to each data chunk and hence

**[13:48]** is located in the chunks header the acknowledgement number and window size are part of each control chunk there is

**[13:57]** no need for a head length field known as HL in the TCP segment because there are

**[14:04]** no options to make the length of the header variable the sctp header length

**[14:12]** is fixed 12 bytes there is no need for an urgent pointer inp as we will see later the

**[14:20]** check sum in TCP is 16 bits in sctb it is 32 bits the verification tag in sctp

**[14:29]** is an association identifier which does not exist in TCP in TCP the combination

**[14:37]** of Ip and Port addresses defines a connection in STP we may have

**[14:43]** multihoming using different IP addresses a unique verification tag is needed to Define each

**[14:52]** Association TCP includes one sequence number in the header which defines the number of First white in the data

**[14:59]** section an actp packet can include several different data chunks TSN is and

**[15:09]** ssns Define each data chunk some segments in TCP that carry control information need to consume one

**[15:18]** sequence number control chunks in actp never use a TSN is or SSN number these

**[15:27]** three identifiers below belong only to data chunks not to the whole packet in sctp control information and

**[15:36]** data information are carried in separate chunks in STP we have data chunks

**[15:43]** streams and packets an association may send many packets a packet may contain several chunks and chunks May belong to

**[15:51]** different streams to make the definitions of these terms clear let us suppose that a process a needs to send

**[16:00]** 11 messages to process B and three streams the first four messages are in the first stream the second three

**[16:08]** messages are in the second stream and the last four messages are in the third stream although a message if long can be

**[16:16]** carried by several data chunks we assume that each message fits into one data chunk therefore we have 11 data chunks

**[16:25]** in three streams the application process delivers 11 messages to sctp where each

**[16:32]** message is ear marked for the appropriate stream although the process could deliver one message from the first

**[16:40]** stream and then another from the second we assume that it delivers all messages belonging to the first stream first all

**[16:50]** messages belonging to the second stream next and finally all messages belonging to the last stream

**[16:59]** we also assume that the network allows only three data chunks per packet which means that we need four packets as shown

**[17:07]** in the figure data chunks in stream zero are carried in the first and part of the

**[17:14]** second packet those in stream one are carried in second and the third packet those in stream two are carried in the

**[17:23]** third and fourth packet no that each data chunk needs

**[17:30]** three identifiers TSN SI and SSN TSN is a cultive number and used as we will see

**[17:40]** later for flow control and error control s defines the stream to which the chunk

**[17:46]** belongs SSN defines the chunk order in a particular stream in our example SSN

**[17:53]** starts from zero for each stream acknowledgement number TCP acknowledgement numbers are bite

**[18:02]** oriented and refer to the sequence numbers sctp acknowledgement numbers are chunk oriented they refer to the

**[18:11]** TSN a second difference between TCP and sctp acknowledgements is the control information recall that this information

**[18:20]** is part of the segment header in TCP to acknowledge segments that carry only control information TCP uses a sequence

**[18:29]** number and acknowledgement number for example a Sy YN segment needs to be acknowledged by an AC

**[18:39]** segment in sctp however the control information is carried by the control chunks which do

**[18:46]** not need a TSN these control chunks are acknowledged by another control chunk of

**[18:53]** the appropriate type for example an init control chunk is acknowledged by an init

**[19:02]** a chunk there is no need for a sequence number or an acknowledgement

**[19:09]** number in actp acknowledgement numbers are used to acknowledge only data chunks

**[19:16]** control chunks are acknowledged by other control chunks if necessary packet format in this section

**[19:26]** we show the format of a packet and different types of chunks most of the information presented in this section

**[19:33]** will become clear later this section can be skipped in the first reading or used only as a reference an actp packet has a

**[19:42]** mandatory General header having 12 bytes and a set of blocks called chunks having variable length there are two types of

**[19:51]** chunks control chunks and data chunks a control chunk controls and maintains the association a data chunk carries user

**[20:01]** 20 minutes, 1 second data in an sctp packet control chunks come before data

**[20:08]** chunks General header the general header that is Packet header defines the end

**[20:15]** points of each Association to which the packet belongs guarantees that the packet belongs to a particular

**[20:23]** Association and preserves the Integrity of the contents of packet including the head itself there are four fields in the

**[20:32]** general header Source port address this is a 16bit field that defines the port number of the process

**[20:40]** sending the packet destination port address this is a 16bit field that defines the port

**[20:48]** number of the process receiving the packet verification tag this is a number

**[20:55]** that matches a packet to an association this PR prevents a packet from a previous Association from being mistaken

**[21:02]** as a packet in this Association it serves as an identifier for the association it is repeated in every

**[21:10]** packet during the association there is a separate verification used for each Direction in the association

**[21:19]** checkum this 32 bit contains a crc32 checkm note that the size of the checkum

**[21:26]** is increased from 16 bits to 32 bits inp to allow the use of crc32

**[21:35]** chum chunks control information or user data are carried in chunks chunks have a

**[21:43]** common layout as shown in the figure the first three fields are common to all chunks the information field

**[21:50]** depends on the type of Chunk the important point to remember that sctp requires the information section to be a

**[21:59]** multiple of four bytes if not padding bytes are added at the end of the section chunks need to terminate on a

**[22:08]** 32bit boundary the description of the common fields are as follows type this 8bit

**[22:17]** field can Define up to 256 types of chunks only a few have been defined so far the rest are reserved for future use

**[22:27]** see the table for list of chunks and their descriptions flag this 8bit field defines special

**[22:36]** flags that a particular chunk may need each bit has a different meaning depending on the type of

**[22:44]** Chunk length since the size of information section is dependent on the type of Chunk we need to define the

**[22:52]** chunk boundaries the 16bit field defines the total size of the Chunk in bytes includ including the type flag and

**[22:59]** length Fields sctp Association sctp like TCP is a

**[23:07]** connection oriented protocol however a connection in sctp is called an association to emphasize

**[23:16]** multihoming a connection in actp is called an association association

**[23:24]** establishment Association establishment in SC TP requires a four-way handshake

**[23:31]** in this procedure or process normally a client wants to establish an association with another process normally a server

**[23:39]** using actp as the transport layer protocol similar to TCP the actp server

**[23:47]** needs to be prepared to receive any association association establishment

**[23:54]** however is initiated by the client sctp associ iation establishment is as shown in the

**[24:02]** figure the steps in a normal situation are as follows the client sends the

**[24:09]** first packet which contains an init chunk the verification tag VT of this

**[24:16]** packet defined in general header is zero because no verification tag has yet been defined for this direction client to

**[24:24]** server the init tag includes an initiation tag to be used for packets from the other direction server to

**[24:32]** client the chunk also defines the initial TSN for this direction and

**[24:38]** advertises a value for RND the value of RND is normally advertised in a

**[24:46]** s chunk it is done here because sctp allows the inclusion of data Chunk in

**[24:53]** the third and fourth packets the server must be aware of the available client

**[24:59]** buffer size note that no other chunks can be sent with the first packet the server sends the second

**[25:08]** packet which contains an init acknowledgement chunk the verification tag is the value of the initial tag

**[25:16]** field in the inet chunk this chunk initiates the tag to be used in the other direction defines the

**[25:25]** initial TSN for data flow from server to client and sets the servers

**[25:31]** rewind the value of rewind is defined to allow the client to send a data chunk with the third packet the init

**[25:40]** acknowledgement also sends a cookie that defines the state of server at this moment we will discuss the use of the

**[25:48]** cookies shortly the client sends the third packet which includes a cookie Eco chunk

**[25:57]** this is a very simple chunk that EOS without change the cookie sent by the server satp allows the included of data

**[26:06]** chunks in this packet the server sends the fourth packet which includes the cookie

**[26:13]** acknowledgement chunk that acknowledges the receipt of cookie e chunk sctp

**[26:20]** allows the inclusion of data chunks with this packet so friends this was all about

**[26:28]** stream control transmission protocol sctp hope the concepts explained in this lecture were understandable and helpful

**[26:38]** hope to see you in the next lecture till then goodbye thank you
