# MANET – Routing Protocols

**Module 41**  
Duration: 23:55  
Video: https://www.youtube.com/watch?v=9eNSUh66Zag

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Sunil Kumar, Department of Electrical and Computer Engineering, Punjab Agriculture University, Ludhiana

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:20]** Hello friends I am engineer s Kumar from school of electrical engineering and information technology Punjab Agriculture University Ludhiana I

**[0:29]** welcome you all to the video lecture series of cyber and information security in this lecture we

**[0:36]** will study about routing protocols used in mobile adog network so now let us

**[0:42]** start before going into the details of routing protocol it is necessary to know about the routing protocol what it

**[0:51]** performs actually and what is their importance in the field of communication generally routing protocol

**[0:59]** represents the relationship or formula that is being used by routers to find the suitable way through which data can

**[1:07]** be forwarded routing protocol is also helpful in exchange of information between routers routing protocol plays a

**[1:16]** vital role to adjust the network according to variable conditions in other words the routing protocol is the

**[1:24]** implementation of routing algorithm in the form of software or Hardware routing protocol uses different matrices to find

**[1:33]** out the path which is used to transfer the packet across the network next types of routing

**[1:41]** protocols there are three types of routing Protocols are used in mobile adhoc network reactive routing protocols

**[1:49]** proactive routing protocols and hybrid routing protocols first reactive routing protocols reactive routing Protocols are

**[1:58]** called On Demand routing protocols so these routing Protocols are called when they are needed and the routers are

**[2:07]** built these routers can be acquired by sending root request through the network disadvantage of this algorithm is that

**[2:15]** it offers High latency in searching a network next proactive routing protocols the routing information about all the

**[2:24]** nodes is built and maintained by the proactive protocols the proactive routing Protocols are independent of

**[2:32]** whether or not the route is needed control messages are transmitted with periodically intervals even if there is

**[2:40]** no data flow still control messages are transmitted because these control messages proactive routing Protocols are

**[2:48]** not bandwidth efficient there are many advantages and disadvantages of proactive rting protocols one of its

**[2:56]** Advantage is that the nodes can easily get routing information and it easily starts a session the disadvantages are

**[3:06]** too much data kept by the nodes for rout maintainance when there is a particular

**[3:11]** link Failure Its reform is too slow next hybrid routing protocol this approach is

**[3:19]** a hybrid approach of combining both benefits of reactive and proactive routing protocols the routing initiates

**[3:27]** using the proactive method of pre planned routs extra demand is then handled by reactive flooding this

**[3:35]** methodology is only suitable for some situations where traffic demand and the number of nodes can be determined befor

**[3:43]** hand first protocol is aodv AD hog on demand distant Vector this is reactive

**[3:50]** protocol seek to set up roots on demand if a node wants to initiate communication with the node to which it

**[3:59]** has no route the routing protocol will try to establish such a route aodv protocol is described in RFC

**[4:08]** 3561 the philosophy in aodv like all reactive protocols is that topology information is only transmitted by nodes

**[4:17]** on demand when a node wishes to transmit traffic to a host to which it has no route it will generate a root request

**[4:26]** which is rreq message that will be FL blooded in a limited way to other nodes this causes control traffic overhead to

**[4:35]** be dynamic and it will result in an initial delay when it initiating such

**[4:41]** communication a rout is considered found when the RQ M reaches either the destination

**[4:49]** itself or an intermediate node with a valid route entry for the destination for as long as route exist between two

**[4:58]** end points if a remains passive when the route becomes invalid or lost aodv will

**[5:06]** again issue a request aodv defines three types of control messages for root maintainance first

**[5:14]** rrq a root request message is transmitted by a node requiring a rout

**[5:20]** to a node as an optimization aodv uses an expanding ring technique when

**[5:27]** flooding these messages every rrq carries a time to live value that states

**[5:34]** for how many hopes this message should be forwarded this value is set to a predefined value at the first

