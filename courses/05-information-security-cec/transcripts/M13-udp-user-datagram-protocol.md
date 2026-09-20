# UDP - User Datagram Protocol

**Module 13**  
Duration: 22:53  
Video: https://www.youtube.com/watch?v=g4p_kJxiRHk

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Sunil Kumar, Department of Electrical and Computer Engineering, Punjab Agriculture University, Ludhiana

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:02]** [Music]

**[0:15]** Hello friends I am engineer Sunil Kumar from school of electrical engineering and information technology Punjab

**[0:22]** Agriculture University Ludhiana I welcome you all to the video lecture series of cyber and information security

**[0:30]** in this lecture we will study about UDP first of all please see the contents which I shall cover after covering brief

**[0:39]** introduction about UDP I shall take up characteristics of user datagram which will be followed by UDP services in the

**[0:48]** last I shall take up UDP features and UDP packages so now let us start UDP is

**[0:55]** a simple transfer protocol that extends the host to host delivery of packets of the underlying Network into a process to

**[1:04]** process communication since there are many processes running on a given host UDP needs to add a level of Dem

**[1:13]** multiplexing which allowing multiple application processes on each host to share the network figure shows the

**[1:21]** relationship of the user datagram protocol to the other protocols and layers of the tcpip protocol suit UTP is

**[1:29]** located between the application layer and the IP layer and serve as the intermediary between the application

**[1:37]** programs and the network operations a transport layer protocol usually has several responsibilities one is to

**[1:45]** create a process to process communication UDP uses port number to accomplish this another responsibility

**[1:53]** is to provide control mechanism at the transport layer UDP does this task at a very min minimal level there is no flow

**[2:02]** control mechanism and there is no acknowledgement for received packets UDP does provide error control to some

**[2:09]** extent if UDP detects an error in the received packet it silently drop it UTP

**[2:17]** is a connectionless unreliable transfer protocol it does not add anything to the services of Ip except for providing

**[2:25]** process to process communication instead of host to host communication UDP is a very simple protocol using a minimum of

**[2:34]** overhead if a processor wants to send a small message and does not care about reliability it can use UDP sending a

**[2:43]** small message using UDP takes much less interaction between the sender and the receiver than

**[2:50]** TCP next user datagram UDP packets called user datagrams have a fixed size

**[2:57]** header of 8 bytes figure shows the form of the user datagram the fields are as follows First Source port number this is

**[3:06]** the port number used by the process running on the source host it is 16bit long which means that P number can range

**[3:16]** from 0 to 65,535 if the source host is a client the port number in most cases is an inal

**[3:25]** port number requested by the process and chosen by the UDP software running on the source host in the source host is

**[3:34]** the server the p number in most cases is a well-known port number next destination port number this

**[3:42]** is the port number used by the process running on the destination host it is also 16 bits long if the destination

**[3:50]** host is the server the port number in most cases is a well-known port number if the destination host is the client

**[3:59]** the port number in most cases and inferable port number in this case the server copies the inferable port number

**[4:06]** it has received in the request packet this is a 16bit field that defines the total length of the user datagram and

**[4:14]** header Plus data the 16 bits can define a total length of 0 to

**[4:21]** 65,535 bytes however the total length needs to be much less because a UDP user

**[4:28]** datagram is stored in a and IP datagram with the total length of 65,535 bytes the length field is a UDP

**[4:37]** user datagram is actually not necessary a user datagram is encapsulated in an IP datagram there is a field in IP datagram

**[4:47]** that defines the total length there is another field in the IP datagram that defines the length of the header so if

**[4:55]** we subtract the value of the second field from the first we can deduce the length of the user datagram that is

**[5:03]** encapsulated in an IP datagram UTP length equal to IP length minus IP

**[5:11]** headers length however the designers of the UDP protocol felt that it was more efficient for the destination UDP to

**[5:19]** calculate the length of the data from the information provided in the UDP used datagram rather than ask the IP software

**[5:28]** to supply this information we should remember that when the IP software delivers the UDP user data gram

**[5:35]** to the UDP layer it has already dro the IP headers next checkm this field is used

**[5:43]** to detect errors over the entire user datagram that is header Plus data I will discuss the dump example of UDP header

**[5:51]** in hexadecimal format the UDP header is CB

**[5:57]** 8400 d 0 01 C 0 01 C some questions based on this UDP header first question

**[6:07]** what is a source port number The Source port number is the first four hexadecimal digits like C B

**[6:15]** 846 which means that the source Board number is 5210 next question what is a destination

**[6:23]** port number the answer is that the destination port number is the second four hexadecimal digits that are 0 0 0

**[6:32]** D14 which means that the destination port number is 13 next question what is the total length of the user datagram

**[6:40]** the third four hexadecimal digits 0 0 1 c16 defines the length of the whole UDP

**[6:47]** packets as 28 bytes next question what is the length of data the length of the

**[6:54]** data is the length of the whole packet minus the length of the header means 28 - 8 equal to 20 bytes next question is

**[7:03]** the packet directed from a client to a server or visce Versa answer since the destination port number is 13 the packet

