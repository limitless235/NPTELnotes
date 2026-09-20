# VoIP Protocols

**Module 45**  
Duration: 32:06  
Video: https://www.youtube.com/watch?v=-ArpkvGMndk

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Lal Chand, Department of Computer Engineering, Punjabi University, Patiala

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** hello viewers I welcome you to the lecture series on cyber security information security today we will

**[0:07]** discuss about V IP protocol that is voice over IP protocol so to start with

**[0:14]** a question arises that what is viip we know that voice can be digitalized the digitalized voice can be transmitted in

**[0:23]** packets over the network Voice transmission comes in the different flavors in the past t communication

**[0:30]** through fixed circuit switch network has dominated in recent years we see data communication Network especially voice

**[0:39]** over IP if you have never heard of VI IP get ready to change the way you think about longdistance phone

**[0:47]** calls viip or voice over Internet Protocol is a method for taking analog

**[0:54]** audio signals like the kind you hear when you talk on the phone and turning them into the Digital Data that can be

**[1:02]** transmitted over the Internet voiceover Internet Protocol is the methodology and group of Technologies for the delivery of voice

**[1:11]** Communications and multimedia sessions over Internet Protocol networks such as Internet Voiceover IP is the

**[1:20]** transmission of voice traffic in packet using the internet as the transmission medium IP is used rather than the

**[1:29]** traditional circuit transmission viip is defined in the

**[1:34]** recommendations it u t h. 32x and RFC

**[1:42]** 2443 why viip the Internet Protocol is used to deliver packets carrying digitalized voice however IP was not

**[1:52]** designed for realtime traffic such as voice and video communication IP is the connectionless

**[1:59]** protoc call meaning a virtual connection is not established through a network prior to

**[2:06]** transmission IP makes no guarantees concerning reliability flow control error detection or error correction

**[2:14]** potential errors include out of sequence packets or even loss of packets Voice transmission requires guaranteed

**[2:22]** connection and a reasonable delay nevertheless IP succeeds partially due to the high cost Associated we the

**[2:30]** traditional circuit switch TDM Network viip uses packet switch Network

**[2:38]** it makes the network transparent to the upper layers that are involved in Voice transmission through an IP based Network

**[2:47]** the existing use of IP network also allows the integration of voice and data integration to leverage the

**[2:54]** connectionless nature of Ip vendors have developed higher layer protocols to address the guaranteed connection and

**[3:01]** 3 minutes, 1 second transmission issue viip and OSI model viip follows a layered model comparable

**[3:09]** to the OSI 7 layered model we are familiar with just like the purpose of developing The OSI model breaking into

**[3:17]** defined layers provides a framework it establishes a standard to make the system more manageable and

**[3:25]** flexible each layer is relatively independent to other layers around it changes made to one layer should have no

**[3:33]** or minimal impact on other layers what are the V protocols the two

**[3:40]** most generally used protocols for Vi area unit the itu normal h.323 and also

**[3:48]** the iatf normal sip each area unit signaling protocols that discovered maintain and terminate a

**[3:58]** VI decision Additionally the media entry management protocol mgcp provides a

**[4:05]** signaling and management protocol between viip gateways and ancient pstn public switch telephone Network

**[4:15]** gateways first protocol is itut h.323

**[4:22]** h.323 may be a comprehensive protocol underneath the itut specifications for

**[4:29]** for cation voice video and information across a network the h.323 specification includes

**[4:39]** many subprotocols h225 for specifying decision controls

**[4:46]** example decision setup and tear down h235 for specifying the protection

**[4:54]** framework for h.323 and also the decision setup up

**[5:02]** h245 for specifying media methods and parameter negotiations like terminal

**[5:10]** capabilities .450 for specifying supplementary services like decision hold and

**[5:17]** telephony h235 additionally provides security measures like authentication Integrity

**[5:25]** privacy and a few non repudiation support in h.323

**[5:32]** Communications it's designed to work seamlessly with different protocols like h245 and

**[5:41]** h225 a decision setup is secured through transport layer security TLS once established a decision

**[5:51]** management is initiated so secret writing and media channel data will be

