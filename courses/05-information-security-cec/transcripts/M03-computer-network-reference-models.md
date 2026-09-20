# Computer Network Reference Models

**Module 03**  
Duration: 26:07  
Video: https://www.youtube.com/watch?v=qpjjzb1yRiM

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr. Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:04]** [Music]

**[0:21]** hello everybody I am Professor yogesh Chaba from Guru jambeshwar University of Science and Technology

**[0:30]** harar harana today in this lecture we will study about computer network

**[0:37]** reference models this lecture on computer network reference models has been divided into three parts basic

**[0:46]** concepts OSI reference model and tcpip reference

**[0:53]** model let us start with computer networks computer network is a collection of auton omous computers

**[1:02]** interconnected by a single technology two computers are set to be interconnected if they are able to

**[1:11]** exchange information the connection between computers can be via a copper wire fiber

**[1:20]** optics microwaves infrared or communication

**[1:26]** satellite there is sometime confusion between a computer network and a distributed system the key distinction

**[1:35]** is that in a distributed system a collection of independent computers

**[1:42]** appear to its users as a single coherent system often a layer of software on the

**[1:52]** top of operating system called middleware is responsible for implementing this model

**[2:00]** a well-known example of a distributed system is the worldwide web in which everything looks

**[2:10]** like a document in computer network different computers are connected

**[2:16]** through single Technology based upon coverage area computer network has been divided into

**[2:26]** four types first is pan that is personal area

**[2:34]** network second is Lan that is local area

**[2:40]** network third is man that is metropolitan area network and last is

**[2:50]** Van that is wide area network let us discuss each of them one

**[2:58]** by one a pan is the interconnection of information technology devices within a

**[3:06]** range of around 10 M connecting a computer to wireless

**[3:12]** keyboard or a mouse or a printer or other computer comes under pan this kind

**[3:21]** of personal area network could also be interconnected with or without wires to

**[3:28]** the internet or or other networks most common pan technology

**[3:35]** available nowadays is Bluetooth Bluetooth uses short range

**[3:41]** radio waves over distances up to approximately 10 m next is local area

**[3:50]** network generally called lens they are privately owned networks within a single

**[3:58]** building or Campus of up to a few kilometers in size they are widely used

**[4:07]** to connect personal computers and workstations in company offices and

**[4:14]** factories to share resources and exchange information lenss are restricted in size

**[4:23]** which means that the worst case transmission time is bounded and known

**[4:30]** in advance various topologies are possible for

**[4:37]** lens figure shows two of them which are bus based and ring based in a bus

**[4:45]** Network as shown in figure a on left side at any instant at most one machine

**[4:54]** is the master and is allowed to transmit the orbit ation mechanism may be

**[5:01]** 5 minutes, 1 second centralized or distributed i e 802.3 popularly called ethernet is a bus

**[5:11]** based broadcast network with decentralized control usually operating

**[5:18]** at 10 Mbps to 10 gbps speed a second

**[5:24]** type of broadcast system is the ring as shown in figure B on the right in a ring

**[5:33]** Network any computer which want to communicate on ring captures a token and starts

**[5:41]** transmission i e 82.5 the token ring is a ring based Lan

**[5:49]** operating at 4 and 16 Mbps speed fddi is another example of a ring

**[5:59]** Network netw next is man that is metropolitan

**[6:05]** area network a network which can cover a city the best known example of a man is

**[6:13]** cable television network available in many cities nowadays YX is also coming

**[6:20]** up which is Wireless man technology a man might look something

**[6:27]** like the system shown in this figure we can see a man network in which both

**[6:34]** television signals and internet is being fed into the centralized headend for

**[6:43]** subsequent distribution to people's homes last type of network is Van that

**[6:51]** is wide area network it spans over a large geographical area maybe a state

**[7:00]** a country or a continent it contains a collection of host intended for running

**[7:08]** user programs the hosts are connected by a communication subnet or just subnet

**[7:17]** for short the hosts are owned by the customers whereas the communication

**[7:24]** subnet is typically owned and operated by a telephone company or Internet

**[7:31]** service provider the job of the subnet is to carry messages from host to host

**[7:39]** just as the telephone system carries words from speaker to

**[7:45]** listener in most wide area networks the subnet consist of two distinct

**[7:52]** components transmission lines and switching elements transmission lines move bits

**[8:00]** between machines they can be made of copper wire optical fiber or even radio

**[8:07]** links switching elements are specialized computers that connect three or more

**[8:14]** transmission lines in Van as shown in figure each host is connected to a lan

**[8:23]** on which a router is present the collection of communication lines and

**[8:30]** routers form the subnet and collection of these lenss through a subnet spread

