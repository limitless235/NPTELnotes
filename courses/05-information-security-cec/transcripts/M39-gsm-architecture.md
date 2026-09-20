# GSM Architecture

**Module 39**  
Duration: 28:47  
Video: https://www.youtube.com/watch?v=OdtB17eovb4

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Sunil Kumar, Department of Electrical and Computer Engineering, Punjab Agriculture University, Ludhiana

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:02]** [Music]

**[0:17]** Hello friends I welcome you all to the video lecture series of cyber security and information security in this lecture

**[0:26]** we will study about GSM system architecture first of all please see the contents which I shall

**[0:33]** cover after covering brief introduction about GSM I shall take up GSM system

**[0:39]** architecture in last I shall take up GSM services so now let us start global

**[0:46]** system for mobile communication that is gsm is a globally accepted standard for digital cellular

**[0:54]** communication digital seller networks are the segment of the market for mobile and wireless devices which are growing

**[1:02]** day to-day they are the wireless extensions of traditional pstn or ISDN networks and allow for seamless roaming

**[1:11]** with the same mobile phone Nation or even worldwide today these systems are mainly used for voice traffic however

**[1:20]** data traffic is continuously growing and there are several Technologies for wireless data transmission using

**[1:27]** Cellular Systems the most popular digital system is gsm with approximately 70% market share

**[1:36]** GSM is the most successful digital mobile telecommunication system in the world it is used by over 800 million

**[1:45]** people in more than 190 countries in the early 1980s Europe had numerous

**[1:51]** coexisting analog mobile phone systems which were often based on similar standards but ran on slightly different

**[2:00]** carrier frequencies to avoid the situation for a second generation fully digital system the group special Mobile

**[2:08]** GSM was founded in 1982 this system was soon named the global system for mobile Communications

**[2:17]** GSM with the specification process lying in the hands of European telecommunications Standard Institute

**[2:26]** etsi in the context of universal mobile telecommunication system UMTS and the creation of

**[2:35]** 3gpp third generation partnership project the whole development process of GSM was transferred to

**[2:42]** 3gpp and further development is combined with 3G development 3G PP assigned new

**[2:49]** numbers to all GSM standards the primary goal of GSM was to provide a mobile phone system that allows users to roam

**[2:58]** throughout Europe and provides voice Services compatible to ISDN and other

**[3:04]** pstn systems GSM is a typical second generation system replacing the first generation analog systems but not

**[3:13]** offering the high worldwide data rates that the third generation systems such as UMTS GSM has initially been deployed in

**[3:22]** Europe using 890 to 915 MHz for uplinks and 935 to 9 60 MHz for down LS now the

**[3:32]** system is also called gsm900 to distinguish it from the later versions these versions comprise GSM at

**[3:42]** 1800 MHz which is called DCs that is digital seller system 1800 and the GSM

**[3:50]** system mainly used in us at 1900 mahz which is called PCS that is personal

**[3:57]** Communications service 9 1900 GSM system architecture GSM comes with a hierarchal

**[4:05]** complex system architecture comprising many entities and interfaces a GSM system consists of three subsystems

**[4:15]** radio subsystem RSS Network and switching subsystem NSS and operation subsystem that is

**[4:24]** OSS each subsystem will be discussed in more detail in the following sections generally a GSM customer only notices a

**[4:33]** very small fraction of the whole network the mobile stations Ms and some antenna of Base transceiver stations that is

**[4:43]** BTS Radio subsystem the radio subsystem RSS comprises all radio specific entities

**[4:52]** that is the mobile stations and the base station subsystem GSM architecture pair in the

**[4:59]** figure shows the connection between the RSS and the NSS via the a interface that

**[5:07]** is solid lines and the connection to the OSS via the O interface these are the dash lines the a interface is typically

**[5:16]** based on circuit switched PCM 30 systems carrying up to 3064 kilobits per second connections

**[5:26]** whereas the O interface uses the signaling system number seven based on x.25 carrying management data to and

**[5:35]** from the radio subsystem base station subsystem that is BSS a GSM network comprises many BSS

**[5:46]** each controlled by a base station controller the BSS performs all functions necessary to maintain radio

**[5:54]** connections to an MS coding decoding of voice and rate adaptation to and from

**[6:01]** 6 minutes, 1 second the wireless network part the base station subsystem contains several base transceiver

**[6:10]** stations base transceiver station BTS a BTS comprises all radio equipment

**[6:18]** that is antennas signal processing amplifiers necessary for radio transmission a BTS can form a radio cell

**[6:27]** or using sectorized Ina and several cells are connected to Mobile station via the um interface and to the BSC