**[5:57]** negotiated h. 32 two three utilizes RTP that is realtime transport protocol or

**[6:05]** rtcp that is realtime transport management protocol as its transport protocol that rides on high of UDP

**[6:15]** secret writing is performed among the RTP packet by thirdparty Hardware or at the network layer authentication

**[6:23]** underneath h.323 will be either radially symmetrical and ention based or subscription

**[6:32]** based for radially symmetrical encryption based authentication previous contact between the ACT entities isn't

**[6:41]** needed as a result of protocol uses defy Helman key exchange to get a

**[6:48]** shared secret identity between the two entities with relevancy the h. 235

**[6:56]** recommendation a subscription based Authentication needs a previous shared secret identity and their area unit

**[7:04]** three variations of this first password based with the radially symmetrical

**[7:10]** secret writing second password based with hashing and third certificate based

**[7:18]** with signatures second protocol is session initiation protocol that is

**[7:25]** sip sip may be a text based application layer protocol that addresses the signaling and session management among

**[7:33]** the packet telephone Network it's outlined in RFC

**[7:40]** 3261 sip uses a request response model in sip authentication and authorization

**[7:48]** area unit handled either by employing a lower layer theme or on a request By Request basis with the challenge

**[7:57]** response mechanism as sip may be a lightweight protocol its security capabilities area unit terribly

**[8:06]** restricted sip requests and responses can't be end to end encrypted as a result of message feels like the request

**[8:14]** and root ought to be visible to proxy servers that area unit gift in several Network architectures to make sure sip

**[8:23]** request area unit rooted properly voice information is transmitted in clear text over UDP and

**[8:32]** Communications protocol though sip supports s mbased secret writing exploitation digital certificates sure

**[8:41]** header feels employed in requests and responses can't be encrypted the Sip protocol depends on

**[8:48]** the transport layer security mechanisms like TLS or IP s to produce the desired security for the entire

**[8:57]** message third Pro protocol is Media entry management protocol that is

**[9:05]** mgcp mgcp is revealed by the media management social unit as RFC

**[9:13]** 3435 it expect that mgcp messages can be continuously be carried over Secure net

**[9:21]** connections as outlined within the science security design as outlined in RFC

**[9:28]** 2401 exploitation either the science authentication Heather outlined in RFC

**[9:35]** 242 or the science encapsulating security payload outlined in RFC

**[9:42]** 246 this enables for information connectionless Integrity origin authentication and no obligatory

**[9:51]** anti-replay protection of messages passed between the media entry that converts circuit switch traffic to pack

**[9:59]** based traffic and also the media entry controller that is mgc that dictates the

**[10:06]** service logic of the traffic next is processing in VIP system at the cender aspect analog voice

**[10:16]** signals area unit reborn into digital signals compressed and so set into a planned format exploitation voice codec

**[10:24]** like g.711 g729 and g723

**[10:32]** Etc next the encoded voice is softened into equal Siz packets moreover in every

**[10:40]** packet headers from completely different layers area unit hooked up to the encoded voice the protocol headers

**[10:48]** accessor to voice packets area unit of RTP UDP and signs further as link layer

**[10:57]** header the packet area interet then sent over the network IP to its destination

**[11:03]** wherever the Des forment and deacetalization of the received packets is disbursed throughput the transmission

**[11:13]** method inference time variation of packet delivery might occur hence a playout buffer is employed

**[11:22]** that smoothens the playout at the receiver finish which can have a delay caused as the result of

**[11:30]** interference packets area unit cued at the playout buffer for a stipulated time before being

**[11:38]** y however packets that arrive later than the playout time area unit

**[11:44]** discarded viip uses the sign protocol specifically session initiation protocol

**[11:51]** that is sep and H Point 323 these sign protocols area unit needed to a certain View new IP calls

**[12:00]** and to shut the media streams between the purchasers another important topic to discuss is quality of service qos in

**[12:09]** viip qos is employed for mensuration of the degree of user satisfactions in

**[12:16]** different words quality of service will be outlined because the network ability to produce smart services that satisfy

**[12:24]** its customers once degree of user satisfaction is over it mean that Qs is additionally

**[12:32]** higher Qs area unit shortly represented as given below delay delay will be outlined because the

