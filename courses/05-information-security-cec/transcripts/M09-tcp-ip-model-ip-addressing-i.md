# TCP/IP Model-IP Addressing – I

**Module 09**  
Duration: 30:01  
Video: https://www.youtube.com/watch?v=Q40gn2Eu1zw

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Prof Maninder Singh, Department of Computer Engineering, Thapar University, Patiala

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** hello class today we are going to talk about cyber security as the name says security the

**[0:07]** first thing which comes in mind that how I'm going to secure my computer system now when we talk about security the first thing which we need to understand

**[0:16]** how the computer network works so we are going to start today with the introductory session on computer

**[0:25]** networks as all of we know that whenever a data has to transfer from one machine to another machine it is going to go

**[0:33]** from application which is going to talk to the user to the physical layer so

**[0:39]** let's first start with TCP IP model of networks so here as you can

**[0:48]** see there are seven layers in total which starts from application layer and you can memorize it by a phrase called

**[0:56]** all people seem to need data processing now there is a client machine and there

**[1:04]** is a server machine server machine will also have the seven layers all people seem to need data

**[1:13]** processing now when we talk about a practical model the first three layers which are called application layer

**[1:20]** presentation layer and session layer these layer are combined together and this is called simply application layer

**[1:29]** so on that application layer we basically talk to a server using a

**[1:38]** browser so browser is an application which is basically interface between user and the

**[1:46]** Machine now here in the browser we are going to type address to which the site we are going

**[1:56]** to go to for example if we say www .

**[2:02]** google.com so this is the address we have typed in the address bar now when these layers are going to talk to each other the conversation

**[2:11]** between the layer happens vertically down so we cannot have a horizontal communication so that means the data

**[2:18]** will travel from application layer to the transport layer and from the transport layer it will go to the network layer and from the network layer

**[2:27]** data link layer and finally it will go to the physical layer so that means the data link layer and physical layer are the two layers which are basically

**[2:36]** dependent upon the network type like whether I am using a Wi-Fi network or I am using a wired

**[2:45]** Network so when we transport the data from an application layer the data is called

**[2:53]** payload that means I'm going to send a payload called www dot

**[3:02]** google.com so this is the payload which is going to go to the next layer now the next layer is called transport

**[3:09]** layer now on the transport layer what happens there are many things which happened at a transport layer which is

**[3:16]** governed by TCP and UDP protocols so there are two protocols prevalent on this

**[3:24]** layer one is called TCP another is called UDP now the thing comes in mind basically what is a protocol so protocol

**[3:33]** is set of instructions or you can say it is set of rules which need to be

**[3:40]** followed in order to respect a particular line of action so that means

**[3:47]** we either choose a TCP or a UDP protocol most of the realtime applications whether we are going to

**[3:55]** talk like www which is basically a HTTP related application or we have a mailing

**[4:04]** application all these applications are going to follow a TCP layer as a protocol so TCP is the

**[4:12]** default protocol for all realtime applications now inside TCP there are many things which will happen which we

**[4:20]** are going to explore in the later classes but as a introductory class we need to understand that there are two things basically which happens at TCP

**[4:29]** layer one is called The Source port address and another is called the destination port

**[4:37]** address now what this addresses basically are these addresses will

**[4:46]** identify a particular application running on the

**[4:53]** server so that mean these are the identifiers which will tell about applications running at those layers

**[5:00]** like if HTTP application is running it is going to respect a number which is

**[5:07]** called Port 0 so Port 0 is recognized as an HTTP application now these are the

**[5:15]** standard application which will run on this particular machine now because we were accessing

**[5:25]** www.google.com so that means we are going to go to HTT P protocol and this will listen at Port number 80 so that

**[5:34]** means from a payload when it comes to the transport layer this will be called as a

**[5:43]** segment so inside the segment we are going to add two things one is one will be the

**[5:50]** payload another will be the source port number and destination port number now

**[5:57]** the destination port number will be 80 by default because we are going to access it through a HTTP protocol so the

**[6:06]** port number 80 is default for HTTP applications but what about the source port number from where the data is going

**[6:15]** to get originated now this Source port number is any random

**[6:21]** number which is above to4 port numbers so basically a port number

**[6:28]** is 16bit entity that means if we say 2 to 16 this

**[6:36]** comes out to be 65,536 ports so these many application

**[6:43]** theoretically can run on one single machine now out of this we are going to bind a particular application to a port

