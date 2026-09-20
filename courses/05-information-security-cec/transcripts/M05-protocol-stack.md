# Protocol Stack

**Module 05**  
Duration: 31:40  
Video: https://www.youtube.com/watch?v=KanyeVKL6cs

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Navdeep Singh, Department of Computer Engineering, Punjabi University, Patiala

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:15]** my dear students hello I welcome you all in our series of lectures on cyber security today we are going to study

**[0:24]** about protocol stack after going through this lesson you will be able to understand the needs

**[0:31]** of protocols and standards also you will be able to identify various protocols at different

**[0:38]** layers of protocol stack so let us begin with it the protocol stack is an implementation of a

**[0:47]** computer networking protocol suit the terms are often used interchangeably the suit is the

**[0:54]** definition of the protocols and the stack is the software implementation of them a protocol stack is a complete set of

**[1:03]** network protocol layers that work together to provide networking capabilities it is called aack because

**[1:12]** it is typically designed as a hierarchy of layers each supporting the one above it and using those below

**[1:20]** it individual protocols within a suit are often designed with a single purpose in mind this modelization makes design

**[1:29]** and EV valuation easier because each protocol module usually communicates with two others

**[1:37]** they're commonly imagined as layers in a stack of protocols the lowest protocol always

**[1:44]** deals with low level physical interaction of the hardware every higher layer adds more

**[1:52]** features user applications usually deal only with the topmost layers in Practical implementation

**[2:01]** 2 minutes, 1 second protocol Stacks are often divided into three major sections media transport and applications a particular operating

**[2:10]** system or platform will often have two well-defined software interfaces one between the media and transport layers and one between the

**[2:19]** transport layers and applications the media to transport interface defines how transport protocol

**[2:26]** software makes use of particular media and Hardware types for example this interface level would Define how TCP IP

**[2:36]** transport software would talk to the ethernet Hardware the application to transport interface defines how application

**[2:45]** programs make use of the transport layers for example this interface level would Define how a web browser program

**[2:52]** would talk to the TCP IP transport software next is OSI model

**[3:01]** 3 minutes, 1 second Osa stands for Open System interconnection model it is a conceptual model that characterizes and standardizes the communication functions

**[3:10]** of a telecommunication or Computing system without regard to their underlying internal structure and Technology its goal is the

**[3:19]** interoperability of diverse communication systems with the standard protocols the model partitions a

**[3:26]** communication system into abstraction layers the original version of the model defines seven

**[3:34]** layers the model is a product of the open systems interconnection project at the International Organization for standardization maintained by

**[3:42]** identification ISO 7498 the Osa model has seven

**[3:49]** layers the principles that were applied to arrive at the seven layers can be briefly summarized as number one a layer

**[3:58]** should be created where a different abstraction is needed number two each layer should perform a well- defined

**[4:08]** function number three the function of each layer should be chosen with an eye toward defining internationally standardized

**[4:16]** protocols and number four the layer boundaries should be chosen to minimize the information flow across the

**[4:24]** interfaces number five the number of layers should be large enough that distinct functions need not be thrown together in the same layer out of

**[4:33]** necessity and small enough that the architecture does not become unwieldy figure shows the OSI reference

**[4:42]** model see this next figure the figure shows the exchange of data using USA

**[4:49]** model D7 means the data unit at L 7 D6 means the data unit at layer six and so

**[4:58]** on the process starts at layer 7 called the application layer and then moves from layer to layer in descending

**[5:05]** sequential order at each layer a header or possibly a trailer can be added to the data

**[5:14]** unit commonly the trailer is added only at Layer Two when the formated data unit passes

**[5:22]** through the physical layer it is changed into an electromagnetic signal and transported along a physical link

**[5:31]** upon reaching its destination the signal passes into layer one and is transformed back into digital

**[5:38]** form the data units then move back up through the OSI layers as each block of data reaches the

**[5:47]** next higher layer the headers and trailers attached to it at the corresponding sending layer are removed

**[5:54]** and actions appropriate to that layer are taken by by the time it reaches L 7 the

**[6:01]** 6 minutes, 1 second message is again in a form appropriate to the application and is made available to the

**[6:08]** recipient next is layers in the Osa model the various layers of Osa model

**[6:16]** are number one physical layer in the seven layer USA model of computer networking the physical layer