**[12:41]** total time it takes since an individual act another person speak words and

**[12:48]** hearing them at the opposite finish delay will be classified into three categories delay at the supply delay at

**[12:57]** the receiver and and network delay Jitter variation in transmission

**[13:05]** delay is thought as interference science network doesn't guarantee of package delivery time that introduces variations

**[13:13]** in transmission delay and its additional negative effects on voice quality packet laws packets transmitted over science

**[13:22]** network is also lost within the network or arrived corrupted or late packets would be discarded guarded after they

**[13:30]** arrive late at the interference buffer of the receiver or once there's overflow in the interference buffer or router

**[13:36]** buffer therefore packet loss is adequate the full loss happens throughout congestion of network and late

**[13:44]** arrival throughout the packet loss the sender is aware to conduct the Lost packets it causes additional packet

**[13:52]** delay and it affects the transmission Qs Eco in VII

**[13:59]** Eco happens once a caller at the center aspect hears the reflection of his own voice once he talked on the phone or the

**[14:09]** electroacoustic transducer whereas the coli doesn't notice the Eco Eco is that

**[14:16]** the term of the reflections of the scent voice signal by the way finish Eco May will be electrical Eco that exists in

**[14:25]** pstn networks or Eco of sound that is difficulty in viip networks

**[14:33]** throughput the output is also outlined because the most range of bits received out of the full range of bits sent

**[14:42]** throughout associate degree interval of your time next topic we are going to discuss is viip

**[14:51]** Security First is viip attacks threats attackers typically Target some

**[14:58]** fashionable and wellknown systems and applications viip has become one in every of such

**[15:05]** application viip like every another system or applications have its weakness therefore protocol designers ought to

**[15:13]** address it before with the success putting in viip on a universal scale thus this section presents a study of

**[15:22]** attacks on the viip Dos denial of service dos attacks that reduces the

**[15:30]** quantity of obtainable science addresses information mayor and different router

**[15:36]** functions a DS attack typically blocks the service of the server a viip based

**[15:43]** mostly DS attack bombards a decision process application with the massive amounts of coincidental requests that it

**[15:51]** cannot method inflicting the motility down of the appliance thereby denying service to approved or supposed

**[16:00]** users DS attacks will be directed toward any network part to disrupt these systems

**[16:08]** practicality Network sniffing Network sniffing attacks occur

**[16:15]** once a personal or offender is observant the network traffic patterns typically

**[16:22]** any system user or attacker on a network that's sharing a transmission medium has the power how to look at different

**[16:30]** systems traffic eavesdropping eavesdropping is a shot towards assembling sensitive data to

**[16:38]** arrange for a Cyber attack or to achieve intelligence in viip E dropping maybe a

**[16:45]** situation wherever the offender is in a position to watch signal or media contents that area unit changed between

**[16:53]** users so as to look at communications to arrange for different future attack ta

**[17:01]** 17 minutes, 1 second spoofing one of the kinds of viip spoofing is display spoofing wherever the offender

**[17:08]** masqueraders itself as a licensed viip user and places a decision the display that seems on the

**[17:16]** user aspect seems authentic even supposing the offender is exploitation unfair means that the offender will

**[17:25]** currently trick the user in giving for free sensitive information spoofing is thus the VIP

**[17:32]** version of ancient fishing toall fraud tall fraud is that

**[17:39]** the ability to possess associate degree unauthorized access to the VIP Services typically for financial gain for VIP

**[17:48]** suppliers this is often one in every of the for most essential attacks toall FR

**[17:56]** will be recognized by the manipulating the sign messages or the configuration of VIP Parts together with the charge

**[18:04]** systems spam over net telephone that is spit due to its a lot of lower

**[18:11]** communication prices VIP network has become additional engaging as another to

**[18:17]** this bstn further as a target for spammers viip spam may be a recorded

**[18:25]** self- dialed phone calls exploitation foration net protocol VIP spam

**[18:32]** additionally called spam over net telephone that is spit is popping Dead Set be a significant downside for VIP

**[18:42]** networks spit is additional sever that your email spam due of its assaultive nature which needs a period defense

