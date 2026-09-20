# Medium Access Control Protocols

**Module 08**  
Duration: 26:29  
Video: https://www.youtube.com/watch?v=Yw1HsIBvLLM

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr. Maninder Singh, Department of Computer Science, Punjabi University, Patiala

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** science Punjabi University patella today's lecture is on Mac protocols in this lecture we are going

**[0:07]** to discuss in detail about the working and Protocols of medium access sublayer of OSI model now let's

**[0:16]** start the medium access sublayer is the bottom part of data link layer the medium access sub layer is also known as

**[0:24]** Mac that is Media Access Control sublay when a common medium is shared by many stations Mac lab plays a very important

**[0:33]** role without this control several stations transmitting simultaneously could produce gobbled messages the media

**[0:41]** Access Control mechanism standardized by i e are implemented in the max sublayer of the data link layer it provides

**[0:49]** service to the LLC logical link control sublayer and receives service from the physical layer below it the basic

**[0:58]** functions of Max sublayer is the media Access Control error detection and station addressing media Access Control

**[1:06]** procedures are implemented to ensure that every station gets a fair chance to transmit and collisions do not take

**[1:14]** place there are several methods of media Access Control in lands and each method is applicable to specific land topology

**[1:23]** in addition to the basic access procedures the Mac layer also handles the frame D limiting address recognition

**[1:31]** and error checking functions when a number of user stations share a single transmission medium this is called a

**[1:38]** multiple access communication the transmission medium is broadcast in nature so all other

**[1:45]** attached stations to the medium can receive the transmission From Any Given station the physical transmission medium

**[1:53]** of a land is shared by the stations connected on the land let's see how media is

**[2:01]** 2 minutes, 1 second shared the two basic approaches to medium Access Control are static and dynamic access control or in other words

**[2:09]** it is called Static Channel allocation and dynamic Channel allocation the dynamic access control is further

**[2:15]** categorized into random access and scheduling the figure here shows various techniques for sharing a transmission

**[2:24]** medium first we'll talk about static Channel allocation in land number of computers are working and only one

**[2:31]** computer is allowed to broadcast on the communication channel the first method of allocating a single Communication

**[2:38]** channel among multiple contending users is by using frequency division multiplexing that is

**[2:45]** fdm if there are n number of users the entire bandwidth is divided into n equal

**[2:52]** partitions and each user is allocated one partition since each user has been allocated a fixed frequency band

**[3:01]** 3 minutes, 1 second therefore interference between them is avoided but this scheme is applicable only when number of users are less and

**[3:11]** each has constant traffic when number of users in the land is large with constantly waiting traffic then the

**[3:19]** bandwidth is divided equally into n partitions if the number of users is less than n than a significant portion

**[3:26]** of frequency spectrum is wasted but if the number of users is greater than n then some of them will not get a

**[3:34]** frequency Channel due to shortage of bandwidth in this case channel is set to be inefficient if all the users who want

**[3:43]** to communicate are arranged in one q and number of users are n then the average

**[3:50]** delay T will be n times the meantime delay the static fdm exhibits poor

**[3:57]** performance of Channel next method of Channel allocation is dynamic Channel allocation Dynamic

**[4:04]** Channel allocation method is included in all lands and vans Dynamic Chanel allocation method is able to handle all

**[4:13]** the different types of traffic conditions an order is built up among the Stations of the land so that proper

**[4:20]** chance is given to each station to transmit its data frames but for this some requirements are to be satisfied by

**[4:28]** the land first requirement is that the workstations or terminals are independent and work is generated at a

**[4:36]** constant rate second requirement is that a single channel is available for all communication all stations can transmit

**[4:45]** and receive through it third requirement is that the workstation can begin signal transmission at any time or in a slotted

**[4:55]** time assigned to it fourth requirement is that if two stations are transmitting simultaneously the signals collide with

**[5:03]** each other and resulting signal is gobbled this process is called Collision this Collision can be detected

**[5:11]** by all the other stations the collided signal may be retransmitted the last requirement is that stations can have

**[5:20]** either carrier sensing or not carrier sensing is a specific electrical signal on the network sensing of carrier gives

**[5:29]** the status of the channel That is busy or free next we are going to discuss multiple access

**[5:38]** protocols one feature of Lan is that its backbone is a shared Channel or transmission link which provides all

**[5:46]** users to access the transmission facilities it may happen that two or more stations transmitting data at the

**[5:54]** same time causing their signals to interfere and data gets gobbled so in order to resolve these type of conflicts

**[6:02]** a number of different medium access protocols have been developed in order to handle the bursty nature of land

