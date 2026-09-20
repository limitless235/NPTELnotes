# TCP/IP Model-IP Addressing – II

**Module 10**  
Duration: 28:44  
Video: https://www.youtube.com/watch?v=FQzPOhnEkjg

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** hello class in the previous lecture we had talked about the flow of data from a

**[0:08]** application layer to the network layer now we said that from application layer the payload gets transported to

**[0:17]** transport layer where the segment is formed and then it is transported to the network layer where a packet is

**[0:26]** formed now this packet is formed with the help of two two things one is called The Source IP address and other is called the destination IP

**[0:34]** address so we discussed about the various classes of IP addresses and we talked about class a IP

**[0:42]** addresses Class B and Class C and we have taken one example where we wanted

**[0:48]** to have a network establishment of a 20 machines so we are going to choose an IP

**[0:55]** [Music]

**[0:58]** 192.168.1.0 and I want to address all the machines in my network where the wastage would be as

**[1:05]** less as possible so we are going to utilize cidr which is called classless interdomain

**[1:13]** routing and this classless Internet Internet domain routing is going to prove sufficient enough in order to

**[1:22]** lessen the wastage of IP addresses so

**[1:28]** 192.168.1 1.0 is our Network address and in order to address 20 machines we'll

**[1:37]** require five bits now how we come to this five bits so you need to memorize a

**[1:44]** table which is called 2 ra to 0 2 ra to 1 2 to 2 2 ra to 3 because computer is

**[1:52]** going to use a binary system 2 4 2 to 5 2 to 6 now if you convert into the

**[2:00]** decimal format this is 1 2 4 8 16 32 64

**[2:10]** 128 and it will go 2 7 2 to 8 and so and so forth now these are the eight bits of

**[2:19]** the last octe so out of these one 2 3 4

**[2:25]** 5 these five bits we want that that these should address host and these

**[2:32]** three bits should address the network now whereever the weight is one

**[2:39]** that will represent Network and wherever the weight is zero that will represent

**[2:46]** host so now we'll add up these values 128 64 and

**[2:54]** 32 so this comes out to be 224 that means the last last octed in

**[3:01]** 3 minutes, 1 second our case is 255 do 255 do 255 do

**[3:10]** 224 now this 224 is going to give us five bits as

**[3:19]** hosts so our address is 192.168.1.0 is our Network address the

**[3:27]** first machine will be 192 16811 second will be 1.2

**[3:35]** 1.3 and it will go up to 1. 20 so these are the 20 machines which will be on our

**[3:43]** Network now the thing comes what would be the broadcast address of my network now how to calculate the

**[3:50]** broadcast address so we are going to write 192 168 do

**[3:56]** [Music]

**[3:58]** 1.0 and subnet mask is 255 255.255

**[4:06]** 224 now whenever we have to do some calculations on IP addresses always remember that first of all take the

**[4:14]** incomplete block so here the incomplete block is 224 so you subtract this from

**[4:22]** 256 so this comes out to be 32 so the block size

**[4:30]** is 32 that means in each block there will be 32 machines which can get address from this IP

**[4:39]** scheme now the last address from this will be the broadcast so if you say 32 -

**[4:46]** 1 this comes out to be 31 so that means 192

**[4:53]** 168 do 1.31 is the broadcast address

**[5:02]** 192.168.1.0 is the network address from 21 to address 30 this is

**[5:10]** the wastage because we only required 20 machines so this is how we are going to

**[5:18]** calculate the number of machines on a network what is the network address what is the broadcast let's take another example

**[5:26]** [Music]

**[5:28]** 192.168.1 0 this is the network address

**[5:36]** calculate broadcast address first host

**[5:46]** address last host address number of

**[5:55]** hosts and number of

**[6:05]** subnets if we want to have 10 machines on the

**[6:14]** network now let's do this so we have been given address 192 168

**[6:22]** 1.0 now we have to address how many machines 10 machines so let's again draw that table

**[6:29]** 1 2 4 8 16 32 64 128 so total there are

**[6:37]** 1 2 3 4 5 6 78 bits so these are the eight

**[6:44]** bits which will address 256 machines so we need to address only 10 machines so

**[6:52]** in order to address 10 machines I would require four bits so four bits are required for addressing this so that