**[8:37]** across it is is when after discussing types of network

**[8:44]** let us move on to network architecture we will discuss two important Network

**[8:51]** architecture The OSI reference model and the tcpip reference model although the

**[8:59]** protocols associated with the OSI model are rarely used anymore the model itself

**[9:06]** is actually quite journal and still valid the features discussed at each

**[9:13]** layer are still very important the protocols in tcpip reference model are

**[9:20]** very widely used the iso's OSI model is based on a proposal developed by the

**[9:28]** internet national standards organization ISO it is first step towards

**[9:37]** International standardization of the protocols used for communication purpose

**[9:44]** OSI here stands for open system interconnection this model is developed

**[9:52]** by ISO for systems which are open for interconnection

**[10:00]** The OSI model has seven layers the principles that were applied to arrive

**[10:07]** at the seven layers can be briefly summarized as follows a layer should be created where

**[10:16]** a different abstraction is needed each layer should perform a well defined

**[10:25]** function the function of each layer should be chosen with with an eye to word defining internationally

**[10:33]** standardized protocols the layer boundaries should be chosen to minimize the information flow

**[10:40]** across the interfaces the number of layers should be large enough that distinct functions

**[10:49]** need not be thrown together in the same layer keeping in view the reasons given

**[10:58]** OSI reference model is divided into seven layers starting from application

**[11:05]** presentation session transport network data link to physical layer all these

**[11:15]** seven layers are available at both transmitter and receiver side on

**[11:22]** transmitter side data from user is given to application layer it moves M layer by

**[11:30]** layer from application layer to physical layer and then to transmission

**[11:37]** media on receiving side data is received by physical layer from where it is

**[11:44]** passed on layer by layer to application layer user receives the data at

**[11:52]** application layer nomenclature of data units exchanged at each layer

**[11:59]** are shown on figure at physical layer it is a bit at data link layer it is called

**[12:07]** frame at Network layer it is a packet at transport layer it is called tpdu that

**[12:14]** is transport protocol data unit at session layer it is sp duu then at

**[12:22]** presentation layer it is called PP du and at application layer it is called

**[12:31]** AP du another important aspect of this model is that there are two types of

**[12:40]** layers chained layers and end to endend layers lower three layers that is

**[12:47]** network data link physical are called chained layers protocols for chain

**[12:54]** layers are available at intermediate Network device in the network also these Protocols are

**[13:03]** between each machine and its immediate neighbors and not between the ultimate

**[13:10]** source and destination machines which may be separated by many

**[13:18]** routers upper four layers application presentation session and transport are

**[13:25]** called end to endend layers these protocol protols are available only on end to endend

**[13:34]** computers now let us see function of each layer one by one lowermost layer

**[13:41]** that is physical layer is concerned with transmitting raw bits over a Communication channel the design issues

**[13:51]** have to do with making sure that when one side sends a one bit it is received

**[13:58]** by the other side as a one bit not as a zero bit job of physical layer is to

**[14:06]** decide about voltage level of bits timings for each bit modulation technique to be implemented and few

**[14:16]** others the design issues here largely deal with mechanical electrical bit

**[14:23]** timing and the physical transmission medium which lies below the physical

**[14:31]** layer next layer is data link layer the main task of the data link layer is to

**[14:38]** transfer raw bits into a line that appears free of undetected transmission

**[14:46]** errors to the network layer it accomplishes this task by having the

**[14:53]** sender break up the input data into Data frames and transmit the frames

**[15:00]** sequentially if the service is reliable the receiver confirms correct reip of

**[15:07]** each frame by sending back an acknowledgement frame another issue that arises in the

**[15:16]** data link layer is how to keep a fast transmitter from drowning a slow

**[15:24]** receiver some traffic regulation mechanism is often need needed to let the transmitter know how much buffer

**[15:32]** space the receiver has at the moment it's job of this layer to take care of

**[15:39]** flow control broadcast networks have an additional issue in the data link layer

**[15:48]** that is how to control access to the shared Channel a special sublayer of the data

**[15:56]** link layer known as Mac that is medium Access Control sublayer deals with this

**[16:07]** problem the network layer controls the operation of the subnet a key design

**[16:14]** issue is determining how packets are rooted from source to destination if too

**[16:22]** many packets are present in the subnet at the same time they will get in one another way forming

**[16:31]** bottlenecks the control of such congestion also belong to the network layer addressing is also job of network

**[16:40]** layer more generally the quality of service provided is also a network layer

**[16:47]** issue moving on to the transport layer the basic function of the transport

**[16:53]** layer is to accept data from above layer split it into two smaller units if need