**[6:51]** number like HTTP will get binded to port number 80 FTP will get binded to two

**[6:57]** port numbers 20 and 21 whereas SMTP gets binded to port number 25 similarly SSH

**[7:06]** will get binded to port number 22 tnet gets binded to port number 23 and these are the standard applications

**[7:15]** which are being used across the world for accessing various kind of applications now when we talk about the

**[7:22]** source port numbers now the source port number cannot be any port number which

**[7:29]** is less less than 1024 because these are standard port numbers so your computer is going to choose any number above 1024

**[7:38]** let's say it chooses 4444 as the source port number now your segment will now look like

**[7:46]** 4444 which is your standard port number randomized

**[7:55]** for transport layer and then we have port number 80 which is default port number for HTTP application and in

**[8:03]** between there will be a payload which has come from the application layer so now the segment is going to go

**[8:11]** to the next layer which is called Network layer now Network layer is responsible

**[8:18]** for giving addresses to the computers like client computer and

**[8:27]** server computer so the client comp computer will also have some address and server computer will also have some

**[8:33]** address now these addresses are given in a form which is called

**[8:40]** dotted decimal notation now this dotted decimal

**[8:47]** notation is called IP address now the size of the IP address

**[8:55]** is 32bit and we are talking here about IP version 4 so IP version 4 has 32bit

**[9:04]** address that means in totality I can have 2 raed to 32 unique addresses

**[9:11]** generated by ipv4 now out of these ipv4 2 ra to 32 address there are

**[9:21]** certain addresses which are being reserved which are called class D and E

**[9:29]** address addresses rest of the addresses are used by our computers which are called Class A address Class B address

**[9:38]** Class C address let's first of all talk about these addressing mechanisms now IP address basically is X

**[9:47]** doy do z. a now where each X or Y or Z or a will go from 0 to

**[9:57]** 255 so this will take eight bits now each OCT dat is going to take 8

**[10:06]** Bits so total we have 32 bits now the addresses will start from

**[10:14]** zero and it will go up to 255 for each

**[10:21]** octet so there are classes which are defined which is called Class A address Class B address Class C address and then

**[10:28]** finally D and E class now Class A how you will distinguish that particular IP

**[10:36]** address belongs to class A now you need to see that IP address is basically divided into two

**[10:45]** parts one part is called Network

**[10:50]** address and another part is called host address now the network address and host

**[11:00]** address which part of IP address will be called as a network address and which part will be called as a host address it

**[11:07]** all depends upon something which is called subnet mask so subnet mask is very important in

**[11:16]** order to know which portion of IP address will be a network and which portion will address

**[11:23]** hosts now each of the classes like Class A address there is a default subnet

**[11:31]** mask now this default subnet mask is 255.0.0.0

**[11:39]** so the addresses which have this subnet mass will be called as Class A

**[11:47]** address now that means the first OCT dat if the value is from 0 to

**[11:55]** 126 these addresses will fall under category a address so let's take an example if I have addressed 10 do 10 do 10.

**[12:08]** 10 now by default if you see the first OCT dat it lies between 0 and

**[12:15]** 126 that means this is a class A address now in the class address the

**[12:25]** subnet mask is 255.0.0.0 this is the default that mean the first

**[12:32]** OCT dat 8 Bits will represent Network and the three

**[12:38]** octat that means 24 bits will represent host that means in a class A there will

**[12:47]** be 2 ra to 8 networks and each network will have 2 ra to 24

**[12:55]** hosts so that means Class A networks are the net networks which are bigger networks there will be millions of

**[13:03]** machines which can be in one of the classy networks then we move to class B now in class B the default subnet mask

**[13:11]** is 255.255.0.0 that means the 16 bits will

**[13:19]** represent Network and 16 bits will represent

**[13:25]** host so the class B networks are two 2 to 16 networks and each network will have 2 ra

**[13:34]** to 16 hosts so these are pretty big networks

**[13:41]** that means each network will have 65,500 36 hosts it's a huge

**[13:48]** number then we come to class C now Class C has a default subnet mask of

**[13:57]** 255.255 do25 5.0 that means 24 bits will represent

**[14:06]** Network and 8 Bits will represent

**[14:11]** host so 2 to 8 number of host are available for each

**[14:20]** Network now 2 ra to 8 if we calculate is 256 hosts so that means the smallest Network

**[14:29]** which we can create using Class C would house 256 hosts now let's takeen a practical

**[14:37]** example where I want to have 20 machines on a