**[5:42]** transmission and increased at retransmissions retransmissions occur if

**[5:48]** no replies are received rrq frame format First Source address then Source

**[5:56]** sequence then broadcast ID then destination address then destination

**[6:02]** sequence Last Hope count next RRP a root reply message is

**[6:09]** unic casted back to the originator of rrq if the receiver is either the node

**[6:16]** using the requested address or it has a valid route to the requested address the reason one can unicast the message back

**[6:25]** is that every route forwarding a rrq cache a rout back to the originator the

**[6:32]** format of RRP is Source address destination address destination sequence

**[6:39]** hope count and lifetime where lifetime indicates how long a path can be used that is r e r r

**[6:48]** nodes monitor the link status of next stops in active routs when a link breakage in an active route is detected

**[6:57]** a root error message is used to notify other nodes of the loss of the link in order to enable this report mechanism

**[7:06]** each node keeps a precursor list which containing the IP addresses for each its neighbors that are likely to use it as a

**[7:14]** next toop towards each destination example the diagram to the left shows a

**[7:22]** setup of four notes on a wireless network the circles illustrate the range of communication for each node

**[7:30]** because of the limited range each node can only communicate with the nodes next to it node one wishes to send a message

**[7:40]** node three node one's neighbors are nodes 2 and four since node one cannot

**[7:47]** directly communicate with node 3 node one sends a root request message the

**[7:54]** root request is H by node four and node two when node one name receive the root request message they have two choices if

**[8:03]** they know a route to the destination or if they are the destination they can send a root reply message back to node

**[8:11]** one otherwise they will rebroadcast the root request to their set of neighbors the message keeps getting rebroadcast

**[8:20]** until its lifespan is up if node one does not receive a reply in a set amount of time it will rebroadcast plus the

**[8:29]** request accept this time the root request message will have a longer lifespan and a new ID number all of the

**[8:37]** nodes use a sequence number in the root request to ensure that they do not rebroadcast a root request in the

**[8:45]** example node two has a root to node three and replies to the root request by sending out a root reply node four on

**[8:55]** the other hand does not have a root to node three so it rebroadcast the root request in the example node one is the

**[9:04]** forwarding a root reply to node four it notices that the root in the root reply has a better sequence number than the

**[9:12]** root in its routing list node one then replace the root it currently has with

**[9:20]** the root in the root reply next root error messages root error messages allow a to adjust root

**[9:29]** Roots When nodes move around whenever a node receives root error it looks at the

**[9:35]** routing table and removes all the roots that contain the bad nodes the diagram

**[9:43]** to the left illustrates the three circumstances under which a node would broadcast a root error to its neighbors

**[9:51]** in the first scenario the node receives a data packet that it is supposed to forward but it does not have a root to

**[9:59]** the destination the real problem is not that the noes does not have a root the problem is that some other nodes thinks

**[10:08]** that the correct route to the destination is through that node in the second scenario the node

**[10:15]** receives a root error that cause at least one of its roots to become invalidated if it happens the node would

**[10:24]** then send out a root error with all the new nodes which are now unreachable in the third scenario the node detects that

**[10:32]** it cannot communicate with one of its neighbors when this happens it looks at the root table for root that uses the

**[10:41]** neighbors for a next hope and marks them as invalid then it sends out a root

**[10:48]** error with the neighbors and the invalid Roots next rooting protocol is

**[10:54]** osr osr is a proactive routing protocol and is also called as table driven protocol because it permanently stores

**[11:03]** and updates its routing table olsr keeps track of routing tables in order to

**[11:09]** provide a route if needed osr can be implemented in any adog network due to

**[11:17]** its nature osr is called as proactive routing protocol this protocol Works in collaboration with other nodes in Manet

**[11:25]** through the exchange of topology information this exchange of information is done

**[11:31]** periodically olsr uses multi-point lays to avoid the broadcast of unnecessary packets

