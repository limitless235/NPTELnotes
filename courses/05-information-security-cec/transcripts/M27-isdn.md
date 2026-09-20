# ISDN

**Module 27**  
Duration: 22:11  
Video: https://www.youtube.com/watch?v=xWRKLxEw-v4

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Lal Chand, Department of Computer Engineering, Punjabi University, Patiala

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:16]** hello viewers I welcome you to the lecture Series in cyber security and information security today we will

**[0:23]** discuss ISDN security ISDN that is integrated Services digital Network is a method to transfer voice data with some

**[0:32]** particular Services accessible for data ISDN is a set of CCI /it standards for circuit switch

**[0:41]** transmission of data over various media using ordinary telephone grade copper wire ISDN provide worldwide digital

**[0:49]** communication service in the transition to electronic documents and business transactions ISDN digital nature

**[0:57]** facilitates adding security but it has been deployed with a little thought to security ISDN provides digital circuit

**[1:05]** switched voice and data services as well as packet switch data services to users

**[1:12]** ISDN is a method to transfer voice data with some particular Services accessible for data history of

**[1:21]** ISDN before the coming of age of ISDN original analogy telecommunication Services also known as plain old

**[1:30]** telephone system PS were the only source of telecommunication worldwide PS was the originally acronymic for post office

**[1:39]** telephone service system but changed when the post offices stopped offering telephone services PS comprised mainly

**[1:47]** of copper wires which link the subscribers home to the central switch office this form of telecommunication

**[1:54]** had its limitations longdistance calls had to be rooted through operators and switchboards which made them highly

**[2:02]** unreliable and timec consuming there was also the issue of static inference known as the line noise which Disturbed

**[2:10]** communication in the 1960s the telecommunication industry began working on the converting its analog systems to

**[2:18]** transmit packets of digitized data by digital switching the United Nations International Telephone and Telegraph

**[2:25]** consultative committee now known as International telecommunication Union telecommunication iut actively pushed

**[2:34]** and encouraged the research for integrated Services digital Network by starting a movement to recommend and provide Sands for international

**[2:43]** digitization of the telecommunication services this was initiated in 1984 two major US networks Northern

**[2:52]** telecommunication and atnt took the first steps towards implementing ISDN but did not interoperate with existing

**[2:59]** equipments and software available to telecommunication networks this led to a setback for ISDN worldwide by 1990 due

**[3:09]** to the worldwide effort National ISDN 1 ni1 was made compatible with existing

**[3:16]** proprietary equipments for telecommunication services this way people did not need to switch brand or buy software for the network they set

**[3:26]** the standards and procedures for future digital telecommunic ation technology to be used by everyone ISDN has resulted in better

**[3:35]** voice quality and internet access due to its packet switch connection with ISDN voice and data are carried by a beer

**[3:44]** channel that is B Channel with a bandwidth of 64 kbps sometimes 56 kbps

**[3:52]** as opposed to telephone line which carry 52 kbps a data channel that is D channel

**[3:59]** is used for controlling Network Services and signaling to construct brake connections and carry data over the beer

**[4:07]** channels this carries a bandwidth of 16 kbps or 64 kbps for now the future of

**[4:15]** ISDN lies with Broadband ISDN that is B ISDN this entails transferring data

**[4:22]** voice and video all at the same time using fiber optic telephone line which can carry data rates from 155 Mbps to

**[4:32]** 622 MVPs and Beyond this is the major topic for research and development now

**[4:39]** we come to the types of ISDN there are two types of ISDN first basic rate ISDN

**[4:47]** that is B second primary rate ISDN that is p there are two services offered by ISDN

**[4:57]** this is known as the B and bi brri basic rate interface consists of 2 kbps beer

**[5:05]** channels and 11 16 kbps data Channel totaling 144 kbps as the name implies B

**[5:14]** usually has enough bandwidth for individual users PRI primary rate interface is used for clients that

**[5:22]** require greater bandwidth it usually comprised of 2 364 kbps B channels and

**[5:29]** one 164 kbps D Channel totaling 1.53 6

**[5:36]** Mbps sometimes the pr service can have 30 B channels and One D channel for a total of

**[5:43]** 1.98 4 Mbps brri has two Bearer that is B channels for transfer data which

**[5:51]** operate at 64 kbps each the other channel is known as the Delta D Channel

**[5:58]** and operates at 6 16 kbps the T channel is used for link management purposes and

**[6:04]** signaling this is known as 2B plus 1D PR depends on the country but a typical PR

**[6:12]** is 23 Beer channels that is B channels at 64 kbps for data and One D Channel at

**[6:20]** 64 kbps one format of the pr interface consisted of 24 DS zeros and looked a

**[6:29]** lot like channelized T1 circuit the PRI is similarly defined for international use where the fundamental historical

**[6:37]** transport bit rate is 2.48 Mbps sometimes called

**[6:44]** E1 in this case one of the 32 DS Z was already used for control purpose so

**[6:51]** there were only 31 available DS zeros for ISDN hence the format was 30b Plus D