**[14:46]** network now that means how many addresses are required if I want to address all the 20 machines we'll start

**[14:52]** with the address one until address 20 so which addressing scheme will suit my network best so we have to choose Class

**[15:01]** 15 minutes, 1 second C because if we choose Class A we'll be wasting huge number of IP addresses so that mean there is a huge wastage which

**[15:10]** will happen if we use Class A because Class A has two ra to 24 hosts per Network so we will be going to choose

**[15:19]** Class C so Class C is going to give me 256 that means I am only wasting 236 IP

**[15:27]** addresses but if if you can see this is a huge wastage again it's a pretty huge wastage so what we need to do in such

**[15:35]** cases let's take an example

**[15:40]** [Music]

**[15:44]** 192.168.1.0 let's take this as an IP address and I want to address 20 machines with this IP address so the

**[15:52]** first address which I'm going to allot to my machine will be 192.168.1.1

**[16:00]** the next machine will be 1.2 1.3 and it will go up to 1. 20 so these are the

**[16:09]** machines which will be allocated using this IP address so each of this machine will be having the same network so there

**[16:18]** are two things which are very important when the machines are going to talk to the another Network number one machine

**[16:27]** should be part of the same Network and second they should have

**[16:34]** something which is called a broadcast address so let's say there is a machine

**[16:44]** 192.168.1.2 it wants to talk to

**[16:47]** [Music]

**[16:52]** 192.168.1.2 so this mechanism will be called as unicast

**[17:00]** communication because a single machine is going to talk to another machine but least let's take an example

**[17:09]** [Music]

**[17:12]** 192.168.1.2 wants to talk to all the machines in its Network all the machines

**[17:19]** in the same network now first thing which we need to know what is the network of

**[17:27]** 192.168.1.2 let's find it in order to find a network we need to take an IP

**[17:36]** address and then take a logical and logical and

**[17:43]** operation of this with the subnet

**[17:51]** mask that means 192.168.1.2 is to be logically and with

**[18:06]** 255.255.255.0 so if we'll take a logical and that means I need to convert all these values into

**[18:13]** binary and then take the logical and so if we are going to take a logical and of anything with zero so this will be zero

**[18:22]** rest of the things will remain same so my network address comes out to be 192 .

**[18:31]** 16810 so this is the network address now what about the broadcast

**[18:39]** address broadcast address is when the all of your host bits are made one all

**[18:46]** host bits are made one that means this will be 192.168.1

**[18:59]** dot 1 one1 1 one1 in binary so this comes out to be

**[19:07]** 255 so that means for this IP address

**[19:14]** 192.168.1.2 the network address is 192.168.1.0 and the broadcast address is

**[19:26]** 192.168.1 255 so that means for each network if the

**[19:33]** network has to talk to some other network we need basically two addresses one will be called as Network address

**[19:42]** and another will be called as broadcast address and if I wish to talk to another Network I'll require another special

**[19:50]** address which will be called as a gateway address so if I want to address 20

**[19:58]** machines and these 20 machines are going to do a unicost communication broadcast

**[20:07]** communication and they also want to talk to some other network which is a different network then we'll require three

**[20:15]** addresses one will be Network address second will be broadcast address and third will

**[20:24]** be gateway address so these three addresses are required for each

**[20:31]** Network whenever a network wants to talk to the another Network so in our example

**[20:41]** 192.168.1.0 is the network address 192.168.1

**[20:49]** 255 is the broadcast address and you can choose any address

**[20:57]** to be chosen as address for your gateway so Gateway is nothing but it's a router which is going to talk to the another

**[21:04]** Network so if you want to follow a standard the standard say the last IP address of your network should be given

**[21:12]** to the Gateway so the gateway address will be 192.168.1.254

**[21:20]** that mean the formula is 2 ra to nus 2

**[21:26]** hosts per Network so in our case the value of n was 8 so 2

**[21:35]** to 8 - 2 which comes out to be 254 hosts in class c network so each class c

**[21:45]** network will have 254 hosts and out of these 254 host one

**[21:54]** particular address will be given to the Gateway so that means my network is having

**[22:02]** 253 live hosts as per our example we needed only 20 addresses so that means finally we

**[22:11]** have 2 33 addresses getting wasted so this addressing scheme which

**[22:19]** is called classless addressing scheme was

**[22:25]** introduced in order to cut down wastage by classful addressing scheme so

**[22:34]** we have two schemes which are available now one is called classful which will use Class A address

