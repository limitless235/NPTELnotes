# Data Link Layer

**Module 07**  
Duration: 22:39  
Video: https://www.youtube.com/watch?v=u9QZrz8pG6A

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr. Maninder Singh, Department of Computer Science, Punjabi University, Patiala

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** sing from Department of computer science Punjabi University patala today's lecture is on data link layer in this

**[0:07]** lecture I'll explain you the working of second layer of OSI reference model that

**[0:13]** is data link layer now let's start in the Osa reference model the layer which

**[0:20]** is directly on top of physical layer is the data link layer or also called dll the dll is also named as Layer Two or of

**[0:30]** the OSI model data link layer is one of the most complex layers and has difficult functionalities and

**[0:37]** responsibilities this layer hides the particulars of underlying hardware and depicts itself to Upper layers as the

**[0:46]** channel to communicate data link lir works between two communicating hosts which are connected directly in some

**[0:54]** sense this direct connection may possibly be broadcast or point to point systems on broadcast network are

**[1:02]** supposed to be on same link the work of data link layer becomes more difficult when it is dealing with several hosts on

**[1:11]** single collision domain data link layer converts the incoming data stream into signals bit by bit and to send it over

**[1:19]** the underlying Hardware at the receiving end data link lay collects the data from underlying Hardware which is in the form

**[1:27]** of electrical signals build them in an identifiable frame format and pass it over to upper layer data link layer has

**[1:35]** two sub layers logical link control and media Access Control logical link control also called

**[1:44]** LLC this sublayer is needed in the case of Point topoint links only it deals with protocols flow control and error

**[1:52]** control media access control the Mac sublayer is in charge of deciding which

**[1:59]** user get to use the broadcast medium at any particular time dll protocols can be implemented either in Hardware or

**[2:08]** software they can be implemented in either a computer's main CPU or in special purpose Hardware known as

**[2:16]** network adapter or network interface card n i a common example of the later case is

**[2:24]** an Ethernet Nic data link lay performs many functions on behalf of upper layer the first function is framing data link

**[2:33]** layer receives packets from Network layer and encapsulates them into frames the next function is addressing the data

**[2:41]** link layer provides layer to Hardware addressing system Hardware address is supposed to be unique and is encoded

**[2:50]** into Hardware at the time of manufacturing the third function is error control sometimes during

**[2:57]** transmission signals May encounter problem and the bit get flipped so the detection of errors and recovery of

**[3:05]** original data is done by this layer the next function is flow control stations present on same link may have different

**[3:13]** speeds data link lay provides flow control that allows both sender and receiver to exchange data at same speed

**[3:22]** the last function is multiaxis when host on the shared link tries to transfer the data it has a high probability of

**[3:31]** collision data link lab provides mechanisms such as csms CD to equip capability of accessing a shared media

**[3:40]** among multiple systems next we are going to discuss the first function of data link layer that is framing the major

**[3:48]** responsibility of data link layer is to make physical link reliable and to do so

**[3:54]** it breaks the network layer data stream into small blocks this process is called segmentation and in order to form a

**[4:03]** frame it adds header and frame flag to each and every block and this process is

**[4:10]** called encapsulation header of the frame generally contains three Fields the first field is address field which

**[4:18]** contains the address of sender and receiver the second field is error detecting code where a check Sim of the

**[4:27]** frame for error detection is stored the Third Field is control field which stores the additional information to

**[4:34]** implement protocol functions the receiving data link layer must know the start and the end of a frame according

**[4:42]** to the frame flag a good design must make it easy for a receiver to find the start of a new frame while using little

**[4:52]** of the channel bandwidth we are now going to look at four of the framing methods the first method is by count

**[5:00]** this framing method uses a field in the header to describe the number of bytes present in the frame when the receiver's

**[5:08]** data link layer sees this count it comes to know how many bytes to follow the next method is flag bytes

**[5:16]** with bite stuffing in this case each frame starts and ends with special bite sequence generally same bite also called

**[5:25]** a flag bite is used as starting and ending D limiter and this bite sequence is shown in figure as