**[7:00]** the major difference between a garden variety T1 and a PR is that the P normally has 23 channels used for

**[7:10]** transport of digital voice or data conversations called Bearer or B channels while the 24th channel was used

**[7:19]** for control called the data or D Channel thus a PRI ISDN circuits is often

**[7:26]** referred to as 23b plus d normally is inserted above because One D

**[7:33]** channel can control more than 23 B channels so it was also possible to have

**[7:39]** a 24b ISDN circuit so long as the control came from another PR so now we

**[7:47]** come to the features of isgn the major feature of isgn is that it put together speech and information on the same line

**[7:56]** which were not presented in the classic telephone system ISDN services are ability to deliver maximum data within the combination of

**[8:05]** voice data video facts over a single line while it provide at least two instantaneous connections ISDN make

**[8:13]** available access to packet switch networks because it is a circuit switch telephone Network system therefore it

**[8:21]** provides better quality of voice data than a analog phone user can attach several devices to the line according to

**[8:29]** their need instead of purchasing many analog phone lines the ISDN B channel is responsible to provide greater data rate

**[8:38]** so now we move on to the ISDN Services ISDN provide three types of

**[8:44]** services beer Services T services supplementary Services Telly and supplementary Services represent the

**[8:52]** type of features and functions which are visible to end users while beer Services represent the parts of the network which

**[9:00]** remain hidden from end users beer Services facilitate the realtime communication of digital information

**[9:07]** between end users these Services main relate to network functions and account for OSI layers 1 to 3 an example of the

**[9:16]** beer Services is that 64 kbps 8 KZ structured speed service this Services

**[9:24]** uses a data rate of 64 kbps together with 8 khz timing information which

**[9:31]** structures the data into octet intervals for transmitting a pulse code modulated that is PCM speech signal the fact that

**[9:40]** the signal represents speech is known to the network allowing it to employ Transformations which may not preserve

**[9:47]** bit Integrity but will result in good quality audio reproduction T services provide a set of higher level functions

**[9:56]** on the top of beerer services these services account for OSI layers 4 to 7

**[10:03]** examples of teleservices are telephony Services which provide speech communication over a b Channel with

**[10:10]** control signaling over the D channel f similar Services which facilitate the communication of bitmap images over a b

**[10:19]** Channel with controlling signals over the D Channel tetch Services which facilitate the interchange and

**[10:27]** communication of textual as well as formatted documents over a b Channel with control signaling over the D

**[10:34]** Channel supplementary Services enhance beerer and T services in an independent fashion examples of supplementary

**[10:42]** services are the Centre service emulates a private Network and provides a specialized feature to a set of

**[10:51]** subscribers The call transfer service allows a user to transfer an active call to a third party the call waiting

**[10:59]** service allows a user already engaged in a call to the informed of another incoming call the calling line ID

**[11:07]** service provides the calling parties address information to the called party although these Services all appear

**[11:15]** geared towards circuit switch telephone calls they are equally applicable to the packet switch data calls working of ISDN

**[11:24]** how does ISDN work one single transmission channel for communic ation is available in analog Network or

**[11:32]** regular telephone lines that are provided to us by telephone companies therefore only one service can be

**[11:39]** carried at a time that is voice data video at same time whereas in ISDN lines

**[11:47]** there are the same pair telephone lines are logically divided into multiple channels they are normally divided into two

**[11:55]** channels B channel is the first type of Channel 6 4 kbps of data can be transferred using B Channel normally

**[12:04]** ISDN lines possess two B channels one channel is dedicated for voice and the other is dedicated for data

**[12:13]** communication the data transmission takes place on one pair copper wire second type of channel is used for line

**[12:21]** and calling system setup is known as D Channel or Delta Channel also third

**[12:28]** Channel on the other hand have 16 kbps of bandwidth concept of ISDN line

**[12:35]** working with the help of image is as shown ISDN protocols components and

**[12:42]** routers option te1 that is terminal equipment type one this is the ISDN

**[12:49]** telephone computer ISDN fax machine or whatever it is that you have hooked up to the ISDN phone line te2 that is

**[12:59]** terminal equipment type two this is the old analog telephone old style fax machine modem or whatever you use to

**[13:07]** hook up to the analog phone line it can also be other Communications equipment that is handled by a ta ta that is

**[13:17]** terminal adapter this lets old te2 stuff talk to the isda network it also adapts

**[13:25]** other kinds of equipment like ethernet interfaces to ISDN nt1 that is Network

**[13:33]** termination type one this is the end of the line for the local phone company and the beginning of your house phone

**[13:42]** network nt2 that is Network termination type two

**[13:49]** in most homes this won't exist if you were a big company with your own private telephone system then this would be the

**[13:56]** guts of that telephone system LT that is line termination this is the physical

**[14:04]** connection of the telephone company ET exchange termination this is the local phone

**[14:12]** company's logical connection from your phones to the phone network letters r s

**[14:19]** Tu and V in the diagram are reference point that everyone uses to talk about

**[14:26]** each of these parts of the network the the r reference point is the interface between an old style telephone and

