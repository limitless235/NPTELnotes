# Transmission Control Protocol

**Module 06**  
Duration: 27:00  
Video: https://www.youtube.com/watch?v=9bKXrX4lz6g

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr. Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:15]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:22]** University of Science and Technology Hisar harana I welcome you all to the lecture series of of cyber and

**[0:31]** information security in this lecture we will study about transmission control

**[0:37]** protocol which is used for connection oriented transmission at transport layer

**[0:44]** level for end to end connectivity of computers first of all please see the contents which I shall

**[0:52]** cover after covering brief introduction about TCP I shall take up header of TCP

**[1:00]** which will be followed by connection management and flow control process in

**[1:07]** TCP so now let us start the foundation of TCP was laid in May

**[1:15]** 1974 when Institute of electrical and electronic Engineers itle published a

**[1:23]** paper entitled a protocol for packet Network intercommunication the papers author

**[1:31]** Surf and KH described an internetworking protocol for sharing resources using

**[1:40]** packet switching among the nodes a central control component of this model

**[1:46]** was the transmission control program TCP that incorporated both connection oriented

**[1:55]** links and datagram services between host this transmission control program was

**[2:04]** later divided into a modular architecture consisting of the transmission control protocol at the

**[2:12]** connection oriented layer and the Internet Protocol at the internet

**[2:19]** layer the model became known informally as PCP IP although formerly it was

**[2:27]** henceforth called the Internet Protocol suit PCP is a reliable stream delivery

**[2:37]** service that guarantees that all bytes received will be identical with bytes

**[2:44]** sent and in the correct order this fundamental technique requires the receiver to respond with an

**[2:52]** acknowledgement message as it receives the data the sender keeps a record of

**[3:00]** each packet it sends the sender also maintains a timer from when the packet

**[3:07]** was sent and retransmits a packet if the timer expires before the message has

**[3:15]** been acknowledged the timer is needed in case a packet gets lost or corrupted TCP was

**[3:25]** formally defined in RFC 793 as time went on various errors and

**[3:33]** inconsistencies were detected and the requirements were changed in some

**[3:39]** areas these clarifications and some bugs fixes are detailed in RFC

**[3:48]** 112 extensions are given in RFC 1323 while IP handles actual delivery of

**[3:58]** the data TCP keeps track of the individual units of data transmission

**[4:04]** called segments the internet layer encapsulates each TCP segment into an IP

**[4:13]** packet by adding an IP header that includes the destination IP address when

**[4:21]** the client program on the destination computer receives them the TCP layer reassembles the individual visual

**[4:30]** segments and ensures they are correctly ordered and error

**[4:36]** free for lack of a better term we will use acronym tpdu that is transport protocol data

**[4:46]** unit for messages sent from transport layer thus tpd exchanged by the

**[4:55]** transport layer are contained in packets at the Network layer in turn packets are

**[5:04]** contained in frames at the data link layer this nesting is Illustrated in

**[5:13]** figure TCP service is obtained by the sender and receiver creating end points called

**[5:21]** sockets each socket has a socket number consisting of the IP address of the host and a 16bit number

**[5:30]** local to that host called a port a port is the TCP name for a transport service

**[5:37]** access point tsap a socket may be used for multiple connections at the same time in other

**[5:47]** words two or more connections May terminate at the same socket connections are identified by the

**[5:56]** socket identifiers at both ends that is Socket 1 socket

**[6:04]** 2 no virtual circuit numbers or other identifiers are used port numbers below

**[6:13]** 1024 are called well-known ports and are reserved for standard

**[6:20]** Services a few of the better known ones are listed in table the internet

**[6:27]** assigned numbers Authority are AA is responsible for maintaining the official

**[6:34]** assignments of port numbers for specific uses as we can see in table Port 20

**[6:42]** supports TCP and UDP communication for FTP data

**[6:50]** transfer Port 23 supports TCP and UDP communication for tnet protocol

**[7:00]** Port 25 supports TCP and UDP communication for simple mail transfer

**[7:08]** protocol SMTP in email system Port 53 supports TCP and UDP

**[7:18]** communication for domain name system DNS Port 69 is for trial file transfer

**[7:28]** protocol tftp Port 0 supports TCP sctp and UDP

**[7:38]** communication for hyper text transfer protocol

**[7:44]** HTTP Port 107 supports TCP and UDP for remote tet service

**[7:54]** protocol Port 109 supports TCP and UDP P for post office protocol

**[8:03]** V2 Port 110 supports TCP and UDP for post office protocol

**[8:11]** V3 Port 115 supports TCP for simple file transfer

**[8:20]** protocol Port 119 supports TCP for Network news transfer protocol nnt

**[8:30]** P Port 143 supports TCP for internet message access protocol

**[8:39]** IMAP Port 220 supports TCP and UDP for

**[8:44]** internet message access protocol IMAP Port 500 supports TCP and UDP for

**[8:54]** Internet Security Association and Key Management prot