**[6:37]** while the abis interface the um interface contains all the mechanisms necessary for wireless

**[6:46]** transmission that is tdma fdma ETC a GSM cell can measor between some 100 m and

**[6:55]** 35 kilomet depending on the environment base station controller that is BSC the

**[7:04]** BSC basically manages the BTS it reserves radio frequencies

**[7:10]** handles the Handover from one BTS to another within the BSS and performs

**[7:17]** paging of the MS the BSC also multiplexes the radio channels onto the

**[7:23]** fixed network connections at the a interface Mobile station that is Ms

**[7:30]** mobile stations are most widely known cell or mobile phones are the section of a GSM cellular network that the user

**[7:39]** sees and operates in recent years their size has fallen dramatically while the level of functionality has greatly

**[7:48]** increased a further Advantage is that the time between charges has significantly increased there are number

**[7:56]** of elements to the cell phone although the two main elements are the main hardware and the Sim the hardware itself contains the

**[8:05]** main elements of the mobile phone including the display case battery and the electronics used to generate the

**[8:13]** signal and process the data receiver and to be transmitted it also contains a number

**[8:20]** known as the international mobile equipment identity that is IMI this is installed in the phone at

**[8:29]** Manu picture and cannot be changed it is accessed by the network during registration to check whether the

**[8:36]** equipment has been reported as stolen the Sim or subscriber identity module contains the information that

**[8:46]** provides the identity of the user to the network it contains a variety of information including a number known as

**[8:54]** the international mobile subscriber identity that is imsi this SIM card contains many identifiers

**[9:02]** and tables such as card type serial number a list of subscribed Services a personal identity number pin a pin

**[9:12]** unblocking key p and authentication key Ki and the international mobile

**[9:19]** subscriber identity that is imsi the PIN is used to unlock the MS

**[9:26]** using the wrong PIN three times will lock the Sim in such cases the p is

**[9:33]** needed to unlock the Sim the MS stores Dynamic information while logged onto the GSM system such as example the

**[9:42]** cipher key KC and the location information consisting of a temporary mobile subscriber identity that is tmsi

**[9:51]** and delocation area identification that is L AI typical Ms for GSM 9 00 have a

**[10:00]** transmit power of up to 2 wat whereas for GSM 1800 1 wat is enough due to the

**[10:09]** smaller Sal size apart from the telephone interface an MS can also offer other types of

**[10:16]** interfaces to users with display loudspeaker microphone and programmable soft keys further interfaces comprise

**[10:25]** computer modems or Bluetooth typical Ms example mobile phones

**[10:33]** comprise many more vendor specific functions and components such as cameras fingerprint sensors calendars address

**[10:42]** books games and internet browsers personal digital assistance PDA with mobile phone functions are also

**[10:51]** available the listeners should be aware that an MS could also be integrated into a car or be used for location tracking

**[10:59]** of a container Network and switching subsystem the heart of the GSM system is

**[11:06]** formed by the network and switching subsystem that is NSS the NSS connects the wireless

**[11:13]** network with standard public networks and performs handovers between different base station subsystems it comprises

**[11:22]** functions for worldwide localization of users and supports charging accounting and roaming of users between different

**[11:30]** providers in different countries the NSS consist of the following switches and databases mobile switching center that

**[11:39]** is MSC the main element within the core Network area of the overall gsm network architecture is the mobile switching

**[11:48]** center that is MSC the MSC acts like a normal switching node within a pstn or ISDN but also

**[11:57]** provides additional functionality to enable the requirements of a mobile user to be supported they set up connections

**[12:05]** to other msc's to and to bsc's Via the a interface and form the fixed backbone

**[12:13]** network of a GSM system an MSE manages several bsc's in a geographical region

**[12:21]** these include registration authentication call location inter MSC handovers and call routing to a mobile

**[12:31]** subscriber it also provides an interface to pstn so that calls can be rooted from the mobile network to a phone connected

**[12:39]** to a landline interfaces to other ms's are provided to enable calls to be made to Mobiles on different networks msse

**[12:49]** can also connect to public data networks PDN such as x.25 an MC handles all

**[12:57]** signaling needed for connection contion setup connection release and Handover of connections to other

**[13:04]** ms's home location register hlr the hlr is the most important

**[13:11]** database in a GSM system it stores all user relevant information this comprises

**[13:19]** static information such as the mobile subscriber ISDN number that is msisdn subscribe Services example call

**[13:28]** forwarding roaming restrictions GPRS and the international mobile subscriber identity that is imsi damic information

**[13:37]** is also needed example the current location area of the MS the mobile

