# Introduction to Mobile IP and Addressing

**Module 36**  
Duration: 20:02  
Video: https://www.youtube.com/watch?v=I2IzxqoP7M8

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Sunil Kumar, Department of Electrical and Computer Engineering, Punjab Agriculture University, Ludhiana

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:39]** Hello friends I welcome you all to the video lecture series of cyber security and information security in this lecture

**[0:47]** we will study about mobile IP and its related terms first of all please see the contents which I shall

**[0:55]** cover first I will cover the brief introduction about mobile IP and addressing after covering brief

**[1:03]** introduction about mobile IP and addressing I shall take up agents in Mobile IP after that I will cover the

**[1:10]** three phases used in Mobile communication and last I shall take up inefficiency in Mobile IP so now let us

**[1:20]** start mobile communication has received a lot of attention in last decade the interest in Mobile communication on the

**[1:28]** internet means that the IP protocol originally designed for stationary devices must be enhanced to allow the

**[1:36]** use of mobile computers computers that move from one network to another addressing the main problem that must be

**[1:43]** solved in providing mobile communication using the IP protocol is addressing stationary hosts the original

**[1:53]** Ip addressing was based on the assumption that a host is stationary attached to one specific Network a

**[2:02]** router uses an IP address to root an IP datagram an IP address has two parts a

**[2:09]** prefix and a suffix the prefix Associates a host to a network for example the IP address

**[2:18]** 10.3.4 24x 8 defines a host attached to the network

**[2:25]** 10.0.0.0 by 8 this implies that a host in the internet does not have an address

**[2:33]** that it can carry with itself from one place to another the address is valid only when the host is attached to the

**[2:40]** network if the network changes the address is no longer valid routers use this Association to

**[2:48]** root a packet they use the prefix to deliver the packet to the network to which the host is attached this scheme

**[2:56]** works perfectly with stationary hosts the IP addresses are designed to work with stationary hosts because part of

**[3:04]** address defines the network to which the host is attached mobile host when a host moves from one network to another the IP

**[3:13]** addressing structure needs to be modified several Solutions have been proposed changing the address one simple

**[3:22]** solution is to let the mobile host change its address as it goes to the new network The Host can use

**[3:31]** DHCP to obtain a new address to associate it with the new network this approach has several drawbacks first the

**[3:40]** configuration files would need to be changed second each time the computer moves from one network to another it

**[3:47]** must be rebooted third the DNS tables need to be revised so that every other host in the internet is aware of the

**[3:56]** change fourth if the host roams from from one network to another during a transmission the data exchange will be

**[4:04]** interrupted this is because the ports and IP addresses of the client and the server must remain constant for the

**[4:12]** duration of the connection two addresses the approach that is more feasible is the use of two

**[4:19]** addresses the host has its original address called the home address and a temporary address called the care of

**[4:27]** address as per figure the home address is permanent it Associates the host to its home network the network that is

**[4:35]** permanent home of the host the care of address is temporary when a host moves from one network to another the care of

**[4:44]** address changes it is associated with the foreign Network the network to which the host moves mobile IP has two

**[4:52]** addresses for a mobile host one home address and one care off address the home address is permanent the care of

**[5:00]** address change as the mobile host moves from one network to another agents to make the change of address transparent

**[5:07]** to rest of the internet requires a home agent and a foreign agent figure shows the position of a home agent relative to

**[5:15]** the home network and a foreign agent relative to foreign Network we have shown the home and the foreign agent as routers but we need to emphasiz that the

**[5:24]** specific functions as an agent is performed in the application layer in other words they are both routers and

**[5:31]** host home agent the home agent is usually a router attached to the home network of the mobile host the home

**[5:40]** agent acts on behalf of the mobile host when a remote host sends a packet to the mobile host the home agent receives the

**[5:49]** packet and sends it to the foreign agent foreign agent the foreign agent is usually a router attached to the foreign

**[5:58]** Network the foreign agent receives and delivers package sent by the Home agent to the mobile host the mobile host can

**[6:06]** also act as a foreign agent in other words the mobile host and foreign agent can be the same however to do this a

**[6:14]** mobile host must be able to receive a care of address by itself which can be done through using the