**[9:00]** protocol Port 530 supports TCP and UDP for remote procedure call

**[9:10]** RPC Port 554 supports TCP and UDP for realtime streaming protocol

**[9:20]** rtsp protocol 587 supports TCP for email message submission SMTP

**[9:29]** Port 698 supports UDP for optimized link state routing

**[9:37]** osr Port 953 supports TCP and UDP for

**[9:43]** domain name system R and DC Service Port 995 supports TCP for post

**[9:53]** office protocol three connections are full duplex and point to point

**[9:59]** full duplex means that traffic can go in both directions at the same time point

**[10:06]** to point means that in each connection has exactly two end points TCP does not

**[10:15]** support multicasting or broadcasting a TCP connection is a bite stream not a message

**[10:23]** stream message boundaries are not preserved end to end for for example if

**[10:30]** the sending process does four 512 byte right to a TCP stream these data may be

**[10:38]** delivered to the receiving process as four 512 byte chunks two 1024 by chunks

**[10:47]** or one 2048 byte chunk as shown in figure or some other way

**[10:55]** also there is no way for the receiver to detect the the unit in which the data were

**[11:03]** written figure a shows four 512 by segments sent as separate IP datagram

**[11:11]** and figure B shows the 2048 byte of data delivered to the application in a single

**[11:19]** read call after basic of TCP and Port let us

**[11:26]** see the TCP segment header figure shows the layout of a TCP segment

**[11:35]** every segment begins with a fixed format of 20 by header the fixed header may be

**[11:42]** followed by header options after the options if any up to

**[11:49]** 65535 -20 -20 which is equal to

**[11:57]** 65495 databytes may follow where the first 20 refers to

**[12:04]** the IP header and second 20 refers to the TCP header segments without any data are

**[12:13]** legal and commonly used for acknowledgements and control messages now let us discuss the TCP

**[12:22]** header Fields One By One The Source port and destination Port

**[12:28]** fields identify the local end points of the connection a port plus its host IP

**[12:36]** address forms a 48 bit unique end point the source and destination end

**[12:44]** points together identify the connection the sequence number and acknowledgement number field performs

**[12:53]** their usual functions for the purpose of delivery confirmation no note that the

**[13:00]** acknowledgement number specifies The Next Bite expected not the last bite

**[13:06]** correctly received both are 32 bits long because every bite of data is numbered

**[13:14]** in a TCP stream the TCP header length tells how

**[13:20]** many 32bit words are contained in the TCP header this information is needed

**[13:28]** because the op options field is of variable length technically this field really indicates the start of the data

**[13:36]** within the segment measured in 32bit words but that number is just the header

**[13:44]** length in words so the effect is the same next comes a six-bit field that is

**[13:52]** not used next are six 1 bit Flags urg is set

**[13:59]** to one if the Urgent pointer is in use the Urgent pointer is used to indicate a

**[14:07]** bite offset from the current sequence number at which urgent data are to be

**[14:15]** found the AK bit is set to one to indicate that the acknowledgement number is

**[14:23]** valid if AK is zero the segment does not contain an acknowledgement so the acknowledgement number field is

**[14:32]** ignored the psh bit indicates pushed data the receiver is hereby kindly

**[14:40]** requested to deliver the data to the application upon arrival and not buffer

**[14:46]** it until a full buffer has been received the rst bit is used to reset a

**[14:53]** connection that has become confused due to host crash or some mother

**[15:01]** 15 minutes, 1 second reason the sin bit is used to establish connections the connection request has

**[15:08]** sin as one and akk as zero to indicate that the piggy back acknowledgement

**[15:16]** field is not in use the connection reply does bear an

**[15:23]** acknowledgement so it has sin as one and AK as one

**[15:29]** in essence the sin bit is used to denote connection request and connection

**[15:37]** accepted if AK bit is used to distinguish between those two

**[15:45]** possibilities the fin bit is used to release a connection it specifies that

**[15:52]** the sender has no more data to transmit flow control in TC p is handled

**[16:00]** using a variable sized sliding window the window size field tells how many

**[16:07]** bytes may be sent starting at the bite acknowledged a check sum is also

**[16:14]** provided for extra reliability it check sums the header the data and the conceptual pseudo

**[16:25]** header after TCP header let us move over to to socket Primitives in

**[16:31]** TCP socket Primitives are widely used for internet programming they are listed in

**[16:40]** figure the socket primitive creates a new communication end point newly created socket do not have

**[16:50]** Network addresses these are assigned using the bind primitive bind primitive is used to

**[16:58]** attach a local address to a socket next comes the listen call which

**[17:06]** announces willingness to accept connections and allocate space to queue incoming calls for the case that several

**[17:15]** clients try to connect at the same time to block waiting for an incoming

**[17:23]** connection the server executes and accept primitive now let us look at the client

**[17:31]** side here to a socket must first be created using the socket primitive but