**[6:10]** burstiness means the data is transmitted irregularly in bursts rather than as continuous streams traffic asynchronous

**[6:19]** stedium is used the asynchronous stedum mechanism is further divided into two methods

**[6:26]** contention method or Random Access method method and deterministic Method or they are also called as controlled

**[6:34]** methods Random Access techniques are Aloha carrier sense multiple xes or

**[6:41]** csma then csma with Collision detection which is also called csms CD and the last one is register insertion it is not

**[6:50]** very popular and is obsolete controlled access to landan can be performed in two types centralized or

**[6:59]** distribute it in centralized technique Master node decides which node is to access the channel at any point of time

**[7:07]** for example polling in distributor technique each station is given an opportunity to transmit on the channel

**[7:14]** for example token passing method and slotted ring method this figure illustrates the

**[7:22]** typical multiple Access Communications where a number of user stations share a transmission medium

**[7:30]** this sharing techniques are used both in wired and wireless communication networks in wired communication

**[7:38]** multi-drop cables are used in data networks to connect number of stations to a host computer the host computer

**[7:46]** broadcasts information to the users on the outbound line the stations transmit information to the host using the

**[7:55]** inbound line this system is shown in this figure a medium access control or Mac protocol

**[8:04]** is developed for the system here the host computer issues polling messages to each stations providing it with

**[8:13]** permission to transmit on the inbound line in radio communication several stations share two frequency bands one

**[8:22]** for transmitting and one for receiving in Satellite Communications each station is assigned a channel in an Uplink

**[8:30]** frequency band that it uses to transmit to the satellite the satellite sends

**[8:37]** back the signals on different frequency band called down link frequency

**[8:43]** band first technique is Aloha the Aloha protocol is a contention

**[8:51]** protocol which was developed at the University of Hawaii in early 1970s and was originally developed for packet

**[9:00]** Radio Networks however it is applicable to any shared transmission medium in a system

**[9:08]** when many users try to send messages to each other using a common broadcast channel Random Access or contention

**[9:16]** techniques are used Random Access means there is no exact time for any station to transmit data this scheme is very

**[9:24]** simple and is asynchronous it is asynchronous because there is no proper coordination among the transmitting

**[9:32]** stations the basic idea of Aloha system is useful to any system in which coordinated stations are competing for

**[9:41]** the use of a single shared Channel when a station sends data another station may

**[9:48]** try to do so at the same time the data from the two stations May Collide and get scbl if there is a collision then

**[9:56]** each station would simply wait for a random period of time before try again the Aloha system is of two types Pure

**[10:05]** Aloha which does not require Global time synchronization and slotted loha which

**[10:12]** requires time synchronization will first discuss Pure Aloha the original Aloha protocol is

**[10:21]** called Pure Aloha in this the whole idea is that each station can send a frame

**[10:28]** whenever it has a frame to send as there is only one channel available to share there is the possibility of collision

**[10:36]** between frames from different stations the Pure Aloha protocol depends upon acknowledgement from the receiver when a

**[10:44]** user sends a frame it expects the receiver to send an acknowledgement if the acknowledgement does not reach the

**[10:52]** transmitter after the timeout period the station assumes that the frame has been destroyed

**[11:00]** and resends the frame the figure shows the frame collisions in Pure Aloha as you can see when two frames are

**[11:09]** transmitted at the same time there will be a collision and both will be gobbled if the first bit of a new frame overlaps

**[11:18]** with just the last bit of a frame almost finished then both the frames will be completely destroyed and both will have

**[11:26]** to be retransmitted again after the time of period if all the stations try to resend their frames after the timeout the

**[11:35]** frames will collide again Pure Aloha dictates that when the timeout period passes each user Waits a

**[11:45]** random amount of time before resending its frame the randomness will help to avoid more collisions this time is

**[11:53]** called as back of time TB the timeout period is equal to the maximum possible roundtrip propagation

**[12:02]** delay which is twice the amount of the time required to send a frame between

**[12:08]** the two most widely separated stations 2 into TP let all the packets have the same

**[12:17]** length and each station requires one time unit for transmission which is TP

**[12:24]** consider any user to send packet a at the time T not if any other user B has

**[12:31]** generated a packet between time T not and T not plus TP the end of a packet B

**[12:40]** will collide with the beginning of packet a since in P Aloha packet a station does not listen to the channel

**[12:48]** before transmitting it has no way of knowing that above frame was already

**[12:56]** underway this figure shows what vable periods during which packets can

**[13:03]** Collide similarly if another user wants to transmit between t plus TP and t + 2