**[6:24]** or layer one is the first and the lowest layer the physical layer coordinates the functions required to carry a bitstream

**[6:33]** over a physical medium it deals with a mechanical and electrical specifications of the interface and transmission

**[6:42]** medium it also defines the procedures and functions that physical devices and interfaces have to perform for

**[6:50]** transmission to occur now what are the services provided by physical layer in digital Communications symbol

**[6:58]** rate also known as board rate and modulation rate is the number of symbol changes waveform changes or signaling

**[7:05]** events across the transmission medium per time unit using a digitally modulated signal or a line

**[7:13]** code the symbol rate is measured in board or symbols per second in the case of a line code the

**[7:20]** symbol rate is the pulse rate in pulses per second number two providing a standardized interface to physical

**[7:29]** transmission media including mechanical specifications of electrical connectors and cables for example maximum cable

**[7:36]** length providing electrical specifications of transmission line signal level and impedance providing

**[7:44]** radio interface including electromagnetic spectrum frequency allocation and specification of signal strength analog bandwidth etra and

**[7:53]** providing specifications for IR over optical fiber or a wireless IR communication link

**[8:01]** 8 minutes, 1 second number three modulation in electronics and Telecommunications modulation is the process of wearing one or more

**[8:09]** properties of a periodic waveform called the carrier signal with a modulating signal that typically contains information to be

**[8:18]** transmitted a modulator is a device that performs modulation a demodulator is a device

**[8:25]** that performs demodulation the inverse of modulation a botom can perform both

**[8:32]** operations number four line coding line coding consists of representing the digital signal to be

**[8:40]** transported by a waveform that is optimally tuned for the specific properties of the physical Channel and of the receiving

**[8:49]** equipment the pattern of voltage current or Photon used to represent the digital data on transmission link is called the

**[8:57]** line encoding the common types of line encoding are unipolar polar bipolar and Manchester

**[9:07]** encoding after line coding the signal is put through a physical Channel either a transmission medium or a data storage

**[9:15]** medium number five bit synchronization the sender and receiver not only must use the same bit rate but

**[9:24]** also must be synchronized at the bit level in other words the and the receiver clocks must be

**[9:33]** synchronized number six line configuration the physical layer is concerned with the connection of devices

**[9:40]** to the media in a point to-point configuration two devices are connected through a dedicated Link in a multipoint configuration a

**[9:49]** link is shared among several devices number seven physical

**[9:56]** topology the physical topology defines how devices are connected to make a

**[10:02]** network and number eight is transmission mode transmission mode defines the

**[10:09]** direction of transmission between two devices Simplex half duplex or full duplex next is data link

**[10:18]** layer the data link cayer or Layer Two is the second layer of the seven layer USA model of computer

**[10:26]** networking this layer is the protocol layer that trans transfers data between adjacent Network nodes in a wide area

**[10:32]** network or between nodes on the same local area network segment the data link clear provides the

**[10:40]** functional and procedural means to transfer data between Network entities and might provide the means to detect

**[10:47]** and possibly correct errors that may occur in the physical layer now what are the services provided by data link

**[10:55]** CER number one framing a frame is the protocol data unit at the data link

**[11:03]** cayer frames are the result of the final layer of encapsulation before the data is transmitted over the physical

**[11:11]** layer a frame is a unit of transmission in a link layer protocol and consist of a link clear header followed by a

**[11:19]** packet number two physical addressing if frames are to be distributed to different systems on the

**[11:27]** network the data link clear adds a header to the frame to define the sender or receiver of the

**[11:34]** frame if the frame is intended for a system outside the senders Network the receiver address is the address of the

**[11:41]** device that connects the network to the next one number three flow control flow

**[11:49]** control is the process of managing the rate of data transmission between two nodes to prevent a fast sender from

**[11:56]** overwhelming a slow receiver it provides a mechanism for the receiver to control the transmission speed so

**[12:04]** that the receiving node is not overwhelmed with data from the transmitting node number four error

**[12:11]** control it allows the receiver to inform the sender if a frame is lost or damaged during transmission and coordinates the

**[12:19]** retransmission of those frames by the sender error control in the data link cleer is based on automatic repeat

**[12:27]** request whenever an is detected specified frames are retransmitted number five logical link control logical

**[12:37]** link control refers to the functions required for the establishment and control of logical links between local devices on a

**[12:45]** network as mentioned this is usually considered a dll sublayer it provides services to the network layer above it