**[22:42]** Class B address or Class C address class D address is reserved for multicasting we'll talk about

**[22:49]** multicasting in the later lectures and Class E is not used this is a reserved

**[22:56]** class so we are left only with three classes Class A Class B and Class C but

**[23:03]** these classes gives us wastage so we are going to adopt another mechanism which

**[23:09]** is called cidr notation classless

**[23:15]** inter domain routing now this scheme is used in order

**[23:23]** to cut down the wastage so we are going to cut down the Wast stage let's see in our example how

**[23:31]** we can use cidr in order to cut down the wastage so we require 20

**[23:40]** addresses so in order to address 20 machines how many bits I will require I will require five bits how

**[23:49]** five bits like we have a chart 1 2 4 8 16

**[23:56]** 32 now we'll give number of bits one bit 2 three four and five so we'll require

**[24:03]** five bits in order to address 31 machines 16 + 4 + 8 + 2 30 +

**[24:13]** 1 so 31 machine can get address with five bits so that means I don't need to

**[24:21]** consume whole of the8 bits of the host address I'll only consume five bits out

**[24:28]** out of this and with the five bits I can address 31 machines so I require only 20

**[24:38]** so that mean the wastage will be only 11 addresses so the cidr notation is going

**[24:48]** to help me in order to cut down this wastage now this kind of notation is

**[24:55]** called subnetting a network so we are going to subnet a network so

**[25:03]** that we can have less number of ips getting wasted so in our case

**[25:14]** 192.168.1 do0 as a network address we are going to consume now only

**[25:22]** five bits so that means three bits will be given to the network so if we are going going to write it in binary so it

**[25:29]** will be 1 1 1 1 2 3 4 5 so these five bits will be host

**[25:37]** bits and these three bits will be Network bits so what would be my

**[25:45]** Subnet MK it will be 255 do 255 do

**[25:52]** 255 dot now these three I have to write it in decimal so this will be 1 2 4 8

**[26:01]** 26 minutes, 1 second 32 64 +28 +

**[26:11]** 255 so this is the value which is to be given in order to cut it to the subnet mask so my

**[26:21]** subnet mask will now will be different so it will not be 255 do

**[26:31]** 255.255 do0 but it will be something else in the next stock

**[26:37]** date so cidr notation gives me a privilege so that less number of ips get

**[26:47]** wasted so we are going to take some examples in the next class where we are going to find out

**[26:54]** subnets and even we'll talk about something which is called supernetting so super netting will be where the number of network will increase and

**[27:02]** subnetting is where the number of networks get decreased so that means we are going to play with the host bits and

**[27:09]** we are going to play with the network bits and this is going to cut down our vage of IP addresses so we are using

**[27:19]** IP V4 as our addressing mechanism so let's sum up whatever we have learned so far so that in the later

**[27:27]** class when we talk about subnetting and uh super netting we will be in the same line so we we started with an

**[27:35]** application layer so application layer has a payload this payload has to go

**[27:42]** vertically down two another layers precisely it will go to the transport layer and at the transport layer there

**[27:49]** are two things which are going to get added one is called Source port number another is called destination port number

**[27:58]** and the protocol data unit which gets created at transport layer is called

**[28:06]** segment now segment will have destination port number which is a fixed entity and this

**[28:14]** destination port number is dependent upon the application from which we are going to receive the data like if we are

**[28:22]** going to receive a data from a browser application by default the destination port number will be 0 so we talked about

**[28:30]** these port numbers these standard port numbers are going to address standard applications and

**[28:37]** then with this segment the data will flow to the network layer now the at the network layer we

**[28:46]** talked about two things one is the source IP address and destination IP

**[28:54]** address and in the IP addressing scheme we talked about about how to address the machines so machines can be addressed

**[29:02]** with the help of a classful IP addressing and classless IP addressing if we start using class full IP

**[29:10]** addressing lots of Ip V4 addresses get wasted as we saw in in an

**[29:16]** example we 192 168 1.2 Network and we wanted 20 machines to get address so we

**[29:24]** were wasting 236 IP addresses so we learned about something which is called classless interdomain routing so we are

**[29:32]** going to pick up some examples where it will be explained that how C is going to help us in order to cut

**[29:40]** down this so thank you very much for listening to this first introductory section on cyber security as a course so

**[29:48]** in the next session we are going to explore about Network addresses and we are going to talk about Mac layer

**[29:56]** addresses which is called data link cayer addresses thank you