**[6:22]** DHCP in addition the mobile host needs the necessary software to allow it to communicate with the home agent and to

**[6:30]** have two addresses its home address and its care of address this dual addressing must be transparent to the application

**[6:38]** programs when the mobile host acts as a foreign agent the care of address is called a colocated care of address when

**[6:48]** the mobile host and the foreign agent are the same the care of address is called a collocated care of

**[6:56]** address the advantage of using a c ated care of addresses that the mobile host can move to any network without worrying

**[7:05]** about the availability of a foreign agent three phases in Mobile communication to communicate with a

**[7:13]** remote host a mobile host goes through three phases agent Discovery registration and data transfer as shown

**[7:22]** in the figure the first phase agent Discovery involves the mobile host the foreign agent and the home

**[7:31]** agent the second phase registration also involves the mobile host and the two

**[7:38]** agents finally in the third phase the remote host is also involved we discuss each phase

**[7:47]** separately agent Discovery the first phase in Mobile communication agent Discovery consists of two surfaces a

**[7:56]** mobile host must discover a home agent before it leaves its home network a mobile host must also discover a foreign

**[8:04]** agent after it has moved to a foreign Network this discovery consists of learning the care of address as well as

**[8:13]** the foreign agent address the discovery involves two types of messages advertisement and

**[8:20]** solicitation agent advertisement when a router advertises its presence on a network using an icmp

**[8:28]** router advertisement it can append an agent advertisement to the packet if it acts as an agent figure shows how an

**[8:38]** agent advertisement is piggy bagged to the router advertisement packet the field descriptions shown in figure are

**[8:45]** as follows type the 8bit type field is set to 16 length the 8bit length field defines

**[8:56]** the total length of the extension message not the length of the icmp advertisement

**[9:03]** message sequence number the 16bit sequence number field holds the message

**[9:09]** number the recipient can use the sequence number to determine if a message is

**[9:16]** lost lifetime the lifetime field defines the number of seconds that the agent will accept

**[9:24]** requests if the value is a string of ones the lifetime is in finite code the

**[9:31]** code field is an 8bit flag in which each bit is set one or unset to

**[9:39]** zero care of addresses this field contains a list of addresses available

**[9:45]** for use as care of addresses the mobile host can choose one of these addresses

**[9:52]** the selection of this SC of address is announced in the registration request note that this field is used only by a

**[10:00]** foreign agent agent solicitation when a mobile host has

**[10:07]** moved to a new network and has not received agent advertisements it can initiate an agent

**[10:14]** solicitation it can use the icmp solicitation message to inform an agent that it needs

**[10:22]** assistance registration the second phase in Mobile communication is registration after a

**[10:30]** mobile host has moved to a foreign Network and discovered the foreign agent it must register there are four aspects

**[10:38]** of registration first the mobile host must register itself with the foreign agent second the mobile host must

**[10:47]** register itself with its home agent this is normally done by the foreign agent on behalf of the mobile host third the

**[10:55]** mobile host must renew registration if it has expired fourth the mobile host must cancel its registration when it

**[11:03]** returns home request and reply to register with the foreign agent and the home agent the mobile host uses a

**[11:11]** registration request and a registration reply registration request a registration request is sent from the

**[11:20]** mobile host to the foreign agent to register its care of address and also to announce its home address and home agent

**[11:28]** address the foreign agent after receiving and registering the request relays the message to the home agent note that the

**[11:37]** home agent now knows the address of foreign agent because the IP packet that is used for relaying has the IP address

**[11:45]** of the foreign agent as the source address figure shows the format of the registration request the field

**[11:53]** descriptions shown in figure are as follows type the the 8bit type field defines the type of message for a

**[12:02]** request message the value of this field is one flag the 8bit flag field defines

**[12:09]** forwarding information the value of each bit can be set or unset lifetime this

**[12:17]** field defines the number of seconds the registration is valid if the field is a string of zeros the request message is

**[12:25]** asking for D registration if the field is a string of once the lifetime is

**[12:32]** infinite home address this field contains the permanent address of the mobile host mobile agent address this

**[12:41]** field contains the address of the home agent care of address this field is the