**[14:34]** terminal adapter equipment since most homes won't have any N2 equipment the s

**[14:41]** and t reference points are usually one and the same and are sometimes called St

**[14:48]** bus different things happen in the different parts of the network different wiring requirements different data

**[14:54]** speeds different encoding Etc the reference Point V and LT and ET

**[15:02]** equipment are in the phone company's domain ISDN provides for digital transmission over ordinary telephone

**[15:10]** copper wire as well as over other media uses asdn uses circuit switching to establish a physical permanent Point

**[15:19]** topoint connection from the source to the destination ISDN has standards defined by the itu that Encompass the

**[15:28]** OSI the bottom three layers of which are physical data link and network as shown

**[15:34]** in the diagram difference between ADSL and ISDN there are some obvious differences

**[15:41]** between the two Services ISDN lines provide two voice channels or one 128

**[15:49]** kbps data Channel whereas ADSL is only data line which is used for only data

**[15:56]** the part for ADSL is by a phone company through the medium of copper while which keeps the line stays alive and works

**[16:05]** even when local power fails whereas in ISDN lines power is required locally and does not work if

**[16:13]** the local power fails ISDN advantages the basic advantage of ISDN

**[16:20]** is to facilitate the user with multiple digital channels these channels can operate concurrently through the same one copper

**[16:29]** wire pair the digital signals broadcasting transversely the telephone lines ISDN

**[16:37]** provides High data rate because of digital scheme which is 56 kbps BR ISDN

**[16:44]** using a channel aggregation protocol such as bonding or multi-link triple P supports an uncompressed data transfer

**[16:53]** speed of 128 kbps plus bandwidth for overhead and signaling PR transfers at

**[17:01]** 17 minutes, 1 second an even higher speed of up to 1 1920 kbps ISDN allows multiple devices to

**[17:09]** share a single line it is possible to combine many different Digital Data sources and have the information rooted

**[17:17]** to the proper destination ISD and network lines are able to switch many fold devices on the

**[17:24]** single line such as faxes computers cash register credit card readers and many

**[17:30]** other devices these all devices can work together and directly be connected to the single

**[17:37]** line ISDN takes only 2 seconds to launch a connection while other modems take 30 to 60 second for

**[17:46]** establishment instead of the phone company sending a ring voltage signal to the ring the bell in your phone inband

**[17:55]** signal it sends a digital packet on a separate Channel that is out of band signal the outof band signal does not

**[18:03]** disturb established connections no bandwidth is taken from the data channels and call setup time is very

**[18:10]** fast as said earlier ISDN disadvantages there are some disadvantages associated with ISDN and

**[18:18]** they are as follows the disadvantage of ISDN lines is that it is very costly

**[18:25]** than the other typical telephone system ISDN line are more expensive when compared to the regular landline telephone

**[18:33]** system ISDN provider companies and ISDN users are required to have special dedicated line and then can Encore at

**[18:42]** extra cost ISDN requires specialized Digital Services just like telephone company so now we come to the security

**[18:51]** issues which is more secure ISDN cable modem DSL T1 Etc on the physic IAL

**[18:59]** medium part EES dropping on a phone land line where dialup modems are used as physically easier than spying on the

**[19:07]** more modern mediums because the lower data rate more easily accommodates homemade Electronics of questionable

**[19:15]** quality also some of the protocols used over various mediums include encryption which may hinder spying attempts on the

**[19:24]** physical line alth the marrow adding in deserted Courtyards during Moon moonless nights crouching under Services boxes to

**[19:32]** our tapping wires is a time honored spying tradition I believe that most attacks nowadays will be on a logical

**[19:39]** layer the attacker will try to hack into the ISP systems or the machines on the customer side be it a cable DSL modem or

**[19:50]** a not totally updated desktop systems and he will do so by sending IP packets from far away these are mostly

**[19:59]** orthogonal to the question of what medium is used logic attacks allow the attacker to try his luck on millions of

**[20:07]** targets from the comfort of his own basement instead of confronting rainy Gloom and ill-tempered cats on the

**[20:15]** random chance that the dozen or so homes that he will approach de night may contain something valuable

**[20:22]** electronically speaking and that no board Insomniac will spot him and call the police physical spying still exist

**[20:30]** but is mostly employed on the specific targets the attacker does not want to spy on anybody he is after you

**[20:38]** personally at which point you should have more pressing needs proofing a some home network against a dedicated

**[20:45]** attacker is hard think about Tempest or even about looking at your display and or keyboard over your shoulder from the

**[20:53]** outside through a window a good telescope a video camera with High FPS and you can record a typed password from

**[21:02]** about 200 M away so for the specifics of DSL T1 cable ISDN I would advise

**[21:11]** selecting the provider choose an ISP with a good repute about security issues in particular with regards to whatever

**[21:19]** modem he provides that's more important security wise than the physical medium

**[21:26]** and to abstract the whole question away never do sensitive stuff over the Internet unless you employ appropriate

**[21:33]** logical protection such as https so this was all about ISDN security thanks for watching this

**[21:41]** program thank you

**[21:44]** [Music]
