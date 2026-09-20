# Introduction to DDoS

**Module 46**  
Duration: 21:49  
Video: https://www.youtube.com/watch?v=jEYv9HSp8lU

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Abhinav Bhandari, Department of Computer Engineering, Punjabi University, Patiala

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:16]** dear viewers today we are going to discuss one serious kind of Cyber attack known as distributed denial of service

**[0:23]** attack we will try to explore about introduction of Dos attacks motivation behind these attacks

**[0:30]** what are the consequences of these attacks vulnerabilities in the basic protocols that can be exploited by the attackers to launch these attacks and in

**[0:39]** the last part of the lecture we will discuss about the classifications of these attacks there has been a tremendous

**[0:47]** growth of Internet especially in the last decade in terms of its usage that has led Our Lives to become increasingly

**[0:54]** dependent on the internet the internet has become essential for information flow business Commerce communication

**[1:02]** education entertainment and research activities initially the major goal of the internet development was to enhance

**[1:10]** the unobstructed flee flow of data and scalability without keeping mind the security issues which now appears to be

**[1:18]** pricious its architectural design Was Made Simple for ease of usage but subsequently it fascinated the attackers

**[1:26]** who exploit the vulnerabilities and launch a variety of attacks for plethora of reasons these threats can Target

**[1:33]** basic CIA model of security which deal with confidentiality of data Integrity of data and availability of services

**[1:42]** availability of services is primarily targeted by launching a denial of service attacks which is characterized by an explicit attempt by attackers to

**[1:51]** prevent legitimate users of service from using that service denial of service attacks has undoubtedly take over taken

**[2:00]** all concerns and has emerged as arguably the most severe form of attacks in the last decade the major goal of Dos

**[2:08]** attacks is to disrupt or deny the services for numerous reasons think out a situation you are a reputed online

**[2:15]** shopping company and suddenly your web service becomes unavailable to the customers when you deeply investigate

**[2:22]** you realizes that a flood of packets is surging into your network you have just become one of the hundreds or thousands

**[2:30]** of victims of denial of service attacks a pervasive and growing threat to the internet traditionally the security

**[2:38]** Community has focused its attention on unauthorized disclosure or modification of information and perhaps theft of

**[2:46]** services denial of service was largely ignored as being unlikely to occur because the characters would not gain

**[2:53]** anything from such an attack clearly this is not the case today denial of services can be devast deating attack it

**[3:01]** 3 minutes, 1 second can put Merchants out of business and can cause major and very visible disruption to our cyber world it can be

**[3:08]** used against specific companies for which the attacker has a grudge or has been paid to attack or it can be used by

**[3:15]** terrorists to cause major disruption to critical intermediate and victim

**[3:23]** infrastructure this type of attack may include attempts to flood a network disrupt connections between two machines

**[3:30]** disrupt service to a specific system or person thereby preventing legitimate Network traffic to assess Network server

**[3:38]** service or website thus a denial of service attack aims to deny assess by legitimate users to Shar services or

**[3:47]** resources such an attack can be configured in many ways like targeting operating system or Network

**[3:53]** Services the first way targets to crash a system by sending one or more carefully crafted packets that exploit

**[4:01]** 4 minutes, 1 second software vulnerabilities On Target server for example the Ping of death attack that sends large International

**[4:08]** control message protocol ping packets that is fragmented into multiple datagrams to Target system which can

**[4:15]** cause certain operating systems to crash freeze or reboot due to buffer overflow the second way is known as

**[4:24]** flooding type of Dos attacks that employs massive volumes of useless traffic to occupy all the resources that

**[4:31]** could hamper service to legitimate traffic while it is possible to prevent the first form of attack by patching non

**[4:39]** vulnerabilities however the second form of attack cannot be easily prevented the targets can be attacked simply because

**[4:46]** they are connected to the public internet next comes the bigger version of denial of service attacks called

**[4:53]** distributed denial of service attack when the traffic of Doss attacks comes from multiple sources it is is called

**[5:00]** distributed denial of service attack by using multiple sources the power of a Dos tax is Amplified and the problem of