**[12:53]** and hides the rest of the details of the data link clear to allow different Technologies to work seamlessly with the higher

**[13:01]** 13 minutes, 1 second layers most local area networking Technologies use the i e 82.2 LLC

**[13:08]** protocol and number six is Media Access Control this refers to the procedures used by devices to control access to the

**[13:17]** network medium since many networks use a shared medium such as a single network cable or a series of cables that are electrically

**[13:26]** connected into single virtual medium it is necessary to have rules for managing the medium to avoid

**[13:33]** conflicts for example ethernet uses the csma CD method of media Access Control

**[13:40]** while token ring uses token passing next is Network layer in the seven layer Osa model of computer

**[13:48]** networking the network layer is layer three the network layer is responsible for packet forwarding including routing

**[13:57]** through intermediate routers since it knows the address of neighboring Network nodes and it also manages quality of

**[14:05]** service the services provided by Network CER are number one logical addressing every device that communicates over a

**[14:14]** network has associated with it a logical address sometimes called a layer three address for example on the internet the

**[14:22]** Internet Protocol is the network clear protocol and every machine has an IP address number two

**[14:30]** routing moving data across a series of interconnected networks is probably the defining function of the network

**[14:37]** layer it is the job of the devices and software routines that functions at the network layer to handle incoming Packers

**[14:45]** from various sources and determine their final destination number three datagram

**[14:53]** encapsulation the network layer normally encapsulate messages received from higher layers by placing them into

**[15:00]** datagrams also called Packers with a network clear header number four fragmentation and

**[15:08]** reassembly the network layer must send messages down to the data link layer for transmission some data link clear

**[15:16]** technologies have limits on the length of any message that can be sent if the packet that the network CER

**[15:23]** wants to send is too large the network cayer must split the packet up send each piece to the data link clear and then

**[15:30]** have pieces reassembled once they arrive at the network clear on the destination machine number five error handling and

**[15:40]** Diagnostics special Protocols are used at the network clear to allow devices that are logically connected or that are

**[15:47]** trying to root traffic to exchange information about the status of host on the network or their devices

**[15:55]** themselves various protocols at Network C are I C MP internet control message protocol igmp internet group management

**[16:04]** protocol IP SEC Internet Protocol security IP version 4 or IP version 6 that is Internet

**[16:12]** Protocol next is transport layer the transport layer is called the host to host transport layer in the

**[16:19]** tcpip model the data communicated by the transport layer is encapsulated in a transport layer pdu and sent in a

**[16:28]** network layer the network clear nodes transfer the transport pdu intact without decoding or

**[16:35]** modifying the content of the pdu in this way only the peer transport entities actually communicate using the

**[16:43]** pdus of the transport protocol it provides services such as connection oriented data stream

**[16:50]** reliability flow control and multiplexing let us discuss them one by

**[16:56]** one number one connection oriented communication it is normally easier for an application to interpret a connection

**[17:04]** as a data stream rather than having to deal with the underlying connectionless models such as the datagram model of the

**[17:11]** user datagram protocol and of the Internet Protocol number two same order

**[17:19]** delivery the network CER doesn't generally guarantee that packet of data will arrive in the same order that they

**[17:26]** were sent but often this is a desirable feature this is usually done through the use of segment numbering with the

**[17:34]** receiver passing them to the application in order number three reliability Packers may be lost during

**[17:43]** the transport due to network congestion and errors by means of an error detection code such as checkum the

**[17:50]** transport protocol May check that the data is not corrupted and verify Crypt reip by sending an act or neack message

**[17:58]** to the sender automatic repeat request schemes may be used to retransmit lost or corrupted

**[18:06]** data number four flow control the rate of data transmission between two nodes must sometimes be

**[18:14]** managed to prevent a fast sender from transmitting more data then can be sported by the receiving data buffer causing a buffer

**[18:23]** overrun this can also be used to improve efficiency by reducing buffer underrun

**[18:30]** number five congestion avoidance congestion control can control traffic entry into a telecommunications

**[18:38]** Network so as to avoid congestive Collapse by attempting to avoid over subscription of any of the processing

**[18:45]** all link capabilities of the intermediate nodes and networks and taking resource reducing steps such as

**[18:52]** reducing the rate of sending packets for example automatic repeat request may keep the n work in a congested State