**[13:12]** TP that is Packet C the beginning of packet c will collide with the end of

**[13:19]** packet a thus if two packets overlap by even the smallest amount of the

**[13:27]** vulnerable period both packets will be corrupted and need to be retransmitted let's calculate the throughput of Pure

**[13:36]** Aloha channel the throughput S of Pure Aloha is defined as an average successful traffic

**[13:45]** transmitted between the stations per unit time the unit of time is slot time

**[13:52]** which is the time required to transmit a frame assuming all frames or packets are

**[13:59]** of same size since only one packet per slot can be transmitted the maximum value of

**[14:07]** ss1 when collisions happen some of the packets are lost and part of available Channel time is wasted the resulting

**[14:16]** value of s is less than one to find the throughput of transmission Channel

**[14:23]** suppose the probability PK that K packets are generated during a given slot time follows a poison distribution

**[14:32]** with the mean G per packet time is given by this equation the throughput S is then just

**[14:40]** the offered load G times the probability of a transmission being successful s is

**[14:47]** equal to G P where p is equal to probability that a packet does not suffer a

**[14:55]** collision the probability of no other traffic being initiated during the entire vulnerable period is thus given

**[15:04]** by P is equal to e raed to the power minus 2 G therefore throughput s is equal to G

**[15:12]** multiplies e the^ minus 2G the maximum throughput occurs at when G is equal

**[15:22]** to.5 therefore for Pure Aloha the best Channel utilization that can be achieved is around

**[15:31]** 18% no synchronization is required for Aloha each station can transmit a packet

**[15:38]** whenever it has one the disadvantage of this scheme is that it is inefficient because the maximum Channel utilization

**[15:46]** is only 18% of the total available capacity next is slotted Aloha in

**[15:55]** slotted Aloha the total Channel time is divided into dis three time slots and the stations can transmit only at

**[16:03]** specific instance of time these time slots are exactly equal to the packet transmission time all stations are then

**[16:11]** synchronized to these time slots so that whenever a station has a packet it must synchronize exactly with the next

**[16:20]** possible time slot the benefit of this scheme is that the wasted time due to collisions can be reduced to one packet

**[16:28]** time or we can say that vulnerable period is reduced to half transmission attempts for four Network users and

**[16:36]** random retransmission delays for colliding packets in slaughtered loha are shown in this

**[16:44]** figure there are few assumptions in case of slaughtered loha all the frames are of the same size

**[16:52]** time is divided into equal size slots a slot equals the time to transmit one

**[16:59]** frame nodes start to transmit frames only at the beginning of a slot nodes are synchronized if two or more nodes

**[17:08]** transmit in a slot all nodes detect Collision before the slot ends let's discuss the throughput of slotted Aloha

**[17:17]** channel in slotted Aloha the packets arrive in a synchronized fashion the probability of single transmission

**[17:25]** during a slot time is p not is equal to e to the power minus G therefore

**[17:31]** throughput s is equal to G multiplied with e ra to power minus G the maximum throughput occurs at G equal to 1 which

**[17:40]** is twice that of Pure Aloha this means that the best Channel utilization that can be achieved is around

**[17:50]** 36.8% next technique is Carrier sense multiple AIS that is csma Carrier sense multiple AIS is a

**[17:59]** probabilistic media Access Control protocol in which a station confirms the absence of other traffic before

**[18:08]** transmitting a data on a shared transmission medium carrier sense means that a transmitting station tries to find out whether another transmission is

**[18:17]** in progress before starting a transmission that is it tries to identify the presence of a carrier

**[18:24]** signal from another station before starting to transmit if if a station senses a carrier the station waits for

**[18:32]** the transmission in progress to finish before starting its own Transmission in other words csma scheme is based on the

**[18:40]** principle of sense before transmit or listen before talk multiple access means that more than one stations may send and

**[18:49]** receive on the shared transmission medium the vulnerable time for csma is the propagation time TP the propag ation

**[18:59]** time is the time required for a packet to propagate from one end to the other end of the medium now look at this

**[19:07]** figure in which station a transmits a frame at time T1 which reaches the rightmost station D at time T1 + TP this

**[19:17]** figure shows the vulnerable time for csma when a station senses the medium to

**[19:24]** be idle it transmits the packet by using one of these approaches nonpersistent csma one persistent csma

**[19:33]** and P persistent csma nonpersistent csma is a non-aggressive transmission protocol

**[19:40]** when the transmitting station has a data to transmit it first senses the medium if the medium is Idle then it transmits

**[19:48]** the data immediately but if the medium is busy then it waits for a random period of time during which it does not