**[5:34]** flag sometimes it may happen that the flag bite is present in the data then in

**[5:41]** order to solve this problem the sender's data link layer inserts a special bite known as ESC or Escape bite immediately

**[5:51]** before each accidental flag bite in the data this technique is known as bite stuffing the third method is flag bits

**[6:01]** 6 minutes, 1 second with bit stuffing as we know that frame flag is a special bit pattern which should not be present any other place

**[6:08]** inside a frame if a special frame flag of 0 6 * 1 0 is used at the start and

**[6:17]** end of the frame and whenever a senders dlc's five consecutive ones in the data then it automatically adds zero after

**[6:25]** five consecutive ones and receiver deletes this Z bit that follows five consecutive one bits in the received data this process is

**[6:35]** called bit stuffing the last method is physical layer coding violations this framing method is used in those networks

**[6:43]** in which the encoding on the physical medium contains some redundancy some lens encode each bit using two physical

**[6:53]** bits and Manchester coding is normally used in this case the one bit is and Ed

**[6:59]** using one0 and 0 bit is encoded using 01 this type of invalid physical code is

**[7:06]** used in 802 lens standards next is flow control modern networks are aimed to support a wide variety of hosts and

**[7:15]** communication mediums suppose a 200 MHz Pentium based host wants to transmit a

**[7:20]** data to 25 MHz based 80386 host naturally the faster Pentium will drone

**[7:28]** the slower 8038 six with data similarly consider Two Hosts and both of them

**[7:35]** using an ethernet land but with the two ethernet connected by a 28.8 kbps model

**[7:42]** link if one host starts transmitting to the other host at ethernet speeds then in this case the model link will quickly

**[7:51]** become overburdened in both of these cases flow control is required to speed the data transfer at suitable rate

**[8:00]** flow control is a technique that informs the sender the amount of data it can transfer before it should

**[8:07]** wait for an acknowledgement from the receiver the flow of data from sender to receiver should not be allowed to

**[8:14]** overburden the receiver receiver must also be able to report to the transmitter before its limits are

**[8:22]** reached and the sender should send less number of frames the limit May well be amount of memory used in order to to

**[8:29]** store the incoming frames or the processing power of receiver the two methods developed for flow control are

**[8:37]** stop and weight and sliding window first we'll discuss stop and weight stop and weight is the simplest form of flow

**[8:45]** control in which a sender transmits a data frame after receiving the data frame the receiver indicates its

**[8:52]** keenness to accept another frame by sending back an acknowledgement frame acknowledging the frame received earlier

**[9:02]** the sender must wait until AK frame is received by it before transmitting the next frame this is also referred to as a

**[9:11]** request reply mechanism which is very easy to understand and implement but not very

**[9:17]** efficient in lens with fast links this is not a major concern but van links will spend most of their time staying

**[9:25]** idle especially if a large number of hops are required figure here shows the working of the

**[9:32]** Stop and waight protocol the blue arrows indicate the sequence of data frames being sent over the link from sender to

**[9:42]** the receiver the protocol depends on two-way transmission either half or full duplex to allow the receiver to return

**[9:50]** acknowledgement frames acknowledging the successful transmission the acknowledgements are shown in green

**[9:56]** color in this diagram which move back to the original sender a small processing delay is introduced between the

**[10:05]** reception of the last data frame and the generation of the acknowledgement major drawbacks of this

**[10:12]** scheme is that only one frame can be transmitted at a time and this leads to inefficiency in the performance if

**[10:21]** propagation delays longer than the transmission delay next we'll calculate the link utilization in stop and waight

**[10:28]** protocol call let's assume the few things the first is transmission time it is the time taken by a station to

**[10:37]** transmit a data frame normalized to a value of one and the second is propagation delay it is a Time taken by

**[10:45]** a bit to travel from sender to receiver expressed as a if the value of a is less

**[10:52]** than one the frame is sufficiently long such that the first bit of the frame arrive at the destination before the

**[10:59]** source has completed transmission of the frame if a is greater than one send a completes transmission of the entire

**[11:08]** frame before the leading bits of the frame arrive at the receiver the link utilization U is equal to 1 by 1 + 2 a