**[5:07]** defense is made much more complicated both dos and dos are a huge threat to the operation of internet sites but the DS problem is more complex

**[5:17]** and harder to solve because of the following reasons first it uses a very large number of machines this yields a

**[5:24]** powerful weapon any Target regardless of how well provisioned it is can be taken offline Gathering and engaging a large

**[5:32]** army of machines has become terbly simple because many automated tools for DS attacks can be found on hacker web

**[5:40]** pages and in chat rooms such tools do not require sophistications to be used and can inflict very effective damage a

**[5:49]** large number of machines gives another advantage to an attacker even if the target were able to identify attacking

**[5:56]** machines and there are effective ways of fighing this information what action can be taken against a network of 1,000

**[6:05]** host the second characteristics of some of the Dos attacks that increase their complexity is the use of seemingly

**[6:12]** legitimate traffic resources are consumed by large number of legitimate looking messages when comparing the attack messages with legitimate one

**[6:21]** there are frequently no feature to distinguish them since the attack misus a legitimate activity it is extremely

**[6:28]** hard to respond to the attack without also disturbing this legitimate activity look at the figure which shows the

**[6:35]** complete modity of the DS attack the operating system and the network Protocols are developed without applying security engineering which results in

**[6:43]** providing hackers a lot of insecure machines on the internet these insecure unpatched machines are used by Doos

**[6:51]** attackers as the Army to launch attack an attacker or a hacker gradually implants attack programs on these

**[6:58]** insecure machines depending upon sophistications and logic of implanted programs these compromised machines are called Master's

**[7:07]** handlers or zombies and collectively called Bots and attack network is called botn net in the hackers

**[7:14]** Community hackers send control instructions to the Masters which in turns communicate it to zombies for launching

**[7:22]** attacks the zombie machines under the control of Masters and handlers as shown in the figure transmit attack attack

**[7:29]** packets which converge at victim or its Network to exhaust either its communication or computational

**[7:38]** resources numerous incidents of Dos attacks are common these days from a normal client users to business communities isps and also the world

**[7:47]** famous companies such as Yahoo Twitter Facebook eBay Google are the victim of desort attacks a few recent and famous D

**[7:56]** do incidents are shown in the table the table describes about the incidents in chronological order right from 2000 to

**[8:03]** 2014 along with the description of attacks it is curled from the table that dos attacks is a sensitive issue

**[8:11]** prevailing among the cyber community and also it has been analyzed from the recent security reports that these attacks have gained a lot of strength in

**[8:20]** recent years that is from 2014 onwards as compared to earlier before year 2005

**[8:27]** the attack size was less than 10 gbps and in 2010 it is reached a mark of 100 gbps furthermore the attack size was

**[8:35]** observed up to 400 gbps in 2014 which shows the severity of problem over the internet now the question comes in our

**[8:44]** mind that why a tackle launch such kinds of attacks what are their motives so in this coming discussion we will be exploring some of the key factors that

**[8:53]** contributes towards launching of these hostile activities on the internet first point to be discussed about his

**[9:00]** recognition some of the early dots attacks were largely proofs of Concepts or simple pranks played by hackers the

**[9:08]** ultimate goal was to prove that something could be done such as taking a popular website offline such a major achievements brings an attacko

**[9:16]** recognition in the underground cyber community next is ideological activism another frequent motive of Dos attacks

**[9:24]** is self-described as being political individuals or groups who disagree with views or actions of certain organization

**[9:31]** an online media site a corporation or a government have been known to launch dos attacks against computers and networks owned by this

**[9:40]** organization financial gain can be another factor which motivate the attackers through the monetary gain to launch several kind of Dos attacks after

**[9:49]** launching these attacks they may also demand for ransome amount of money to prevent further attacks the attackers

**[9:56]** involved these types of are most experienced next is vandalism the motive of this category of attacker is to destroy the

**[10:05]** available resources as they don't believe in anything and are senseless according to the recent reports the attackers related to this type of

**[10:13]** attacks have been increased recently lastly revenge or competitive spirit in the business attackers May

**[10:21]** launch the Dos attacks to take the Revenge the attackers may be employees of certain organizations that were