**[19:55]** sense the transmission medium before repeating the whole process that is sensing the transmission medium for idle

**[20:03]** or busy again this scheme reduces the collisions and which results in higher medium

**[20:11]** throughput next is one persistent csma one persistent csma is an aggressive

**[20:18]** transmission algorithm when the transmitting station is ready to transmit data it senses the medium for

**[20:24]** idle or busy if the medium is Idle then it transmits the data immediately but if the medium is busy then the station

**[20:32]** senses the medium continuously until it becomes idle then it transmits the message unconditionally that is with

**[20:40]** probability equals to 1 in case of any Collision the sender waits for a random period of time and attempts to transmit

**[20:48]** again unconditionally that is with probability equals to 1 one persistent csme is used in CSM CD systems including

**[20:58]** it ethernet next is p persistent CSM this is an approach

**[21:05]** between non-persistent and one persistent csma access schemes when the transmitting station has a data to

**[21:12]** transmit it then senses the transmission medium for idle or busy if the medium is Idle then it transmits the data

**[21:20]** immediately but if the medium is busy then it senses the medium continuously until it becomes idle then transmits a

**[21:28]** data frame with probability P if the station does not transmit data frame that is the probability of this event is

**[21:37]** 1 minus P then it waits until the next available time slot P persistent csma is

**[21:44]** used in CS smca systems including Wi-Fi and other packet Radio Systems next technique is Carrier sense

**[21:53]** multiple aess with Collision detection that is CSM CD carrier sense multiple access with

**[22:00]** Collision detection is a media access control method used mostly in lens which are using early ethernet technology it

**[22:10]** uses a carrier sensing technology in which a transmitting station detects other signals in the medium while

**[22:18]** transmitting a frame and stops transmitting that frame transmits a jamming signal in case of collisions and

**[22:26]** then waits for a random period of time time before trying to resend the frame csms CD is a modification of pure

**[22:35]** carrier sense multiple access that is CSM scheme CSM CD is used to improve csma performance by terminating

**[22:44]** transmission as soon as Collision is detected the base protocol is that a station with a message to send must

**[22:52]** monitor the channel to see if any other station is sending if another station is sending the second station must wait or

**[23:01]** 23 minutes, 1 second defer until the sending station has finished then it may send its message if no station was sending at the time that

**[23:10]** it first listened the station may send its message immediately the term carrier sensing

**[23:17]** indicates this listening before transmitting Behavior if two or more stations have messages to send at the

**[23:25]** same time and they are separated by a significant distance is on the bus each May begin transmitting at roughly the

**[23:33]** same time without being aware of the other station the signals from each station will superimpose on the channel

**[23:42]** and is gobbled beyond the decoding ability of the receiving station this is termed as Collision let's discuss

**[23:51]** Collision detection procedure in csms the following procedure is used to resolve a detected Collision

**[23:59]** the procedure is complete when retransmission is initiated or the retransmission is aborted due to

**[24:07]** numerous collisions continue transmission with a jam signal instead

**[24:13]** of frame header data or CRC until minimum packet time is reached to ensure

**[24:20]** that all receivers detect the Collision increment re transmission counter was the maximum number of

**[24:29]** transmission attempts reached if so about transmission calculate and wait random

**[24:36]** back of period based on number of collisions re-enter main procedure at stage

**[24:45]** one because of quick termination of transmission time and bandwidth is saved therefore CSM CD is more efficient

**[24:53]** than Aloha slotted Aloha and csma CSM CD Network Works work best on bus

**[25:01]** 25 minutes, 1 second multi-point topology with busty asynchronous transmission all stations are attached to One path and monitor the

**[25:09]** signal on the channel through transceiver attached to the cable csmd has totally decentralized control and is

**[25:16]** based on contention access csms CD supports both baseband and broadband system csmd offers four options in terms

**[25:26]** of bit rate signaling method and maximum electrical cable segment length these

**[25:32]** are 10 Bas 5 10 Bas 2 10 broad 36 and 1 base 5 the numeric field in the

**[25:42]** beginning indicates the bit rate in MVPs the middle term indicates the type

**[25:49]** of signaling system that is baseband or Broadband the numeric field in the end indicates the electrical cable segment

**[25:56]** length in multi of 100 m Manchester signal code is used at the basement

**[26:03]** level of transmission in Broadband transmission different phase shift keying is used to convert the Manchester

**[26:11]** encoded signal into analog form so friends this was all about Mac

**[26:17]** Subler and Mac protocols hope all the concepts are clear to you hope to see you in the next lecture till then

**[26:26]** goodbye thank you