**[7:11]** is from the client to the server next question what is the client process the client process is the

**[7:19]** daytime next UDP Services I discuss the general Services provided by the UDP in

**[7:26]** transport layer first process to process communication UDP provides process to process communication using sockets with

**[7:35]** the combination of IP addresses and port numbers several port numbers used by UDP

**[7:41]** are as follows port s is for Eco Port 9 is for discard port 11 is for users port

**[7:50]** 13 for daytime Port 17 is for COD Port 19 is for charging port 53 is for domain

**[7:58]** Port 6 67 is for boot PS Port 68 is for boot PC Port 69 is for tftp Port 111 is

**[8:08]** for RPC Port 123 is for ntp Port 161 is for SNMP Port 162 is for SNMP

**[8:18]** trap next service is connectionless service UDP provides a connectionless service this means that each user

**[8:26]** datagram sent by UTP is an independent datagram there is no relationship between the different users datagram

**[8:34]** even if they are coming from the same Source process and going to the same destination program the user datagrams

**[8:42]** are not numbered also there is no connection establishment and no connection termination as is the case of

**[8:49]** TCP this means that each user datagram can travel on a different path one of the ramifications of being

**[8:57]** connectionless is that the processes that uses UDP cannot send a steam of

**[9:03]** data to UDP and expect UDP to chop them into different related users datagrams

**[9:10]** instead each request must be small enough to fit into one user datagram in the case of UDP only those processes

**[9:18]** sending short messages when messages less than 6557 bytes next flow control UDP is a

**[9:27]** very simple protocol there is no flow control and hence no window mechanism the receiver May overflow with incoming

**[9:35]** messages the lack of flow control means that the process using UDP should provide for this service if it is needed

**[9:45]** next error control there is no error control mechanism in a UDP except for the check sum this means that the sender

**[9:54]** does not know if a message has been lost or duplicated when when the receiver detects an error through the check sum

**[10:02]** the user datagram is silently discarded the lack of error control means that the process using UTP should provide for

**[10:11]** this service if it is needed next checkm UDP check sum calculation is different

**[10:18]** from the 104 IP here the checkm includes three sections a pursuer header a UDP

**[10:26]** header and the data coming from the application layer the pursu header is the part of the header of the IP packet

**[10:33]** in which the user datagram is to be encapsulated with some Fields filled with zeros if the check sum does not

**[10:42]** include pedo header a user datagram may arrive safe and sound however if the IP

**[10:49]** header is corrupted it may be delivered to the wrong host the protocol field is added to ensure that the packets belong

**[10:58]** to UDP and to TCP we will see later that if a process can use either UDP or TCP

**[11:06]** the destination p number can be the same the value of the protocol field for UDP is 17 if this value is changed during

**[11:15]** the transmission the check some calculation at the receiver will detected and UDP drops the packet it is

**[11:23]** not delivered to the wrong protocol note the similarities between the pursued header fields and the last 12 bytes of

**[11:31]** the IP address next congestion control since UDP is a connectionless protocol it does not provide congestion control

**[11:40]** UDP assumes that the packets sent are small and cannot create congestion in the network this assumption may or may

**[11:48]** not be true today when UDP is used for realtime transfer of audio and video

**[11:55]** next encapsulation and D encapsulation to send a message from one process to another process the UDP protocol

**[12:02]** encapsulates and de encapsulates the messages first encapsulation when a process has a message to send through

**[12:11]** UDP it means the message to UDP along with the pair of socket addresses and the length of data UDP receives the data

**[12:20]** and adds the UDP header UDP then passes the user datagram to IP with the socket addresses IP adds its own head

**[12:29]** using the value 17 in the protocol field which indicating that the data has come

**[12:36]** from the UDP protocol the IP datagram is then passed to the data link layer the

**[12:42]** data link layer receives the IP datagram which adds its own header and passes it to the physical layer the physical layer

**[12:51]** encodes the bits into electrical or Optical signals and send it to the remote machine next decapsulation

**[12:59]** when the message arrives at the destination host the physical layer decodes the signal into bits and passes

**[13:06]** it to the data link layer the data link layer uses the header to check the data if there is no error the header and the

**[13:15]** trailer are dropped and the datagram is passed to IP the IP software does its

**[13:22]** own checking if there is no error the header is dropped and the user datagram is passed to UDP with the sender and the

**[13:31]** receiver IP addresses UDP uses the check sum to check the entire user datagram if there is no error the header is dropped

**[13:40]** and the application data along with the sender socket addresses is passed to the processes the cender socket address is

**[13:48]** passed to the processes in case it needs to respond to the message received next

**[13:55]** queing in UDP qes are associated with ports at the client side when a process

**[14:02]** starts it request a port number from the operating system some implementations create both an incoming and outgoing

**[14:11]** cues associated with each process other implementations create only an incoming queue associated with each process note

**[14:20]** that even if a process wants to communicate with multiple processes it obtains only one p number and eventually

**[14:28]** one outgoing and one incoming queue the cues opened by the clients are in most cases identified by eeral P numbers the