**[17:01]** 17 minutes, 1 second be pass these to the network layer and ensure that the pieces all arrive

**[17:08]** correctly at the other end the transport layer also determines what type of

**[17:16]** service to provide to the session layer and ultimately to the users of the

**[17:24]** network the transport layer is a true end to endend layer all the way from the source to the

**[17:33]** destination in other words a program on the source machine carries on a conversation with a similar program on

**[17:42]** the destination machine the session layer allows users

**[17:49]** on different machines to establish sessions between them sessions offer

**[17:56]** various services including dialog control token management to prevent two parties from attempting the

**[18:05]** same critical operation at the same time and synchronization next layer is the

**[18:13]** presentation layer unlike lower layers which are mostly concerned with moving

**[18:20]** bits around the presentation layer is concerned with syntax and semantics of

**[18:27]** the information transmiss it also take care of encoding and decoding of

**[18:34]** data last layer that is application layer contains a variety of protocols

**[18:41]** that are commonly needed by users application layer protocols provides

**[18:48]** interface to the user one widely used application protocol is

**[18:55]** HTTP that is hyper text transfer protocol which is the basis for the

**[19:02]** worldwide web other application Protocols are for file transfer

**[19:08]** electronic mail and network news so this was iso's OSI reference model now let us

**[19:18]** see the TCP IP reference model the TCP IP reference model is the network model

**[19:26]** used in the current Internet AR architecture it has its origin back in

**[19:33]** 1960s with the grandfather of the internet the arpanet this was a research Network

**[19:41]** sponsored by the Department of Defense in the United States the major design

**[19:48]** goals of tcpip reference model were ability to connect multiple

**[19:55]** networks together seamlessly ability for connections to remain intact

**[20:02]** as long as the source and destination machines were functioning to be built on flexible

**[20:10]** architecture the reference model was named after two of its main protocols TCP that is transmission control

**[20:19]** protocol and IP that is Internet Protocol there are four layers in TCP IP

**[20:28]** reference model model as compared to 7 in OSI reference model host to network

**[20:35]** layer performs the jobs of data link layer and physical layer of OSI

**[20:41]** reference model internet layer is same as Network layer in OSI reference model

**[20:49]** for session and transport layer in OSI reference model there is only one layer that is named as transport layer in

**[20:58]** tcpip reference model similarly for application and presentation there is application

**[21:06]** layer different protocols and networks in the initial version of TCP IP models

**[21:14]** are as shown in figure at Host to network layer there is arpanet setet

**[21:22]** Packet radio and Lan at Network layer there is IP

**[21:28]** protocol that is Internet Protocol its job is to take care of routing

**[21:35]** addressing and congestion control at transport layer there is TCP and UDP TCP

**[21:45]** is reliable connection oriented and UDP is unreliable connectionless service

**[21:53]** their job is endtoend connectivity and flow control between and

**[22:01]** 22 minutes, 1 second users on top of Transport layer is the application layer it contains all the

**[22:08]** higher level protocols the early ones included virtual terminal tet file transfer

**[22:16]** protocol FTP and electronic mail protocol SMTP many other protocols have been

**[22:25]** added to these over the years like like the domain name system DNS for mapping

**[22:33]** host names onto their Network addresses mntp the protocol for moving

**[22:40]** uset news articles around and HTTP the protocol for fetching pages on the

**[22:48]** worldwide web and many others The OSI and tcpip reference

**[22:56]** models have much in common both are based on the concept of a stack

**[23:03]** of independent protocols also the functionality of layers is roughly

**[23:09]** similar for example in both models the layer provide an endtoend Network

**[23:17]** independent Transport service to processes wishing to communicate again

**[23:25]** in both models the layers about trans Port are application oriented users of

**[23:32]** the transport service despite these fundamental similarities the two models

**[23:39]** also have many differences The OSI model completes the job using seven layers whereas tcpip

**[23:49]** model has only four layers the tcpip model did not originally clearly

**[23:56]** distinguish between service interface and protocol whereas OSI model does

**[24:05]** so another difference is in the area of connectionless versus connection oriented

**[24:13]** communication The OSI model supports both connectionless and connection

**[24:20]** oriented communication in the network layer but only connection oriented

**[24:26]** communication in the transport layer but the TCP IP model has only connectionless

**[24:34]** mode in the network layer but supports both modes in the transport layer giving

**[24:41]** the user a choice so dear friends today in this lecture we have covered

**[24:48]** introductory concepts of computer networks followed by two very important

**[24:55]** reference models OSI and tcpip in last we have also seen

**[25:03]** comparison of these two models thank you

**[25:09]** [Music]