**[13:44]** subscriber roaming number that is msrn the current vlr and MSC as soon as an MS leaves its current

**[13:53]** LA the information in the hlr is updated when a user switches on their phone the

**[14:00]** phone registers with the network and from this it is possible to determine which BTS it communicates with so that

**[14:08]** incoming calls can be rooted appropriately even when the phone is not active but switched on it re-registers

**[14:17]** periodically to ensure that the network hlr is aware of its latest position this information is necessary

**[14:26]** to localize a user in the world while G M Network all these user specific information elements only exist once for

**[14:35]** each user in a single hlr which also supports charging and

**[14:41]** accounting hlrs can manage data for several million customers and contain

**[14:48]** highly specialized databases which must fulfill certain realtime requirements to answer requests within certain time

**[14:56]** bounds there is one HL per Network although it may be distributed across

**[15:03]** various subcenters to for operational reasons visitor location register that

**[15:11]** is VR the vlr associated to each MSC is the dynamic database which stores all

**[15:19]** information needed for the MS users currently in the location area that is associated to the

**[15:27]** MSC example I MSI msisdn hlr address if a new Mobile station comes into a

**[15:36]** location area La the VR is responsible for this process and it copies all

**[15:43]** relevant information for this user from home location register this hierarchy of

**[15:49]** vlr and hlr avoids frequent hlr updates and long distance signaling of user

**[15:57]** information the vlr can be implemented as a separate entity but it is commonly realized as a integral part of the msse

**[16:06]** rather than a separate entity in this way exess is made faster and more convenient equipment identity register

**[16:16]** e the E is the entity that decides whether given mobile equipment may be allowed onto the network each mobile

**[16:25]** equipment has a number known as the international mobile equipment identity this number is installed in the

**[16:33]** equipment and is checked by the network during registration authentication Center Au

**[16:41]** the Au is a protected database that contains the secret key also contained in the users's SIM card it is used for

**[16:49]** authentication and for ciphering on the radio channel Gateway mobile switching Center

**[16:57]** gmsc the GM SC is the point to which a mobile equipment terminating call is initially rooted without any knowledge

**[17:06]** of the MS location the gmsc is thus in charge of obtaining the msrn that is

**[17:14]** Mobile station roaming number from the hlr based on the msisdn Mobile station ISDN number the

**[17:23]** directory number of a Mobile station and routing the call to correct visited

**[17:29]** mobile switching service center the MSC part of the term

**[17:35]** gmsc is misleading since the Gateway operation does not require any linking to an

**[17:43]** MSC SMS gateway smsg the smsg or SMS gateway is the term that is used to

**[17:52]** collectively describe the two short message Services gateways defined in the GSM standards the two gateways handle

**[18:00]** messages directed in different directions the SMS gmsc short message

**[18:07]** service Gateway mobile switching Center is for short messages being sent to a

**[18:12]** mobile equipment the SMS iwmc short message service interworking

**[18:21]** mobile switching Center is used for short messages originated with the mobile on that Network the SMS gmsc role

**[18:31]** is similar to that of gmsc whereas the SMS iwmc provides a fixed access point to

**[18:40]** the short message service center operation subsystem the third part of a GSM system the operational

**[18:50]** subsystem that is OSS contains the necessary functions for Network operation and

**[18:57]** maintenance the old SS processes its own network entities and accesses other

**[19:04]** entities via ss7 signaling the operation support subsystem is an element within the

**[19:11]** overall gsm network architecture that is connected to components of the NSS and the

**[19:17]** BSC it is used to control and monitor the overall gsm network and it is also used to control the traffic load of the

**[19:26]** BSS it must be noted that as the number of BS increases with the scaling of the subscriber population some of the

**[19:35]** maintenance tasks are transferred to the BTS which allowing Savings in the cost of ownership of the

**[19:43]** system the following entities have been defined operation and maintenance center that is OMC the OMC monitors and

**[19:53]** controls all other network entities via the O interface typical OMC management functions are traffic monitoring status

**[20:01]** 20 minutes, 1 second reports of network entities subscriber and Security Management or accounting

**[20:08]** and billing OMC has use the concept of telecommunication management Network that is tmn as standardized by the

**[20:16]** [Music]

**[20:18]** itu authentication center that is au as a radio interface and mobile stations are particularly vulnerable a separate

**[20:27]** Au has been defined defined to protect user identity and data transmission the Au contains the algorithms for

**[20:35]** authentication as well as the keys for encryption and generates the values needed for user authentication in the

**[20:43]** hlr the Au May in fact be situated in a special protected part of the

**[20:50]** hlr equipment identity register that is eir the eir is a database for all IM Eis