**[10:28]** Dishonored in some dispute however there is a major lack of data on preparators and motives of Dos attacks

**[10:35]** the vast majority of attacks are not reported in further discussion we will be exploring what are the consequences of these

**[10:43]** attacks the consequences of do attacks may be very severe it depends on the kind of attack launched by the attackers

**[10:50]** the organization and the target of the attackers the long duration dos attacks are more rigorous and these must be

**[10:57]** mitigated quickly after detection DS attacks may lead to the following consequences huge revenue losses

**[11:06]** reputation of organization may go down loss of shareholders confidence customers dissatisfaction loss of important data

**[11:15]** due to system crashes extra operational cost hence consequences of these attacks are so severe that it may lead to social

**[11:24]** financial and legal implication among the cyber community let's now discussed about the vulnerabilities present in our

**[11:31]** basic protocols and architecture that lead to perform this type of sophisticated attack firstly the stateless nature of

**[11:40]** the internet it means that intermediate routers do not maintain any straight information about the forwarded packets

**[11:48]** because of this accountability computer forensics are difficult to conduct that theft that Ur unidentified secondly there is a lack of

**[11:56]** authenticity over the internet without authentication malicious internet users can claim the identities of other users

**[12:04]** without being easily detected or located the most common example of this type of attack is IP spoofing where

**[12:11]** attacker can easily spoof The Source IP address of the another machine thirdly the deterministic nature of the Internet Protocol this is not a

**[12:20]** design flaw but is often necessary to proper operation of Internet protocols that is the TCP connection establishment

**[12:28]** procedure and TCP connection control mechanism the three-way handshake TCP mode mechanism which is predictable and

**[12:36]** can be easily exploited to launch flooding type of attack known as Sin flooding attack last but not the least is the

**[12:44]** mimicking legitimate user Behavior attackers can easily mimic the behavior of legitimate users which leads

**[12:52]** them to perform a kind of attack called application layer dos attacks in the last last part of the

**[12:59]** lecture we will be discussing about the classification of D attacks D do attacks may occur at every

**[13:07]** layer of USI model therefore these can be classified as follows as shown in the

**[13:14]** figure physical layer attack volumetric attacks application layer attacks so first comes the physical

**[13:22]** layer attacks also known as layer one attack these types of attacks are concerned with physical security these

**[13:30]** attacks includes the destruction obstruction malfunctioning or manipulation of physical assets at the

**[13:38]** physical level the communication relies on nodes host switches hubs routers and server and the medium of transmission

**[13:46]** that can be wired or Wireless if the devices through which the services are granted gets down there will be a disruption of

**[13:54]** services this target can be easily achieved if the signals are interrupted between communicating devices to prevent

**[14:02]** them from reaching to their destinations so the attackers May attain their targets of denying the services by

**[14:09]** compromising the physical security of the assets the various kinds of physical aay attacks destruction of

**[14:17]** Assets in this kind of attack the attacker may damage the physical assets or may cut down the backbone wires of

**[14:24]** local area network so that Services can be denied by this the availability of these assets could be reduced and there may

**[14:32]** become unresponsive resulting in denying of services to prevent such kind of an attack physical security of assets is

**[14:40]** required next is jamming the jamming attack is executed primarily in the wireless sensory

**[14:47]** networks jamers can be used by attackers to hamper the functioning of the wireless networks by generating noise

**[14:54]** signals close to the network by doing this the throughput of the network may fall drastically in Jing attacks packets

**[15:02]** may be corrupted by generating interference between the communicating nodes next is tempering the attackers

**[15:11]** May temper with the functioning of nodes by erasing all programs or by modifying the codes for assessing the information

**[15:18]** of high layers cryptographic keys and other sensitive information may be extracted by coming the nodes and

**[15:26]** keeping the packages temper approved the tempering attack can be prevented next category is volumetric

**[15:36]** attack also known as layer two to four attacks in this attack congestion is caused by consuming the bandwidth of the

**[15:44]** network through flooding attacks like mac flooding ICM flooding UDP flooding sin flooding

**[15:52]** Etc therefore these attacks cause high traffic to the network a large number of DS attacks variants fall under this