**[7:00]** means these four bits will represent Network and these four bits will represent

**[7:09]** host so 2 to 4 - 2 is the number of

**[7:17]** hosts which comes out to be 14 so we'll be able to address 14 machines with help of this addressing

**[7:25]** mechanism so what would be my subnet mask let's calculate so my subnet mask is

**[7:32]** 255 do 255 do 255 dot 1 2 3 4 4 1es and four

**[7:42]** zeros so if we convert this into decimal this comes out to be 240 so all the weights which are being

**[7:51]** given one value you need to add

**[7:54]** those so 1 2 4 8 16 32 64 128 1 1 1 1 0

**[8:05]** 0 0 0 so these values are to be added so 128 + 64 + 32 + 16 this comes out to be

**[8:16]** 240 so this 240 is my last octe so your last OCT dat is

**[8:23]** 240 so the address will be 192.168.1.0 and the subnet mass will be

**[8:31]** 255 do 255.255 do2 40 so that means I am going

**[8:40]** to consume four bits for host and 28 bits for

**[8:48]** Network because my IP V4 address is of 32 bits so out of these 32 bits only

**[8:57]** four bits are being used as host and rest 28 are being used for Network so we can also specify in

**[9:06]** another format 192.168.1.0 sl28 so this is called

**[9:15]** cidr notation so IP address can either be specified in a subnet MK mask notation

**[9:24]** or they can be specified as cidr notation one and same thing so our network is

**[9:35]** 192.168.1.0 sl28 so this 28 is basically 255 do

**[9:44]** 255 255 240 now let's calculate the block so

**[9:51]** block is calculated with the help of incomplete octat so here the fourth OCT is incomplete

**[10:00]** rest all are complete 255 is the last value which this octet can have so

**[10:07]** subtract it from 256 so 256 minus 240 this gives me the value 16 so 16 is my

**[10:16]** block size so the first address in the block is my network address

**[10:26]** 192.168.1.0 this is the first address and the last address in the block will be my broadcast

**[10:34]** address which is 192.168.1.5 so these are the addresses

**[10:45]** for my network so 192.168.1.0 is the network

**[10:52]** address 192.168.1.5 is the broadcast address

**[11:02]** first machine will have 192.168.1.1 as the address and the last machine will be

**[11:12]** 192.168.1.10 because I had only 10 machines in my network but we have few more addresses

**[11:21]** 112 13 and 14 so these four addresses are going to get faced if we are going

**[11:28]** to use C IDR notation in order to address 10 machines on the network so

**[11:35]** these addresses are being used at Network layer so the network layer is going to

**[11:44]** form a packet this packet will have Source IP address which is the address of my

**[11:51]** client machine and this will have destination IP address the address of the server machine and it will have the

**[11:59]** data from the upper layer transport layer and application layer data so this particular layer is called

**[12:09]** host to host communication layer so this is going to address a host

**[12:18]** as a client and host as a server now once this packet is

**[12:25]** prepared as I told previously also the communication has to happen vertically down so from the network layer the data

**[12:34]** is going to get transported to the data link layer now what happens at data link

**[12:42]** layer now at data link layer pdu is called

**[12:50]** frame so the frames are going to get formed at data link layer and this is hardware dependent

**[12:58]** layer so that that means if I'm using WiFi then the frame format is different if I'm going to use wired Network the

**[13:06]** frame format is different but whether it is a WiFi network or a wied network one thing is very common that we'll have a

**[13:16]** source Mac address and destination Mac address so these Mac addresses are

**[13:23]** called physical addresses so IP addresses logical

**[13:32]** address which is at Network layer and Mac address is physical

**[13:43]** address which is at data link layer now if you want to uh just correlate this

**[13:49]** with some analogy so it's very similar that each of you have a mobile phone so your mobile number is is

**[13:59]** basically a logical number like if your mobile number is a

**[14:07]** 10 digigit number so this number will represent a logical number like if you change your uh cell phone and if you

**[14:16]** want to take a new number the same number can be utilized by somebody else so this is a logical number and then you

**[14:23]** have a physical number which is assigned to your mobile set this is called II

**[14:32]** number so this is your physical address on the same lines on a network we have a physical