**[11:17]** where a is equal to propagation time divided by transmission time it is clear from this equation that the link

**[11:26]** utilization is strongly dependent on the ratio of the propagation time to the transmission time when the propagation

**[11:34]** time is very small as it happens in case of lands the link utilization is good but when the propagation delays are very

**[11:42]** long in case of uh Satellite Communication the link utilization can become very poor so to improve the link

**[11:52]** utilization we can use sliding window protocol instead of using stop and weight protocol the next method of flow

**[12:00]** control is sliding window the simple stop and weight protocol does not work well if multiple data frames are used

**[12:08]** for single message only one data frame can be in transmission mode at a time in stop and weight protocol if a is greater

**[12:17]** than one severe inefficiencies result efficiency of the protocol can be improved if multiple frames are

**[12:24]** transmitted at the same time and also by using the full duplex line the sending station keep track on the

**[12:32]** frames by transmitting sequentially numbered frames the sequence number should be of limited size because it

**[12:40]** occupies a field in the data frame if there are K bits in the header of the data frame then the range of the

**[12:47]** sequence numbers must be from 0 to 2K minus 1 sender keeps a list of sequence

**[12:55]** numbers that it is authorized to send and this list is is called a sender window the maximum size of the sender's

**[13:02]** window is 2K minus1 the sender is allocated above a space equal to the window size receiver also keeps a window

**[13:11]** called a receiver window of size 2K minus1 the receiver acknowledges every frame by sending back

**[13:18]** an acknowledgement frame which includes the sequence number of the expected next frame this also makes a public

**[13:27]** announcement that the receiver is ready to receive the next end frames starting with the specified

**[13:34]** number this scheme is used to acknowledge multiple frames sliding window algorithm provides a flow control

**[13:42]** for network data transfers TCP protocol uses a sliding window protocol a buffer is placed between the application

**[13:50]** program and network data flow by the sliding window protocol for TCP the buffer is normally present in the kernel

**[13:58]** of the operating system the data which is received from the network gets stored in the buffer

**[14:05]** space from where the application can read data at its own speed as the data

**[14:13]** is read by the application buffer space gets empty and is ready to accept more data from the network now we are going

**[14:21]** to discuss the sender and receiver sliding windows at any point of time the sender is allowed to transmit frames

**[14:29]** with sequence numbers in a particular range the center window as shown in the figure here the next is receiver sliding

**[14:39]** window the receiver keeps a window of size one if receiver sees that frame should arrive in a particular order if

**[14:48]** frames are received out of order then it is discarded and needs to be recent however the receiver window increased by

**[14:57]** one if a particular frame is received the frame is acknowledged by sending back an AK frame which includes uh the

**[15:07]** sequence number of the next frame this also openly announces that it is ready to receive the next end frames starting

**[15:16]** with the specified number this scheme can also be used to acknowledge multiple frames sliding window is beneficial if

**[15:24]** local application processes data at the same rate at which it is being transferred if packet size is smaller

**[15:32]** than the window size then multiple packets can be present in the network because the sender knows that the space

**[15:39]** exists on the receiver site to store all the packets ideally steady state can be

**[15:45]** attained where a number of packets in the forward Direction and window announcements in the reverse direction

**[15:53]** are constantly in traveling when the sender receives new window announcement it transmits more data packets and when

**[16:02]** data from the buffer is read by the application more window announcements are generated maintaining a sequence of

**[16:09]** data packets during transfer guarantees the effective use of network resources third function that is error control of

**[16:18]** data link layer when the receiver detects an error in the message or packet it then informs the sender to retransmit the particular message or

**[16:27]** packet the most most popular retransmission scheme is known as automatic repeat request or

**[16:35]** arq the three well-known erq techniques are stop and wait arq go back and erq

**[16:42]** and selective repeat arq first we will discuss stop and weight arq stop and weight arq is the simplest protocol

**[16:51]** among all the protocols in which the sender sends a frame and then it waits till a positive acknowledgement or

**[16:58]** negative acknowledgement is received from the receiver the receiver sends a positive acknowledgement only if the