**[11:40]** retransmissions in a network a node broadcast a message periodically to its neighboring nodes this is done to

**[11:48]** compute the multi-point relay set as well as the exchange of information about the neighborhoods from the information about

**[11:57]** the neighborhood this node calcul Cal Ates the minimum set of one hop lay point that is needed to reach the two

**[12:05]** hope neighbors and this set is called the multi-point relay set osr differs

**[12:12]** from the link State protocols in two factors based on the dissemination of routing information first is by

**[12:20]** construction that is only the multi-oil lay nodes of a node a need to forward updates about link state that are issued

**[12:28]** by node a secondly the size of the link State update of node a is reduced because it only consist of those

**[12:37]** neighbors that selected nodes a as their multi-point lay node thus we can conclude that olsr reduce the link State

**[12:46]** protocol it is used in a network where nodes are densely deployed the olsr

**[12:53]** calculates the shortest path in such networks to an arbitary destination following are the functions of protocol

**[13:02]** first neighbor sensing in wireless adog networks each node has to certify its nature of link with the neighbor nodes

**[13:11]** because of radio transmission in osr specifications there are two types of Link symmetric and

**[13:20]** asymmetric each node sends hello interval to its one of neighbors Hello message to achieve neighbor sensing

**[13:28]** which have no not be forwarded when node send the message it contains node neighbor list and their link status

**[13:37]** which allow them to reduce the hold to Hope neighbor and their status afterward MPR selection is made and the list is

**[13:47]** added into hello messages in final step using this MPR list a MP selector list

**[13:54]** is constructed which contains a neighbors list which have selected it as ampere now the messages received from

**[14:03]** their ampere selectors will be forwarded by the nodes second ampere flooding the aim of multi-point relas is

**[14:12]** possibly control traffic flooding in ampere flooding ampers are selected in such a way that when a flooding message

**[14:20]** is transmitted by the Ampere set it must reaches all two hope neighbors Amper set

**[14:28]** of a node n which is also represented as the smaller subset of symmetric one of

**[14:34]** neighbors of n having symmetric links with two hope neighbors of Amper flooding mechanism makes way to the

**[14:42]** elimination of transmission duplication as well as reception duplication is minimized by it next topology diffusion

**[14:52]** the objective of topology diffusion is to create routing tables using periodic topology control messages that is TC

**[14:59]** messages TC messages are circulated by each node with the nonn empty amp selector set to all Network nodes

**[15:08]** broadcasting at least links between itself and the nodes in its ampers Lector set to achieve topology diffusion

**[15:17]** these TC messages contain sufficient information which enable nodes first to construct their topology table and then

**[15:25]** to derive their routing table the roots are using short path algorithm such as digra shortest path algorithm after

**[15:34]** their calculation and providing the best possible hopes number however there is always a need to recalculate the routing

**[15:42]** tables to update the route information as the tables are based on information concerning links to neighbors and

**[15:51]** topology which can be changed at any instant next protocol is Tora temporary order routing algorithm

**[15:59]** Tora is a hybrid routing protocol it is effective in solving the existing limitations in Mobile AOG networks due

**[16:08]** to the high mobility of nodes congestion is one of the major problems in manets traditional shortest path algorithm

**[16:16]** adoptive shortest path algorithm and Link state routing can not work properly in Mobile Stations it is difficult to

**[16:24]** update the routing tables of each Dynamic nodes in to each node broadcast a cury packet and

**[16:32]** the recipients broadcast an update packet it Sports the loop free multiple route facilities using flat a non

**[16:42]** hierarchical routing algorithm it also provides better scalability to discover a route it uses

**[16:48]** a dag dag means directed a cyc graph and also uses a set of totally ordered

**[16:55]** Heights at all times in this approach information may only in One Direction hence it is only undirectional there is

**[17:04]** no chance to fail in infinite low it performs three basic operations root Creations root maintainance and root