**[12:48]** temporary address of mobile host identification this field contains the 64bit number that is inserted into the

**[12:56]** request by the mobile host and repeat in the reply message it matches a request with a reply

**[13:05]** extensions variable length extensions are used for authentication they allow a home agent to authenticate the mobile

**[13:13]** agent registration reply a registration reply is sent from the home agent to the foreign agent and then relay to the

**[13:22]** mobile host the reply confirms or denies the registration request data transfer after agent

**[13:31]** Discovery and registration a mobile host can communicate with the remote host figure shows the process of data

**[13:39]** transfer I'll explain one by one from remote host to home

**[13:45]** agent path one of figure shows this step when a remote host wants to send a packer to the mobile host it uses its

**[13:54]** address as the source address and the home address of the mobile host as the destination address in other words the

**[14:02]** remote host sends a packet as though the mobile host is at its home network the packet however is intercepted by the

**[14:10]** Home agent which pretends it is the mobile Host this is done using the proxy ARP

**[14:18]** technique from home agent to foreign agent path two of the figures shows the

**[14:25]** step after receiving the packet the home agent sends the packet to the foreign agent using the tunneling concept the

**[14:34]** home agent encapsulates the whole IP packet inside another IP packet using its address as the source and the

**[14:42]** foreign agent's address as the destination from foreign agent to mobile host part three of figur shows this step

**[14:51]** when the foreign agent receives the packet it removes the original packet however since the destination address is

**[14:59]** is the home address of mobile host the foreign agent consults a registry table to find the care of address of the

**[15:06]** mobile host otherwise the packet would just be sent back to the home network the packet is then sent to the care of

**[15:14]** address from mobile host to remote host path four of figure shows the step when a mobile host wants to send a packet to

**[15:23]** a remote host for example a response to the packet it has received it sends as it does normally the mobile host

**[15:31]** prepares a packet with its home address as the source and the address of remote host as the destination although the packet comes

**[15:40]** from the foreign Network it has the home address of the mobile host transparency in this data transfer process the remote

**[15:49]** host is unaware of any Movement by the mobile host the remote host send packets using the home address of the mobile

**[15:56]** host as the destination address it receives the packets that have the home address of the mobile host as the source

**[16:04]** address the movement is totally transparent the rest of the internet is not aware of the mobility of mobile

**[16:12]** host inefficiency in Mobile IP communication involving mobile IP can be

**[16:20]** inefficient the inefficiency can be severe or moderate this severe case is called double crossing or 2X

**[16:29]** the moderate case is called triangle routing or dog leg routing double crossing according to

**[16:37]** figure double crossing occurs when a remote host communicates with the mobile host that has moved to the same network

**[16:46]** as the remote host when the mobile host sends a packet to the remote host there is no inefficiency the communication is

**[16:55]** local however when the remote host sends a packet to the mobile host the packet crosses the internet twice since a

**[17:03]** computer usually communicates with other local computers the inefficiency from double crossing is significant triangle

**[17:11]** routing triangle routing occurs when the remote host Communications with the mobile host that is not attached to the

**[17:19]** same network or site as the mobile host when the mobile host sends a packet to the remote host there is no inefficiency

**[17:29]** however when the remote host sends a packet to the mobile host the packet goes from remote host to the home agent

**[17:36]** and then to the mobile host the packet travels the two sides of a triangle instead of just one side one solution to

**[17:45]** inefficiency is for the remote host to bind the care of address to the home address of a mobile host for example

**[17:53]** when a home agent receives the first packet for a mobile host it forwards the packet to the foreign agent it could

**[18:01]** 18 minutes, 1 second also send an update binding packet to the remote host so that future packets to this host can be sent to the care of

**[18:09]** address the remote host can keep this information in a cache the problem with this strategy is that the cash entry

**[18:18]** becomes outdated once the mobile host Moves In this case the home agent needs to send a warning packet to the remote

**[18:26]** host to inform it of the change so friends this was all about mobile IP and its related terms hope the concepts

**[18:34]** explained in this lecture were understandable and helpful hope to see you in next lecture till then goodbye thank you

**[18:44]** [Music]

**[19:10]** [Music]

**[19:59]** [Music]