**[14:39]** address and we have a logical address so logical addresses are at Network layer

**[14:47]** and physical addresses are at data link layer so that means when I want to go to

**[14:54]** a data link layer I have to form a

**[15:02]** frame now frame is being formed with the help of source Mac address and destination Mac

**[15:11]** address now source Mac address or a destination Mac address these Mac addresses are of 48

**[15:19]** bit so this is a 48 bit number which is a hexad decimal notation

**[15:27]** it is defined in a hexad decimal format like 0 0 colon a0 colon C 0 colon

**[15:38]** AB colon CD colon 01 so this is a typical Mac address now this Mac address

**[15:47]** has two parts one is called the manufacturer another is the serial

**[15:54]** number so first three bytes of a MAC address is going to have OEM

**[16:05]** specification so OEM is original equipment manufacturer so the first three bytes represents OEM so this card

**[16:14]** can be from Cisco it may be from Intel it may be from dink so this is the number which will represent that company

**[16:22]** and after that three bytes they will represent the serial number of the net

**[16:28]** network card so that means we have a MAC address which basically gets mapped to the IP

**[16:36]** address which is again going to get ma to the address which is represented in the

**[16:44]** address bar of a browser so this is complete hierarchy which is being followed from an

**[16:51]** application layer to data link layer whenever we want to Traverse or whenever we want to surf internet

**[16:59]** that means from an application layer we specify a string why we specify string because we

**[17:08]** as a human being are very good at remembering names we are not good at remembering numbers but as a machine

**[17:15]** computer system only works on numbers so we need to convert this naming convention into the number convention

**[17:23]** and vice versa the number convention gets translated into naming convention so that that human and machine can work

**[17:31]** together so we specify a string like www do

**[17:40]** google.com now the computer doesn't understand what is www.google.com so it asks me to get some

**[17:48]** logical number for this so This logical number is given at Network layer so

**[17:55]** there will be one IP address which is being given to www.google.com now this IP address will

**[18:03]** finally get converted into a MAC address which is the address being specified on that particular host

**[18:13]** so that particular host will have a 48-bit number and that number will represent the MAC address now as an

**[18:21]** experiment if you want to see what is my IP address and what is my Mac address it's very simple you need to go to the command prompt

**[18:29]** and at the command prompt you enter a command called ip config

**[18:36]** /all now this is going to yield IP address and Mac addresses for your interface like here in this case if

**[18:46]** you can see this we have an IP address assigned to this machine 1921

**[18:54]** 1681 2351 and this is the subnet mask so this is the IP address and subnet

**[19:01]** 19 minutes, 1 second mask combination on this particular machine as well as if you can see

**[19:06]** here this is your physical address 00

**[19:13]** 5056 01 so this Mac address is the physical address of this particular machine so these addresses are unique so

**[19:23]** that means this unique address gets translated into ipv4 address which again gets translated into

**[19:31]** some name like www.google.com this is how we can see the IP addresses now let's say I want to

**[19:39]** know what is IP address of www.google.com so you simply type ping

**[19:46]** this is a ping command there is a command whenever you are got connected to the internet you give command P

**[19:53]** followed by www.google.com now you see it pops up an address now

**[20:02]** you would be very familiar about this address this is 1731 1941 126.80 so this is the IP

**[20:12]** address which is assigned to www.google.com at this point of time so this IP address by virtue of this IP

**[20:22]** address I'll be able to make a frame so let's copy this address

**[20:29]** and make a frame copy now let's create a network

**[20:37]** packet first then we are going to form a frame so in the network packet we'll have a source IP address which is the IP

**[20:46]** address of my machine and then we have a destination IP which is the IP which we have got

**[20:55]** from Google so this is the IP address which is get going to get translated here in the destination field so in the

**[21:04]** destination field we'll have this IP address now then this packet goes to the data link layer now what is the job of a

**[21:13]** data link layer data link layer is going to translate the packet which has come from a network

**[21:21]** layer and makes a frame out of it now one common mistake which is made

**[21:29]** by students is that the frame Mac address source Mac address is the MAC

**[21:36]** address of the client and destination Mac address is the address of the server which is not actually the case this

**[21:45]** destination Mac address is the MAC address of your gateway now let's learn this concept