**[19:01]** 19 minutes, 1 second this situation can be avoided by adding congestion avoidance to the flow control including slow start this keeps the bandwidth

**[19:10]** consumption at a low level in the beginning of the transmission or after packet retransmission and number six is

**[19:19]** multiplexing ports can provide multiple end points on a single node for example the name on a postal address is a kind

**[19:26]** of multiplexing and distinguish ises between different recipients of the same location Computer Applications will each

**[19:35]** listen for information on their own ports which enables the use of more than one network service at the same

**[19:42]** time it is the part of the transport layer in the tcpip model but of the session layer in the Osa

**[19:50]** model let us now learn about two most important protocols at transport layer number one transmission control

**[20:00]** protocol TCP is a connection oriented protocol which means a connection is established and maintained until the

**[20:08]** application programs at each end have finished exchanging messages it determines how to break

**[20:15]** application data into packets that networks can deliver sends packet to and accepts packet from the network CER

**[20:23]** manages flow control and because it is meant to provide error free data transmission handles retransmission of dropped or

**[20:31]** garbed packets as well as acknowledgement of all packets that arrive and second is user datagram protocol the user datagram protocol is a

**[20:40]** transport layer protocol defined for use with the IP network layer protocol it provides a best effort datagram service

**[20:46]** to an end system the service provided by UDP is an unreliable service that provides no guarantees for delivery and

**[20:54]** no protection for duplication the Simplicity of UDP reduces the overhead from using the protocol and the services

**[21:01]** 21 minutes, 1 second may be adequate in many cases UDP provides a minimal unreliable best effort message passing transport to

**[21:08]** applications and upper layer protocols compared to other transport protocols UDP and its UDP light variant are unique

**[21:17]** in that they do not establish endtoend connections between communicating and systems UDP communication consequently

**[21:24]** does not incur connection establishment and tear down overheads and there is minimal Associated end System state

**[21:32]** because of these characteristics UDP can offer a very efficient communication transport to some applications but has no inherent

**[21:40]** congestion control or liability on many platforms applications can send UDP datagrams at the line rate of the link

**[21:48]** interface which is often much greater than the available path capacity and doing so would contribute to congestion

**[21:55]** along the path applications therefore need to be designed responsibly next is session layer the

**[22:04]** session layer provides the mechanism for opening closing and managing a session between end user application

**[22:11]** processes that is a semi-permanent dialogue communication sessions consist of requests and responses that occur

**[22:20]** between applications session layer services are commonly used in application environments that make use of remote procedure calls

**[22:29]** now the services provided by session layer are number one authentication number two

**[22:36]** authorization and number three session restoration the session layer of the USA model is responsible for session

**[22:45]** checkpointing and Recovery it allows information of different streams perhaps originating from different sources to be properly

**[22:53]** combined or synchronized an example usage of the session layer is session beans which are

**[23:00]** only active as long as the session is active and are deleted when the session is disconnected developers can use them

**[23:07]** to store information about the user during a web session an example application is web conferencing in which

**[23:14]** the streams of audio and video must be synchronous to avoid so-called lip sync problems flow control ensures that the

**[23:22]** person displayed on screen is the current Speaker another application is in live TV programs where streams of audio and video need to be seamlessly

**[23:31]** merged and transitioned from one to the other to avoid silent air time or excessive

**[23:38]** overlap next is presentation layer the primary goal of this layer is to take care of the synex and semantics of the

**[23:46]** information exchanged between two communication systems presentation layer takes care that the data is sent in such a way that the receiver will understand

**[23:54]** the information and will be able to use the data language syntax can be different of the two communicating systems under this condition

**[24:03]** presentation layer plays a role translator the various functions of presentation layer are number one translation before being transmitted

**[24:12]** information in the form of characters and numbers should be changed to bit frames the presentation layer is responsible for interoperability between

**[24:20]** encoding methods as different computers use different encoding methods it translates data between the formats the network requires and then the data

**[24:29]** according to the computer number two encryption the presentation layer carries out encryption at the transmitter and decryption at the

**[24:37]** receiver and number three is compression it carries out data compression to reduce the bandwidth of the data to be

**[24:45]** transmitted the primary role of data compression is to reduce the number of bits to be transmitted it is important

**[24:52]** in transmitting multimedia such as audio video text Etc last but not the least is application

**[24:59]** layer it is the topmost layer of OSI model manipulation of data or information in various ways is done in