**[20:59]** that is it stores all device identifications registered for this network as Ms are mobile they can be

**[21:08]** easily stolen with the valid Sim anyone could use the stolen Ms the E has a

**[21:16]** blacklist of stolen or locked devices Unfortunately The Blacklist of different providers are not usually

**[21:24]** synchronized and the illegal use of a device in another operator network is possible the equipment identity register

**[21:33]** also contains a list of valid imis white list and a list of malfunctioning devices that is gy

**[21:41]** list GSM Services GSM offers much more than just voice telephony contact your

**[21:48]** local gsm network operator to the specific services that you can Avail GSM offers the three basic types of services

**[21:57]** telepone Serv services or T services data services or beer Services supplementary Services T services the

**[22:07]** abilities of a bearer service are used by a t service to transport data these services are further transited in the

**[22:15]** following ways voice calls the most basic T service supported by GSM is

**[22:22]** telon this includes full rate speech at 13 kbps and emergency calls where the

**[22:30]** nearest emergency service provider is notified by dialing three digits video text and F mile another group of T

**[22:38]** services include video text access tet text transmission F Smiley alternate

**[22:45]** speech and automatic F smiling group short text messages short messaging

**[22:52]** services SMS service is a text messaging service that allows sending and receiving text messages message on your

**[22:59]** GSM mobile phone in addition to simple text messages other text Data including

**[23:05]** News sports Financial language and location based data can also be transmitted Bearer

**[23:15]** Services data services or Bearer services are used through a GSM phone to receive and send data is the essential

**[23:22]** building block leading to widespread mobile internet access and mobile data transfer

**[23:29]** GSM currently has a data transfer rate of 9.6 kbps new development that will push up

**[23:36]** the data transfer rates for GSM users are hscsd that is highspeed circuit switch

**[23:44]** data and GPRS that is General packet Radio Service are now available supplementary Services

**[23:54]** supplementary services are additional services that are provided in in addition to T services and Bearer

**[24:01]** 24 minutes, 1 second Services these Services include caller identification call forwarding call waiting multi-party conversations and

**[24:10]** barring of international outgoing calls among others a brief description of supplementary Services is given here

**[24:20]** conferencing it allows a mobile subscriber to establish a multi-party conversation that is a simultaneous

**[24:27]** conversation between three or more subscriber to set up a conference call this service is only applicable to

**[24:35]** normal telephoning call waiting this service notifies a mobile

**[24:41]** subscriber of an incoming call during a conversation the subscriber can answer reject or ignore the incoming call call

**[24:51]** hold this service allows a subscriber to put an incoming call on hold and resume after a while the call hold service is

**[25:00]** applicable to normal telephony call forwarding call forwarding is used to

**[25:07]** divert calls from the original recipient to another number it is normally set up by the subscriber himself it can be used

**[25:16]** by the subscriber to divert calls from Mobile station when the subscriber is not available call

**[25:24]** baring call barring is useful to restrict certain types of outgoing calls such as ISD or stop incoming calls from

**[25:34]** undesired numbers call baring is a flexible service that enables the subscriber to conditionally bar

**[25:42]** calls number identification there are following supplementary Services related to number

**[25:48]** identification call line identification presentation this service displays the telephone number of the calling party on

**[25:56]** your screen calling line identification restriction a person not wishing their number to be

**[26:04]** presented to others subscribes to this service connected line identification

**[26:11]** presentation this service is provided to give the calling party the telephone number of the person to whom they are

**[26:19]** connected this service is useful in situations such as forwardings where the number connected is not number

**[26:27]** dialed connected line identification restriction there are times when the person called does not wish to have

**[26:34]** their number presented and so they would subscribe to this person normally this overrides the presentation

**[26:43]** service malicious call identification the malicious call identification service was provided to

**[26:51]** combat thead of obscene or annoying calls the victim should subscribe to

**[26:58]** this service and then they could cause unnown malicious calls to be identified

**[27:04]** in the gsm network using a simple command advice of charge

**[27:11]** AOC this service was designed to give the subscriber an indication of the cost of the services that they are used

**[27:20]** furthermore those service providers who wish to offer rental services to subscribers without their own Sim can

**[27:28]** also utilize this service in a slightly different form AOC for data calls is provided on the basis of time

**[27:37]** measurements closed user groups cugs this service is meant for groups of

**[27:44]** subscribers who wish to call only each other and no one else so friends this was all about GSM

**[27:52]** system architecture hope the concepts explained in this lecture were understandable and helpful hope to see

**[28:00]** you in the next lecture till then goodbye thank you

**[28:05]** [Music]