**[18:51]** reaction what is the security measures for viip according downside on DUS there has been a report that sure

**[19:00]** viip phones area unit Lael to each do attacks and sure viip routers also are

**[19:08]** at risk of malicious Traffic Solutions to avoid a DS attack

**[19:15]** monitoring and filtering to take care of list of suspicious users and deny those users from getting any connection or

**[19:24]** session authentication to ATT test the identity of a US user before forwarding his or her messages through the

**[19:33]** network stateless proxy to lower the risks of memory exhaustion du as

**[19:40]** homeless proxy will be accustomed to perform different Security checks like user authentication third party

**[19:48]** registration and filtering spam sources server style to create computer

**[19:55]** hardware memory and network affiliation the primary line of defense against any dos

**[20:03]** attacks reported downside on EES dropping an Internet Security Systems

**[20:10]** team discovered the issues in viip system during a vendor decision manager the vendors offer associate

**[20:19]** degree offender the power to concentrate in or forward calls additionally to gain unauthorized access to networks running

**[20:27]** on VI answer to eavesdropping employing perfect

**[20:34]** Hardware only approved forx or to tend access to wiring

**[20:41]** closets vulnerable Network purpose or to implement a port based mostly waterproof

**[20:48]** address security for instance on a reception ctsy phone a method ought to often scan the

**[20:57]** network of devices is running in unauthorized mode another answer is secret writing of

**[21:05]** viip traffic reported downside on spoofing there are many reports that Banks and

**[21:13]** online payment services were victims of attack wherever the offender referred to as a credit card client and receiv

**[21:21]** received the purchases into giving for free sensitive data relating to their accounts by declaring that there had

**[21:28]** been dishonorable activity on their accounts solution to spoofing an effective authentication module combined

**[21:37]** with secret writing would be an efficient answer to spoofing and masquerading

**[21:44]** attacks reported downside on tall fraud tall fraud threat is commonly most

**[21:51]** vital within the eyes of enormous organization an eminent theory of service from from an outsized

**[21:59]** organization will go unnoticed for quite your time permitting the offender to rack up an outsized bill at the

**[22:08]** organization's expense but tall fraud is additionally quite simple to accomplish a straightforward configuration downside

**[22:18]** within the dial set up with leave lines open for check purpose associate degreed remote exess will be abused by an

**[22:26]** offender it t but profitable from the purpose of fre of the offender to commit tall fraud as a result of once the

**[22:36]** attack is over the offender will abuse the service quite speedily by reselling them with no real prices concerned from

**[22:45]** the attackers aspect solution to tall fraud viip suppliers will stop tall

**[22:53]** fraud by configuring powerful Fireballs that stop attacks and by protective the

**[23:01]** 23 minutes, 1 second ports reported downside on spit it is potential Network for an offender to

**[23:09]** impersonate as another VIP caller for instance associate degree offender May

**[23:15]** probably inject a pretend ID into a standard VIP decision so the receiver mistakes the decision to be real and

**[23:24]** coming back from a best known and short supply the receiver mistaken by the electronic

**[23:32]** ID of the caller might Place unwarranted trust within the person at the opposite finish in such a communication the

**[23:41]** receiver is also hawed into revealing personal data like account number SSN or

**[23:48]** answers to security questions a mother's family name for instance solution to spit a normal blacklisting approach l

**[23:58]** through all the calls coming back from the best known Science address VIP vendors additionally give security

**[24:06]** measurements to Dam suspicious callers above all receiver ought to be allowed to not break any vital data to

**[24:15]** the offender next topic is configuration of viip adapters USB viip phone adapters

**[24:25]** enable USA to use any as ient telephone to position VIP calls they typically

**[24:33]** appear as if USB adapters these USB adapters have a typical standard Telephone Phone Port so

**[24:42]** that one will connect a daily connective once hooked up your phone operates as if connected to traditional

**[24:51]** public utility software controlled VIP applications soft phones soft phone's area unit phones

**[25:00]** that enable USA to create viip phone calls directly from a PC that has a web

**[25:07]** affiliation soft phones build decision with the assistance of a laptop telephone receiver and a sound card a