**[14:37]** cues function as long as the process is running when the process terminates the cues are destroyed the client processes

**[14:45]** can send messages to the outgoing cues by using Source Board number specified in the request UDP removes the messages

**[14:54]** one by one and after adding the UDP header deliver them to IP an outgoing queue can overflow if this

**[15:02]** happens the operating system can ask the client processes to wait before sending any more messages next multiplexing and

**[15:11]** Dem multiplexing in a host running a tcpip protocol suit there is only one UDP but possibly several processes that

**[15:20]** may want to use this service of UDP to handle this situation UDP multiplexes

**[15:26]** and D multiplexes first mul Lexing at the center side there may be several processes that need to send user

**[15:35]** datagrams however there is only one UDP this is a many to one relationship and

**[15:42]** requires multiplexing UDP accepts messages from different processes differentiated by their assigned P

**[15:50]** numbers after adding the header UDP passes the user datagram to IP next d

**[15:58]** multiplexing at the receiver side there is only one UDP however we may have many

**[16:04]** processes that canes user datagrams this is one to many relationship and requires

**[16:11]** Dem multiplexing UDP receives user datagrams from IP after error checking and dropping of the header UDP delivers

**[16:20]** each message to the appropriate process based on the port numbers next comparison between UDP and generic

**[16:28]** simple protocols we can compare UDP with the connectionless simple protocol the only difference is that the UDP provides

**[16:36]** an optional check sum to detect corrupted packets at the receiver side if the check sum is added to the packet

**[16:44]** the receiving UDP can check the packet and discard the packet if it is corrupted no feedback however is sent to

**[16:52]** the center UDP is an example of the connectionless simple protocol with the exception of an optional checkm added to

**[17:01]** 17 minutes, 1 second packets for error detection next UDP features we briefly discuss some

**[17:08]** features of UDP and their advantages and disadvantages First connectionless Service as we mentioned previously UDP

**[17:16]** is a connectionless protocol each UDP packet is independent from other packets sent by the same application program

**[17:24]** this feature can be considered as an advantage or disadvantage depending on the application requirement it is an

**[17:32]** advantage if for example a client application needs to send a short request to a server and to receive a

**[17:39]** short response if the request and response can each fit in one single user datagram a connectionless service may be

**[17:47]** preferable the overhead to establish and close the connection may be significant in this case in the connection oriented

**[17:55]** service to achieve the above goal at least nine packets are exchanged between the client and the server in

**[18:03]** connectionless service only two packets are exchanged the connectionless service provides less delay and the connection

**[18:10]** oriented service creates more delay if delay is an important issue for the application the connection L service is

**[18:17]** preferred next lack of error control UDP does not provide error control it

**[18:24]** provides an unreliable service most applications accept reliable services from a transport lay protocol although a

**[18:34]** reliable service is desirable it may have some side effects that are not acceptable to some applications when a

**[18:42]** transport layer provides reliable Services if a part of the message is lost or corrupted it needs to resend

**[18:50]** this means that the receiving transport layer cannot deliver that part of the application immediately there is an

**[18:57]** uneven delay between different parts of the message delivered to the application layer some applications by Nature do not

**[19:05]** even notice these uneven delays but for some they are very crucial next lack of

**[19:12]** congestion control UDP does not provide congestion control however UDP does not create additional traffic in an error

**[19:21]** prone Network TCP May resent a packet several times and thus contribute to the creation of the congestion therefore in

**[19:30]** some cases lack of error control in UDP can be considered an advantage when congestion is a big issue next UDP

**[19:39]** package to show how UDP handles the sending and receiving of UD package we present a simple version of UDP package

**[19:48]** we can say that UDP package involve five components first control Block Table

**[19:55]** input q a control block module an input module and a output module figure shows the five components and

**[20:05]** their interactions first control Block Table in our package UDP has control

**[20:11]** Block Table to keep track of the open ports each entry in this table has a minimum of four Fields the state which

**[20:21]** can be free or in use the process ID the port number and the corresponding Q

**[20:27]** number next next input cues our UDP package uses a set of input cues one for

**[20:34]** each process in this design we do not use output cues next control block module the control block module is

**[20:44]** responsible for the management of the control block table when a process starts it asks for a port number from

**[20:52]** the operating system the operating system assigns well-known port numbers to servers and imperal port numbers to

**[21:00]** the client the processes passes the process ID and the port number to the control block module to create an entry

**[21:09]** in the table for the process the field for Q number has a value of zero note that we have not include a strategy to

**[21:18]** deal with the table that is full next input module the input module receives a

**[21:24]** user datagram from the IP it searches the control Block Table to find an entry

**[21:31]** having the same port number as this user datagram if the entry is found the module uses the information in the entry

**[21:40]** to NQ the data if the entry is not found it generates an icmp message next output

**[21:49]** module the output module is responsible for creating and sending user

**[21:55]** datagrams so friends this was all about UDP hope the concepts explained in this

**[22:01]** 22 minutes, 1 second lecture were understandable and helpful hope to see you in the next lecture till then goodbye thank

**[22:10]** [Music]

**[22:27]** you for

**[22:34]** [Music]