**[17:06]** frame is received correctly or else it sends back negative acknowledgement the sender sends a new frame only after

**[17:15]** receiving positive acknowledgement otherwise it retransmits the old frame if negative acknowledgement is received

**[17:23]** this is Illustrated in the figure here to deal with the issue of a lost or damag frame the sender is provided with

**[17:30]** the timer if acknowledgement is lost the sender transmits the old frame in the

**[17:38]** figure the second pdu of data is lost during transmission the sender does not know about this loss but starts a timer

**[17:47]** after transmitting each pdu generally a positive acknowledgement pdu is received before the timer

**[17:54]** expires in this case no acknowledgement is received and and the timer counts down to zero and retransmission of the

**[18:02]** same pdu is initiated by the sender the sender always starts a timer immediately after transmitting a pdu but the second

**[18:10]** transmission receives an acknowledgement pdu before the timer expires finally indicating that the data has now been

**[18:19]** received by the remote node as the duplicate frame is received by the receiver therefore it is

**[18:26]** discarded the receiver now can identify that it has received a duplicate frame

**[18:33]** from the label of the frame and it is discarded to address the issue of lost or damaged frames for example a frame

**[18:41]** gets corrupted due to noise during the transmission and there is a concept of negative acknowledgement frames the

**[18:50]** receiver sends back a negative acknowledgement frame to the sender if it founds that the received frame is corrupted when a transmitter receives a

**[18:59]** negative acknowledgement frame before the timeout of the timer the old frame is transmitted again as shown in the

**[19:06]** figure the major advantage of stop and weight erq is its Simplicity it also requires minimum buffer size however it

**[19:15]** makes highly inefficient use of communication links particularly when propagation delay is large second arq

**[19:22]** scheme is go backen arq go backen is one of the most popular arq in which which the sender transmits the frames

**[19:31]** continuously without even waiting for acknowledgement that is why this protocol is called as continuous arq

**[19:39]** when the frame is received by the receiver it continues to send acknowledgments or negative acknowledgements back to the sender if

**[19:47]** negative acknowledgement frame is received by the sender it retransmits the frame including all the successive frames as shown in the figure therefore

**[19:57]** this protocol is called go n erq if a frame is lost during transmission then the receiver sends negative

**[20:05]** acknowledgement frame if there is a long delay in sending the N frame the sender will retransmits the Lost frame after

**[20:14]** its timer times out if the AK frame is lost in this case the sender resends the

**[20:21]** frames after its timer times out as shown in the figure suppose a case of full duplex transmission the receiver

**[20:29]** sends back piggybacked acknowledgement by using some number in the acknowledgement field of its data frame

**[20:37]** for example if a 3 bit sequence number is used and suppose that a station sends frame 0er and gets back an rr1 and then

**[20:47]** sends frame 1 2 3 4 5 6 7 and zero and gets another rr1 this might either mean

**[20:57]** that rr1 is a cumulative AK or all eight frames were damaged this uncertainty can

**[21:05]** be defeated if the maximum window size is limited to seven that is for a k bit

**[21:11]** sequence number field it limited to 2K minus1 the number n which is equal to 2K

**[21:20]** minus1 specifies how many frames can be sent without receiving acknowledgement if no acknowledgement is

**[21:28]** received after sending end frames the sender takes the help of a timer after the timer timeout it resumes free trans

**[21:36]** Mission the go backend protocol also takes care of damaged frames and damaged acknowledgements this scheme is a little

**[21:44]** more complex than the previous one but gives much higher throughput the last arq scheme is selective repeat arq the

**[21:53]** selective repeat arq scheme retransmits only those for which n Cas are received

**[22:00]** or for which timer has expired so this is shown in the figure here this is the

**[22:06]** most efficient method among all the arq schemes but the sender must be more

**[22:13]** complex so that it can send out of the order frames the receiver also must have

**[22:20]** storage space to store the post n frames and processing power to reinsert frames in proper sequence so friends this this was all

**[22:28]** about data link cair hope all the concepts are clear to you hope to see you in the next lecture till then

**[22:36]** goodbye thank you