**[25:15]** soft phone sort of a traditional phone just with the distinction that the affiliation is coming back from your

**[25:23]** laptop viip suppliers devel soft phones for free of charge in exchange of availing their

**[25:30]** service code controlled VIP application permits users to speak to others dedicated VIP phones

**[25:40]** exploitation these services at no further price a viip phone feels like a

**[25:47]** daily telephone an evid viip phone connects on an electronic network instead of a standard telephone line an

**[25:56]** evid VIP phone May match in two ways that a phone and a base station that

**[26:04]** connects to the net it should operate on a neighborhood wireless network dedicated viip phones need a

**[26:13]** supplier further as a service setup dedicated routers these routers in viip enable

**[26:22]** user to attach standard phones to the net to position VIP calls wherever the

**[26:29]** router is connected to associate degree ADSL cable electronic equipment and

**[26:36]** permit users to connect a standard telephone viip routers have the extra practicality of associate degree science

**[26:45]** router as that permits USA to attach to the laptop further viip suppliers piece

**[26:53]** these routers underneath a particular setup for a charge these routers may also perform their functions freelance

**[27:01]** 27 minutes, 1 second of any PC or any code Wireless compatibility of

**[27:07]** viip with the wireless router mobile devices and smartphones may also use the

**[27:14]** viip system if you put in a wireless computer network you would like a applicable security like a firewall or

**[27:23]** secret writing problems with wireless VIP VIP on computer network is deployed

**[27:31]** principally in company environments like in corporations instead of homes Wireless VIP poses issues of

**[27:40]** measurability for Enterprises as just in case with all wireless network quality of service is

**[27:48]** poor compared to wide networks setup price and maintain prices higher during a wireless VIP

**[27:56]** Network due to variety of exess points among the restricted space of network security threat is higher over a

**[28:05]** wireless VIP Network limitations of viip the popularity of viip can rely

**[28:13]** upon some key problems a number of these problems area unit a resultant of the very fact that science was designed for

**[28:22]** information packets whereas some problems stem from vendors that don't seem to be Mee meeting the Necessities to the

**[28:30]** standards the key problems area unit mentioned as follows quality of service the design of science doesn't guarantee

**[28:39]** realtime transmission of voice packets as science was designed for information packets that guarantee error-free

**[28:48]** ordered delivery of information packets acceptableness of viip depends

**[28:55]** on delay that should not exceed a given threshold worth prioritization of packets means

**[29:03]** that giving voice packets high priority will guarantee smart quality of voice

**[29:11]** interoperability you need to Interchange the sign mechanism of pstn with viip sign mechanism if you wish to create

**[29:19]** viip common among net users a number of the suitable sign mechanisms area unit

**[29:27]** h. 3 to three standards sip protocols and mgcp every of those protocols integrates

**[29:36]** information voice and video over constant wire security the question of security arises as a result of the

**[29:44]** backbone of uip is that the net that isn't a really secure medium there will

**[29:51]** be interception of calls due as fraud Security will be provided by exploit ation tunneling protocols like

**[30:00]** layer to tunneling the secret writing mechanism used in Secure sockets layer

**[30:07]** that is SSL however secret writing isn't wide out there for viip integration with

**[30:14]** public switch telephone Network that is pstn viip Works in Union with pstn and

**[30:22]** that they seem as one network to the users of the service in viip technology your telephone number has associate

**[30:31]** degree Science address therefore anytime a viip phone engages during a decision

**[30:38]** its Science address is translated into the telephone number and two-handed over to the pstn network you would like to

**[30:48]** mix of each viip a pstn as a result of not everybody has switched to viip and

**[30:55]** their area unit are closer range of users still exploitation pstn

**[31:03]** scalability since calls over science have lower price and also the work on the rising the standard of voice further

**[31:11]** as transmission goes on there has been a high rate in VIP users the most obstacle lies in its

**[31:19]** measurability so viewers in today's lecture we discussed viip Protocols of viip Qs in viip and and security

**[31:28]** implementation on viip we also discussed the security measur and configuration of

**[31:35]** viip we will discuss the VIP protocols in detail in forthcoming lectures thanks

**[31:41]** for watching this program thank you