**[25:07]** this layer which enables user or softwares to get access to the network some Services provided by this layer

**[25:14]** includes email transferring of files Distributing the results to the user directory Services network resources at

**[25:21]** stra various functions provided by application layer are number one mail services this layer provides the basis

**[25:29]** for email forwarding and storage number two Network virtual terminal it allows a user to log onto a remote host the

**[25:37]** application creates software emulation of a terminal at the remote host users computer talks to the software terminal which in turn talks to the host and vice

**[25:46]** versa then the remote host believes it is communicating with one of its own Terminals and allows users to log on

**[25:54]** number three directory services this layer provides access for Global Information about various services and

**[26:01]** 26 minutes, 1 second number four is file transfer access and management it is a standard mechanism to access files and manage it users can

**[26:09]** access files in a remote computer and manage it they can also retrieve files from a remote computer next is the TCP

**[26:16]** IP reference model the TCP IP reference model is the network model used in the current Internet architecture the reference model was named after two of

**[26:24]** its main protocols TCP transmission control protocol and IP that is Internet Protocol the developers choose to build

**[26:33]** a pack switch network based on a connectionless inter Network layer the figure shows various layers of TCP IP reference model let us now briefly

**[26:41]** discuss about the various layers of TCP IP model number one the host to network layer that is physical layer the TCP IP reference model does

**[26:51]** not specify in any great detail the operation of this layer except that the host has to connect to the network using some protocol so it can send IP packets

**[27:00]** over it number two the network layer the job of the network layer is to inject Packers into any network and have them

**[27:08]** travel independently to the destination the layer defines IP for its official packet format and protocol

**[27:16]** packet routing is a major job of this protocol number three the transport layer the transport layer is the

**[27:24]** interface between the application layer and the complex Hardware of the Network it is designed to allow peer

**[27:31]** entities of the source and destination host to carry on conversations data may be user data or Control Data two modes are available

**[27:40]** full duplex and half duplex in full duplex operation both sides can transmit and receive data simultaneously whereas

**[27:48]** in half duplex a site can only send or receive at one time any program running in the

**[27:55]** application layer has the ability to send a message using TCP or UDP which are the two protocols defined for the transport

**[28:04]** layer the application can communicate with the TCP or the UDP service whichever it

**[28:12]** requires both the TCP and UDP communicate with the Internet Protocol in the internet

**[28:20]** layer in all cases communication is a two-way process the applications can

**[28:26]** read and write to the trans transport layer number four the application

**[28:33]** layer the original TCP IP specification described a number of different applications that fit into the top layer of the protocol

**[28:42]** stack these applications include tnet FTP SMTP and

**[28:49]** DNS tnet is a program that supports the tenet protocol over TCP tenet is a general two-way

**[28:57]** communication protocol that can be used to connect to another host and run applications on that host

**[29:05]** remotely FTP that is file transfer protocol is a protocol that was originally designed to promote the sharing of files among computer

**[29:14]** users it Shields the user from the variations of file storage on different architectures and allow for a reliable

**[29:21]** and efficient transfer of data SMTP that is simple male transfer protocol is the protocol used to

**[29:30]** Transport electronic mail from one computer to another through a series of other computers along the

**[29:37]** road DNS domain name system resolves the numerical address of a network node into its textual name or vice

**[29:45]** versa it would translate www.yahoo.com to 204.

**[29:52]** 71177 71 to allow the routing protocols to find the host that the the packet is designed

**[30:00]** for now what are the merits of tcpip number one it operates independently number two it is

**[30:09]** scalable number three client server architecture number four Sports a number of routing

**[30:16]** protocols and number five can be used to establish a connection between two computers next is Dem merits of

**[30:26]** tcpip number number one in this the transport layer does not guarantee delivery of packets number two the model cannot be

**[30:35]** used in any other application number three replacing protocols is not easy and number four it

**[30:43]** has not clearly separated its services interfaces and protocols so with this our today's

**[30:49]** lecture is over concluding this today we learned about the need of protocols and standards also we learned about about

**[30:58]** various protocols at different layers of protocol stack hope you understood today's lecture in the next lecture we'll learn

**[31:05]** about few more concepts of networks and cyber security till then goodbye thank you have a nice day

**[31:13]** [Music]

**[31:28]** n

**[31:34]** [Music]