**[17:37]** bind is not required since the address used does not matter to the

**[17:45]** server the connect primitive blocks the caller and actively starts the connection

**[17:52]** process when the appropriate tpdu is received from the server the client process is unblocked and the connection

**[18:01]** 18 minutes, 1 second is established both sides can now use send or receive to transmit and receive data

**[18:11]** over the full duplex connection connection release with

**[18:18]** socket is symmetric when both sides have executed a close primitive the connection is

**[18:27]** released now we shall learn how TCP connection is established connections are established

**[18:36]** in TCP by means of the threeway handshake process to establish a

**[18:42]** connection one side say the server passively waits for an incoming Connection by executing the listen and

**[18:51]** accept Primitives the other side say the client executes a connect PR

**[18:59]** primitive the connect primitive sets a TCP segment with a sin bit on and AK bit

**[19:07]** off and waits for a response when this segment arrives at

**[19:15]** the destination the TCP entity checks to see if there is a process that has done

**[19:22]** a listen on the port given in the destination Port field if not it sends a

**[19:29]** reply with the RSD bit on to reject the connection if some process is listening

**[19:37]** to the port that process is given the incoming TCP segment it can then either accept or

**[19:46]** reject the connection if it accepts an acknowledgement segment is sent

**[19:53]** back the sequence of TCP segments sent in the normal case is shown in figure a

**[20:01]** 20 minutes, 1 second on the left side on receip of sin with SQ as X host

**[20:09]** to return sin with seq as Y and AK as x +

**[20:17]** 1 further host one sends data with seq

**[20:22]** as x + 1 and AK as y + 1

**[20:30]** in the event that Two Hosts simultaneously attempt to establish a connection between the same two sockets

**[20:39]** the sequence of events is as Illustrated in Part B on right side of

**[20:48]** figure which clearly shows that Collision will occur after connection setup let us see

**[20:57]** how TCP connection is released to release a connection either

**[21:04]** party can send a TCP segment with a fin bit set which means that it has no more

**[21:12]** data to transmit when the fin is acknowledged that direction is shut down

**[21:18]** for new data data may continue to flow indefinitely in the other

**[21:26]** direction when both directions have been shut down the connection is released

**[21:32]** normally four TCP segments are needed to release a

**[21:39]** connection one Fin and one AK for each Direction however it is possible for the

**[21:49]** first AK and the second fin to be contained in the same segment reducing

**[21:56]** the total segment count to three to avoid the two Army problem

**[22:04]** timers are used if a response to a fin is not forthcoming within two maximum

**[22:12]** packet lifetime the cender of the fin releases the connection the other side will

**[22:21]** eventually notice that nobody seems to be listening to it anymore and will time

**[22:27]** out as as well now let us see TCP connection management and flow

**[22:34]** control as mentioned earlier window Management in TCP is not directly tied to

**[22:42]** acknowledgements as it is in most data link protocols now let us see TCP

**[22:49]** connection management and flow control process step by

**[22:55]** step in Step One the receiv has a 4,096 byte buffer as shown in right side

**[23:04]** of figure if the sender transmits a 2048 byte segment in step one with sequence

**[23:14]** as zero and it is correctly received the receiver will acknowledge the segment in

**[23:21]** step two however since receiver has now only 2048 bytes of buffer space it will

**[23:30]** advertise a window of 204 rate starting at the next bite expected and AK as

**[23:40]** 2048 at this point 2K space is available in receiver buffer as shown on right

**[23:48]** side in step two in step three the sender transmits

**[23:55]** another 2048 bytes with sequence as 2048 receiver receives this 2K data and

**[24:04]** it receiver buffer is full so in step four it is acknowledged

**[24:11]** with AK as 4096 and win as zero the center must stop until the

**[24:21]** application process on the receiving host has removed some data from the

**[24:27]** buffer at which TCP can advertise a larger window when the window is zero the

**[24:35]** cender may not normally send segments with two exceptions first Urgent data may be sent

**[24:44]** for example to allow the user to kill the process running on the remote

**[24:51]** machine second the sender may send a one byte segment to make the receiver will

**[24:58]** re announce the next bite expected and window size the TCP standard explicitly

**[25:08]** provides this option to prevent deadlock if a window announcement ever gets

**[25:15]** lost as soon as receiver application reads 2K data it has 2K window size so

**[25:24]** receiver replies with AK as 409 96 and win as

**[25:32]** 2048 in Next Step transmitter will send 1K data with sequence as

**[25:41]** 4096 so in this way communication takes place and endtoend flow control through

**[25:50]** TCP so friends this was transmission control protocol finally summarizing

**[25:59]** we learned about introduction to TCP protocol which was followed by TCP

**[26:06]** header in the end we discussed connection management and flow control in

**[26:14]** TCP hope the concepts explained in this lecture were understand and helpful hope

**[26:22]** to see you in the next lecture till then goodbye enjoy the day thank you

**[26:32]** [Music]