**[17:13]** deletion to perform these three basic operations this protocol uses three control packets such as cury update and

**[17:23]** clear first root creation two control packets such as cury and updates are used to create a new route within the

**[17:31]** network a cury packet consist of a destination ID which is used for identifying the destination node and upd

**[17:40]** packet holds destination ID and height of the node each node maintains a root

**[17:46]** required flag which is initially unset and also maintains the time of broadcast for the last update packet within a

**[17:56]** network when a node has no directed link and an unset rout requested flag it broadcast a cury packet to its neighbor

**[18:05]** nodes and set its root required flag when any node receives a cury packet then it checks the following condition

**[18:14]** first if there is no down stream link and route required flag is unset it rebroadcast the cury control packet and

**[18:23]** sets the root required flag next if there is no Downstream link and root

**[18:30]** required flag is set it discards the cury packet if the receiving node has at least one Downstream link with null

**[18:38]** height it sets its height and broadcast a upd packet if the receiving node has

**[18:46]** at least one Downstream link with the nonnull height first compares the time of Last Broadcast of update packet with

**[18:54]** the time of Link over which cury packet was received became active next when the link becomes active

**[19:02]** in a node it broadcast a update packet and discards the query packet if the

**[19:09]** root required flag is set of any node it broadcast a query packet when a node receives a update package from its

**[19:17]** neighbors it updates the entities of array height and proceeds through the following steps if the root required

**[19:26]** flag is set node sets its high height and update all the entities in its link

**[19:32]** State array and unsets the root required flag then it broadcast a update packets

**[19:39]** with New Height if the root required flag is not set it just update the entities of the link State array and

**[19:49]** applies the root maintainance techniques next a root maintainance in Mobile hog Network Tora

**[19:57]** maintains the root when any topological change has occurred it also ensur the reestablishment of roots between nodes

**[20:06]** within finite amount of time the root maintenance is needed for a node when its height is non null if any neighbor

**[20:14]** node has null value that neighbor node will not be considered for this operation there are five different cases

**[20:22]** available in Tora to root maintenance case one generate new reference level case two propagate the highest neighbors

**[20:31]** reference level case three reflect back a higher sub level case four partition detection and case five is generate new

**[20:41]** reference level in case one due to link failure the node lost its last downstep

**[20:48]** link if the node has any upam neighbor node it updates its reference value

**[20:54]** otherwise it sets its height to null if the node has no Downstream link it propagates the reference level to its

**[21:03]** Upstream Neighbors which is show in case to due to link reversal if the

**[21:10]** downstream links fail then the node reflects back the reference height with setting the reflection bit according to

**[21:17]** the case three if the set reference value is equal to the reference height of neighbor nodes the nod has detected

**[21:25]** the partition and has started to raise the root setting the height value to null which is shown in case four in case

**[21:34]** five generation of new reference value occurs when the node has experienced a link failure between the time of

**[21:44]** propagation of a reference level and reflects Su level next operation is root deletion in case four of root

**[21:52]** maintenance node sets its height which is determined by the direction of edges to the destination and updates all the

**[22:02]** entries of its link State array and broadcast control packet when a node receives a control packet it follows the

**[22:11]** following procedures first if the reference level in the control packet is matched with the reference level of that receiving

**[22:20]** node the node sets its height and sets the height for each neighbor to null it

**[22:27]** also updat all the entries in the link State arrays and broadcastter control packet second if the reference level of

**[22:36]** the control packet does not match with the reference level of the node it sets its height for each neighbor and it also

**[22:45]** updates corresponding link State array entries at the end the height of each node in the portion of the network which

**[22:53]** was partitioned is set to null and erase all the invalid r Roots so friends this

**[23:00]** was all about roting protocols in Manet hope the concepts explained in this lecture were understandable and helpful

**[23:08]** hope to see you in the next lecture till then goodbye thank you

**[23:14]** [Music]