**[21:54]** that why this destination Mac address is not of the server but this Mac address is of the

**[22:01]** 22 minutes, 1 second Gateway now as previously we had done let's take the same example 192.168.1.1 let's say this machine wants

**[22:10]** to talk to 192.168.1.3 machine now the first thing which is

**[22:18]** being done by your computer is it's going to calculate the network address of both of these

**[22:26]** addresses if the network address is same in that case we are going to request the

**[22:34]** physical address from the Machine by way of broadcast let's see how this

**[22:41]** communication will happen

**[22:44]** [Music]

**[22:48]** 192.168.1.1 wants to talk to 192.168.1.3 so that mean this machine

**[22:58]** knows about the IP address of another machine so they are at which layer they are at Network

**[23:06]** layer because Source IP is also known and destination IP is also

**[23:12]** known now in order to make a frame I would require a source Mac

**[23:20]** address and I would also require a destination Mac address so the source Mac address will

**[23:27]** be the MAC address add of my machine so I can get it from IP config /all command

**[23:35]** so that Mac address will go here now what about this Mac address now if the machine is on a same network it is going

**[23:43]** to request the MAC address of another Machine by way of

**[23:52]** broadcasting now this broadcasting is called as ARP broadcasting AR RP stands for

**[24:01]** 24 minutes, 1 second address resolution protocol so if machine knows the IP

**[24:10]** address of another machine it can only be at Network layer now because it has to go down to the data link layer in

**[24:19]** order to access the frame so it needs to acquire Mac address and Mac address can be require

**[24:27]** acquired with with the help of ARP which is called address resolution protocol so my machine is going to send a ARP

**[24:39]** broadcast and another machine 1.3 in our case is going to reply back with ARP

**[24:47]** reply which is unicost that means my machine is going

**[24:55]** to say that what is Mac address of 1.3 then 1.3 is going to say back that

**[25:03]** my Mac address is 00 0 0 0 C the whole 48 bit

**[25:10]** number now with the help of this 48-bit number my machine will be able to form a frame and with this Frame I'll be able

**[25:20]** to go to the data link layer so that means we'll specify a string that that

**[25:28]** string is converted into some logical number which is called IP and this IP is going to get converted into a physical

**[25:37]** address now this is the case when we are on a same network now if we are on a different network this Mac address will be the MAC

**[25:46]** address of router so this we are going to explain in the next lecture that what is a

**[25:52]** router for this lecture let's first of all understand what we have learned so far for so that we can recap

**[26:01]** 26 minutes, 1 second this so in this lecture we understood that classful addressing scheme wastes

**[26:08]** IPS so we can adapt to cidr notation now this cidr notation is going to help us to lower

**[26:17]** down the wastage of IP addresses so as the number of machines are required those many bits can be chosen from the

**[26:26]** IP address and then we need to calculate the network address and broadcast address so we learned about how to

**[26:34]** calculate the network address broadcast address first host address last host address

**[26:41]** also we found out that after knowing this addresses we need to get a MAC address so that we'll be able

**[26:51]** to prepare the frame so Mac address would be delivered with the help of ARP protocol which is called address

**[26:59]** resolution protocol and this Mac address is of 48 bits now out of these 48

**[27:07]** bits first three bytes that means 24 bits will represent the OEM which has manufactured this

**[27:16]** particular card and then next 24 bits they will represent the sequence number

**[27:25]** sequence number of the card getting produced this is how the machines are going to talk from an application layer where we

**[27:34]** are going to specify just a string and then the network layer in between there is a transport layer which

**[27:41]** is responsible for specifying the process addresses so process addresses were called Port

**[27:48]** addresses and then we have a network layer which is going to address the IP and finally we have a data link layer

**[27:56]** which is going to tell us about Mac addresses so each of these layer transport layer is called process to

**[28:04]** process communication Network layer is called host to host communication and data link layer is

**[28:12]** called node to node communication so with these Concepts we are ready to

**[28:21]** go into the topic which is called security and we learn about how these

**[28:27]** addresses are helpful in order to get to a particular host and there are certain terms which will come up like we can

**[28:36]** spoof these IPS and how this spoofing is done that is a part of the next lecture

**[28:42]** thank you thank you very much