**[15:59]** category of volumetric attacks the basic protocol of this attack category is to congest the

**[16:06]** network or Target machine with large amount of packets that is flooding the target this results in total consumption of

**[16:15]** resources by the attacker moreover the targeted machine may become unresponsive and possibly it may crash

**[16:23]** completely the attacker transmit such kind of amount of data toward the target Target machine through well distributed

**[16:31]** and Scattered Bots that are remotely controlled by the bot Masters the key features of these attacks is the most of the IP packets

**[16:39]** used have spoofed Source IP addresses the spoofing of addresses in the IP packets protect the actual attackers

**[16:46]** from being traced back the different kinds of volumetric attacks are Mac flooding icmp flooding UDP

**[16:55]** flooding the attackers clone the Mac addresses and send a huge number of frames of data towards the switches

**[17:02]** besides the non-existing Mac addresses are used by The Tackle to alter the ARP

**[17:09]** caches switches have a certain memory that is used to handle the request and to reserve the resources for

**[17:16]** them when huge volume of forged requests are received by the switches it starts allocating the resources for the cloned

**[17:25]** Mac addresses and start denying the request to the legit M ones likewise it may also affect the routing tables of

**[17:34]** the routers at the network to drop the entries in the table which make the routing Services unavailable next comes the icap

**[17:43]** flooding icmp flood is the error control protocol in the network layer query messages are used to diagnose the

**[17:51]** network problem through icmp requests that are encapsulated into IP packet attackers send numerous ICM MP packets

**[17:59]** to the Target server with huge range of smoed source IP addresses the target servers in turn replies to these queries

**[18:08]** which results in consumption of bandwidth on the network consequently the network gets congested and becomes

**[18:16]** unresponsive Additionally the fragmented icmp packets are also used by the attackers with very high sending rating

**[18:24]** such that server gets overloaded by This Server key keeps resembling to fake data packets and

**[18:31]** legitimate users do not get the services Smurf attacks and the Ping of De attacks are the common example which make use of

**[18:39]** icmp protocol next is the TCP flooding the attackers exploit the vulnerability of three-way handshake

**[18:48]** mechanism in the TCB protocol of the transport layer to launch such kinds of attack sin flooding attack sin flooding

**[18:56]** attack fragmented acknowledgement packets are examples of TCP flood attack in sin flooding attack the attackers

**[19:04]** send large number of send requests to the Target server without spoof address to the establish the

**[19:11]** connection upon receiving the S request the server allocate the resources to each request and sends response with S A

**[19:19]** packets as responses of the server will not entertained due to the spoofed addresses and TCP 3way handshake

**[19:26]** connections remains in half open State till time out a very large number of such requests

**[19:34]** are sent by the attackers to make the target machine unavailable the scenario of sin while flooding attack is shown in the

**[19:43]** figure next is the UDP flood unlike TCP UDP is connectionless

**[19:50]** Protocols of Transport layer UDP packets are used by attackers to exhaust the bandwidth of network by launching the

**[19:59]** attack from distributed side with the help of bots attack converges high traffic towards the victim the Eco and the charging Services

**[20:07]** of UDP are generally exploited to launch such kind of attack other kinds of attacks which can be launched through UDP are DNS flood

**[20:16]** UDP fragmentation viip flood Etc final classification is based on the

**[20:24]** application layer attacks which are also known as layer five to layer 7even attacks in contrast to volumetric attacks these

**[20:32]** attacks generate low traffic at the network but send the large request to the web server hence these attacks can

**[20:40]** critically overwhelm the resources of the web server these attacks include HTTP get

**[20:46]** and post request flooding Etc various Protocols of the application like HTTP

**[20:53]** https and DNS Etc are being exploited by the attacker At Last I would like to conclude that

**[21:01]** 21 minutes, 1 second dos attacks is a devastating attacks among the cyber community though there are many commercial Solutions present in

**[21:08]** the market but the ideal solution to this problem is eluded so far in the next lecture we will discuss

**[21:16]** about the different approaches which by which we can tackle about the dasas problem thank you

**[21:43]** [Music]
